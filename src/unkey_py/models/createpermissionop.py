"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unkey_py.types import BaseModel


class CreatePermissionRequestBodyTypedDict(TypedDict):
    name: str
    r"""The unique name of your permission."""
    description: NotRequired[str]
    r"""Explain what this permission does. This is just for your team, your users will not see this."""


class CreatePermissionRequestBody(BaseModel):
    name: str
    r"""The unique name of your permission."""

    description: Optional[str] = None
    r"""Explain what this permission does. This is just for your team, your users will not see this."""


class CreatePermissionResponseBodyTypedDict(TypedDict):
    r"""Sucessfully created a permission"""

    permission_id: str
    r"""The id of the permission. This is used internally"""


class CreatePermissionResponseBody(BaseModel):
    r"""Sucessfully created a permission"""

    permission_id: Annotated[str, pydantic.Field(alias="permissionId")]
    r"""The id of the permission. This is used internally"""


class CreatePermissionResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    object: NotRequired[CreatePermissionResponseBodyTypedDict]
    r"""Sucessfully created a permission"""


class CreatePermissionResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    object: Optional[CreatePermissionResponseBody] = None
    r"""Sucessfully created a permission"""
