# ListKeysRequest


## Fields

| Field                    | Type                     | Required                 | Description              | Example                  |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `api_id`                 | *str*                    | :heavy_check_mark:       | N/A                      | api_1234                 |
| `limit`                  | *Optional[int]*          | :heavy_minus_sign:       | N/A                      | 100                      |
| `cursor`                 | *Optional[str]*          | :heavy_minus_sign:       | N/A                      |                          |
| `owner_id`               | *Optional[str]*          | :heavy_minus_sign:       | N/A                      |                          |
| `external_id`            | *Optional[str]*          | :heavy_minus_sign:       | N/A                      |                          |
| `decrypt`                | *OptionalNullable[bool]* | :heavy_minus_sign:       | N/A                      |                          |
| `revalidate_keys_cache`  | *OptionalNullable[bool]* | :heavy_minus_sign:       | N/A                      |                          |