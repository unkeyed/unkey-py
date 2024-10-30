# Migrations
(*migrations*)

## Overview

### Available Operations

* [create_keys](#create_keys)
* [enqueue](#enqueue)

## create_keys

### Example Usage

```python
import os
import unkey_py
from unkey_py import Unkey

s = Unkey(
    bearer_auth=os.getenv("UNKEY_BEARER_AUTH", ""),
)

res = s.migrations.create_keys(request=[
    {
        "api_id": "api_123",
        "name": "my key",
        "start": "unkey_32kq",
        "owner_id": "team_123",
        "meta": {
            "billingTier": "PRO",
            "trialEnds": "2023-06-16T17:16:37.161Z",
        },
        "roles": [
            "admin",
            "finance",
        ],
        "permissions": [
            "domains.create_record",
            "say_hello",
        ],
        "expires": 1623869797161,
        "remaining": 1000,
        "refill": {
            "interval": unkey_py.V1MigrationsCreateKeysInterval.DAILY,
            "amount": 100,
        },
        "ratelimit": {
            "limit": 10,
            "refill_rate": 1,
            "refill_interval": 60,
            "type": unkey_py.V1MigrationsCreateKeysType.FAST,
        },
        "enabled": False,
    },
])

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [List[models.RequestBody]](../../models/.md)                        | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.V1MigrationsCreateKeysResponse](../../models/v1migrationscreatekeysresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrBadRequest          | 400                           | application/json              |
| models.ErrUnauthorized        | 401                           | application/json              |
| models.ErrForbidden           | 403                           | application/json              |
| models.ErrNotFound            | 404                           | application/json              |
| models.ErrConflict            | 409                           | application/json              |
| models.ErrTooManyRequests     | 429                           | application/json              |
| models.ErrInternalServerError | 500                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |

## enqueue

### Example Usage

```python
import os
import unkey_py
from unkey_py import Unkey

s = Unkey(
    bearer_auth=os.getenv("UNKEY_BEARER_AUTH", ""),
)

res = s.migrations.enqueue(request={
    "migration_id": "<id>",
    "api_id": "<id>",
    "keys": [
        {
            "name": "my key",
            "start": "unkey_32kq",
            "owner_id": "team_123",
            "meta": {
                "billingTier": "PRO",
                "trialEnds": "2023-06-16T17:16:37.161Z",
            },
            "roles": [
                "admin",
                "finance",
            ],
            "permissions": [
                "domains.create_record",
                "say_hello",
            ],
            "expires": 1623869797161,
            "remaining": 1000,
            "refill": {
                "interval": unkey_py.V1MigrationsEnqueueKeysInterval.DAILY,
                "amount": 100,
            },
            "ratelimit": {
                "limit": 10,
                "duration": 60000,
                "type": unkey_py.V1MigrationsEnqueueKeysType.FAST,
            },
            "enabled": False,
        },
    ],
})

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.V1MigrationsEnqueueKeysRequestBody](../../models/v1migrationsenqueuekeysrequestbody.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.V1MigrationsEnqueueKeysResponse](../../models/v1migrationsenqueuekeysresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrBadRequest          | 400                           | application/json              |
| models.ErrUnauthorized        | 401                           | application/json              |
| models.ErrForbidden           | 403                           | application/json              |
| models.ErrNotFound            | 404                           | application/json              |
| models.ErrConflict            | 409                           | application/json              |
| models.ErrTooManyRequests     | 429                           | application/json              |
| models.ErrInternalServerError | 500                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |