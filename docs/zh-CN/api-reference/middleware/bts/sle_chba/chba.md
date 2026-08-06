# chba

SLE (Star Flash Low Energy) CHBA manager 提供 SLE CHBA 网络设备管理能力，支持基于 SLE 链路的网络设备创建、销毁、链路维护与数据收发，并通过回调机制向上层通知发送队列状态、链路状态及上行数据。

**头文件清单**

```c
#include "include/middleware/services/bts/sle_chba/sle_chba_manager.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [sle_chba_netdev_create](#sle_chba_netdev_create) | 创建 SLE CHBA 网络设备并指定角色与模式 |
| [sle_chba_netdev_destroy](#sle_chba_netdev_destroy) | 销毁已创建的 SLE CHBA 网络设备 |
| [sle_chba_netdev_add_link](#sle_chba_netdev_add_link) | 向 SLE CHBA 网络设备添加一条链路 |
| [sle_chba_netdev_del_link](#sle_chba_netdev_del_link) | 从 SLE CHBA 网络设备删除一条链路 |
| [sle_chba_netdev_get_linkinfo](#sle_chba_netdev_get_linkinfo) | 查询指定连接 ID 对应的链路信息 |
| [sle_chba_netdev_driver_send](#sle_chba_netdev_driver_send) | 通过 SLE CHBA 网络设备驱动发送数据 |
| [sle_chba_netdev_register_callbacks](#sle_chba_netdev_register_callbacks) | 注册 SLE CHBA 网络设备事件回调函数集 |

## Functions

### sle_chba_netdev_create <a id="sle_chba_netdev_create"></a>

```c
errcode_t sle_chba_netdev_create(uint8_t chba_role, uint8_t chba_mode)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle_chba/sle_chba_manager.h"
```

**功能说明**

- 创建一个 SLE CHBA 网络设备实例
- 按入参指定的设备角色（AP (Access Point) 或 STA (Station)）与工作模式初始化该网络设备
- 为后续的链路添加、数据收发及回调注册提供运行基础

**前置条件**

- 调用时序约束：当前接口必须在 SLE 协议栈初始化完成、SLE 设备使能后调用
- 依赖关系：当前接口依赖底层 SLE 链路资源及本地设备地址已就绪

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| chba_role | uint8_t | SLE CHBA 设备角色，取值参考 [sle_chba_role](#enum_sle_chba_role) | [CHBA_ROLE_AP](#enum_sle_chba_role)(0) / [CHBA_ROLE_STA](#enum_sle_chba_role)(1) |
| chba_mode | uint8_t | SLE CHBA 工作模式 | 0 ~ 255 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| errcode_t | - | - |

**参考案例**

- `application/samples/bt/sle_chba/src/sle_chba_server.c`

### sle_chba_netdev_destroy <a id="sle_chba_netdev_destroy"></a>

```c
errcode_t sle_chba_netdev_destroy(void)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle_chba/sle_chba_manager.h"
```

**功能说明**

- 销毁已创建的 SLE CHBA 网络设备实例
- 释放网络设备相关运行资源
- 解除后续链路维护与数据收发的运行基础

**前置条件**

- 调用时序约束：当前接口必须在 [sle_chba_netdev_create](#sle_chba_netdev_create) 成功返回后调用
- 依赖关系：当前接口执行前应已完成所有链路的删除与数据收发停止

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| errcode_t | - | - |

### sle_chba_netdev_add_link <a id="sle_chba_netdev_add_link"></a>

```c
errcode_t sle_chba_netdev_add_link(uint16_t conn_id, const sle_addr_t *remote_addr)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle_chba/sle_chba_manager.h"
```

**功能说明**

- 向 SLE CHBA 网络设备添加一条对端链路
- 以连接 ID 与对端设备地址标识该链路
- 链路添加成功后即可用于后续的数据收发与链路信息查询

**前置条件**

- 调用时序约束：当前接口必须在 [sle_chba_netdev_create](#sle_chba_netdev_create) 成功返回后调用，且对应 conn_id 的 SLE 连接已建立
- 依赖关系：当前接口依赖入参 remote_addr 指向有效的对端设备地址

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| conn_id | uint16_t | SLE 连接 ID，用于标识一条链路 | 0 ~ 65535 |
| remote_addr | const sle_addr_t * | 对端 SLE 设备地址指针 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| errcode_t | - | - |

**参考案例**

- `application/samples/bt/sle_chba/src/sle_chba_server.c`

### sle_chba_netdev_del_link <a id="sle_chba_netdev_del_link"></a>

```c
errcode_t sle_chba_netdev_del_link(uint16_t conn_id, const sle_addr_t *remote_addr)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle_chba/sle_chba_manager.h"
```

**功能说明**

- 从 SLE CHBA 网络设备删除一条已添加的对端链路
- 按连接 ID 与对端设备地址定位待删除的链路
- 链路删除后不再参与后续数据收发与链路信息查询

**前置条件**

- 调用时序约束：当前接口必须在 [sle_chba_netdev_add_link](#sle_chba_netdev_add_link) 添加对应链路后调用
- 依赖关系：当前接口依赖入参 remote_addr 指向有效的对端设备地址

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| conn_id | uint16_t | SLE 连接 ID，用于标识待删除链路 | 0 ~ 65535 |
| remote_addr | const sle_addr_t * | 对端 SLE 设备地址指针 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| errcode_t | - | - |

**参考案例**

- `application/samples/bt/sle_chba/src/sle_chba_server.c`

### sle_chba_netdev_get_linkinfo <a id="sle_chba_netdev_get_linkinfo"></a>

```c
errcode_t sle_chba_netdev_get_linkinfo(uint16_t conn_id, sle_ip_link_info *link)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle_chba/sle_chba_manager.h"
```

**功能说明**

- 查询指定连接 ID 对应链路的统计信息
- 输出对端设备地址与该链路的收发包计数及收发字节数
- 供上层获取链路运行状态

**前置条件**

- 调用时序约束：当前接口必须在 [sle_chba_netdev_add_link](#sle_chba_netdev_add_link) 添加对应链路后调用
- 依赖关系：当前接口依赖入参 link 指向调用方分配的 [sle_ip_link_info](#struct_sle_ip_link_info) 存储空间

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| conn_id | uint16_t | SLE 连接 ID，用于标识待查询链路 | 0 ~ 65535 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| link | sle_ip_link_info * | 调用方分配内存、接口填充的链路信息，包含连接 ID、对端地址与收发统计 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| errcode_t | - | - |

### sle_chba_netdev_driver_send <a id="sle_chba_netdev_driver_send"></a>

```c
errcode_t sle_chba_netdev_driver_send(uint8_t *data, uint16_t len)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle_chba/sle_chba_manager.h"
```

**功能说明**

- 通过 SLE CHBA 网络设备驱动发送一帧数据
- 按入参 data 与 len 指定的数据缓冲区及长度执行发送
- 供上层网络协议栈在 SLE CHBA 链路上进行数据发送

**前置条件**

- 调用时序约束：当前接口必须在 [sle_chba_netdev_create](#sle_chba_netdev_create) 成功返回且至少添加一条链路后调用
- 依赖关系：当前接口依赖入参 data 指向有效的待发送数据缓冲区

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| data | uint8_t * | 待发送数据缓冲区指针 | 不为 NULL |
| len | uint16_t | 待发送数据长度，单位字节 | 0 ~ 65535 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| errcode_t | - | - |

**参考案例**

- `application/samples/bt/sle_chba/src/sle_chba_netif_mng.c`
- `application/samples/bt/sle_chba/src/sle_chba_bridge.c`

### sle_chba_netdev_register_callbacks <a id="sle_chba_netdev_register_callbacks"></a>

```c
errcode_t sle_chba_netdev_register_callbacks(sle_chba_netdev_callbacks_t *func)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle_chba/sle_chba_manager.h"
```

**功能说明**

- 向 SLE CHBA 网络设备注册一组事件回调函数
- 注册的回调用于通知发送队列停止/唤醒、链路启用/禁用及上行数据上报
- 注册后由网络设备在对应事件发生时回调，回调返回值在当前实现中不被检查

**前置条件**

- 调用时序约束：当前接口必须在 [sle_chba_netdev_create](#sle_chba_netdev_create) 成功返回后调用
- 依赖关系：当前接口依赖入参 func 指向调用方填充好的 [sle_chba_netdev_callbacks_t](#struct_sle_chba_netdev_callbacks_t) 结构体

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func | sle_chba_netdev_callbacks_t * | 回调函数集结构体指针，包含停止/唤醒发送队列、链路启用/禁用、上行数据上报等回调 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| errcode_t | - | - |

**参考案例**

- `application/samples/bt/sle_chba/src/sle_chba_netif_mng.c`

## Type definitions

### sle_chba_netdev_stop_queue_callback <a id="sle_chba_netdev_stop_queue_callback"></a>

```c
// 源码原始定义
typedef errcode_t (*sle_chba_netdev_stop_queue_callback)(void);
```

**使用说明**

SLE CHBA 网络设备停止发送队列回调函数指针类型，由 [sle_chba_netdev_register_callbacks](#sle_chba_netdev_register_callbacks) 注册，在网络设备需要停止发送队列时被回调。

### sle_chba_netdev_wake_queue_callback <a id="sle_chba_netdev_wake_queue_callback"></a>

```c
// 源码原始定义
typedef errcode_t (*sle_chba_netdev_wake_queue_callback)(void);
```

**使用说明**

SLE CHBA 网络设备唤醒发送队列回调函数指针类型，由 [sle_chba_netdev_register_callbacks](#sle_chba_netdev_register_callbacks) 注册，在网络设备需要唤醒发送队列时被回调。

### sle_chba_netdev_set_link_up_callback <a id="sle_chba_netdev_set_link_up_callback"></a>

```c
// 源码原始定义
typedef errcode_t (*sle_chba_netdev_set_link_up_callback)(void);
```

**使用说明**

SLE CHBA 网络设备设置链路启用回调函数指针类型，由 [sle_chba_netdev_register_callbacks](#sle_chba_netdev_register_callbacks) 注册，在网络设备链路启用时被回调。

### sle_chba_netdev_set_link_down_callback <a id="sle_chba_netdev_set_link_down_callback"></a>

```c
// 源码原始定义
typedef errcode_t (*sle_chba_netdev_set_link_down_callback)(void);
```

**使用说明**

SLE CHBA 网络设备设置链路禁用回调函数指针类型，由 [sle_chba_netdev_register_callbacks](#sle_chba_netdev_register_callbacks) 注册，在网络设备链路禁用时被回调。

### sle_chba_netdev_input_callback <a id="sle_chba_netdev_input_callback"></a>

```c
// 源码原始定义
typedef errcode_t (*sle_chba_netdev_input_callback)(uint8_t *data, uint16_t len);
```

**使用说明**

SLE CHBA 网络设备上行数据上报回调函数指针类型，由 [sle_chba_netdev_register_callbacks](#sle_chba_netdev_register_callbacks) 注册，在网络设备接收到上行数据时被回调，参数 data 指向上行数据缓冲区、len 标识数据长度。

## Enumerations

### enum_sle_chba_role <a id="enum_sle_chba_role"></a>

```c
// 源码原始定义
enum sle_chba_role {
    CHBA_ROLE_AP, // AP模式下，设备作为无线网络中心，管理STA，提供数据中继，支持多设备连接。sle作为client端
    CHBA_ROLE_STA, // STA模式下，为叶子节点。终端设备连接到无线网络，进行数据传输。sle作为server端
};
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| CHBA_ROLE_AP | 0 | AP 模式，设备作为无线网络中心，管理 STA，提供数据中继，支持多设备连接，SLE 作为 client 端 |
| CHBA_ROLE_STA | 1 | STA 模式，设备作为叶子节点，终端设备连接到无线网络进行数据传输，SLE 作为 server 端 |

