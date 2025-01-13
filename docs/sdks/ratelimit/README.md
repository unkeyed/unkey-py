# Ratelimit
(*ratelimit*)

## Overview

### Available Operations

* [set_override](#set_override)
* [list_overrides](#list_overrides)
* [get_override](#get_override)

## set_override

### Example Usage

```python
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.ratelimit.set_override(request={
        "identifier": "user_123",
        "limit": 10,
        "duration": 60000,
        "namespace_id": "rlns_1234",
        "namespace_name": "email.outbound",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.SetOverrideRequestBody](../../models/setoverriderequestbody.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.SetOverrideResponse](../../models/setoverrideresponse.md)**

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

## list_overrides

### Example Usage

```python
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.ratelimit.list_overrides(namespace_id="rlns_1234", namespace_name="email.outbound", limit=100)

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `namespace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | rlns_1234                                                           |
| `namespace_name`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | email.outbound                                                      |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 100                                                                 |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListOverridesResponse](../../models/listoverridesresponse.md)**

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

## get_override

### Example Usage

```python
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.ratelimit.get_override(identifier="user_123", namespace_id="rlns_1234", namespace_name="email.outbound")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `identifier`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | user_123                                                            |
| `namespace_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | rlns_1234                                                           |
| `namespace_name`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | email.outbound                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetOverrideResponse](../../models/getoverrideresponse.md)**

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