# DeleteAPIResponse


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `http_meta`                                                                                    | [models.HTTPMetadata](../models/httpmetadata.md)                                               | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `object`                                                                                       | [Optional[models.DeleteAPIResponseBody]](../models/deleteapiresponsebody.md)                   | :heavy_minus_sign:                                                                             | The api was successfully deleted, it may take up to 30s for this to take effect in all regions |