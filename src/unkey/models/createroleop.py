"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unkey.types import BaseModel


class CreateRoleRequestBodyTypedDict(TypedDict):
    name: str
    r"""The unique name of your role."""
    description: NotRequired[str]
    r"""Explain what this role does. This is just for your team, your users will not see this."""


class CreateRoleRequestBody(BaseModel):
    name: str
    r"""The unique name of your role."""

    description: Optional[str] = None
    r"""Explain what this role does. This is just for your team, your users will not see this."""


class CreateRoleResponseBodyTypedDict(TypedDict):
    r"""Sucessfully created a role"""

    role_id: str
    r"""The id of the role. This is used internally"""


class CreateRoleResponseBody(BaseModel):
    r"""Sucessfully created a role"""

    role_id: Annotated[str, pydantic.Field(alias="roleId")]
    r"""The id of the role. This is used internally"""
