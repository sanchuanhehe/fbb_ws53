# SSAP Client

SSAP (Service Access Protocol) client 提供 SLE (Star Flash Low Energy) 协议中服务接入协议客户端侧的能力，支持注册与注销客户端、注册回调函数、发起服务/属性/描述符查找、按句柄或 UUID (Universally Unique Identifier) 读取、发起写请求与写命令以及交换信息请求。

**模块公共头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_client.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [ssapc_register_client](#ssapc_register_client) | 注册 SSAP 客户端，分配客户端 ID |
| [ssapc_unregister_client](#ssapc_unregister_client) | 注销已注册的 SSAP 客户端 |
| [ssapc_find_structure](#ssapc_find_structure) | 发起服务、属性、描述符查找请求 |
| [ssapc_read_req_by_uuid](#ssapc_read_req_by_uuid) | 发起按 UUID 读取请求 |
| [ssapc_read_req](#ssapc_read_req) | 发起按句柄读取请求 |
| [ssapc_write_req](#ssapc_write_req) | 发起写请求（需服务端响应） |
| [ssapc_write_cmd](#ssapc_write_cmd) | 发起写命令（无需服务端响应） |
| [ssapc_exchange_info_req](#ssapc_exchange_info_req) | 发送交换信息请求（协商 MTU (Maximum Transmission Unit) 等） |
| [ssapc_register_callbacks](#ssapc_register_callbacks) | 注册 SSAP 客户端回调函数集合 |

## Functions

### ssapc_register_client <a id="ssapc_register_client"></a>

```c
errcode_t ssapc_register_client(sle_uuid_t *app_uuid, uint8_t *client_id)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_client.h"
```

**功能说明**

- 注册 SSAP 客户端，向上层应用分配并返回客户端 ID
- 以应用 UUID 标识上层应用身份
- 注册成功后该客户端 ID 可用于后续查找、读写、交换信息等请求

**前置条件**

- 调用时序约束：当前接口必须在 SLE 协议栈初始化完成后调用
- 依赖关系：当前接口依赖 SLE service 已就绪
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| app_uuid | [sle_uuid_t](#struct_sle_uuid_t) * | 上层应用 UUID | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| client_id | uint8_t * | 由 SLE service 分配的客户端 ID，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 请求成功发起 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_client/src/sle_speed_client.c`

### ssapc_unregister_client <a id="ssapc_unregister_client"></a>

```c
errcode_t ssapc_unregister_client(uint8_t client_id)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_client.h"
```

**功能说明**

- 注销已注册的 SSAP 客户端
- 释放该客户端 ID 占用的资源
- 注销后该客户端 ID 不再可用于发起请求

**前置条件**

- 调用时序约束：当前接口必须在 [ssapc_register_client](#ssapc_register_client) 成功返回后调用
- 依赖关系：当前接口依赖传入的客户端 ID 已通过注册获得
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| client_id | uint8_t | 已注册的客户端 ID | 由 ssapc_register_client 分配 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 请求成功发起 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

### ssapc_find_structure <a id="ssapc_find_structure"></a>

```c
errcode_t ssapc_find_structure(uint8_t client_id, uint16_t conn_id, ssapc_find_structure_param_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_client.h"
```

**功能说明**

- 向对端发起服务、属性、描述符查找请求
- 支持按 UUID 过滤或发现全部结构（param 为 NULL 时发现全部结构）
- 查找结果通过已注册的回调函数返回

**前置条件**

- 调用时序约束：当前接口必须在 [ssapc_register_client](#ssapc_register_client) 成功返回后调用，且对应的 SLE 连接已建立
- 依赖关系：当前接口依赖 [ssapc_register_callbacks](#ssapc_register_callbacks) 已注册用于接收结果的回调函数
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| client_id | uint8_t | 客户端 ID | 由 ssapc_register_client 分配 |
| conn_id | uint16_t | 连接 ID | 已建立的 SLE 连接 ID |
| param | [ssapc_find_structure_param_t](#struct_ssapc_find_structure_param_t) * | 查找参数，传 NULL 表示发现全部结构 | 为NULL 或指向有效的查找参数结构体 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0 | 执行成功 | 请求发起成功；服务发现结果将在 ssapc_find_structure_callback 和 ssapc_find_structure_complete_callback 中返回 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 请求发起失败 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_client/src/sle_speed_client.c`

### ssapc_read_req_by_uuid <a id="ssapc_read_req_by_uuid"></a>

```c
errcode_t ssapc_read_req_by_uuid(uint8_t client_id, uint16_t conn_id, ssapc_read_req_by_uuid_param_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_client.h"
```

**功能说明**

- 向对端发起按 UUID 的读取请求
- 读取范围由参数中的句柄区间与 UUID 共同确定
- 读取结果通过已注册的回调函数返回

**前置条件**

- 调用时序约束：当前接口必须在 [ssapc_register_client](#ssapc_register_client) 成功返回后调用，且对应的 SLE 连接已建立
- 依赖关系：当前接口依赖 [ssapc_register_callbacks](#ssapc_register_callbacks) 已注册用于接收结果的回调函数
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| client_id | uint8_t | 客户端 ID | 由 ssapc_register_client 分配 |
| conn_id | uint16_t | 连接 ID | 已建立的 SLE 连接 ID |
| param | [ssapc_read_req_by_uuid_param_t](#struct_ssapc_read_req_by_uuid_param_t) * | 按 UUID 读取请求参数 | 不为NULL |

**参考案例**

- `src/application/samples/bt/sle/sle_sensor_report/sle_sensor_report_client/src/sle_sensor_report_client.c`

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0 | 执行成功 | 请求发起成功；读取结果将在 ssapc_read_cfm_callback 和 ssapc_read_by_uuid_complete_callback 中返回 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 请求发起失败 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

### ssapc_read_req <a id="ssapc_read_req"></a>

```c
errcode_t ssapc_read_req(uint8_t client_id, uint16_t conn_id, uint16_t handle, uint8_t type)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_client.h"
```

**功能说明**

- 向对端发起按句柄的读取请求
- 读取对象由属性句柄与特征类型共同确定
- 读取结果通过已注册的回调函数返回

**前置条件**

- 调用时序约束：当前接口必须在 [ssapc_register_client](#ssapc_register_client) 成功返回后调用，且对应的 SLE 连接已建立
- 依赖关系：当前接口依赖 [ssapc_register_callbacks](#ssapc_register_callbacks) 已注册用于接收结果的回调函数
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| client_id | uint8_t | 客户端 ID | 由 ssapc_register_client 分配 |
| conn_id | uint16_t | 连接 ID | 已建立的 SLE 连接 ID |
| handle | uint16_t | 属性句柄 | 有效属性句柄 |
| type | uint8_t | 特征类型 | [SSAP_PROPERTY_TYPE_VALUE](#enum_ssap_property_type_t):0 / [SSAP_DESCRIPTOR_USER_DESCRIPTION](#enum_ssap_property_type_t):1 / [SSAP_DESCRIPTOR_CLIENT_CONFIGURATION](#enum_ssap_property_type_t):2 / [SSAP_DESCRIPTOR_SERVER_CONFIGURATION](#enum_ssap_property_type_t):3 / [SSAP_DESCRIPTOR_PRESENTATION_FORMAT](#enum_ssap_property_type_t):4 / [SSAP_DESCRIPTOR_RFU](#enum_ssap_property_type_t):5 / [SSAP_DESCRIPTOR_CUSTOM](#enum_ssap_property_type_t):255 |

**参考案例**

- `src/application/samples/bt/sle/sle_hello/sle_hello_client/src/sle_hello_client.c`

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0 | 执行成功 | 请求发起成功；读取结果将在 ssapc_read_cfm_callback 中返回 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 请求发起失败 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_client/src/sle_speed_client.c`

### ssapc_write_req <a id="ssapc_write_req"></a>

```c
errcode_t ssapc_write_req(uint8_t client_id, uint16_t conn_id, ssapc_write_param_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_client.h"
```

**功能说明**

- 向对端发起写请求，需服务端回复响应
- 写入对象与数据内容由参数指定
- 写结果通过已注册的回调函数返回

**前置条件**

- 调用时序约束：当前接口必须在 [ssapc_register_client](#ssapc_register_client) 成功返回后调用，且对应的 SLE 连接已建立
- 依赖关系：当前接口依赖 [ssapc_register_callbacks](#ssapc_register_callbacks) 已注册用于接收结果的回调函数
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| client_id | uint8_t | 客户端 ID | 由 ssapc_register_client 分配 |
| conn_id | uint16_t | 连接 ID | 已建立的 SLE 连接 ID |
| param | [ssapc_write_param_t](#struct_ssapc_handle_value_t) * | 写请求参数 | 不为NULL |

**参考案例**

- `src/application/samples/bt/sle/sle_hello/sle_hello_client/src/sle_hello_client.c`

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0 | 执行成功 | 请求发起成功；写结果将在 ssapc_write_cfm_callback 中返回 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 请求发起失败 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

### ssapc_write_cmd <a id="ssapc_write_cmd"></a>

```c
errcode_t ssapc_write_cmd(uint8_t client_id, uint16_t conn_id, ssapc_write_param_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_client.h"
```

**功能说明**

- 向对端发起写命令，无需服务端回复响应
- 写入对象与数据内容由参数指定
- 写命令不产生写结果回调

**前置条件**

- 调用时序约束：当前接口必须在 [ssapc_register_client](#ssapc_register_client) 成功返回后调用，且对应的 SLE 连接已建立
- 依赖关系：当前接口依赖对应 SLE 连接已建立
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| client_id | uint8_t | 客户端 ID | 由 ssapc_register_client 分配 |
| conn_id | uint16_t | 连接 ID | 已建立的 SLE 连接 ID |
| param | [ssapc_write_param_t](#struct_ssapc_handle_value_t) * | 写命令参数 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 请求成功发起 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

### ssapc_exchange_info_req <a id="ssapc_exchange_info_req"></a>

```c
errcode_t ssapc_exchange_info_req(uint8_t client_id, uint16_t conn_id, ssap_exchange_info_t* param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_client.h"
```

**功能说明**

- 向对端发送交换信息请求，用于协商 MTU (Maximum Transmission Unit) 等
- 交换信息内容由参数指定
- 交换结果通过已注册的回调函数返回

**前置条件**

- 调用时序约束：当前接口必须在 [ssapc_register_client](#ssapc_register_client) 成功返回后调用，且对应的 SLE 连接已建立
- 依赖关系：当前接口依赖 [ssapc_register_callbacks](#ssapc_register_callbacks) 已注册用于接收结果的回调函数
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| client_id | uint8_t | 客户端 ID | 由 ssapc_register_client 分配 |
| conn_id | uint16_t | 连接 ID | 已建立的 SLE 连接 ID |
| param | [ssap_exchange_info_t](#struct_ssap_exchange_info_t) * | 客户端交换信息 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0 | 执行成功 | 请求发起成功；MTU 改变结果将在 ssapc_exchange_info_callback 中返回 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 请求发起失败 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_client/src/sle_speed_client.c`

### ssapc_register_callbacks <a id="ssapc_register_callbacks"></a>

```c
errcode_t ssapc_register_callbacks(ssapc_callbacks_t *func)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_client.h"
```

**功能说明**

- 注册 SSAP 客户端回调函数集合
- 注册后回调集合用于接收服务发现、读写、通知、指示等异步事件
- 回调运行于 SLE service 线程，回调内不应阻塞或长时间等待

**前置条件**

- 调用时序约束：当前接口必须在 SLE 协议栈初始化完成后调用，建议在发起查找/读写请求前完成注册
- 依赖关系：当前接口依赖 func 指向的回调集合已由上层正确填充
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func | [ssapc_callbacks_t](#struct_ssapc_callbacks_t) * | 回调函数集合 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 请求成功发起 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_client/src/sle_speed_client.c`

## Type definitions

### typedef_errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块返回类型为 errcode_t 的对外接口的返回值类型。

### ssapc_find_structure_callback <a id="typedef_ssapc_find_structure_callback"></a>

```c
typedef void (*ssapc_find_structure_callback)(uint8_t client_id, uint16_t conn_id,
    ssapc_find_service_result_t *service, errcode_t status);
```

**使用说明**

服务发现的回调函数类型。回调说明：调用时机为服务发现产生结果时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 service 指向由 SLE service 申请并释放内存的发现服务信息，回调中不应释放；参数 status 为执行结果错误码。

### ssapc_find_property_callback <a id="typedef_ssapc_find_property_callback"></a>

```c
typedef void (*ssapc_find_property_callback)(uint8_t client_id, uint16_t conn_id,
    ssapc_find_property_result_t *property, errcode_t status);
```

**使用说明**

属性发现的回调函数类型。回调说明：调用时机为属性发现产生结果时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 property 指向由 SLE service 申请并释放内存的特征信息，回调中不应释放；参数 status 为执行结果错误码。

### ssapc_find_structure_complete_callback <a id="typedef_ssapc_find_structure_complete_callback"></a>

```c
typedef void (*ssapc_find_structure_complete_callback)(uint8_t client_id, uint16_t conn_id,
    ssapc_find_structure_result_t *structure_result, errcode_t status);
```

**使用说明**

查找完成的回调函数类型。回调说明：调用时机为查找流程完成时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 structure_result 为入参回传；参数 status 为执行结果错误码。

### ssapc_read_cfm_callback <a id="typedef_ssapc_read_cfm_callback"></a>

```c
typedef void (*ssapc_read_cfm_callback)(uint8_t client_id, uint16_t conn_id, ssapc_handle_value_t *read_data,
    errcode_t status);
```

**使用说明**

收到读响应的回调函数类型。回调说明：调用时机为收到对端读响应时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 read_data 指向由 SLE service 申请并释放内存的读取数据，回调中不应释放；参数 status 为执行结果错误码。

### ssapc_read_by_uuid_complete_callback <a id="typedef_ssapc_read_by_uuid_complete_callback"></a>

```c
typedef void (*ssapc_read_by_uuid_complete_callback)(uint8_t client_id, uint16_t conn_id,
    ssapc_read_by_uuid_cmp_result_t *cmp_result, errcode_t status);
```

**使用说明**

按 UUID 读取完成的回调函数类型。回调说明：调用时机为按 UUID 读取流程完成时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 cmp_result 为入参回传；参数 status 为执行结果错误码。

### ssapc_write_cfm_callback <a id="typedef_ssapc_write_cfm_callback"></a>

```c
typedef void (*ssapc_write_cfm_callback)(uint8_t client_id, uint16_t conn_id, ssapc_write_result_t *write_result,
    errcode_t status);
```

**使用说明**

收到写响应的回调函数类型。回调说明：调用时机为收到对端写响应时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 write_result 指向由 SLE service 申请并释放内存的写结果，回调中不应释放；参数 status 为执行结果错误码。

### ssapc_exchange_info_callback <a id="typedef_ssapc_exchange_info_callback"></a>

```c
typedef void (*ssapc_exchange_info_callback)(uint8_t client_id, uint16_t conn_id, ssap_exchange_info_t *param,
    errcode_t status);
```

**使用说明**

MTU 改变（交换信息）的回调函数类型。回调说明：调用时机为收到对端交换信息响应时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 param 指向交换信息；参数 status 为执行结果错误码。

### ssapc_notification_callback <a id="typedef_ssapc_notification_callback"></a>

```c
typedef void (*ssapc_notification_callback)(uint8_t client_id, uint16_t conn_id, ssapc_handle_value_t *data,
    errcode_t status);
```

**使用说明**

收到通知的回调函数类型。回调说明：调用时机为收到对端通知时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 data 指向由 SLE service 申请并释放内存的通知数据，回调中不应释放；参数 status 为执行结果错误码。

### ssapc_indication_callback <a id="typedef_ssapc_indication_callback"></a>

```c
typedef void (*ssapc_indication_callback)(uint8_t client_id, uint16_t conn_id, ssapc_handle_value_t *data,
    errcode_t status);
```

**使用说明**

收到指示的回调函数类型。回调说明：调用时机为收到对端指示时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 data 指向由 SLE service 申请并释放内存的指示数据，回调中不应释放；参数 status 为执行结果错误码。

## Enumerations

### ssap_find_type_t <a id="enum_ssap_find_type_t"></a>

```c
typedef enum {
    SSAP_FIND_TYPE_SERVICE_STRUCTURE = 0x00,
    SSAP_FIND_TYPE_PRIMARY_SERVICE   = 0x01,
    SSAP_FIND_TYPE_REFERENCE_SERVICE = 0x02,
    SSAP_FIND_TYPE_PROPERTY          = 0x03,
    SSAP_FIND_TYPE_METHOD            = 0x04,
    SSAP_FIND_TYPE_EVENT             = 0x05,
} ssap_find_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SSAP_FIND_TYPE_SERVICE_STRUCTURE | 0x00 | 服务结构 |
| SSAP_FIND_TYPE_PRIMARY_SERVICE | 0x01 | 首要服务 |
| SSAP_FIND_TYPE_REFERENCE_SERVICE | 0x02 | 引用服务 |
| SSAP_FIND_TYPE_PROPERTY | 0x03 | 属性 |
| SSAP_FIND_TYPE_METHOD | 0x04 | 方法 |
| SSAP_FIND_TYPE_EVENT | 0x05 | 事件 |

### ssap_property_type_t <a id="enum_ssap_property_type_t"></a>

```c
typedef enum {
    SSAP_PROPERTY_TYPE_VALUE             = 0x00,
    SSAP_DESCRIPTOR_USER_DESCRIPTION     = 0x01,
    SSAP_DESCRIPTOR_CLIENT_CONFIGURATION = 0x02,
    SSAP_DESCRIPTOR_SERVER_CONFIGURATION = 0x03,
    SSAP_DESCRIPTOR_PRESENTATION_FORMAT  = 0x04,
    SSAP_DESCRIPTOR_RFU                  = 0x05,
    SSAP_DESCRIPTOR_CUSTOM               = 0xFF,
} ssap_property_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SSAP_PROPERTY_TYPE_VALUE | 0x00 | 特征值 |
| SSAP_DESCRIPTOR_USER_DESCRIPTION | 0x01 | 属性说明描述符 |
| SSAP_DESCRIPTOR_CLIENT_CONFIGURATION | 0x02 | 客户端配置描述符 |
| SSAP_DESCRIPTOR_SERVER_CONFIGURATION | 0x03 | 服务端配置描述符 |
| SSAP_DESCRIPTOR_PRESENTATION_FORMAT | 0x04 | 格式描述符 |
| SSAP_DESCRIPTOR_RFU | 0x05 | 服务管理保留描述符，0x05 – 0x1F |
| SSAP_DESCRIPTOR_CUSTOM | 0xFF | 厂商自定义描述符 |

## Structures

### sle_uuid_t <a id="struct_sle_uuid_t"></a>

```c
typedef struct {
    uint8_t len;
    uint8_t uuid[SLE_UUID_LEN];
} sle_uuid_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| len | uint8_t | UUID 长度 |
| uuid | uint8_t[] | UUID 字段，长度为 SLE_UUID_LEN(16) |

### ssap_exchange_info_t <a id="struct_ssap_exchange_info_t"></a>

```c
typedef struct {
    uint32_t mtu_size;
    uint16_t version;
} ssap_exchange_info_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| mtu_size | uint32_t | MTU 大小 |
| version | uint16_t | 版本，预留字段 |

### ssapc_find_service_result_t <a id="struct_ssapc_find_service_result_t"></a>

```c
typedef struct {
    uint16_t   start_hdl;
    uint16_t   end_hdl;
    sle_uuid_t uuid;
} ssapc_find_service_result_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| start_hdl | uint16_t | 服务起始句柄 |
| end_hdl | uint16_t | 服务结束句柄 |
| uuid | sle_uuid_t | 服务 UUID |

### ssapc_find_property_result_t <a id="struct_ssapc_find_property_result_t"></a>

```c
typedef struct {
    uint16_t   handle;
    uint32_t   operate_indication;
    sle_uuid_t uuid;
    uint8_t    descriptors_count;
    uint8_t    descriptors_type[0];
} ssapc_find_property_result_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| handle | uint16_t | 属性句柄 |
| operate_indication | uint32_t | 操作指示 |
| uuid | sle_uuid_t | UUID 标识 |
| descriptors_count | uint8_t | 属性描述符类型列表长度 |
| descriptors_type | uint8_t[] | 属性描述符类型列表，长度由 descriptors_count 决定 |

### ssapc_handle_value_t <a id="struct_ssapc_handle_value_t"></a>

```c
typedef struct {
    uint16_t handle;
    uint8_t  type;
    uint16_t data_len;
    uint8_t  *data;
} ssapc_handle_value_t, ssapc_write_param_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| handle | uint16_t | 属性句柄 |
| type | uint8_t | 属性类型 |
| data_len | uint16_t | 数据长度 |
| data | uint8_t * | 数据内容 |

### ssapc_write_result_t <a id="struct_ssapc_write_result_t"></a>

```c
typedef struct {
    uint16_t handle;
    uint8_t  type;
    uint16_t data_len;
    uint8_t  *data;
} ssapc_write_result_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| handle | uint16_t | 属性句柄 |
| type | uint8_t | 属性类型 |
| data_len | uint16_t | 数据长度 |
| data | uint8_t * | 数据内容 |

### ssapc_read_by_uuid_cmp_result_t <a id="struct_ssapc_read_by_uuid_cmp_result_t"></a>

```c
typedef struct {
    sle_uuid_t uuid;
    uint8_t type;
    uint16_t   start_hdl;
    uint16_t   end_hdl;
} ssapc_read_by_uuid_cmp_result_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| uuid | sle_uuid_t | 属性对应的 UUID |
| type | uint8_t | 属性类型 |
| start_hdl | uint16_t | 起始句柄 |
| end_hdl | uint16_t | 结束句柄 |

### ssapc_find_structure_param_t <a id="struct_ssapc_find_structure_param_t"></a>

```c
typedef struct {
    uint8_t    type;
    uint16_t   start_hdl;
    uint16_t   end_hdl;
    sle_uuid_t uuid;
    uint8_t    reserve;
} ssapc_find_structure_param_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| type | uint8_t | 查找类型，取值见 [ssap_find_type_t](#enum_ssap_find_type_t) |
| start_hdl | uint16_t | 起始句柄 |
| end_hdl | uint16_t | 结束句柄 |
| uuid | sle_uuid_t | UUID，按 UUID 查找时生效，其余不生效 |
| reserve | uint8_t | 预留，默认值写 0 |

### ssapc_find_structure_result_t <a id="struct_ssapc_find_structure_result_t"></a>

```c
typedef struct {
    uint8_t    type;
    sle_uuid_t uuid;
} ssapc_find_structure_result_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| type | uint8_t | 查找类型，取值见 [ssap_find_type_t](#enum_ssap_find_type_t) |
| uuid | sle_uuid_t | UUID |

### ssapc_read_req_by_uuid_param_t <a id="struct_ssapc_read_req_by_uuid_param_t"></a>

```c
typedef struct {
    uint8_t    type;
    uint16_t   start_hdl;
    uint16_t   end_hdl;
    sle_uuid_t uuid;
} ssapc_read_req_by_uuid_param_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| type | uint8_t | 查找类型，取值见 [ssap_property_type_t](#enum_ssap_property_type_t) |
| start_hdl | uint16_t | 起始句柄 |
| end_hdl | uint16_t | 结束句柄 |
| uuid | sle_uuid_t | UUID |

### ssapc_callbacks_t <a id="struct_ssapc_callbacks_t"></a>

```c
typedef struct {
    ssapc_find_structure_callback find_structure_cb;
    ssapc_find_property_callback ssapc_find_property_cbk;
    ssapc_find_structure_complete_callback find_structure_cmp_cb;
    ssapc_read_cfm_callback read_cfm_cb;
    ssapc_read_by_uuid_complete_callback read_by_uuid_cmp_cb;
    ssapc_write_cfm_callback write_cfm_cb;
    ssapc_exchange_info_callback exchange_info_cb;
    ssapc_notification_callback notification_cb;
    ssapc_indication_callback indication_cb;
} ssapc_callbacks_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| find_structure_cb | ssapc_find_structure_callback | 发现服务回调函数 |
| ssapc_find_property_cbk | ssapc_find_property_callback | 发现特征回调函数 |
| find_structure_cmp_cb | ssapc_find_structure_complete_callback | 发现特征完成回调函数 |
| read_cfm_cb | ssapc_read_cfm_callback | 收到读响应回调函数 |
| read_by_uuid_cmp_cb | ssapc_read_by_uuid_complete_callback | 读特征值完成回调钩子 |
| write_cfm_cb | ssapc_write_cfm_callback | 收到写响应回调函数 |
| exchange_info_cb | ssapc_exchange_info_callback | 更新 MTU 大小回调钩子 |
| notification_cb | ssapc_notification_callback | 通知事件上报钩子 |
| indication_cb | ssapc_indication_callback | 指示事件上报钩子 |

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```

### SLE_UUID_LEN <a id="SLE_UUID_LEN"></a>

```c
#define SLE_UUID_LEN 16
```
