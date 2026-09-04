# Time

Time 模块提供定时器管理功能，包括普通定时器与高精度定时器的生命周期管理，以及系统时间获取与毫秒/Ticks 单位转换能力。

**模块公共头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_timer_init](#osal_timer_init) | 初始化定时器 |
| [osal_timer_start](#osal_timer_start) | 启动定时器 |
| [osal_timer_mod](#osal_timer_mod) | 修改定时器超时时间 |
| [osal_timer_start_on](#osal_timer_start_on) | 在指定 CPU 上启动定时器 |
| [osal_timer_stop](#osal_timer_stop) | 停止定时器 |
| [osal_timer_destroy](#osal_timer_destroy) | 销毁定时器 |
| [osal_timer_get_private_data](#osal_timer_get_private_data) | 获取定时器回调函数的私有数据 |
| [osal_timer_destroy_sync](#osal_timer_destroy_sync) | 同步销毁定时器并等待回调完成 |
| [osal_sched_clock](#osal_sched_clock) | 获取系统时间（纳秒） |
| [osal_get_jiffies](#osal_get_jiffies) | 获取 Ticks 或 jiffies 数 |
| [osal_msecs_to_jiffies](#osal_msecs_to_jiffies) | 将毫秒转换为 Ticks/jiffies |
| [osal_jiffies_to_msecs](#osal_jiffies_to_msecs) | 将 Ticks/jiffies 转换为毫秒 |
| [osal_get_cycle_per_tick](#osal_get_cycle_per_tick) | 获取一个 tick 中的周期数 |
| [osal_gettimeofday](#osal_gettimeofday) | 获取当前系统内核时间 |
| [osal_hrtimer_create](#osal_hrtimer_create) | 创建高精度定时器 |
| [osal_hrtimer_start](#osal_hrtimer_start) | 启动高精度定时器 |
| [osal_hrtimer_destroy](#osal_hrtimer_destroy) | 删除高精度定时器 |

## Functions

### osal_timer_init <a id="osal_timer_init"></a>

```c
int osal_timer_init(osal_timer *timer)
```

**声明头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

**功能说明**

- 初始化定时器并设置到期回调。
- 定时器到期时通过注册的回调函数通知调用方。
- 支持 linux、liteos、freertos 系统。

**前置条件**

- 依赖关系：调用前需设置 timer 的 handler 和 data 字段，初始化完成后无法再修改这两个字段。
- 依赖关系：不再使用定时器时应调用 osal_timer_destroy 释放，否则会导致内存泄漏。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| timer | [osal_timer](#struct_osal_timer) * | 输入输出参数。要初始化的定时器，调用前需设置 handler 和 data 字段，函数填充内部定时器资源 | 不为NULL；timer->handler 不为NULL；timer->timer 为 NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)：0 | 执行成功 | 定时器初始化成功 |
| [OSAL_FAILURE](#OSAL_FAILURE)：-1 | 执行失败 | 参数无效、interval 无效或内存分配失败 |

**参考案例**

- `src/application/samples/peripheral/adc/adc_demo.c`
- `src/middleware/utils/dfx/log_file/log_file.c`

### osal_timer_start <a id="osal_timer_start"></a>

```c
int osal_timer_start(osal_timer *timer)
```

**声明头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

**功能说明**

- 启动已初始化的定时器，按设定超时时间调度。
- 定时器到期时内核将通过定时器中断回调 handler。
- 支持 linux、liteos、freertos 系统。

**前置条件**

- 调用时序约束：必须在 osal_timer_init 成功返回后调用。
- 上下文限制：定时器到期时回调将在定时器中断上下文中执行。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| timer | [osal_timer](#struct_osal_timer) * | 要启动的定时器 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)：0 | 执行成功 | 定时器启动成功 |
| [OSAL_FAILURE](#OSAL_FAILURE)：-1 | 执行失败 | 参数无效 |

**参考案例**

- `src/application/samples/peripheral/adc/adc_demo.c`
- `src/middleware/utils/dfx/log_file/log_file.c`

### osal_timer_mod <a id="osal_timer_mod"></a>

```c
int osal_timer_mod(osal_timer *timer, unsigned int interval)
```

**声明头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

**功能说明**

- 修改定时器的超时时间。
- 对活跃定时器更新过期时间，对非活跃定时器将其激活。
- 支持 linux、liteos、freertos 系统。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| timer | [osal_timer](#struct_osal_timer) * | 要修改的定时器 | 不为NULL |
| interval | unsigned int | 新的超时时间，单位 ms | > 0 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)：0 | 执行成功 | 定时器超时时间修改成功 |
| [OSAL_FAILURE](#OSAL_FAILURE)：-1 | 执行失败 | 参数无效或 interval 无效 |

**参考案例**

- `src/application/samples/peripheral/lpc/lpc_gpio_wakeup_demo.c`

### osal_timer_start_on <a id="osal_timer_start_on"></a>

```c
int osal_timer_start_on(osal_timer *timer, unsigned long delay, int cpu)
```

**声明头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

**功能说明**

- 在指定 CPU 上启动定时器。
- 支持 linux 系统。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| timer | [osal_timer](#struct_osal_timer) * | 要启动的定时器 | 不为NULL |
| delay | unsigned long | 延迟时间，单位 ms | - |
| cpu | int | 启动定时器的 CPU 编号 | 有效 CPU 编号 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)：0 | 执行成功 | 定时器在指定 CPU 上启动成功 |
| [OSAL_FAILURE](#OSAL_FAILURE)：-1 | 执行失败 | 参数无效 |

### osal_timer_stop <a id="osal_timer_stop"></a>

```c
int osal_timer_stop(osal_timer *timer)
```

**声明头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

**功能说明**

- 停止定时器，对活跃和非活跃定时器均生效。
- 支持 linux、liteos、freertos 系统。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| timer | [osal_timer](#struct_osal_timer) * | 要停止的定时器 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 1 | 停止成功，定时器处于 pending 状态 | 仅 Linux 和 LiteOS 支持返回 1 |
| [OSAL_SUCCESS](#OSAL_SUCCESS)：0 | 停止成功，定时器已停止 | 定时器未处于活跃状态 |
| [OSAL_FAILURE](#OSAL_FAILURE)：-1 | 执行失败 | 参数无效 |

**参考案例**

- `src/middleware/utils/dfx/log_file/log_file.c`
- `src/protocol/wifi/source/host/frw/frw_timer.c`

### osal_timer_destroy <a id="osal_timer_destroy"></a>

```c
int osal_timer_destroy(osal_timer *timer)
```

**声明头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

**功能说明**

- 销毁定时器，停止定时器并释放内部资源。
- 支持 linux、liteos、freertos 系统。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| timer | [osal_timer](#struct_osal_timer) * | 要销毁的定时器 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)：0 | 执行成功 | 定时器销毁成功 |
| [OSAL_FAILURE](#OSAL_FAILURE)：-1 | 执行失败 | 参数无效 |

**参考案例**

- `src/middleware/utils/dfx/log_file/log_file.c`

### osal_timer_get_private_data <a id="osal_timer_get_private_data"></a>

```c
unsigned long osal_timer_get_private_data(const void *sys_data)
```

**声明头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

**功能说明**

- 在定时器回调函数中获取可直接使用的参数数据。
- 定时器回调函数的参数不能直接使用，需通过此接口转换获取。
- 支持 linux、liteos、freertos 系统。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| sys_data | const void * | 传给回调函数的参数 | 不为NULL |

**返回值**

- 返回类型：unsigned long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 获取失败 | sys_data 为 NULL |
| 非 0 值 | 可直接使用的参数数据 | 正常获取定时器私有数据 |

### osal_timer_destroy_sync <a id="osal_timer_destroy_sync"></a>

```c
int osal_timer_destroy_sync(osal_timer *timer)
```

**声明头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

**功能说明**

- 停止定时器并等待回调函数执行完成。
- 在 SMP（Symmetric Multi-Processing）环境下确保其他 CPU 上的回调已执行完毕。
- 支持 linux 系统。

**前置条件**

- 调用时序约束：必须在 osal_timer_init 成功返回后调用。
- 上下文限制：禁止在中断上下文调用（除非定时器为 irqsafe 类型）。
- 依赖关系：调用者不能持有会阻止定时器回调函数完成的锁；调用者必须阻止定时器被重新启动。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| timer | [osal_timer](#struct_osal_timer) * | 要同步销毁的定时器 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)：0 | 执行成功 | 定时器已同步销毁 |
| [OSAL_FAILURE](#OSAL_FAILURE)：-1 | 执行失败 | 参数无效 |

### osal_sched_clock <a id="osal_sched_clock"></a>

```c
unsigned long long osal_sched_clock(void)
```

**声明头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

**功能说明**

- 获取当前系统时间，单位为纳秒。
- 支持 linux 和 liteos 系统。

**返回值**

- 返回类型：unsigned long long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| unsigned long long | 当前系统时间，单位纳秒 | 调用成功返回当前时间 |

### osal_get_jiffies <a id="osal_get_jiffies"></a>

```c
unsigned long long osal_get_jiffies(void)
```

**声明头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

**功能说明**

- 获取系统的 Ticks（liteos）或 jiffies（linux）数量。
- 支持 linux、liteos、freertos 系统。

**返回值**

- 返回类型：unsigned long long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| unsigned long long | Ticks（liteos）或 jiffies（linux）数量 | 调用成功返回当前节拍数 |

**参考案例**

- `src/middleware/services/wifi_service/wpa/osdep/osdep_osal.c`

### osal_msecs_to_jiffies <a id="osal_msecs_to_jiffies"></a>

```c
unsigned long osal_msecs_to_jiffies(const unsigned int m)
```

**声明头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

**功能说明**

- 将毫秒转换为 Ticks/jiffies。
- 支持 linux、liteos、freertos 系统。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| m | const unsigned int | 要转换的时间，单位 ms | - |

**返回值**

- 返回类型：unsigned long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| unsigned long | 转换后的 Ticks/jiffies 数 | 调用成功返回转换结果 |

### osal_jiffies_to_msecs <a id="osal_jiffies_to_msecs"></a>

```c
unsigned int osal_jiffies_to_msecs(const unsigned int n)
```

**声明头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

**功能说明**

- 将 Ticks/jiffies 转换为毫秒。
- 若转换结果超过 0xFFFFFFFF，则返回 0xFFFFFFFF。
- 支持 linux、liteos、freertos 系统。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| n | const unsigned int | 要转换的 Ticks/jiffies 数 | - |

**返回值**

- 返回类型：unsigned int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| unsigned int | 转换后的毫秒数，超过 0xFFFFFFFF 时返回 0xFFFFFFFF | 调用成功返回转换结果 |

### osal_get_cycle_per_tick <a id="osal_get_cycle_per_tick"></a>

```c
unsigned int osal_get_cycle_per_tick(void)
```

**声明头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

**功能说明**

- 获取一个 tick 中包含的周期数。
- 支持 liteos 系统。

**返回值**

- 返回类型：unsigned int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| unsigned int | 一个 tick 中的周期数 | 调用成功返回周期数 |

### osal_gettimeofday <a id="osal_gettimeofday"></a>

```c
void osal_gettimeofday(osal_timeval *tv)
```

**声明头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

**功能说明**

- 获取当前系统内核时间。
- 时间通过 osal_timeval 结构体返回，包含秒和微秒。
- 支持 linux、liteos、freertos 系统。

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| tv | [osal_timeval](#struct_osal_timeval) * | 获取的当前系统内核时间，由调用方分配内存、函数填充 |

**参考案例**

- `src/middleware/services/wifi_service/service/soc_wifi_service_api.c`
- `src/protocol/wifi/source/host/hmac/hmac_dfx.c`

### osal_hrtimer_create <a id="osal_hrtimer_create"></a>

```c
int osal_hrtimer_create(osal_hrtimer *hrtimer)
```

**声明头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

**功能说明**

- 创建高精度定时器节点并初始化定时器参数。
- 支持 liteos 系统。

**前置条件**

- 依赖关系：调用前需设置 hrtimer 的 handler 和 interval 字段，初始化完成后无法再修改这两个字段。
- 上下文限制：模块退出时必须调用 osal_hrtimer_destroy 释放定时器，否则会导致内存泄漏。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| hrtimer | [osal_hrtimer](#struct_osal_hrtimer) * | 输入输出参数。要创建的高精度定时器，调用前需设置 handler 和 interval 字段，函数填充内部定时器资源 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)：0 | 执行成功 | 高精度定时器创建成功 |
| [OSAL_FAILURE](#OSAL_FAILURE)：-1 | 执行失败 | 高精度定时器创建失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| LOSCFG_COMPAT_LINUX_HRTIMER | 特性宏 | 支持 high resolution timer 接口（接口级，liteos 实现体由 #ifdef 包裹，LiteOS Kconfig 声明） | n |

### osal_hrtimer_start <a id="osal_hrtimer_start"></a>

```c
int osal_hrtimer_start(osal_hrtimer *hrtimer)
```

**声明头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

**功能说明**

- 启动高精度定时器，将定时器节点添加到全局链表并开始计时。
- 支持 liteos 系统。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| hrtimer | [osal_hrtimer](#struct_osal_hrtimer) * | 要启动的高精度定时器 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| -1 | 启动失败 | 高精度定时器启动失败 |
| 0 | 启动成功 | 高精度定时器启动成功 |
| 1 | 节点已存在 | 高精度定时器节点已在链表中 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| LOSCFG_COMPAT_LINUX_HRTIMER | 特性宏 | 支持 high resolution timer 接口（接口级，liteos 实现体由 #ifdef 包裹，LiteOS Kconfig 声明） | n |

### osal_hrtimer_destroy <a id="osal_hrtimer_destroy"></a>

```c
int osal_hrtimer_destroy(osal_hrtimer *hrtimer)
```

**声明头文件**

```c
#include "src/kernel/osal/include/time/osal_timer.h"
```

**功能说明**

- 删除已存在的高精度定时器。
- 支持 liteos 系统。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| hrtimer | [osal_hrtimer](#struct_osal_hrtimer) * | 要删除的高精度定时器 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)：0 | 执行成功 | 高精度定时器删除成功 |
| [OSAL_FAILURE](#OSAL_FAILURE)：-1 | 执行失败 | 参数为空或定时器节点不存在 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| LOSCFG_COMPAT_LINUX_HRTIMER | 特性宏 | 支持 high resolution timer 接口（接口级，liteos 实现体由 #ifdef 包裹，LiteOS Kconfig 声明） | n |

## Enumerations

### osal_hrtimer_restart <a id="enum_osal_hrtimer_restart"></a>

```c
typedef enum {
    OSAL_HRTIMER_NORESTART, /* < The timer will not be restarted. */
    OSAL_HRTIMER_RESTART    /* < The timer must be restarted. */
} osal_hrtimer_restart;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| OSAL_HRTIMER_NORESTART | 0 | 定时器不再重启 |
| OSAL_HRTIMER_RESTART | 1 | 定时器需要重启 |

## Structures

### osal_timer <a id="struct_osal_timer"></a>

```c
typedef struct {
    void *timer;
    void (*handler)(unsigned long);
    unsigned long data;    // data for handler
    unsigned int interval; // timer timing duration, unit: ms.
} osal_timer;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| timer | void * | 定时器内部资源指针 |
| handler | void (\*)(unsigned long) | 定时器超时回调函数指针 |
| data | unsigned long | 回调函数的参数数据 |
| interval | unsigned int | 定时器定时时长，单位 ms |

### osal_timeval <a id="struct_osal_timeval"></a>

```c
typedef struct {
    long tv_sec;
    long tv_usec;
} osal_timeval;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| tv_sec | long | 秒 |
| tv_usec | long | 微秒 |

### osal_hrtimer <a id="struct_osal_hrtimer"></a>

```c
typedef struct osal_hrtimer {
    void *timer;
    osal_hrtimer_restart (*handler)(void *timer);
    unsigned long interval; /* Unit ms */
} osal_hrtimer;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| timer | void * | 高精度定时器内部资源指针 |
| handler | [osal_hrtimer_restart](#enum_osal_hrtimer_restart) (\*)(void \*) |
| interval | unsigned long | 定时器定时间隔，单位 ms |

## Macros

### OSAL_SUCCESS <a id="OSAL_SUCCESS"></a>

```c
#define OSAL_SUCCESS 0
```

### OSAL_FAILURE <a id="OSAL_FAILURE"></a>

```c
#define OSAL_FAILURE (-1)
```
