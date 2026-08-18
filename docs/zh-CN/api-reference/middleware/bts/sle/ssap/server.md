# SSAP Server

SSAP (Service Access Protocol) server 提供 SLE (Star Flash Low Energy) 协议中服务接入协议服务端侧的能力，支持注册与注销服务端、注册回调函数、异步与同步添加服务/特征/描述符、启动与删除服务、回复读写响应以及按句柄或 UUID (Universally Unique Identifier) 向对端发送通知或指示。

**模块公共头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_server.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [ssaps_register_server](#ssaps_register_server) | 注册 SSAP 服务端，分配服务端 ID |
| [ssaps_unregister_server](#ssaps_unregister_server) | 注销已注册的 SSAP 服务端 |
| [ssaps_add_service](#ssaps_add_service) | 异步添加一个 SSAP 服务，句柄在回调中返回 |
| [ssaps_add_property](#ssaps_add_property) | 异步添加一个 SSAP 特征，句柄在回调中返回 |
| [ssaps_add_descriptor](#ssaps_add_descriptor) | 异步添加一个 SSAP 特征描述符，结果在回调中返回 |
| [ssaps_add_service_sync](#ssaps_add_service_sync) | 同步添加一个 SSAP 服务，句柄由出参返回 |
| [ssaps_add_property_sync](#ssaps_add_property_sync) | 同步添加一个 SSAP 特征，句柄由出参返回 |
| [ssaps_add_descriptor_sync](#ssaps_add_descriptor_sync) | 添加一个 SSAP 特征描述符 |
| [ssaps_start_service](#ssaps_start_service) | 启动指定的 SSAP 服务，结果在回调中返回 |
| [ssaps_delete_all_services](#ssaps_delete_all_services) | 删除指定服务端的全部 SSAP 服务 |
| [ssaps_send_response](#ssaps_send_response) | 收到需用户回复的请求时发送响应 |
| [ssaps_notify_indicate](#ssaps_notify_indicate) | 按句柄向对端发送通知或指示 |
| [ssaps_notify_indicate_by_uuid](#ssaps_notify_indicate_by_uuid) | 按 UUID 向对端发送通知或指示 |
| [ssaps_set_info](#ssaps_set_info) | 在连接之前设置服务端交换信息（如 MTU） |
| [ssaps_register_callbacks](#ssaps_register_callbacks) | 注册 SSAP 服务端回调函数集合 |

## Functions

### ssaps_register_server <a id="ssaps_register_server"></a>

```c
errcode_t ssaps_register_server(sle_uuid_t *app_uuid, uint8_t *server_id)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_server.h"
```

**功能说明**

- 注册 SSAP 服务端，向上层应用分配并返回服务端 ID
- 以应用 UUID 标识上层应用身份
- 注册成功后该服务端 ID 可用于后续添加服务、特征、启动服务等操作

**前置条件**

- 调用时序约束：当前接口必须在 SLE 协议栈初始化完成后调用
- 依赖关系：当前接口依赖 SLE service 已就绪

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| app_uuid | [sle_uuid_t](#struct_sle_uuid_t) * | 上层应用 UUID | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| server_id | uint8_t * | 由 SLE service 分配的服务端 ID，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0 | 成功 | 注册成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 注册失败 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`

### ssaps_unregister_server <a id="ssaps_unregister_server"></a>

```c
errcode_t ssaps_unregister_server(uint8_t server_id)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_server.h"
```

**功能说明**

- 注销已注册的 SSAP 服务端
- 释放该服务端 ID 占用的资源
- 注销后该服务端 ID 不再可用于添加服务、启动服务等操作

**前置条件**

- 调用时序约束：当前接口必须在 [ssaps_register_server](#ssaps_register_server) 成功返回后调用
- 依赖关系：当前接口依赖传入的服务端 ID 已通过注册获得

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 已通过 [ssaps_register_server](#ssaps_register_server) 获得的有效 ID |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0 | 成功 | 注销成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 注销失败 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`

### ssaps_add_service <a id="ssaps_add_service"></a>

```c
errcode_t ssaps_add_service(uint8_t server_id, sle_uuid_t *service_uuid, bool is_primary)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_server.h"
```

**功能说明**

- 异步添加一个 SSAP 服务
- 注册的 service handle 在 [ssaps_add_service_callback](#typedef_ssaps_add_service_callback) 中返回
- 服务添加结果通过注册的服务端回调通知上层应用

**前置条件**

- 调用时序约束：当前接口必须在 [ssaps_register_server](#ssaps_register_server) 成功返回后调用
- 依赖关系：当前接口依赖已通过 [ssaps_register_callbacks](#ssaps_register_callbacks) 注册回调函数以接收服务添加结果

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 已通过 [ssaps_register_server](#ssaps_register_server) 获得的有效 ID |
| service_uuid | [sle_uuid_t](#struct_sle_uuid_t) * | 服务 UUID | 不为NULL |
| is_primary | bool | 是否为首要服务 | true / false |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0 | 执行成功 | 请求发起成功；服务句柄将在 [ssaps_add_service_callback](#typedef_ssaps_add_service_callback) 中返回 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 请求发起失败 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 请求失败 |

### ssaps_add_property <a id="ssaps_add_property"></a>

```c
errcode_t ssaps_add_property(uint8_t server_id, uint16_t service_handle, ssaps_property_info_t *property)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_server.h"
```

**功能说明**

- 异步添加一个 SSAP 特征
- 注册的特征 handle 在 [ssaps_add_property_callback](#typedef_ssaps_add_property_callback) 中返回
- 特征添加结果通过注册的服务端回调通知上层应用

**前置条件**

- 调用时序约束：当前接口必须在 [ssaps_add_service](#ssaps_add_service) 或 [ssaps_add_service_sync](#ssaps_add_service_sync) 成功并获得 service_handle 后调用
- 依赖关系：当前接口依赖已通过 [ssaps_register_callbacks](#ssaps_register_callbacks) 注册回调函数以接收特征添加结果

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 已通过 [ssaps_register_server](#ssaps_register_server) 获得的有效 ID |
| service_handle | uint16_t | 服务句柄 | 已通过 [ssaps_add_service](#ssaps_add_service) 回调或 [ssaps_add_service_sync](#ssaps_add_service_sync) 出参获得的有效句柄 |
| property | [ssaps_property_info_t](#struct_ssaps_property_info_t) * | SSAP 特征信息 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0 | 执行成功 | 请求发起成功；特征句柄将在 [ssaps_add_property_callback](#typedef_ssaps_add_property_callback) 中返回 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 请求发起失败 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 请求失败 |

### ssaps_add_descriptor <a id="ssaps_add_descriptor"></a>

```c
errcode_t ssaps_add_descriptor(uint8_t server_id, uint16_t service_handle, uint16_t property_handle,
    ssaps_desc_info_t *descriptor)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_server.h"
```

**功能说明**

- 异步添加一个 SSAP 特征描述符
- 注册结果在 [ssaps_add_descriptor_callback](#typedef_ssaps_add_descriptor_callback) 中返回
- 描述符添加结果通过注册的服务端回调通知上层应用

**前置条件**

- 调用时序约束：当前接口必须在 [ssaps_add_property](#ssaps_add_property) 或 [ssaps_add_property_sync](#ssaps_add_property_sync) 成功并获得 property_handle 后调用
- 依赖关系：当前接口依赖已通过 [ssaps_register_callbacks](#ssaps_register_callbacks) 注册回调函数以接收描述符添加结果

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 已通过 [ssaps_register_server](#ssaps_register_server) 获得的有效 ID |
| service_handle | uint16_t | 服务句柄 | 已通过 [ssaps_add_service](#ssaps_add_service) 回调或 [ssaps_add_service_sync](#ssaps_add_service_sync) 出参获得的有效句柄 |
| property_handle | uint16_t | 特征句柄 | 已通过 [ssaps_add_property](#ssaps_add_property) 回调或 [ssaps_add_property_sync](#ssaps_add_property_sync) 出参获得的有效句柄 |
| descriptor | [ssaps_desc_info_t](#struct_ssaps_desc_info_t) * | SSAP 特征描述符 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0 | 执行成功 | 请求发起成功；描述符句柄将在 [ssaps_add_descriptor_callback](#typedef_ssaps_add_descriptor_callback) 中返回 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 请求发起失败 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 请求失败 |

### ssaps_add_service_sync <a id="ssaps_add_service_sync"></a>

```c
errcode_t ssaps_add_service_sync(uint8_t server_id, sle_uuid_t *service_uuid, bool is_primary, uint16_t *handle)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_server.h"
```

**功能说明**

- 同步添加一个 SSAP 服务
- 服务句柄由出参 handle 返回
- 调用返回即表示添加操作已完成，无需经回调获取句柄

**前置条件**

- 调用时序约束：当前接口必须在 [ssaps_register_server](#ssaps_register_server) 成功返回后调用
- 依赖关系：当前接口依赖 SLE service 已就绪

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 已通过 [ssaps_register_server](#ssaps_register_server) 获得的有效 ID |
| service_uuid | [sle_uuid_t](#struct_sle_uuid_t) * | 服务 UUID | 不为NULL |
| is_primary | bool | 是否为首要服务 | true / false |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| handle | uint16_t * | 服务句柄，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0 | 成功 | 服务添加成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 服务添加失败 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`

### ssaps_add_property_sync <a id="ssaps_add_property_sync"></a>

```c
errcode_t ssaps_add_property_sync(uint8_t server_id, uint16_t service_handle, ssaps_property_info_t *property,
    uint16_t *handle)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_server.h"
```

**功能说明**

- 同步添加一个 SSAP 特征
- 特征句柄由出参 handle 返回
- 调用返回即表示添加操作已完成，无需经回调获取句柄

**前置条件**

- 调用时序约束：当前接口必须在 [ssaps_add_service_sync](#ssaps_add_service_sync) 或 [ssaps_add_service](#ssaps_add_service) 成功并获得 service_handle 后调用
- 依赖关系：当前接口依赖 SLE service 已就绪

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 已通过 [ssaps_register_server](#ssaps_register_server) 获得的有效 ID |
| service_handle | uint16_t | 服务句柄 | 已通过 [ssaps_add_service](#ssaps_add_service) 回调或 [ssaps_add_service_sync](#ssaps_add_service_sync) 出参获得的有效句柄 |
| property | [ssaps_property_info_t](#struct_ssaps_property_info_t) * | SSAP 特征信息 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| handle | uint16_t * | 特征句柄，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0 | 成功 | 特征添加成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 特征添加失败 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`

### ssaps_add_descriptor_sync <a id="ssaps_add_descriptor_sync"></a>

```c
errcode_t ssaps_add_descriptor_sync(uint8_t server_id, uint16_t service_handle, uint16_t property_handle,
    ssaps_desc_info_t *descriptor)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_server.h"
```

**功能说明**

- 添加一个 SSAP 特征描述符
- 将描述符挂载到指定的特征句柄下
- 调用返回即表示添加操作已完成

**前置条件**

- 调用时序约束：当前接口必须在 [ssaps_add_property_sync](#ssaps_add_property_sync) 或 [ssaps_add_property](#ssaps_add_property) 成功并获得 property_handle 后调用
- 依赖关系：当前接口依赖 SLE service 已就绪

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 已通过 [ssaps_register_server](#ssaps_register_server) 获得的有效 ID |
| service_handle | uint16_t | 服务句柄 | 已通过 [ssaps_add_service](#ssaps_add_service) 回调或 [ssaps_add_service_sync](#ssaps_add_service_sync) 出参获得的有效句柄 |
| property_handle | uint16_t | 描述符所属特征句柄 | 已通过 [ssaps_add_property](#ssaps_add_property) 回调或 [ssaps_add_property_sync](#ssaps_add_property_sync) 出参获得的有效句柄 |
| descriptor | [ssaps_desc_info_t](#struct_ssaps_desc_info_t) * | 特征描述符 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0 | 成功 | 描述符添加成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 描述符添加失败 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`

### ssaps_start_service <a id="ssaps_start_service"></a>

```c
errcode_t ssaps_start_service(uint8_t server_id, uint16_t service_handle)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_server.h"
```

**功能说明**

- 启动指定的 SSAP 服务
- 服务启动结果在 [ssaps_start_service_callback](#typedef_ssaps_start_service_callback) 中返回
- 服务启动后可被远端客户端发现并访问

**前置条件**

- 调用时序约束：当前接口必须在服务及其特征/描述符添加完成（[ssaps_add_service](#ssaps_add_service) / [ssaps_add_service_sync](#ssaps_add_service_sync) 及对应特征、描述符接口）后调用
- 依赖关系：当前接口依赖已通过 [ssaps_register_callbacks](#ssaps_register_callbacks) 注册回调函数以接收服务启动结果

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 已通过 [ssaps_register_server](#ssaps_register_server) 获得的有效 ID |
| service_handle | uint16_t | 服务句柄 | 已通过 [ssaps_add_service](#ssaps_add_service) 回调或 [ssaps_add_service_sync](#ssaps_add_service_sync) 出参获得的有效句柄 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0 | 执行成功 | 请求发起成功；服务启动结果将在 [ssaps_start_service_callback](#typedef_ssaps_start_service_callback) 中返回 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 请求发起失败 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 请求失败 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`

### ssaps_delete_all_services <a id="ssaps_delete_all_services"></a>

```c
errcode_t ssaps_delete_all_services(uint8_t server_id)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_server.h"
```

**功能说明**

- 删除指定服务端的全部 SSAP 服务
- 删除结果在 [ssaps_delete_all_service_callback](#typedef_ssaps_delete_all_service_callback) 中通知
- 删除后该服务端下的全部服务、特征、描述符不再可用

**前置条件**

- 调用时序约束：当前接口必须在 [ssaps_register_server](#ssaps_register_server) 成功返回后调用
- 依赖关系：当前接口依赖已通过 [ssaps_register_callbacks](#ssaps_register_callbacks) 注册回调函数以接收删除结果

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 已通过 [ssaps_register_server](#ssaps_register_server) 获得的有效 ID |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0 | 成功 | 删除请求成功发起 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 删除请求失败 |

### ssaps_send_response <a id="ssaps_send_response"></a>

```c
errcode_t ssaps_send_response(uint8_t server_id, uint16_t conn_id, ssaps_send_rsp_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_server.h"
```

**功能说明**

- 当收到需要用户回复响应的读/写请求时，向对端发送响应
- 与 [ssaps_read_request_callback](#typedef_ssaps_read_request_callback) / [ssaps_write_request_callback](#typedef_ssaps_write_request_callback) 配合使用
- 响应内容由调用方通过 param 指定

**前置条件**

- 调用时序约束：当前接口必须在收到读/写请求回调（[ssaps_read_request_callback](#typedef_ssaps_read_request_callback) / [ssaps_write_request_callback](#typedef_ssaps_write_request_callback)）且 need_rsp 为 true 后调用
- 依赖关系：当前接口依赖传入的 conn_id 对应的连接仍处于有效状态

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 已通过 [ssaps_register_server](#ssaps_register_server) 获得的有效 ID |
| conn_id | uint16_t | 连接 ID | 有效的连接 ID |
| param | [ssaps_send_rsp_t](#struct_ssaps_send_rsp_t) * | 响应参数 | 不为NULL |

**参考案例**

- `src/application/samples/bt/sle/sle_device_config/sle_device_config_server/src/sle_device_config_server.c`

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0 | 成功 | 响应发送成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 响应发送失败 |

### ssaps_notify_indicate <a id="ssaps_notify_indicate"></a>

```c
errcode_t ssaps_notify_indicate(uint8_t server_id, uint16_t conn_id, ssaps_ntf_ind_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_server.h"
```

**功能说明**

- 按特征句柄向对端发送通知或指示
- 具体发送状态取决于特征描述符：客户端特征配置（value=0x0000 不允许通知与指示；value=0x0001 允许通知；value=0x0002 允许指示）
- 通过指定 conn_id = 0xffff 可向全部对端发送

**前置条件**

- 调用时序约束：当前接口必须在服务启动（[ssaps_start_service](#ssaps_start_service)）成功后调用
- 依赖关系：当前接口依赖特征已配置对应的通知或指示操作指示位，且对端已使能相应配置

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 已通过 [ssaps_register_server](#ssaps_register_server) 获得的有效 ID |
| conn_id | uint16_t | 连接 ID，向全部对端发送时填 0xffff | 有效连接 ID 或 0xffff |
| param | [ssaps_ntf_ind_t](#struct_ssaps_ntf_ind_t) * | 通知或指示参数 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0 | 成功 | 通知或指示发送成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 通知或指示发送失败 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`

### ssaps_notify_indicate_by_uuid <a id="ssaps_notify_indicate_by_uuid"></a>

```c
errcode_t ssaps_notify_indicate_by_uuid(uint8_t server_id, uint16_t conn_id, ssaps_ntf_ind_by_uuid_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_server.h"
```

**功能说明**

- 按特征 UUID 向对端发送通知或指示
- 具体发送状态取决于客户端特征配置描述符值（value=0x0000 不允许通知与指示；value=0x0001 允许通知；value=0x0002 允许指示）
- 通过指定 conn_id = 0xffff 可向全部对端发送

**前置条件**

- 调用时序约束：当前接口必须在服务启动（[ssaps_start_service](#ssaps_start_service)）成功后调用
- 依赖关系：当前接口依赖 UUID 对应特征已配置对应的通知或指示操作指示位，且对端已使能相应配置

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 已通过 [ssaps_register_server](#ssaps_register_server) 获得的有效 ID |
| conn_id | uint16_t | 连接 ID，向全部对端发送时填 0xffff | 有效连接 ID 或 0xffff |
| param | [ssaps_ntf_ind_by_uuid_t](#struct_ssaps_ntf_ind_by_uuid_t) * | 通知或指示参数 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0 | 成功 | 通知或指示发送成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 通知或指示发送失败 |

### ssaps_set_info <a id="ssaps_set_info"></a>

```c
errcode_t ssaps_set_info(uint8_t server_id, ssap_exchange_info_t *info)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_server.h"
```

**功能说明**

- 在连接之前设置服务端交换信息（如 MTU (Maximum Transmission Unit) 大小）
- 设置的信息在后续 SSAP 交换流程中生效
- 通过该接口可在建立连接前预置服务端期望的交换参数

**前置条件**

- 调用时序约束：当前接口必须在 [ssaps_register_server](#ssaps_register_server) 成功返回后、建立 SLE 连接之前调用
- 依赖关系：当前接口依赖 SLE service 已就绪

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | 服务端 ID | 已通过 [ssaps_register_server](#ssaps_register_server) 获得的有效 ID |
| info | [ssap_exchange_info_t](#struct_ssap_exchange_info_t) * | 服务端交换信息 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0 | 成功 | 设置成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 设置失败 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`

### ssaps_register_callbacks <a id="ssaps_register_callbacks"></a>

```c
errcode_t ssaps_register_callbacks(ssaps_callbacks_t *func)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_ssap_server.h"
```

**功能说明**

- 注册 SSAP 服务端回调函数集合
- 通过回调集合接收服务/特征/描述符添加、服务启动/删除、读/写请求、MTU 改变、指示确认等事件通知
- 回调函数运行于 SLE service 线程，回调内不应阻塞或长时间等待

**前置条件**

- 调用时序约束：当前接口必须在 [ssaps_register_server](#ssaps_register_server) 成功返回后、发起添加服务/启动服务等异步操作之前调用
- 依赖关系：当前接口依赖传入的回调函数集合各成员已正确初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func | [ssaps_callbacks_t](#struct_ssaps_callbacks_t) * | 回调函数集合 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0 | 成功 | 注册成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 注册失败 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`

## Type definitions

### typedef_errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块返回类型为 errcode_t 的对外接口的返回值类型。

### ssaps_add_service_callback <a id="typedef_ssaps_add_service_callback"></a>

```c
typedef void (*ssaps_add_service_callback)(uint8_t server_id, sle_uuid_t *uuid, uint16_t handle, errcode_t status);
```

**使用说明**

服务注册的回调函数类型。回调说明：调用时机为异步添加服务产生结果时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 uuid 指向服务 UUID，由 SLE service 申请内存并释放，回调中不应释放；参数 handle 为注册成功时返回的服务属性句柄；参数 status 为执行结果错误码。

### ssaps_add_property_callback <a id="typedef_ssaps_add_property_callback"></a>

```c
typedef void (*ssaps_add_property_callback)(uint8_t server_id, sle_uuid_t *uuid, uint16_t service_handle,
                                            uint16_t handle, errcode_t status);
```

**使用说明**

特征注册的回调函数类型。回调说明：调用时机为异步添加特征产生结果时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 uuid 指向特征 UUID，由 SLE service 申请内存并释放，回调中不应释放；参数 service_handle 为所属服务属性句柄；参数 handle 为注册成功时返回的特征属性句柄；参数 status 为执行结果错误码。

### ssaps_add_descriptor_callback <a id="typedef_ssaps_add_descriptor_callback"></a>

```c
typedef void (*ssaps_add_descriptor_callback)(uint8_t server_id, sle_uuid_t *uuid, uint16_t service_handle,
    uint16_t property_handle, errcode_t status);
```

**使用说明**

特征描述符注册的回调函数类型。回调说明：调用时机为异步添加特征描述符产生结果时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 uuid 指向特征 UUID，由 SLE service 申请内存并释放，回调中不应释放；参数 service_handle 为所属服务属性句柄；参数 property_handle 为特征描述符所属的特征属性句柄；参数 status 为执行结果错误码。

### ssaps_start_service_callback <a id="typedef_ssaps_start_service_callback"></a>

```c
typedef void (*ssaps_start_service_callback)(uint8_t server_id, uint16_t handle, errcode_t status);
```

**使用说明**

开始服务的回调函数类型。回调说明：调用时机为启动服务产生结果时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 handle 为被启动服务的属性句柄；参数 status 为执行结果错误码。

### ssaps_delete_all_service_callback <a id="typedef_ssaps_delete_all_service_callback"></a>

```c
typedef void (*ssaps_delete_all_service_callback)(uint8_t server_id, errcode_t status);
```

**使用说明**

删除全部服务的回调函数类型。回调说明：调用时机为删除全部服务产生结果时由 bts 调用，运行于 bts 线程，不应阻塞或长时间等待；参数 server_id 为服务端 ID；参数 status 为执行结果错误码。

### ssaps_read_request_callback <a id="typedef_ssaps_read_request_callback"></a>

```c
typedef void (*ssaps_read_request_callback)(uint8_t server_id, uint16_t conn_id, ssaps_req_read_cb_t *read_cb_para,
                                            errcode_t status);
```

**使用说明**

收到读请求的回调函数类型。回调说明：调用时机为收到对端读请求时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 conn_id 为连接 ID；参数 read_cb_para 指向读请求参数，由 SLE service 申请内存并释放，回调中不应释放；参数 status 为执行结果错误码。

### ssaps_read_by_uuid_request_callback <a id="typedef_ssaps_read_by_uuid_request_callback"></a>

```c
typedef void (*ssaps_read_by_uuid_request_callback)(uint8_t server_id, uint16_t conn_id,
                                                    ssaps_req_read_by_uuid_cb_t *read_cb_para, errcode_t status);
```

**使用说明**

收到基于 UUID 读请求的回调函数类型。回调说明：调用时机为收到对端基于 UUID 读请求时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 conn_id 为连接 ID；参数 read_cb_para 指向基于 UUID 读请求参数，由 SLE service 申请内存并释放，回调中不应释放；参数 status 为执行结果错误码。

### ssaps_write_request_callback <a id="typedef_ssaps_write_request_callback"></a>

```c
typedef void (*ssaps_write_request_callback)(uint8_t server_id, uint16_t conn_id, ssaps_req_write_cb_t *write_cb_para,
                                             errcode_t status);
```

**使用说明**

收到写请求的回调函数类型。回调说明：调用时机为收到对端写请求时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 conn_id 为连接 ID；参数 write_cb_para 指向写请求参数，由 SLE service 申请内存并释放，回调中不应释放；参数 status 为执行结果错误码。

### ssaps_indicate_cfm_callback <a id="typedef_ssaps_indicate_cfm_callback"></a>

```c
typedef void (*ssaps_indicate_cfm_callback)(uint8_t server_id, uint16_t conn_id, sle_indication_cfm_result_t cfm_result,
                                            errcode_t status);
```

**使用说明**

收到指示确认的回调函数类型。回调说明：调用时机为收到对端指示确认时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 conn_id 为连接 ID；参数 cfm_result 为指示确认结果（[SLE_INDICATION_CFM_FAIL](#enum_sle_indication_cfm_result_t) / [SLE_INDICATION_CFM_SUCESS](#enum_sle_indication_cfm_result_t)）；参数 status 为执行结果错误码。

### ssaps_mtu_changed_callback <a id="typedef_ssaps_mtu_changed_callback"></a>

```c
typedef void (*ssaps_mtu_changed_callback)(uint8_t server_id, uint16_t conn_id, ssap_exchange_info_t *info,
                                           errcode_t status);
```

**使用说明**

MTU 大小改变的回调函数类型。回调说明：调用时机为 MTU 大小改变时由 SLE service 调用，运行于 SLE service 线程，不应阻塞或长时间等待；参数 conn_id 为连接 ID；参数 info 指向交换信息，由 SLE service 申请内存并释放，回调中不应释放；参数 status 为执行结果错误码。

## Enumerations

### sle_indication_cfm_result_t <a id="enum_sle_indication_cfm_result_t"></a>

```c
typedef enum {
    SLE_INDICATION_CFM_FAIL           = 0x00,
    SLE_INDICATION_CFM_SUCESS         = 0x01,
} sle_indication_cfm_result_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_INDICATION_CFM_FAIL | 0x00 | 指示接收失败 |
| SLE_INDICATION_CFM_SUCESS | 0x01 | 指示接收成功 |

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

### ssaps_property_info_t <a id="struct_ssaps_property_info_t"></a>

```c
typedef struct {
    sle_uuid_t uuid;
    uint16_t permissions;
    uint32_t operate_indication;
    uint16_t value_len;
    uint8_t *value;
} ssaps_property_info_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| uuid | sle_uuid_t | SSAP 特征 UUID |
| permissions | uint16_t | 特征权限 |
| operate_indication | uint32_t | 操作指示 |
| value_len | uint16_t | 响应的数据长度 |
| value | uint8_t * | 响应的数据 |

### ssaps_desc_info_t <a id="struct_ssaps_desc_info_t"></a>

```c
typedef struct {
    sle_uuid_t uuid;
    uint16_t permissions;
    uint32_t operate_indication;
    uint8_t type;
    uint16_t value_len;
    uint8_t *value;
} ssaps_desc_info_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| uuid | sle_uuid_t | SSAP 描述符 UUID |
| permissions | uint16_t | 特征权限 |
| operate_indication | uint32_t | 操作指示 |
| type | uint8_t | 描述符类型 |
| value_len | uint16_t | 数据长度 |
| value | uint8_t * | 数据 |

### ssaps_req_read_cb_t <a id="struct_ssaps_req_read_cb_t"></a>

```c
typedef struct {
    uint16_t request_id;
    uint16_t handle;
    uint8_t type;
    bool need_rsp;
    bool need_authorize;
} ssaps_req_read_cb_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| request_id | uint16_t | 请求 ID |
| handle | uint16_t | 请求读的属性句柄 |
| type | uint8_t | 属性类型 |
| need_rsp | bool | 是否需要发送响应 |
| need_authorize | bool | 是否授权 |

### ssaps_req_read_by_uuid_cb_t <a id="struct_ssaps_req_read_by_uuid_cb_t"></a>

```c
typedef struct {
    uint16_t request_id;
    uint16_t begin_handle;
    uint16_t end_handle;
    uint8_t type;
    sle_uuid_t uuid;
    bool need_rsp;
    bool need_authorize;
} ssaps_req_read_by_uuid_cb_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| request_id | uint16_t | 请求 ID |
| begin_handle | uint16_t | 请求读的起始属性句柄 |
| end_handle | uint16_t | 请求读的结束属性句柄 |
| type | uint8_t | 属性类型 |
| uuid | sle_uuid_t | 属性 UUID |
| need_rsp | bool | 是否需要发送响应 |
| need_authorize | bool | 是否授权 |

### ssaps_req_write_cb_t <a id="struct_ssaps_req_write_cb_t"></a>

```c
typedef struct {
    uint16_t request_id;
    uint16_t handle;
    uint8_t type;
    bool need_rsp;
    bool need_authorize;
    uint16_t length;
    uint8_t *value;
} ssaps_req_write_cb_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| request_id | uint16_t | 请求 ID |
| handle | uint16_t | 请求写的属性句柄 |
| type | uint8_t | 属性类型 |
| need_rsp | bool | 是否需要发送响应 |
| need_authorize | bool | 是否授权 |
| length | uint16_t | 请求写的数据长度 |
| value | uint8_t * | 请求写的数据 |

### ssaps_send_rsp_t <a id="struct_ssaps_send_rsp_t"></a>

```c
typedef struct {
    uint16_t request_id;
    uint8_t status;
    uint16_t value_len;
    uint8_t *value;
} ssaps_send_rsp_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| request_id | uint16_t | 请求 ID |
| status | uint8_t | 读写结果的状态，成功为 ERRCODE_SLE_SUCCESS，异常参考 errcode_sle_ssap_t |
| value_len | uint16_t | 响应的数据长度 |
| value | uint8_t * | 响应的数据 |

### ssaps_ntf_ind_t <a id="struct_ssaps_ntf_ind_t"></a>

```c
typedef struct {
    uint16_t handle;
    uint8_t type;
    uint16_t value_len;
    uint8_t *value;
} ssaps_ntf_ind_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| handle | uint16_t | 属性句柄 |
| type | uint8_t | 属性类型 |
| value_len | uint16_t | 通知/指示数据长度 |
| value | uint8_t * | 发送的通知/指示数据 |

### ssaps_ntf_ind_by_uuid_t <a id="struct_ssaps_ntf_ind_by_uuid_t"></a>

```c
typedef struct {
    sle_uuid_t uuid;
    uint16_t start_handle;
    uint16_t end_handle;
    uint8_t type;
    uint16_t value_len;
    uint8_t *value;
} ssaps_ntf_ind_by_uuid_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| uuid | sle_uuid_t | 特征 UUID |
| start_handle | uint16_t | 起始句柄 |
| end_handle | uint16_t | 结束句柄 |
| type | uint8_t | 属性类型 |
| value_len | uint16_t | 通知/指示数据长度 |
| value | uint8_t * | 发送的通知/指示数据 |

### ssaps_callbacks_t <a id="struct_ssaps_callbacks_t"></a>

```c
typedef struct {
    ssaps_add_service_callback add_service_cb;
    ssaps_add_property_callback add_property_cb;
    ssaps_add_descriptor_callback add_descriptor_cb;
    ssaps_start_service_callback start_service_cb;
    ssaps_delete_all_service_callback delete_all_service_cb;
    ssaps_read_request_callback read_request_cb;
    ssaps_read_by_uuid_request_callback read_by_uuid_request_cb;
    ssaps_write_request_callback write_request_cb;
    ssaps_mtu_changed_callback mtu_changed_cb;
    ssaps_indicate_cfm_callback indicate_cfm_cb;
} ssaps_callbacks_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| add_service_cb | ssaps_add_service_callback | 添加服务回调函数 |
| add_property_cb | ssaps_add_property_callback | 添加特征回调函数 |
| add_descriptor_cb | ssaps_add_descriptor_callback | 添加描述符回调函数 |
| start_service_cb | ssaps_start_service_callback | 启动服务回调函数 |
| delete_all_service_cb | ssaps_delete_all_service_callback | 删除服务回调函数 |
| read_request_cb | ssaps_read_request_callback | 收到远端读请求回调函数 |
| read_by_uuid_request_cb | ssaps_read_by_uuid_request_callback | 收到远端基于 UUID 读请求回调函数 |
| write_request_cb | ssaps_write_request_callback | 收到远端写请求回调函数 |
| mtu_changed_cb | ssaps_mtu_changed_callback | MTU 大小更新回调函数 |
| indicate_cfm_cb | ssaps_indicate_cfm_callback | 指示确认回调函数 |

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```

### SLE_UUID_LEN <a id="SLE_UUID_LEN"></a>

```c
#define SLE_UUID_LEN 16
```
