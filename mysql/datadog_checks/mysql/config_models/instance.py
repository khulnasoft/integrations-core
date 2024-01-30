# (C) Khulnasoft, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from types import MappingProxyType
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, field_validator, model_validator

from khulnasoft_checks.base.utils.functions import identity
from khulnasoft_checks.base.utils.models import validation

from . import defaults, validators


class Aws(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    instance_endpoint: Optional[str] = None


class Azure(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    deployment_type: Optional[str] = None
    fully_qualified_domain_name: Optional[str] = None


class CollectSettings(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    collection_interval: Optional[float] = None
    enabled: Optional[bool] = None


class CustomQuery(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    columns: Optional[tuple[MappingProxyType[str, Any], ...]] = None
    query: Optional[str] = None
    tags: Optional[tuple[str, ...]] = None


class Gcp(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    instance_id: Optional[str] = None
    project_id: Optional[str] = None


class MetricPatterns(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[str, ...]] = None


class ObfuscatorOptions(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    collect_commands: Optional[bool] = None
    collect_comments: Optional[bool] = None
    collect_metadata: Optional[bool] = None
    collect_tables: Optional[bool] = None
    keep_boolean: Optional[bool] = None
    keep_identifier_quotation: Optional[bool] = None
    keep_null: Optional[bool] = None
    keep_positional_parameter: Optional[bool] = None
    keep_sql_alias: Optional[bool] = None
    keep_trailing_semicolon: Optional[bool] = None
    obfuscation_mode: Optional[str] = None
    remove_space_between_parentheses: Optional[bool] = None
    replace_digits: Optional[bool] = None


class Options(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    disable_innodb_metrics: Optional[bool] = None
    extra_innodb_metrics: Optional[bool] = None
    extra_performance_metrics: Optional[bool] = None
    extra_status_metrics: Optional[bool] = None
    galera_cluster: Optional[bool] = None
    replication: Optional[bool] = None
    replication_channel: Optional[str] = None
    replication_non_blocking_status: Optional[bool] = None
    schema_size_metrics: Optional[bool] = None
    system_table_size_metrics: Optional[bool] = None
    table_rows_stats_metrics: Optional[bool] = None
    table_size_metrics: Optional[bool] = None


class QueryActivity(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    collection_interval: Optional[float] = None
    enabled: Optional[bool] = None


class QueryMetrics(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    collection_interval: Optional[float] = None
    enabled: Optional[bool] = None


class QuerySamples(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    collection_interval: Optional[float] = None
    collection_strategy_cache_maxsize: Optional[int] = None
    collection_strategy_cache_ttl: Optional[int] = None
    enabled: Optional[bool] = None
    events_statements_enable_procedure: Optional[str] = None
    events_statements_row_limit: Optional[int] = None
    events_statements_temp_table_name: Optional[str] = None
    explain_procedure: Optional[str] = None
    explained_queries_cache_maxsize: Optional[int] = None
    explained_queries_per_hour_per_query: Optional[int] = None
    fully_qualified_explain_procedure: Optional[str] = None
    samples_per_hour_per_query: Optional[int] = None
    seen_samples_cache_maxsize: Optional[int] = None


class Ssl(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    ca: Optional[str] = None
    cert: Optional[str] = None
    check_hostname: Optional[bool] = None
    key: Optional[str] = None


class InstanceConfig(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        arbitrary_types_allowed=True,
        frozen=True,
    )
    additional_status: Optional[tuple[MappingProxyType[str, Any], ...]] = None
    additional_variable: Optional[tuple[MappingProxyType[str, Any], ...]] = None
    aws: Optional[Aws] = None
    azure: Optional[Azure] = None
    charset: Optional[str] = None
    collect_settings: Optional[CollectSettings] = None
    connect_timeout: Optional[float] = None
    custom_queries: Optional[tuple[CustomQuery, ...]] = None
    database_instance_collection_interval: Optional[float] = None
    dbm: Optional[bool] = None
    defaults_file: Optional[str] = None
    disable_generic_tags: Optional[bool] = None
    empty_default_hostname: Optional[bool] = None
    gcp: Optional[Gcp] = None
    host: Optional[str] = None
    log_unobfuscated_plans: Optional[bool] = None
    log_unobfuscated_queries: Optional[bool] = None
    max_custom_queries: Optional[int] = None
    metric_patterns: Optional[MetricPatterns] = None
    min_collection_interval: Optional[float] = None
    obfuscator_options: Optional[ObfuscatorOptions] = None
    only_custom_queries: Optional[bool] = None
    options: Optional[Options] = None
    password: Optional[str] = None
    port: Optional[float] = None
    queries: Optional[tuple[MappingProxyType[str, Any], ...]] = None
    query_activity: Optional[QueryActivity] = None
    query_metrics: Optional[QueryMetrics] = None
    query_samples: Optional[QuerySamples] = None
    reported_hostname: Optional[str] = None
    service: Optional[str] = None
    sock: Optional[str] = None
    ssl: Optional[Ssl] = None
    tags: Optional[tuple[str, ...]] = None
    use_global_custom_queries: Optional[str] = None
    username: Optional[str] = None

    @model_validator(mode='before')
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @field_validator('*', mode='before')
    def _validate(cls, value, info):
        field = cls.model_fields[info.field_name]
        field_name = field.alias or info.field_name
        if field_name in info.context['configured_fields']:
            value = getattr(validators, f'instance_{info.field_name}', identity)(value, field=field)
        else:
            value = getattr(defaults, f'instance_{info.field_name}', lambda: value)()

        return validation.utils.make_immutable(value)

    @model_validator(mode='after')
    def _final_validation(cls, model):
        return validation.core.check_model(getattr(validators, 'check_instance', identity)(model))
