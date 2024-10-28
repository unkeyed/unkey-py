# RemoveRolesRequestBody


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `key_id`                                                       | *str*                                                          | :heavy_check_mark:                                             | The id of the key.                                             |                                                                |
| `roles`                                                        | List[[models.RemoveRolesRoles](../models/removerolesroles.md)] | :heavy_check_mark:                                             | The roles you want to remove from this key.                    | [<br/>{<br/>"id": "role_123"<br/>},<br/>{<br/>"name": "dns.record.create"<br/>}<br/>] |