# Keys
(*keys*)

## Overview

### Available Operations

* [get](#get)
* [whoami](#whoami)
* [delete](#delete)
* [create](#create)
* [verify](#verify)
* [update](#update)
* [update_remaining](#update_remaining)
* [get_verifications](#get_verifications)
* [add_permissions](#add_permissions)
* [remove_permissions](#remove_permissions)
* [set_permissions](#set_permissions)
* [add_roles](#add_roles)
* [remove_roles](#remove_roles)
* [set_roles](#set_roles)

## get

### Example Usage

```python
from unkey_py import Unkey


with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.keys.get(key_id="key_1234")

    assert res.key is not None

    # Handle response
    print(res.key)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `key_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | key_1234                                                            |
| `decrypt`                                                           | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetKeyResponse](../../models/getkeyresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrBadRequest          | 400                           | application/json              |
| models.ErrUnauthorized        | 401                           | application/json              |
| models.ErrForbidden           | 403                           | application/json              |
| models.ErrNotFound            | 404                           | application/json              |
| models.ErrConflict            | 409                           | application/json              |
| models.ErrPreconditionFailed  | 412                           | application/json              |
| models.ErrTooManyRequests     | 429                           | application/json              |
| models.ErrInternalServerError | 500                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |

## whoami

### Example Usage

```python
from unkey_py import Unkey


with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.keys.whoami(request={
        "key": "sk_123",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.WhoamiRequestBody](../../models/whoamirequestbody.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WhoamiResponse](../../models/whoamiresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrBadRequest          | 400                           | application/json              |
| models.ErrUnauthorized        | 401                           | application/json              |
| models.ErrForbidden           | 403                           | application/json              |
| models.ErrNotFound            | 404                           | application/json              |
| models.ErrConflict            | 409                           | application/json              |
| models.ErrPreconditionFailed  | 412                           | application/json              |
| models.ErrTooManyRequests     | 429                           | application/json              |
| models.ErrInternalServerError | 500                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |

## delete

### Example Usage

```python
from unkey_py import Unkey


with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.keys.delete(request={
        "key_id": "key_1234",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.DeleteKeyRequestBody](../../models/deletekeyrequestbody.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteKeyResponse](../../models/deletekeyresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrBadRequest          | 400                           | application/json              |
| models.ErrUnauthorized        | 401                           | application/json              |
| models.ErrForbidden           | 403                           | application/json              |
| models.ErrNotFound            | 404                           | application/json              |
| models.ErrConflict            | 409                           | application/json              |
| models.ErrPreconditionFailed  | 412                           | application/json              |
| models.ErrTooManyRequests     | 429                           | application/json              |
| models.ErrInternalServerError | 500                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |

## create

### Example Usage

```python
import unkey_py
from unkey_py import Unkey


with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.keys.create(request={
        "api_id": "api_123",
        "name": "my key",
        "external_id": "team_123",
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
            "interval": unkey_py.CreateKeyInterval.MONTHLY,
            "amount": 100,
            "refill_day": 15,
        },
        "ratelimit": {
            "limit": 10,
            "duration": 60000,
        },
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CreateKeyRequestBody](../../models/createkeyrequestbody.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateKeyResponse](../../models/createkeyresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrBadRequest          | 400                           | application/json              |
| models.ErrUnauthorized        | 401                           | application/json              |
| models.ErrForbidden           | 403                           | application/json              |
| models.ErrNotFound            | 404                           | application/json              |
| models.ErrConflict            | 409                           | application/json              |
| models.ErrPreconditionFailed  | 412                           | application/json              |
| models.ErrTooManyRequests     | 429                           | application/json              |
| models.ErrInternalServerError | 500                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |

## verify

### Example Usage

```python
from unkey_py import Unkey


with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.keys.verify(request={
        "api_id": "api_1234",
        "key": "sk_1234",
        "tags": [
            "path=/v1/users/123",
            "region=us-east-1",
        ],
        "ratelimits": [
            {
                "name": "tokens",
                "limit": 500,
                "duration": 3600000,
            },
            {
                "name": "tokens",
                "limit": 20000,
                "duration": 86400000,
            },
        ],
    })

    assert res.v1_keys_verify_key_response is not None

    # Handle response
    print(res.v1_keys_verify_key_response)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.V1KeysVerifyKeyRequest](../../models/v1keysverifykeyrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.VerifyKeyResponse](../../models/verifykeyresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrBadRequest          | 400                           | application/json              |
| models.ErrUnauthorized        | 401                           | application/json              |
| models.ErrForbidden           | 403                           | application/json              |
| models.ErrNotFound            | 404                           | application/json              |
| models.ErrConflict            | 409                           | application/json              |
| models.ErrPreconditionFailed  | 412                           | application/json              |
| models.ErrTooManyRequests     | 429                           | application/json              |
| models.ErrInternalServerError | 500                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |

## update

### Example Usage

```python
import unkey_py
from unkey_py import Unkey


with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.keys.update(request={
        "key_id": "key_123",
        "name": "Customer X",
        "external_id": "user_123",
        "meta": {
            "roles": [
                "admin",
                "user",
            ],
            "stripeCustomerId": "cus_1234",
        },
        "expires": 0,
        "ratelimit": {
            "type": unkey_py.UpdateKeyType.FAST,
            "limit": 10,
            "refill_rate": 1,
            "refill_interval": 60,
        },
        "remaining": 1000,
        "refill": {
            "interval": unkey_py.UpdateKeyInterval.DAILY,
            "amount": 100,
        },
        "enabled": True,
        "roles": [
            {
                "id": "perm_123",
            },
            {
                "name": "dns.record.create",
            },
            {
                "name": "dns.record.delete",
                "create": True,
            },
        ],
        "permissions": [
            {
                "id": "perm_123",
            },
            {
                "name": "dns.record.create",
            },
            {
                "name": "dns.record.delete",
                "create": True,
            },
        ],
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.UpdateKeyRequestBody](../../models/updatekeyrequestbody.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateKeyResponse](../../models/updatekeyresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrBadRequest          | 400                           | application/json              |
| models.ErrUnauthorized        | 401                           | application/json              |
| models.ErrForbidden           | 403                           | application/json              |
| models.ErrNotFound            | 404                           | application/json              |
| models.ErrConflict            | 409                           | application/json              |
| models.ErrPreconditionFailed  | 412                           | application/json              |
| models.ErrTooManyRequests     | 429                           | application/json              |
| models.ErrInternalServerError | 500                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |

## update_remaining

### Example Usage

```python
import unkey_py
from unkey_py import Unkey


with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.keys.update_remaining(request={
        "key_id": "key_123",
        "op": unkey_py.Op.SET,
        "value": 1,
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.UpdateRemainingRequestBody](../../models/updateremainingrequestbody.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.UpdateRemainingResponse](../../models/updateremainingresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrBadRequest          | 400                           | application/json              |
| models.ErrUnauthorized        | 401                           | application/json              |
| models.ErrForbidden           | 403                           | application/json              |
| models.ErrNotFound            | 404                           | application/json              |
| models.ErrConflict            | 409                           | application/json              |
| models.ErrPreconditionFailed  | 412                           | application/json              |
| models.ErrTooManyRequests     | 429                           | application/json              |
| models.ErrInternalServerError | 500                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |

## get_verifications

### Example Usage

```python
from unkey_py import Unkey


with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.keys.get_verifications(request={
        "key_id": "key_1234",
        "owner_id": "chronark",
        "start": 1620000000000,
        "end": 1620000000000,
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.KeysGetVerificationsRequest](../../models/keysgetverificationsrequest.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.KeysGetVerificationsResponse](../../models/keysgetverificationsresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrBadRequest          | 400                           | application/json              |
| models.ErrUnauthorized        | 401                           | application/json              |
| models.ErrForbidden           | 403                           | application/json              |
| models.ErrNotFound            | 404                           | application/json              |
| models.ErrConflict            | 409                           | application/json              |
| models.ErrPreconditionFailed  | 412                           | application/json              |
| models.ErrTooManyRequests     | 429                           | application/json              |
| models.ErrInternalServerError | 500                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |

## add_permissions

### Example Usage

```python
from unkey_py import Unkey


with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.keys.add_permissions(request={
        "key_id": "<id>",
        "permissions": [
            {},
            {},
            {},
        ],
    })

    assert res.response_bodies is not None

    # Handle response
    print(res.response_bodies)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.AddPermissionsRequestBody](../../models/addpermissionsrequestbody.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.AddPermissionsResponse](../../models/addpermissionsresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrBadRequest          | 400                           | application/json              |
| models.ErrUnauthorized        | 401                           | application/json              |
| models.ErrForbidden           | 403                           | application/json              |
| models.ErrNotFound            | 404                           | application/json              |
| models.ErrConflict            | 409                           | application/json              |
| models.ErrPreconditionFailed  | 412                           | application/json              |
| models.ErrTooManyRequests     | 429                           | application/json              |
| models.ErrInternalServerError | 500                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |

## remove_permissions

### Example Usage

```python
from unkey_py import Unkey


with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.keys.remove_permissions(request={
        "key_id": "<id>",
        "permissions": [
            {
                "id": "perm_123",
            },
            {
                "name": "dns.record.create",
            },
        ],
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.RemovePermissionsRequestBody](../../models/removepermissionsrequestbody.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.RemovePermissionsResponse](../../models/removepermissionsresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrBadRequest          | 400                           | application/json              |
| models.ErrUnauthorized        | 401                           | application/json              |
| models.ErrForbidden           | 403                           | application/json              |
| models.ErrNotFound            | 404                           | application/json              |
| models.ErrConflict            | 409                           | application/json              |
| models.ErrPreconditionFailed  | 412                           | application/json              |
| models.ErrTooManyRequests     | 429                           | application/json              |
| models.ErrInternalServerError | 500                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |

## set_permissions

### Example Usage

```python
from unkey_py import Unkey


with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.keys.set_permissions(request={
        "key_id": "<id>",
        "permissions": [
            {
                "id": "perm_123",
            },
            {
                "name": "dns.record.create",
            },
            {
                "name": "dns.record.delete",
                "create": True,
            },
        ],
    })

    assert res.response_bodies is not None

    # Handle response
    print(res.response_bodies)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.SetPermissionsRequestBody](../../models/setpermissionsrequestbody.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.SetPermissionsResponse](../../models/setpermissionsresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrBadRequest          | 400                           | application/json              |
| models.ErrUnauthorized        | 401                           | application/json              |
| models.ErrForbidden           | 403                           | application/json              |
| models.ErrNotFound            | 404                           | application/json              |
| models.ErrConflict            | 409                           | application/json              |
| models.ErrPreconditionFailed  | 412                           | application/json              |
| models.ErrTooManyRequests     | 429                           | application/json              |
| models.ErrInternalServerError | 500                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |

## add_roles

### Example Usage

```python
from unkey_py import Unkey


with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.keys.add_roles(request={
        "key_id": "<id>",
        "roles": [
            {
                "id": "role_123",
            },
            {
                "name": "dns.record.create",
            },
            {
                "name": "dns.record.delete",
                "create": True,
            },
        ],
    })

    assert res.response_bodies is not None

    # Handle response
    print(res.response_bodies)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.AddRolesRequestBody](../../models/addrolesrequestbody.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AddRolesResponse](../../models/addrolesresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrBadRequest          | 400                           | application/json              |
| models.ErrUnauthorized        | 401                           | application/json              |
| models.ErrForbidden           | 403                           | application/json              |
| models.ErrNotFound            | 404                           | application/json              |
| models.ErrConflict            | 409                           | application/json              |
| models.ErrPreconditionFailed  | 412                           | application/json              |
| models.ErrTooManyRequests     | 429                           | application/json              |
| models.ErrInternalServerError | 500                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |

## remove_roles

### Example Usage

```python
from unkey_py import Unkey


with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.keys.remove_roles(request={
        "key_id": "<id>",
        "roles": [
            {
                "id": "role_123",
            },
            {
                "name": "dns.record.create",
            },
        ],
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.RemoveRolesRequestBody](../../models/removerolesrequestbody.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.RemoveRolesResponse](../../models/removerolesresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrBadRequest          | 400                           | application/json              |
| models.ErrUnauthorized        | 401                           | application/json              |
| models.ErrForbidden           | 403                           | application/json              |
| models.ErrNotFound            | 404                           | application/json              |
| models.ErrConflict            | 409                           | application/json              |
| models.ErrPreconditionFailed  | 412                           | application/json              |
| models.ErrTooManyRequests     | 429                           | application/json              |
| models.ErrInternalServerError | 500                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |

## set_roles

### Example Usage

```python
from unkey_py import Unkey


with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.keys.set_roles(request={
        "key_id": "<id>",
        "roles": [
            {
                "id": "role_123",
            },
            {
                "name": "dns.record.create",
            },
            {
                "name": "dns.record.delete",
                "create": True,
            },
        ],
    })

    assert res.response_bodies is not None

    # Handle response
    print(res.response_bodies)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SetRolesRequestBody](../../models/setrolesrequestbody.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SetRolesResponse](../../models/setrolesresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrBadRequest          | 400                           | application/json              |
| models.ErrUnauthorized        | 401                           | application/json              |
| models.ErrForbidden           | 403                           | application/json              |
| models.ErrNotFound            | 404                           | application/json              |
| models.ErrConflict            | 409                           | application/json              |
| models.ErrPreconditionFailed  | 412                           | application/json              |
| models.ErrTooManyRequests     | 429                           | application/json              |
| models.ErrInternalServerError | 500                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |