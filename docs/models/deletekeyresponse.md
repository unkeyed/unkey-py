# DeleteKeyResponse


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `http_meta`                                                                                    | [models.HTTPMetadata](../models/httpmetadata.md)                                               | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `object`                                                                                       | [Optional[models.DeleteKeyResponseBody]](../models/deletekeyresponsebody.md)                   | :heavy_minus_sign:                                                                             | The key was successfully revoked, it may take up to 30s for this to take effect in all regions |