"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
import pydantic
from typing import Callable, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unkey_py.types import BaseModel
from unkey_py.utils import FieldMetadata, QueryParamMetadata


class ListIdentitiesRequestTypedDict(TypedDict):
    environment: NotRequired[str]
    limit: NotRequired[int]
    cursor: NotRequired[str]


class ListIdentitiesRequest(BaseModel):
    environment: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "default"

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 100

    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None


class ListIdentitiesRatelimitsTypedDict(TypedDict):
    name: str
    r"""The name of this limit. You will need to use this again when verifying a key."""
    limit: int
    r"""How many requests may pass within a given window before requests are rejected."""
    duration: int
    r"""The duration for each ratelimit window in milliseconds."""


class ListIdentitiesRatelimits(BaseModel):
    name: str
    r"""The name of this limit. You will need to use this again when verifying a key."""

    limit: int
    r"""How many requests may pass within a given window before requests are rejected."""

    duration: int
    r"""The duration for each ratelimit window in milliseconds."""


class ListIdentitiesIdentitiesTypedDict(TypedDict):
    id: str
    r"""The id of this identity. Used to interact with unkey's API"""
    external_id: str
    r"""The id in your system"""
    ratelimits: List[ListIdentitiesRatelimitsTypedDict]
    r"""When verifying keys, you can specify which limits you want to use and all keys attached to this identity, will share the limits."""


class ListIdentitiesIdentities(BaseModel):
    id: str
    r"""The id of this identity. Used to interact with unkey's API"""

    external_id: Annotated[str, pydantic.Field(alias="externalId")]
    r"""The id in your system"""

    ratelimits: List[ListIdentitiesRatelimits]
    r"""When verifying keys, you can specify which limits you want to use and all keys attached to this identity, will share the limits."""


class ListIdentitiesResponseBodyTypedDict(TypedDict):
    r"""A list of identities."""

    identities: List[ListIdentitiesIdentitiesTypedDict]
    r"""A list of identities."""
    total: int
    r"""The total number of identities for this environment"""
    cursor: NotRequired[str]
    r"""The cursor to use for the next page of results, if no cursor is returned, there are no more results"""


class ListIdentitiesResponseBody(BaseModel):
    r"""A list of identities."""

    identities: List[ListIdentitiesIdentities]
    r"""A list of identities."""

    total: int
    r"""The total number of identities for this environment"""

    cursor: Optional[str] = None
    r"""The cursor to use for the next page of results, if no cursor is returned, there are no more results"""


class ListIdentitiesResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    object: NotRequired[ListIdentitiesResponseBodyTypedDict]
    r"""A list of identities."""


class ListIdentitiesResponse(BaseModel):
    next: Callable[[], Optional[ListIdentitiesResponse]]

    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    object: Optional[ListIdentitiesResponseBody] = None
    r"""A list of identities."""