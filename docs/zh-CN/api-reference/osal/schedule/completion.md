# Completion

Completion 提供完成量同步原语，用于线程间基于完成事件的阻塞等待与唤醒。该模块属于 OSAL（Operating System Abstraction Layer），对 linux、liteos、freertos 等多操作系统的完成量接口进行统一封装，向上提供一致的同步 API（Application Programming Interface）。

**模块公共头文件**

```c
#include "kernel/osal/include/schedule/osal_completion.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_completion_init](#osal_completion_init) | 初始化一个动态分配的 completion 结构体 |
| [osal_completion_reinit](#osal_completion_reinit) | 将 completion 的完成计数重置为 0 |
| [osal_complete](#osal_complete) | 向 completion 发送完成信号，唤醒一个等待线程 |
| [osal_wait_for_completion](#osal_wait_for_completion) | 阻塞等待 completion 的完成信号 |
| [osal_wait_for_completion_timeout](#osal_wait_for_completion_timeout) | 在超时时间内等待 completion 的完成信号 |
| [osal_complete_all](#osal_complete_all) | 向 completion 发送完成信号，唤醒所有等待线程 |
| [osal_complete_destory](#osal_complete_destory) | 释放动态分配的 completion 资源 |

## Functions

### osal_completion_init <a id="osal_completion_init"></a>

```c
int osal_completion_init(osal_completion *com)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_completion.h"
```

**功能说明**

- 初始化一个动态分配的 completion 结构体。
- 使 completion 进入可用于等待与唤醒的状态。
- 通过返回值指示初始化是否成功。

**前置条件**

- com 必须指向调用方已分配的有效 osal_completion 结构体内存。
- 成功初始化后的 completion 必须通过 osal_complete_destory 释放。

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| com | [osal_completion *](#osal_completion) | 指向待初始化的 completion 结构体；调用前其 completion 成员必须为 NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 执行成功 | completion 结构体初始化成功 |
| -1 | 执行失败 | com 为 NULL、completion 已初始化或底层资源分配失败 |

### osal_completion_reinit <a id="osal_completion_reinit"></a>

```c
void osal_completion_reinit(osal_completion *com)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_completion.h"
```

**功能说明**

- 将指定 completion 的完成计数重置为 0。
- 使 completion 恢复到未完成状态。
- 重置后该 completion 可被重新用于等待与唤醒流程。

**前置条件**

- 调用时序约束：com 必须已通过 osal_completion_init 完成初始化。
- 上下文限制：仅在 linux 系统下可用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| com | [osal_completion *](#osal_completion) | 指向已初始化的 completion 结构体 | 不为 NULL |

### osal_complete <a id="osal_complete"></a>

```c
void osal_complete(osal_completion *com)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_completion.h"
```

**功能说明**

- 向指定 completion 发送完成信号。
- 唤醒一个等待该 completion 的线程。
- 按入队顺序唤醒等待线程。

**前置条件**

- 调用时序约束：com 必须已通过 osal_completion_init 完成初始化。
- 依赖关系：com->completion 必须为非 NULL 的有效指针。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| com | [osal_completion *](#osal_completion) | 指向已初始化的 completion 结构体 | 不为 NULL |

### osal_wait_for_completion <a id="osal_wait_for_completion"></a>

```c
void osal_wait_for_completion(osal_completion *com)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_completion.h"
```

**功能说明**

- 阻塞等待指定 completion 的完成信号。
- 等待过程不可中断。
- 无超时限制，直到收到完成信号才返回。

**前置条件**

- 调用时序约束：com 必须已通过 osal_completion_init 完成初始化。
- 依赖关系：com->completion 必须为非 NULL 的有效指针。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| com | [osal_completion *](#osal_completion) | 指向已初始化的 completion 结构体 | 不为 NULL |

### osal_wait_for_completion_timeout <a id="osal_wait_for_completion_timeout"></a>

```c
unsigned long osal_wait_for_completion_timeout(osal_completion *com, unsigned long timeout)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_completion.h"
```

**功能说明**

- 在指定超时时间内等待 completion 的完成信号。
- 收到完成信号时返回剩余超时时间。
- 超时未收到信号时返回 0。
- 等待过程不可中断。

**前置条件**

- 调用时序约束：com 必须已通过 osal_completion_init 完成初始化。
- 依赖关系：com->completion 必须为非 NULL 的有效指针。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| com | [osal_completion *](#osal_completion) | 指向已初始化的 completion 结构体 | 不为 NULL |
| timeout | unsigned long | 超时等待时间 | 单位为 jiffies（linux）/ tick（liteos） |

**返回值**

- 返回类型：unsigned long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 等待超时 | 在超时时间内未收到完成信号 |
| >0 | 成功完成 | 收到完成信号，返回距离超时的剩余时间 |
| -1 | 执行失败 | com 为 NULL 或 completion 未初始化 |

### osal_complete_all <a id="osal_complete_all"></a>

```c
void osal_complete_all(osal_completion *com)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_completion.h"
```

**功能说明**

- 向指定 completion 发送完成信号。
- 唤醒所有等待该 completion 的线程。
- 一次性唤醒全部等待线程。

**前置条件**

- 调用时序约束：com 必须已通过 osal_completion_init 完成初始化。
- 依赖关系：com->completion 必须为非 NULL 的有效指针。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| com | [osal_completion *](#osal_completion) | 指向已初始化的 completion 结构体 | 不为 NULL |

### osal_complete_destory <a id="osal_complete_destory"></a>

```c
void osal_complete_destory(osal_completion *com)
```

**声明头文件**

```c
#include "kernel/osal/include/schedule/osal_completion.h"
```

**功能说明**

- 释放动态分配的 completion 占用的资源。
- 释放后将 completion 指针置空。
- 释放后该 completion 不再可用。

**前置条件**

- 调用时序约束：com 必须来自 osal_completion_init 成功初始化的 completion。
- 依赖关系：com->completion 必须为非 NULL 的有效指针。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| com | [osal_completion *](#osal_completion) | 指向待释放的 completion 结构体 | 不为 NULL |

## Structures

### osal_completion <a id="osal_completion"></a>

```c
typedef struct {
    void *completion;
} osal_completion;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| completion | void * | 指向底层 completion 实现对象的指针 |
