# GATT Server

GATT Server（Generic Attribute Profile）提供蓝牙低功耗（Bluetooth Low Energy）服务端的属性服务管理能力，支持服务、特征与描述符的注册与同步注册，服务的启动、停止、删除，以及对客户端读写请求的响应、通知 (Notification) 与指示 (Indication) 的发送，并通过回调机制向应用层上报服务注册、特征注册、读写请求、MTU（Maximum Transmission Unit）变化与指示确认等事件。

**模块公共头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [gatts_register_server](#gatts_register_server) | 注册 GATT 服务端，分配服务端 ID |
| [gatts_unregister_server](#gatts_unregister_server) | 注销 GATT 服务端 |
| [gatts_add_service](#gatts_add_service) | 异步添加一个 GATT 服务 |
| [gatts_add_characteristic](#gatts_add_characteristic) | 异步添加一个 GATT 特征 |
| [gatts_add_descriptor](#gatts_add_descriptor) | 异步添加一个 GATT 特征描述符 |
| [gatts_add_service_sync](#gatts_add_service_sync) | 同步添加一个 GATT 服务，返回服务句柄 |
| [gatts_add_characteristic_sync](#gatts_add_characteristic_sync) | 同步添加一个 GATT 特征，返回特征句柄 |
| [gatts_add_descriptor_sync](#gatts_add_descriptor_sync) | 同步添加一个 GATT 特征描述符，返回描述符句柄 |
| [gatts_start_service](#gatts_start_service) | 启动一个 GATT 服务 |
| [gatts_stop_service](#gatts_stop_service) | 停止一个 GATT 服务 |
| [gatts_delete_service](#gatts_delete_service) | 删除一个 GATT 服务 |
| [gatts_delete_all_services](#gatts_delete_all_services) | 删除指定服务端的全部 GATT 服务 |
| [gatts_send_response](#gatts_send_response) | 对需要用户回复的读/写请求发送响应 |
| [gatts_notify_indicate](#gatts_notify_indicate) | 向对端发送通知或指示 |
| [gatts_notify_indicate_by_uuid](#gatts_notify_indicate_by_uuid) | 通过特征 UUID 向对端发送通知或指示 |
| [gatts_set_mtu_size](#gatts_set_mtu_size) | 在连接前设置服务端接收 MTU 大小 |
| [gatts_register_callbacks](#gatts_register_callbacks) | 注册 GATT 服务端回调函数 |
| [gatts_exchange_mtu_req](#gatts_exchange_mtu_req) | 发送交换 MTU 请求 |

## Functions

### gatts_register_server <a id="gatts_register_server"></a>

```c
errcode_t gatts_register_server(bt_uuid_t *app_uuid, uint8_t *server_id)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 注册一个 GATT 服务端，向上层应用分配唯一的服务端 ID。
- 服务端 ID 是后续添加服务、特征、描述符及收发数据等操作的关键标识。
- 成功注册后服务端进入可用状态，可继续调用服务/特征注册相关接口。

**前置条件**

- 调用时序约束：调用本模块服务端相关接口前必须先调用本接口完成服务端注册。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| app_uuid | bt_uuid_t * | 上层应用 UUID，用于标识当前应用 | 不为 NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| server_id | uint8_t * | 成功注册后分配的服务端 ID，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功注册 | 服务端注册成功 |
| Other | 其他错误码，参考 errcode_t | 注册失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`
- `src/application/samples/bt/ble/ble_wifi_cfg_server/src/ble_wifi_cfg_server.c`

### gatts_unregister_server <a id="gatts_unregister_server"></a>

```c
errcode_t gatts_unregister_server(uint8_t server_id)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 注销已注册的 GATT 服务端，释放对应服务端 ID 及其关联资源。
- 注销后该服务端 ID 不再有效，禁止继续使用该 ID 进行后续操作。
- 与 `gatts_register_server` 配对使用，用于服务端生命周期的收尾。

**前置条件**

- 调用时序约束：必须在 `gatts_register_server` 成功返回后再调用本接口。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 已注册的服务端 ID | 由 gatts_register_server 分配的有效 ID |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功注销 | 服务端注销成功 |
| Other | 其他错误码，参考 errcode_t | 注销失败 |

### gatts_add_service <a id="gatts_add_service"></a>

```c
errcode_t gatts_add_service(uint8_t server_id, bt_uuid_t *service_uuid, bool is_primary)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 向指定服务端异步添加一个 GATT 服务。
- 通过 `is_primary` 指定该服务为主服务或次服务。
- 服务添加结果及服务句柄通过 `gatts_add_service_callback` 回调异步返回。

**前置条件**

- 调用时序约束：必须在 `gatts_register_server` 成功返回后调用，且需先通过 `gatts_register_callbacks` 注册服务添加回调以接收服务句柄。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 由 gatts_register_server 分配的有效 ID |
| service_uuid | bt_uuid_t * | 服务的 UUID | 不为 NULL |
| is_primary | bool | 是否为主服务 | true；<br>false。 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 请求成功 | 添加服务请求成功发起，服务句柄将在回调中返回 |
| Other | 其他错误码，参考 errcode_t | 添加服务请求失败 |

### gatts_add_characteristic <a id="gatts_add_characteristic"></a>

```c
errcode_t gatts_add_characteristic(uint8_t server_id, uint16_t service_handle, gatts_add_chara_info_t *character)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 向指定服务下异步添加一个 GATT 特征。
- 特征信息包含特征 UUID、权限、特性、初始值等，由 `gatts_add_chara_info_t` 描述。
- 特征添加结果及特征句柄通过 `gatts_add_characteristic_callback` 回调异步返回。

**前置条件**

- 调用时序约束：必须在对应服务添加完成（`gatts_add_service` 回调返回服务句柄）后调用，且需先注册特征添加回调以接收特征句柄。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 由 gatts_register_server 分配的有效 ID |
| service_handle | uint16_t | 所属服务的属性句柄 | gatts_add_service 回调返回的有效服务句柄 |
| character | [gatts_add_chara_info_t](#struct_gatts_add_chara_info_t) * | 特征信息 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 请求成功 | 添加特征请求成功发起，特征句柄将在回调中返回 |
| Other | 其他错误码，参考 errcode_t | 添加特征请求失败 |

### gatts_add_descriptor <a id="gatts_add_descriptor"></a>

```c
errcode_t gatts_add_descriptor(uint8_t server_id, uint16_t service_handle, gatts_add_desc_info_t *descriptor)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 向指定服务下异步添加一个 GATT 特征描述符。
- 描述符信息包含描述符 UUID、权限、初始值等，由 `gatts_add_desc_info_t` 描述。
- 描述符添加结果及描述符句柄通过 `gatts_add_descriptor_callback` 回调异步返回。

**前置条件**

- 调用时序约束：必须在对应服务添加完成后调用，且需先注册描述符添加回调以接收描述符句柄。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 由 gatts_register_server 分配的有效 ID |
| service_handle | uint16_t | 所属服务的属性句柄 | gatts_add_service 回调返回的有效服务句柄 |
| descriptor | [gatts_add_desc_info_t](#struct_gatts_add_desc_info_t) * | 特征描述符信息 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 请求成功 | 添加描述符请求成功发起，描述符句柄将在回调中返回 |
| Other | 其他错误码，参考 errcode_t | 添加描述符请求失败 |

### gatts_add_service_sync <a id="gatts_add_service_sync"></a>

```c
errcode_t gatts_add_service_sync(uint8_t server_id, bt_uuid_t *service_uuid, bool is_primary, uint16_t *handle)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 同步方式向指定服务端添加一个 GATT 服务。
- 通过 `is_primary` 指定该服务为主服务或次服务。
- 服务句柄通过出参 `handle` 同步返回，调用方可直接获取结果。

**前置条件**

- 调用时序约束：必须在 `gatts_register_server` 成功返回后调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 由 gatts_register_server 分配的有效 ID |
| service_uuid | bt_uuid_t * | 服务的 UUID | 不为 NULL |
| is_primary | bool | 是否为主服务 | true；<br>false。 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| handle | uint16_t * | 添加成功后的服务属性句柄，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 添加成功 | 服务添加成功，服务句柄通过 handle 返回 |
| Other | 其他错误码，参考 errcode_t | 添加服务失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`
- `src/application/samples/bt/ble/ble_wifi_cfg_server/src/ble_wifi_cfg_server.c`

### gatts_add_characteristic_sync <a id="gatts_add_characteristic_sync"></a>

```c
errcode_t gatts_add_characteristic_sync(uint8_t server_id, uint16_t service_handle, gatts_add_chara_info_t *character, gatts_add_character_result_t *result)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 同步方式向指定服务下添加一个 GATT 特征。
- 特征信息由 `gatts_add_chara_info_t` 描述，包含特征 UUID、权限、特性、初始值等。
- 特征句柄信息通过出参 `result` 同步返回。

**前置条件**

- 调用时序约束：必须在对应服务添加完成（已获取服务句柄）后调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 由 gatts_register_server 分配的有效 ID |
| service_handle | uint16_t | 所属服务的属性句柄 | gatts_add_service；<br>gatts_add_service_sync 返回的有效服务句柄。 |
| character | [gatts_add_chara_info_t](#struct_gatts_add_chara_info_t) * | 特征信息 | 不为 NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| result | [gatts_add_character_result_t](#struct_gatts_add_character_result_t) * | 特征句柄信息，包含特征声明句柄与特征值句柄，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 添加成功 | 特征添加成功，特征句柄通过 result 返回 |
| Other | 其他错误码，参考 errcode_t | 添加特征失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`
- `src/application/samples/bt/ble/ble_wifi_cfg_server/src/ble_wifi_cfg_server.c`

### gatts_add_descriptor_sync <a id="gatts_add_descriptor_sync"></a>

```c
errcode_t gatts_add_descriptor_sync(uint8_t server_id, uint16_t service_handle, gatts_add_desc_info_t *descriptor, uint16_t *handle)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 同步方式向指定服务下添加一个 GATT 特征描述符。
- 描述符信息由 `gatts_add_desc_info_t` 描述，包含描述符 UUID、权限、初始值等。
- 描述符句柄通过出参 `handle` 同步返回。

**前置条件**

- 调用时序约束：必须在对应服务添加完成（已获取服务句柄）后调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 由 gatts_register_server 分配的有效 ID |
| service_handle | uint16_t | 所属服务的属性句柄 | gatts_add_service；<br>gatts_add_service_sync 返回的有效服务句柄。 |
| descriptor | [gatts_add_desc_info_t](#struct_gatts_add_desc_info_t) * | 特征描述符信息 | 不为 NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| handle | uint16_t * | 添加成功后的描述符属性句柄，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 添加成功 | 描述符添加成功，描述符句柄通过 handle 返回 |
| Other | 其他错误码，参考 errcode_t | 添加描述符失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`
- `src/application/samples/bt/ble/ble_wifi_cfg_server/src/ble_wifi_cfg_server.c`

### gatts_start_service <a id="gatts_start_service"></a>

```c
errcode_t gatts_start_service(uint8_t server_id, uint16_t service_handle)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 启动指定服务端下的一个 GATT 服务。
- 启动后该服务对外可见，可被客户端发现与访问。
- 服务启动结果通过 `gatts_start_service_callback` 回调异步返回。

**前置条件**

- 调用时序约束：必须在对应服务及其下的特征、描述符全部添加完成后调用，且需先注册启动服务回调以接收启动结果。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 由 gatts_register_server 分配的有效 ID |
| service_handle | uint16_t | 待启动服务的属性句柄 | gatts_add_service；<br>gatts_add_service_sync 返回的有效服务句柄。 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 请求成功 | 启动服务请求成功发起，启动结果将在回调中返回 |
| Other | 其他错误码，参考 errcode_t | 启动服务请求失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`
- `src/application/samples/bt/ble/ble_wifi_cfg_server/src/ble_wifi_cfg_server.c`

### gatts_stop_service <a id="gatts_stop_service"></a>

```c
errcode_t gatts_stop_service(uint8_t server_id, uint16_t service_handle)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 停止指定服务端下的一个已启动 GATT 服务。
- 停止后该服务对外不可见，客户端无法继续发现与访问。
- 服务停止结果通过 `gatts_stop_service_callback` 回调异步返回。

**前置条件**

- 调用时序约束：必须在对应服务已通过 `gatts_start_service` 启动后调用，且需先注册停止服务回调以接收停止结果。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 由 gatts_register_server 分配的有效 ID |
| service_handle | uint16_t | 待停止服务的属性句柄 | 已启动服务的有效服务句柄 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 请求成功 | 停止服务请求成功发起，停止结果将在回调中返回 |
| Other | 其他错误码，参考 errcode_t | 停止服务请求失败 |

### gatts_delete_service <a id="gatts_delete_service"></a>

```c
errcode_t gatts_delete_service(uint8_t server_id, uint16_t service_handle)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 删除指定服务端下的一个 GATT 服务及其下全部特征与描述符。
- 删除后该服务句柄失效，对应属性资源被释放。
- 服务删除结果通过 `gatts_delete_service_callback` 回调异步返回。

**前置条件**

- 调用时序约束：建议在服务已停止后调用，且需先注册删除服务回调以接收删除结果。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 由 gatts_register_server 分配的有效 ID |
| service_handle | uint16_t | 待删除服务的属性句柄 | 有效服务句柄 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 请求成功 | 删除服务请求成功发起，删除结果将在回调中返回 |
| Other | 其他错误码，参考 errcode_t | 删除服务请求失败 |

### gatts_delete_all_services <a id="gatts_delete_all_services"></a>

```c
errcode_t gatts_delete_all_services(uint8_t server_id)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 删除指定服务端下的全部 GATT 服务及其下全部特征与描述符。
- 删除后该服务端的所有服务句柄失效，对应属性资源被释放。
- 删除结果通过 `gatts_delete_service_callback` 回调异步返回。

**前置条件**

- 调用时序约束：必须在 `gatts_register_server` 成功返回后调用，且需先注册删除服务回调以接收删除结果。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 由 gatts_register_server 分配的有效 ID |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 请求成功 | 删除全部服务请求成功发起，删除结果将在回调中返回 |
| Other | 其他错误码，参考 errcode_t | 删除全部服务请求失败 |

### gatts_send_response <a id="gatts_send_response"></a>

```c
errcode_t gatts_send_response(uint8_t server_id, uint16_t conn_id, gatts_send_rsp_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 当收到需要用户回复响应的读/写请求时，向对端发送响应。
- 响应参数由 `gatts_send_rsp_t` 描述，包含请求 ID、状态码、偏移、响应数据等。
- 与 `gatts_read_request_callback`、`gatts_write_request_callback` 回调配合使用。

**前置条件**

- 调用时序约束：必须在收到读/写请求回调（且该回调中 `need_rsp` 为真）后调用，以响应对应请求。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 由 gatts_register_server 分配的有效 ID |
| conn_id | uint16_t | 连接 ID | 有效连接 ID |
| param | [gatts_send_rsp_t](#struct_gatts_send_rsp_t) * | 响应参数 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功发送 | 响应发送成功 |
| Other | 其他错误码，参考 errcode_t | 响应发送失败 |

### gatts_notify_indicate <a id="gatts_notify_indicate"></a>

```c
errcode_t gatts_notify_indicate(uint8_t server_id, uint16_t conn_id, gatts_ntf_ind_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 向对端设备发送通知或指示。
- 发送参数由 `gatts_ntf_ind_t` 描述，包含属性句柄、数据长度与数据。
- 具体发送状态（通知或指示）取决于特征描述符：客户端特征配置的值。

**前置条件**

- 调用时序约束：必须在对应服务已启动、连接已建立后调用，且目标特征的客户端特征配置描述符已使能对应的通知或指示。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 由 gatts_register_server 分配的有效 ID |
| conn_id | uint16_t | 连接 ID | 有效连接 ID |
| param | [gatts_ntf_ind_t](#struct_gatts_ntf_ind_t) * | 通知或指示参数 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功发送 | 通知/指示发送成功 |
| Other | 其他错误码，参考 errcode_t | 通知/指示发送失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`
- `src/application/samples/bt/ble/ble_wifi_cfg_server/src/ble_wifi_cfg_server.c`

### gatts_notify_indicate_by_uuid <a id="gatts_notify_indicate_by_uuid"></a>

```c
errcode_t gatts_notify_indicate_by_uuid(uint8_t server_id, uint16_t conn_id, gatts_ntf_ind_by_uuid_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 通过特征 UUID 向对端设备发送通知或指示。
- 发送参数由 `gatts_ntf_ind_by_uuid_t` 描述，包含特征 UUID、起止句柄范围、数据长度与数据。
- 具体发送状态取决于客户端特征配置描述符的值：0 不允许通知和指示，1 允许通知，2 允许指示。

**前置条件**

- 调用时序约束：必须在对应服务已启动、连接已建立后调用，且目标特征的客户端特征配置描述符已配置为允许对应的通知或指示。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 由 gatts_register_server 分配的有效 ID |
| conn_id | uint16_t | 连接 ID | 有效连接 ID |
| param | [gatts_ntf_ind_by_uuid_t](#struct_gatts_ntf_ind_by_uuid_t) * | 通知或指示参数 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功发送 | 通过 UUID 发送通知/指示成功 |
| Other | 其他错误码，参考 errcode_t | 通过 UUID 发送通知/指示失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`
- `src/application/samples/bt/ble/ble_wifi_cfg_server/src/ble_wifi_cfg_server.c`

### gatts_set_mtu_size <a id="gatts_set_mtu_size"></a>

```c
errcode_t gatts_set_mtu_size(uint8_t server_id, uint16_t mtu_size)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 在连接建立之前设置服务端接收 MTU 大小。
- 设置的 MTU 大小影响后续连接建立后的数据收发最大长度。

**前置条件**

- 调用时序约束：必须在 `gatts_register_server` 成功返回后、连接建立之前调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 由 gatts_register_server 分配的有效 ID |
| mtu_size | uint16_t | 服务端接收 MTU 大小 | [SDK_BLE_MTU_MIN](#SDK_BLE_MTU_MIN)：23 ~ [SDK_BLE_MTU_MAX](#SDK_BLE_MTU_MAX)：517 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功设置 | MTU 大小设置成功 |
| Other | 其他错误码，参考 errcode_t | MTU 大小设置失败 |

### gatts_register_callbacks <a id="gatts_register_callbacks"></a>

```c
errcode_t gatts_register_callbacks(gatts_callbacks_t *func)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 注册 GATT 服务端回调函数集合。
- 回调集合由 `gatts_callbacks_t` 描述，覆盖服务/特征/描述符注册结果、读写请求、MTU 变化、指示确认等事件。
- 注册后相关事件将通过所注册的回调异步通知应用层。

**前置条件**

- 调用时序约束：建议在 `gatts_register_server` 之前或之后、但在发起任何会产生回调的操作（如添加服务、启动服务）之前调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func | [gatts_callbacks_t](#struct_gatts_callbacks_t) * | 回调函数集合 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功注册 | 回调函数注册成功 |
| Other | 其他错误码，参考 errcode_t | 回调函数注册失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`
- `src/application/samples/bt/ble/ble_wifi_cfg_server/src/ble_wifi_cfg_server.c`

### gatts_exchange_mtu_req <a id="gatts_exchange_mtu_req"></a>

```c
errcode_t gatts_exchange_mtu_req(uint16_t conn_id, uint16_t mtu_size)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_server.h"
```

**功能说明**

- 向对端发送交换 MTU 请求，协商连接的 MTU 大小。
- 协商结果通过 `gatts_mtu_changed_callback` 回调异步通知应用层。

**前置条件**

- 调用时序约束：必须在连接已建立后调用，且需先注册 MTU 变化回调以接收协商结果。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| conn_id | uint16_t | 连接 ID | 有效连接 ID |
| mtu_size | uint16_t | 服务端接收 MTU | [SDK_BLE_MTU_MIN](#SDK_BLE_MTU_MIN)：23 ~ [SDK_BLE_MTU_MAX](#SDK_BLE_MTU_MAX)：517 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 请求成功 | 交换 MTU 请求发送成功 |
| Other | 其他错误码，参考 errcode_t | 交换 MTU 请求发送失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`

## Type definitions

### errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块全部对外接口的返回值类型，表示接口执行结果。`ERRCODE_SUCC` 表示成功，其余值表示失败，具体错误码见 SDK 公共 `errcode.h`。

### gatts_add_service_callback <a id="gatts_add_service_callback"></a>

```c
typedef void (*gatts_add_service_callback)(uint8_t server_id, bt_uuid_t *uuid, uint16_t handle, errcode_t status);
```

**使用说明**

服务添加完成的回调函数指针类型。回调说明：在服务添加完成时由 BTS 上下文异步调用；参数 `server_id` 为服务端 ID，`uuid` 为服务 UUID，`handle` 为服务属性句柄，`status` 为执行结果错误码；该回调运行于 BTS 线程，不能阻塞或长时间等待。

### gatts_add_characteristic_callback <a id="gatts_add_characteristic_callback"></a>

```c
typedef void (*gatts_add_characteristic_callback)(uint8_t server_id, bt_uuid_t *uuid, uint16_t service_handle,
    gatts_add_character_result_t *result, errcode_t status);
```

**使用说明**

特征添加完成的回调函数指针类型。回调说明：在特征添加完成时由 BTS 上下文异步调用；参数 `server_id` 为服务端 ID，`uuid` 为特征 UUID，`service_handle` 为所属服务属性句柄，`result` 为特征句柄信息，`status` 为执行结果错误码；该回调运行于 BTS 线程，不能阻塞或长时间等待。

### gatts_add_descriptor_callback <a id="gatts_add_descriptor_callback"></a>

```c
typedef void (*gatts_add_descriptor_callback)(uint8_t server_id, bt_uuid_t *uuid, uint16_t service_handle,
    uint16_t handle, errcode_t status);
```

**使用说明**

特征描述符添加完成的回调函数指针类型。回调说明：在特征描述符添加完成时由 BTS 上下文异步调用；参数 `server_id` 为服务端 ID，`uuid` 为特征 UUID，`service_handle` 为所属服务属性句柄，`handle` 为描述符属性句柄，`status` 为执行结果错误码；该回调运行于 BTS 线程，不能阻塞或长时间等待。

### gatts_start_service_callback <a id="gatts_start_service_callback"></a>

```c
typedef void (*gatts_start_service_callback)(uint8_t server_id, uint16_t handle, errcode_t status);
```

**使用说明**

服务启动完成的回调函数指针类型。回调说明：在服务启动完成时由 BTS 上下文异步调用；参数 `server_id` 为服务端 ID，`handle` 为服务属性句柄，`status` 为执行结果错误码；该回调运行于 BTS 线程，不能阻塞或长时间等待。

### gatts_stop_service_callback <a id="gatts_stop_service_callback"></a>

```c
typedef void (*gatts_stop_service_callback)(uint8_t server_id, uint16_t handle, errcode_t status);
```

**使用说明**

服务停止完成的回调函数指针类型。回调说明：在服务停止完成时由 BTS 上下文异步调用；参数 `server_id` 为服务端 ID，`handle` 为服务属性句柄，`status` 为执行结果错误码；该回调运行于 BTS 线程，不能阻塞或长时间等待。

### gatts_delete_service_callback <a id="gatts_delete_service_callback"></a>

```c
typedef void (*gatts_delete_service_callback)(uint8_t server_id, errcode_t status);
```

**使用说明**

服务删除完成的回调函数指针类型。回调说明：在服务删除完成时由 BTS 上下文异步调用；参数 `server_id` 为服务端 ID，`status` 为执行结果错误码；该回调运行于 BTS 线程，不能阻塞或长时间等待。

### gatts_read_request_callback <a id="gatts_read_request_callback"></a>

```c
typedef void (*gatts_read_request_callback)(uint8_t server_id, uint16_t conn_id, gatts_req_read_cb_t *read_cb_para,
    errcode_t status);
```

**使用说明**

收到远端读请求的回调函数指针类型。回调说明：在收到远端读请求时由 BTS 上下文异步调用；参数 `server_id` 为服务端 ID，`conn_id` 为连接 ID，`read_cb_para` 为读请求参数，`status` 为执行结果错误码；若 `read_cb_para` 中 `need_rsp` 为真，应用层需通过 `gatts_send_response` 发送响应；该回调运行于 BTS 线程，不能阻塞或长时间等待。

### gatts_write_request_callback <a id="gatts_write_request_callback"></a>

```c
typedef void (*gatts_write_request_callback)(uint8_t server_id, uint16_t conn_id, gatts_req_write_cb_t *write_cb_para,
    errcode_t status);
```

**使用说明**

收到远端写请求的回调函数指针类型。回调说明：在收到远端写请求时由 BTS 上下文异步调用；参数 `server_id` 为服务端 ID，`conn_id` 为连接 ID，`write_cb_para` 为写请求参数，`status` 为执行结果错误码；若 `write_cb_para` 中 `need_rsp` 为真，应用层需通过 `gatts_send_response` 发送响应；该回调运行于 BTS 线程，不能阻塞或长时间等待。

### gatts_mtu_changed_callback <a id="gatts_mtu_changed_callback"></a>

```c
typedef void (*gatts_mtu_changed_callback)(uint8_t server_id, uint16_t conn_id, uint16_t mtu_size, errcode_t status);
```

**使用说明**

MTU 大小更新的回调函数指针类型。回调说明：在连接 MTU 协商完成或 MTU 大小变化时由 BTS 上下文异步调用；参数 `server_id` 为服务端 ID，`conn_id` 为连接 ID，`mtu_size` 为协商后的 MTU 大小，`status` 为执行结果错误码；该回调运行于 BTS 线程，不能阻塞或长时间等待。

### gatts_indication_confirm_callback <a id="gatts_indication_confirm_callback"></a>

```c
typedef void (*gatts_indication_confirm_callback)(uint8_t server_id, uint16_t conn_id, errcode_t status);
```

**使用说明**

收到对端指示确认（Indication Confirm）的回调函数指针类型。回调说明：在对端确认收到指示时由 BTS 上下文异步调用；参数 `server_id` 为服务端 ID，`conn_id` 为连接 ID，`status` 为执行结果错误码；该回调运行于 BTS 线程，不能阻塞或长时间等待。

## Structures

### gatts_add_chara_info_t <a id="struct_gatts_add_chara_info_t"></a>

```c
typedef struct {
    bt_uuid_t chara_uuid;   /*!< UUID of GATT characteristic. */
    uint8_t permissions;    /*!< Characteristic permissions, { gatt_attribute_permission_t }. */
    uint8_t properties;    /*!< Characteristic properties, { gatt_characteristic_property_t }. */
    uint16_t value_len;     /*!< Length of reponse data. */
    uint8_t *value;         /*!< Reponse data. */
} gatts_add_chara_info_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| chara_uuid | bt_uuid_t | GATT 特征 UUID |
| permissions | uint8_t | 特征权限，取值参考 gatt_attribute_permission_t |
| properties | uint8_t | 特征特性，取值参考 gatt_characteristic_property_t |
| value_len | uint16_t | 响应的数据长度 |
| value | uint8_t * | 响应的数据 |

### gatts_add_desc_info_t <a id="struct_gatts_add_desc_info_t"></a>

```c
typedef struct {
    bt_uuid_t desc_uuid;   /*!< UUID of GATT descriptor. */
    uint8_t permissions;   /*!< Descriptor permissions, { gatt_attribute_permission_t }. */
    uint16_t value_len;    /*!< Length of reponse data. */
    uint8_t *value;        /*!< Reponse data. */
} gatts_add_desc_info_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| desc_uuid | bt_uuid_t | GATT 描述符 UUID |
| permissions | uint8_t | 描述符权限，取值参考 gatt_attribute_permission_t |
| value_len | uint16_t | 响应的数据长度 |
| value | uint8_t * | 响应的数据 |

### gatts_req_read_cb_t <a id="struct_gatts_req_read_cb_t"></a>

```c
typedef struct {
    uint16_t request_id;  /*!< Request id. */
    uint16_t handle;      /*!< Attribute handle of the read request. */
    uint16_t offset;      /*!< Offset of the read request in bytes. */
    bool need_rsp;        /*!< Whether response is needed. */
    bool need_authorize;  /*!< Whether authorization is needed. */
    bool is_long;         /*!< Whether request is Long Read. */
} gatts_req_read_cb_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| request_id | uint16_t | 请求 ID |
| handle | uint16_t | 请求读的属性句柄 |
| offset | uint16_t | 请求读的字节偏移 |
| need_rsp | bool | 是否需要发送响应 |
| need_authorize | bool | 是否需要授权 |
| is_long | bool | 请求是否是读长特征 |

### gatts_req_write_cb_t <a id="struct_gatts_req_write_cb_t"></a>

```c
typedef struct {
    uint16_t request_id;  /*!< Request id. */
    uint16_t handle;      /*!< Attribute handle of the write request. */
    uint16_t offset;      /*!< Offset of the write request in bytes. */
    bool need_rsp;        /*!< Whether response is needed. */
    bool need_authorize;  /*!< Whether authorization is needed. */
    bool is_prep;         /*!< Whether request is Prepare Write. */
    uint16_t length;      /*!< Length of write request data. */
    uint8_t *value;       /*!< Write request data. */
} gatts_req_write_cb_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| request_id | uint16_t | 请求 ID |
| handle | uint16_t | 请求写的属性句柄 |
| offset | uint16_t | 请求写的字节偏移 |
| need_rsp | bool | 是否需要发送响应 |
| need_authorize | bool | 是否需要授权 |
| is_prep | bool | 请求是否是准备写 |
| length | uint16_t | 请求写的数据长度 |
| value | uint8_t * | 请求写的数据 |

### gatts_send_rsp_t <a id="struct_gatts_send_rsp_t"></a>

```c
typedef struct {
    uint16_t request_id; /*!< Request ID. */
    uint8_t status;      /*!< Status code of read/write, { gatt_status_t }. */
    uint16_t offset;     /*!< Offset. */
    uint16_t value_len;  /*!< Length of reponse data. */
    uint8_t *value;      /*!< Reponse data. */
} gatts_send_rsp_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| request_id | uint16_t | 请求 ID |
| status | uint8_t | 读写结果的状态，取值参考 gatt_status_t |
| offset | uint16_t | 属性偏移 |
| value_len | uint16_t | 响应的数据长度 |
| value | uint8_t * | 响应的数据 |

### gatts_ntf_ind_t <a id="struct_gatts_ntf_ind_t"></a>

```c
typedef struct {
    uint16_t attr_handle; /*!< Attribute handle. */
    uint16_t value_len;   /*!< Length of notification/indication data. */
    uint8_t *value;       /*!< Notification/indication data. */
} gatts_ntf_ind_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| attr_handle | uint16_t | 属性句柄 |
| value_len | uint16_t | 通知/指示数据长度 |
| value | uint8_t * | 发送的通知/指示数据 |

### gatts_ntf_ind_by_uuid_t <a id="struct_gatts_ntf_ind_by_uuid_t"></a>

```c
typedef struct {
    bt_uuid_t chara_uuid;  /*!< Characteristic UUID. */
    uint16_t start_handle; /*!< start handle. */
    uint16_t end_handle;   /*!< end handle. */
    uint16_t value_len;    /*!< Length of notification/indication data. */
    uint8_t *value;        /*!< Notification/indication data. */
} gatts_ntf_ind_by_uuid_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| chara_uuid | bt_uuid_t | 特征 UUID |
| start_handle | uint16_t | 起始句柄 |
| end_handle | uint16_t | 结束句柄 |
| value_len | uint16_t | 通知/指示数据长度 |
| value | uint8_t * | 发送的通知/指示数据 |

### gatts_add_character_result_t <a id="struct_gatts_add_character_result_t"></a>

```c
typedef struct {
    uint16_t handle;         /*!< decl handle. */
    uint16_t value_handle;   /*!< value handle. */
} gatts_add_character_result_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| handle | uint16_t | 特征声明句柄 |
| value_handle | uint16_t | 特征值句柄 |

### gatts_callbacks_t <a id="struct_gatts_callbacks_t"></a>

```c
typedef struct {
    gatts_add_service_callback add_service_cb;               /*!< Service added callback. */
    gatts_add_characteristic_callback add_characteristic_cb; /*!< Characteristc added callback. */
    gatts_add_descriptor_callback add_descriptor_cb;         /*!< Descriptor added callback. */
    gatts_start_service_callback start_service_cb;           /*!< Service started callback. */
    gatts_stop_service_callback stop_service_cb;             /*!< Service stoped callback. */
    gatts_delete_service_callback delete_service_cb;         /*!< All service deleted callback. */
    gatts_read_request_callback read_request_cb;             /*!< Read request received callback. */
    gatts_write_request_callback write_request_cb;           /*!< Write request received callback. */
    gatts_mtu_changed_callback mtu_changed_cb;               /*!< Mtu changed callback. */
    gatts_indication_confirm_callback indicate_confirm_cb;   /*!< Indication confirm callback. */
} gatts_callbacks_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| add_service_cb | gatts_add_service_callback | 添加服务回调函数 |
| add_characteristic_cb | gatts_add_characteristic_callback | 添加特征回调函数 |
| add_descriptor_cb | gatts_add_descriptor_callback | 添加描述符回调函数 |
| start_service_cb | gatts_start_service_callback | 启动服务回调函数 |
| stop_service_cb | gatts_stop_service_callback | 停止服务回调函数 |
| delete_service_cb | gatts_delete_service_callback | 删除所有服务回调函数 |
| read_request_cb | gatts_read_request_callback | 收到远端读请求回调函数 |
| write_request_cb | gatts_write_request_callback | 收到远端写请求回调函数 |
| mtu_changed_cb | gatts_mtu_changed_callback | MTU 大小更新回调函数 |
| indicate_confirm_cb | gatts_indication_confirm_callback | Indication Confirm 回调函数 |

## Macros

### SDK_BLE_MTU_MIN <a id="SDK_BLE_MTU_MIN"></a>

```c
#define SDK_BLE_MTU_MIN 23
```

### SDK_BLE_MTU_MAX <a id="SDK_BLE_MTU_MAX"></a>

```c
#define SDK_BLE_MTU_MAX 517
```


### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```
