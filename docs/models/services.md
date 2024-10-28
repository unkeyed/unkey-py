# Services


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  | Example                                      |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `metrics`                                    | *str*                                        | :heavy_check_mark:                           | The name of the connected metrics service    | AxiomMetrics                                 |
| `logger`                                     | *str*                                        | :heavy_check_mark:                           | The name of the connected logger service     | AxiomLogger or ConsoleLogger                 |
| `ratelimit`                                  | *str*                                        | :heavy_check_mark:                           | The name of the connected ratelimit service  |                                              |
| `usagelimit`                                 | *str*                                        | :heavy_check_mark:                           | The name of the connected usagelimit service |                                              |
| `analytics`                                  | *str*                                        | :heavy_check_mark:                           | The name of the connected analytics service  |                                              |