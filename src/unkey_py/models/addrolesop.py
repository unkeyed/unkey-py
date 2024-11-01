"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unkey_py.types import BaseModel


class AddRolesRolesTypedDict(TypedDict):
    id: NotRequired[str]
    r"""The id of the role. Provide either `id` or `name`. If both are provided `id` is used."""
    name: NotRequired[str]
    r"""Identify the role via its name. Provide either `id` or `name`. If both are provided `id` is used."""
    create: NotRequired[bool]
    r"""Set to true to automatically create the permissions they do not exist yet. Only works when specifying `name`.
    Autocreating roles requires your root key to have the `rbac.*.create_role` permission, otherwise the request will get rejected
    """


class AddRolesRoles(BaseModel):
    id: Optional[str] = None
    r"""The id of the role. Provide either `id` or `name`. If both are provided `id` is used."""

    name: Optional[str] = None
    r"""Identify the role via its name. Provide either `id` or `name`. If both are provided `id` is used."""

    create: Optional[bool] = None
    r"""Set to true to automatically create the permissions they do not exist yet. Only works when specifying `name`.
    Autocreating roles requires your root key to have the `rbac.*.create_role` permission, otherwise the request will get rejected
    """


class AddRolesRequestBodyTypedDict(TypedDict):
    key_id: str
    r"""The id of the key."""
    roles: List[AddRolesRolesTypedDict]
    r"""The roles you want to set for this key. This overwrites all existing roles.
    Setting roles requires the `rbac.*.add_role_to_key` permission.
    """


class AddRolesRequestBody(BaseModel):
    key_id: Annotated[str, pydantic.Field(alias="keyId")]
    r"""The id of the key."""

    roles: List[AddRolesRoles]
    r"""The roles you want to set for this key. This overwrites all existing roles.
    Setting roles requires the `rbac.*.add_role_to_key` permission.
    """


class AddRolesResponseBodyTypedDict(TypedDict):
    id: str
    r"""The id of the role. This is used internally"""
    name: str
    r"""The name of the role"""


class AddRolesResponseBody(BaseModel):
    id: str
    r"""The id of the role. This is used internally"""

    name: str
    r"""The name of the role"""


class AddRolesResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    response_bodies: NotRequired[List[AddRolesResponseBodyTypedDict]]
    r"""All currently connected roles"""


class AddRolesResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    response_bodies: Optional[List[AddRolesResponseBody]] = None
    r"""All currently connected roles"""
