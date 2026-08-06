# sdio

SDIO (Secure Digital Input Output) Slave 接口提供 SDIO 从设备侧的初始化、去初始化、软复位、消息收发与状态查询能力，支持中断回调注册、ADMA (ADMA Descriptor Table) 描述符配置与扩展信息读写，用于 DEVICE 与 HOST 之间的数据传输与消息交互。

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_sdio_slave_init](#uapi_sdio_slave_init) | 初始化 SDIO 通道 |
| [uapi_sdio_slave_deinit](#uapi_sdio_slave_deinit) | 去初始化 SDIO 通道 |
| [uapi_sdio_slave_reinit](#uapi_sdio_slave_reinit) | 重新初始化 SDIO 通道 |
| [uapi_sdio_slave_soft_reset](#uapi_sdio_slave_soft_reset) | 执行 SDIO IP 芯片复位 |
| [uapi_sdio_slave_register_callback](#uapi_sdio_slave_register_callback) | 注册 SDIO 中断回调函数 |
| [uapi_sdio_slave_complete_send](#uapi_sdio_slave_complete_send) | 配置 EDMA 描述符结束标志 |
| [uapi_sdio_slave_set_pad_admatab](#uapi_sdio_slave_set_pad_admatab) | 配置数据对齐后的 ADMA 表 |
| [uapi_sdio_slave_write_extend_info](#uapi_sdio_slave_write_extend_info) | 写入 SDIO 扩展信息 |
| [uapi_sdio_slave_get_extend_info](#uapi_sdio_slave_get_extend_info) | 获取 SDIO 扩展区配置信息 |
| [uapi_sdio_slave_prepare_send_data](#uapi_sdio_slave_prepare_send_data) | 启动数据发送 |
| [uapi_sdio_slave_set_admatab](#uapi_sdio_slave_set_admatab) | 设置 ADMA 传输通道 |
| [uapi_sdio_slave_sched_msg](#uapi_sdio_slave_sched_msg) | 调度 SDIO 挂起消息 |
| [uapi_sdio_slave_sync_msg](#uapi_sdio_slave_sync_msg) | 将消息加入队列并发送 |
| [uapi_sdio_slave_send_msg_ack](#uapi_sdio_slave_send_msg_ack) | 发送指定消息并覆盖当前发送消息 |
| [uapi_sdio_slave_process_msg](#uapi_sdio_slave_process_msg) | 清除指定挂起消息并发送新消息 |
| [uapi_sdio_slave_is_pending_msg](#uapi_sdio_slave_is_pending_msg) | 判断 SDIO 是否挂起指定消息 |
| [uapi_sdio_slave_is_sending_msg](#uapi_sdio_slave_is_sending_msg) | 判断 SDIO 是否正在发送指定消息 |
| [uapi_sdio_slave_register_notify_message_callback](#uapi_sdio_slave_register_notify_message_callback) | 注册通知 HOST 消息或数据事件的回调 |
| [uapi_sdio_slave_read_retry_when_read_err](#uapi_sdio_slave_read_retry_when_read_err) | 读错误事件存在时尝试重新读取 |
| [uapi_sdio_slave_init_no_wait](#uapi_sdio_slave_init_no_wait) | 非阻塞方式初始化 SDIO 通道 |
| [uapi_sdio_slave_host_clk_ready](#uapi_sdio_slave_host_clk_ready) | 判断 HOST 时钟是否就绪 |
| [uapi_sdio_slave_get_status](#uapi_sdio_slave_get_status) | 获取当前 SDIO 通道状态信息 |
| [uapi_sdio_slave_set_status](#uapi_sdio_slave_set_status) | 设置当前 SDIO 通道状态信息 |
| [uapi_sdio_slave_memory_init](#uapi_sdio_slave_memory_init) | SDIO 内存初始化 |
| [uapi_sdio_slave_get_info](#uapi_sdio_slave_get_info) | 获取 SDIO 信息结构体指针 |
| [uapi_sdio_slave_set_extend_val_info](#uapi_sdio_slave_set_extend_val_info) | 写入扩展信息指定地址偏移的值 |
| [uapi_sdio_slave_get_extend_val_info](#uapi_sdio_slave_get_extend_val_info) | 获取扩展信息指定地址偏移的值 |

## Functions

### uapi_sdio_slave_init <a id="uapi_sdio_slave_init"></a>

```c
errcode_t uapi_sdio_slave_init(sdio_bus_t bus)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 初始化指定 SDIO 通道，完成从设备侧初始化
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口需在 SDIO 硬件资源就绪后调用
- 依赖关系：当前接口依赖 SDIO 总线硬件已就绪
- 上下文限制：当前接口需在主线程调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 初始化成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**参考案例**

- `src/drivers/chips/ws53/rom/app/middleware/utils/hcc/acore/slave/hcc_sdio_device.c`

### uapi_sdio_slave_deinit <a id="uapi_sdio_slave_deinit"></a>

```c
void uapi_sdio_slave_deinit(sdio_bus_t bus)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 去初始化指定 SDIO 通道，释放从设备侧初始化资源

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |

**参考案例**

- `src/drivers/chips/ws53/rom/app/middleware/utils/hcc/acore/slave/hcc_sdio_device.c`

### uapi_sdio_slave_reinit <a id="uapi_sdio_slave_reinit"></a>

```c
errcode_t uapi_sdio_slave_reinit(sdio_bus_t bus)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 重新初始化指定 SDIO 通道
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化
- 上下文限制：当前接口需在主线程调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 重新初始化成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**参考案例**

- `src/drivers/chips/ws53/rom/app/middleware/utils/hcc/acore/slave/hcc_sdio_device.c`

### uapi_sdio_slave_soft_reset <a id="uapi_sdio_slave_soft_reset"></a>

```c
void uapi_sdio_slave_soft_reset(sdio_bus_t bus)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 执行 SDIO IP 芯片复位

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |

**参考案例**

- `src/drivers/chips/ws53/rom/app/middleware/utils/hcc/acore/slave/hcc_sdio_device.c`

### uapi_sdio_slave_register_callback <a id="uapi_sdio_slave_register_callback"></a>

```c
errcode_t uapi_sdio_slave_register_callback(sdio_bus_t bus, const sdio_callback_func_t *fun)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 为指定 SDIO 通道注册中断回调函数结构体
- 回调覆盖读开始、读结束、读错误、写开始、写结束、消息处理、软复位等事件
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化
- 上下文限制：当前接口需在主线程调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |
| fun | [sdio_callback_func_t](#sdio_callback_func_t) * | SDIO 中断回调函数结构体指针，参考 [sdio_callback_func_t](#sdio_callback_func_t) | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 注册成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**参考案例**

- `src/drivers/chips/ws53/rom/app/middleware/utils/hcc/acore/slave/hcc_sdio_device.c`

### uapi_sdio_slave_complete_send <a id="uapi_sdio_slave_complete_send"></a>

```c
errcode_t uapi_sdio_slave_complete_send(uint8_t *adma_tab, uint32_t adma_index)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 配置内部 EDMA (Enhanced Direct Memory Access) 描述符的结束标志
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口需在 SDIO 通道初始化后调用
- 依赖关系：当前接口依赖 ADMA 表内存已分配

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| adma_tab | uint8_t * | ADMA 表首地址 | 不为NULL |
| adma_index | uint32_t | ADMA 传输通道号 | 0 ~ 4294967295 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 配置成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### uapi_sdio_slave_set_pad_admatab <a id="uapi_sdio_slave_set_pad_admatab"></a>

```c
errcode_t uapi_sdio_slave_set_pad_admatab(uint8_t *adma_tab, uint32_t adma_index, uint32_t padlen)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 配置数据对齐后的 ADMA 表
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口需在 SDIO 通道初始化后调用
- 依赖关系：当前接口依赖 ADMA 表内存已分配

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| adma_tab | uint8_t * | ADMA 表首地址 | 不为NULL |
| adma_index | uint32_t | ADMA 传输通道号 | 0 ~ 4294967295 |
| padlen | uint32_t | 数据对齐后要发送的数据长度 | 0 ~ 4294967295 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 配置成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### uapi_sdio_slave_write_extend_info <a id="uapi_sdio_slave_write_extend_info"></a>

```c
errcode_t uapi_sdio_slave_write_extend_info(sdio_bus_t bus, sdio_extendfunc_t* extfunc)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 将扩展信息结构体写入指定 SDIO 通道
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |
| extfunc | [sdio_extendfunc_t](#sdio_extendfunc_t) * | 扩展信息结构体指针，参考 [sdio_extendfunc_t](#sdio_extendfunc_t) | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 写入成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SDIO_EXTEND_INFO | 特性宏 | 支持 SDIO 扩展信息读写接口功能（接口级） | n |

### uapi_sdio_slave_get_extend_info <a id="uapi_sdio_slave_get_extend_info"></a>

```c
sdio_extendfunc_t* uapi_sdio_slave_get_extend_info(sdio_bus_t bus)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 获取指定 SDIO 通道的扩展区配置信息指针
- 返回扩展信息缓冲区指针

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |

**返回值**

- 返回类型：sdio_extendfunc_t *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非 NULL | 扩展区配置信息指针，参考 [sdio_extendfunc_t](#sdio_extendfunc_t) | 获取成功 |
| NULL | 获取失败 | 扩展信息不可用 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SDIO_EXTEND_INFO | 特性宏 | 支持 SDIO 扩展信息读写接口功能（接口级） | n |

### uapi_sdio_slave_prepare_send_data <a id="uapi_sdio_slave_prepare_send_data"></a>

```c
errcode_t uapi_sdio_slave_prepare_send_data(sdio_bus_t bus, uint32_t data_len)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 启动指定 SDIO 通道的数据发送
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化
- 上下文限制：当前接口需在主线程调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |
| data_len | uint32_t | 发送数据长度 | 0 ~ 4294967295 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 启动发送成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### uapi_sdio_slave_set_admatab <a id="uapi_sdio_slave_set_admatab"></a>

```c
errcode_t uapi_sdio_slave_set_admatab(uint8_t *adma_tab, uint32_t adma_index, const uint32_t *data_addr, uint32_t data_len)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 设置 ADMA 传输通道，配置传输目的地址与数据长度
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口需在 SDIO 通道初始化后调用
- 依赖关系：当前接口依赖 ADMA 表内存已分配

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| adma_tab | uint8_t * | ADMA 表首地址 | 不为NULL |
| adma_index | uint32_t | ADMA 传输通道号 | 0 ~ 4294967295 |
| data_addr | const uint32_t * | ADMA 传输目的地址 | 不为NULL |
| data_len | uint32_t | ADMA 传输数据长度 | 0 ~ 4294967295 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 设置成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### uapi_sdio_slave_sched_msg <a id="uapi_sdio_slave_sched_msg"></a>

```c
errcode_t uapi_sdio_slave_sched_msg(sdio_bus_t bus)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 调度指定 SDIO 通道的挂起消息
- 没有挂起消息或挂起消息发送成功时返回成功
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化
- 上下文限制：当前接口需在主线程调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 没有挂起的消息，或将挂起的消息发送成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | SDIO 不在工作状态，或 SDIO 正在发送消息 |

### uapi_sdio_slave_sync_msg <a id="uapi_sdio_slave_sync_msg"></a>

```c
errcode_t uapi_sdio_slave_sync_msg(sdio_bus_t bus, uint32_t msg)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 将给定消息加入消息队列并发送
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化
- 上下文限制：当前接口需在主线程调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |
| msg | uint32_t | 给定消息号 | 0 ~ 31 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 消息加入队列并发送成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### uapi_sdio_slave_send_msg_ack <a id="uapi_sdio_slave_send_msg_ack"></a>

```c
errcode_t uapi_sdio_slave_send_msg_ack(sdio_bus_t bus, uint32_t msg)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 发送指定消息，当前正在发送的消息将被该消息覆盖
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化
- 上下文限制：当前接口需在主线程调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |
| msg | uint32_t | 用于覆盖当前正在发送消息的指定消息号 | 0 ~ 31 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 发送成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### uapi_sdio_slave_process_msg <a id="uapi_sdio_slave_process_msg"></a>

```c
errcode_t uapi_sdio_slave_process_msg(sdio_bus_t bus, uint32_t send_msg, uint32_t clear_msg)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 清除消息队列中挂起的指定消息，将新消息加入消息队列并发送
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化
- 上下文限制：当前接口需在主线程调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |
| send_msg | uint32_t | 指定发送的消息号 | 0 ~ 31 |
| clear_msg | uint32_t | 指定清除的消息号 | 0 ~ 31 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 清除并发送成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### uapi_sdio_slave_is_pending_msg <a id="uapi_sdio_slave_is_pending_msg"></a>

```c
bool uapi_sdio_slave_is_pending_msg(sdio_bus_t bus, uint32_t msg)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 判断指定 SDIO 通道是否挂起指定消息
- 返回布尔判定结果

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |
| msg | uint32_t | 给定消息号 | 0 ~ 31 |

**返回值**

- 返回类型：bool

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| true | 指定消息处于挂起状态 | 消息挂起 |
| false | 指定消息不处于挂起状态 | 消息未挂起 |

### uapi_sdio_slave_is_sending_msg <a id="uapi_sdio_slave_is_sending_msg"></a>

```c
bool uapi_sdio_slave_is_sending_msg(sdio_bus_t bus, uint32_t msg)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 判断指定 SDIO 通道是否正在发送指定消息
- 返回布尔判定结果

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |
| msg | uint32_t | 给定消息号 | 0 ~ 31 |

**返回值**

- 返回类型：bool

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| true | 指定消息处于发送状态 | 消息正在发送 |
| false | 指定消息不处于发送状态 | 消息未在发送 |

### uapi_sdio_slave_register_notify_message_callback <a id="uapi_sdio_slave_register_notify_message_callback"></a>

```c
void uapi_sdio_slave_register_notify_message_callback(notify_host_event_t event_callback)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 注册通知 HOST 消息或数据事件发生的回调函数
- 回调在发送消息或数据时被调用

**前置条件**

- 调用时序约束：当前接口需在 SDIO 通道初始化前或初始化后均可调用
- 依赖关系：当前接口依赖回调函数已实现

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| event_callback | [notify_host_event_t](#notify_host_event_t) | 消息或数据发送时调用的回调函数，参考 [notify_host_event_t](#notify_host_event_t) | 不为NULL |

### uapi_sdio_slave_read_retry_when_read_err <a id="uapi_sdio_slave_read_retry_when_read_err"></a>

```c
void uapi_sdio_slave_read_retry_when_read_err(sdio_bus_t bus, uint32_t read_bytes)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 在 SDIO 读错误事件存在时尝试重新读取

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化
- 上下文限制：当前接口需在主线程调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |
| read_bytes | uint32_t | 读取的数据长度 | 0 ~ 4294967295 |

### uapi_sdio_slave_init_no_wait <a id="uapi_sdio_slave_init_no_wait"></a>

```c
void uapi_sdio_slave_init_no_wait(sdio_bus_t bus)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 以非阻塞方式初始化指定 SDIO 通道

**前置条件**

- 调用时序约束：当前接口需在 SDIO 硬件资源就绪后调用
- 依赖关系：当前接口依赖 SDIO 总线硬件已就绪
- 上下文限制：当前接口需在主线程调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |

### uapi_sdio_slave_host_clk_ready <a id="uapi_sdio_slave_host_clk_ready"></a>

```c
bool uapi_sdio_slave_host_clk_ready(sdio_bus_t bus)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 判断指定 SDIO 通道的 HOST 时钟是否就绪
- 返回布尔判定结果

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |

**返回值**

- 返回类型：bool

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| true | HOST 时钟准备就绪 | 时钟就绪 |
| false | HOST 时钟未准备就绪 | 时钟未就绪 |

### uapi_sdio_slave_get_status <a id="uapi_sdio_slave_get_status"></a>

```c
errcode_t uapi_sdio_slave_get_status(sdio_bus_t bus, sdio_status_info_t* satus_info)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 获取指定 SDIO 通道的当前状态信息
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化
- 上下文限制：当前接口需在主线程调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| satus_info | [sdio_status_info_t](#sdio_status_info_t) * | 存储状态信息的缓冲区指针，由调用方分配、函数填充，参考 [sdio_status_info_t](#sdio_status_info_t) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 获取成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**参考案例**

- `src/drivers/chips/ws53/rom/app/middleware/utils/hcc/acore/slave/hcc_sdio_device.c`

### uapi_sdio_slave_set_status <a id="uapi_sdio_slave_set_status"></a>

```c
errcode_t uapi_sdio_slave_set_status(sdio_bus_t bus, const sdio_status_info_t* satus_info)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 设置指定 SDIO 通道的当前状态信息
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化
- 上下文限制：当前接口需在主线程调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |
| satus_info | const [sdio_status_info_t](#sdio_status_info_t) * | 指向存储状态信息缓冲区的指针，参考 [sdio_status_info_t](#sdio_status_info_t) | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 设置成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**参考案例**

- `src/drivers/chips/ws53/rom/app/middleware/utils/hcc/acore/slave/hcc_sdio_device.c`

### uapi_sdio_slave_memory_init <a id="uapi_sdio_slave_memory_init"></a>

```c
void uapi_sdio_slave_memory_init(sdio_bus_t bus)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 执行指定 SDIO 通道的内存初始化

**前置条件**

- 调用时序约束：当前接口需在 SDIO 通道初始化前或初始化早期调用
- 依赖关系：当前接口依赖 SDIO 内存资源已分配

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |

**参考案例**

- `src/drivers/chips/ws53/rom/app/middleware/utils/hcc/acore/slave/hcc_sdio_device.c`

### uapi_sdio_slave_get_info <a id="uapi_sdio_slave_get_info"></a>

```c
sdio_info_t* uapi_sdio_slave_get_info(sdio_bus_t bus)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 获取指定 SDIO 通道的状态信息结构体指针
- 返回 SDIO 信息结构体指针

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |

**返回值**

- 返回类型：sdio_info_t *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非 NULL | SDIO 信息结构体指针，参考 [sdio_info_t](#sdio_info_t) | 获取成功 |
| NULL | 获取失败 | 信息不可用 |

### uapi_sdio_slave_set_extend_val_info <a id="uapi_sdio_slave_set_extend_val_info"></a>

```c
void uapi_sdio_slave_set_extend_val_info(sdio_bus_t bus, uint32_t offset, uint32_t val)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 向指定 SDIO 通道的扩展信息指定地址偏移写入值

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |
| offset | uint32_t | 地址偏移量 | 0 ~ 4294967295 |
| val | uint32_t | 设置的值 | 0 ~ 4294967295 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SDIO_EXTEND_INFO | 特性宏 | 支持 SDIO 扩展信息读写接口功能（接口级） | n |

### uapi_sdio_slave_get_extend_val_info <a id="uapi_sdio_slave_get_extend_val_info"></a>

```c
uint32_t uapi_sdio_slave_get_extend_val_info(sdio_bus_t bus, uint32_t offset)
```

**头文件清单**

```c
#include "include/driver/sdio/sdio_slave.h"
```

**功能说明**

- 获取指定 SDIO 通道扩展信息指定地址偏移的值
- 返回扩展信息地址对应的值

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_sdio_slave_init](#uapi_sdio_slave_init) 成功返回后调用
- 依赖关系：当前接口依赖 SDIO 通道已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [sdio_bus_t](#sdio_bus_t) | SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t) | [SDIO_BUS_0](#sdio_bus_t)(0) |
| offset | uint32_t | 地址偏移量 | 0 ~ 4294967295 |

**返回值**

- 返回类型：uint32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 扩展信息地址的值 | 获取成功 | 读取扩展信息偏移对应的值 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SDIO_EXTEND_INFO | 特性宏 | 支持 SDIO 扩展信息读写接口功能（接口级） | n |

## Type definitions

### errcode_t <a id="typedef_errcode_t"></a> 
```c
// 源码原始定义
typedef uint32_t errcode_t;
```

**使用说明**

作为本模块多个对外接口（如 [uapi_sdio_slave_init](#uapi_sdio_slave_init)、[uapi_sdio_slave_register_callback](#uapi_sdio_slave_register_callback) 等）的返回值类型，表示接口执行结果状态码。 
### notify_host_event_t <a id="notify_host_event_t"></a>

```c
// 源码原始定义
typedef void (*notify_host_event_t)(sdio_bus_t bus);
```

**使用说明**

- 作为 [uapi_sdio_slave_register_notify_message_callback](#uapi_sdio_slave_register_notify_message_callback) 的入参类型，用于通知 HOST 消息或数据事件发生的回调函数。
- 回调参数 bus 透传 SDIO 通道号，参考 [sdio_bus_t](#sdio_bus_t)。
- 回调返回 void，调用方注册后由 SDIO 发送消息或数据时触发调用。

## Enumerations

### sdio_bus_t <a id="sdio_bus_t"></a>

```c
// 源码原始定义
typedef enum sdio_bus {
    SDIO_BUS_0,             /*!< SDIO Bus 0 */
    SDIO_BUS_MAX_NUM
} sdio_bus_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SDIO_BUS_0 | 0 | SDIO Bus 0 |
| SDIO_BUS_MAX_NUM | 1 | SDIO 总线数量上限 |

### sdio_channel_t <a id="sdio_channel_t"></a>

```c
// 源码原始定义
typedef enum {
    SDIO_CHANNEL_ERR    = 0x0,          /*!< SDIO err. */
    SDIO_CHANNEL_RESET,                 /*!< Reset SDIO. */
    SDIO_CHANNEL_INIT,                  /*!< Initialize the SDIO. */
    SDIO_CHANNEL_SLEEP,                 /*!< Sleep the SDIO. */
    SDIO_CHANNEL_WAKE,                  /*!< Wake the SDIO. */
    SDIO_CHANNEL_WORK,                  /*!< SDIO work. */
    SDIO_CHANNEL_BUTT                   /*!< SDIO status number. */
} sdio_channel_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SDIO_CHANNEL_ERR | 0x0 | SDIO 错误 |
| SDIO_CHANNEL_RESET | 0x1 | 重置 SDIO |
| SDIO_CHANNEL_INIT | 0x2 | 初始化 SDIO |
| SDIO_CHANNEL_SLEEP | 0x3 | SDIO 睡眠状态 |
| SDIO_CHANNEL_WAKE | 0x4 | 唤醒 SDIO |
| SDIO_CHANNEL_WORK | 0x5 | SDIO 工作状态 |
| SDIO_CHANNEL_BUTT | 0x6 | SDIO 状态枚举数 |

## Structures

### sdio_msg_t <a id="sdio_msg_t"></a>

```c
// 源码原始定义
typedef struct sdio_msg {
    uint32_t pending_msg;                       /*!< Pending message. */
    uint32_t sending_msg;                       /*!< Sending message. */
} sdio_msg_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| pending_msg | uint32_t | 挂起中的消息 |
| sending_msg | uint32_t | 发送中的消息 |

### sdio_status_info_t <a id="sdio_status_info_t"></a>

```c
// 源码原始定义
typedef struct sdio_status_info {
    uint8_t     allow_sleep;                    /*!< Allow sleep. */
    uint8_t     tx_status;                      /*!< Tx status. */
    uint8_t     sleep_status;                   /*!< Sleep status. */
    sdio_channel_t  work_status;         /*!< Work status. */
} sdio_status_info_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| allow_sleep | uint8_t | 允许睡眠 |
| tx_status | uint8_t | tx 状态 |
| sleep_status | uint8_t | 睡眠状态 |
| work_status | [sdio_channel_t](#sdio_channel_t) | 工作状态 |

### sdio_extendfunc_t <a id="sdio_extendfunc_t"></a>

```c
// 源码原始定义
typedef struct sdio_extendfunc {
    uint32_t                   int_stat;
    uint32_t                   msg_stat;
    uint32_t                   xfer_count;
    uint32_t                   credit_info;
    uint8_t                    comm_reg[SDIO_EXTENDREG_COUNT];
    int32_t                    valid_commreg_cnt;
    int8_t                     commreg_isvalid;
    int8_t                     credit_isvalid;
} sdio_extendfunc_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| int_stat | uint32_t | 中断状态 |
| msg_stat | uint32_t | 消息状态 |
| xfer_count | uint32_t | 传输计数 |
| credit_info | uint32_t | credit 信息 |
| comm_reg | uint8_t[[SDIO_EXTENDREG_COUNT](#SDIO_EXTENDREG_COUNT)] | 通信寄存区 |
| valid_commreg_cnt | int32_t | 有效通信寄存数量 |
| commreg_isvalid | int8_t | 通信寄存有效标志 |
| credit_isvalid | int8_t | credit 有效标志 |

### sdio_status_t <a id="sdio_status_t"></a>

```c
// 源码原始定义
typedef struct sdio_status {
    uint16_t          rd_arg_invalid_cnt;
    uint16_t          wr_arg_invlaid_cnt;
    uint16_t          unsupport_int_cnt;
    uint16_t          mem_int_cnt;
    uint16_t          fn1_wr_over;
    uint16_t          fn1_rd_over;
    uint16_t          fn1_rd_error;
    uint16_t          fn1_rd_start;
    uint16_t          fn1_wr_start;
    uint16_t          fn1_rst;
    uint16_t          fn1_msg_rdy;
    uint16_t          fn1_ack_to_arm_int_cnt;
    uint16_t          fn1_adma_end_int;
    uint16_t          fn1_suspend;
    uint16_t          fn1_resume;
    uint16_t          fn1_adma_int;
    uint16_t          fn1_adma_err;
    uint16_t          fn1_en_int;
    uint16_t          fn1_msg_isr;
    uint16_t          soft_reset_cnt;
} sdio_status_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| rd_arg_invalid_cnt | uint16_t | 读参数非法计数 |
| wr_arg_invlaid_cnt | uint16_t | 写参数非法计数 |
| unsupport_int_cnt | uint16_t | 不支持中断计数 |
| mem_int_cnt | uint16_t | 内存中断计数 |
| fn1_wr_over | uint16_t | function 1 写完成计数 |
| fn1_rd_over | uint16_t | function 1 读完成计数 |
| fn1_rd_error | uint16_t | function 1 读错误计数 |
| fn1_rd_start | uint16_t | function 1 读开始计数 |
| fn1_wr_start | uint16_t | function 1 写开始计数 |
| fn1_rst | uint16_t | function 1 复位计数 |
| fn1_msg_rdy | uint16_t | function 1 消息就绪计数 |
| fn1_ack_to_arm_int_cnt | uint16_t | function 1 ack 到 ARM 中断计数 |
| fn1_adma_end_int | uint16_t | function 1 ADMA 结束中断计数 |
| fn1_suspend | uint16_t | function 1 挂起计数 |
| fn1_resume | uint16_t | function 1 恢复计数 |
| fn1_adma_int | uint16_t | function 1 ADMA 中断计数 |
| fn1_adma_err | uint16_t | function 1 ADMA 错误计数 |
| fn1_en_int | uint16_t | function 1 使能中断计数 |
| fn1_msg_isr | uint16_t | function 1 消息中断服务计数 |
| soft_reset_cnt | uint16_t | 软复位计数 |

### sdio_chan_info_t <a id="sdio_chan_info_t"></a>

```c
// 源码原始定义
typedef struct sdio_chan_info {
    uint32_t                 send_data_len;
    uint16_t                 last_msg;
    uint16_t                 panic_forced_timeout;
    uint16_t                 chan_msg_cnt[D2H_MSG_COUNT];
} sdio_chan_info_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| send_data_len | uint32_t | 发送数据长度 |
| last_msg | uint16_t | 最近一次消息号 |
| panic_forced_timeout | uint16_t | panic 强制超时 |
| chan_msg_cnt | uint16_t[[D2H_MSG_COUNT](#D2H_MSG_COUNT)] | 通道消息计数 |

### sdio_info_t <a id="sdio_info_t"></a>

```c
// 源码原始定义
typedef struct sdio_info {
    uint8_t                 volt_switch_flag;

    uint8_t                 host_to_device_msg_flag;

    uint16_t                reinit_times;
    uint16_t                gpio_int_times;
    uint16_t                pad;
    sdio_status_t           sdio_status;
    sdio_chan_info_t        chan_info;
    sdio_msg_t         sdio_msg_status;
} sdio_info_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| volt_switch_flag | uint8_t | 电压切换标志 |
| host_to_device_msg_flag | uint8_t | HOST 到 DEVICE 消息标志 |
| reinit_times | uint16_t | 重新初始化次数 |
| gpio_int_times | uint16_t | GPIO 中断次数 |
| pad | uint16_t | 填充字段 |
| sdio_status | [sdio_status_t](#sdio_status_t) | SDIO 状态 |
| chan_info | [sdio_chan_info_t](#sdio_chan_info_t) | SDIO 传输通道信息 |
| sdio_msg_status | [sdio_msg_t](#sdio_msg_t) | SDIO 消息状态 |

### sdio_callback_func_t <a id="sdio_callback_func_t"></a>

```c
// 源码原始定义
typedef struct sdio_callback_func {
    uint32_t (*read_start_callback)(uint32_t len, uint8_t *dma_tbl);    /*!< HOST reading. */
    uint32_t (*read_over_callback)(void);                               /*!< HOST reading over. */
    void (*read_err_callback)(void);                                    /*!< HOST read error. */
    uint32_t (*write_start_callback)(uint32_t len, uint8_t *dma_tbl);   /*!< HOST writting. */
    uint32_t (*write_over_callback)(void);                              /*!< HOST write over. */
    void (*process_msg_callback)(uint32_t);                             /*!< HOST getting message. */
    void (*soft_rst_callback)(void);                                    /*!< HOST getting reset interruption. */
} sdio_callback_func_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| read_start_callback | uint32_t (*)(uint32_t len, uint8_t *dma_tbl) | DEVICE 感知到 HOST 发起读操作时调用，参数为读取长度与 DMA 表 |
| read_over_callback | uint32_t (*)(void) | DEVICE 感知到 HOST 读操作结束时调用 |
| read_err_callback | void (*)(void) | DEVICE 感知到 HOST 读数据错误时调用 |
| write_start_callback | uint32_t (*)(uint32_t len, uint8_t *dma_tbl) | DEVICE 感知到 HOST 发起写操作时调用，参数为写入长度与 DMA 表 |
| write_over_callback | uint32_t (*)(void) | DEVICE 感知到 HOST 写操作结束时调用 |
| process_msg_callback | void (*)(uint32_t) | DEVICE 接收到 HOST 发来的消息时调用，参数为消息号 |
| soft_rst_callback | void (*)(void) | DEVICE 接收到 HOST 发来的软复位时调用 |

## Macros

### SDIO_EXTENDREG_COUNT <a id="SDIO_EXTENDREG_COUNT"></a>

```c
#define SDIO_EXTENDREG_COUNT        64
```

### D2H_MSG_COUNT <a id="D2H_MSG_COUNT"></a>

```c
#define D2H_MSG_COUNT 32
```
