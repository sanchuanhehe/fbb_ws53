# Delaywork

Delaywork 提供延迟工作队列功能，支持在指定超时时间后将任务提交到内核全局工作队列执行，并支持延迟工作的初始化、销毁、调度与同步取消。

**模块公共头文件**

```c
#include "src/kernel/osal/include/schedule/osal_delaywork.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_delayedwork_init](#osal_delayedwork_init) | 初始化延迟工作对象 |
| [osal_delayedwork_destroy](#osal_delayedwork_destroy) | 销毁延迟工作对象 |
| [osal_delayedwork_schedule](#osal_delayedwork_schedule) | 将延迟工作提交到全局工作队列并在指定超时后执行 |
| [osal_delayedwork_cancel_sync](#osal_delayedwork_cancel_sync) | 同步取消延迟工作并等待其执行完成 |

## Functions

### osal_delayedwork_init <a id="osal_delayedwork_init"></a>

```c
int osal_delayedwork_init(osal_delayedwork *work, osal_delayedwork_handler handler)
```

**声明头文件**

```c
#include "src/kernel/osal/include/schedule/osal_delaywork.h"
```

**功能说明**

- 初始化延迟工作对象，分配内核延迟工作资源并关联回调处理函数。
- 延迟工作节点纳入调度管理。
- 初始化完成后可通过 osal_delayedwork_schedule 调度执行。

**前置条件**

- 调用时序约束：当前接口必须在延迟工作对象使用前调用，且必须通过 osal_delayedwork_destroy 释放资源。
- 上下文限制：当前接口在 Linux 内核空间调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| work | [osal_delayedwork](#osal_delayedwork) * | 待初始化的延迟工作对象指针 | 不为 NULL，且 work->work 为 NULL |
| handler | [osal_delayedwork_handler](#osal_delayedwork_handler) | 延迟工作超时回调处理函数 | 不为 NULL |

**返回值**

返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)：0 | 执行成功 | 延迟工作对象初始化成功 |
| [OSAL_FAILURE](#OSAL_FAILURE)：-1 | 执行失败 | work 为 NULL、work->work 非 NULL 或内存分配失败 |

### osal_delayedwork_destroy <a id="osal_delayedwork_destroy"></a>

```c
void osal_delayedwork_destroy(osal_delayedwork *work)
```

**声明头文件**

```c
#include "src/kernel/osal/include/schedule/osal_delaywork.h"
```

**功能说明**

- 销毁延迟工作对象，释放内核延迟工作资源。
- 从内部管理链表中移除对应节点。
- 释放延迟工作对象关联的内核资源并将 work->work 置空。

**前置条件**

- 调用时序约束：当前接口必须在 osal_delayedwork_init 成功返回后调用。
- 上下文限制：当前接口在 Linux 内核空间调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| work | [osal_delayedwork](#osal_delayedwork) * | 待销毁的延迟工作对象指针 | 不为 NULL，且 work->work 不为 NULL |

### osal_delayedwork_schedule <a id="osal_delayedwork_schedule"></a>

```c
int osal_delayedwork_schedule(osal_delayedwork *work, int timeout)
```

**声明头文件**

```c
#include "src/kernel/osal/include/schedule/osal_delaywork.h"
```

**功能说明**

- 将延迟工作提交到内核全局工作队列，在指定超时时间后执行回调处理函数。
- 超时时间以毫秒为单位，内部转换为 jiffies 后调度执行。
- 超时时间为 0 时立即提交执行。

**前置条件**

- 调用时序约束：当前接口必须在 osal_delayedwork_init 成功返回后调用。
- 上下文限制：当前接口在 Linux 内核空间调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| work | [osal_delayedwork](#osal_delayedwork) * | 待调度的延迟工作对象指针 | 不为 NULL，且 work->work 不为 NULL |
| timeout | int | 延迟执行的超时时间，单位 ms | 0 表示立即执行，大于 0 为延迟毫秒数 |

**返回值**

返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)：0 | 执行成功 | 延迟工作调度成功 |
| [OSAL_FAILURE](#OSAL_FAILURE)：-1 | 执行失败 | work 为 NULL 或 work->work 为 NULL |

### osal_delayedwork_cancel_sync <a id="osal_delayedwork_cancel_sync"></a>

```c
int osal_delayedwork_cancel_sync(osal_delayedwork *work)
```

**声明头文件**

```c
#include "src/kernel/osal/include/schedule/osal_delaywork.h"
```

**功能说明**

- 同步取消延迟工作，等待正在执行的回调处理函数完成后返回。
- 取消尚未执行的延迟工作调度。
- 确保回调处理函数在当前接口返回后不再运行。

**前置条件**

- 调用时序约束：当前接口必须在 osal_delayedwork_init 成功返回后调用。
- 上下文限制：当前接口在 Linux 内核空间调用，禁止在回调处理函数中调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| work | [osal_delayedwork](#osal_delayedwork) * | 待取消的延迟工作对象指针 | 不为 NULL，且 work->work 不为 NULL |

**返回值**

返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)：0 | 执行成功 | 延迟工作取消成功 |
| [OSAL_FAILURE](#OSAL_FAILURE)：-1 | 执行失败 | work 为 NULL 或 work->work 为 NULL |

## Type definitions

### osal_delayedwork_handler <a id="osal_delayedwork_handler"></a>

```c
typedef void (*osal_delayedwork_handler)(osal_delayedwork *delayedwork);
```

**使用说明**

延迟工作超时回调函数指针类型，在延迟工作超时后由内核工作队列调用。回调说明：调用时机为延迟工作超时后由内核工作队列触发；参数 delayedwork 为触发超时的延迟工作对象；返回值为 void，回调返回值不被检查。

## Structures

### osal_delayedwork <a id="osal_delayedwork"></a>

```c
typedef struct osal_delayedwork_ {
    void *work;
    void (*handler)(struct osal_delayedwork_ *delayedwork);
} osal_delayedwork;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| work | void * | 内核延迟工作对象指针，由初始化接口填充 |
| handler | void (\*)(struct osal_delayedwork_ \*) | 延迟工作超时回调处理函数指针 |

## Macros

### OSAL_SUCCESS <a id="OSAL_SUCCESS"></a>

```c
#define OSAL_SUCCESS 0
```

### OSAL_FAILURE <a id="OSAL_FAILURE"></a>

```c
#define OSAL_FAILURE (-1)
```
