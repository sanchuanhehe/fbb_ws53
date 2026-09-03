# Task

task 提供操作系统抽象层（OSAL，Operating System Abstraction Layer）的任务调度与管理功能，支持线程创建与销毁、优先级设置、CPU（Central Processing Unit）亲和性绑定、调度锁定与解锁、线程状态控制、延时等待以及内核初始化与状态查询。

**模块公共头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_kthread_create](#osal_kthread_create) | 创建内核线程 |
| [osal_kthread_create_static_ext](#osal_kthread_create_static_ext) | 使用静态栈创建线程 |
| [osal_kthread_create_ext](#osal_kthread_create_ext) | 使用初始化结构体创建线程 |
| [osal_kthread_set_priority](#osal_kthread_set_priority) | 设置线程优先级 |
| [osal_kthread_set_affinity](#osal_kthread_set_affinity) | 设置线程的 CPU 亲和性 |
| [osal_kthread_should_stop](#osal_kthread_should_stop) | 检查线程是否应停止运行 |
| [osal_kthread_wakeup_process](#osal_kthread_wakeup_process) | 唤醒指定线程 |
| [osal_kthread_bind](#osal_kthread_bind) | 绑定线程到指定 CPU 核心运行 |
| [osal_kthread_lock](#osal_kthread_lock) | 锁定任务调度 |
| [osal_kthread_unlock](#osal_kthread_unlock) | 解锁任务调度 |
| [osal_kthread_destroy](#osal_kthread_destroy) | 销毁已创建的线程 |
| [osal_kthread_schedule](#osal_kthread_schedule) | 将当前线程设置为不可中断睡眠状态并延时 |
| [osal_kthread_set_uninterrupt](#osal_kthread_set_uninterrupt) | 将当前线程设置为不可中断状态 |
| [osal_kthread_set_running](#osal_kthread_set_running) | 将当前线程状态设置为可运行 |
| [osal_cond_resched](#osal_cond_resched) | 主动让出 CPU 资源以避免软死锁 |
| [osal_schedule](#osal_schedule) | 将当前任务放回就绪队列并触发调度 |
| [osal_kneon_begin](#osal_kneon_begin) | 启用 NEON 算法加速 |
| [osal_kneon_end](#osal_kneon_end) | 关闭 NEON 算法加速 |
| [osal_yield](#osal_yield) | 暂停当前线程并重新竞争调度权 |
| [osal_get_current_pid](#osal_get_current_pid) | 获取当前线程的 PID |
| [osal_get_current_tid](#osal_get_current_tid) | 获取当前线程的 TID |
| [osal_get_current_tgid](#osal_get_current_tgid) | 获取当前线程的 TGID |
| [osal_get_current_taskname](#osal_get_current_taskname) | 获取当前线程的名称 |
| [osal_msleep](#osal_msleep) | 以毫秒为单位休眠当前线程 |
| [osal_msleep_uninterruptible](#osal_msleep_uninterruptible) | 以毫秒为单位不可中断休眠 |
| [osal_udelay](#osal_udelay) | 以微秒为单位忙等待延时 |
| [osal_mdelay](#osal_mdelay) | 以毫秒为单位忙等待延时 |
| [osal_kthread_suspend](#osal_kthread_suspend) | 挂起指定线程 |
| [osal_kthread_resume](#osal_kthread_resume) | 恢复已挂起的线程 |
| [osal_kernel_init](#osal_kernel_init) | 初始化内核 |
| [osal_kernel_start](#osal_kernel_start) | 启动内核 |
| [osal_kernel_get_state](#osal_kernel_get_state) | 获取内核运行状态 |

## Functions

### osal_kthread_create <a id="osal_kthread_create"></a>

```c
osal_task *osal_kthread_create(osal_kthread_handler handler, void *data, const char *name, unsigned int stack_size)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 创建一个内核线程并启动运行。
- 通过传入的处理函数、数据指针、线程名称和栈大小来配置线程参数。
- 创建成功时返回线程指针，失败时返回 NULL。

**前置条件**

- 调用时序约束：handler 参数不可为 NULL，否则创建失败。
- 依赖关系：系统内存资源需充足，用于分配线程控制块和栈空间。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| handler | [osal_kthread_handler](#osal_kthread_handler) | 线程入口处理函数 | 不为NULL |
| data | void * | 传递给线程入口函数的参数数据 | - |
| name | const char * | 线程名称，用于标识和调试 | - |
| stack_size | unsigned int | 线程栈空间大小（字节） | 大于0 |

**返回值**

- 返回类型：osal_task *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL指针 | 线程创建成功 | 线程创建并启动成功 |
| NULL | 线程创建失败 | handler 为 NULL 或内存分配失败或内核创建线程失败 |

**参考案例**

- `src/application/samples/peripheral/blinky/blinky_demo.c`

### osal_kthread_create_static_ext <a id="osal_kthread_create_static_ext"></a>

```c
osal_task *osal_kthread_create_static_ext(osal_kthread_init *init_handle, void *topStack)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 使用静态分配的栈空间创建线程。
- 通过初始化结构体配置线程参数（入口函数、优先级、栈大小、名称等）。
- 适用于需要确定性内存分配的场景。

**前置条件**

- 调用时序约束：init_handle 参数不可为 NULL，否则返回 NULL。
- 依赖关系：需启用 LOSCFG_TASK_STACK_STATIC_ALLOCATION 宏，否则返回 NULL。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| init_handle | [osal_kthread_init](#osal_kthread_init) * | 线程初始化配置结构体 | 不为NULL |
| topStack | void * | 静态分配的栈空间指针 | - |

**返回值**

- 返回类型：osal_task *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL指针 | 线程创建成功 | 静态栈线程创建成功 |
| NULL | 线程创建失败 | init_handle 为 NULL 或未启用静态栈分配或内存分配失败或 LOS_TaskCreateStatic 失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| LOSCFG_TASK_STACK_STATIC_ALLOCATION | 特性宏 | 支持静态栈线程创建（接口级，liteos 实现体由 #ifdef 包裹；LiteOS Kconfig 声明） | n |

### osal_kthread_create_ext <a id="osal_kthread_create_ext"></a>

```c
osal_task *osal_kthread_create_ext(osal_kthread_init *init_handle)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 使用初始化结构体创建线程，栈空间由系统动态分配。
- 通过初始化结构体配置线程参数（入口函数、优先级、栈大小、名称等）。
- 适用于需要自定义线程优先级和栈大小的场景。

**前置条件**

- 调用时序约束：init_handle 参数不可为 NULL，否则返回 NULL。
- 依赖关系：系统内存资源需充足，用于分配线程控制块和栈空间。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| init_handle | [osal_kthread_init](#osal_kthread_init) * | 线程初始化配置结构体 | 不为NULL |

**返回值**

- 返回类型：osal_task *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL指针 | 线程创建成功 | 线程创建成功 |
| NULL | 线程创建失败 | init_handle 为 NULL 或内存分配失败或 LOS_TaskCreate 失败 |

### osal_kthread_set_priority <a id="osal_kthread_set_priority"></a>

```c
int osal_kthread_set_priority(osal_task *task, unsigned int priority)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 设置指定线程的调度优先级。
- 优先级参数须使用本模块定义的 OSAL_TASK_PRIORITY_* 系列宏。
- 返回 OSAL_SUCCESS 表示设置成功，返回 OSAL_FAILURE 表示设置失败。

**前置条件**

- 调用时序约束：task 参数及其内部 task 指针不可为 NULL。
- 依赖关系：目标线程需已通过 osal_kthread_create 成功创建。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| task | [osal_task](#osal_task) * | 目标线程指针 | 不为NULL |
| priority | unsigned int | 线程优先级 | [OSAL_TASK_PRIORITY_ABOVE_HIGH](#OSAL_TASK_PRIORITY_ABOVE_HIGH) / [OSAL_TASK_PRIORITY_HIGH](#OSAL_TASK_PRIORITY_HIGH) / [OSAL_TASK_PRIORITY_BELOW_HIGH](#OSAL_TASK_PRIORITY_BELOW_HIGH) / [OSAL_TASK_PRIORITY_ABOVE_MIDDLE](#OSAL_TASK_PRIORITY_ABOVE_MIDDLE) / [OSAL_TASK_PRIORITY_MIDDLE](#OSAL_TASK_PRIORITY_MIDDLE) / [OSAL_TASK_PRIORITY_BELOW_MIDDLE](#OSAL_TASK_PRIORITY_BELOW_MIDDLE) / [OSAL_TASK_PRIORITY_ABOVE_LOW](#OSAL_TASK_PRIORITY_ABOVE_LOW) / [OSAL_TASK_PRIORITY_LOW](#OSAL_TASK_PRIORITY_LOW) / [OSAL_TASK_PRIORITY_BELOW_LOW](#OSAL_TASK_PRIORITY_BELOW_LOW) |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS：0 | 设置成功 | 优先级设置成功 |
| OSAL_FAILURE：-1 | 设置失败 | task 为 NULL 或内核设置优先级失败 |

**参考案例**

- `src/application/samples/peripheral/blinky/blinky_demo.c`
- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`

### osal_kthread_set_affinity <a id="osal_kthread_set_affinity"></a>

```c
void osal_kthread_set_affinity(osal_task *task, int cpu_mask)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 设置线程的 CPU 亲和性，指定线程可在哪些 CPU 核心上运行。
- 通过位掩码指定目标 CPU 核心，支持同时指定多个核心。
- 当 cpu_mask 为 0 时不执行任何操作。

**前置条件**

- 调用时序约束：task 参数不可为 NULL。
- 依赖关系：目标线程需已通过 osal_kthread_create 成功创建。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| task | [osal_task](#osal_task) * | 目标线程指针 | 不为NULL |
| cpu_mask | int | CPU 核心掩码 | OSAL_CPU_ALL：0 / OSAL_CPU_0：2 / OSAL_CPU_1：4 / OSAL_CPU_2：8 / OSAL_CPU_3：16 |

**参考案例**

- `src/protocol/wifi/source/host/frw/frw_thread.c`

### osal_kthread_should_stop <a id="osal_kthread_should_stop"></a>

```c
int osal_kthread_should_stop(void)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 检查当前线程是否应停止运行。
- 用于线程循环体内判断退出条件，配合 osal_kthread_destroy 使用。
- 返回 0 表示线程继续运行，返回 1 表示线程应停止。

**前置条件**

- 调用时序约束：当前线程需处于运行状态。
- 依赖关系：需配合 osal_kthread_destroy 的 stop_flag 参数使用。

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 线程应继续运行 | 未收到停止请求 |
| 1 | 线程应停止 | 收到 kthread_stop 停止请求 |


### osal_kthread_wakeup_process <a id="osal_kthread_wakeup_process"></a>

```c
int osal_kthread_wakeup_process(osal_task *task)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 唤醒指定的线程。
- 将处于睡眠状态的线程唤醒使其进入可运行状态。
- 返回 0 表示唤醒成功，返回 -1 表示唤醒失败。

**前置条件**

- 调用时序约束：task 参数不可为 NULL，否则返回 -1。
- 依赖关系：目标线程需已通过 osal_kthread_create 成功创建。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| task | [osal_task](#osal_task) * | 待唤醒的目标线程指针 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 唤醒成功 | 线程成功被唤醒 |
| -1 | 唤醒失败 | task 为 NULL 或唤醒操作失败 |

### osal_kthread_bind <a id="osal_kthread_bind"></a>

```c
void osal_kthread_bind(osal_task *task, unsigned int cpu)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 将指定线程绑定到特定 CPU 核心上运行。
- 绑定后线程只会在指定的 CPU 核心上调度执行。
- 当 task 为 NULL 时不执行任何操作。

**前置条件**

- 调用时序约束：task 参数不可为 NULL。
- 依赖关系：目标线程需已通过 osal_kthread_create 成功创建。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| task | [osal_task](#osal_task) * | 目标线程指针 | 不为NULL |
| cpu | unsigned int | 绑定的 CPU 核心编号 | 0 ~ 系统最大CPU核心数-1 |

### osal_kthread_lock <a id="osal_kthread_lock"></a>

```c
void osal_kthread_lock(void)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 锁定任务调度，防止当前任务被切换。
- 调度锁定期间中断仍可触发，但不会发生任务切换。

**前置条件**

- 调用时序约束：须与 osal_kthread_unlock 配对调用，确保锁计数最终归零。
- 上下文限制：禁止在中断上下文中调用。

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`

### osal_kthread_unlock <a id="osal_kthread_unlock"></a>

```c
void osal_kthread_unlock(void)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 解锁任务调度，使任务调度恢复。
- 调用后任务调度锁计数减一，锁计数归零时调度恢复。

**前置条件**

- 调用时序约束：须在 osal_kthread_lock 之后调用，确保锁计数不为负。
- 上下文限制：禁止在中断上下文中调用。

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`

### osal_kthread_destroy <a id="osal_kthread_destroy"></a>

```c
void osal_kthread_destroy(osal_task *task, unsigned int stop_flag)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 销毁已创建的线程并释放相关资源。
- 当 stop_flag 非 0 时，先调用内核接口停止线程再释放资源；当 stop_flag 为 0 时，仅释放资源不停止线程。
- 释放后调用方应将线程指针置为 NULL 以避免悬空指针。

**前置条件**

- 调用时序约束：task 参数及其内部 task 指针不可为 NULL。
- 依赖关系：目标线程需由 osal_kthread_create 创建；stop_flag 非 0 时目标线程函数不能已自行结束。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| task | [osal_task](#osal_task) * | 待销毁的线程指针 | 不为NULL |
| stop_flag | unsigned int | 线程停止标志，0 表示不停止线程，非 0 表示停止线程 | - |


### osal_kthread_schedule <a id="osal_kthread_schedule"></a>

```c
void osal_kthread_schedule(unsigned int sleep_ns)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 将当前线程设置为 TASK_UNINTERRUPTIBLE 状态并睡眠指定纳秒时长。
- 睡眠期间不可被外部信号唤醒，仅由内核在睡眠时间到达后唤醒。
- 睡眠时间单位为纳秒。

**前置条件**

- 调用时序约束：须在线程上下文中调用。
- 上下文限制：禁止在中断上下文中调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| sleep_ns | unsigned int | 睡眠时长（纳秒） | 大于0 |

### osal_kthread_set_uninterrupt <a id="osal_kthread_set_uninterrupt"></a>

```c
void osal_kthread_set_uninterrupt(void)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 将当前线程状态设置为 TASK_UNINTERRUPTIBLE。
- 设置后线程不可被外部信号唤醒，仅可由内核自身唤醒。
- 用于线程需要进入不可中断等待的场景。

**前置条件**

- 调用时序约束：须在线程上下文中调用。
- 上下文限制：禁止在中断上下文中调用。

### osal_kthread_set_running <a id="osal_kthread_set_running"></a>

```c
void osal_kthread_set_running(void)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 将当前线程状态设置为 TASK_RUNNING。
- 设置后线程进入可运行状态，等待调度器选中后即可获得 CPU 执行。
- 不保证立即获得 CPU，仅表示线程已就绪可被调度。

**前置条件**

- 调用时序约束：须在线程上下文中调用。
- 上下文限制：禁止在中断上下文中调用。

### osal_cond_resched <a id="osal_cond_resched"></a>

```c
void osal_cond_resched(void)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 主动让出 CPU 资源，请求重新调度。
- 防止内核态长时间运行导致的软死锁或调度延迟。
- 调用后如果有更高优先级任务就绪，当前任务将被抢占。

**前置条件**

- 调用时序约束：须在内核态线程上下文中调用。
- 上下文限制：禁止在中断上下文中调用。

### osal_schedule <a id="osal_schedule"></a>

```c
void osal_schedule(void)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 将当前任务放回就绪队列并触发调度。
- 当前任务主动让出 CPU，由调度器选择下一个运行的任务。
- 当前任务可能在后续被调度器重新选中执行。

**前置条件**

- 调用时序约束：须在任务上下文中调用。
- 上下文限制：禁止在中断上下文中调用。

### osal_kneon_begin <a id="osal_kneon_begin"></a>

```c
void osal_kneon_begin(void)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 启用内核态 NEON 算法加速。
- 仅在定义了 CONFIG_KERNEL_MODE_NEON 时生效，否则不执行任何操作。
- 用于内核线程中需要使用 NEON 指令进行向量运算的场景。

**前置条件**

- 依赖关系：需启用 CONFIG_KERNEL_MODE_NEON 配置项。
- 上下文限制：须在内核态线程上下文中调用，且须与 osal_kneon_end 配对使用。

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_KERNEL_MODE_NEON | 特性宏 | 支持内核态 NEON 加速功能（分支级） | n |

### osal_kneon_end <a id="osal_kneon_end"></a>

```c
void osal_kneon_end(void)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 关闭内核态 NEON 算法加速。
- 仅在定义了 CONFIG_KERNEL_MODE_NEON 时生效，否则不执行任何操作。

**前置条件**

- 调用时序约束：须在 osal_kneon_begin 之后调用。
- 依赖关系：需启用 CONFIG_KERNEL_MODE_NEON 配置项。
- 上下文限制：须在内核态线程上下文中调用。

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_KERNEL_MODE_NEON | 特性宏 | 支持内核态 NEON 加速功能（分支级） | n |

### osal_yield <a id="osal_yield"></a>

```c
void osal_yield(void)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 暂停当前线程，释放 CPU 时间片。
- 当前线程变为就绪状态，重新与其他线程竞争 CPU 调度权。
- 不保证当前线程会立即让出，取决于调度器决策。

**前置条件**

- 调用时序约束：须在任务上下文中调用。
- 上下文限制：禁止在中断上下文中调用。

**参考案例**

- `src/application/ws53/ws53_application/main.c`

### osal_get_current_pid <a id="osal_get_current_pid"></a>

```c
long osal_get_current_pid(void)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 获取当前线程的 PID（Process IDentifier）。
- 返回当前线程所属进程的标识号。
- 用于在多线程环境中标识当前执行流的进程。

**返回值**

- 返回类型：long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非负整数 | 当前线程的 PID | 正常获取 |

### osal_get_current_tid <a id="osal_get_current_tid"></a>

```c
long osal_get_current_tid(void)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 获取当前线程的 TID（Thread IDentifier）。
- 返回当前线程的唯一标识号。
- 用于在多线程环境中标识当前执行流。

**返回值**

- 返回类型：long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非负整数 | 当前线程的 TID | 正常获取 |
| OSAL_FAILURE：-1 | 获取失败 | LOS_CurTaskIDGet 返回无效值 |

**参考案例**

- `src/kernel/osal_adapt/src/osal_adapt_task.c`

### osal_get_current_tgid <a id="osal_get_current_tgid"></a>

```c
int osal_get_current_tgid(void)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 获取当前线程的 TGID（Thread Group IDentifier）。
- 返回当前线程所属线程组的标识号。
- 用于标识共享相同地址空间的线程组。

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 整数 | 当前线程的 TGID | 正常获取 |

### osal_get_current_taskname <a id="osal_get_current_taskname"></a>

```c
char *osal_get_current_taskname(void)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 获取当前线程的名称字符串。
- 返回线程创建时指定的名称。
- 用于调试和日志中标识当前执行线程。

**返回值**

- 返回类型：char *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL指针 | 当前线程名称字符串 | 正常获取 |

### osal_msleep <a id="osal_msleep"></a>

```c
unsigned long osal_msleep(unsigned int msecs)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 以毫秒为单位使当前线程休眠。
- 休眠期间线程可被信号唤醒。
- 定时到期返回 0，被信号提前唤醒时返回剩余毫秒数。

**前置条件**

- 调用时序约束：须在任务上下文中调用。
- 上下文限制：禁止在中断上下文中调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| msecs | unsigned int | 休眠时长（毫秒） | 大于0 |

**返回值**

- 返回类型：unsigned long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 定时到期 | 休眠完整到期 |
| 非零值 | 剩余毫秒数 | 被信号提前唤醒 |

**参考案例**

- `src/application/samples/peripheral/blinky/blinky_demo.c`

### osal_msleep_uninterruptible <a id="osal_msleep_uninterruptible"></a>

```c
void osal_msleep_uninterruptible(unsigned int msecs)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 以毫秒为单位使当前线程进入不可中断休眠。
- 休眠期间不会被外部信号唤醒，仅在时间到期后由内核唤醒。
- 适用于必须确保休眠完整执行的场景。

**前置条件**

- 调用时序约束：须在任务上下文中调用。
- 上下文限制：禁止在中断上下文中调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| msecs | unsigned int | 休眠时长（毫秒） | 大于0 |


### osal_udelay <a id="osal_udelay"></a>

```c
void osal_udelay(unsigned int usecs)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 以微秒为单位进行忙等待延时。
- 延时期间 CPU 忙等待，不会让出执行权。
- 适用于短时间精确延时场景。

**前置条件**

- 调用时序约束：须在可执行上下文中调用。
- 上下文限制：短延时可在中断上下文中使用，长延时禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| usecs | unsigned int | 延时时长（微秒） | 大于0 |

**参考案例**

- `src/drivers/chips/ws53/rom/app/middleware/utils/hcc/acore/master/comm/hcc_test_service.c`

### osal_mdelay <a id="osal_mdelay"></a>

```c
void osal_mdelay(unsigned int msecs)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 以毫秒为单位进行忙等待延时。
- 延时期间 CPU 忙等待，不会让出执行权。
- 适用于短时间精确延时场景。

**前置条件**

- 调用时序约束：须在可执行上下文中调用。
- 上下文限制：短延时可在中断上下文中使用，长延时禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| msecs | unsigned int | 延时时长（毫秒） | 大于0 |


### osal_kthread_suspend <a id="osal_kthread_suspend"></a>

```c
void osal_kthread_suspend(osal_task *task)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 挂起指定线程，将其从就绪队列中移除。
- 被挂起的线程不再参与调度，直到被 osal_kthread_resume 恢复。
- 若目标线程已处于挂起状态则不重复操作。

**前置条件**

- 调用时序约束：task 参数不可为 NULL。
- 依赖关系：目标线程需已通过 osal_kthread_create 成功创建。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| task | [osal_task](#osal_task) * | 待挂起的目标线程指针 | 不为NULL |

### osal_kthread_resume <a id="osal_kthread_resume"></a>

```c
void osal_kthread_resume(osal_task *task)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 恢复已挂起的线程，将其重新加入就绪队列。
- 仅对通过 osal_kthread_suspend 挂起的线程生效。
- 若目标线程未处于挂起状态则不执行操作。

**前置条件**

- 调用时序约束：task 参数不可为 NULL。
- 依赖关系：目标线程需已通过 osal_kthread_suspend 挂起。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| task | [osal_task](#osal_task) * | 待恢复的目标线程指针 | 不为NULL |

### osal_kernel_init <a id="osal_kernel_init"></a>

```c
unsigned int osal_kernel_init(void)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 初始化内核，完成内核基础数据结构和资源初始化。
- 初始化成功后内核状态由 INACTIVE 转为 READY。

**前置条件**

- 调用时序约束：须在内核处于 INACTIVE 状态时调用，不可重复调用。
- 上下文限制：禁止在中断上下文中调用。

**返回值**

- 返回类型：unsigned int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS：0 | 初始化成功 | 内核初始化完成 |
| OSAL_FAILURE：-1 | 初始化失败 | 在中断中调用或内核非 INACTIVE 状态或 OsMain 失败 |

### osal_kernel_start <a id="osal_kernel_start"></a>

```c
unsigned int osal_kernel_start(void)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 启动内核调度，开始任务调度执行。
- 启动后内核状态由 READY 转为 RUNNING。
- 须在 osal_kernel_init 成功之后调用。

**前置条件**

- 调用时序约束：须在 osal_kernel_init 成功返回后调用，内核须处于 READY 状态。
- 上下文限制：禁止在中断上下文中调用。

**返回值**

- 返回类型：unsigned int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS：0 | 启动成功 | 内核调度已启动 |
| OSAL_FAILURE：-1 | 启动失败 | 在中断中调用或内核非 READY 状态 |

### osal_kernel_get_state <a id="osal_kernel_get_state"></a>

```c
osal_kernel_status osal_kernel_get_state(void)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_task.h"
```

**功能说明**

- 获取内核当前运行状态。
- 返回内核的调度状态（未激活、就绪、运行中、调度锁定、错误）。
- 用于在运行时查询内核调度器的状态信息。

**返回值**

- 返回类型：[osal_kernel_status](#osal_kernel_status)

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_KERNEL_STATUS_INACTIVE：0 | 内核未激活 | 内核尚未初始化 |
| OSAL_KERNEL_STATUS_READY：1 | 内核就绪 | 内核已初始化但未启动调度 |
| OSAL_KERNEL_STATUS_RUNING：2 | 内核运行中 | 内核调度器正在运行 |
| OSAL_KERNEL_STATUS_SCHEDULE_LOCK：3 | 调度已锁定 | 任务调度锁已生效 |
| OSAL_KERNEL_STATUS_ERROR：-1 | 内核状态错误 | 内核状态异常 |

## Type definitions

### osal_kthread_handler <a id="osal_kthread_handler"></a>

```c
typedef int (*osal_kthread_handler)(void *data);
```

**使用说明**

线程入口函数指针类型，用于 osal_kthread_create 创建线程时指定线程处理函数。回调说明：线程创建后由调度器调用执行，参数 data 为创建时传入的用户数据指针，返回值为线程退出码。

## Enumerations

### osal_kernel_status <a id="osal_kernel_status"></a>

```c
typedef enum {
    OSAL_KERNEL_STATUS_INACTIVE         = 0, // Inactive.
    OSAL_KERNEL_STATUS_READY            = 1, // Ready.
    OSAL_KERNEL_STATUS_RUNING           = 2, // Running.
    OSAL_KERNEL_STATUS_SCHEDULE_LOCK    = 3, // Blocked.
    OSAL_KERNEL_STATUS_ERROR            = -1 // Error.
} osal_kernel_status;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| OSAL_KERNEL_STATUS_INACTIVE | 0 | 内核未激活状态 |
| OSAL_KERNEL_STATUS_READY | 1 | 内核就绪状态 |
| OSAL_KERNEL_STATUS_RUNING | 2 | 内核运行中状态 |
| OSAL_KERNEL_STATUS_SCHEDULE_LOCK | 3 | 内核调度锁定状态 |
| OSAL_KERNEL_STATUS_ERROR | -1 | 内核错误状态 |

## Structures

### osal_task <a id="osal_task"></a>

```c
typedef struct {
    void *task;
} osal_task;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| task | void * | 底层任务句柄指针，指向操作系统内核的任务控制块 |

### osal_kthread_init <a id="osal_kthread_init"></a>

```c
typedef struct {
    osal_kthread_handler    handler;    /**< Task entrance function */
    unsigned int            taskprio;   /**< Task priority */
    unsigned int            stacksize;  /**< Task stack size */
    char                    *taskname;  /**< Task name */
    void                    *data;      /**< data */
} osal_kthread_init;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| handler | [osal_kthread_handler](#osal_kthread_handler) | 线程入口函数 |
| taskprio | unsigned int | 线程优先级 |
| stacksize | unsigned int | 线程栈大小（字节） |
| taskname | char * | 线程名称字符串指针 |
| data | void * | 传递给线程入口函数的用户数据指针 |

## Macros

### OSAL_TASK_PRIORITY_ABOVE_HIGH <a id="OSAL_TASK_PRIORITY_ABOVE_HIGH"></a>

```c
#define OSAL_TASK_PRIORITY_ABOVE_HIGH   2
```

### OSAL_TASK_PRIORITY_HIGH <a id="OSAL_TASK_PRIORITY_HIGH"></a>

```c
#define OSAL_TASK_PRIORITY_HIGH         3
```

### OSAL_TASK_PRIORITY_BELOW_HIGH <a id="OSAL_TASK_PRIORITY_BELOW_HIGH"></a>

```c
#define OSAL_TASK_PRIORITY_BELOW_HIGH   4
```

### OSAL_TASK_PRIORITY_ABOVE_MIDDLE <a id="OSAL_TASK_PRIORITY_ABOVE_MIDDLE"></a>

```c
#define OSAL_TASK_PRIORITY_ABOVE_MIDDLE 5
```

### OSAL_TASK_PRIORITY_MIDDLE <a id="OSAL_TASK_PRIORITY_MIDDLE"></a>

```c
#define OSAL_TASK_PRIORITY_MIDDLE       6
```

### OSAL_TASK_PRIORITY_BELOW_MIDDLE <a id="OSAL_TASK_PRIORITY_BELOW_MIDDLE"></a>

```c
#define OSAL_TASK_PRIORITY_BELOW_MIDDLE 7
```

### OSAL_TASK_PRIORITY_ABOVE_LOW <a id="OSAL_TASK_PRIORITY_ABOVE_LOW"></a>

```c
#define OSAL_TASK_PRIORITY_ABOVE_LOW    8
```

### OSAL_TASK_PRIORITY_LOW <a id="OSAL_TASK_PRIORITY_LOW"></a>

```c
#define OSAL_TASK_PRIORITY_LOW          10
```

### OSAL_TASK_PRIORITY_BELOW_LOW <a id="OSAL_TASK_PRIORITY_BELOW_LOW"></a>

```c
#define OSAL_TASK_PRIORITY_BELOW_LOW    11
```
