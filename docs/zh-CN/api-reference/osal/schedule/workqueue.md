# Workqueue

workqueue 提供工作队列功能，用于在系统全局工作队列中异步调度执行工作任务，支持工作队列的初始化、调度、销毁与刷新操作。

**头文件清单**

```c
#include "schedule/osal_workqueue.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_workqueue_init](#osal_workqueue_init) | 初始化工作队列，关联回调处理函数 |
| [osal_workqueue_schedule](#osal_workqueue_schedule) | 将工作任务加入全局工作队列异步执行 |
| [osal_workqueue_destroy](#osal_workqueue_destroy) | 销毁工作队列，释放内部资源 |
| [osal_workqueue_flush](#osal_workqueue_flush) | 等待工作队列完成最后一次调度执行 |

## Functions

### osal_workqueue_init <a id="osal_workqueue_init"></a>

```c
int osal_workqueue_init(osal_workqueue *work, osal_workqueue_handler handler)
```

**头文件清单**

```c
#include "schedule/osal_workqueue.h"
```

**功能说明**

- 初始化工作队列，建立工作队列与回调处理函数的关联
- 初始化完成后工作队列进入可调度状态
- 支持 Linux、LiteOS、FreeRTOS 系统

**前置条件**

- 调用时序约束：work 必须未被初始化（work->work 应为 NULL），禁止重复初始化
- 依赖关系：当前接口是工作队列模块的初始化接口，需在调度、刷新、销毁等操作之前调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| work | [osal_workqueue](#osal_workqueue) * | 待初始化的工作队列结构体指针 | 不为NULL，且 work->work 为NULL |
| handler | [osal_workqueue_handler](#osal_workqueue_handler) | 工作队列回调处理函数，在工作被调度执行时调用 | 有效函数指针或NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| work | [osal_workqueue](#osal_workqueue) * | 函数向 work->work 写入内部工作结构体指针，向 work->handler 写入回调函数指针 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS):0 | 初始化成功 | 工作队列初始化成功，关联回调处理函数 |
| [OSAL_FAILURE](#OSAL_FAILURE):-1 | 初始化失败 | work 为 NULL、work->work 不为 NULL，或内存分配失败 |

### osal_workqueue_schedule <a id="osal_workqueue_schedule"></a>

```c
int osal_workqueue_schedule(osal_workqueue *work)
```

**头文件清单**

```c
#include "schedule/osal_workqueue.h"
```

**功能说明**

- 将工作任务加入系统全局工作队列进行异步执行
- 若工作已在队列中，保持其在队列中的原有位置
- 支持 Linux、LiteOS、FreeRTOS 系统

**前置条件**

- 调用时序约束：当前接口必须在 osal_workqueue_init() 成功返回后调用
- 依赖关系：work 必须已通过 osal_workqueue_init() 完成初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| work | [osal_workqueue](#osal_workqueue) * | 待调度的工作队列结构体指针 | 不为NULL，且 work->work 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 1 | 调度成功 | 工作成功加入全局工作队列 |
| 0 | 调度失败 | work 为 NULL、work->work 为 NULL，或工作已在队列中 |

### osal_workqueue_destroy <a id="osal_workqueue_destroy"></a>

```c
void osal_workqueue_destroy(osal_workqueue *work)
```

**头文件清单**

```c
#include "schedule/osal_workqueue.h"
```

**功能说明**

- 销毁工作队列，释放内部工作资源
- 销毁后工作队列不再可用，需重新初始化才能使用
- 支持 Linux、LiteOS、FreeRTOS 系统

**前置条件**

- 调用时序约束：当前接口必须在 osal_workqueue_init() 成功返回后调用，销毁后禁止再使用该 work
- 依赖关系：work 必须由 osal_workqueue_init() 创建，销毁操作会释放内存

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| work | [osal_workqueue](#osal_workqueue) * | 待销毁的工作队列结构体指针 | 不为NULL，且 work->work 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| work | [osal_workqueue](#osal_workqueue) * | 函数将 work->work 置为 NULL，释放内部工作结构体内存 |

### osal_workqueue_flush <a id="osal_workqueue_flush"></a>

```c
int osal_workqueue_flush(osal_workqueue *work)
```

**头文件清单**

```c
#include "schedule/osal_workqueue.h"
```

**功能说明**

- 等待工作队列完成最后一次调度执行
- 阻塞直到当前工作执行完成
- 支持 Linux、LiteOS 系统

**前置条件**

- 调用时序约束：当前接口必须在 osal_workqueue_init() 成功返回后调用
- 依赖关系：work 必须已通过 osal_workqueue_init() 完成初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| work | [osal_workqueue](#osal_workqueue) * | 待刷新的工作队列结构体指针 | 不为NULL，且 work->work 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_FAILURE](#OSAL_FAILURE):-1 | 参数无效 | work 为 NULL 或 work->work 为 NULL |
| 1 | 刷新完成 | 工作已在队列中或正在执行，flush_work 返回非零值，已等待其完成 |
| 0 | 无需刷新 | 工作未在队列中且未在执行，flush_work 返回 0 |

## Type definitions

### osal_workqueue_handler <a id="osal_workqueue_handler"></a>

```c
typedef void (*osal_workqueue_handler)(osal_workqueue *workqueue);
```

**使用说明**

工作队列回调处理函数指针类型，在工作被调度执行时由工作队列调用，接收关联的工作队列结构体指针作为参数。

## Structures

### osal_workqueue <a id="osal_workqueue"></a>

```c
typedef struct osal_workqueue_ {
    int queue_flag;
    void *work;
    void (*handler)(struct osal_workqueue_ *workqueue);
} osal_workqueue;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| queue_flag | int | 工作队列标志位 |
| work | void * | 内部工作结构体指针 |
| handler | void (*)(struct osal_workqueue_ *workqueue) | 工作队列回调处理函数指针，在工作被调度执行时调用 |

## Macros

### OSAL_SUCCESS <a id="OSAL_SUCCESS"></a> [SDK公共共享宏]

```c
#define OSAL_SUCCESS 0
```

### OSAL_FAILURE <a id="OSAL_FAILURE"></a> [SDK公共共享宏]

```c
#define OSAL_FAILURE (-1)
```
