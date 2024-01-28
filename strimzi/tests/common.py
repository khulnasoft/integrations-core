# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

from khulnasoft_checks.dev import get_here

STRIMZI_VERSION = os.environ["STRIMZI_VERSION"]
HERE = get_here()

MOCKED_CLUSTER_OPERATOR_INSTANCE = {'cluster_operator_endpoint': 'http://cluster-operator:8080/metrics'}

MOCKED_TOPIC_OPERATOR_INSTANCE = {'topic_operator_endpoint': 'http://entity-operator:8080/metrics'}

MOCKED_USER_OPERATOR_INSTANCE = {'user_operator_endpoint': 'http://entity-operator:8081/metrics'}

MOCKED_CLUSTER_OPERATOR_TAG = f'endpoint:{MOCKED_CLUSTER_OPERATOR_INSTANCE["cluster_operator_endpoint"]}'

MOCKED_TOPIC_OPERATOR_TAG = f'endpoint:{MOCKED_TOPIC_OPERATOR_INSTANCE["topic_operator_endpoint"]}'

MOCKED_USER_OPERATOR_TAG = f'endpoint:{MOCKED_USER_OPERATOR_INSTANCE["user_operator_endpoint"]}'

CLUSTER_OPERATOR_METRICS = (
    "strimzi.cluster_operator.jvm.buffer.count_buffers",
    "strimzi.cluster_operator.jvm.buffer.memory_used_bytes",
    "strimzi.cluster_operator.jvm.buffer.total_capacity_bytes",
    "strimzi.cluster_operator.jvm.classes.loaded_classes",
    "strimzi.cluster_operator.jvm.classes.unloaded_classes.count",
    "strimzi.cluster_operator.jvm.gc.live_data_size_bytes",
    "strimzi.cluster_operator.jvm.gc.max_data_size_bytes",
    "strimzi.cluster_operator.jvm.gc.memory_allocated_bytes.count",
    "strimzi.cluster_operator.jvm.gc.memory_promoted_bytes.count",
    "strimzi.cluster_operator.jvm.gc.pause_seconds.count",
    "strimzi.cluster_operator.jvm.gc.pause_seconds.max",
    "strimzi.cluster_operator.jvm.gc.pause_seconds.sum",
    "strimzi.cluster_operator.jvm.memory.committed_bytes",
    "strimzi.cluster_operator.jvm.memory.max_bytes",
    "strimzi.cluster_operator.jvm.memory.used_bytes",
    "strimzi.cluster_operator.jvm.threads.daemon_threads",
    "strimzi.cluster_operator.jvm.threads.live_threads",
    "strimzi.cluster_operator.jvm.threads.peak_threads",
    "strimzi.cluster_operator.jvm.threads.states_threads",
    "strimzi.cluster_operator.process.cpu_usage",
    "strimzi.cluster_operator.reconciliations.already_enqueued.count",
    "strimzi.cluster_operator.reconciliations.count",
    "strimzi.cluster_operator.reconciliations.duration_seconds.bucket",
    "strimzi.cluster_operator.reconciliations.duration_seconds.count",
    "strimzi.cluster_operator.reconciliations.duration_seconds.max",
    "strimzi.cluster_operator.reconciliations.duration_seconds.sum",
    "strimzi.cluster_operator.reconciliations.locked.count",
    "strimzi.cluster_operator.reconciliations.periodical.count",
    "strimzi.cluster_operator.reconciliations.successful.count",
    "strimzi.cluster_operator.resource.state",
    "strimzi.cluster_operator.resources",
    "strimzi.cluster_operator.resources.paused",
    "strimzi.cluster_operator.system.cpu_count",
    "strimzi.cluster_operator.system.cpu_usage",
    "strimzi.cluster_operator.system.load_average_1m",
    "strimzi.cluster_operator.vertx.http_client.active_connections",
    "strimzi.cluster_operator.vertx.http_client.active_requests",
    "strimzi.cluster_operator.vertx.http_client.bytes_read.count",
    "strimzi.cluster_operator.vertx.http_client.bytes_written.count",
    "strimzi.cluster_operator.vertx.http_client.queue_pending",
    "strimzi.cluster_operator.vertx.http_client.queue_time_seconds.count",
    "strimzi.cluster_operator.vertx.http_client.queue_time_seconds.max",
    "strimzi.cluster_operator.vertx.http_client.queue_time_seconds.sum",
    "strimzi.cluster_operator.vertx.http_client.request_bytes.count",
    "strimzi.cluster_operator.vertx.http_client.request_bytes.max",
    "strimzi.cluster_operator.vertx.http_client.request_bytes.sum",
    "strimzi.cluster_operator.vertx.http_client.requests.count",
    "strimzi.cluster_operator.vertx.http_client.response_bytes.count",
    "strimzi.cluster_operator.vertx.http_client.response_bytes.max",
    "strimzi.cluster_operator.vertx.http_client.response_bytes.sum",
    "strimzi.cluster_operator.vertx.http_client.response_time_seconds.count",
    "strimzi.cluster_operator.vertx.http_client.response_time_seconds.max",
    "strimzi.cluster_operator.vertx.http_client.response_time_seconds.sum",
    "strimzi.cluster_operator.vertx.http_client.responses.count",
    "strimzi.cluster_operator.vertx.http_server.active_connections",
    "strimzi.cluster_operator.vertx.http_server.active_requests",
    "strimzi.cluster_operator.vertx.http_server.bytes_written.count",
    "strimzi.cluster_operator.vertx.http_server.errors.count",
    "strimzi.cluster_operator.vertx.http_server.request_bytes.count",
    "strimzi.cluster_operator.vertx.http_server.request_bytes.max",
    "strimzi.cluster_operator.vertx.http_server.request_bytes.sum",
    "strimzi.cluster_operator.vertx.http_server.request_resets.count",
    "strimzi.cluster_operator.vertx.http_server.requests.count",
    "strimzi.cluster_operator.vertx.http_server.response_bytes.count",
    "strimzi.cluster_operator.vertx.http_server.response_bytes.max",
    "strimzi.cluster_operator.vertx.http_server.response_bytes.sum",
    "strimzi.cluster_operator.vertx.http_server.response_time_seconds.count",
    "strimzi.cluster_operator.vertx.http_server.response_time_seconds.max",
    "strimzi.cluster_operator.vertx.http_server.response_time_seconds.sum",
    "strimzi.cluster_operator.vertx.pool.completed.count",
    "strimzi.cluster_operator.vertx.pool.in_use",
    "strimzi.cluster_operator.vertx.pool.queue_pending",
    "strimzi.cluster_operator.vertx.pool.queue_time_seconds.count",
    "strimzi.cluster_operator.vertx.pool.queue_time_seconds.max",
    "strimzi.cluster_operator.vertx.pool.queue_time_seconds.sum",
    "strimzi.cluster_operator.vertx.pool.ratio",
    "strimzi.cluster_operator.vertx.pool.usage_seconds.count",
    "strimzi.cluster_operator.vertx.pool.usage_seconds.max",
    "strimzi.cluster_operator.vertx.pool.usage_seconds.sum",
)

