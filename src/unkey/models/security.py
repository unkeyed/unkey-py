"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unkey.types import BaseModel
from unkey.utils import FieldMetadata, SecurityMetadata


class SecurityTypedDict(TypedDict):
    bearer_auth: NotRequired[str]


class Security(BaseModel):
    bearer_auth: Annotated[
        Optional[str],
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="http",
                sub_type="bearer",
                field_name="Authorization",
            )
        ),
    ] = None
