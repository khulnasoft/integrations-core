# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

CHECK_NAME = "presto"

METRICS = [
    "presto.execution.cpu_input_byte_rate.one_minute.avg",
    "presto.execution.cpu_input_byte_rate.all_time.avg",
    "presto.execution.execution_time.all_time.avg",
    "presto.execution.execution_time.all_time.max",
    "presto.execution.execution_time.all_time.min",
    "presto.execution.execution_time.all_time.p75",
    "presto.execution.execution_time.all_time.p95",
    "presto.execution.execution_time.one_minute.avg",
    "presto.execution.execution_time.one_minute.max",
    "presto.execution.execution_time.one_minute.min",
    "presto.execution.execution_time.one_minute.p75",
    "presto.execution.execution_time.one_minute.p95",
    "presto.execution.wall_input_bytes_rate.one_minute.avg",
    "presto.execution.abandoned_queries.one_minute.count",
    "presto.execution.abandoned_queries.one_minute.rate",
    "presto.execution.abandoned_queries.total_count",
    "presto.execution.canceled_queries.one_minute.count",
    "presto.execution.canceled_queries.one_minute.rate",
    "presto.execution.canceled_queries.total_count",
    "presto.execution.completed_queries.one_minute.count",
    "presto.execution.completed_queries.one_minute.rate",
    "presto.execution.completed_queries.total_count",
    "presto.execution.consumed_cpu_time_secs.one_minute.count",
    "presto.execution.consumed_cpu_time_secs.one_minute.rate",
    "presto.execution.consumed_cpu_time_secs.total_count",
    "presto.execution.cpu_input_byte_rate.all_time.p75",
    "presto.execution.cpu_input_byte_rate.all_time.p95",
    "presto.execution.cpu_input_byte_rate.one_minute.count",
    "presto.execution.cpu_input_byte_rate.one_minute.max",
    "presto.execution.cpu_input_byte_rate.one_minute.min",
    "presto.execution.cpu_input_byte_rate.one_minute.p75",
    "presto.execution.cpu_input_byte_rate.one_minute.p95",
    "presto.execution.cpu_input_byte_rate.one_minute.total",
    "presto.execution.execution_time.all_time.count",
    "presto.execution.executor.blocked_splits",
    "presto.execution.executor.processor_executor.queued_task_count",
    "presto.execution.executor.running_splits",
    "presto.execution.executor.total_splits",
    "presto.execution.executor.waiting_splits",
    "presto.execution.external_failures.one_minute.count",
    "presto.execution.external_failures.one_minute.rate",
    "presto.execution.external_failures.total_count",
    "presto.execution.failed_queries.one_minute.count",
    "presto.execution.failed_queries.one_minute.rate",
    "presto.execution.failed_queries.total_count",
    "presto.execution.input_data_size.one_minute.count",
    "presto.execution.input_data_size.one_minute.rate",
    "presto.execution.input_data_size.total_count",
    "presto.execution.input_positions.one_minute.count",
    "presto.execution.input_positions.one_minute.rate",
    "presto.execution.input_positions.total_count",
    "presto.execution.insufficient_resources_failures.one_minute.count",
    "presto.execution.insufficient_resources_failures.one_minute.rate",
    "presto.execution.insufficient_resources_failures.total_count",
    "presto.execution.internal_failures.one_minute.count",
    "presto.execution.internal_failures.one_minute.rate",
    "presto.execution.internal_failures.total_count",
    "presto.execution.output_data_size.one_minute.count",
    "presto.execution.output_data_size.one_minute.rate",
    "presto.execution.output_data_size.total_count",
    "presto.execution.output_positions.one_minute.count",
    "presto.execution.output_positions.one_minute.rate",
    "presto.execution.output_positions.total_count",
    "presto.execution.running_queries",
    "presto.execution.started_queries.one_minute.count",
    "presto.execution.started_queries.one_minute.rate",
    "presto.execution.started_queries.total_count",
    "presto.execution.task_notification_executor.active_count",
    "presto.execution.task_notification_executor.completed_task_count",
    "presto.execution.task_notification_executor.pool_size",
    "presto.execution.task_notification_executor.queued_task_count",
    "presto.execution.user_error_failures.one_minute.count",
    "presto.execution.user_error_failures.one_minute.rate",
    "presto.execution.user_error_failures.total_count",
    "presto.execution.wall_input_bytes_rate.one_minute.max",
    "presto.execution.wall_input_bytes_rate.one_minute.min",
    "presto.execution.wall_input_bytes_rate.one_minute.p75",
    "presto.execution.wall_input_bytes_rate.one_minute.p95",
    "presto.memory.assigned_queries",
    "presto.memory.blocked_nodes",
    "presto.memory.cluster_memory_bytes",
    "presto.memory.free_bytes",
    "presto.memory.free_distributed_bytes",
    "presto.memory.max_bytes",
    "presto.memory.nodes",
    "presto.memory.reserved_bytes",
    "presto.memory.reserved_distributed_bytes",
    "presto.memory.reserved_revocable_bytes",
    "presto.memory.reserved_revocable_distributed_bytes",
    "presto.memory.total_distributed_bytes",
]

OPTIONAL_METRICS = (
    "presto.execution.executor.active_count",
    "presto.execution.executor.completed_task_count",
    "presto.execution.executor.core_pool_size",
    "presto.execution.executor.pool_size",
    "presto.execution.executor.queued_task_count",
    "presto.execution.executor.task_count",
    "presto.execution.management_executor.active_count",
    "presto.execution.management_executor.completed_task_count",
    "presto.execution.management_executor.queued_task_count",
    "presto.failure_detector.active_count",
)
