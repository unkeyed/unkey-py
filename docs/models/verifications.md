# Verifications


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `time`                                               | *int*                                                | :heavy_check_mark:                                   | The timestamp of the usage data                      | 1620000000000                                        |
| `success`                                            | *int*                                                | :heavy_check_mark:                                   | The number of successful requests                    | 100                                                  |
| `rate_limited`                                       | *int*                                                | :heavy_check_mark:                                   | The number of requests that were rate limited        | 10                                                   |
| `usage_exceeded`                                     | *int*                                                | :heavy_check_mark:                                   | The number of requests that exceeded the usage limit | 0                                                    |