# V1KeysVerifyKeyResponseRatelimit

The ratelimit configuration for this key. If this field is null or undefined, the key has no ratelimit.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `limit`                                                      | *int*                                                        | :heavy_check_mark:                                           | Maximum number of requests that can be made inside a window  | 10                                                           |
| `remaining`                                                  | *int*                                                        | :heavy_check_mark:                                           | Remaining requests after this verification                   | 9                                                            |
| `reset`                                                      | *int*                                                        | :heavy_check_mark:                                           | Unix timestamp in milliseconds when the ratelimit will reset | 3600000                                                      |