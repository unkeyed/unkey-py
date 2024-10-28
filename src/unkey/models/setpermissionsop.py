"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unkey.types import BaseModel


class SetPermissionsPermissionsTypedDict(TypedDict):
    id: NotRequired[str]
    r"""The id of the permission. Provide either `id` or `name`. If both are provided `id` is used."""
    name: NotRequired[str]
    r"""Identify the permission via its name. Provide either `id` or `name`. If both are provided `id` is used."""
    create: NotRequired[bool]
    r"""Set to true to automatically create the permissions they do not exist yet. Only works when specifying `name`.
    Autocreating permissions requires your root key to have the `rbac.*.create_permission` permission, otherwise the request will get rejected
    """


class SetPermissionsPermissions(BaseModel):
    id: Optional[str] = None
    r"""The id of the permission. Provide either `id` or `name`. If both are provided `id` is used."""

    name: Optional[str] = None
    r"""Identify the permission via its name. Provide either `id` or `name`. If both are provided `id` is used."""

    create: Optional[bool] = None
    r"""Set to true to automatically create the permissions they do not exist yet. Only works when specifying `name`.
    Autocreating permissions requires your root key to have the `rbac.*.create_permission` permission, otherwise the request will get rejected
    """


class SetPermissionsRequestBodyTypedDict(TypedDict):
    key_id: str
    r"""The id of the key."""
    permissions: List[SetPermissionsPermissionsTypedDict]
    r"""The permissions you want to set for this key. This overwrites all existing permissions.
    Setting permissions requires the `rbac.*.add_permission_to_key` permission.
    """


class SetPermissionsRequestBody(BaseModel):
    key_id: Annotated[str, pydantic.Field(alias="keyId")]
    r"""The id of the key."""

    permissions: List[SetPermissionsPermissions]
    r"""The permissions you want to set for this key. This overwrites all existing permissions.
    Setting permissions requires the `rbac.*.add_permission_to_key` permission.
    """


class SetPermissionsResponseBodyTypedDict(TypedDict):
    id: str
    r"""The id of the permission. This is used internally"""
    name: str
    r"""The name of the permission"""


class SetPermissionsResponseBody(BaseModel):
    id: str
    r"""The id of the permission. This is used internally"""

    name: str
    r"""The name of the permission"""