TOPIC_OPERATOR_METRICS = (
    "strimzi.topic_operator.jvm.gc.memory_promoted_bytes.count",
    "strimzi.topic_operator.jvm.buffer.count_buffers",
    "strimzi.topic_operator.jvm.buffer.memory_used_bytes",
    "strimzi.topic_operator.jvm.buffer.total_capacity_bytes",
    "strimzi.topic_operator.jvm.classes.loaded_classes",
    "strimzi.topic_operator.jvm.classes.unloaded_classes.count",
    "strimzi.topic_operator.jvm.gc.live_data_size_bytes",
    "strimzi.topic_operator.jvm.gc.max_data_size_bytes",
    "strimzi.topic_operator.jvm.gc.memory_allocated_bytes.count",
    "strimzi.topic_operator.jvm.gc.pause_seconds.count",
    "strimzi.topic_operator.jvm.gc.pause_seconds.max",
    "strimzi.topic_operator.jvm.gc.pause_seconds.sum",
    "strimzi.topic_operator.jvm.memory.committed_bytes",
    "strimzi.topic_operator.jvm.memory.max_bytes",
    "strimzi.topic_operator.jvm.memory.used_bytes",
    "strimzi.topic_operator.jvm.threads.daemon_threads",
    "strimzi.topic_operator.jvm.threads.live_threads",
    "strimzi.topic_operator.jvm.threads.peak_threads",
    "strimzi.topic_operator.jvm.threads.states_threads",
    "strimzi.topic_operator.process.cpu_usage",
    "strimzi.topic_operator.reconciliations.count",
    "strimzi.topic_operator.reconciliations.duration_seconds.bucket",
    "strimzi.topic_operator.reconciliations.duration_seconds.count",
    "strimzi.topic_operator.reconciliations.duration_seconds.max",
    "strimzi.topic_operator.reconciliations.duration_seconds.sum",
    "strimzi.topic_operator.reconciliations.failed.count",
    "strimzi.topic_operator.reconciliations.locked.count",
    "strimzi.topic_operator.reconciliations.periodical.count",
    "strimzi.topic_operator.reconciliations.successful.count",
    "strimzi.topic_operator.resources.paused",
    "strimzi.topic_operator.resource.state",
    "strimzi.topic_operator.resources",
    "strimzi.topic_operator.system.cpu_count",
    "strimzi.topic_operator.system.cpu_usage",
    "strimzi.topic_operator.system.load_average_1m",
    "strimzi.topic_operator.vertx.http_server.active_connections",
    "strimzi.topic_operator.vertx.http_server.active_requests",
    "strimzi.topic_operator.vertx.http_server.bytes_written.count",
    "strimzi.topic_operator.vertx.http_server.errors.count",
    "strimzi.topic_operator.vertx.http_server.request_bytes.count",
    "strimzi.topic_operator.vertx.http_server.request_bytes.max",
    "strimzi.topic_operator.vertx.http_server.request_bytes.sum",
    "strimzi.topic_operator.vertx.http_server.requests.count",
    "strimzi.topic_operator.vertx.http_server.response_bytes.count",
    "strimzi.topic_operator.vertx.http_server.response_bytes.max",
    "strimzi.topic_operator.vertx.http_server.response_bytes.sum",
    "strimzi.topic_operator.vertx.http_server.response_time_seconds.count",
    "strimzi.topic_operator.vertx.http_server.response_time_seconds.max",
    "strimzi.topic_operator.vertx.http_server.response_time_seconds.sum",
    "strimzi.topic_operator.vertx.pool.completed.count",
    "strimzi.topic_operator.vertx.pool.in_use",
    "strimzi.topic_operator.vertx.pool.queue_pending",
    "strimzi.topic_operator.vertx.pool.queue_time_seconds.count",
    "strimzi.topic_operator.vertx.pool.queue_time_seconds.max",
    "strimzi.topic_operator.vertx.pool.queue_time_seconds.sum",
    "strimzi.topic_operator.vertx.pool.ratio",
    "strimzi.topic_operator.vertx.pool.usage_seconds.count",
    "strimzi.topic_operator.vertx.pool.usage_seconds.max",
    "strimzi.topic_operator.vertx.pool.usage_seconds.sum",
)

