# (C) Khulnasoft, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from khulnasoft_checks.base import OpenMetricsBaseCheck

DEFAULT_METRICS = {
    'admission_webhooks_certificate_expiry': 'admission_webhooks.certificate_expiry',
    'admission_webhooks_library_injection_attempts': 'admission_webhooks.library_injection_attempts',
    'admission_webhooks_library_injection_errors': 'admission_webhooks.library_injection_errors',
    'admission_webhooks_mutation_attempts': 'admission_webhooks.mutation_attempts',
    'admission_webhooks_mutation_errors': 'admission_webhooks.mutation_errors',
    'admission_webhooks_patcher_attempts': 'admission_webhooks.patcher.attempts',
    'admission_webhooks_patcher_completed': 'admission_webhooks.patcher.completed',
    'admission_webhooks_patcher_errors': 'admission_webhooks.patcher.errors',
    'admission_webhooks_rc_provider_configs': 'admission_webhooks.rc_provider.configs',
    'admission_webhooks_rc_provider_configs_invalid': 'admission_webhooks.rc_provider.invalid_configs',
    'admission_webhooks_reconcile_errors': 'admission_webhooks.reconcile_errors',
    'admission_webhooks_reconcile_success': 'admission_webhooks.reconcile_success',
    'admission_webhooks_response_duration': 'admission_webhooks.response_duration',
    'admission_webhooks_webhooks_received': 'admission_webhooks.webhooks_received',
    'aggregator__flush': 'aggregator.flush',
    'aggregator__processed': 'aggregator.processed',
    'api_requests': 'api_requests',
    'autodiscovery_errors': 'autodiscovery.errors',
    'autodiscovery_poll_duration': 'autodiscovery.poll_duration',
    'autodiscovery_watched_resources': 'autodiscovery.watched_resources',
    'cluster_checks_busyness': 'cluster_checks.busyness',
    'cluster_checks_configs_dangling': 'cluster_checks.configs_dangling',
    'cluster_checks_configs_dispatched': 'cluster_checks.configs_dispatched',
    'cluster_checks_configs_info': 'cluster_checks.configs_info',
    'cluster_checks_failed_stats_collection': 'cluster_checks.failed_stats_collection',
    'cluster_checks_nodes_reporting': 'cluster_checks.nodes_reporting',
    'cluster_checks_rebalancing_decisions': 'cluster_checks.rebalancing_decisions',
    'cluster_checks_rebalancing_duration_seconds': 'cluster_checks.rebalancing_duration_seconds',
    'cluster_checks_successful_rebalancing_moves': 'cluster_checks.successful_rebalancing_moves',
    'cluster_checks_updating_stats_duration_seconds': 'cluster_checks.updating_stats_duration_seconds',
    'khulnasoft_requests': 'khulnasoft.requests',
    'endpoint_checks_configs_dispatched': 'endpoint_checks.configs_dispatched',
    'external_metrics': 'external_metrics',
    'external_metrics_api_elapsed': 'external_metrics.api_elapsed',
    'external_metrics_api_requests': 'external_metrics.api_requests',
    'external_metrics_khulnasoft_metrics': 'external_metrics.khulnasoft_metrics',
    'external_metrics_delay_seconds': 'external_metrics.delay_seconds',
    'external_metrics_processed_value': 'external_metrics.processed_value',
    'go_goroutines': 'go.goroutines',
    'go_memstats_alloc_bytes': 'go.memstats.alloc_bytes',
    'go_threads': 'go.threads',
    'kubernetes_apiserver_emitted_events': 'kubernetes_apiserver.emitted_events',
    'kubernetes_apiserver_kube_events': 'kubernetes_apiserver.kube_events',
    'rate_limit_queries_limit': 'khulnasoft.rate_limit_queries.limit',
    'rate_limit_queries_period': 'khulnasoft.rate_limit_queries.period',
    'rate_limit_queries_remaining': 'khulnasoft.rate_limit_queries.remaining',
    'rate_limit_queries_remaining_min': 'khulnasoft.rate_limit_queries.remaining_min',
    'rate_limit_queries_reset': 'khulnasoft.rate_limit_queries.reset',
    'secret_backend__elapsed_ms': 'secret_backend.elapsed',
}


class KhulnasoftClusterAgentCheck(OpenMetricsBaseCheck):
    DEFAULT_METRIC_LIMIT = 0

    def __init__(self, name, init_config, instances):
        super(KhulnasoftClusterAgentCheck, self).__init__(
            name,
            init_config,
            instances,
            default_instances={
                'khulnasoft.cluster_agent': {
                    'prometheus_url': 'http://localhost:5000/metrics',
                    'namespace': 'khulnasoft.cluster_agent',
                    'metrics': [DEFAULT_METRICS],
                    'label_joins': {
                        'leader_election_is_leader': {
                            'labels_to_match': ['*'],
                            'labels_to_get': ['is_leader'],
                        }
                    },
                    'send_histograms_buckets': True,
                    'send_distribution_counts_as_monotonic': True,
                    'send_distribution_sums_as_monotonic': True,
                }
            },
            default_namespace='khulnasoft.cluster_agent',
        )
