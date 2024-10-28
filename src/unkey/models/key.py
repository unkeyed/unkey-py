"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import pydantic
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unkey.types import BaseModel


class Interval(str, Enum):
    r"""Determines the rate at which verifications will be refilled."""

    DAILY = "daily"
    MONTHLY = "monthly"


class RefillTypedDict(TypedDict):
    r"""Unkey allows you to refill remaining verifications on a key on a regular interval."""

    interval: Interval
    r"""Determines the rate at which verifications will be refilled."""
    amount: int
    r"""Resets `remaining` to this value every interval."""
    last_refill_at: NotRequired[int]
    r"""The unix timestamp in miliseconds when the key was last refilled."""


class Refill(BaseModel):
    r"""Unkey allows you to refill remaining verifications on a key on a regular interval."""

    interval: Interval
    r"""Determines the rate at which verifications will be refilled."""

    amount: int
    r"""Resets `remaining` to this value every interval."""

    last_refill_at: Annotated[Optional[int], pydantic.Field(alias="lastRefillAt")] = (
        None
    )
    r"""The unix timestamp in miliseconds when the key was last refilled."""


class Type(str, Enum):
    r"""Fast ratelimiting doesn't add latency, while consistent ratelimiting is more accurate.
    https://unkey.dev/docs/features/ratelimiting - Learn more
    """

    FAST = "fast"
    CONSISTENT = "consistent"


class RatelimitTypedDict(TypedDict):
    r"""Unkey comes with per-key ratelimiting out of the box."""

    async_: bool
    limit: int
    r"""The total amount of burstable requests."""
    duration: int
    r"""The duration of the ratelimit window, in milliseconds."""
    type: NotRequired[Type]
    r"""Fast ratelimiting doesn't add latency, while consistent ratelimiting is more accurate.
    https://unkey.dev/docs/features/ratelimiting - Learn more
    """
    refill_rate: NotRequired[int]
    r"""How many tokens to refill during each refillInterval."""
    refill_interval: NotRequired[int]
    r"""Determines the speed at which tokens are refilled, in milliseconds."""


class Ratelimit(BaseModel):
    r"""Unkey comes with per-key ratelimiting out of the box."""

    async_: Annotated[bool, pydantic.Field(alias="async")]

    limit: int
    r"""The total amount of burstable requests."""

    duration: int
    r"""The duration of the ratelimit window, in milliseconds."""

    type: Optional[Type] = None
    r"""Fast ratelimiting doesn't add latency, while consistent ratelimiting is more accurate.
    https://unkey.dev/docs/features/ratelimiting - Learn more
    """

    refill_rate: Annotated[Optional[int], pydantic.Field(alias="refillRate")] = None
    r"""How many tokens to refill during each refillInterval."""

    refill_interval: Annotated[
        Optional[int], pydantic.Field(alias="refillInterval")
    ] = None
    r"""Determines the speed at which tokens are refilled, in milliseconds."""


class IdentityTypedDict(TypedDict):
    r"""The identity of the key"""

    id: str
    r"""The id of the identity"""
    external_id: str
    r"""The external id of the identity"""
    meta: NotRequired[Dict[str, Any]]
    r"""Any additional metadata attached to the identity"""


class Identity(BaseModel):
    r"""The identity of the key"""

    id: str
    r"""The id of the identity"""

    external_id: Annotated[str, pydantic.Field(alias="externalId")]
    r"""The external id of the identity"""

    meta: Optional[Dict[str, Any]] = None
    r"""Any additional metadata attached to the identity"""


class KeyTypedDict(TypedDict):
    id: str
    r"""The id of the key"""
    start: str
    r"""The first few characters of the key to visually identify it"""
    workspace_id: str
    r"""The id of the workspace that owns the key"""
    created_at: int
    r"""The unix timestamp in milliseconds when the key was created"""
    api_id: NotRequired[str]
    r"""The id of the api that this key is for"""
    name: NotRequired[str]
    r"""The name of the key, give keys a name to easily identify their purpose"""
    owner_id: NotRequired[str]
    r"""The id of the tenant associated with this key. Use whatever reference you have in your system to identify the tenant. When verifying the key, we will send this field back to you, so you know who is accessing your API."""
    meta: NotRequired[Dict[str, Any]]
    r"""Any additional metadata you want to store with the key"""
    updated_at: NotRequired[int]
    r"""The unix timestamp in milliseconds when the key was last updated"""
    expires: NotRequired[int]
    r"""The unix timestamp in milliseconds when the key will expire. If this field is null or undefined, the key is not expiring."""
    remaining: NotRequired[int]
    r"""The number of requests that can be made with this key before it becomes invalid. If this field is null or undefined, the key has no request limit."""
    refill: NotRequired[RefillTypedDict]
    r"""Unkey allows you to refill remaining verifications on a key on a regular interval."""
    ratelimit: NotRequired[RatelimitTypedDict]
    r"""Unkey comes with per-key ratelimiting out of the box."""
    roles: NotRequired[List[str]]
    r"""All roles this key belongs to"""
    permissions: NotRequired[List[str]]
    r"""All permissions this key has"""
    enabled: NotRequired[bool]
    r"""Sets if key is enabled or disabled. Disabled keys are not valid."""
    plaintext: NotRequired[str]
    r"""The key in plaintext"""
    identity: NotRequired[IdentityTypedDict]
    r"""The identity of the key"""


class Key(BaseModel):
    id: str
    r"""The id of the key"""

    start: str
    r"""The first few characters of the key to visually identify it"""

    workspace_id: Annotated[str, pydantic.Field(alias="workspaceId")]
    r"""The id of the workspace that owns the key"""

    created_at: Annotated[int, pydantic.Field(alias="createdAt")]
    r"""The unix timestamp in milliseconds when the key was created"""

    api_id: Annotated[Optional[str], pydantic.Field(alias="apiId")] = None
    r"""The id of the api that this key is for"""

    name: Optional[str] = None
    r"""The name of the key, give keys a name to easily identify their purpose"""

    owner_id: Annotated[Optional[str], pydantic.Field(alias="ownerId")] = None
    r"""The id of the tenant associated with this key. Use whatever reference you have in your system to identify the tenant. When verifying the key, we will send this field back to you, so you know who is accessing your API."""

    meta: Optional[Dict[str, Any]] = None
    r"""Any additional metadata you want to store with the key"""

    updated_at: Annotated[Optional[int], pydantic.Field(alias="updatedAt")] = None
    r"""The unix timestamp in milliseconds when the key was last updated"""

    expires: Optional[int] = None
    r"""The unix timestamp in milliseconds when the key will expire. If this field is null or undefined, the key is not expiring."""

    remaining: Optional[int] = None
    r"""The number of requests that can be made with this key before it becomes invalid. If this field is null or undefined, the key has no request limit."""

    refill: Optional[Refill] = None
    r"""Unkey allows you to refill remaining verifications on a key on a regular interval."""

    ratelimit: Optional[Ratelimit] = None
    r"""Unkey comes with per-key ratelimiting out of the box."""

    roles: Optional[List[str]] = None
    r"""All roles this key belongs to"""

    permissions: Optional[List[str]] = None
    r"""All permissions this key has"""

    enabled: Optional[bool] = None
    r"""Sets if key is enabled or disabled. Disabled keys are not valid."""

    plaintext: Optional[str] = None
    r"""The key in plaintext"""

    identity: Optional[Identity] = None
    r"""The identity of the key"""