## Structures

### struct_sle_ip_link_info <a id="struct_sle_ip_link_info"></a>

```c
// 源码原始定义
typedef struct {
    uint8_t conn_id;
    sle_addr_t remote_addr;
    uint32_t tx_pkts_cnt;
    uint32_t tx_bytes;
    uint32_t rx_pkts_cnt;
    uint32_t rx_bytes;
} sle_ip_link_info;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| conn_id | uint8_t | SLE 连接 ID |
| remote_addr | sle_addr_t | 对端 SLE 设备地址 |
| tx_pkts_cnt | uint32_t | 发送数据包计数 |
| tx_bytes | uint32_t | 发送字节数 |
| rx_pkts_cnt | uint32_t | 接收数据包计数 |
| rx_bytes | uint32_t | 接收字节数 |

### struct_sle_chba_netdev_callbacks_t <a id="struct_sle_chba_netdev_callbacks_t"></a>

```c
// 源码原始定义
typedef struct {
    sle_chba_netdev_stop_queue_callback stop_queue_cb;              /*!< @if Eng Chba net device stop queue callback.
                                                                    @else   CHBA网络设备停止发送队列回调函数。 @endif */
    sle_chba_netdev_wake_queue_callback wake_queue_cb;              /*!< @if Eng Chba net device wake queue callback.
                                                                    @else   CHBA网络设备唤醒发送队列回调函数。 @endif */
    sle_chba_netdev_set_link_up_callback set_link_up_cb;            /*!< @if Eng Chba net device set link up callback.
                                                                    @else   CHBA网络设备设置链路启用回调函数。 @endif */
    sle_chba_netdev_set_link_down_callback set_link_down_cb;        /*!< @if Eng Chba net device set link down callback.
                                                                    @else   CHBA网络设备设置链路禁用回调函数。 @endif */
    sle_chba_netdev_input_callback netdev_input_cb;                 /*!< @if Eng Chba net device input callback.
                                                                    @else   CHBA网络设备数据上报回调函数。 @endif */
} sle_chba_netdev_callbacks_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| stop_queue_cb | sle_chba_netdev_stop_queue_callback | CHBA 网络设备停止发送队列回调函数 |
| wake_queue_cb | sle_chba_netdev_wake_queue_callback | CHBA 网络设备唤醒发送队列回调函数 |
| set_link_up_cb | sle_chba_netdev_set_link_up_callback | CHBA 网络设备设置链路启用回调函数 |
| set_link_down_cb | sle_chba_netdev_set_link_down_callback | CHBA 网络设备设置链路禁用回调函数 |
| netdev_input_cb | sle_chba_netdev_input_callback | CHBA 网络设备数据上报回调函数 |
