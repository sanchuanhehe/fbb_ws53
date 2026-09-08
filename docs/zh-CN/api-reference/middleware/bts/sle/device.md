# Device

Device 模块提供 SLE（Star Flash Low Energy）协议栈的使能、去使能以及设备管理回调注册功能，用于在 SLE 设备上电后驱动协议栈进入工作状态并通过回调向应用层上报上电与协议栈使能/去使能结果。

**模块公共头文件**

```c
#include "include/middleware/services/bts/sle/sle_device_manager.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [enable_sle](#enable_sle) | 使能 SLE 协议栈 |
| [disable_sle](#disable_sle) | 关闭 SLE 协议栈 |
| [sle_dev_manager_register_callbacks](#sle_dev_manager_register_callbacks) | 注册 SLE 设备管理回调函数 |

## Functions

### enable_sle <a id="enable_sle"></a>

```c
errcode_t enable_sle(void)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_device_manager.h"
```

**功能说明**

- 发起 SLE 协议栈使能流程，驱动协议栈进入工作状态。
- 使能结果通过已注册的 [sle_enable_callback](#sle_enable_callback) 回调异步上报，状态取值见回调定义。
- 使能成功后 SLE 协议栈相关业务接口方可调用。

**前置条件**

- 调用时序约束：当前接口必须在 SLE 设备上电完成（已收到 [sle_power_on_callback](#sle_power_on_callback) 上电成功回调）后调用。
- 依赖关系：当前接口依赖 SLE service 已就绪且底层协议栈资源已初始化。
- 上下文限制：当前接口需在应用任务上下文调用，禁止在中断上下文调用。

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 使能请求成功发起 |
| Other | 失败，参考 [errcode_t](#typedef_errcode_t) | 使能请求发起失败 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`
- `src/application/samples/bt/sle/sle_speed_client/src/sle_speed_client.c`
- `src/application/samples/bt/sle_chba/src/sle_chba_server.c`

### disable_sle <a id="disable_sle"></a>

```c
errcode_t disable_sle(void)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_device_manager.h"
```

**功能说明**

- 发起 SLE 协议栈去使能流程，关闭协议栈工作状态。
- 去使能结果通过已注册的 [sle_disable_callback](#sle_disable_callback) 回调异步上报，状态取值见回调定义。
- 去使能后 SLE 协议栈相关业务接口不再可用。

**前置条件**

- 调用时序约束：当前接口必须在 SLE 协议栈已成功使能后调用。
- 依赖关系：当前接口依赖 SLE service 已就绪。
- 上下文限制：当前接口需在应用任务上下文调用，禁止在中断上下文调用。

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 去使能请求成功发起 |
| Other | 失败，参考 [errcode_t](#typedef_errcode_t) | 去使能请求发起失败 |

### sle_dev_manager_register_callbacks <a id="sle_dev_manager_register_callbacks"></a>

```c
errcode_t sle_dev_manager_register_callbacks(sle_dev_manager_callbacks_t *func)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_device_manager.h"
```

**功能说明**

- 向 SLE 设备管理模块注册上电、使能、去使能事件回调函数集合。
- 成功注册后，SLE 设备上电结果及协议栈使能/去使能结果将通过对应回调异步上报。
- 回调函数集合由 [sle_dev_manager_callbacks_t](#sle_dev_manager_callbacks_t) 组织，包含上电、使能、去使能三个回调。

**前置条件**

- 调用时序约束：当前接口必须在调用 [enable_sle](#enable_sle) 之前完成注册。
- 依赖关系：当前接口依赖 SLE service 已就绪。
- 上下文限制：当前接口需在应用任务上下文调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func | [sle_dev_manager_callbacks_t](#sle_dev_manager_callbacks_t) * | 回调函数集合指针，回调在 SLE service 线程被调用，不能阻塞或长时间等待；指针所指内存的生命周期需覆盖整个使用周期 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| Other | 执行结果错误码 | 注册回调函数的执行结果 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_client/src/sle_speed_client.c`
- `src/application/samples/bt/sle/sle_speed_server/src/sle_speed_server_adv.c`

## Type definitions

### sle_power_on_callback <a id="sle_power_on_callback"></a>

```c
typedef void (*sle_power_on_callback)(uint8_t status);
```

**使用说明**

SLE 设备上电完成事件触发的回调函数指针类型，回调在 SLE service 线程被调用。

回调说明：
- 调用时机：SLE 设备上电流程完成时由 SLE service 调用。
- 参数语义：`status` 为上电执行结果错误码，由 SLE service 透传。
- 返回值处理：返回类型为 void，无返回值；回调中不应阻塞或长时间等待。

### sle_enable_callback <a id="sle_enable_callback"></a>

```c
typedef void (*sle_enable_callback)(uint8_t status);
```

**使用说明**

SLE 协议栈使能完成事件触发的回调函数指针类型，回调在 SLE service 线程被调用。

回调说明：
- 调用时机：SLE 协议栈使能流程完成时由 SLE service 调用。
- 参数语义：`status` 为使能状态，取值参考 `sle_enable_disable_status_t`
- 返回值处理：返回类型为 void，无返回值；回调中不应阻塞或长时间等待。

### sle_disable_callback <a id="sle_disable_callback"></a>

```c
typedef void (*sle_disable_callback)(uint8_t status);
```

**使用说明**

SLE 协议栈去使能完成事件触发的回调函数指针类型，回调在 SLE service 线程被调用。

回调说明：
- 调用时机：SLE 协议栈去使能流程完成时由 SLE service 调用。
- 参数语义：`status` 为去使能状态，取值参考 `sle_enable_disable_status_t`
- 返回值处理：返回类型为 void，无返回值；回调中不应阻塞或长时间等待。

## Type definitions

### typedef_errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块返回类型为 errcode_t 的对外接口的返回值类型。

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```

## Structures

### sle_dev_manager_callbacks_t <a id="sle_dev_manager_callbacks_t"></a>

```c
typedef struct {
    sle_power_on_callback sle_power_on_cb;                  /*!< SLE设备上电回调函数。 */
    sle_enable_callback sle_enable_cb;                      /*!< SLE协议栈使能回调函数。 */
    sle_disable_callback sle_disable_cb;                    /*!< SLE协议栈去使能回调函数。 */
} sle_dev_manager_callbacks_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| sle_power_on_cb | sle_power_on_callback | SLE 设备上电回调函数，上电完成时触发 |
| sle_enable_cb | sle_enable_callback | SLE 协议栈使能回调函数，使能完成时触发 |
| sle_disable_cb | sle_disable_callback | SLE 协议栈去使能回调函数，去使能完成时触发 |
