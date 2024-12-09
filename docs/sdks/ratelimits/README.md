# Ratelimits
(*ratelimits*)

## Overview

### Available Operations

* [limit](#limit)
* [delete_override](#delete_override)

## limit

### Example Usage

```python
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as s:
    res = s.ratelimits.limit(request={
        "identifier": "user_123",
        "limit": 10,
        "duration": 60000,
        "namespace": "email.outbound",
        "cost": 2,
        "resources": [
            {
                "type": "organization",
                "id": "org_123",
                "name": "unkey",
            },
        ],
    })

    if res.object is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.LimitRequestBody](../../models/limitrequestbody.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LimitResponse](../../models/limitresponse.md)**

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

## delete_override

### Example Usage

```python
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as s:
    res = s.ratelimits.delete_override(request={
        "identifier": "user_123",
        "namespace_id": "rlns_1234",
        "namespace_name": "email.outbound",
    })

    if res.object is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.DeleteOverrideRequestBody](../../models/deleteoverriderequestbody.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.DeleteOverrideResponse](../../models/deleteoverrideresponse.md)**

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