# dfx

dfx（Design For eXcellence）提供 DIAG (Diagnosis) 诊断通道的命令注册、报文上报、消息上报与统计量注册能力，并通过 diag_log 子模块提供 Error / Warning / Info / Debug 四个级别的日志打印接口。

**模块公共头文件**

```c
#include "include/middleware/utils/diag.h"
#include "include/middleware/utils/diag_log.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_diag_register_cmd](#uapi_diag_register_cmd) | 注册 diag 命令处理函数表 |
| [uapi_diag_unregister_cmd](#uapi_diag_unregister_cmd) | 解注册已注册的 diag 命令处理函数表 |
| [uapi_diag_report_packet](#uapi_diag_report_packet) | 上报单个 diag 报文给 DIAG 客户端 |
| [uapi_diag_report_packets_critical](#uapi_diag_report_packets_critical) | 上报多个关键级别 diag 报文给 DIAG 客户端 |
| [uapi_diag_report_packets_normal](#uapi_diag_report_packets_normal) | 上报多个普通级别 diag 报文给 DIAG 客户端 |
| [uapi_diag_report_sys_msg](#uapi_diag_report_sys_msg) | 上报系统消息给 DIAG 客户端 |
| [uapi_diag_register_ind](#uapi_diag_register_ind) | 注册 diag 应答（ind）处理函数表 |
| [uapi_diag_run_cmd](#uapi_diag_run_cmd) | 按 cmd_id 触发执行已注册的 diag 命令处理函数 |
| [uapi_diag_register_stat_obj](#uapi_diag_register_stat_obj) | 注册 diag 统计量对象表 |

## Functions

### uapi_diag_register_cmd <a id="uapi_diag_register_cmd"></a>

```c
errcode_t uapi_diag_register_cmd(const diag_cmd_reg_obj_t *cmd_tbl, uint16_t cmd_num)
```

**声明头文件**

```c
#include "include/middleware/utils/diag.h"
```

**功能说明**

- 向 DIAG 子系统注册一组 diag 命令处理函数表，使后续到来的 cmd_id 命中该表区间时能够分发到对应的处理函数。
- 注册时按命令表中最小/最大命令 ID 区间进行索引，DIAG 子系统在分发命令时按区间匹配查找处理函数。
- 命令表必须以常量数组形式提供，命令条数由调用方显式传入。

**前置条件**

- 调用时序约束：DIAG 子系统已完成初始化（命令分发控制结构可用）。
- 上下文限制：内部通过关中断保护命令表写入，调用方应避免在中断上下文中长时间持表注册。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| cmd_tbl | [diag_cmd_reg_obj_t](#diag_cmd_reg_obj_t) | diag 命令注册表，需声明为常量数组后传入 | 不为NULL |
| cmd_num | uint16_t | 命令条数 | 不为0 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 命令表注册成功，已写入空闲槽位 |
| ERRCODE_FAIL：0xFFFFFFFF | 执行失败 | 命令表已满，无空闲槽位可注册 |

**参考案例**

- `src/middleware/chips/ws53/dfx/dfx_system_init.c`
- `src/middleware/utils/dfx/zdiag/diag_system_cmd/diag_mocked_shell.c`

### uapi_diag_unregister_cmd <a id="uapi_diag_unregister_cmd"></a>

```c
errcode_t uapi_diag_unregister_cmd(const diag_cmd_reg_obj_t *cmd_tbl, uint16_t cmd_num)
```

**声明头文件**

```c
#include "include/middleware/utils/diag.h"
```

**功能说明**

- 将先前通过 uapi_diag_register_cmd 注册的命令处理函数表从 DIAG 子系统中清除。
- 通过命令表指针与命令条数联合匹配定位待清除的注册项，匹配成功后清空对应槽位。
- 解注册后该命令表区间不再参与命令分发。

**前置条件**

- 调用时序约束：待解注册的命令表必须已通过 uapi_diag_register_cmd 成功注册。
- 依赖关系：传入的 cmd_tbl 与 cmd_num 必须与注册时完全一致，否则无法匹配。
- 上下文限制：内部通过关中断保护命令表写入，调用方应避免在中断上下文中长时间持表操作。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| cmd_tbl | [diag_cmd_reg_obj_t](#diag_cmd_reg_obj_t) | 待解注册的 diag 命令注册表，需与注册时传入的指针一致 | 不为NULL |
| cmd_num | uint16_t | 待解注册的命令条数，需与注册时传入的条数一致 | 不为0 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 命令表匹配成功，已清空对应槽位 |
| ERRCODE_FAIL：0xFFFFFFFF | 执行失败 | 未找到与传入 cmd_tbl/cmd_num 匹配的注册项 |

### uapi_diag_report_packet <a id="uapi_diag_report_packet"></a>

```c
errcode_t uapi_diag_report_packet(uint16_t cmd_id, diag_option_t *option, const uint8_t *packet, uint16_t packet_size, bool sync)
```

**声明头文件**

```c
#include "include/middleware/utils/diag.h"
```

**功能说明**

- 向 DIAG 客户端上报单个 diag 通道报文，cmd_id 用于标识报文 ID。
- 通过 option 参数指示报文是本地报文还是远端报文（携带对端地址）。
- 支持同步（sync 为 true，阻塞上报）与异步（sync 为 false，经 OS 队列缓存后非阻塞上报）两种上报方式。

**前置条件**

- 调用时序约束：DIAG 通道已连接（zdiag 已使能），否则直接返回失败。
- 依赖关系：传入的 packet 缓冲区在同步上报返回前需保持有效；异步上报时由 OS 队列缓存后释放。
- 上下文限制：同步上报会阻塞当前流程，调用方需评估与 DIAG 接收侧的时序关系。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| cmd_id | uint16_t | 报文上报 ID，与命令回调函数中的 cmd_id 一致时复用该值 | 0 ~ 65535 |
| option | [diag_option_t](#diag_option_t) | option 选项，携带对端地址，用于识别报文是本地报文还是远端报文；为 NULL 时按本地默认地址处理 | 可为NULL |
| packet | const uint8_t * | 数据包缓冲区地址 | 不为NULL |
| packet_size | uint16_t | 数据包大小（单位：字节） | 0 ~ 65535 |
| sync | bool | 上报方式，true 表示同步阻塞上报，false 表示异步非阻塞上报 | true；<br>false。 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 报文成功投递至 DIAG 路由处理流程 |
| ERRCODE_FAIL：0xFFFFFFFF | 执行失败 | DIAG 未连接（zdiag 未使能） |

**参考案例**

- `src/middleware/chips/ws53/dfx/diag_sample_data.c`
- `src/middleware/chips/ws53/dfx/sample_data_adapt.c`
- `src/middleware/chips/ws53/nv/nv_zdiag/nv_adapt_zdiag.c`
- `src/middleware/utils/at/at/src/at_zdiag.c`
- `src/middleware/utils/dfx/zdiag/diag_system_cmd/diag_cmd_beat_heart.c`

### uapi_diag_report_packets_critical <a id="uapi_diag_report_packets_critical"></a>

```c
errcode_t uapi_diag_report_packets_critical(uint16_t cmd_id, diag_option_t *option, uint8_t **packet, uint16_t *packet_size, uint8_t pkt_cnt)
```

**声明头文件**

```c
#include "include/middleware/utils/diag.h"
```

**功能说明**

- 向 DIAG 客户端上报多个关键级别（critical）的 diag 通道报文。
- 通过 packet 指针数组与 packet_size 数组联合描述多个数据包，pkt_cnt 指定数据包个数。
- 关键级别报文在 DIAG 路由处理中按 critical 标记优先处理。

**前置条件**

- 调用时序约束：DIAG 通道已连接（zdiag 已使能），否则直接返回失败。
- 依赖关系：packet 指针数组与 packet_size 数组的元素个数必须不小于 pkt_cnt，且各 packet[i] 缓冲区在投递完成前保持有效。
- 上下文限制：无特殊上下文限制。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| cmd_id | uint16_t | 报文上报 ID | 0 ~ 65535 |
| option | [diag_option_t](#diag_option_t) | option 选项，携带对端地址；为 NULL 时按本地默认地址处理 | 可为NULL |
| packet | uint8_t ** | 指向数据包指针数组的指针，每个元素为一个数据包缓冲区地址 | 不为NULL |
| packet_size | uint16_t * | 指向数据包大小数组的指针，每个元素与 packet 数组元素一一对应（单位：字节） | 不为NULL |
| pkt_cnt | uint8_t | 数据包个数 | 0 ~ DIAG_PKT_DATA_ID_USR_MAX-1（实现仅拒绝超出上界的值） |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 多包报文成功投递至 DIAG 路由处理流程 |
| ERRCODE_FAIL：0xFFFFFFFF | 执行失败 | DIAG 未连接或 pkt_cnt 超出允许上限 |

**参考案例**

- `src/middleware/utils/dfx/zdiag/diag_system_cmd/diag_cmd_trace_info.c`
- `src/middleware/utils/dfx/zdiag/diag_system_cmd/last_dump.c`

### uapi_diag_report_packets_normal <a id="uapi_diag_report_packets_normal"></a>

```c
errcode_t uapi_diag_report_packets_normal(uint16_t cmd_id, diag_option_t *option, uint8_t **packet, uint16_t *packet_size, uint8_t pkt_cnt)
```

**声明头文件**

```c
#include "include/middleware/utils/diag.h"
```

**功能说明**

- 向 DIAG 客户端上报多个普通级别（normal）的 diag 通道报文。
- 通过 packet 指针数组与 packet_size 数组联合描述多个数据包，pkt_cnt 指定数据包个数。
- 普通级别报文不携带 critical 标记，按常规 DIAG 路由流程处理。

**前置条件**

- 调用时序约束：DIAG 通道已连接（zdiag 已使能），否则直接返回失败。
- 依赖关系：packet 指针数组与 packet_size 数组的元素个数必须不小于 pkt_cnt，且各 packet[i] 缓冲区在投递完成前保持有效。
- 上下文限制：无特殊上下文限制。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| cmd_id | uint16_t | 报文上报 ID | 0 ~ 65535 |
| option | [diag_option_t](#diag_option_t) | option 选项，携带对端地址；为 NULL 时按本地默认地址处理 | 可为NULL |
| packet | uint8_t ** | 指向数据包指针数组的指针，每个元素为一个数据包缓冲区地址 | 不为NULL |
| packet_size | uint16_t * | 指向数据包大小数组的指针，每个元素与 packet 数组元素一一对应（单位：字节） | 不为NULL |
| pkt_cnt | uint8_t | 数据包个数 | 0 ~ DIAG_PKT_DATA_ID_USR_MAX-1（实现仅拒绝超出上界的值） |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 多包报文成功投递至 DIAG 路由处理流程 |
| ERRCODE_FAIL：0xFFFFFFFF | 执行失败 | DIAG 未连接或 pkt_cnt 超出允许上限 |

**参考案例**

- `src/middleware/utils/dfx/zdiag/diag_system_cmd/diag_bt_sample_data.c`

### uapi_diag_report_sys_msg <a id="uapi_diag_report_sys_msg"></a>

```c
errcode_t uapi_diag_report_sys_msg(uint32_t module_id, uint32_t msg_id, const uint8_t *buf, uint16_t buf_size, uint8_t level)
```

**声明头文件**

```c
#include "include/middleware/utils/diag.h"
```

**功能说明**

- 向 DIAG 客户端上报系统消息，携带源模块 ID、消息 ID、内容缓冲区与日志级别。
- 上报前根据 module_id 与 level 进行过滤判定，未通过过滤则直接返回失败。
- 当离线日志文件功能使能且开启时，消息会被写入离线日志文件；否则通过 DIAG 报文路由投递。

**前置条件**

- 调用时序约束：DIAG 子系统已初始化，且 diag_rom_api 中的 report_sys_msg 已注册。
- 依赖关系：buf 缓冲区在函数返回前需保持有效；level 需为合法日志级别。
- 上下文限制：当离线日志文件写入失败时，函数会通过 printf 输出错误信息，调用方需评估日志输出环境。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| module_id | uint32_t | 打印日志的源模块 ID | 0 ~ 4294967295 |
| msg_id | uint32_t | 打印日志的消息 ID | 0 ~ 4294967295 |
| buf | const uint8_t * | 打印内容缓冲区 | 不为NULL（buf_size 非 0 时） |
| buf_size | uint16_t | 内容大小（单位：字节） | 0 ~ 65535 |
| level | uint8_t | 日志级别 | DIAG_LEVEL_DEBUG/DIAG_LEVEL_NOTICE/DIAG_LEVEL_WARNING/DIAG_LEVEL_ERROR/DIAG_LEVEL_FATAL 中有效值（由 diag 定义的日志级别枚举决定） |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 消息成功通过过滤并投递 |
| ERRCODE_FAIL：0xFFFFFFFF | 执行失败 | diag_rom_api 中 report_sys_msg 未注册，或消息未通过过滤判定 |
| Other | 其他错误码，参考 errcode_t（定义于 errcode.h） | 含离线日志文件写入内存分配失败（ERRCODE_MALLOC）等 |

**参考案例**

- `src/middleware/chips/ws53/dfx/diag_adapt_sdt.c`
- `src/middleware/chips/ws53/dfx/diag_sample_data.c`
- `src/middleware/utils/dfx/log/log_printf.c`
- `src/middleware/utils/dfx/zdiag/romable/diag_oam_log.c`
- `src/middleware/utils/dfx/zdiag/zdiag_dfx.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DFX_SUPPORT_OFFLINE_LOG_FILE | 特性宏 | 支持离线日志文件写入分支（分支级，DFX_FEATURE_CONFIG 宏，默认关闭） | n |