USER_OPERATOR_METRICS = (
    "strimzi.user_operator.jvm.buffer.count_buffers",
    "strimzi.user_operator.jvm.buffer.memory_used_bytes",
    "strimzi.user_operator.jvm.buffer.total_capacity_bytes",
    "strimzi.user_operator.jvm.classes.loaded_classes",
    "strimzi.user_operator.jvm.classes.unloaded_classes.count",
    "strimzi.user_operator.jvm.gc.live_data_size_bytes",
    "strimzi.user_operator.jvm.gc.max_data_size_bytes",
    "strimzi.user_operator.jvm.gc.memory_allocated_bytes.count",
    "strimzi.user_operator.jvm.gc.memory_promoted_bytes.count",
    "strimzi.user_operator.jvm.gc.pause_seconds.count",
    "strimzi.user_operator.jvm.gc.pause_seconds.max",
    "strimzi.user_operator.jvm.gc.pause_seconds.sum",
    "strimzi.user_operator.jvm.memory.committed_bytes",
    "strimzi.user_operator.jvm.memory.max_bytes",
    "strimzi.user_operator.jvm.memory.used_bytes",
    "strimzi.user_operator.jvm.threads.daemon_threads",
    "strimzi.user_operator.jvm.threads.live_threads",
    "strimzi.user_operator.jvm.threads.peak_threads",
    "strimzi.user_operator.jvm.threads.states_threads",
    "strimzi.user_operator.process.cpu_usage",
    "strimzi.user_operator.reconciliations.count",
    "strimzi.user_operator.reconciliations.duration_seconds.bucket",
    "strimzi.user_operator.reconciliations.duration_seconds.count",
    "strimzi.user_operator.reconciliations.duration_seconds.max",
    "strimzi.user_operator.reconciliations.duration_seconds.sum",
    "strimzi.user_operator.reconciliations.failed.count",
    "strimzi.user_operator.reconciliations.locked.count",
    "strimzi.user_operator.reconciliations.periodical.count",
    "strimzi.user_operator.reconciliations.successful.count",
    "strimzi.user_operator.resources",
    "strimzi.user_operator.system.cpu_count",
    "strimzi.user_operator.system.cpu_usage",
    "strimzi.user_operator.system.load_average_1m",
)

