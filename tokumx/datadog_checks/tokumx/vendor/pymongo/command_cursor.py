# Copyright 2014-2015 MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""CommandCursor class to iterate over command results."""

import datetime

from collections import deque

from khulnasoft_checks.tokumx.vendor.bson.py3compat import integer_types
from khulnasoft_checks.tokumx.vendor.pymongo import helpers
from khulnasoft_checks.tokumx.vendor.pymongo.errors import AutoReconnect, NotMasterError, OperationFailure
from khulnasoft_checks.tokumx.vendor.pymongo.message import _CursorAddress, _GetMore, _convert_exception


class CommandCursor(object):
    """A cursor / iterator over command cursors.
    """

    def __init__(self, collection, cursor_info, address, retrieved=0):
        """Create a new command cursor.
        """
        self.__collection = collection
        self.__id = cursor_info['id']
        self.__address = address
        self.__data = deque(cursor_info['firstBatch'])
        self.__retrieved = retrieved
        self.__batch_size = 0
        self.__killed = (self.__id == 0)

        if "ns" in cursor_info:
            self.__ns = cursor_info["ns"]
        else:
            self.__ns = collection.full_name

    def __del__(self):
        if self.__id and not self.__killed:
            self.__die()

    def __die(self, synchronous=False):
        """Closes this cursor.
        """
        if self.__id and not self.__killed:
            address = _CursorAddress(
                self.__address, self.__collection.full_name)
            if synchronous:
                self.__collection.database.client._close_cursor_now(
                    self.__id, address)
            else:
                self.__collection.database.client.close_cursor(
                    self.__id, address)
        self.__killed = True

    def close(self):
        """Explicitly close / kill this cursor.
        """
        self.__die(True)

    def batch_size(self, batch_size):
        """Limits the number of documents returned in one batch. Each batch
        requires a round trip to the server. It can be adjusted to optimize
        performance and limit data transfer.

        .. note:: batch_size can not override MongoDB's internal limits on the
           amount of data it will return to the client in a single batch (i.e
           if you set batch size to 1,000,000,000, MongoDB will currently only
           return 4-16MB of results per batch).

        Raises :exc:`TypeError` if `batch_size` is not an integer.
        Raises :exc:`ValueError` if `batch_size` is less than ``0``.

        :Parameters:
          - `batch_size`: The size of each batch of results requested.
        """
        if not isinstance(batch_size, integer_types):
            raise TypeError("batch_size must be an integer")
        if batch_size < 0:
            raise ValueError("batch_size must be >= 0")

        self.__batch_size = batch_size == 1 and 2 or batch_size
        return self

    def __send_message(self, operation):
        """Send a getmore message and handle the response.
        """
        client = self.__collection.database.client
        listeners = client._event_listeners
        publish = listeners.enabled_for_commands
        try:
            response = client._send_message_with_response(
                operation, address=self.__address)
        except AutoReconnect:
            # Don't try to send kill cursors on another socket
            # or to another server. It can cause a _pinValue
            # assertion on some server releases if we get here
            # due to a socket timeout.
            self.__killed = True
            raise

        cmd_duration = response.duration
        rqst_id = response.request_id
        from_command = response.from_command

        if publish:
            start = datetime.datetime.now()
        try:
            doc = helpers._unpack_response(response.data,
                                           self.__id,
                                           self.__collection.codec_options)
            if from_command:
                helpers._check_command_response(doc['data'][0])

        except OperationFailure as exc:
            self.__killed = True

            if publish:
                duration = (datetime.datetime.now() - start) + cmd_duration
                listeners.publish_command_failure(
                    duration, exc.details, "getMore", rqst_id, self.__address)

            raise
        except NotMasterError as exc:
            # Don't send kill cursors to another server after a "not master"
            # error. It's completely pointless.
            self.__killed = True

            if publish:
                duration = (datetime.datetime.now() - start) + cmd_duration
                listeners.publish_command_failure(
                    duration, exc.details, "getMore", rqst_id, self.__address)

            client._reset_server_and_request_check(self.address)
            raise
        except Exception as exc:
            if publish:
                duration = (datetime.datetime.now() - start) + cmd_duration
                listeners.publish_command_failure(
                    duration, _convert_exception(exc), "getMore", rqst_id,
                    self.__address)
            raise

        if from_command:
            cursor = doc['data'][0]['cursor']
            documents = cursor['nextBatch']
            self.__id = cursor['id']
            self.__retrieved += len(documents)
        else:
            documents = doc["data"]
            self.__id = doc["cursor_id"]
            self.__retrieved += doc["number_returned"]

        if publish:
            duration = (datetime.datetime.now() - start) + cmd_duration
            # Must publish in getMore command response format.
            res = {"cursor": {"id": self.__id,
                              "ns": self.__collection.full_name,
                              "nextBatch": documents},
                   "ok": 1}
            listeners.publish_command_success(
                duration, res, "getMore", rqst_id, self.__address)

        if self.__id == 0:
            self.__killed = True
        self.__data = deque(documents)


    def _refresh(self):
        """Refreshes the cursor with more data from the server.

        Returns the length of self.__data after refresh. Will exit early if
        self.__data is already non-empty. Raises OperationFailure when the
        cursor cannot be refreshed due to an error on the query.
        """
        if len(self.__data) or self.__killed:
            return len(self.__data)

        if self.__id:  # Get More
            dbname, collname = self.__ns.split('.', 1)
            self.__send_message(
                _GetMore(dbname,
                         collname,
                         self.__batch_size,
                         self.__id,
                         self.__collection.codec_options))

        else:  # Cursor id is zero nothing else to return
            self.__killed = True

        return len(self.__data)

    @property
    def alive(self):
        """Does this cursor have the potential to return more data?

        Even if :attr:`alive` is ``True``, :meth:`next` can raise
        :exc:`StopIteration`. Best to use a for loop::

            for doc in collection.aggregate(pipeline):
                print(doc)

        .. note:: :attr:`alive` can be True while iterating a cursor from
          a failed server. In this case :attr:`alive` will return False after
          :meth:`next` fails to retrieve the next batch of results from the
          server.
        """
        return bool(len(self.__data) or (not self.__killed))

    @property
    def cursor_id(self):
        """Returns the id of the cursor."""
        return self.__id

    @property
    def address(self):
        """The (host, port) of the server used, or None.

        .. versionadded:: 3.0
        """
        return self.__address

    def __iter__(self):
        return self

    def next(self):
        """Advance the cursor."""
        if len(self.__data) or self._refresh():
            coll = self.__collection
            return coll.database._fix_outgoing(self.__data.popleft(), coll)
        else:
            raise StopIteration

    __next__ = next

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
