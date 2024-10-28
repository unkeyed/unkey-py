<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import os
from unkey import Unkey

s = Unkey(
    bearer_auth=os.getenv("UNKEY_BEARER_AUTH", ""),
)

res = s.liveness.check()

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
from unkey import Unkey

async def main():
    s = Unkey(
        bearer_auth=os.getenv("UNKEY_BEARER_AUTH", ""),
    )
    res = await s.liveness.check_async()
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->