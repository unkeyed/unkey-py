"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .httpmetadata import HTTPMetadata, HTTPMetadataTypedDict
from enum import Enum
import pydantic
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict, deprecated
from unkey_py.types import BaseModel


class Variant(str, Enum):
    r"""The algorithm for hashing and encoding, currently only sha256 and base64 are supported"""

    SHA256_BASE64 = "sha256_base64"


class HashTypedDict(TypedDict):
    r"""Provide either `hash` or `plaintext`"""

    value: str
    r"""The hashed and encoded key"""
    variant: Variant
    r"""The algorithm for hashing and encoding, currently only sha256 and base64 are supported"""


class Hash(BaseModel):
    r"""Provide either `hash` or `plaintext`"""

    value: str
    r"""The hashed and encoded key"""

    variant: Variant
    r"""The algorithm for hashing and encoding, currently only sha256 and base64 are supported"""


class V1MigrationsCreateKeysInterval(str, Enum):
    r"""Unkey will automatically refill verifications at the set interval."""

    DAILY = "daily"
    MONTHLY = "monthly"


class V1MigrationsCreateKeysRefillTypedDict(TypedDict):
    r"""Unkey enables you to refill verifications for each key at regular intervals."""

    interval: V1MigrationsCreateKeysInterval
    r"""Unkey will automatically refill verifications at the set interval."""
    amount: int
    r"""The number of verifications to refill for each occurrence is determined individually for each key."""


class V1MigrationsCreateKeysRefill(BaseModel):
    r"""Unkey enables you to refill verifications for each key at regular intervals."""

    interval: V1MigrationsCreateKeysInterval
    r"""Unkey will automatically refill verifications at the set interval."""

    amount: int
    r"""The number of verifications to refill for each occurrence is determined individually for each key."""


@deprecated(
    "warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
)
class V1MigrationsCreateKeysType(str, Enum):
    r"""Fast ratelimiting doesn't add latency, while consistent ratelimiting is more accurate.
    https://unkey.dev/docs/features/ratelimiting - Learn more
    """

    FAST = "fast"
    CONSISTENT = "consistent"


class V1MigrationsCreateKeysRatelimitTypedDict(TypedDict):
    r"""Unkey comes with per-key ratelimiting out of the box."""

    limit: int
    r"""The total amount of burstable requests."""
    refill_rate: int
    r"""How many tokens to refill during each refillInterval."""
    refill_interval: int
    r"""Determines the speed at which tokens are refilled, in milliseconds."""
    async_: NotRequired[bool]
    r"""Async will return a response immediately, lowering latency at the cost of accuracy.
    https://unkey.dev/docs/features/ratelimiting - Learn more
    """
    type: NotRequired[V1MigrationsCreateKeysType]
    r"""Fast ratelimiting doesn't add latency, while consistent ratelimiting is more accurate.
    https://unkey.dev/docs/features/ratelimiting - Learn more
    """


