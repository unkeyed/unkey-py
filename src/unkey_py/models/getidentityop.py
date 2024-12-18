"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
import pydantic
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unkey_py.types import BaseModel
from unkey_py.utils import FieldMetadata, QueryParamMetadata


class GetIdentityRequestTypedDict(TypedDict):
    identity_id: NotRequired[str]
    external_id: NotRequired[str]


class GetIdentityRequest(BaseModel):
    identity_id: Annotated[
        Optional[str],
        pydantic.Field(alias="identityId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    external_id: Annotated[
        Optional[str],
        pydantic.Field(alias="externalId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None


class GetIdentityRatelimitsTypedDict(TypedDict):
    name: str
    r"""The name of this limit. You will need to use this again when verifying a key."""
    limit: int
    r"""How many requests may pass within a given window before requests are rejected."""
    duration: int
    r"""The duration for each ratelimit window in milliseconds."""


class GetIdentityRatelimits(BaseModel):
    name: str
    r"""The name of this limit. You will need to use this again when verifying a key."""

    limit: int
    r"""How many requests may pass within a given window before requests are rejected."""

    duration: int
    r"""The duration for each ratelimit window in milliseconds."""


class GetIdentityResponseBodyTypedDict(TypedDict):
    r"""The configuration for an api"""

    id: str
    r"""The id of this identity. Used to interact with unkey's API"""
    external_id: str
    r"""The id in your system"""
    meta: Dict[str, Any]
    r"""The meta object defined for this identity."""
    ratelimits: List[GetIdentityRatelimitsTypedDict]
    r"""When verifying keys, you can specify which limits you want to use and all keys attached to this identity, will share the limits."""


class GetIdentityResponseBody(BaseModel):
    r"""The configuration for an api"""

    id: str
    r"""The id of this identity. Used to interact with unkey's API"""

    external_id: Annotated[str, pydantic.Field(alias="externalId")]
    r"""The id in your system"""

    meta: Dict[str, Any]
    r"""The meta object defined for this identity."""

    ratelimits: List[GetIdentityRatelimits]
    r"""When verifying keys, you can specify which limits you want to use and all keys attached to this identity, will share the limits."""


class GetIdentityResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    object: NotRequired[GetIdentityResponseBodyTypedDict]
    r"""The configuration for an api"""


class GetIdentityResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    object: Optional[GetIdentityResponseBody] = None
    r"""The configuration for an api"""
