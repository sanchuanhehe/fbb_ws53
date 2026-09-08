# AT

AT（Attention）提供 Hayes AT 命令集解析与处理服务，支持注册自定义 AT 命令表、命令执行/设置/读取/测试/查询回调、异步命令结果上报、命令交互处理以及向默认或指定通道输出 AT 响应信息与 URC（Unsolicited Result Code）主动上报。

**模块公共头文件**

```c
#include "include/middleware/utils/at.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_at_cmd_table_register](#uapi_at_cmd_table_register) | 注册 AT 命令表，将一组 AT 命令实体加入命令链表 |
| [uapi_at_cmd_abort_register](#uapi_at_cmd_abort_register) | 注册当前 AT 命令的打断处理函数及其入参 |
| [uapi_at_send_async_result](#uapi_at_send_async_result) | 发送异步阻塞式 AT 命令的执行结果 |
| [uapi_at_interactivity_func_register](#uapi_at_interactivity_func_register) | 注册 AT 交互命令处理函数 |
| [uapi_at_report](#uapi_at_report) | 向当前命令所在默认通道输出 AT 打印信息 |
| [uapi_at_print](#uapi_at_print) | 向默认通道输出格式化 AT 打印信息 |
| [uapi_at_report_to_single_channel](#uapi_at_report_to_single_channel) | 向指定通道输出 AT 打印信息 |
| [uapi_at_urc_to_channel](#uapi_at_urc_to_channel) | 向指定通道发送 URC 主动上报消息 |

## Functions

### uapi_at_cmd_table_register <a id="uapi_at_cmd_table_register"></a>

```c
errcode_t uapi_at_cmd_table_register(const at_cmd_entry_t *table, uint32_t len,
                                     uint32_t struct_max_size)
```

**声明头文件**

```c
#include "include/middleware/utils/at.h"
```

**功能说明**

- 将由调用方构造的 AT 命令实体表注册到 AT 框架的命令链表中，使表中的 AT 命令可被框架识别与分发。
- 注册过程中记录命令设置函数入参结构体的最大尺寸，供 AT 命令参数解析时统一分配缓冲使用。
- 当开启 CONFIG_AT_SUPPORT_CMD_TABLE_CHECK 配置时，对命令名、命令回调和参数校验语法进行合法性检查，并在命令名重复时返回错误。

**前置条件**

- 调用时序约束：当前接口必须在 AT 基础接口 uapi_at_base_api_register 成功初始化（提供内存与消息队列等回调）之后调用，否则注册的命令表无法被命令处理流程解析。
- 依赖关系：当前接口依赖 table 指向的命令实体表在调用后仍保持有效，框架仅保存表首地址，不进行内容拷贝。
- 上下文限制：当前接口需在任务上下文调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| table | [at_cmd_entry_t](#at_cmd_entry_t) * | AT 命令实体表起始地址，表中每个元素描述一条 AT 命令的名称、命令 ID、属性、参数校验语法及各类型回调 | 不为 NULL，表内各命令 name 成员不为 NULL |
| len | uint32_t | AT 命令实体表中命令条目的数量 | 大于 0 |
| struct_max_size | uint32_t | 命令设置函数入参结构体的最大尺寸，框架会保留历史最大值 | 大于 0 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 命令表注册成功 |
| ERRCODE_INVALID_PARAM：0x80000001 | 参数无效 | table 为 NULL 或 len 为 0 |
| ERRCODE_MALLOC：0x80000005 | 内存分配失败 | 分配命令链表节点失败 |
| ERRCODE_AT_CMD_REPEAT：0x80003022 | 命令名重复 | 已注册存在同名命令（仅在开启 CONFIG_AT_SUPPORT_CMD_TABLE_CHECK 时检查） |
| ERRCODE_AT_CMD_TABLE_PARA_ERROR：0x80003023 | 命令表参数错误 | 命令名超长或包含非大写字母字符、命令回调全部为空、set 回调存在但 syntax 为空、参数校验语法冲突（仅在开启 CONFIG_AT_SUPPORT_CMD_TABLE_CHECK 时检查） |

**参考案例**

- `src/middleware/utils/at/at_wifi_cmd/src/at_cmd_register.c`
- `src/middleware/utils/at/at_plt_cmd/src/at_plt_cmd_register.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_AT_SUPPORT_CMD_TABLE_CHECK | 特性宏 | 启用注册时命令表合法性检查分支（分支级；Kconfig 未声明，需构建系统注入） | - |

### uapi_at_cmd_abort_register <a id="uapi_at_cmd_abort_register"></a>

```c
errcode_t uapi_at_cmd_abort_register(at_abort_func_t func, void *arg)
```

**声明头文件**

```c
#include "include/middleware/utils/at.h"
```

**功能说明**

- 注册当前 AT 命令执行过程中使用的打断处理函数及其入参，用于在框架判定需要打断当前命令时回调该函数。
- 注册的函数与入参会覆盖此前注册的当前命令打断函数，框架在执行打断流程时优先调用本接口注册的函数。
- 接口可用性由构建配置控制（见 Kconfig配置）。

**前置条件**

