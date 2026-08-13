# Watchdog

watchdog 提供看门狗定时器功能，用于系统运行监控和异常恢复，支持复位与中断两种触发模式以及超时回调注册。

**模块公共头文件**

```c
#include "include/driver/watchdog.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_watchdog_init](#uapi_watchdog_init) | 初始化看门狗并设置超时时间 |
| [uapi_watchdog_deinit](#uapi_watchdog_deinit) | 去初始化看门狗 |
| [uapi_watchdog_enable](#uapi_watchdog_enable) | 按指定模式使能看门狗 |
| [uapi_watchdog_disable](#uapi_watchdog_disable) | 去使能看门狗 |
| [uapi_watchdog_kick](#uapi_watchdog_kick) | 喂狗，清零看门狗计数器 |
| [uapi_watchdog_set_time](#uapi_watchdog_set_time) | 设置看门狗超时时间 |
| [uapi_watchdog_get_left_time](#uapi_watchdog_get_left_time) | 获取看门狗计数器剩余时间 |
| [uapi_register_watchdog_callback](#uapi_register_watchdog_callback) | 注册看门狗超时回调 |
| [uapi_watchdog_resume](#uapi_watchdog_resume) | 恢复看门狗模块运行 |
| [uapi_watchdog_suspend](#uapi_watchdog_suspend) | 挂起看门狗模块 |

## Functions

### uapi_watchdog_init <a id="uapi_watchdog_init"></a>

```c
errcode_t uapi_watchdog_init(uint32_t timeout)
```

**声明头文件**

```c
#include "include/driver/watchdog.h"
```

**功能说明**

- 初始化看门狗模块
- 设置看门狗超时时间
- 注册看门狗硬件抽象层函数与中断

**前置条件**

- 调用时序约束：当前接口为看门狗模块的初始化入口，须在其他看门狗接口之前调用
- 依赖关系：当前接口依赖看门狗硬件抽象层函数与中断注册接口已可用
- 上下文限制：当前接口内部通过关中断保护临界区，无额外上下文限制

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| timeout | uint32_t | 看门狗超时时间，单位秒 | 0 ~ 4294967295 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 初始化成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**参考案例**

- `src/application/samples/peripheral/watchdog/watchdog_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_WATCHDOG_ALREADY_START | 特性宏 | 控制初始化时是否调用硬件抽象层设置超时属性（分支级，当看门狗已在另一份镜像中启动时不再重复设置） | n |
| CONFIG_WATCHDOG_SUPPORT_LPM | 特性宏 | 支持低功耗模式下保存超时时间（分支级） | n |

### uapi_watchdog_deinit <a id="uapi_watchdog_deinit"></a>

```c
errcode_t uapi_watchdog_deinit(void)
```

**声明头文件**

```c
#include "include/driver/watchdog.h"
```

**功能说明**

- 去初始化看门狗模块
- 当看门狗处于使能状态时先去使能
- 注销看门狗硬件抽象层函数

**前置条件**

- 调用时序约束：当前接口须在 uapi_watchdog_init() 成功返回后调用
- 依赖关系：当前接口依赖看门狗硬件抽象层去初始化与注销接口已可用
- 上下文限制：当前接口未做关中断保护，调用方需自行避免与其他看门狗接口并发

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 去初始化成功 |

**参考案例**

- `src/application/samples/peripheral/watchdog/watchdog_demo.c`

### uapi_watchdog_enable <a id="uapi_watchdog_enable"></a>

```c
errcode_t uapi_watchdog_enable(wdt_mode_t mode)
```

**声明头文件**

```c
#include "include/driver/watchdog.h"
```

**功能说明**

- 按指定模式使能看门狗
- 设置看门狗触发模式为复位或中断
- 记录看门狗使能状态

**前置条件**

