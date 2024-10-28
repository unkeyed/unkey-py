# UpdateRemainingRequestBody


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       | Example                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `key_id`                                                          | *str*                                                             | :heavy_check_mark:                                                | The id of the key you want to modify                              | key_123                                                           |
| `op`                                                              | [models.Op](../models/op.md)                                      | :heavy_check_mark:                                                | The operation you want to perform on the remaining count          |                                                                   |
| `value`                                                           | *Nullable[int]*                                                   | :heavy_check_mark:                                                | The value you want to set, add or subtract the remaining count by | 1                                                                 |