- 调用时序约束：当前接口必须在 AT 基础接口 uapi_at_base_api_register 成功初始化之后调用，且需在开启 CONFIG_AT_SUPPORT_ASYNCHRONOUS 特性的构建配置下编译。
- 依赖关系：当前接口依赖异步特性已使能，并依赖调用方保证 func 与 arg 在打断发生时仍有效。
- 上下文限制：当前接口需在任务上下文调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func | [at_abort_func_t](#at_abort_func_t) | AT 命令打断处理函数指针，框架在打断当前命令时回调，回调返回 at_ret_t 表示打断结果 | 不为 NULL |
| arg | void * | 将打断处理函数的入参直接透传给回调函数 | 调用方自定义 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 打断处理函数注册成功 |
| ERRCODE_INVALID_PARAM：0x80000001 | 参数无效 | func 为 NULL |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_AT_SUPPORT_ASYNCHRONOUS | 特性宏 | 支持异步打断、异步结果上报与交互命令功能（接口级） | n |

### uapi_at_send_async_result <a id="uapi_at_send_async_result"></a>

```c
errcode_t uapi_at_send_async_result(uint16_t err)
```

**声明头文件**

```c
#include "include/middleware/utils/at.h"
```

**功能说明**

- 向 AT 框架发送异步阻塞式 AT 命令的执行结果，由框架在消息处理后输出对应响应。
- 输入 0 表示执行成功，其他值表示失败，框架据此决定后续响应流程。
- 接口可用性由构建配置控制（见 Kconfig配置）。

**前置条件**

- 调用时序约束：当前接口必须在一个异步阻塞式 AT 命令执行过程中调用，且需在开启 CONFIG_AT_SUPPORT_ASYNCHRONOUS 特性的构建配置下编译。
- 依赖关系：当前接口依赖 AT 消息队列已创建并运行，框架通过消息机制异步处理该结果。
- 上下文限制：当前接口可在命令回调上下文调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| err | uint16_t | AT 命令执行结果，0 表示成功，其他值表示失败 | 0 ~ 65535 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 结果消息写入消息队列成功 |
| ERRCODE_AT_MSG_SEND_ERROR：0x80003024 | 消息发送失败 | 结果消息写入消息队列失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_AT_SUPPORT_ASYNCHRONOUS | 特性宏 | 支持异步打断、异步结果上报与交互命令功能（接口级） | n |

### uapi_at_interactivity_func_register <a id="uapi_at_interactivity_func_register"></a>

```c
errcode_t uapi_at_interactivity_func_register(at_interactivity_func_t func)
```

**声明头文件**

```c
#include "include/middleware/utils/at.h"
```

**功能说明**

- 注册 AT 交互命令处理函数，用于在框架进入交互等待状态时回调该函数处理后续交互数据。
- 注册的函数会覆盖此前注册的交互处理函数，框架在交互流程中通过该回调向调用方传递交互数据。
- 接口可用性由构建配置控制（见 Kconfig配置）。

**前置条件**

- 调用时序约束：当前接口必须在 AT 基础接口 uapi_at_base_api_register 成功初始化之后调用，且需在开启 CONFIG_AT_SUPPORT_ASYNCHRONOUS 特性的构建配置下编译。
- 依赖关系：当前接口依赖异步特性已使能，并依赖调用方保证 func 在交互发生时仍有效。
- 上下文限制：当前接口需在任务上下文调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func | [at_interactivity_func_t](#at_interactivity_func_t) | AT 交互命令处理函数指针，框架在交互过程中回调，回调入参为字符串数据及其长度，回调返回 at_ret_t 表示处理结果 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 交互处理函数注册成功 |
| ERRCODE_INVALID_PARAM：0x80000001 | 参数无效 | func 为 NULL |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_AT_SUPPORT_ASYNCHRONOUS | 特性宏 | 支持异步打断、异步结果上报与交互命令功能（接口级） | n |

### uapi_at_report <a id="uapi_at_report"></a>

```c
void uapi_at_report(const char *str)
```

**声明头文件**

```c
#include "include/middleware/utils/at.h"
```

**功能说明**

- 向当前命令所在的默认通道输出 AT 打印信息，str 必须以字符串结束符结尾。
- 取当前命令处理上下文对应的通道写回调将字符串发送至对端。
- 同时将该打印信息记录到 AT 日志通道。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| str | const char * | AT 打印信息字符串，需携带字符串结束符 | 不为 NULL |

**参考案例**

- `src/middleware/utils/at/at_plt_cmd/at/at_plt.c`
- `src/middleware/utils/at/at_wifi_cmd/at/at_ccpriv.c`
- `src/middleware/utils/at/at_wifi_cmd/at/at_mfg.c`
- `src/middleware/utils/at/at_wifi_cmd/at/at_wifi.c`

### uapi_at_print <a id="uapi_at_print"></a>

```c
void uapi_at_print(const char* str, ...)
```

**声明头文件**

```c
#include "include/middleware/utils/at.h"
```

**功能说明**

- 向默认通道输出格式化 AT 打印信息，按 printf 风格的格式串与可变参数生成最终字符串。
- 格式化缓冲区大小由 CONFIG_AT_PRINT_BUFFER_SIZE 配置决定，未配置时使用默认值。
- 格式化失败或参数非法时不输出内容，并在结束时释放缓冲区。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| str | const char * | 格式化打印信息字符串，需携带字符串结束符 | 不为 NULL |
| ... | 可变参数 | 与 str 中格式说明符一一对应的可变参数 | 与格式串匹配 |

**参考案例**

- `drivers/chips/ws53/porting/uart/uart_porting.c`
- `drivers/chips/ws53/porting/version/version_porting.c`
- `src/middleware/utils/at/at_plt_cmd/at/at_plt.c`

### uapi_at_report_to_single_channel <a id="uapi_at_report_to_single_channel"></a>

```c
void uapi_at_report_to_single_channel(at_channel_id_t channel_id, const char *str)
```

**声明头文件**

```c
#include "include/middleware/utils/at.h"
```

**功能说明**

- 向指定通道输出 AT 打印信息，str 必须以字符串结束符结尾。
- 取该通道注册的写回调将字符串发送至对端。
- 同时将该打印信息记录到 AT 日志通道。

**前置条件**

- 调用时序约束：当前接口必须在对应该 channel_id 的通道写回调已注册之后调用，否则不会输出内容。
- 依赖关系：当前接口依赖 at_config.h 中定义的 at_channel_id_t 通道号取值有效，且对应通道已使能。
- 上下文限制：当前接口需在任务上下文调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel_id | at_channel_id_t | AT 通道号，取值由 at_config.h 中 at_channel_id_t 枚举定义 | AT_UART_PORT(0)；<br>AT_ZDIAG_PORT(1)（仅开启 CONFIG_AT_SUPPORT_ZDIAG 时存在）；<br>AT_MAX_PORT_NUMBER 之前的合法值。 |
| str | const char * | AT 打印信息字符串，需携带字符串结束符 | 不为 NULL |

**参考案例**

- `src/middleware/utils/at/at_plt_cmd/src/at_plt_cmd_register.c`
- `src/middleware/utils/at/at_wifi_cmd/src/at_cmd_register.c`

### uapi_at_urc_to_channel <a id="uapi_at_urc_to_channel"></a>

```c
errcode_t uapi_at_urc_to_channel(at_channel_id_t channel_id, const char *msg, uint32_t msg_len)
```

**声明头文件**

```c
#include "include/middleware/utils/at.h"
```

**功能说明**

- 向指定通道发送 URC 主动上报消息，消息内容与长度由调用方提供。
- 将上报消息加入内部上报队列，并通过消息机制触发框架在处理流程中实际向通道输出。
- 仅当框架支持主动上报特性时此接口对外可用。

**前置条件**

- 调用时序约束：当前接口必须在 AT 基础接口 uapi_at_base_api_register 成功初始化并已通过消息任务完成主动上报互斥锁初始化之后调用，且需在开启 CONFIG_AT_SUPPORT_NOTIFY_REPORT 特性的构建配置下编译。
- 依赖关系：当前接口依赖 at_config.h 中定义的 at_channel_id_t 通道号取值有效，并依赖内存分配与消息队列机制可用。
- 上下文限制：当前接口需在任务上下文调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel_id | at_channel_id_t | AT 通道号，取值由 at_config.h 中 at_channel_id_t 枚举定义 | AT_UART_PORT(0)；<br>AT_ZDIAG_PORT(1)（仅开启 CONFIG_AT_SUPPORT_ZDIAG 时存在）；<br>AT_MAX_PORT_NUMBER 之前的合法值。 |
| msg | const char * | 主动上报消息内容起始地址 | 不为 NULL |
| msg_len | uint32_t | 主动上报消息长度，单位 Bytes | 大于 0 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 上报消息成功加入队列并触发消息发送 |
| ERRCODE_INVALID_PARAM：0x80000001 | 参数无效 | msg 为 NULL 或 msg_len 为 0 |
| ERRCODE_MALLOC：0x80000005 | 内存分配失败 | 分配上报节点或消息字符串缓冲区失败 |
| ERRCODE_AT_MSG_SEND_ERROR：0x80003024 | 消息发送失败 | 消息队列写入失败 |
| ERRCODE_MEMCPY：0x80000004 | 内存拷贝失败 | 拷贝消息内容到缓冲区失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_AT_SUPPORT_NOTIFY_REPORT | 特性宏 | 支持 URC 主动上报功能（接口级） | n |

## Type definitions

### at_ret_t <a id="at_ret_t"></a>

```c
// 源码原始定义
typedef enum {
    AT_RET_OK = 0,
    AT_RET_SYNTAX_ERROR,
    AT_RET_MALLOC_ERROR,
    AT_RET_MEM_API_ERROR,
    AT_RET_CHANNEL_PARA_ERROR,
    AT_RET_CHANNEL_NOT_INIT,
    AT_RET_CHANNEL_DATA_NULL,
    AT_RET_CMD_PARA_ERROR,
    AT_RET_CMD_FORMAT_ERROR,
    AT_RET_CMD_NO_MATCH,
    AT_RET_CMD_TYPE_ERROR,
    AT_RET_CMD_IN_PROGRESS_BLOCK,
    AT_RET_CMD_ATTR_NOT_ALLOW,
    AT_RET_PROC_CMD_FUNC_MISSING,
    AT_RET_PROC_READ_FUNC_MISSING,
    AT_RET_PROC_TEST_FUNC_MISSING,
    AT_RET_PROC_SET_FUNC_MISSING,
    AT_RET_PROC_WAIT_INTERACTIVITY,
    AT_RET_PROC_ABORT_CURRENT_COMMAND,
    AT_RET_PARSE_PARA_ERROR,
    AT_RET_PARSE_PARA_MISSING_ERROR,
    AT_RET_PROGRESS_BLOCK,
    AT_RET_TIMER_ERROR,
    AT_RET_ABORT_DELAY
} at_ret_t;
```

**使用说明**

本模块对外接口所注册的命令回调函数（at_cmd_func_t、at_set_func_t、at_read_func_t、at_test_func_t、at_query_func_t、at_abort_func_t、at_interactivity_func_t）的返回值类型，用于向 AT 框架反馈命令执行与处理结果。

回调说明：调用时机由 AT 框架在命令分发、参数解析、打断处理或交互处理流程中回调；参数语义由各回调类型签名决定；返回值会被框架在命令处理流程中读取以决定后续响应与状态切换。

### at_abort_func_t <a id="at_abort_func_t"></a>

```c
// 源码原始定义
typedef at_ret_t(*at_abort_func_t)(void *arg);
```

**使用说明**

AT 命令打断处理函数指针类型，作为入参出现于 uapi_at_cmd_abort_register 接口签名中。

回调说明：调用时机为 AT 框架在判定需要打断当前正在执行的命令时回调；参数 arg 为注册打断函数时透传的入参，由调用方自定义语义；返回的 at_ret_t 由框架读取以判断打断是否成功，打断成功时框架会重置命令执行状态。

### at_interactivity_func_t <a id="at_interactivity_func_t"></a>

```c
// 源码原始定义
typedef at_ret_t(*at_interactivity_func_t)(const char *data, uint32_t len);
```

**使用说明**

AT 命令交互处理函数指针类型，作为入参出现于 uapi_at_interactivity_func_register 接口签名中。

回调说明：调用时机为 AT 框架进入交互等待状态并接收到交互数据时回调；参数 data 为交互数据字符串起始地址，len 为数据长度；返回的 at_ret_t 由框架读取以决定交互结果处理。

### at_cmd_func_t <a id="at_cmd_func_t"></a>

```c
// 源码原始定义
typedef at_ret_t(*at_cmd_func_t)(void);
```

**使用说明**

AT 命令执行函数指针类型（对应 "AT+TEST" 形式），作为 at_cmd_entry_t 结构体的 cmd 成员类型被 uapi_at_cmd_table_register 间接使用。

### at_set_func_t <a id="at_set_func_t"></a>

```c
// 源码原始定义
typedef at_ret_t(*at_set_func_t)(const void *arg);
```

**使用说明**

AT 命令设置函数指针类型（对应 "AT+TEST=520" 形式），作为 at_cmd_entry_t 结构体的 set 成员类型被 uapi_at_cmd_table_register 间接使用。回调入参 arg 为框架按命令参数校验语法解析填充的参数结构体指针。

### at_read_func_t <a id="at_read_func_t"></a>

```c
// 源码原始定义
typedef at_ret_t(*at_read_func_t)(void);
```

**使用说明**

AT 命令读取函数指针类型（对应 "AT+TEST?" 形式），作为 at_cmd_entry_t 结构体的 read 成员类型被 uapi_at_cmd_table_register 间接使用。

### at_test_func_t <a id="at_test_func_t"></a>

```c
// 源码原始定义
typedef at_ret_t(*at_test_func_t)(void);
```

**使用说明**

AT 命令测试函数指针类型（对应 "AT+TEST=?" 形式），作为 at_cmd_entry_t 结构体的 test 成员类型被 uapi_at_cmd_table_register 间接使用。

### at_query_func_t <a id="at_query_func_t"></a>

```c
// 源码原始定义
typedef at_ret_t(*at_query_func_t)(const void *arg);
```

**使用说明**

AT 命令查询函数指针类型（对应 "AT+TEST?=" 形式），仅当开启 CONFIG_AT_SUPPORT_QUERY 特性时存在，作为 at_cmd_entry_t 结构体的 query 成员类型被 uapi_at_cmd_table_register 间接使用。回调入参 arg 为框架按命令参数校验语法解析填充的参数结构体指针。

### at_token_int_range_t <a id="at_token_int_range_t"></a>

```c
// 源码原始定义
typedef struct {
    int32_t min_val;
    int32_t max_val;
} at_token_int_range_t;
```

**使用说明**

基于取值范围的整型参数校验语法结构，作为 at_para_parse_syntax_t 内部联合体的成员类型被 uapi_at_cmd_table_register 间接使用。

### at_token_int_list_t <a id="at_token_int_list_t"></a>

```c
// 源码原始定义
typedef struct {
    uint32_t num;
    const int32_t *values;
} at_token_int_list_t;
```

**使用说明**

基于白名单的整型参数校验语法结构，作为 at_para_parse_syntax_t 内部联合体的成员类型被 uapi_at_cmd_table_register 间接使用。

### at_token_string_t <a id="at_token_string_t"></a>

```c
// 源码原始定义
typedef struct {
    uint32_t max_length;
} at_token_string_t;
```

**使用说明**

基于长度的字符串参数校验语法结构，作为 at_para_parse_syntax_t 内部联合体的成员类型被 uapi_at_cmd_table_register 间接使用。

### at_token_string_values_t <a id="at_token_string_values_t"></a>

```c
// 源码原始定义
typedef struct {
    uint32_t num;
    const uint8_t * const *values;
} at_token_string_values_t;
```

**使用说明**

基于白名单的字符串参数校验语法结构，作为 at_para_parse_syntax_t 内部联合体的成员类型被 uapi_at_cmd_table_register 间接使用。

### at_token_bit_string_range_t <a id="at_token_bit_string_range_t"></a>

```c
// 源码原始定义
typedef struct {
    uint32_t max_value;
} at_token_bit_string_range_t;
```

**使用说明**

基于范围值的二进制字符串参数校验语法结构，作为 at_para_parse_syntax_t 内部联合体的成员类型被 uapi_at_cmd_table_register 间接使用。

### at_token_bit_string_list_t <a id="at_token_bit_string_list_t"></a>

```c
// 源码原始定义
typedef struct {
    uint32_t num;
    const uint32_t *values;
} at_token_bit_string_list_t;
```

**使用说明**

基于白名单的二进制字符串参数校验语法结构，作为 at_para_parse_syntax_t 内部联合体的成员类型被 uapi_at_cmd_table_register 间接使用。

### at_token_hex_string_t <a id="at_token_hex_string_t"></a>

```c
// 源码原始定义
typedef struct {
    uint32_t length_field_offset;
    uint32_t max_length;
} at_token_hex_string_t;
```

**使用说明**

基于长度的十六进制字符串参数校验语法结构，作为 at_para_parse_syntax_t 内部联合体的 octet_string 成员类型被 uapi_at_cmd_table_register 间接使用。

### at_syntax_type_t <a id="at_syntax_type_t"></a>

```c
// 源码原始定义
typedef enum {
    AT_SYNTAX_TYPE_INT,
    AT_SYNTAX_TYPE_STRING,
    AT_SYNTAX_TYPE_BIT_STRING,
    AT_SYNTAX_TYPE_OCTET_STRING,
    AT_SYNTAX_TYPE_NUM
} at_syntax_type_t;
```

**使用说明**

AT 命令参数类型枚举，作为 at_para_parse_syntax_t 结构体的 type 位域的底层类型被 uapi_at_cmd_table_register 间接使用。

### at_syntax_attribute_t <a id="at_syntax_attribute_t"></a>

```c
// 源码原始定义
typedef enum {
    AT_SYNTAX_ATTR_NOT_SUPPORTED    = 0x0001,
    AT_SYNTAX_ATTR_OPTIONAL         = 0x0002,
    AT_SYNTAX_ATTR_AT_MIN_VALUE     = 0x0004,
    AT_SYNTAX_ATTR_AT_MAX_VALUE     = 0x0008,
    AT_SYNTAX_ATTR_LIST_VALUE       = 0x0010,
    AT_SYNTAX_ATTR_MAX_LENGTH       = 0x0020,
    AT_SYNTAX_ATTR_ADD_LENGTH       = 0x0040,
    AT_SYNTAX_ATTR_FIX_CASE         = 0x0080,
    AT_SYNTAX_ATTR_LENGTH_FIELD     = 0x0100
} at_syntax_attribute_t;
```

**使用说明**

AT 命令参数校验属性枚举，作为 at_para_parse_syntax_t 结构体的 attribute 位域的底层类型被 uapi_at_cmd_table_register 间接使用。

### at_para_parse_syntax_t <a id="at_para_parse_syntax_t"></a>

```c
// 源码原始定义
typedef struct {
    uint32_t type : 4;    /*!< Parameter type(at_syntax_type_t). */
    uint32_t last : 1;    /*!< Identify whether it is the last parameter. */
    uint32_t attribute : 12;    /*!< Parameter type(at_syntax_attribute_t). */
    uint32_t offset : 15;    /*!< Parameter offset of para blob. */
    union {
        at_token_int_range_t int_range;
        at_token_int_list_t  int_list;
        at_token_string_t string;
        at_token_string_values_t string_list;
        at_token_bit_string_range_t bit_string_range;
        at_token_bit_string_list_t bit_string_list;
        at_token_hex_string_t octet_string;
    } entry;
} at_para_parse_syntax_t;
```

**使用说明**

AT 命令单个参数的校验语法结构，作为 at_cmd_entry_t 结构体的 syntax 成员类型被 uapi_at_cmd_table_register 间接使用，描述参数类型、属性、偏移与具体校验范围或白名单。

### at_cmd_entry_t <a id="at_cmd_entry_t"></a>

```c
// 源码原始定义
typedef struct {
    const char *name;    /*!< The name cannot be duplicate. */
    const uint16_t cmd_id;    /*!< The cmd_id cannot be duplicate. */
    const uint16_t attribute;
    const at_para_parse_syntax_t *syntax;
    at_cmd_func_t cmd;
    at_set_func_t set;
    at_read_func_t read;
    at_test_func_t test;
#ifdef CONFIG_AT_SUPPORT_QUERY
    at_query_func_t query;
#endif
} at_cmd_entry_t;
```

**使用说明**

AT 命令实体结构，作为入参出现于 uapi_at_cmd_table_register 接口签名中，描述一条 AT 命令的名称、命令 ID、属性、参数校验语法表及各类型命令回调函数。

### errcode_t <a id="errcode_t"></a>

```c
// 源码原始定义
typedef uint32_t errcode_t;
```

**使用说明**

本模块多个对外接口（uapi_at_cmd_table_register、uapi_at_cmd_abort_register、uapi_at_send_async_result、uapi_at_interactivity_func_register、uapi_at_urc_to_channel）的返回值类型。 

## Associations

### at_para_parse_syntax_t::entry <a id="union_at_para_parse_syntax_entry"></a>

```c
// 源码原始定义（嵌套于 at_para_parse_syntax_t 的命名成员 entry）
union {
    at_token_int_range_t int_range;
    at_token_int_list_t  int_list;
    at_token_string_t string;
    at_token_string_values_t string_list;
    at_token_bit_string_range_t bit_string_range;
    at_token_bit_string_list_t bit_string_list;
    at_token_hex_string_t octet_string;
} entry;
```

| 成员名称 | 类型 | 描述 | 接口使用逻辑 |
| ------- | ---- | ---- | ----------- |
| int_range | at_token_int_range_t | 整型参数取值范围校验项 | 作为 at_para_parse_syntax_t 的 entry 成员被 uapi_at_cmd_table_register 间接使用 |
| int_list | at_token_int_list_t | 整型参数白名单校验项 | 作为 at_para_parse_syntax_t 的 entry 成员被 uapi_at_cmd_table_register 间接使用 |
| string | at_token_string_t | 字符串参数长度校验项 | 作为 at_para_parse_syntax_t 的 entry 成员被 uapi_at_cmd_table_register 间接使用 |
| string_list | at_token_string_values_t | 字符串参数白名单校验项 | 作为 at_para_parse_syntax_t 的 entry 成员被 uapi_at_cmd_table_register 间接使用 |
| bit_string_range | at_token_bit_string_range_t | 二进制字符串参数范围校验项 | 作为 at_para_parse_syntax_t 的 entry 成员被 uapi_at_cmd_table_register 间接使用 |
| bit_string_list | at_token_bit_string_list_t | 二进制字符串参数白名单校验项 | 作为 at_para_parse_syntax_t 的 entry 成员被 uapi_at_cmd_table_register 间接使用 |
| octet_string | at_token_hex_string_t | 十六进制字符串参数长度校验项 | 作为 at_para_parse_syntax_t 的 entry 成员被 uapi_at_cmd_table_register 间接使用 |

## Enumerations

### at_ret_t <a id="enum_at_ret_t"></a>

```c
// 源码原始定义
typedef enum {
    AT_RET_OK = 0,
    AT_RET_SYNTAX_ERROR,
    AT_RET_MALLOC_ERROR,
    AT_RET_MEM_API_ERROR,
    AT_RET_CHANNEL_PARA_ERROR,
    AT_RET_CHANNEL_NOT_INIT,
    AT_RET_CHANNEL_DATA_NULL,
    AT_RET_CMD_PARA_ERROR,
    AT_RET_CMD_FORMAT_ERROR,
    AT_RET_CMD_NO_MATCH,
    AT_RET_CMD_TYPE_ERROR,
    AT_RET_CMD_IN_PROGRESS_BLOCK,
    AT_RET_CMD_ATTR_NOT_ALLOW,
    AT_RET_PROC_CMD_FUNC_MISSING,
    AT_RET_PROC_READ_FUNC_MISSING,
    AT_RET_PROC_TEST_FUNC_MISSING,
    AT_RET_PROC_SET_FUNC_MISSING,
    AT_RET_PROC_WAIT_INTERACTIVITY,
    AT_RET_PROC_ABORT_CURRENT_COMMAND,
    AT_RET_PARSE_PARA_ERROR,
    AT_RET_PARSE_PARA_MISSING_ERROR,
    AT_RET_PROGRESS_BLOCK,
    AT_RET_TIMER_ERROR,
    AT_RET_ABORT_DELAY
} at_ret_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| AT_RET_OK | 0 | 执行成功 |
| AT_RET_SYNTAX_ERROR | 1 | 语法错误 |
| AT_RET_MALLOC_ERROR | 2 | 内存分配错误 |
| AT_RET_MEM_API_ERROR | 3 | 内存接口错误 |
| AT_RET_CHANNEL_PARA_ERROR | 4 | 通道参数错误 |
| AT_RET_CHANNEL_NOT_INIT | 5 | 通道未初始化 |
| AT_RET_CHANNEL_DATA_NULL | 6 | 通道数据为空 |
| AT_RET_CMD_PARA_ERROR | 7 | 命令参数错误 |
| AT_RET_CMD_FORMAT_ERROR | 8 | 命令格式错误 |
| AT_RET_CMD_NO_MATCH | 9 | 无匹配命令 |
| AT_RET_CMD_TYPE_ERROR | 10 | 命令类型错误 |
| AT_RET_CMD_IN_PROGRESS_BLOCK | 11 | 命令执行中阻塞 |
| AT_RET_CMD_ATTR_NOT_ALLOW | 12 | 命令属性不允许 |
| AT_RET_PROC_CMD_FUNC_MISSING | 13 | 缺少执行函数 |
| AT_RET_PROC_READ_FUNC_MISSING | 14 | 缺少读函数 |
| AT_RET_PROC_TEST_FUNC_MISSING | 15 | 缺少测试函数 |
| AT_RET_PROC_SET_FUNC_MISSING | 16 | 缺少设置函数 |
| AT_RET_PROC_WAIT_INTERACTIVITY | 17 | 等待交互 |
| AT_RET_PROC_ABORT_CURRENT_COMMAND | 18 | 打断当前命令 |
| AT_RET_PARSE_PARA_ERROR | 19 | 参数解析错误 |
| AT_RET_PARSE_PARA_MISSING_ERROR | 20 | 参数缺失错误 |
| AT_RET_PROGRESS_BLOCK | 21 | 流程阻塞 |
| AT_RET_TIMER_ERROR | 22 | 定时器错误 |
| AT_RET_ABORT_DELAY | 23 | 打断延迟 |

### at_syntax_type_t <a id="enum_at_syntax_type_t"></a>

```c
// 源码原始定义
typedef enum {
    AT_SYNTAX_TYPE_INT,
    AT_SYNTAX_TYPE_STRING,
    AT_SYNTAX_TYPE_BIT_STRING,
    AT_SYNTAX_TYPE_OCTET_STRING,
    AT_SYNTAX_TYPE_NUM
} at_syntax_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| AT_SYNTAX_TYPE_INT | 0 | 整型参数 |
| AT_SYNTAX_TYPE_STRING | 1 | 字符串参数 |
| AT_SYNTAX_TYPE_BIT_STRING | 2 | 二进制字符串参数 |
| AT_SYNTAX_TYPE_OCTET_STRING | 3 | 十六进制字符串参数 |
| AT_SYNTAX_TYPE_NUM | 4 | 参数类型总数 |

### at_syntax_attribute_t <a id="enum_at_syntax_attribute_t"></a>

```c
// 源码原始定义
typedef enum {
    AT_SYNTAX_ATTR_NOT_SUPPORTED    = 0x0001,
    AT_SYNTAX_ATTR_OPTIONAL         = 0x0002,
    AT_SYNTAX_ATTR_AT_MIN_VALUE     = 0x0004,
    AT_SYNTAX_ATTR_AT_MAX_VALUE     = 0x0008,
    AT_SYNTAX_ATTR_LIST_VALUE       = 0x0010,
    AT_SYNTAX_ATTR_MAX_LENGTH       = 0x0020,
    AT_SYNTAX_ATTR_ADD_LENGTH       = 0x0040,
    AT_SYNTAX_ATTR_FIX_CASE         = 0x0080,
    AT_SYNTAX_ATTR_LENGTH_FIELD     = 0x0100
} at_syntax_attribute_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| AT_SYNTAX_ATTR_NOT_SUPPORTED | 0x0001 | 标识该参数当前不支持 |
| AT_SYNTAX_ATTR_OPTIONAL | 0x0002 | 标识该参数可缺省 |
| AT_SYNTAX_ATTR_AT_MIN_VALUE | 0x0004 | 校验方式为最小值校验 |
| AT_SYNTAX_ATTR_AT_MAX_VALUE | 0x0008 | 校验方式为最大值校验 |
| AT_SYNTAX_ATTR_LIST_VALUE | 0x0010 | 校验方式为白名单校验 |
| AT_SYNTAX_ATTR_MAX_LENGTH | 0x0020 | 校验方式为长度校验 |
| AT_SYNTAX_ATTR_ADD_LENGTH | 0x0040 | 为该参数新增长度字段 |
| AT_SYNTAX_ATTR_FIX_CASE | 0x0080 | 字符串支持大小写混合 |
| AT_SYNTAX_ATTR_LENGTH_FIELD | 0x0100 | 该参数已预设长度字段 |

## Structures

### at_token_int_range_t <a id="struct_at_token_int_range_t"></a>

```c
// 源码原始定义
typedef struct {
    int32_t min_val;
    int32_t max_val;
} at_token_int_range_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| min_val | int32_t | 整型参数取值范围下限 |
| max_val | int32_t | 整型参数取值范围上限 |

### at_token_int_list_t <a id="struct_at_token_int_list_t"></a>

```c
// 源码原始定义
typedef struct {
    uint32_t num;
    const int32_t *values;
} at_token_int_list_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| num | uint32_t | 白名单取值数量 |
| values | const int32_t * | 白名单取值数组起始地址 |

### at_token_string_t <a id="struct_at_token_string_t"></a>

```c
// 源码原始定义
typedef struct {
    uint32_t max_length;
} at_token_string_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| max_length | uint32_t | 字符串参数最大长度 |

### at_token_string_values_t <a id="struct_at_token_string_values_t"></a>

```c
// 源码原始定义
typedef struct {
    uint32_t num;
    const uint8_t * const *values;
} at_token_string_values_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| num | uint32_t | 白名单取值数量 |
| values | const uint8_t * const * | 白名单字符串数组起始地址 |

### at_token_bit_string_range_t <a id="struct_at_token_bit_string_range_t"></a>

```c
// 源码原始定义
typedef struct {
    uint32_t max_value;
} at_token_bit_string_range_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| max_value | uint32_t | 二进制字符串参数取值范围上限 |

### at_token_bit_string_list_t <a id="struct_at_token_bit_string_list_t"></a>

```c
// 源码原始定义
typedef struct {
    uint32_t num;
    const uint32_t *values;
} at_token_bit_string_list_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| num | uint32_t | 白名单取值数量 |
| values | const uint32_t * | 白名单取值数组起始地址 |

### at_token_hex_string_t <a id="struct_at_token_hex_string_t"></a>

```c
// 源码原始定义
typedef struct {
    uint32_t length_field_offset;
    uint32_t max_length;
} at_token_hex_string_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| length_field_offset | uint32_t | 标识长度字段的偏移，用于存储十六进制字符串转换后的数据长度 |
| max_length | uint32_t | 十六进制字符串参数最大长度 |

### at_para_parse_syntax_t <a id="struct_at_para_parse_syntax_t"></a>

```c
// 源码原始定义
typedef struct {
    uint32_t type : 4;    /*!< Parameter type(at_syntax_type_t). */
    uint32_t last : 1;    /*!< Identify whether it is the last parameter. */
    uint32_t attribute : 12;    /*!< Parameter type(at_syntax_attribute_t). */
    uint32_t offset : 15;    /*!< Parameter offset of para blob. */
    union {
        at_token_int_range_t int_range;
        at_token_int_list_t  int_list;
        at_token_string_t string;
        at_token_string_values_t string_list;
        at_token_bit_string_range_t bit_string_range;
        at_token_bit_string_list_t bit_string_list;
        at_token_hex_string_t octet_string;
    } entry;
} at_para_parse_syntax_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| type | uint32_t : 4 | 参数类型，取值见 at_syntax_type_t |
| last | uint32_t : 1 | 标识是否为最后一个参数 |
| attribute | uint32_t : 12 | 参数校验属性，取值见 at_syntax_attribute_t |
| offset | uint32_t : 15 | 参数在参数 blob 中的偏移 |
| entry | union | 参数校验范围或白名单联合体，具体成员依 type 与 attribute 选用 |

### at_cmd_entry_t <a id="struct_at_cmd_entry_t"></a>

```c
// 源码原始定义
typedef struct {
    const char *name;    /*!< The name cannot be duplicate. */
    const uint16_t cmd_id;    /*!< The cmd_id cannot be duplicate. */
    const uint16_t attribute;
    const at_para_parse_syntax_t *syntax;
    at_cmd_func_t cmd;
    at_set_func_t set;
    at_read_func_t read;
    at_test_func_t test;
#ifdef CONFIG_AT_SUPPORT_QUERY
    at_query_func_t query;
#endif
} at_cmd_entry_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| name | const char * | AT 命令名称，不可重复，开启命令表检查时需全部由大写字母组成且长度不超过 AT_CMD_NAME_MAX_LENGTH |
| cmd_id | const uint16_t | AT 命令 ID，不可重复 |
| attribute | const uint16_t | AT 命令属性标志 |
| syntax | const at_para_parse_syntax_t * | AT 命令参数校验语法表起始地址，set 回调存在时不可为 NULL |
| cmd | at_cmd_func_t | 执行命令回调函数 |
| set | at_set_func_t | 设置命令回调函数 |
| read | at_read_func_t | 读取命令回调函数 |
| test | at_test_func_t | 测试命令回调函数 |
| query | at_query_func_t | 查询命令回调函数，仅开启 CONFIG_AT_SUPPORT_QUERY 时存在 |

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```

### ERRCODE_INVALID_PARAM <a id="ERRCODE_INVALID_PARAM"></a>

```c
#define ERRCODE_INVALID_PARAM                               0x80000001
```

### ERRCODE_MEMCPY <a id="ERRCODE_MEMCPY"></a>

```c
#define ERRCODE_MEMCPY                                      0x80000004
```

### ERRCODE_MALLOC <a id="ERRCODE_MALLOC"></a>

```c
#define ERRCODE_MALLOC                                      0x80000005
```

### ERRCODE_AT_CMD_REPEAT <a id="ERRCODE_AT_CMD_REPEAT"></a>

```c
#define ERRCODE_AT_CMD_REPEAT                               0x80003022
```

### ERRCODE_AT_CMD_TABLE_PARA_ERROR <a id="ERRCODE_AT_CMD_TABLE_PARA_ERROR"></a>

```c
#define ERRCODE_AT_CMD_TABLE_PARA_ERROR                     0x80003023
```

### ERRCODE_AT_MSG_SEND_ERROR <a id="ERRCODE_AT_MSG_SEND_ERROR"></a>

```c
#define ERRCODE_AT_MSG_SEND_ERROR                           0x80003024
```
