# (C) Datadog, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

from ..config import is_affirmative

try:
    import khulnasoft_agent

    if khulnasoft_agent.get_config('integration_tracing'):
        from ddtrace import patch

        # handle thread monitoring as an additional option
        # See: http://pypi.khulnasoft.com/trace/docs/other_integrations.html#futures
        if khulnasoft_agent.get_config('integration_tracing_futures'):
            patch(logging=True, requests=True, futures=True)
        else:
            patch(logging=True, requests=True)

    if is_affirmative(khulnasoft_agent.get_config('integration_profiling')):
        from ddtrace.profiling import Profiler

        prof = Profiler(service='datadog-agent-integrations')
        prof.start()

except ImportError:
    # Tracing & profiling Integrations is only available with Agent 6
    pass