class V1MigrationsCreateKeysRatelimit(BaseModel):
    r"""Unkey comes with per-key ratelimiting out of the box."""

    limit: int
    r"""The total amount of burstable requests."""

    refill_rate: Annotated[
        int,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="refillRate",
        ),
    ]
    r"""How many tokens to refill during each refillInterval."""

    refill_interval: Annotated[
        int,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="refillInterval",
        ),
    ]
    r"""Determines the speed at which tokens are refilled, in milliseconds."""

    async_: Annotated[Optional[bool], pydantic.Field(alias="async")] = False
    r"""Async will return a response immediately, lowering latency at the cost of accuracy.
    https://unkey.dev/docs/features/ratelimiting - Learn more
    """

    type: Annotated[
        Optional[V1MigrationsCreateKeysType],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = V1MigrationsCreateKeysType.FAST
    r"""Fast ratelimiting doesn't add latency, while consistent ratelimiting is more accurate.
    https://unkey.dev/docs/features/ratelimiting - Learn more
    """


class RequestBodyTypedDict(TypedDict):
    api_id: str
    r"""Choose an `API` where this key should be created."""
    prefix: NotRequired[str]
    r"""To make it easier for your users to understand which product an api key belongs to, you can add prefix them.

    For example Stripe famously prefixes their customer ids with cus_ or their api keys with sk_live_.

    The underscore is automatically added if you are defining a prefix, for example: \"prefix\": \"abc\" will result in a key like abc_xxxxxxxxx

    """
    name: NotRequired[str]
    r"""The name for your Key. This is not customer facing."""
    plaintext: NotRequired[str]
    r"""The raw key in plaintext. If provided, unkey encrypts this value and stores it securely. Provide either `hash` or `plaintext`"""
    hash: NotRequired[HashTypedDict]
    r"""Provide either `hash` or `plaintext`"""
    start: NotRequired[str]
    r"""The first 4 characters of the key. If a prefix is used, it should be the prefix plus 4 characters."""
    owner_id: NotRequired[str]
    r"""Your user’s Id. This will provide a link between Unkey and your customer record.
    When validating a key, we will return this back to you, so you can clearly identify your user from their api key.
    """
    meta: NotRequired[Dict[str, Any]]
    r"""This is a place for dynamic meta data, anything that feels useful for you should go here"""
    roles: NotRequired[List[str]]
    r"""A list of roles that this key should have. If the role does not exist, an error is thrown"""
    permissions: NotRequired[List[str]]
    r"""A list of permissions that this key should have. If the permission does not exist, an error is thrown"""
    expires: NotRequired[int]
    r"""You can auto expire keys by providing a unix timestamp in milliseconds. Once Keys expire they will automatically be disabled and are no longer valid unless you enable them again."""
    remaining: NotRequired[int]
    r"""You can limit the number of requests a key can make. Once a key reaches 0 remaining requests, it will automatically be disabled and is no longer valid unless you update it.
    https://unkey.dev/docs/features/remaining - Learn more
    """
    refill: NotRequired[V1MigrationsCreateKeysRefillTypedDict]
    r"""Unkey enables you to refill verifications for each key at regular intervals."""
    ratelimit: NotRequired[V1MigrationsCreateKeysRatelimitTypedDict]
    r"""Unkey comes with per-key ratelimiting out of the box."""
    enabled: NotRequired[bool]
    r"""Sets if key is enabled or disabled. Disabled keys are not valid."""
    environment: NotRequired[str]
    r"""Environments allow you to divide your keyspace.

    Some applications like Stripe, Clerk, WorkOS and others have a concept of \"live\" and \"test\" keys to
    give the developer a way to develop their own application without the risk of modifying real world
    resources.

    When you set an environment, we will return it back to you when validating the key, so you can
    handle it correctly.

    """


class RequestBody(BaseModel):
    api_id: Annotated[str, pydantic.Field(alias="apiId")]
    r"""Choose an `API` where this key should be created."""

    prefix: Optional[str] = None
    r"""To make it easier for your users to understand which product an api key belongs to, you can add prefix them.

    For example Stripe famously prefixes their customer ids with cus_ or their api keys with sk_live_.

    The underscore is automatically added if you are defining a prefix, for example: \"prefix\": \"abc\" will result in a key like abc_xxxxxxxxx

    """

    name: Optional[str] = None
    r"""The name for your Key. This is not customer facing."""

    plaintext: Optional[str] = None
    r"""The raw key in plaintext. If provided, unkey encrypts this value and stores it securely. Provide either `hash` or `plaintext`"""

    hash: Optional[Hash] = None
    r"""Provide either `hash` or `plaintext`"""

    start: Optional[str] = None
    r"""The first 4 characters of the key. If a prefix is used, it should be the prefix plus 4 characters."""

    owner_id: Annotated[Optional[str], pydantic.Field(alias="ownerId")] = None
    r"""Your user’s Id. This will provide a link between Unkey and your customer record.
    When validating a key, we will return this back to you, so you can clearly identify your user from their api key.
    """

    meta: Optional[Dict[str, Any]] = None
    r"""This is a place for dynamic meta data, anything that feels useful for you should go here"""

    roles: Optional[List[str]] = None
    r"""A list of roles that this key should have. If the role does not exist, an error is thrown"""

    permissions: Optional[List[str]] = None
    r"""A list of permissions that this key should have. If the permission does not exist, an error is thrown"""

    expires: Optional[int] = None
    r"""You can auto expire keys by providing a unix timestamp in milliseconds. Once Keys expire they will automatically be disabled and are no longer valid unless you enable them again."""

    remaining: Optional[int] = None
    r"""You can limit the number of requests a key can make. Once a key reaches 0 remaining requests, it will automatically be disabled and is no longer valid unless you update it.
    https://unkey.dev/docs/features/remaining - Learn more
    """

    refill: Optional[V1MigrationsCreateKeysRefill] = None
    r"""Unkey enables you to refill verifications for each key at regular intervals."""

    ratelimit: Optional[V1MigrationsCreateKeysRatelimit] = None
    r"""Unkey comes with per-key ratelimiting out of the box."""

    enabled: Optional[bool] = True
    r"""Sets if key is enabled or disabled. Disabled keys are not valid."""

    environment: Optional[str] = None
    r"""Environments allow you to divide your keyspace.

    Some applications like Stripe, Clerk, WorkOS and others have a concept of \"live\" and \"test\" keys to
    give the developer a way to develop their own application without the risk of modifying real world
    resources.

    When you set an environment, we will return it back to you when validating the key, so you can
    handle it correctly.

    """


class V1MigrationsCreateKeysResponseBodyTypedDict(TypedDict):
    r"""The key ids of all created keys"""

    key_ids: List[str]
    r"""The ids of the keys. This is not a secret and can be stored as a reference if you wish. You need the keyId to update or delete a key later."""


class V1MigrationsCreateKeysResponseBody(BaseModel):
    r"""The key ids of all created keys"""

    key_ids: Annotated[List[str], pydantic.Field(alias="keyIds")]
    r"""The ids of the keys. This is not a secret and can be stored as a reference if you wish. You need the keyId to update or delete a key later."""


class V1MigrationsCreateKeysResponseTypedDict(TypedDict):
    http_meta: HTTPMetadataTypedDict
    object: NotRequired[V1MigrationsCreateKeysResponseBodyTypedDict]
    r"""The key ids of all created keys"""


class V1MigrationsCreateKeysResponse(BaseModel):
    http_meta: Annotated[Optional[HTTPMetadata], pydantic.Field(exclude=True)] = None

    object: Optional[V1MigrationsCreateKeysResponseBody] = None
    r"""The key ids of all created keys"""