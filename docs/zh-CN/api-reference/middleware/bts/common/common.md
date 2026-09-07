# BTS Common

BTS Common 提供蓝牙基础设备管理能力，包括 BLE（Bluetooth Low Energy）协议栈的使能与去使能，以及设备上电、BLE 使能/去使能结果的回调通知注册。该模块基于 errcode_t 统一错误码返回执行结果，并通过回调机制异步上报协议栈运行状态。

**模块公共头文件**

```c
#include "include/middleware/services/bts/common/bts_device_manager.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [enable_ble](#enable_ble) | 使能 BLE 协议栈 |
| [disable_ble](#disable_ble) | 去使能 BLE 协议栈 |
| [bts_dev_manager_register_callbacks](#bts_dev_manager_register_callbacks) | 注册设备管理回调函数 |

## Functions

### enable_ble <a id="enable_ble"></a>

```c
errcode_t enable_ble(void)
```

**声明头文件**

```c
#include "include/middleware/services/bts/common/bts_device_manager.h"
```

**功能说明**

- 发起使能 BLE 协议栈的请求。
- 异步触发协议栈启动流程，启动结果通过已注册的 `bts_ble_enable_callback` 回调上报。
- 返回值仅表示请求发起是否成功，实际使能结果需在回调中获取。

**前置条件**

- 调用时序约束：需先调用 `bts_dev_manager_register_callbacks` 注册 `bts_ble_enable_callback` 回调，否则无法接收使能结果。
- 依赖关系：当前接口依赖 BTS（Bluetooth Stack）设备管理模块已初始化、底层蓝牙硬件资源已就绪。

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 请求发起成功 | 使能 BLE 请求提交成功 |
| Other | 其他错误码，参考 errcode_t | 请求发起失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`
- `src/application/samples/bt/ble/ble_wifi_cfg_server/src/ble_wifi_cfg_server.c`

### disable_ble <a id="disable_ble"></a>

```c
errcode_t disable_ble(void)
```

**声明头文件**

```c
#include "include/middleware/services/bts/common/bts_device_manager.h"
```

**功能说明**

- 发起去使能 BLE 协议栈的请求。
- 异步触发协议栈关闭流程，关闭结果通过已注册的 `bts_ble_disable_callback` 回调上报。
- 返回值仅表示请求发起是否成功，实际去使能结果需在回调中获取。

**前置条件**

- 调用时序约束：需先调用 `bts_dev_manager_register_callbacks` 注册 `bts_ble_disable_callback` 回调，否则无法接收去使能结果。
- 依赖关系：当前接口依赖 BTS 设备管理模块已初始化、BLE 协议栈已通过 `enable_ble` 成功使能。

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 去使能 BLE 请求提交成功 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

### bts_dev_manager_register_callbacks <a id="bts_dev_manager_register_callbacks"></a>

```c
errcode_t bts_dev_manager_register_callbacks(bts_dev_manager_callbacks_t *func)
```

**声明头文件**

```c
#include "include/middleware/services/bts/common/bts_device_manager.h"
```

**功能说明**

- 注册设备管理回调函数集合，用于接收 BTS 设备上电、BLE 使能、BLE 去使能等异步事件通知。
- 注册后由 BTS 在相应事件发生时调用对应回调，向应用层透传状态结果。
- 通过单一回调结构体一次性完成上电、使能、去使能三类事件的回调注册。

**前置条件**

- 调用时序约束：应在调用 `enable_ble`、`disable_ble` 之前完成注册，以确保能接收到对应结果回调。
- 依赖关系：当前接口依赖 BTS 设备管理模块已初始化。
- 上下文限制：注册的回调函数运行于 BTS 线程，回调内不能阻塞或长时间等待。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func | [bts_dev_manager_callbacks_t](#bts_dev_manager_callbacks_t) * | 指向回调函数结构体的指针，结构体内含设备上电回调、BLE 使能回调、BLE 去使能回调 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 回调注册成功 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_wifi_cfg_server/src/ble_wifi_cfg_server.c`

## Type definitions

### bts_power_on_callback <a id="bts_power_on_callback"></a>

```c
typedef void (*bts_power_on_callback)(uint8_t status);
```

**使用说明**

设备上电结果上报回调函数类型，由 BTS 在设备上电完成后调用。回调说明：调用时机为设备上电完成时，由 BTS 线程触发；参数 `status` 取值为 `bts_power_on_status_t` 枚举（BT_POWER_ON_SUCCESS(0) / BT_POWER_ON_FAIL(1)），表示上电结果；无返回值，回调返回值不被检查。

### bts_ble_enable_callback <a id="bts_ble_enable_callback"></a>

```c
typedef void (*bts_ble_enable_callback)(uint8_t status);
```

**使用说明**

BLE 协议栈启动结果上报回调函数类型，由 BTS 在 BLE 协议栈启动后调用。回调说明：调用时机为 BLE 协议栈启动完成后，由 BTS 线程触发；参数 `status` 取值为 `bts_enable_disable_status_t` 枚举（BT_ENABLE_DISABLE_SUCCESS(0) / BT_ENABLE_DISABLE_FAIL(1)），表示使能结果；无返回值，回调返回值不被检查。

### bts_ble_disable_callback <a id="bts_ble_disable_callback"></a>

```c
typedef void (*bts_ble_disable_callback)(uint8_t status);
```

**使用说明**

BLE 协议栈关闭结果上报回调函数类型，由 BTS 在 BLE 协议栈关闭后调用。回调说明：调用时机为 BLE 协议栈关闭完成后，由 BTS 线程触发；参数 `status` 取值为 `bts_enable_disable_status_t` 枚举（BT_ENABLE_DISABLE_SUCCESS(0) / BT_ENABLE_DISABLE_FAIL(1)），表示去使能结果；无返回值，回调返回值不被检查。

## Enumerations

### bts_power_on_status_t <a id="bts_power_on_status_t"></a>

```c
typedef enum {
    BT_POWER_ON_SUCCESS,
    BT_POWER_ON_FAIL,
} bts_power_on_status_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| BT_POWER_ON_SUCCESS | 0 | BT 上电成功 |
| BT_POWER_ON_FAIL | 1 | BT 上电失败 |

### bts_enable_disable_status_t <a id="bts_enable_disable_status_t"></a>

```c
typedef enum {
    BT_ENABLE_DISABLE_SUCCESS,
    BT_ENABLE_DISABLE_FAIL,
} bts_enable_disable_status_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| BT_ENABLE_DISABLE_SUCCESS | 0 | BT 使能/去使能成功 |
| BT_ENABLE_DISABLE_FAIL | 1 | BT 使能/去使能失败 |

## Structures

### bts_dev_manager_callbacks_t <a id="bts_dev_manager_callbacks_t"></a>

```c
typedef struct {
    bts_power_on_callback power_on_cb;
    bts_ble_enable_callback ble_enable_cb;
    bts_ble_disable_callback ble_disable_cb;
} bts_dev_manager_callbacks_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| power_on_cb | bts_power_on_callback | 设备上电回调函数 |
| ble_enable_cb | bts_ble_enable_callback | BLE 启动回调函数 |
| ble_disable_cb | bts_ble_disable_callback | BLE 关闭回调函数 |

