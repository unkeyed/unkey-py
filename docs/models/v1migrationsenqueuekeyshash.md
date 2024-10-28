# V1MigrationsEnqueueKeysHash

Provide either `hash` or `plaintext`


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `value`                                                                                | *str*                                                                                  | :heavy_check_mark:                                                                     | The hashed and encoded key                                                             |
| `variant`                                                                              | [models.V1MigrationsEnqueueKeysVariant](../models/v1migrationsenqueuekeysvariant.md)   | :heavy_check_mark:                                                                     | The algorithm for hashing and encoding, currently only sha256 and base64 are supported |