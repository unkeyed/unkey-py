"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unkey_py.types import BaseModel


class RemoveRolesRolesTypedDict(TypedDict):
    id: NotRequired[str]
    r"""The id of the role. Provide either `id` or `name`. If both are provided `id` is used."""
    name: NotRequired[str]
    r"""Identify the role via its name. Provide either `id` or `name`. If both are provided `id` is used."""


class RemoveRolesRoles(BaseModel):
    id: Optional[str] = None
    r"""The id of the role. Provide either `id` or `name`. If both are provided `id` is used."""

    name: Optional[str] = None
    r"""Identify the role via its name. Provide either `id` or `name`. If both are provided `id` is used."""


class RemoveRolesRequestBodyTypedDict(TypedDict):
    key_id: str
    r"""The id of the key."""
    roles: List[RemoveRolesRolesTypedDict]
    r"""The roles you want to remove from this key."""


class RemoveRolesRequestBody(BaseModel):
    key_id: Annotated[str, pydantic.Field(alias="keyId")]
    r"""The id of the key."""

    roles: List[RemoveRolesRoles]
    r"""The roles you want to remove from this key."""


class RemoveRolesResponseBodyTypedDict(TypedDict):
    r"""Success"""


class RemoveRolesResponseBody(BaseModel):
    r"""Success"""


class RemoveRolesResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    object: NotRequired[RemoveRolesResponseBodyTypedDict]
    r"""Success"""


class RemoveRolesResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    object: Optional[RemoveRolesResponseBody] = None
    r"""Success"""