# Event

Event 提供事件标志组的创建、写入、读取、清除与销毁功能，支持任务间基于事件标志的同步机制。

**模块公共头文件**

```c
#include "event/osal_event.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_event_init](#osal_event_init) | 初始化事件控制块 |
| [osal_event_write](#osal_event_write) | 向事件控制块写入指定事件 |
| [osal_event_read](#osal_event_read) | 读取事件控制块中指定事件 |
| [osal_event_clear](#osal_event_clear) | 清除事件控制块中指定事件 |
| [osal_event_destroy](#osal_event_destroy) | 销毁事件控制块 |

## Functions

### osal_event_init <a id="osal_event_init"></a>

```c
int osal_event_init(osal_event *event_obj)
```

**声明头文件**

```c
#include "event/osal_event.h"
```

**功能说明**

- 初始化事件控制块，为事件控制块分配内存资源。
- 初始化底层事件对象，使其处于可操作状态。
- 初始化成功后可进行事件的写入、读取与清除操作。

**前置条件**

- 调用时序约束：event_obj 指向的内存必须已分配且 event_obj->event 为 NULL。
- 上下文限制：禁止在中断上下文中调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| event_obj | [osal_event](#osal_event) * | 指向待初始化的事件控制块 | 不为 NULL，且 event 成员为 NULL |

**返回值**

返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)：0 | 执行成功 | 事件控制块初始化成功 |
| [OSAL_FAILURE](#OSAL_FAILURE)：-1 | 执行失败 | event_obj 为 NULL、event 成员非 NULL 或内存分配失败 |
| Other | 其他错误码 | 底层 LiteOS 接口失败时透传的错误码 |

**参考案例**

- `src/middleware/services/wifi_service/wpa/osdep/osdep_osal.c`

### osal_event_write <a id="osal_event_write"></a>

```c
int osal_event_write(osal_event *event_obj, unsigned int mask)
```

**声明头文件**

```c
#include "event/osal_event.h"
```

**功能说明**

- 向事件控制块写入指定事件掩码。
- 写入后等待该事件的任务将被唤醒。
- 支持 bit[0:30] 的事件位写入。

**前置条件**

- 调用时序约束：当前接口必须在 [osal_event_init](#osal_event_init) 成功返回后调用。
- 上下文限制：禁止在中断上下文中调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| event_obj | [osal_event](#osal_event) * | 指向目标事件控制块 | 不为 NULL |
| mask | unsigned int | 待写入的事件掩码 | bit[0:30]，禁止使用 bit[31] |

**返回值**

返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)：0 | 执行成功 | 事件写入成功 |
| [OSAL_FAILURE](#OSAL_FAILURE)：-1 | 执行失败 | event_obj 为 NULL 或 mask 使用了 bit[31] |
| Other | 其他错误码 | 底层 LiteOS 接口失败时透传的错误码 |

**参考案例**

- `src/middleware/services/wifi_service/wpa/osdep/osdep_osal.c`

### osal_event_read <a id="osal_event_read"></a>

```c
int osal_event_read(osal_event *event_obj, unsigned int mask, unsigned int timeout_ms, unsigned int mode)
```

**声明头文件**

```c
#include "event/osal_event.h"
```

**功能说明**

- 读取事件控制块中指定掩码的事件，支持阻塞等待。
- 支持按 AND 模式（等待所有期望事件发生）或 OR 模式（等待任一期望事件发生）读取事件。
- 支持读取后立即清除已读取的事件标志。

**前置条件**

- 调用时序约束：当前接口必须在 [osal_event_init](#osal_event_init) 成功返回后调用。
- 上下文限制：禁止在中断上下文中调用；不推荐在软件定时器回调中调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| event_obj | [osal_event](#osal_event) * | 指向目标事件控制块 | 不为 NULL |
| mask | unsigned int | 期望读取的事件掩码 | bit[0:30]，禁止使用 bit[31]；liteos 上禁止使用 bit[25] |
| timeout_ms | unsigned int | 读取超时时间，单位 ms；[OSAL_EVENT_FOREVER](#OSAL_EVENT_FOREVER)：0xFFFFFFFF 表示永久等待 | 0 ~ 0xFFFFFFFF |
| mode | unsigned int | 事件读取模式，可组合使用 | [OSAL_WAITMODE_AND](#OSAL_WAITMODE_AND)：4U；<br>[OSAL_WAITMODE_OR](#OSAL_WAITMODE_OR)：2U；<br>[OSAL_WAITMODE_CLR](#OSAL_WAITMODE_CLR)：1U。 |

**返回值**

返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非零位掩码 | 成功读取到的事件位 | 等待条件满足，返回实际读取到的事件位 |
| 0 | 未读取到事件 | 超时或事件已被消费 |
| [OSAL_FAILURE](#OSAL_FAILURE)：-1 | 参数无效 | event_obj 为 NULL |
| Other | 其他错误码 | 底层 LiteOS 接口失败时透传的错误码（含 LOS_ERRTYPE_ERROR 标志） |

**参考案例**

- `src/middleware/services/wifi_service/wpa/osdep/osdep_osal.c`

### osal_event_clear <a id="osal_event_clear"></a>

```c
int osal_event_clear(osal_event *event_obj, unsigned int mask)
```

**声明头文件**

```c
#include "event/osal_event.h"
```

**功能说明**

- 清除事件控制块中指定掩码的事件标志位。
- 清除后对应事件位被置为 0。
- 未在掩码中指定的事件位不受影响。

**前置条件**

- 调用时序约束：当前接口必须在 [osal_event_init](#osal_event_init) 成功返回后调用。
- 上下文限制：禁止在中断上下文中调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| event_obj | [osal_event](#osal_event) * | 指向目标事件控制块 | 不为 NULL |
| mask | unsigned int | 待清除的事件掩码 | 0 ~ 0xFFFFFFFF |

**返回值**

返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)：0 | 执行成功 | 事件清除成功 |
| [OSAL_FAILURE](#OSAL_FAILURE)：-1 | 执行失败 | event_obj 为 NULL |
| Other | 其他错误码 | 底层 LiteOS 接口失败时透传的错误码 |

**参考案例**

- `src/middleware/services/wifi_service/wpa/osdep/osdep_osal.c`

### osal_event_destroy <a id="osal_event_destroy"></a>

```c
int osal_event_destroy(osal_event *event_obj)
```

**声明头文件**

```c
#include "event/osal_event.h"
```

**功能说明**

- 销毁事件控制块，释放其占用的内存资源。
- 销毁后将 event 成员置为 NULL。
- 销毁后该事件控制块不可再被使用。

**前置条件**

- 调用时序约束：当前接口必须在 [osal_event_init](#osal_event_init) 成功返回后调用，且 event_obj 应由 osal_event_init 初始化。
- 上下文限制：禁止在中断上下文中调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| event_obj | [osal_event](#osal_event) * | 指向待销毁的事件控制块 | 不为 NULL |

**返回值**

返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_SUCCESS](#OSAL_SUCCESS)：0 | 执行成功 | 事件控制块销毁成功 |
| [OSAL_FAILURE](#OSAL_FAILURE)：-1 | 执行失败 | event_obj 为 NULL |
| Other | 其他错误码 | 底层 LiteOS 接口失败时透传的错误码 |

**参考案例**

- `src/middleware/services/wifi_service/wpa/osdep/osdep_osal.c`

## Structures

### osal_event <a id="osal_event"></a>

```c
typedef struct {
    void *event;
} osal_event;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| event | void * | 事件控制块指针，指向底层事件对象 |

## Macros

### OSAL_EVENT_FOREVER <a id="OSAL_EVENT_FOREVER"></a>

```c
#define OSAL_EVENT_FOREVER 0xFFFFFFFF
```

### OSAL_WAITMODE_AND <a id="OSAL_WAITMODE_AND"></a>

```c
#define OSAL_WAITMODE_AND 4U
```

### OSAL_WAITMODE_OR <a id="OSAL_WAITMODE_OR"></a>

```c
#define OSAL_WAITMODE_OR 2U
```

### OSAL_WAITMODE_CLR <a id="OSAL_WAITMODE_CLR"></a>

```c
#define OSAL_WAITMODE_CLR 1U
```

### OSAL_SUCCESS <a id="OSAL_SUCCESS"></a>

```c
#define OSAL_SUCCESS 0
```

### OSAL_FAILURE <a id="OSAL_FAILURE"></a>

```c
#define OSAL_FAILURE (-1)
```