FLAKY_E2E_METRICS = (
    "strimzi.cluster_operator.reconciliations.periodical.count",
    "strimzi.cluster_operator.resources.paused",
    "strimzi.cluster_operator.vertx.http_client.active_connections",
    "strimzi.cluster_operator.vertx.http_client.active_requests",
    "strimzi.cluster_operator.vertx.http_client.bytes_read.count",
    "strimzi.cluster_operator.vertx.http_client.bytes_written.count",
    "strimzi.cluster_operator.vertx.http_client.queue_pending",
    "strimzi.cluster_operator.vertx.http_client.queue_time_seconds.count",
    "strimzi.cluster_operator.vertx.http_client.queue_time_seconds.max",
    "strimzi.cluster_operator.vertx.http_client.queue_time_seconds.sum",
    "strimzi.cluster_operator.vertx.http_client.request_bytes.count",
    "strimzi.cluster_operator.vertx.http_client.request_bytes.max",
    "strimzi.cluster_operator.vertx.http_client.request_bytes.sum",
    "strimzi.cluster_operator.vertx.http_client.requests.count",
    "strimzi.cluster_operator.vertx.http_client.response_bytes.count",
    "strimzi.cluster_operator.vertx.http_client.response_bytes.max",
    "strimzi.cluster_operator.vertx.http_client.response_bytes.sum",
    "strimzi.cluster_operator.vertx.http_client.response_time_seconds.count",
    "strimzi.cluster_operator.vertx.http_client.response_time_seconds.max",
    "strimzi.cluster_operator.vertx.http_client.response_time_seconds.sum",
    "strimzi.cluster_operator.vertx.http_client.responses.count",
    "strimzi.cluster_operator.vertx.http_server.errors.count",
    "strimzi.cluster_operator.vertx.http_server.request_resets.count",
    "strimzi.topic_operator.vertx.http_server.errors.count",
    "strimzi.user_operator.reconciliations.locked.count",
    "strimzi.user_operator.reconciliations.periodical.count",
    "strimzi.user_operator.reconciliations.successful.count",
)
