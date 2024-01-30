# (C) Khulnasoft, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from khulnasoft_checks.base.utils.functions import identity
from khulnasoft_checks.base.utils.models import validation

from . import defaults, validators


class MetricPatterns(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[str, ...]] = None


class InstanceConfig(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        arbitrary_types_allowed=True,
        frozen=True,
    )
    collect_client_metrics: Optional[bool] = None
    command_stats: Optional[bool] = None
    db: Optional[int] = None
    disable_connection_cache: Optional[bool] = None
    disable_generic_tags: Optional[bool] = None
    empty_default_hostname: Optional[bool] = None
    host: str
    keys: Optional[tuple[str, ...]] = None
    metric_patterns: Optional[MetricPatterns] = None
    min_collection_interval: Optional[float] = None
    password: Optional[str] = None
    port: int
    service: Optional[str] = None
    slowlog_max_len: Optional[int] = Field(None, alias='slowlog-max-len')
    socket_timeout: Optional[int] = None
    ssl: Optional[bool] = None
    ssl_ca_certs: Optional[str] = None
    ssl_cert_reqs: Optional[int] = None
    ssl_certfile: Optional[str] = None
    ssl_keyfile: Optional[str] = None
    tags: Optional[tuple[str, ...]] = None
    unix_socket_path: Optional[str] = None
    username: Optional[str] = None
    warn_on_missing_keys: Optional[bool] = None

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
