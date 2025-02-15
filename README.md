# unkey

Developer-friendly & type-safe Python SDK for Unkey's API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=unkey&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />

<!-- Start Summary [summary] -->
## Summary


<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [unkey](#unkey)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Pagination](#pagination)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Authentication](#authentication)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install unkey.py
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add unkey.py
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from unkey.py python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "unkey.py",
# ]
# ///

from unkey_py import Unkey

sdk = Unkey(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.liveness.check()

    assert res.object is not None

    # Handle response
    print(res.object)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from unkey_py import Unkey

async def main():
    async with Unkey(
        bearer_auth="UNKEY_ROOT_KEY",
    ) as unkey:

        res = await unkey.liveness.check_async()

        assert res.object is not None

        # Handle response
        print(res.object)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [analytics](docs/sdks/analytics/README.md)

* [get_verifications](docs/sdks/analytics/README.md#get_verifications)

### [apis](docs/sdks/apis/README.md)

* [get](docs/sdks/apis/README.md#get)
* [create](docs/sdks/apis/README.md#create)
* [list_keys](docs/sdks/apis/README.md#list_keys)
* [delete](docs/sdks/apis/README.md#delete)
* [delete_keys](docs/sdks/apis/README.md#delete_keys)

### [identities](docs/sdks/identities/README.md)

* [create](docs/sdks/identities/README.md#create)
* [get](docs/sdks/identities/README.md#get)
* [list](docs/sdks/identities/README.md#list)
* [update](docs/sdks/identities/README.md#update)
* [delete](docs/sdks/identities/README.md#delete)

### [keys](docs/sdks/keys/README.md)

* [get](docs/sdks/keys/README.md#get)
* [whoami](docs/sdks/keys/README.md#whoami)
* [delete](docs/sdks/keys/README.md#delete)
* [create](docs/sdks/keys/README.md#create)
* [verify](docs/sdks/keys/README.md#verify)
* [update](docs/sdks/keys/README.md#update)
* [update_remaining](docs/sdks/keys/README.md#update_remaining)
* [get_verifications](docs/sdks/keys/README.md#get_verifications)
* [add_permissions](docs/sdks/keys/README.md#add_permissions)
* [remove_permissions](docs/sdks/keys/README.md#remove_permissions)
* [set_permissions](docs/sdks/keys/README.md#set_permissions)
* [add_roles](docs/sdks/keys/README.md#add_roles)
* [remove_roles](docs/sdks/keys/README.md#remove_roles)
* [set_roles](docs/sdks/keys/README.md#set_roles)

### [liveness](docs/sdks/liveness/README.md)

* [check](docs/sdks/liveness/README.md#check)

### [migrations](docs/sdks/migrations/README.md)

* [create_keys](docs/sdks/migrations/README.md#create_keys)
* [enqueue](docs/sdks/migrations/README.md#enqueue)

### [permissions](docs/sdks/permissions/README.md)

* [create](docs/sdks/permissions/README.md#create)
* [delete](docs/sdks/permissions/README.md#delete)
* [get](docs/sdks/permissions/README.md#get)
* [list](docs/sdks/permissions/README.md#list)
* [create_role](docs/sdks/permissions/README.md#create_role)
* [delete_role](docs/sdks/permissions/README.md#delete_role)
* [get_role](docs/sdks/permissions/README.md#get_role)
* [list_roles](docs/sdks/permissions/README.md#list_roles)

### [ratelimit](docs/sdks/ratelimit/README.md)

* [set_override](docs/sdks/ratelimit/README.md#set_override)
* [list_overrides](docs/sdks/ratelimit/README.md#list_overrides)
* [get_override](docs/sdks/ratelimit/README.md#get_override)

### [ratelimits](docs/sdks/ratelimits/README.md)

* [limit](docs/sdks/ratelimits/README.md#limit)
* [delete_override](docs/sdks/ratelimits/README.md#delete_override)


</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Pagination [pagination] -->
## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
```python
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.identities.list()

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Pagination [pagination] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from unkey_py import Unkey
from unkey_py.utils import BackoffStrategy, RetryConfig

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.liveness.check(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res.object is not None

    # Handle response
    print(res.object)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from unkey_py import Unkey
from unkey_py.utils import BackoffStrategy, RetryConfig

with Unkey(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.liveness.check()

    assert res.object is not None

    # Handle response
    print(res.object)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `check_async` method may raise the following exceptions:

| Error Type                    | Status Code | Content Type     |
| ----------------------------- | ----------- | ---------------- |
| models.ErrBadRequest          | 400         | application/json |
| models.ErrUnauthorized        | 401         | application/json |
| models.ErrForbidden           | 403         | application/json |
| models.ErrNotFound            | 404         | application/json |
| models.ErrConflict            | 409         | application/json |
| models.ErrPreconditionFailed  | 412         | application/json |
| models.ErrTooManyRequests     | 429         | application/json |
| models.ErrInternalServerError | 500         | application/json |
| models.SDKError               | 4XX, 5XX    | \*/\*            |

### Example

```python
from unkey_py import Unkey, models

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:
    res = None
    try:

        res = unkey.liveness.check()

        assert res.object is not None

        # Handle response
        print(res.object)

    except models.ErrBadRequest as e:
        # handle e.data: models.ErrBadRequestData
        raise(e)
    except models.ErrUnauthorized as e:
        # handle e.data: models.ErrUnauthorizedData
        raise(e)
    except models.ErrForbidden as e:
        # handle e.data: models.ErrForbiddenData
        raise(e)
    except models.ErrNotFound as e:
        # handle e.data: models.ErrNotFoundData
        raise(e)
    except models.ErrConflict as e:
        # handle e.data: models.ErrConflictData
        raise(e)
    except models.ErrPreconditionFailed as e:
        # handle e.data: models.ErrPreconditionFailedData
        raise(e)
    except models.ErrTooManyRequests as e:
        # handle e.data: models.ErrTooManyRequestsData
        raise(e)
    except models.ErrInternalServerError as e:
        # handle e.data: models.ErrInternalServerErrorData
        raise(e)
    except models.SDKError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from unkey_py import Unkey

with Unkey(
    server_url="https://api.unkey.dev",
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.liveness.check()

    assert res.object is not None

    # Handle response
    print(res.object)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from unkey_py import Unkey
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Unkey(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from unkey_py import Unkey
from unkey_py.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Unkey(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type | Scheme      | Environment Variable |
| ------------- | ---- | ----------- | -------------------- |
| `bearer_auth` | http | HTTP Bearer | `UNKEY_BEARER_AUTH`  |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as unkey:

    res = unkey.liveness.check()

    assert res.object is not None

    # Handle response
    print(res.object)

```
<!-- End Authentication [security] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Unkey` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from unkey_py import Unkey
def main():
    with Unkey(
        bearer_auth="UNKEY_ROOT_KEY",
    ) as unkey:
        # Rest of application here...


# Or when using async:
async def amain():
    async with Unkey(
        bearer_auth="UNKEY_ROOT_KEY",
    ) as unkey:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from unkey_py import Unkey
import logging

logging.basicConfig(level=logging.DEBUG)
s = Unkey(debug_logger=logging.getLogger("unkey_py"))
```

You can also enable a default debug logger by setting an environment variable `UNKEY_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=unkey&utm_campaign=python)
