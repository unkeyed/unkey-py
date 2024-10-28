# Hash

Provide either `hash` or `plaintext`


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `value`                                                                                | *str*                                                                                  | :heavy_check_mark:                                                                     | The hashed and encoded key                                                             |
| `variant`                                                                              | [models.Variant](../models/variant.md)                                                 | :heavy_check_mark:                                                                     | The algorithm for hashing and encoding, currently only sha256 and base64 are supported |