# Apis
(*apis*)

## Overview

### Available Operations

* [get](#get)
* [create](#create)
* [list_keys](#list_keys)
* [delete](#delete)
* [delete_keys](#delete_keys)

## get

### Example Usage

```python
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.apis.get(api_id="api_1234")

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | api_1234                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetAPIResponse](../../models/getapiresponse.md)**

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
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.apis.create(request={
        "name": "my-api",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CreateAPIRequestBody](../../models/createapirequestbody.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateAPIResponse](../../models/createapiresponse.md)**

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

## list_keys

### Example Usage

```python
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.apis.list_keys(request={
        "api_id": "api_1234",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ListKeysRequest](../../models/listkeysrequest.md)           | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListKeysResponse](../../models/listkeysresponse.md)**

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

    res = unkey.apis.delete(request={
        "api_id": "api_1234",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.DeleteAPIRequestBody](../../models/deleteapirequestbody.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteAPIResponse](../../models/deleteapiresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| models.ErrBadRequest          | 400                           | application/json              |
| models.ErrUnauthorized        | 401                           | application/json              |
| models.ErrForbidden           | 403                           | application/json              |
| models.ErrNotFound            | 404                           | application/json              |
| models.ErrConflict            | 409                           | application/json              |
| models.ErrPreconditionFailed  | 412                           | application/json              |
| models.ErrDeleteProtected     | 429                           | application/json              |
| models.ErrInternalServerError | 500                           | application/json              |
| models.SDKError               | 4XX, 5XX                      | \*/\*                         |

## delete_keys

### Example Usage

```python
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.apis.delete_keys(request={
        "api_id": "api_1234",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.DeleteKeysRequestBody](../../models/deletekeysrequestbody.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.DeleteKeysResponse](../../models/deletekeysresponse.md)**

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