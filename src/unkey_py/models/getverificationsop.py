"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unkey_py.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from unkey_py.utils import FieldMetadata, QueryParamMetadata


class Granularity(str, Enum):
    r"""The granularity of the usage data to fetch, currently only `day` is supported"""

    DAY = "day"


class GetVerificationsRequestTypedDict(TypedDict):
    key_id: NotRequired[str]
    owner_id: NotRequired[str]
    start: NotRequired[Nullable[int]]
    end: NotRequired[Nullable[int]]
    granularity: NotRequired[Granularity]
    r"""The granularity of the usage data to fetch, currently only `day` is supported"""


class GetVerificationsRequest(BaseModel):
    key_id: Annotated[
        Optional[str],
        pydantic.Field(alias="keyId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    owner_id: Annotated[
        Optional[str],
        pydantic.Field(alias="ownerId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    start: Annotated[
        OptionalNullable[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    end: Annotated[
        OptionalNullable[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    granularity: Annotated[
        Optional[Granularity],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = Granularity.DAY
    r"""The granularity of the usage data to fetch, currently only `day` is supported"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["keyId", "ownerId", "start", "end", "granularity"]
        nullable_fields = ["start", "end"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class VerificationsTypedDict(TypedDict):
    time: int
    r"""The timestamp of the usage data"""
    success: int
    r"""The number of successful requests"""
    rate_limited: int
    r"""The number of requests that were rate limited"""
    usage_exceeded: int
    r"""The number of requests that exceeded the usage limit"""


class Verifications(BaseModel):
    time: int
    r"""The timestamp of the usage data"""

    success: int
    r"""The number of successful requests"""

    rate_limited: Annotated[int, pydantic.Field(alias="rateLimited")]
    r"""The number of requests that were rate limited"""

    usage_exceeded: Annotated[int, pydantic.Field(alias="usageExceeded")]
    r"""The number of requests that exceeded the usage limit"""


class GetVerificationsResponseBodyTypedDict(TypedDict):
    r"""Usage numbers over time"""

    verifications: List[VerificationsTypedDict]


class GetVerificationsResponseBody(BaseModel):
    r"""Usage numbers over time"""

    verifications: List[Verifications]


class GetVerificationsResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    object: NotRequired[GetVerificationsResponseBodyTypedDict]
    r"""Usage numbers over time"""


class GetVerificationsResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    object: Optional[GetVerificationsResponseBody] = None
    r"""Usage numbers over time"""