- 调用时序约束：当前接口须在 uapi_watchdog_init() 成功返回后调用
- 依赖关系：当前接口依赖看门狗硬件抽象层使能接口已可用
- 上下文限制：当前接口内部通过关中断保护临界区，无额外上下文限制

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| mode | [wdt_mode_t](#enum_wdt_mode_t) | 看门狗触发模式 | [WDT_MODE_RESET](#enum_wdt_mode_t)(0) / [WDT_MODE_INTERRUPT](#enum_wdt_mode_t)(1) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 使能成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 看门狗未初始化或模式超出有效范围 |

**参考案例**

- `src/application/samples/peripheral/watchdog/watchdog_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_WATCHDOG_ALREADY_START | 特性宏 | 控制使能时是否调用硬件抽象层使能接口（接口级，当选中时看门狗已在另一份镜像中启动，使能接口不再操作硬件） | n |
| CONFIG_WATCHDOG_SUPPORT_LPM | 特性宏 | 支持低功耗模式下记录触发模式（分支级） | n |

### uapi_watchdog_disable <a id="uapi_watchdog_disable"></a>

```c
errcode_t uapi_watchdog_disable(void)
```

**声明头文件**

```c
#include "include/driver/watchdog.h"
```

**功能说明**

- 去使能看门狗
- 调用硬件抽象层去使能看门狗
- 清除看门狗使能状态

**前置条件**

- 调用时序约束：当前接口须在 uapi_watchdog_init() 成功返回后调用
- 依赖关系：当前接口依赖看门狗硬件抽象层去使能接口已可用
- 上下文限制：当前接口内部通过关中断保护临界区，无额外上下文限制

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 去使能成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 看门狗未初始化 |

### uapi_watchdog_kick <a id="uapi_watchdog_kick"></a>

```c
errcode_t uapi_watchdog_kick(void)
```

**声明头文件**

```c
#include "include/driver/watchdog.h"
```

**功能说明**

- 喂狗，清零看门狗计数器
- 调用硬件抽象层喂狗接口
- 重置看门狗超时计时

**前置条件**

- 调用时序约束：当前接口须在 uapi_watchdog_enable() 成功返回后调用
- 依赖关系：当前接口依赖看门狗硬件抽象层喂狗接口已可用
- 上下文限制：当前接口内部通过关中断保护临界区，无额外上下文限制

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 喂狗成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 看门狗未使能 |

**参考案例**

- `src/application/samples/peripheral/watchdog/watchdog_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_WATCHDOG_SUPPORT_ULP_WDT | 特性宏 | 支持低功耗看门狗喂狗（分支级，选中时同时调用 ulp_wdt_kick） | n |

### uapi_watchdog_set_time <a id="uapi_watchdog_set_time"></a>

```c
errcode_t uapi_watchdog_set_time(uint32_t timeout)
```

**声明头文件**

```c
#include "include/driver/watchdog.h"
```

**功能说明**

- 设置看门狗超时时间
- 当看门狗处于使能状态时先去使能再设置
- 调用硬件抽象层设置超时属性

**前置条件**

- 调用时序约束：当前接口须在 uapi_watchdog_init() 成功返回后调用
- 依赖关系：当前接口依赖看门狗硬件抽象层设置属性接口已可用
- 上下文限制：当前接口内部通过关中断保护临界区，无额外上下文限制

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| timeout | uint32_t | 看门狗超时时间，单位秒 | 0 ~ 4294967295 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 设置成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 看门狗未初始化或设置失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_WATCHDOG_SUPPORT_LPM | 特性宏 | 支持低功耗模式下更新超时时间（分支级） | n |

### uapi_watchdog_get_left_time <a id="uapi_watchdog_get_left_time"></a>

```c
errcode_t uapi_watchdog_get_left_time(uint32_t *timeout)
```

**声明头文件**

```c
#include "include/driver/watchdog.h"
```

**功能说明**

- 获取看门狗计数器剩余时间
- 调用硬件抽象层读取剩余时间
- 输出剩余时间值，单位秒

**前置条件**

- 调用时序约束：当前接口须在 uapi_watchdog_enable() 成功返回后调用
- 依赖关系：当前接口依赖看门狗硬件抽象层获取剩余时间接口已可用
- 上下文限制：当前接口未做关中断保护，调用方需自行避免与其他看门狗接口并发

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| timeout | uint32_t * | 剩余时间值，单位秒，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 获取成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 看门狗未使能或剩余时间为 0 |

### uapi_register_watchdog_callback <a id="uapi_register_watchdog_callback"></a>

```c
errcode_t uapi_register_watchdog_callback(watchdog_callback_t callback)
```

**声明头文件**

```c
#include "include/driver/watchdog.h"
```

**功能说明**

- 注册看门狗超时回调
- 当看门狗超时触发时调用注册的回调处理异常
- 调用硬件抽象层注册回调接口

**前置条件**

- 调用时序约束：当前接口须在 uapi_watchdog_init() 成功返回后调用
- 依赖关系：当前接口依赖看门狗硬件抽象层注册回调接口已可用
- 上下文限制：当前接口内部通过关中断保护临界区，无额外上下文限制

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| callback | [watchdog_callback_t](#typedef_watchdog_callback_t) | 看门狗超时回调函数，看门狗超时触发时被调用，回调返回值在当前实现中不被检查 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 注册成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 看门狗未初始化或回调为 NULL |

**参考案例**

- `src/application/samples/peripheral/watchdog/watchdog_demo.c`

### uapi_watchdog_resume <a id="uapi_watchdog_resume"></a>

```c
errcode_t uapi_watchdog_resume(uintptr_t arg)
```

**声明头文件**

```c
#include "include/driver/watchdog.h"
```

**功能说明**

- 恢复看门狗模块运行
- 调用硬件抽象层重新设置超时属性与使能看门狗
- 看门狗未初始化时直接返回成功

**前置条件**

- 调用时序约束：当前接口须在 uapi_watchdog_init() 成功返回后调用
- 依赖关系：当前接口依赖看门狗硬件抽象层设置属性与使能接口已可用
- 上下文限制：当前接口未做关中断保护，调用方需自行避免与其他看门狗接口并发

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| arg | uintptr_t | 恢复参数，当前实现中未使用 | 0 ~ 4294967295 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 恢复成功或看门狗未初始化 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 设置超时属性失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_WATCHDOG_SUPPORT_LPM | 特性宏 | 支持看门狗低功耗恢复接口（接口级，该宏包裹整个函数声明，控制接口对外可见性） | n |

### uapi_watchdog_suspend <a id="uapi_watchdog_suspend"></a>

```c
errcode_t uapi_watchdog_suspend(uintptr_t arg)
```

**声明头文件**

```c
#include "include/driver/watchdog.h"
```

**功能说明**

- 挂起看门狗模块
- 当前实现为预留接口，直接返回成功

**前置条件**

- 调用时序约束：当前接口须在 uapi_watchdog_init() 成功返回后调用
- 依赖关系：当前接口依赖看门狗模块已初始化
- 上下文限制：当前接口未做关中断保护，调用方需自行避免与其他看门狗接口并发

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| arg | uintptr_t | 挂起参数，当前实现中未使用 | 0 ~ 4294967295 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 挂起成功 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_WATCHDOG_SUPPORT_LPM | 特性宏 | 支持看门狗低功耗挂起接口（接口级，该宏包裹整个函数声明，控制接口对外可见性） | n |

## Type definitions

### typedef_errcode_t <a id="typedef_errcode_t"></a>

```c
// 源码原始定义
typedef uint32_t errcode_t;
```

**使用说明**

本模块所有对外接口的返回值类型。该类型为 SDK 公共基础类型，定义于 SDK 全局公共头文件 include/errcode.h，被多个模块共用。
### typedef_watchdog_callback_t <a id="typedef_watchdog_callback_t"></a>

```c
// 源码原始定义
typedef errcode_t (*watchdog_callback_t)(uintptr_t param);
```

**使用说明**

看门狗超时回调函数指针类型，作为 uapi_register_watchdog_callback 的入参类型。回调在看门狗超时触发中断时被调用；参数 param 为超时中断上下文透传的 uintptr_t 参数，头文件未定义具体语义；回调返回的 errcode_t 在当前实现中不被检查。

## Enumerations

### enum_wdt_mode_t <a id="enum_wdt_mode_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    WDT_MODE_RESET = 0,     /** @if Eng Will reset core direcotry, when Watchdog trigger.
                             *  @else   当看门狗触发时，将重启系统。
                             *  @endif */
    WDT_MODE_INTERRUPT,     /** @if Eng Will enter interrupt, when WDT trigger. If WDT not kick in interrupt, \n
                             *          core will reset.
                             *  @else   当看门狗触发时，将进入中断。如果在中断中没有喂狗，系统将重启。
                             *  @endif */
    WDT_MODE_MAX
} wdt_mode_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| WDT_MODE_RESET | 0 | 当看门狗触发时，将重启系统 |
| WDT_MODE_INTERRUPT | 1 | 当看门狗触发时，将进入中断。如果在中断中没有喂狗，系统将重启 |
| WDT_MODE_MAX | 2 | 模式上限边界值，非有效触发模式 |

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```
