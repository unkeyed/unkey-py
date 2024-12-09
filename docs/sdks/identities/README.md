# Identities
(*identities*)

## Overview

### Available Operations

* [create](#create)
* [get](#get)
* [list](#list)
* [update](#update)
* [delete](#delete)

## create

### Example Usage

```python
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as s:
    res = s.identities.create(request={
        "external_id": "user_123",
        "ratelimits": [
            {
                "name": "tokens",
                "limit": 10,
                "duration": 1000,
            },
            {
                "name": "tokens",
                "limit": 10,
                "duration": 1000,
            },
        ],
    })

    if res.object is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.CreateIdentityRequestBody](../../models/createidentityrequestbody.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.CreateIdentityResponse](../../models/createidentityresponse.md)**

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

## get

### Example Usage

```python
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as s:
    res = s.identities.get(identity_id="id_1234", external_id="id_1234")

    if res.object is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `identity_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | id_1234                                                             |
| `external_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | id_1234                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetIdentityResponse](../../models/getidentityresponse.md)**

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

## list

### Example Usage

```python
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as s:
    res = s.identities.list(limit=100)

    if res.object is not None:
        while True:
            # handle items

            res = res.next()
            if res is None:
                break

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `environment`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 100                                                                 |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListIdentitiesResponse](../../models/listidentitiesresponse.md)**

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

## update

### Example Usage

```python
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as s:
    res = s.identities.update(request={
        "identity_id": "id_1234",
        "external_id": "user_1234",
        "ratelimits": [
            {
                "name": "tokens",
                "limit": 10,
                "duration": 1000,
            },
            {
                "name": "tokens",
                "limit": 10,
                "duration": 1000,
            },
            {
                "name": "tokens",
                "limit": 10,
                "duration": 1000,
            },
        ],
    })

    if res.object is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.UpdateIdentityRequestBody](../../models/updateidentityrequestbody.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.UpdateIdentityResponse](../../models/updateidentityresponse.md)**

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

## delete

### Example Usage

```python
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as s:
    res = s.identities.delete(request={
        "identity_id": "id_1234",
    })

    if res.object is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.DeleteIdentityRequestBody](../../models/deleteidentityrequestbody.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.DeleteIdentityResponse](../../models/deleteidentityresponse.md)**

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