### uapi_diag_register_ind <a id="uapi_diag_register_ind"></a>

```c
errcode_t uapi_diag_register_ind(const diag_cmd_reg_obj_t *cmd_tbl, uint16_t cmd_num)
```

**声明头文件**

```c
#include "include/middleware/utils/diag.h"
```

**功能说明**

- 向 DIAG 子系统注册一组应答（ind）处理函数表，用于接收侧的 ind 命令分发。
- 注册项按 cmd_tbl 指针与 cmd_num 联合索引，写入应答表的空闲槽位。
- 命令表必须以常量数组形式提供。

**前置条件**

- 调用时序约束：DIAG 子系统已完成初始化（应答分发控制结构可用）。
- 上下文限制：内部通过关中断保护应答表写入，调用方应避免在中断上下文中长时间持表注册。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| cmd_tbl | [diag_cmd_reg_obj_t](#diag_cmd_reg_obj_t) | 注册应答表，需声明为常量数组后传入 | 不为NULL |
| cmd_num | uint16_t | 应答个数 | 不为0 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 应答表注册成功，已写入空闲槽位 |
| ERRCODE_FAIL：0xFFFFFFFF | 执行失败 | 应答表已满，无空闲槽位可注册 |

### uapi_diag_run_cmd <a id="uapi_diag_run_cmd"></a>

```c
errcode_t uapi_diag_run_cmd(uint16_t cmd_id, uint8_t *data, uint16_t data_size, diag_option_t *option)
```

**声明头文件**

```c
#include "include/middleware/utils/diag.h"
```

**功能说明**

- 按 cmd_id 构造 diag 命令请求报文，并异步投递至 DIAG 路由处理流程。
- 通过 option 参数携带对端地址，用于指示命令的目标。
- 数据内容由 data 缓冲区与 data_size 联合描述。

**前置条件**

- 调用时序约束：DIAG 通道已连接（zdiag 已使能）。
- 依赖关系：data 缓冲区在报文投递完成前需保持有效；option 不能为 NULL（内部直接解引用 option->peer_addr）。
- 上下文限制：以异步方式（DIAG_PKT_PROC_USR_ASYNC_CMD_IND）投递，调用方不阻塞等待命令处理结果。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| cmd_id | uint16_t | diag 命令请求 ID | 0 ~ 65535 |
| data | uint8_t * | 数据内容缓冲区地址 | 不为NULL |
| data_size | uint16_t | 数据大小（单位：字节） | 0 ~ 65535 |
| option | [diag_option_t](#diag_option_t) | option 选项，携带对端地址 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 命令请求报文成功投递至 DIAG 路由处理流程 |
| ERRCODE_FAIL：0xFFFFFFFF | 执行失败 | DIAG 路由处理返回失败 |

### uapi_diag_register_stat_obj <a id="uapi_diag_register_stat_obj"></a>

```c
errcode_t uapi_diag_register_stat_obj(const diag_sys_stat_obj_t *stat_obj_tbl, uint16_t obj_num)
```

**声明头文件**

```c
#include "include/middleware/utils/diag.h"
```

**功能说明**

- 向 DIAG 子系统注册一组统计量对象表，供后续统计量查询与上报使用。
- 注册项按 stat_obj_tbl 指针与 obj_num 联合索引，写入统计量控制结构的空闲槽位。
- 每个统计量对象包含统计量 ID、数组数量、单个统计结构大小与统计量数据指针。

**前置条件**

- 调用时序约束：DIAG 子系统已完成初始化（统计量控制结构可用）。
- 依赖关系：统计量数据指针（stat_packet）需在统计量生命周期内保持有效。
- 上下文限制：内部通过关中断保护统计量表写入，调用方应避免在中断上下文中长时间持表注册。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| stat_obj_tbl | [diag_sys_stat_obj_t](#diag_sys_stat_obj_t) | 统计量注册表，需声明为常量数组后传入 | 不为NULL |
| obj_num | uint16_t | 统计量个数 | 不为0 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 统计量对象表注册成功，已写入空闲槽位 |
| ERRCODE_FAIL：0xFFFFFFFF | 执行失败 | 统计量表已满，无空闲槽位可注册 |

## Type definitions

### diag_addr <a id="diag_addr"></a>

```c
typedef uint8_t diag_addr;
```

**使用说明**

diag 通道地址类型，用于标识报文的对端地址，作为 [diag_option_t](#diag_option_t) 的成员被本模块对外接口使用。

### diag_cmd_f <a id="diag_cmd_f"></a>

```c
typedef errcode_t (*diag_cmd_f)(uint16_t cmd_id, void *cmd_param, uint16_t cmd_param_size, diag_option_t *option);
```

**使用说明**

diag 命令行处理函数指针类型，作为 [diag_cmd_reg_obj_t](#diag_cmd_reg_obj_t) 的成员被 uapi_diag_register_cmd / uapi_diag_register_ind 接口注册。

回调说明：
- 调用时机：DIAG 子系统在分发命令时，按注册表中的命令 ID 区间匹配命中后调用该处理函数。
- 参数 cmd_id：触发本次处理的 diag 命令 ID。
- 参数 cmd_param：命令参数数据指针，内容来源于命令请求报文。
- 参数 cmd_param_size：命令参数数据大小（单位：字节）。
- 参数 option：option 选项，携带对端地址信息。
- 返回值处理：处理函数返回的 errcode_t 由 DIAG 命令分发流程接收。

## Structures

### diag_option_t <a id="diag_option_t"></a>

```c
typedef struct {
    diag_addr peer_addr;        /*!< peer addr. */
    uint8_t pad[3];             /*!< pad. */
} diag_option_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| peer_addr | diag_addr | 对端地址 |
| pad | uint8_t[3] | 预留字段 |

### diag_cmd_reg_obj_t <a id="diag_cmd_reg_obj_t"></a>

```c
typedef struct {
    uint16_t min_id;               /*!< Minimum DIAG ID. */
    uint16_t max_id;               /*!< Maximum DIAG ID. */
    diag_cmd_f fn_input_cmd;      /*!< This Handler is used to process the HSO command. */
} diag_cmd_reg_obj_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| min_id | uint16_t | Diag 最小命令 ID |
| max_id | uint16_t | Diag 最大命令 ID |
| fn_input_cmd | diag_cmd_f | Diag 命令处理函数 |

### diag_sys_stat_obj_t <a id="diag_sys_stat_obj_t"></a>

```c
typedef struct {
    uint16_t id;                 /*!< Statistics ID. */
    uint16_t array_cnt;          /*!< Number of statistic structures. */
    uint32_t stat_packet_size;   /*!< Size of a single statistic structure (unit: byte). */
    void *stat_packet;           /*!< Pointer to the statistic structure. */
} diag_sys_stat_obj_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| id | uint16_t | 统计量 ID |
| array_cnt | uint16_t | 统计量数量 |
| stat_packet_size | uint32_t | 每个统计量的大小（单位：字节） |
| stat_packet | void * | 指向统计量的指针 |

## Macros

### uapi_diag_error_log <a id="uapi_diag_error_log"></a>

```c
#define uapi_diag_error_log(id, fmt, args...)         uapi_diag_error_logx(id, fmt, ##args)
```

### uapi_diag_warning_log <a id="uapi_diag_warning_log"></a>

```c
#define uapi_diag_warning_log(id, fmt, args...)       uapi_diag_warning_logx(id, fmt, ##args)
```

### uapi_diag_info_log <a id="uapi_diag_info_log"></a>

```c
#define uapi_diag_info_log(id, fmt, args...)          uapi_diag_info_logx(id, fmt, ##args)
```

### uapi_diag_debug_log <a id="uapi_diag_debug_log"></a>

```c
#define uapi_diag_debug_log(id, fmt, args...)         uapi_diag_debug_logx(id, fmt, ##args)
```
