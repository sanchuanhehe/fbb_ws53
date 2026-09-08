# Debug

Debug 模块提供 OSAL（OS Abstract Layer）内核调试与诊断功能，包括格式化日志打印、内核 panic 触发、调用栈回溯打印与 CPU（Central Processing Unit） D-Cache（Data Cache）刷新能力，用于系统运行时调试与异常诊断。该模块面向 linux、liteos、seliteos、freertos、nonos 等多种操作系统环境提供统一的调试接口抽象。

**模块公共头文件**

```c
#include "debug/osal_debug.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_printk](#osal_printk) | 格式化日志打印，支持可变参数 |
| [osal_panic](#osal_panic) | 触发内核 panic 并打印栈信息 |
| [osal_dump_stack](#osal_dump_stack) | 打印当前任务调用栈回溯信息 |
| [osal_flush_cache](#osal_flush_cache) | 刷新 CPU D-Cache |

## Functions

### osal_printk <a id="osal_printk"></a>

```c
void osal_printk(const char *fmt, ...)
```

**声明头文件**

```c
#include "debug/osal_debug.h"
```

**功能说明**

- 提供内核日志打印功能，支持可变参数格式化输出。
- 支持 linux、liteos、seliteos、freertos 系统。
- 当 fmt 为 NULL 时，函数直接返回，不执行打印操作。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| fmt | const char * | 格式化字符串指针 | 非 NULL，指向有效的格式化字符串 |
| ... | ... | 可变参数列表 | 与 fmt 中的格式说明符匹配 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`
- `src/application/samples/peripheral/uart/uart_demo.c`

### osal_panic <a id="osal_panic"></a>

```c
void osal_panic(const char *fmt, const char *fun, int line, const char *cond)
```

**声明头文件**

```c
#include "debug/osal_debug.h"
```

**功能说明**

- 内核 panic 函数，打印内核 panic 信息及调用栈后系统停止响应。
- 支持 linux、liteos 系统。
- 调用后系统将无法继续运行，属于致命错误处理接口。

**前置条件**

- 仅在 linux、liteos 系统下可用。
- 仅在发生不可恢复的致命错误时调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| fmt | const char * | 格式化字符串指针 | 非 NULL |
| fun | const char * | 发生 panic 的函数名 | 非 NULL |
| line | int | 发生 panic 的行号 | 有效源码行号 |
| cond | const char * | 触发 panic 的条件表达式 | 非 NULL |

### osal_dump_stack <a id="osal_dump_stack"></a>

```c
void osal_dump_stack(void)
```

**声明头文件**

```c
#include "debug/osal_debug.h"
```

**功能说明**

- 内核回溯函数，打印当前运行任务的调用栈信息。
- 支持 linux、liteos 系统。
- 用于调试定位问题时的调用链追踪。

**前置条件**

- 仅在 linux、liteos 系统下可用。

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| OSAL_DEBUG_DUMP | 特性宏 | linux 实现中控制 dump_stack 调用分支（分支级，无前缀注入宏） | 由构建目标决定 |

### osal_flush_cache <a id="osal_flush_cache"></a>

```c
void osal_flush_cache(void)
```

**声明头文件**

```c
#include "debug/osal_debug.h"
```

**功能说明**

- 刷新 CPU DCache，将数据缓存写回内存。
- 支持 liteos 系统。
- 在 DMA（Direct Memory Access）传输等需要 Cache 一致性操作的场景下调用。

**前置条件**

- 仅在 liteos 系统下可用。
