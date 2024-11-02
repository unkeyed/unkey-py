# V1MigrationsEnqueueKeysRefill

Unkey enables you to refill verifications for each key at regular intervals.


## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `interval`                                                                                         | [models.V1MigrationsEnqueueKeysInterval](../models/v1migrationsenqueuekeysinterval.md)             | :heavy_check_mark:                                                                                 | Unkey will automatically refill verifications at the set interval.                                 |
| `amount`                                                                                           | *int*                                                                                              | :heavy_check_mark:                                                                                 | The number of verifications to refill for each occurrence is determined individually for each key. |
| `refill_day`                                                                                       | *Optional[float]*                                                                                  | :heavy_minus_sign:                                                                                 | The day verifications will refill each month, when interval is set to 'monthly'                    |