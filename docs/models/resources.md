# Resources


## Fields

| Field                                   | Type                                    | Required                                | Description                             | Example                                 |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `type`                                  | *str*                                   | :heavy_check_mark:                      | The type of resource                    | organization                            |
| `id`                                    | *str*                                   | :heavy_check_mark:                      | The unique identifier for the resource  | org_123                                 |
| `name`                                  | *Optional[str]*                         | :heavy_minus_sign:                      | A human readable name for this resource | unkey                                   |
| `meta`                                  | Dict[str, *Nullable[Any]*]              | :heavy_minus_sign:                      | Attach any metadata to this resources   |                                         |