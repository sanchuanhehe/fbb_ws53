# Semaphore

osal_semaphore 提供信号量功能，用于任务间同步与互斥，支持计数信号量与二值信号量的创建、获取、释放、超时获取、尝试获取及销毁操作。

**头文件清单**

```c
#include "semaphore/osal_semaphore.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_sem_init](#osal_sem_init) | 创建信号量并按指定初始值初始化信号量控制结构 |
| [osal_sem_binary_sem_init](#osal_sem_binary_sem_init) | 创建二值信号量并按指定初始值初始化信号量控制结构 |
| [osal_sem_down](#osal_sem_down) | 请求获取信号量，未获取时永久阻塞等待 |
| [osal_sem_down_timeout](#osal_sem_down_timeout) | 在指定超时时间内请求获取信号量 |
| [osal_sem_down_interruptible](#osal_sem_down_interruptible) | 请求获取信号量，阻塞等待期间可被信号中断 |
| [osal_sem_trydown](#osal_sem_trydown) | 尝试获取信号量，不阻塞等待 |
| [osal_sem_up](#osal_sem_up) | 释放信号量 |
| [osal_sem_destroy](#osal_sem_destroy) | 销毁信号量并释放资源 |

## Functions

### osal_sem_init <a id="osal_sem_init"></a>

```c
int osal_sem_init(osal_semaphore *sem, int val)
```

**头文件清单**

```c
#include "semaphore/osal_semaphore.h"
```

**功能说明**

- 创建信号量并按指定初始可用数量初始化信号量控制结构
- 支持设置初始信号量计数值（val），作为可用信号量的初始数量
- 适用于任务间同步与资源计数场景

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| val | int | 信号量初始可用数量 | >= 0 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| sem | [osal_semaphore](#struct_osal_semaphore) * | 信号量控制结构指针，由函数初始化填充 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)(0) | 执行成功 | 信号量创建并初始化成功 |
| [OSAL_FAILURE](#OSAL_FAILURE)(-1) | 执行失败 | 参数无效（sem 为 NULL、sem 已初始化或 val 为负数）或内存分配失败 |

**参考案例**

- `src/middleware/utils/hcc/host/hcc_sdio_host.c`
- `src/protocol/wifi/source/host/hmac/hmac_sniffer.c`

### osal_sem_binary_sem_init <a id="osal_sem_binary_sem_init"></a>

```c
int osal_sem_binary_sem_init(osal_semaphore *sem, int val)
```

**头文件清单**

```c
#include "semaphore/osal_semaphore.h"
```

**功能说明**

- 创建二值信号量并按指定初始值初始化信号量控制结构
- 初始值取值范围为 0 或 1，表示信号量的初始可用状态
- 适用于仅需两种状态（可用/不可用）的同步场景

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| val | int | 二值信号量初始可用数量 | 0 ~ 1 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| sem | [osal_semaphore](#struct_osal_semaphore) * | 信号量控制结构指针，由函数初始化填充 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)(0) | 执行成功 | 二值信号量创建并初始化成功 |
| [OSAL_FAILURE](#OSAL_FAILURE)(-1) | 执行失败 | 参数无效（sem 为 NULL 或 val 不在 0~1 范围）或创建失败 |

**参考案例**

- `src/middleware/utils/dfx/log_reader/log_uart.c`
- `src/middleware/utils/nv/nv_storage_lib/nv_async_store.c`

### osal_sem_down <a id="osal_sem_down"></a>

```c
int osal_sem_down(osal_semaphore *sem)
```

**头文件清单**

```c
#include "semaphore/osal_semaphore.h"
```

**功能说明**

- 请求获取信号量，若信号量不可用则将当前任务阻塞等待
- 信号量可用时获取成功，信号量计数值递减
- 阻塞等待为永久等待，直到信号量被释放

**前置条件**

- 调用时序约束：当前接口必须在 `osal_sem_init` 成功返回后调用
- 上下文限制：禁止在中断上下文调用，禁止在系统任务（idle、swtmr）中调用，不推荐在软件定时器回调中使用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| sem | [osal_semaphore](#struct_osal_semaphore) * | 待获取的信号量 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)(0) | 执行成功 | 成功获取信号量 |
| [OSAL_FAILURE](#OSAL_FAILURE)(-1) | 执行失败 | 参数无效（sem 为 NULL）或获取信号量失败 |

**参考案例**

- `src/middleware/utils/dfx/log_reader/log_uart.c`
- `src/protocol/wifi/source/host/hmac/hmac_sniffer.c`

### osal_sem_down_timeout <a id="osal_sem_down_timeout"></a>

```c
int osal_sem_down_timeout(osal_semaphore *sem, unsigned int timeout)
```

**头文件清单**

```c
#include "semaphore/osal_semaphore.h"
```

**功能说明**

- 在指定超时时间内请求获取信号量
- 信号量可用时获取成功；超时未获取则停止等待并返回失败
- 超时时间可设置为 OSAL_SEM_WAIT_FOREVER 表示永久等待

**前置条件**

- 调用时序约束：当前接口必须在 `osal_sem_init` 成功返回后调用
- 上下文限制：禁止在中断上下文调用，禁止在系统任务（idle、swtmr）中调用，不推荐在软件定时器回调中使用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| sem | [osal_semaphore](#struct_osal_semaphore) * | 待获取的信号量 | 不为NULL |
| timeout | unsigned int | 等待超时时间（单位 ms） | [OSAL_SEM_WAIT_FOREVER](#OSAL_SEM_WAIT_FOREVER)(-1) / 0 ~ 0xFFFFFFFE |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)(0) | 执行成功 | 在超时时间内成功获取信号量 |
| [OSAL_FAILURE](#OSAL_FAILURE)(-1) | 执行失败 | 参数无效（sem 为 NULL）、超时未获取或获取失败 |

**参考案例**

- `src/middleware/utils/hcc/host/hcc_sdio_host.c`
- `src/middleware/utils/nv/nv_storage_lib/nv_async_store.c`

### osal_sem_down_interruptible <a id="osal_sem_down_interruptible"></a>

```c
int osal_sem_down_interruptible(osal_semaphore *sem)
```

**头文件清单**

```c
#include "semaphore/osal_semaphore.h"
```

**功能说明**

- 请求获取信号量，若信号量不可用则将当前任务阻塞等待
- 阻塞等待期间可被信号中断，中断后停止等待并返回
- 适用于需要在等待信号量时响应信号的场景

**前置条件**

- 调用时序约束：当前接口必须在 `osal_sem_init` 成功返回后调用
- 上下文限制：接口会使任务进入睡眠，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| sem | [osal_semaphore](#struct_osal_semaphore) * | 待获取的信号量 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)(0) | 执行成功 | 成功获取信号量 |
| [OSAL_FAILURE](#OSAL_FAILURE)(-1) | 执行失败 | 参数无效（sem 为 NULL）或获取信号量失败 |
| [OSAL_EINTR](#OSAL_EINTR)(-4) | 被信号中断 | 阻塞等待期间被信号中断 |

### osal_sem_trydown <a id="osal_sem_trydown"></a>

```c
int osal_sem_trydown(osal_semaphore *sem)
```

**头文件清单**

```c
#include "semaphore/osal_semaphore.h"
```

**功能说明**

- 尝试获取信号量，不阻塞当前任务
- 信号量可用时获取成功，不可用时立即返回失败状态
- 可在中断上下文调用，信号量可由任意任务或中断释放

**前置条件**

- 调用时序约束：当前接口必须在 `osal_sem_init` 成功返回后调用
- 上下文限制：当前接口可在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| sem | [osal_semaphore](#struct_osal_semaphore) * | 待获取的信号量 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 获取信号量成功 | 成功获取信号量 |
| 1 | 未能获取信号量 | 信号量不可获取或参数无效，函数立即返回不等待 |

### osal_sem_up <a id="osal_sem_up"></a>

```c
void osal_sem_up(osal_semaphore *sem)
```

**头文件清单**

```c
#include "semaphore/osal_semaphore.h"
```

**功能说明**

- 释放信号量，信号量计数值递增
- 若有任务正在等待该信号量，释放后唤醒等待任务
- 可在任意上下文调用，包括未获取过该信号量的任务

**前置条件**

- 调用时序约束：当前接口必须在 `osal_sem_init` 成功返回后调用
- 上下文限制：当前接口可在任意上下文调用，包括未调用过 `osal_sem_down` 的任务

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| sem | [osal_semaphore](#struct_osal_semaphore) * | 待释放的信号量 | 不为NULL |

**参考案例**

- `src/middleware/utils/hcc/host/hcc_sdio_host.c`
- `src/middleware/utils/dfx/log_reader/log_uart.c`

### osal_sem_destroy <a id="osal_sem_destroy"></a>

```c
void osal_sem_destroy(osal_semaphore *sem)
```

**头文件清单**

```c
#include "semaphore/osal_semaphore.h"
```

**功能说明**

- 销毁信号量并释放其占用的资源
- 销毁后信号量控制结构不再可用
- 适用于信号量不再需要时的资源回收

**前置条件**

- 调用时序约束：当前接口必须在 `osal_sem_init` 成功返回后调用
- 依赖关系：销毁后信号量句柄失效，不可再用于其他信号量接口

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| sem | [osal_semaphore](#struct_osal_semaphore) * | 待销毁的信号量 | 不为NULL |

**参考案例**

- `src/middleware/utils/hcc/host/hcc_sdio_host.c`

## Structures

### osal_semaphore <a id="struct_osal_semaphore"></a>

```c
typedef struct {
    void *sem;
} osal_semaphore;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| sem | void * | 信号量内部句柄指针，由 osal_sem_init 或 osal_sem_binary_sem_init 初始化填充 |

## Macros

### OSAL_SEM_WAIT_FOREVER <a id="OSAL_SEM_WAIT_FOREVER"></a>

```c
#define OSAL_SEM_WAIT_FOREVER (-1)
```

### OSAL_SUCCESS <a id="OSAL_SUCCESS"></a> [SDK公共共享宏]

```c
#define OSAL_SUCCESS 0
```

### OSAL_FAILURE <a id="OSAL_FAILURE"></a> [SDK公共共享宏]

```c
#define OSAL_FAILURE (-1)
```

### OSAL_EINTR <a id="OSAL_EINTR"></a> [SDK公共共享宏]

```c
#define OSAL_EINTR (-4)  /* Interrupted system call */
```
