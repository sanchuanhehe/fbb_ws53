# GATT Client

本页记录 GATT（Generic Attribute Profile） Client 相关接口声明，包括向远端服务端发起服务发现、特征发现、特征描述符发现，按照句柄或 UUID（Universally Unique Identifier）读取与写入属性值，以及通过回调上报发现结果、读写响应、MTU（Maximum Transmission Unit）协商结果、Notification 与 Indication 等事件。

!!! warning "当前 WS53 方案不支持 BLE Client"

    当前 WS53 SDK 解决方案未集成 BLE Central（中心设备）/GATT Client（客户端）相关组件，不支持使用本页接口开发 BLE Client。公共头文件中保留的接口声明不代表当前 WS53 方案支持该能力；WS53 仅支持 BLE Peripheral（外设）/GATT Server（服务端）角色。

**模块公共头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_client.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [gattc_register_client](#gattc_register_client) | 注册 GATT 客户端，分配客户端 ID |
| [gattc_unregister_client](#gattc_unregister_client) | 注销已注册的 GATT 客户端 |
| [gattc_discovery_service](#gattc_discovery_service) | 向远端发起服务发现请求 |
| [gattc_discovery_character](#gattc_discovery_character) | 向远端发起特征发现请求 |
| [gattc_discovery_descriptor](#gattc_discovery_descriptor) | 向远端发起特征描述符发现请求 |
| [gattc_read_req_by_handle](#gattc_read_req_by_handle) | 按照属性句柄发起读取请求 |
| [gattc_read_req_by_uuid](#gattc_read_req_by_uuid) | 按照 UUID 发起读取请求 |
| [gattc_write_req](#gattc_write_req) | 发起写请求（需要远端响应） |
| [gattc_write_cmd](#gattc_write_cmd) | 发起写命令（不需要远端响应） |
| [gattc_exchange_mtu_req](#gattc_exchange_mtu_req) | 发起 MTU 交换请求 |
| [gattc_register_callbacks](#gattc_register_callbacks) | 注册 GATT 客户端事件回调函数集合 |

## Functions

### gattc_register_client <a id="gattc_register_client"></a>

```c
errcode_t gattc_register_client(bt_uuid_t *app_uuid, uint8_t *client_id)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_client.h"
```

**功能说明**

- 注册上层应用为 GATT 客户端。
- 根据应用 UUID 分配并返回客户端 ID。
- 客户端 ID 作为后续服务发现、读写等操作的客户端标识。

**前置条件**

- 调用时序约束：需在 BTS（Bluetooth Stack）协议栈初始化完成、BLE 功能就绪后调用。
- 依赖关系：入参 app_uuid 指向由调用方填充的应用 UUID 结构。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| app_uuid | bt_uuid_t * | 上层应用 UUID | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| client_id | uint8_t * | 成功注册后由 BTS（Bluetooth Stack）填充的客户端 ID |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 客户端注册成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### gattc_unregister_client <a id="gattc_unregister_client"></a>

```c
errcode_t gattc_unregister_client(uint8_t client_id)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_client.h"
```

**功能说明**

- 注销已注册的 GATT 客户端。
- 释放与该客户端 ID 关联的资源。

**前置条件**

- 调用时序约束：需先调用 gattc_register_client 成功获取客户端 ID。
- 依赖关系：传入的 client_id 必须为已注册且未注销的有效客户端 ID。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| client_id | uint8_t | 待注销的客户端 ID | 已注册的有效客户端 ID |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 客户端注销成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### gattc_discovery_service <a id="gattc_discovery_service"></a>

```c
errcode_t gattc_discovery_service(uint8_t client_id, uint16_t conn_id, bt_uuid_t *uuid)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_client.h"
```

**功能说明**

- 向远端 GATT 服务端发起服务发现请求。
- 当 uuid 长度为 0 时发现全部服务，否则按 uuid 过滤目标服务。
- 服务发现结果通过已注册的 gattc_discovery_service_callback 与 gattc_discovery_service_complete_callback 回调异步返回。

**前置条件**

- 调用时序约束：需先调用 gattc_register_client 获取 client_id，并通过 gattc_register_callbacks 注册回调。
- 依赖关系：conn_id 对应的 BLE 连接必须已建立。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| client_id | uint8_t | 客户端 ID | 已注册的有效客户端 ID |
| conn_id | uint16_t | 连接 ID | 已建立的 BLE 连接 ID |
| uuid | bt_uuid_t * | 服务过滤 UUID，长度为 0 表示发现全部服务 | 不为NULL，uuid_len 取值 0 ~ 16 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 服务发现请求成功发起，结果通过回调返回 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### gattc_discovery_character <a id="gattc_discovery_character"></a>

```c
errcode_t gattc_discovery_character(uint8_t client_id, uint16_t conn_id, gattc_discovery_character_param_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_client.h"
```

**功能说明**

- 在指定服务范围内向远端发起特征发现请求。
- 当 param 中 uuid 长度为 0 时发现服务内的全部特征，否则按 uuid 过滤。
- 特征发现结果通过已注册的 gattc_discovery_character_callback 与 gattc_discovery_character_complete_callback 回调异步返回。

**前置条件**

- 调用时序约束：需先调用 gattc_discovery_service 获取目标服务句柄范围。
- 依赖关系：conn_id 对应的 BLE 连接必须已建立，回调集合需已注册。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| client_id | uint8_t | 客户端 ID | 已注册的有效客户端 ID |
| conn_id | uint16_t | 连接 ID | 已建立的 BLE 连接 ID |
| param | [gattc_discovery_character_param_t](#struct_gattc_discovery_character_param_t) * | 特征发现参数，包含服务起始句柄与过滤 uuid | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 特征发现请求成功发起，结果通过回调返回 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### gattc_discovery_descriptor <a id="gattc_discovery_descriptor"></a>

```c
errcode_t gattc_discovery_descriptor(uint8_t client_id, uint16_t conn_id, uint16_t character_handle)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_client.h"
```

**功能说明**

- 向远端发起指定特征声明句柄下的特征描述符发现请求。
- 特征描述符发现结果通过已注册的 gattc_discovery_descriptor_callback 与 gattc_discovery_descriptor_complete_callback 回调异步返回。

**前置条件**

- 调用时序约束：需先调用 gattc_discovery_character 获取目标特征的声明句柄。
- 依赖关系：conn_id 对应的 BLE 连接必须已建立，回调集合需已注册。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| client_id | uint8_t | 客户端 ID | 已注册的有效客户端 ID |
| conn_id | uint16_t | 连接 ID | 已建立的 BLE 连接 ID |
| character_handle | uint16_t | 目标特征的声明句柄 | 有效特征声明句柄 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 特征描述符发现请求成功发起，结果通过回调返回 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### gattc_read_req_by_handle <a id="gattc_read_req_by_handle"></a>

```c
errcode_t gattc_read_req_by_handle(uint8_t client_id, uint16_t conn_id, uint16_t handle)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_client.h"
```

**功能说明**

- 按照属性句柄向远端发起读取请求。
- 读取结果通过已注册的 gattc_read_cfm_callback 回调异步返回。

**前置条件**

- 调用时序约束：需先通过服务/特征发现获取到目标属性句柄。
- 依赖关系：conn_id 对应的 BLE 连接必须已建立，回调集合需已注册。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| client_id | uint8_t | 客户端 ID | 已注册的有效客户端 ID |
| conn_id | uint16_t | 连接 ID | 已建立的 BLE 连接 ID |
| handle | uint16_t | 待读取的属性句柄 | 有效属性句柄 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 读取请求成功发起，结果通过回调返回 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### gattc_read_req_by_uuid <a id="gattc_read_req_by_uuid"></a>

```c
errcode_t gattc_read_req_by_uuid(uint8_t client_id, uint16_t conn_id, gattc_read_req_by_uuid_param_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_client.h"
```

**功能说明**

- 在指定句柄范围内按照 UUID 向远端发起读取请求。
- 读取结果通过已注册的 gattc_read_cfm_callback 与 gattc_read_by_uuid_complete_callback 回调异步返回。

**前置条件**

- 调用时序约束：需先通过服务/特征发现获取到目标句柄范围。
- 依赖关系：conn_id 对应的 BLE 连接必须已建立，回调集合需已注册。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| client_id | uint8_t | 客户端 ID | 已注册的有效客户端 ID |
| conn_id | uint16_t | 连接 ID | 已建立的 BLE 连接 ID |
| param | [gattc_read_req_by_uuid_param_t](#struct_gattc_read_req_by_uuid_param_t) * | 按 UUID 读取请求参数，包含句柄范围与 uuid | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 读取请求成功发起，结果通过回调返回 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### gattc_write_req <a id="gattc_write_req"></a>

```c
errcode_t gattc_write_req(uint8_t client_id, uint16_t conn_id, gattc_handle_value_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_client.h"
```

**功能说明**

- 向远端属性句柄发起写请求（需要远端响应）。
- 写结果通过已注册的 gattc_write_cfm_callback 回调异步返回。

**前置条件**

- 调用时序约束：需先通过服务/特征发现获取到目标属性句柄。
- 依赖关系：conn_id 对应的 BLE 连接必须已建立，回调集合需已注册。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| client_id | uint8_t | 客户端 ID | 已注册的有效客户端 ID |
| conn_id | uint16_t | 连接 ID | 已建立的 BLE 连接 ID |
| param | [gattc_handle_value_t](#struct_gattc_handle_value_t) * | 写请求参数，包含目标句柄、数据及数据长度 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 写请求成功发起，结果通过回调返回 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### gattc_write_cmd <a id="gattc_write_cmd"></a>

```c
errcode_t gattc_write_cmd(uint8_t client_id, uint16_t conn_id, gattc_handle_value_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_client.h"
```

**功能说明**

- 向远端属性句柄发起写命令（不需要远端响应）。
- 不产生写响应回调。

**前置条件**

- 调用时序约束：需先通过服务/特征发现获取到目标属性句柄。
- 依赖关系：conn_id 对应的 BLE 连接必须已建立。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| client_id | uint8_t | 客户端 ID | 已注册的有效客户端 ID |
| conn_id | uint16_t | 连接 ID | 已建立的 BLE 连接 ID |
| param | [gattc_handle_value_t](#struct_gattc_handle_value_t) * | 写命令参数，包含目标句柄、数据及数据长度 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 写命令成功发起 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### gattc_exchange_mtu_req <a id="gattc_exchange_mtu_req"></a>

```c
errcode_t gattc_exchange_mtu_req(uint8_t client_id, uint16_t conn_id, uint16_t mtu_size)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_client.h"
```

**功能说明**

- 向远端发起 MTU 交换请求，协商本次连接的 ATT（Attribute Protocol）最大传输单元。
- MTU 协商结果通过已注册的 gattc_mtu_changed_callback 回调异步返回。

**前置条件**

- 调用时序约束：需在 BLE 连接建立后调用。
- 依赖关系：conn_id 对应的 BLE 连接必须已建立，回调集合需已注册。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| client_id | uint8_t | 客户端 ID | 已注册的有效客户端 ID |
| conn_id | uint16_t | 连接 ID | 已建立的 BLE 连接 ID |
| mtu_size | uint16_t | 客户端接收 MTU，即客户端支持的接收侧 MTU 大小 | 23 ~ 517 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | MTU 交换请求成功发起，结果通过回调返回 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### gattc_register_callbacks <a id="gattc_register_callbacks"></a>

```c
errcode_t gattc_register_callbacks(gattc_callbacks_t *func)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_gatt_client.h"
```

**功能说明**

- 注册 GATT 客户端事件回调函数集合。
- 注册后，服务发现、特征发现、特征描述符发现、读写响应、MTU 改变、Notification、Indication 等事件通过对应回调上报给上层应用。

**前置条件**

- 调用时序约束：建议在 gattc_register_client 之前或之后、发起任何发现或读写操作之前调用。
- 依赖关系：func 指向由调用方填充的 gattc_callbacks_t 结构。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func | [gattc_callbacks_t](#struct_gattc_callbacks_t) * | 回调函数集合 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 回调函数集合注册成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

## Type definitions

### gattc_discovery_service_callback <a id="gattc_discovery_service_callback"></a>

```c
typedef void (*gattc_discovery_service_callback)(uint8_t client_id, uint16_t conn_id,
    gattc_discovery_service_result_t *service, errcode_t status);
```

**使用说明**

服务发现结果回调函数指针类型，每当 gattc_discovery_service 发现到一个服务时由 BTS 线程调用上报该服务信息。

回调说明：
- 调用时机：运行于 BTS 线程，服务发现过程中每发现一个服务触发一次，禁止阻塞或长时间等待。
- 参数语义：client_id 为发起发现的客户端 ID；conn_id 为连接 ID；service 指向本次发现的服务结果（内存由 BTS 申请并在内部释放，回调中不应释放）；status 为本次服务发现结果错误码。
- 返回值处理：回调无返回值。

### gattc_discovery_service_complete_callback <a id="gattc_discovery_service_complete_callback"></a>

```c
typedef void (*gattc_discovery_service_complete_callback)(uint8_t client_id, uint16_t conn_id,
    bt_uuid_t *uuid, errcode_t status);
```

**使用说明**

服务发现完成回调函数指针类型，服务发现流程结束时由 BTS 线程调用。

回调说明：
- 调用时机：运行于 BTS 线程，服务发现流程完成时触发，禁止阻塞或长时间等待。
- 参数语义：client_id 为发起发现的客户端 ID；conn_id 为连接 ID；uuid 为发起发现时传入的入参回传；status 为整体发现流程结果错误码。
- 返回值处理：回调无返回值。

### gattc_discovery_character_callback <a id="gattc_discovery_character_callback"></a>

```c
typedef void (*gattc_discovery_character_callback)(uint8_t client_id, uint16_t conn_id,
    gattc_discovery_character_result_t *character, errcode_t status);
```

**使用说明**

特征发现结果回调函数指针类型，每当 gattc_discovery_character 发现到一个特征时由 BTS 线程调用上报该特征信息。

回调说明：
- 调用时机：运行于 BTS 线程，特征发现过程中每发现一个特征触发一次，禁止阻塞或长时间等待。
- 参数语义：client_id 为发起发现的客户端 ID；conn_id 为连接 ID；character 指向本次发现的特征结果（内存由 BTS 申请并在内部释放，回调中不应释放）；status 为本次特征发现结果错误码。
- 返回值处理：回调无返回值。

### gattc_discovery_character_complete_callback <a id="gattc_discovery_character_complete_callback"></a>

```c
typedef void (*gattc_discovery_character_complete_callback)(uint8_t client_id, uint16_t conn_id,
    gattc_discovery_character_param_t *param, errcode_t status);
```

**使用说明**

特征发现完成回调函数指针类型，特征发现流程结束时由 BTS 线程调用。

回调说明：
- 调用时机：运行于 BTS 线程，特征发现流程完成时触发，禁止阻塞或长时间等待。
- 参数语义：client_id 为发起发现的客户端 ID；conn_id 为连接 ID；param 为发起发现时传入的入参回传；status 为整体发现流程结果错误码。
- 返回值处理：回调无返回值。

### gattc_discovery_descriptor_callback <a id="gattc_discovery_descriptor_callback"></a>

```c
typedef void (*gattc_discovery_descriptor_callback)(uint8_t client_id, uint16_t conn_id,
    gattc_discovery_descriptor_result_t *descriptor, errcode_t status);
```

**使用说明**

特征描述符发现结果回调函数指针类型，每当 gattc_discovery_descriptor 发现到一个特征描述符时由 BTS 线程调用上报该描述符信息。

回调说明：
- 调用时机：运行于 BTS 线程，特征描述符发现过程中每发现一个描述符触发一次，禁止阻塞或长时间等待。
- 参数语义：client_id 为发起发现的客户端 ID；conn_id 为连接 ID；descriptor 指向本次发现的特征描述符结果（内存由 BTS 申请并在内部释放，回调中不应释放）；status 为本次描述符发现结果错误码。
- 返回值处理：回调无返回值。

### gattc_discovery_descriptor_complete_callback <a id="gattc_discovery_descriptor_complete_callback"></a>

```c
typedef void (*gattc_discovery_descriptor_complete_callback)(uint8_t client_id, uint16_t conn_id,
    uint16_t character_handle, errcode_t status);
```

**使用说明**

特征描述符发现完成回调函数指针类型，特征描述符发现流程结束时由 BTS 线程调用。

回调说明：
- 调用时机：运行于 BTS 线程，特征描述符发现流程完成时触发，禁止阻塞或长时间等待。
- 参数语义：client_id 为发起发现的客户端 ID；conn_id 为连接 ID；character_handle 为发起发现时传入的目标特征声明句柄回传；status 为整体发现流程结果错误码。
- 返回值处理：回调无返回值。

### gattc_read_cfm_callback <a id="gattc_read_cfm_callback"></a>

```c
typedef void (*gattc_read_cfm_callback)(uint8_t client_id, uint16_t conn_id, gattc_handle_value_t *read_result,
    gatt_status_t status);
```

**使用说明**

读响应回调函数指针类型，远端返回读响应时由 BTS 线程调用上报读取结果。

回调说明：
- 调用时机：运行于 BTS 线程，收到远端读响应时触发，禁止阻塞或长时间等待。
- 参数语义：client_id 为发起读取的客户端 ID；conn_id 为连接 ID；read_result 指向读取到的句柄值结果（内存由 BTS 申请并在内部释放，回调中不应释放）；status 为 GATT 错误码。
- 返回值处理：回调无返回值。

### gattc_read_by_uuid_complete_callback <a id="gattc_read_by_uuid_complete_callback"></a>

```c
typedef void (*gattc_read_by_uuid_complete_callback)(uint8_t client_id, uint16_t conn_id,
    gattc_read_req_by_uuid_param_t *param, errcode_t status);
```

**使用说明**

按 UUID 读取完成回调函数指针类型，按 UUID 读取流程结束时由 BTS 线程调用。

回调说明：
- 调用时机：运行于 BTS 线程，按 UUID 读取流程完成时触发，禁止阻塞或长时间等待。
- 参数语义：client_id 为发起读取的客户端 ID；conn_id 为连接 ID；param 为发起读取时传入的入参回传；status 为整体读取流程结果错误码。
- 返回值处理：回调无返回值。

### gattc_write_cfm_callback <a id="gattc_write_cfm_callback"></a>

```c
typedef void (*gattc_write_cfm_callback)(uint8_t client_id, uint16_t conn_id, uint16_t handle, gatt_status_t status);
```

**使用说明**

写响应回调函数指针类型，远端返回写响应时由 BTS 线程调用上报写结果。

回调说明：
- 调用时机：运行于 BTS 线程，收到远端写响应时触发，禁止阻塞或长时间等待。
- 参数语义：client_id 为发起写入的客户端 ID；conn_id 为连接 ID；handle 为请求写入的属性句柄；status 为 GATT 错误码。
- 返回值处理：回调无返回值。

### gattc_mtu_changed_callback <a id="gattc_mtu_changed_callback"></a>

```c
typedef void (*gattc_mtu_changed_callback)(uint8_t client_id, uint16_t conn_id, uint16_t mtu_size, errcode_t status);
```

**使用说明**

MTU 改变回调函数指针类型，MTU 交换完成时由 BTS 线程调用上报最终协商的 MTU 大小。

回调说明：
- 调用时机：运行于 BTS 线程，MTU 交换流程完成时触发，禁止阻塞或长时间等待。
- 参数语义：client_id 为发起 MTU 交换的客户端 ID；conn_id 为连接 ID；mtu_size 为协商后的 MTU 大小；status 为 MTU 交换结果错误码。
- 返回值处理：回调无返回值。

### gattc_notification_callback <a id="gattc_notification_callback"></a>

```c
typedef void (*gattc_notification_callback)(uint8_t client_id, uint16_t conn_id, gattc_handle_value_t *data,
    errcode_t status);
```

**使用说明**

收到 Notification 回调函数指针类型，远端通过 Notification 上报数据时由 BTS 线程调用。

回调说明：
- 调用时机：运行于 BTS 线程，收到远端 Notification 时触发，禁止阻塞或长时间等待。
- 参数语义：client_id 为接收通知的客户端 ID；conn_id 为连接 ID；data 指向通知数据（内存由 BTS 申请并在内部释放，回调中不应释放）；status 为执行结果错误码。
- 返回值处理：回调无返回值。

### gattc_indication_callback <a id="gattc_indication_callback"></a>

```c
typedef void (*gattc_indication_callback)(uint8_t client_id, uint16_t conn_id, gattc_handle_value_t *data,
    errcode_t status);
```

**使用说明**

收到 Indication 回调函数指针类型，远端通过 Indication 上报数据时由 BTS 线程调用。

回调说明：
- 调用时机：运行于 BTS 线程，收到远端 Indication 时触发，禁止阻塞或长时间等待。
- 参数语义：client_id 为接收指示的客户端 ID；conn_id 为连接 ID；data 指向指示数据（内存由 BTS 申请并在内部释放，回调中不应释放）；status 为执行结果错误码。
- 返回值处理：回调无返回值。

### errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块所有对外接口的返回值类型，表示接口执行结果的错误码。本类型定义位于 SDK 公共头文件 `errcode.h`，被本模块全部对外接口的返回值直接使用。

## Structures

### gattc_handle_value_t <a id="struct_gattc_handle_value_t"></a>

```c
typedef struct {
    uint16_t handle;   /*!< 属性句柄。 */
    uint16_t data_len; /*!< 数据长度。 */
    uint8_t *data;     /*!< 数据。 */
} gattc_handle_value_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| handle | uint16_t | 属性句柄，作为读写操作的目标句柄或读取结果的来源句柄 |
| data_len | uint16_t | 数据长度，单位 Bytes |
| data | uint8_t * | 数据指针，指向句柄对应的数据内容 |

### gattc_discovery_character_param_t <a id="struct_gattc_discovery_character_param_t"></a>

```c
typedef struct {
    uint16_t service_handle; /*!< 服务起始句柄。 */
    bt_uuid_t uuid;          /*!< 特征uuid，如果uuid长度为0，发现服务内的所有特征，否则按照uuid过滤。 */
} gattc_discovery_character_param_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| service_handle | uint16_t | 服务起始句柄，作为特征发现的范围起点 |
| uuid | bt_uuid_t | 特征过滤 UUID，uuid_len 为 0 时发现服务内全部特征，否则按该 uuid 过滤 |

### gattc_discovery_service_result_t <a id="struct_gattc_discovery_service_result_t"></a>

```c
typedef struct {
    uint16_t start_hdl; /*!< 服务起始句柄。 */
    uint16_t end_hdl;   /*!< 服务结束句柄。 */
    bt_uuid_t uuid;     /*!< 服务uuid。 */
} gattc_discovery_service_result_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| start_hdl | uint16_t | 服务起始句柄 |
| end_hdl | uint16_t | 服务结束句柄 |
| uuid | bt_uuid_t | 服务 UUID |

### gattc_discovery_character_result_t <a id="struct_gattc_discovery_character_result_t"></a>

```c
typedef struct {
    bt_uuid_t uuid;          /*!< 特征uuid。 */
    uint16_t declare_handle; /*!< 特征声明句柄。 */
    uint16_t value_handle;   /*!< 特征值句柄。 */
    uint8_t properties;      /*!< 特征特性 { gatt_characteristic_property_t }。 */
} gattc_discovery_character_result_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| uuid | bt_uuid_t | 特征 UUID |
| declare_handle | uint16_t | 特征声明句柄 |
| value_handle | uint16_t | 特征值句柄 |
| properties | uint8_t | 特征特性，取值为 gatt_characteristic_property_t 各特性位的按位或 |

### gattc_discovery_descriptor_result_t <a id="struct_gattc_discovery_descriptor_result_t"></a>

```c
typedef struct {
    uint16_t descriptor_hdl; /*!< 特征描述符句柄。 */
    bt_uuid_t uuid;          /*!< 特征描述符uuid。 */
} gattc_discovery_descriptor_result_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| descriptor_hdl | uint16_t | 特征描述符句柄 |
| uuid | bt_uuid_t | 特征描述符 UUID |

### gattc_read_req_by_uuid_param_t <a id="struct_gattc_read_req_by_uuid_param_t"></a>

```c
typedef struct {
    uint16_t start_hdl; /*!< 起始句柄。 */
    uint16_t end_hdl;   /*!< 结束句柄。 */
    bt_uuid_t uuid;     /*!< uuid。 */
} gattc_read_req_by_uuid_param_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| start_hdl | uint16_t | 起始句柄，作为按 UUID 读取的句柄范围起点 |
| end_hdl | uint16_t | 结束句柄，作为按 UUID 读取的句柄范围终点 |
| uuid | bt_uuid_t | 待读取属性的 UUID 过滤条件 |

### gattc_callbacks_t <a id="struct_gattc_callbacks_t"></a>

```c
typedef struct ble_gattc_callbacks {
    gattc_discovery_service_callback discovery_svc_cb;                  /*!< 发现服务回调函数。 */
    gattc_discovery_service_complete_callback discovery_svc_cmp_cb;     /*!< 发现服务完成回调函数。 */
    gattc_discovery_character_callback discovery_chara_cb;              /*!< 发现特征回调函数。 */
    gattc_discovery_character_complete_callback discovery_chara_cmp_cb; /*!< 发现特征完成回调函数。 */
    gattc_discovery_descriptor_callback discovery_desc_cb;              /*!< 发现特征描述符回调函数。 */
    gattc_discovery_descriptor_complete_callback discovery_desc_cmp_cb; /*!< 发现特征描述符完成回调函数。 */
    gattc_read_cfm_callback read_cb;                                    /*!< 收到读响应回调函数。 */
    gattc_read_by_uuid_complete_callback read_cmp_cb;                   /*!< 按照uuid读取完成回调函数。 */
    gattc_write_cfm_callback write_cb;                                  /*!< 收到写响应回调函数。 */
    gattc_mtu_changed_callback mtu_changed_cb;                          /*!< mtu改变回调函数。 */
    gattc_notification_callback notification_cb;                        /*!< 收到通知回调函数。 */
    gattc_indication_callback indication_cb;                            /*!< 收到指示回调函数。 */
} gattc_callbacks_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| discovery_svc_cb | [gattc_discovery_service_callback](#gattc_discovery_service_callback) | 发现服务回调函数，每个服务发现结果上报入口 |
| discovery_svc_cmp_cb | [gattc_discovery_service_complete_callback](#gattc_discovery_service_complete_callback) | 发现服务完成回调函数，服务发现流程结束上报入口 |
| discovery_chara_cb | [gattc_discovery_character_callback](#gattc_discovery_character_callback) | 发现特征回调函数，每个特征发现结果上报入口 |
| discovery_chara_cmp_cb | [gattc_discovery_character_complete_callback](#gattc_discovery_character_complete_callback) | 发现特征完成回调函数，特征发现流程结束上报入口 |
| discovery_desc_cb | [gattc_discovery_descriptor_callback](#gattc_discovery_descriptor_callback) | 发现特征描述符回调函数，每个描述符发现结果上报入口 |
| discovery_desc_cmp_cb | [gattc_discovery_descriptor_complete_callback](#gattc_discovery_descriptor_complete_callback) | 发现特征描述符完成回调函数，描述符发现流程结束上报入口 |
| read_cb | [gattc_read_cfm_callback](#gattc_read_cfm_callback) | 收到读响应回调函数 |
| read_cmp_cb | [gattc_read_by_uuid_complete_callback](#gattc_read_by_uuid_complete_callback) | 按照 UUID 读取完成回调函数 |
| write_cb | [gattc_write_cfm_callback](#gattc_write_cfm_callback) | 收到写响应回调函数 |
| mtu_changed_cb | [gattc_mtu_changed_callback](#gattc_mtu_changed_callback) | MTU 改变回调函数 |
| notification_cb | [gattc_notification_callback](#gattc_notification_callback) | 收到通知回调函数 |
| indication_cb | [gattc_indication_callback](#gattc_indication_callback) | 收到指示回调函数 |
