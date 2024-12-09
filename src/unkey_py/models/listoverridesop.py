"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unkey_py.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from unkey_py.utils import FieldMetadata, QueryParamMetadata


class ListOverridesRequestTypedDict(TypedDict):
    namespace_id: NotRequired[str]
    namespace_name: NotRequired[str]
    limit: NotRequired[int]
    cursor: NotRequired[str]


class ListOverridesRequest(BaseModel):
    namespace_id: Annotated[
        Optional[str],
        pydantic.Field(alias="namespaceId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    namespace_name: Annotated[
        Optional[str],
        pydantic.Field(alias="namespaceName"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 100

    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None


class OverridesTypedDict(TypedDict):
    id: str
    identifier: str
    limit: int
    duration: int
    async_: NotRequired[Nullable[bool]]


class Overrides(BaseModel):
    id: str

    identifier: str

    limit: int

    duration: int

    async_: Annotated[OptionalNullable[bool], pydantic.Field(alias="async")] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["async"]
        nullable_fields = ["async"]
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


class ListOverridesResponseBodyTypedDict(TypedDict):
    r"""List of overrides for the given namespace."""

    overrides: List[OverridesTypedDict]
    total: int
    r"""The total number of overrides for the namespace"""
    cursor: NotRequired[str]
    r"""The cursor to use for the next page of results, if no cursor is returned, there are no more results"""


class ListOverridesResponseBody(BaseModel):
    r"""List of overrides for the given namespace."""

    overrides: List[Overrides]

    total: int
    r"""The total number of overrides for the namespace"""

    cursor: Optional[str] = None
    r"""The cursor to use for the next page of results, if no cursor is returned, there are no more results"""


class ListOverridesResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    object: NotRequired[ListOverridesResponseBodyTypedDict]
    r"""List of overrides for the given namespace."""


class ListOverridesResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    object: Optional[ListOverridesResponseBody] = None
    r"""List of overrides for the given namespace."""