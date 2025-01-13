<!-- Start SDK Example Usage [usage] -->
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