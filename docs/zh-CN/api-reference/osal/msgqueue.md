# MsgQueue

MsgQueue 提供操作系统抽象层（OSAL, Operating System Abstract Layer）的消息队列功能，支持消息队列的创建、删除、读写与状态查询操作，适用于 LiteOS 与 FreeRTOS 系统。

**模块公共头文件**

```c
#include "msgqueue/osal_msgqueue.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_msg_queue_create](#osal_msg_queue_create) | 创建消息队列 |
| [osal_msg_queue_write_copy](#osal_msg_queue_write_copy) | 向消息队列写入数据 |
| [osal_msg_queue_read_copy](#osal_msg_queue_read_copy) | 从消息队列读取数据 |
| [osal_msg_queue_write_head_copy](#osal_msg_queue_write_head_copy) | 向消息队列头部写入数据 |
| [osal_msg_queue_delete](#osal_msg_queue_delete) | 删除消息队列 |
| [osal_msg_queue_is_full](#osal_msg_queue_is_full) | 检查消息队列是否已满 |
| [osal_msg_queue_get_msg_num](#osal_msg_queue_get_msg_num) | 获取消息队列中的消息数量 |

## Functions

### osal_msg_queue_create <a id="osal_msg_queue_create"></a>

```c
int osal_msg_queue_create(const char *name, unsigned short queue_len, unsigned long *queue_id, unsigned int flags, unsigned short max_msgsize)
```

**声明头文件**

```c
#include "msgqueue/osal_msgqueue.h"
```

**功能说明**

- 创建消息队列，用于任务间消息传递。
- 支持配置队列长度与单个消息节点大小。
- 创建成功后通过 queue_id 返回队列标识。

**前置条件**

- 依赖关系：LiteOS 系统下需启用 LOSCFG_QUEUE_DYNAMIC_ALLOCATION 配置。
- 依赖关系：可用队列数量受 LOSCFG_BASE_IPC_QUEUE_LIMIT 限制。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| name | const char * | 消息队列名称（保留参数，暂未使用） | 可为 NULL |
| queue_len | unsigned short | 队列长度 | 1 ~ 0xFFFF |
| flags | unsigned int | 队列模式（保留参数，暂未使用） | 保留参数 |
| max_msgsize | unsigned short | 单个消息节点大小 | 1 ~ 0xFFFF |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| queue_id | unsigned long * | 成功创建的队列标识 ID |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 执行成功 | 消息队列创建成功 |
| 非 0 | 执行失败 | 消息队列创建失败 |

**参考案例**

- `src/application/ws53/ws53_application/main.c`
- `src/middleware/chips/ws53/dfx/dfx_system_init.c`
- `src/middleware/services/wifi_service/wpa/liteos_wpa_api/wifi_api.c`
- `src/middleware/utils/nv/nv_storage_lib/nv_async_store.c`
- `src/test/common/testsuite/src/test_suite_task.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| TINY_KERNEL | 特性宏 | 精简内核模式下此接口不编译 | 由构建目标决定 |

### osal_msg_queue_write_copy <a id="osal_msg_queue_write_copy"></a>

```c
int osal_msg_queue_write_copy(unsigned long queue_id, void *buffer_addr, unsigned int buffer_size, unsigned int timeout)
```

**声明头文件**

```c
#include "msgqueue/osal_msgqueue.h"
```

**功能说明**

- 向指定消息队列写入数据。
- 写入数据的大小由 buffer_size 指定，数据存储于 buffer_addr 指向的地址。
- 支持超时等待，当队列满时按 timeout 阻塞等待。

**前置条件**

