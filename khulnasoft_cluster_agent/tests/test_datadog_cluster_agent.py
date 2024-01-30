# (C) Khulnasoft, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from typing import Any, Dict  # noqa: F401

import pytest

from khulnasoft_checks.base import AgentCheck
from khulnasoft_checks.base.stubs.aggregator import AggregatorStub  # noqa: F401
from khulnasoft_checks.khulnasoft_cluster_agent import KhulnasoftClusterAgentCheck
from khulnasoft_checks.dev.utils import get_metadata_metrics

NAMESPACE = 'khulnasoft.cluster_agent'

METRICS = [
    'admission_webhooks.certificate_expiry',
    'admission_webhooks.library_injection_attempts',
    'admission_webhooks.library_injection_errors',
    'admission_webhooks.mutation_attempts',
    'admission_webhooks.mutation_errors',
    'admission_webhooks.patcher.attempts',
    'admission_webhooks.patcher.completed',
    'admission_webhooks.patcher.errors',
    'admission_webhooks.rc_provider.configs',
    'admission_webhooks.rc_provider.invalid_configs',
    'admission_webhooks.reconcile_errors',
    'admission_webhooks.reconcile_success',
    'admission_webhooks.response_duration.count',
    'admission_webhooks.response_duration.sum',
    'admission_webhooks.webhooks_received',
    'aggregator.flush',
    'aggregator.processed',
    'api_requests',
    'autodiscovery.errors',
    'autodiscovery.poll_duration.count',
    'autodiscovery.poll_duration.sum',
    'autodiscovery.watched_resources',
    'cluster_checks.busyness',
    'cluster_checks.configs_dangling',
    'cluster_checks.configs_dispatched',
    'cluster_checks.configs_info',
    'cluster_checks.failed_stats_collection',
    'cluster_checks.nodes_reporting',
    'cluster_checks.rebalancing_decisions',
    'cluster_checks.rebalancing_duration_seconds',
    'cluster_checks.successful_rebalancing_moves',
    'cluster_checks.updating_stats_duration_seconds',
    'khulnasoft.rate_limit_queries.limit',
    'khulnasoft.rate_limit_queries.period',
    'khulnasoft.rate_limit_queries.remaining',
    'khulnasoft.rate_limit_queries.remaining_min',
    'khulnasoft.rate_limit_queries.reset',
    'khulnasoft.requests',
    'endpoint_checks.configs_dispatched',
    'external_metrics',
    'external_metrics.api_elapsed.count',
    'external_metrics.api_elapsed.sum',
    'external_metrics.api_requests',
    'external_metrics.khulnasoft_metrics',
    'external_metrics.delay_seconds',
    'external_metrics.processed_value',
    'go.goroutines',
    'go.memstats.alloc_bytes',
    'go.threads',
    'kubernetes_apiserver.emitted_events',
    'kubernetes_apiserver.kube_events',
    'secret_backend.elapsed',
]


def test_check(aggregator, instance, mock_metrics_endpoint):
    # type: (AggregatorStub, Dict[str, Any]) -> None
    check = KhulnasoftClusterAgentCheck('khulnasoft_cluster_agent', {}, [instance])

    # dry run to build mapping for label joins
    check.check(instance)

    check.check(instance)

    for metric in METRICS:
        aggregator.assert_metric(NAMESPACE + '.' + metric)
        aggregator.assert_metric_has_tag_prefix(NAMESPACE + '.' + metric, 'is_leader:')

    aggregator.assert_all_metrics_covered()
    aggregator.assert_metrics_using_metadata(get_metadata_metrics())


# Minimal E2E testing
@pytest.mark.e2e
def test_e2e(dd_agent_check, aggregator, instance):
    with pytest.raises(Exception):
        dd_agent_check(instance, rate=True)
    tag = "endpoint:" + instance.get('prometheus_url')
    aggregator.assert_service_check("khulnasoft.cluster_agent.prometheus.health", AgentCheck.CRITICAL, count=2, tags=[tag])
