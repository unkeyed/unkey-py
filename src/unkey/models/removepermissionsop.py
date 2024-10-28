"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unkey.types import BaseModel


class RemovePermissionsPermissionsTypedDict(TypedDict):
    id: NotRequired[str]
    r"""The id of the permission. Provide either `id` or `name`. If both are provided `id` is used."""
    name: NotRequired[str]
    r"""Identify the permission via its name. Provide either `id` or `name`. If both are provided `id` is used."""


class RemovePermissionsPermissions(BaseModel):
    id: Optional[str] = None
    r"""The id of the permission. Provide either `id` or `name`. If both are provided `id` is used."""

    name: Optional[str] = None
    r"""Identify the permission via its name. Provide either `id` or `name`. If both are provided `id` is used."""


class RemovePermissionsRequestBodyTypedDict(TypedDict):
    key_id: str
    r"""The id of the key."""
    permissions: List[RemovePermissionsPermissionsTypedDict]
    r"""The permissions you want to remove from this key."""


class RemovePermissionsRequestBody(BaseModel):
    key_id: Annotated[str, pydantic.Field(alias="keyId")]
    r"""The id of the key."""

    permissions: List[RemovePermissionsPermissions]
    r"""The permissions you want to remove from this key."""


class RemovePermissionsResponseBodyTypedDict(TypedDict):
    r"""Success"""


class RemovePermissionsResponseBody(BaseModel):
    r"""Success"""


class RemovePermissionsResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    object: NotRequired[RemovePermissionsResponseBodyTypedDict]
    r"""Success"""


class RemovePermissionsResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    object: Optional[RemovePermissionsResponseBody] = None
    r"""Success"""