- 调用时序约束：当前接口需在 LiteOS 初始化后调用，且目标队列已通过 osal_msg_queue_create 创建。
- 上下文限制：除 FreeRTOS 外，禁止在中断上下文及软件定时器回调中调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| queue_id | unsigned long | 由 osal_msg_queue_create 创建的队列 ID | 由 osal_msg_queue_create 创建 |
| buffer_addr | void * | 存储待写入数据的缓冲区起始地址 | 不为 NULL |
| buffer_size | unsigned int | 待写入数据的缓冲区大小 | 大于 0 |
| timeout | unsigned int | 超时时间（单位：Tick） | [OSAL_MSGQ_NO_WAIT](#OSAL_MSGQ_NO_WAIT)：0 ~ [OSAL_MSGQ_WAIT_FOREVER](#OSAL_MSGQ_WAIT_FOREVER)(0xFFFFFFFF) |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 执行成功 | 数据写入成功 |
| 非 0 | 执行失败 | 数据写入失败 |

**参考案例**

- `src/application/ws53/ws53_application/main.c`
- `src/middleware/services/wifi_service/wpa/liteos_wpa_api/wifi_api.c`
- `src/middleware/utils/nv/nv_storage_lib/nv_async_store.c`
- `src/test/common/testsuite/src/test_suite_task.c`

### osal_msg_queue_read_copy <a id="osal_msg_queue_read_copy"></a>

```c
int osal_msg_queue_read_copy(unsigned long queue_id, void *buffer_addr, unsigned int *buffer_size, unsigned int timeout)
```

**声明头文件**

```c
#include "msgqueue/osal_msgqueue.h"
```

**功能说明**

- 从指定消息队列读取数据。
- 读取的数据存储于 buffer_addr 指向的地址，实际读取大小通过 buffer_size 返回。
- 采用 FIFO（First In First Out）方式读取，支持超时等待。

**前置条件**

- 调用时序约束：当前接口需在 LiteOS 初始化后调用，且目标队列已通过 osal_msg_queue_create 创建。
- 上下文限制：除 FreeRTOS 外，禁止在中断上下文及软件定时器回调中调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| queue_id | unsigned long | 由 osal_msg_queue_create 创建的队列 ID | 由 osal_msg_queue_create 创建 |
| buffer_size | unsigned int * | 读取前为期望读取的缓冲区大小 | 大于 0 |
| timeout | unsigned int | 超时时间（单位：Tick） | [OSAL_MSGQ_NO_WAIT](#OSAL_MSGQ_NO_WAIT)：0 ~ [OSAL_MSGQ_WAIT_FOREVER](#OSAL_MSGQ_WAIT_FOREVER)(0xFFFFFFFF) |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| buffer_addr | void * | 读取到的数据存储缓冲区，由调用方分配内存、函数填充 |
| buffer_size | unsigned int * | 读取后为实际读取的数据大小 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 执行成功 | 数据读取成功 |
| 非 0 | 执行失败 | 数据读取失败 |

**参考案例**

- `src/application/ws53/ws53_application/main.c`
- `src/middleware/chips/ws53/dfx/dfx_system_init.c`
- `src/middleware/services/wifi_service/wpa/liteos_wpa_api/wifi_api.c`
- `src/middleware/utils/nv/nv_storage_lib/nv_async_store.c`
- `src/test/common/testsuite/src/test_suite_task.c`

### osal_msg_queue_write_head_copy <a id="osal_msg_queue_write_head_copy"></a>

```c
int osal_msg_queue_write_head_copy(unsigned long queue_id, void *buffer_addr, unsigned int buffer_size, unsigned int timeout)
```

**声明头文件**

```c
#include "msgqueue/osal_msgqueue.h"
```

**功能说明**

- 向指定消息队列头部写入数据。
- 写入数据的大小由 buffer_size 指定，数据存储于 buffer_addr 指向的地址。
- 支持超时等待，当队列满时按 timeout 阻塞等待。

**前置条件**

- 调用时序约束：当前接口需在 LiteOS 初始化后调用，且目标队列已通过 osal_msg_queue_create 创建。
- 上下文限制：除 FreeRTOS 外，禁止在中断上下文及软件定时器回调中调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| queue_id | unsigned long | 由 osal_msg_queue_create 创建的队列 ID | 由 osal_msg_queue_create 创建 |
| buffer_addr | void * | 存储待写入数据的缓冲区起始地址 | 不为 NULL |
| buffer_size | unsigned int | 待写入数据的缓冲区大小 | 1 ~ 0xFFFFFFFF |
| timeout | unsigned int | 超时时间（单位：Tick） | [OSAL_MSGQ_NO_WAIT](#OSAL_MSGQ_NO_WAIT)：0 ~ [OSAL_MSGQ_WAIT_FOREVER](#OSAL_MSGQ_WAIT_FOREVER)(0xFFFFFFFF) |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 执行成功 | 数据写入成功 |
| 非 0 | 执行失败 | 数据写入失败 |

### osal_msg_queue_delete <a id="osal_msg_queue_delete"></a>

```c
void osal_msg_queue_delete(unsigned long queue_id)
```

**声明头文件**

```c
#include "msgqueue/osal_msgqueue.h"
```

**功能说明**

- 删除指定的消息队列。
- 删除后该队列不可再用于读写操作。
- 无法删除未创建的队列。

**前置条件**

- 调用时序约束：仅可删除已通过 osal_msg_queue_create 创建的队列。
- 依赖关系：若有任务阻塞在队列上或队列正在被读写，删除操作将失败。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| queue_id | unsigned long | 由 osal_msg_queue_create 创建的队列 ID | 由 osal_msg_queue_create 创建 |

**参考案例**

- `src/test/common/testsuite/src/test_suite_task.c`

### osal_msg_queue_is_full <a id="osal_msg_queue_is_full"></a>

```c
int osal_msg_queue_is_full(unsigned long queue_id)
```

**声明头文件**

```c
#include "msgqueue/osal_msgqueue.h"
```

**功能说明**

- 检查指定消息队列是否已满。
- 返回 true 表示队列已满，false 表示未满。
- 可用于写入前判断队列剩余空间。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| queue_id | unsigned long | 由 osal_msg_queue_create 创建的队列 ID | 由 osal_msg_queue_create 创建 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 1 | 队列已满 | 队列已满或获取队列信息失败 |
| 0 | 队列未满 | 队列未满 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SEC_CORE | 特性宏 | 支持安全内核特性（分支级，Kconfig 未声明） | - |

### osal_msg_queue_get_msg_num <a id="osal_msg_queue_get_msg_num"></a>

```c
unsigned int osal_msg_queue_get_msg_num(unsigned long queue_id)
```

**声明头文件**

```c
#include "msgqueue/osal_msgqueue.h"
```

**功能说明**

- 获取指定消息队列中当前的消息数量。
- 返回当前队列中的消息数。
- 获取失败时返回 OSAL_INVALID_MSG_NUM。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| queue_id | unsigned long | 由 osal_msg_queue_create 创建的队列 ID | 由 osal_msg_queue_create 创建 |

**返回值**

- 返回类型：unsigned int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| >= 0 | 当前消息队列中的消息数量 | 获取成功 |
| OSAL_INVALID_MSG_NUM：0xFFFFFFFF | 获取消息数量失败 | 获取队列信息失败 |

**参考案例**

- `src/middleware/utils/nv/nv_storage_lib/nv_async_store.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SEC_CORE | 特性宏 | 支持安全内核特性（分支级，Kconfig 未声明） | - |

## Macros

### OSAL_INVALID_MSG_NUM <a id="OSAL_INVALID_MSG_NUM"></a>

```c
#define OSAL_INVALID_MSG_NUM 0xFFFFFFFF
```

### OSAL_MSGQ_WAIT_FOREVER <a id="OSAL_MSGQ_WAIT_FOREVER"></a>

```c
#ifdef LOS_WAIT_FOREVER
#define OSAL_MSGQ_WAIT_FOREVER LOS_WAIT_FOREVER
#else
#define OSAL_MSGQ_WAIT_FOREVER 0xFFFFFFFF
#endif
```

### OSAL_MSGQ_NO_WAIT <a id="OSAL_MSGQ_NO_WAIT"></a>

```c
#ifdef LOS_NO_WAIT
#define OSAL_MSGQ_NO_WAIT LOS_NO_WAIT
#else
#define OSAL_MSGQ_NO_WAIT 0
#endif
```