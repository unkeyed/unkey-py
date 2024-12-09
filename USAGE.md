<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from unkey_py import Unkey

with Unkey(
    bearer_auth="UNKEY_ROOT_KEY",
) as s:
    res = s.liveness.check()

    if res.object is not None:
        # handle response
        pass
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
    ) as s:
        res = await s.liveness.check_async()

        if res.object is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->