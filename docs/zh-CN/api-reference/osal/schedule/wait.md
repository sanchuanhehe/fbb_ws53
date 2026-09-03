# Wait

wait 提供 OSAL（Operating System Abstraction Layer）的等待队列机制，支持线程在指定条件满足前阻塞睡眠、超时自动唤醒以及主动唤醒等待队列上的线程，用于线程间同步与事件等待。

**模块公共头文件**

```c
#include "kernel/osal/include/schedule/osal_wait.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_wait_init](#osal_wait_init) | 初始化一个等待队列 |
| [osal_wait_interruptible](#osal_wait_interruptible) | 阻塞睡眠直到条件为真或被信号打断 |
| [osal_wait_uninterruptible](#osal_wait_uninterruptible) | 阻塞睡眠（不可中断）直到条件为真 |
| [osal_wait_timeout_interruptible](#osal_wait_timeout_interruptible) | 阻塞睡眠直到条件为真、超时或被信号打断 |
| [osal_wait_timeout_uninterruptible](#osal_wait_timeout_uninterruptible) | 阻塞睡眠（不可中断）直到条件为真或超时 |
| [osal_wait_wakeup](#osal_wait_wakeup) | 唤醒阻塞在等待队列上的线程 |
| [osal_wait_wakeup_interruptible](#osal_wait_wakeup_interruptible) | 唤醒阻塞在等待队列上的可中断等待线程 |
| [osal_wait_destroy](#osal_wait_destroy) | 销毁等待队列并释放其占用的资源 |

## Functions

### osal_wait_init <a id="osal_wait_init"></a>

```c
int osal_wait_init(osal_wait *wait)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_wait.h"
```

**功能说明**

- 初始化一个等待队列，使其进入可用状态。
- 初始化成功后该等待队列可用于阻塞等待、唤醒与销毁操作。
- 支持 linux、LiteOS、FreeRTOS 系统。

**前置条件**

- 调用时序约束：wait 指向的 osal_wait 结构体须由调用方预先分配，且 wait->wait 必须为 NULL（未重复初始化）。
- 上下文限制：初始化成功后方可调用等待、唤醒与销毁接口。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| wait | [osal_wait](#osal_wait) * | 待初始化的等待队列句柄 | 不为NULL 且 wait->wait 为 NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 执行成功 (OSAL_SUCCESS) | 等待队列初始化成功 |
| -1 | 执行失败 (OSAL_FAILURE) | wait 为 NULL、wait->wait 非空（已初始化）或底层资源分配失败 |

**参考案例**

- `src/middleware/utils/hcc/comm/hcc.c`

### osal_wait_interruptible <a id="osal_wait_interruptible"></a>

```c
int osal_wait_interruptible(osal_wait *wait, osal_wait_condition_func func, const void *param)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_wait.h"
```

**功能说明**

- 阻塞当前线程睡眠，直到条件函数返回真或收到信号。
- 每次等待队列被唤醒时检查条件函数的返回值。
- 在 LiteOS 上等价于 osal_wait_uninterruptible（不支持可中断等待）。
- 支持 linux、LiteOS 系统。

**前置条件**

- 调用时序约束：当前接口必须在 osal_wait_init 成功返回后调用。
- 上下文限制：当前接口会阻塞当前线程，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| wait | [osal_wait](#osal_wait) * | 等待的等待队列句柄 | 不为NULL 且 wait->wait 已初始化 |
| func | [osal_wait_condition_func](#osal_wait_condition_func) | 条件判断回调函数，每次唤醒时调用；为 NULL 时按永真条件等待 | 为 NULL 或指向有效的条件判断函数 |
| param | const void * | 传递给条件判断回调函数的参数 | - |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 执行成功 (OSAL_SUCCESS) | 条件满足或被唤醒 |
| -1 | 执行失败 (OSAL_FAILURE) | wait 为 NULL 或 wait->wait 为 NULL |
| -512 | 被信号中断 (-OSAL_ERESTARTSYS) | Linux 下被信号打断；LiteOS 不产生该返回值 |

**参考案例**

- `src/middleware/utils/hcc/comm/hcc.c`

### osal_wait_uninterruptible <a id="osal_wait_uninterruptible"></a>

```c
int osal_wait_uninterruptible(osal_wait *wait, osal_wait_condition_func func, const void *param)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_wait.h"
```

**功能说明**

- 阻塞当前线程睡眠（不可中断），直到条件函数返回真。
- 每次等待队列被唤醒时检查条件函数的返回值。
- 支持 linux、LiteOS、FreeRTOS 系统。

**前置条件**

- 调用时序约束：当前接口必须在 osal_wait_init 成功返回后调用。
- 上下文限制：当前接口会阻塞当前线程，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| wait | [osal_wait](#osal_wait) * | 等待的等待队列句柄 | 不为NULL 且 wait->wait 已初始化 |
| func | [osal_wait_condition_func](#osal_wait_condition_func) | 条件判断回调函数，每次唤醒时调用；为 NULL 时按永真条件等待 | 为 NULL 或指向有效的条件判断函数 |
| param | const void * | 传递给条件判断回调函数的参数 | - |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 执行成功 (OSAL_SUCCESS) | 条件满足或被唤醒 |
| -1 | 执行失败 (OSAL_FAILURE) | wait 为 NULL 或 wait->wait 为 NULL |

### osal_wait_timeout_interruptible <a id="osal_wait_timeout_interruptible"></a>

```c
int osal_wait_timeout_interruptible(osal_wait *wait, osal_wait_condition_func func, const void *param, unsigned long ms)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_wait.h"
```

**功能说明**

- 阻塞当前线程睡眠，直到条件函数返回真、超时或收到信号。
- 超时时间以毫秒为单位。
- 支持 linux、LiteOS、FreeRTOS 系统。

**前置条件**

- 调用时序约束：当前接口必须在 osal_wait_init 成功返回后调用。
- 上下文限制：当前接口会阻塞当前线程，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| wait | [osal_wait](#osal_wait) * | 等待的等待队列句柄 | 不为NULL 且 wait->wait 已初始化 |
| func | [osal_wait_condition_func](#osal_wait_condition_func) | 条件判断回调函数，每次唤醒时调用；为 NULL 时按永真条件等待并默认返回超时 | 为 NULL 或指向有效的条件判断函数 |
| param | const void * | 传递给条件判断回调函数的参数 | - |
| ms | unsigned long | 超时时间，单位毫秒 | 0 ~ 0xFFFFFFFF；[OSAL_WAIT_FOREVER](#OSAL_WAIT_FOREVER)(0xFFFFFFFF) 表示永久等待 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 超时且条件未满足 | 超时结束后条件仍为假 |
| 大于 0 | 条件已满足，返回剩余时间 | 条件在超时前满足，返回剩余 tick 数（Linux 为 jiffies）；LiteOS 下条件在超时点为真时返回 1 |
| -1 | 参数无效 (OSAL_FAILURE) | wait 为 NULL 或 wait->wait 为 NULL |
| -512 | 被信号中断 (-OSAL_ERESTARTSYS) | Linux 下被信号打断 |

**参考案例**

- `src/middleware/utils/hcc/comm/hcc_flow_ctrl.c`

### osal_wait_timeout_uninterruptible <a id="osal_wait_timeout_uninterruptible"></a>

```c
int osal_wait_timeout_uninterruptible(osal_wait *wait, osal_wait_condition_func func, const void *param, unsigned long ms)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_wait.h"
```

**功能说明**

- 阻塞当前线程睡眠（不可中断），直到条件函数返回真或超时。
- 超时时间以毫秒为单位。
- 支持 linux、LiteOS 系统。

**前置条件**

- 调用时序约束：当前接口必须在 osal_wait_init 成功返回后调用。
- 上下文限制：当前接口会阻塞当前线程，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| wait | [osal_wait](#osal_wait) * | 等待的等待队列句柄 | 不为NULL 且 wait->wait 已初始化 |
| func | [osal_wait_condition_func](#osal_wait_condition_func) | 条件判断回调函数，每次唤醒时调用；为 NULL 时按永真条件等待 | 为 NULL 或指向有效的条件判断函数 |
| param | const void * | 传递给条件判断回调函数的参数 | - |
| ms | unsigned long | 超时时间，单位毫秒 | 0 ~ 0xFFFFFFFF；[OSAL_WAIT_FOREVER](#OSAL_WAIT_FOREVER)(0xFFFFFFFF) 表示永久等待 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 超时且条件未满足 | 超时结束后条件仍为假 |
| 大于 0 | 条件已满足，返回剩余时间 | 条件在超时前满足，返回剩余 tick 数（Linux 为 jiffies） |
| -1 | 参数无效 (OSAL_FAILURE) | wait 为 NULL 或 wait->wait 为 NULL |

### osal_wait_wakeup <a id="osal_wait_wakeup"></a>

```c
void osal_wait_wakeup(osal_wait *wait)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_wait.h"
```

**功能说明**

- 唤醒阻塞在指定等待队列上的所有线程。
- 与等待接口（如 osal_wait_uninterruptible）配对使用。
- 支持 linux、LiteOS、FreeRTOS 系统。

**前置条件**

- 调用时序约束：当前接口必须在 osal_wait_init 成功返回后调用。
- 依赖关系：改变等待条件后须调用本接口唤醒等待队列上的线程。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| wait | [osal_wait](#osal_wait) * | 待唤醒的等待队列句柄 | 不为NULL 且 wait->wait 已初始化 |

**参考案例**

- `src/middleware/utils/hcc/comm/hcc.c`

### osal_wait_wakeup_interruptible <a id="osal_wait_wakeup_interruptible"></a>

```c
void osal_wait_wakeup_interruptible(osal_wait *wait)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_wait.h"
```

**功能说明**

- 唤醒阻塞在指定等待队列上的可中断等待线程。
- 与 osal_wait_interruptible 配对使用。
- 在 LiteOS 上等价于 osal_wait_wakeup。
- 支持 linux、LiteOS 系统。

**前置条件**

- 调用时序约束：当前接口必须在 osal_wait_init 成功返回后调用。
- 依赖关系：改变等待条件后须调用本接口唤醒等待队列上的线程。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| wait | [osal_wait](#osal_wait) * | 待唤醒的等待队列句柄 | 不为NULL 且 wait->wait 已初始化 |

### osal_wait_destroy <a id="osal_wait_destroy"></a>

```c
void osal_wait_destroy(osal_wait *wait)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_wait.h"
```

**功能说明**

- 销毁等待队列并释放其占用的资源。
- 销毁后 wait->wait 被置空，等待队列不可再使用。
- 支持 linux、LiteOS、FreeRTOS 系统。

**前置条件**

- 调用时序约束：当前接口必须在 osal_wait_init 成功返回后调用。
- 依赖关系：销毁后等待队列不可再使用，调用方应确保无其他线程正在该队列上等待。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| wait | [osal_wait](#osal_wait) * | 待销毁的等待队列句柄 | 不为NULL 且 wait->wait 已初始化 |

**参考案例**

- `src/middleware/utils/hcc/comm/hcc.c`

## Type definitions

### osal_wait_condition_func <a id="osal_wait_condition_func"></a>

```c
/* return value is a bool type */
typedef int (*osal_wait_condition_func)(const void *param);
```

**使用说明**

等待队列条件判断回调函数指针类型，在 osal_wait_interruptible、osal_wait_uninterruptible、osal_wait_timeout_interruptible、osal_wait_timeout_uninterruptible 等待接口中每次唤醒时被调用以判定等待条件是否满足。

回调说明：
- 调用时机：等待队列每次被唤醒时调用。
- 参数 param：由等待接口的 param 入参透传而来，用于条件判定的上下文数据。
- 返回值处理：返回非零值表示条件满足（结束等待），返回 0 表示条件未满足（继续等待）；返回值按布尔类型使用。

## Structures

### osal_wait <a id="osal_wait"></a>

```c
typedef struct {
    void *wait;
} osal_wait;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| wait | void * | 等待队列底层句柄；由 osal_wait_init 写入，调用方不应直接访问或修改 |

## Macros

### OSAL_WAIT_FOREVER <a id="OSAL_WAIT_FOREVER"></a>

```c
#define OSAL_WAIT_FOREVER 0xFFFFFFFF
```
