# UART

UART（Universal Asynchronous Receiver/Transmitter）提供串口的初始化、去初始化、属性配置与查询、收发数据（轮询、中断、DMA（Direct Memory Access））、接收回调注册、错误回调注册、FIFO（First In First Out）状态查询及低功耗挂起与恢复能力。

**模块公共头文件**

```c
#include "include/driver/uart.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_uart_init](#uapi_uart_init) | 初始化指定的串口，配置引脚、基础属性、扩展属性与接收缓存 |
| [uapi_uart_deinit](#uapi_uart_deinit) | 去初始化指定的串口，释放引脚与状态资源 |
| [uapi_uart_set_attr](#uapi_uart_set_attr) | 设置指定串口的基础配置参数（波特率、数据位、停止位、校验位、流控） |
| [uapi_uart_get_attr](#uapi_uart_get_attr) | 获取指定串口当前的基础配置参数 |
| [uapi_uart_has_pending_transmissions](#uapi_uart_has_pending_transmissions) | 判断指定串口是否存在正在等待或正在进行的传输 |
| [uapi_uart_rx_fifo_is_empty](#uapi_uart_rx_fifo_is_empty) | 判断指定串口的接收 FIFO 是否为空 |
| [uapi_uart_tx_fifo_is_empty](#uapi_uart_tx_fifo_is_empty) | 判断指定串口的发送 FIFO 是否为空 |
| [uapi_uart_register_rx_callback](#uapi_uart_register_rx_callback) | 注册接收数据回调，按指定触发条件与数据长度触发 |
| [uapi_uart_unregister_rx_callback](#uapi_uart_unregister_rx_callback) | 注销已注册的接收数据回调，并刷新接收 FIFO 中的数据 |
| [uapi_uart_register_parity_error_callback](#uapi_uart_register_parity_error_callback) | 注册奇偶校验错误处理回调 |
| [uapi_uart_register_frame_error_callback](#uapi_uart_register_frame_error_callback) | 注册帧错误处理回调 |
| [uapi_uart_register_overrun_error_callback](#uapi_uart_register_overrun_error_callback) | 注册溢出错误处理回调 |
| [uapi_uart_write](#uapi_uart_write) | 以轮询方式向指定串口发送数据 |
| [uapi_uart_write_nolock](#uapi_uart_write_nolock) | 以轮询方式向指定串口发送数据，发送过程不锁中断 |
| [uapi_uart_write_int](#uapi_uart_write_int) | 以中断方式向指定串口发送数据，发送完成后触发回调 |
| [uapi_uart_write_by_dma](#uapi_uart_write_by_dma) | 通过 DMA 向指定串口发送数据 |
| [uapi_uart_read_by_dma](#uapi_uart_read_by_dma) | 通过 DMA 从指定串口读取数据 |
| [uapi_uart_register_read_by_dma_callback](#uapi_uart_register_read_by_dma_callback) | 注册接收中断触发 DMA 搬运数据的回调配置 |
| [uapi_uart_unregister_read_by_dma_callback](#uapi_uart_unregister_read_by_dma_callback) | 注销接收中断触发 DMA 搬运数据的回调配置 |
| [uapi_uart_recv_raw_data_end_transfer](#uapi_uart_recv_raw_data_end_transfer) | 结束 UART 的不定长数据 DMA 接收 |
| [uapi_uart_dma_recv_raw_data](#uapi_uart_dma_recv_raw_data) | 启动 UART DMA 不定长数据接收，并在接收完成时触发回调 |
| [uapi_uart_read](#uapi_uart_read) | 从指定串口以轮询方式读取数据 |
| [uapi_uart_update_rx_buff](#uapi_uart_update_rx_buff) | 更新指定串口接收缓存的地址和长度 |
| [uapi_uart_suspend](#uapi_uart_suspend) | 挂起所有已初始化的 UART 通道 |
| [uapi_uart_resume](#uapi_uart_resume) | 恢复所有已挂起的 UART 通道 |
| [uapi_uart_register_write_by_dma_callback](#uapi_uart_register_write_by_dma_callback) | 注册在 UART DMA 发送完成中断中直接进行 DMA 写的回调 |

## Functions

### uapi_uart_init <a id="uapi_uart_init"></a>

```c
errcode_t uapi_uart_init(uart_bus_t bus, const uart_pin_config_t *pins, const uart_attr_t *attr, const uart_extra_attr_t *extra_attr, uart_buffer_config_t *uart_buffer_config)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 初始化指定的 UART 串口，配置引脚、基础属性、扩展属性和接收缓冲区。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |
| pins | const [uart_pin_config_t](#uart_pin_config_t) * | UART 的引脚配置（TX/RX/RTS/CTS） | 不为 NULL |
| attr | const [uart_attr_t](#uart_attr_t) * | 基础属性配置结构体指针 | 不为 NULL |
| extra_attr | const [uart_extra_attr_t](#uart_extra_attr_t) * | 扩展属性配置结构体指针 | 可为 NULL |
| uart_buffer_config | [uart_buffer_config_t](#uart_buffer_config_t) * | 接收缓冲区配置结构体指针 | - |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 成功初始化 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 初始化失败 |

**参考案例**

- `src/application/samples/peripheral/uart/uart_demo.c`
- `src/application/samples/bt/sle/sle_uart/sle_uart.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_TX | 特性宏 | 启用 UART 发送支持 | y |
| CONFIG_UART_SUPPORT_RX | 特性宏 | 启用 UART 接收支持 | y |
| CONFIG_UART_SUPPORT_DMA | 特性宏 | 启用 UART DMA 支持 | y |

### uapi_uart_deinit <a id="uapi_uart_deinit"></a>

```c
errcode_t uapi_uart_deinit(uart_bus_t bus)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 去初始化指定的 UART 串口，释放资源。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 成功去初始化 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 去初始化失败 |

**参考案例**

- `src/application/samples/peripheral/uart/uart_demo.c`
- `src/application/samples/bt/sle/sle_uart/sle_uart.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_RX | 特性宏 | 启用 UART 接收支持 | y |
| CONFIG_UART_SUPPORT_TX | 特性宏 | 启用 UART 发送支持 | y |
| CONFIG_UART_SUPPORT_DMA | 特性宏 | 启用 UART DMA 支持 | y |


### uapi_uart_get_attr <a id="uapi_uart_get_attr"></a>

```c
errcode_t uapi_uart_get_attr(uart_bus_t bus, const uart_attr_t *attr)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 获取 UART 当前基础配置参数。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |
| attr | const [uart_attr_t](#uart_attr_t) * | 用于接收当前基础配置的结构体指针（注意：源码签名使用 const 限定，实际无法通过该参数返回配置数据） | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 成功获取 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 获取失败 |

### uapi_uart_has_pending_transmissions <a id="uapi_uart_has_pending_transmissions"></a>

```c
bool uapi_uart_has_pending_transmissions(uart_bus_t bus)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 判断指定 UART 是否存在正在等待发送的数据。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |

**返回值**

返回类型：bool

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| true | 存在正在等待的传输 | 总线存在待发送数据 |
| false | 无正在等待的传输 | 总线无待发送数据 |

### uapi_uart_rx_fifo_is_empty <a id="uapi_uart_rx_fifo_is_empty"></a>

```c
bool uapi_uart_rx_fifo_is_empty(uart_bus_t bus)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 判断指定 UART 的接收 FIFO 是否为空。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |

**返回值**

返回类型：bool

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| true | RX FIFO 为空 | 接收 FIFO 为空 |
| false | RX FIFO 非空 | 接收 FIFO 非空 |

### uapi_uart_tx_fifo_is_empty <a id="uapi_uart_tx_fifo_is_empty"></a>

```c
bool uapi_uart_tx_fifo_is_empty(uart_bus_t bus)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 判断指定 UART 的发送 FIFO 是否为空。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |

**返回值**

返回类型：bool

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| true | TX FIFO 为空 | 发送 FIFO 为空 |
| false | TX FIFO 非空 | 发送 FIFO 非空 |

### uapi_uart_set_attr <a id="uapi_uart_set_attr"></a>

```c
errcode_t uapi_uart_set_attr(uart_bus_t bus, const uart_attr_t *attr)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 设置 UART 基础配置参数，包括波特率、数据位、校验位、停止位等。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |
| attr | const [uart_attr_t](#uart_attr_t) * | 基础属性配置结构体指针 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC(0) | 成功 | 成功设置 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 设置失败 |

### uapi_uart_register_rx_callback <a id="uapi_uart_register_rx_callback"></a>

```c
errcode_t uapi_uart_register_rx_callback(uart_bus_t bus, uart_rx_condition_t condition, uint32_t size, uart_rx_callback_t callback)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 注册接收数据回调函数，回调会根据触发条件和数据长度触发，运行于中断上下文。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。
- 使用中断模式或 DMA 模式。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |
| condition | [uart_rx_condition_t](#uart_rx_condition_t) | 回调触发的条件 | 见枚举定义 |
| size | uint32_t | 触发条件涉及长度时表示所需的数据长度 | - |
| callback | [uart_rx_callback_t](#uart_rx_callback_t) | 接收数据的回调函数 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 成功注册 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 注册失败 |

**参考案例**

- `src/application/samples/peripheral/uart/uart_demo.c`
- `src/application/samples/bt/sle/sle_uart/sle_uart.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_RX | 特性宏 | 启用 UART 接收支持 | y |

### uapi_uart_unregister_rx_callback <a id="uapi_uart_unregister_rx_callback"></a>

```c
void uapi_uart_unregister_rx_callback(uart_bus_t bus)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 去注册 UART 接收数据回调函数。

**前置条件**

- 已调用 `uapi_uart_register_rx_callback` 注册回调。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_RX | 特性宏 | 启用 UART 接收支持 | y |

### uapi_uart_register_parity_error_callback <a id="uapi_uart_register_parity_error_callback"></a>

```c
errcode_t uapi_uart_register_parity_error_callback(uart_bus_t bus, uart_error_callback_t callback)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 注册奇偶校验错误处理回调函数，当 UART 检测到奇偶校验错误时触发回调，运行于中断上下文。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。
- 配置了奇偶校验功能。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |
| callback | [uart_error_callback_t](#uart_error_callback_t) | 奇偶校验错误处理回调函数 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 成功注册 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 注册失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_RX | 特性宏 | 启用 UART 接收支持 | y |

### uapi_uart_register_frame_error_callback <a id="uapi_uart_register_frame_error_callback"></a>

```c
errcode_t uapi_uart_register_frame_error_callback(uart_bus_t bus, uart_error_callback_t callback)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 注册帧错误处理回调函数，当 UART 检测到帧错误时触发回调，运行于中断上下文。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |
| callback | [uart_error_callback_t](#uart_error_callback_t) | 帧错误处理回调函数 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 成功注册 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 注册失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_RX | 特性宏 | 启用 UART 接收支持 | y |

### uapi_uart_register_overrun_error_callback <a id="uapi_uart_register_overrun_error_callback"></a>

```c
errcode_t uapi_uart_register_overrun_error_callback(uart_bus_t bus, uart_error_callback_t callback)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 注册溢出错误处理回调函数，当 UART 检测到溢出错误时触发回调，运行于中断上下文。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |
| callback | [uart_error_callback_t](#uart_error_callback_t) | 溢出错误处理回调函数 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 成功注册 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 注册失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_RX | 特性宏 | 启用 UART 接收支持 | y |

### uapi_uart_write <a id="uapi_uart_write"></a>

```c
int32_t uapi_uart_write(uart_bus_t bus, const uint8_t *buffer, uint32_t length, uint32_t timeout)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 以轮询（直接发送）方式将数据发送到已打开的 UART 上。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |
| buffer | const uint8_t * | 要发送的数据 Buffer | 不为 NULL |
| length | uint32_t | 要发送的数据 Buffer 长度（字节） | - |
| timeout | uint32_t | 超时时间（ms） | - |

**返回值**

返回类型：int32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| >=0 | 实际发送到 UART 的数据长度（字节） | 发送完成 |
| <0 | 错误码，参考[errcode_t](#errcode_t) | 发送失败 |

**参考案例**

- `src/application/samples/peripheral/uart/uart_demo.c`
- `src/application/samples/bt/sle/sle_uart/sle_uart.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_TX | 特性宏 | 启用 UART 发送支持 | y |

### uapi_uart_write_nolock <a id="uapi_uart_write_nolock"></a>

```c
int32_t uapi_uart_write_nolock(uart_bus_t bus, const uint8_t *buffer, uint32_t length, uint32_t timeout)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 以轮询（直接发送）方式将数据发送到已打开的 UART 上，发送过程不锁中断。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |
| buffer | const uint8_t * | 要发送的数据 Buffer | 不为 NULL |
| length | uint32_t | 要发送的数据 Buffer 长度（字节） | - |
| timeout | uint32_t | 超时时间（ms） | - |

**返回值**

返回类型：int32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| >=0 | 实际发送到 UART 的数据长度（字节） | 发送完成 |
| <0 | 错误码，参考[errcode_t](#errcode_t) | 发送失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_TX | 特性宏 | 启用 UART 发送支持 | y |

### uapi_uart_write_int <a id="uapi_uart_write_int"></a>

```c
errcode_t uapi_uart_write_int(uart_bus_t bus, const uint8_t *buffer, uint32_t length, void *params, uart_tx_callback_t finished_with_buffer_func)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 以中断模式将数据发送到已打开的 UART 上，发送完成后调用回调函数（运行于中断上下文）。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。
- 使用中断模式。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |
| buffer | const uint8_t * | 要发送的数据 Buffer | 不为 NULL |
| length | uint32_t | 要发送的数据 Buffer 长度（字节） | - |
| params | void * | 传递到完成传输回调函数的参数 | 可为 NULL |
| finished_with_buffer_func | [uart_tx_callback_t](#uart_tx_callback_t) | 数据发送完成的回调函数 | 可为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 成功发送 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 发送失败 |

**参考案例**

- `src/application/samples/peripheral/uart/uart_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_TX | 特性宏 | 启用 UART 发送支持 | y |
| CONFIG_UART_SUPPORT_TX_INT | 特性宏 | 支持 UART 中断发送 | y |

### uapi_uart_write_by_dma <a id="uapi_uart_write_by_dma"></a>

```c
int32_t uapi_uart_write_by_dma(uart_bus_t bus, const void *buffer, uint32_t length, uart_write_dma_config_t *dma_cfg)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 通过 DMA 将数据发送到 UART。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。
- 使用 DMA 模式。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |
| buffer | const void * | 要发送的数据 Buffer | 不为 NULL |
| length | uint32_t | 要发送的数据 Buffer 长度（字节） | - |
| dma_cfg | [uart_write_dma_config_t](#uart_write_dma_config_t) * | 发送数据时的 DMA 配置 | 不为 NULL |

**返回值**

返回类型：int32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| >=0 | 完成发送的数据长度（字节） | 发送完成 |
| <0 | 错误码，参考[errcode_t](#errcode_t) | 发送失败 |

**参考案例**

- `src/application/samples/peripheral/uart/uart_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_TX | 特性宏 | 启用 UART 发送支持 | y |
| CONFIG_UART_SUPPORT_DMA | 特性宏 | 启用 UART DMA 支持 | y |

### uapi_uart_read_by_dma <a id="uapi_uart_read_by_dma"></a>

```c
int32_t uapi_uart_read_by_dma(uart_bus_t bus, const void *buffer, uint32_t length, uart_write_dma_config_t *dma_cfg)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 通过 DMA 从 UART 读取数据。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。
- 使用 DMA 模式。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |
| buffer | const void * | 存储接收数据的 Buffer | 不为 NULL |
| length | uint32_t | 存储接收数据的 Buffer 长度（字节） | - |
| dma_cfg | [uart_write_dma_config_t](#uart_write_dma_config_t) * | 接收数据时的 DMA 配置 | 不为 NULL |

**返回值**

返回类型：int32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| >=0 | 完成接收的数据长度（字节） | 接收完成 |
| <0 | 错误码，参考[errcode_t](#errcode_t) | 接收失败 |

**参考案例**

- `src/application/samples/peripheral/uart/uart_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_TX | 特性宏 | 启用 UART 发送支持 | y |
| CONFIG_UART_SUPPORT_DMA | 特性宏 | 启用 UART DMA 支持 | y |

### uapi_uart_register_read_by_dma_callback <a id="uapi_uart_register_read_by_dma_callback"></a>

```c
errcode_t uapi_uart_register_read_by_dma_callback(uart_bus_t bus, uart_write_dma_config_t *dma_cfg)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 注册接收中断触发 DMA 搬运数据的回调配置。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | 串口号 | 有效 UART 总线 |
| dma_cfg | [uart_write_dma_config_t](#uart_write_dma_config_t) * | 接收数据时使用的 DMA 配置 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| ---- | ---- | ---- |
| ERRCODE_SUCC：0 | 成功 | 成功注册 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 注册失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_TX | 特性宏 | 支持 UART 发送功能（接口级，嵌套包裹接口声明） | y |
| CONFIG_UART_SUPPORT_DMA | 特性宏 | 支持 UART DMA 传输功能（接口级，嵌套包裹接口声明） | y |
| CONFIG_UART_SUPPORT_INT_TRIGGER_DMA | 特性宏 | 支持中断触发 DMA 功能（接口级，嵌套包裹接口声明） | y |

### uapi_uart_unregister_read_by_dma_callback <a id="uapi_uart_unregister_read_by_dma_callback"></a>

```c
void uapi_uart_unregister_read_by_dma_callback(uart_bus_t bus)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 注销接收中断触发 DMA 搬运数据的回调配置。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | 串口号 | 有效 UART 总线 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_TX | 特性宏 | 支持 UART 发送功能（接口级，嵌套包裹接口声明） | y |
| CONFIG_UART_SUPPORT_DMA | 特性宏 | 支持 UART DMA 传输功能（接口级，嵌套包裹接口声明） | y |
| CONFIG_UART_SUPPORT_INT_TRIGGER_DMA | 特性宏 | 支持中断触发 DMA 功能（接口级，嵌套包裹接口声明） | y |

### uapi_uart_recv_raw_data_end_transfer <a id="uapi_uart_recv_raw_data_end_transfer"></a>

```c
errcode_t uapi_uart_recv_raw_data_end_transfer(uart_bus_t uart_bus)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 结束 UART 的不定长数据 DMA 接收。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| uart_bus | [uart_bus_t](#uart_bus_t) | 串口号 | 有效 UART 总线，小于 UART_BUS_MAX_NUM |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 成功结束 DMA 不定长接收 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM)：0x80000001 | 参数无效 | uart_bus 越界 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_TX | 特性宏 | 支持 UART 发送功能（接口级，嵌套包裹接口声明） | y |
| CONFIG_UART_SUPPORT_DMA | 特性宏 | 支持 UART DMA 传输功能（接口级，嵌套包裹接口声明） | y |
| CONFIG_UART_SUPPORT_DMA_LLI | 特性宏 | 支持 DMA 链表传输功能（接口级，嵌套包裹接口声明） | n |
| CONFIG_UART_SUPPORT_RECV_RAW_DATA | 特性宏 | 支持不定长数据接收功能（接口级，嵌套包裹接口声明） | n |

### uapi_uart_dma_recv_raw_data <a id="uapi_uart_dma_recv_raw_data"></a>

```c
errcode_t uapi_uart_dma_recv_raw_data(uart_bus_t uart_bus, uart_idle_int_receive_cb_t callback)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 启动 UART DMA 不定长数据接收，并在接收完成时触发回调。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| uart_bus | [uart_bus_t](#uart_bus_t) | 串口号 | 有效 UART 总线，小于 UART_BUS_MAX_NUM |
| callback | [uart_idle_int_receive_cb_t](#uart_idle_int_receive_cb_t) | 接收完成后触发的 IDLE 回调 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | DMA 不定长接收启动成功 |
| [ERRCODE_FAIL](#ERRCODE_FAIL)：0xFFFFFFFF | 执行失败 | 配置或启动 DMA 接收失败 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_TX | 特性宏 | 支持 UART 发送功能（接口级，嵌套包裹接口声明） | y |
| CONFIG_UART_SUPPORT_DMA | 特性宏 | 支持 UART DMA 传输功能（接口级，嵌套包裹接口声明） | y |
| CONFIG_UART_SUPPORT_DMA_LLI | 特性宏 | 支持 DMA 链表传输功能（接口级，嵌套包裹接口声明） | n |
| CONFIG_UART_SUPPORT_RECV_RAW_DATA | 特性宏 | 支持不定长数据接收功能（接口级，嵌套包裹接口声明） | n |

### uapi_uart_read <a id="uapi_uart_read"></a>

```c
int32_t uapi_uart_read(uart_bus_t bus, const uint8_t *buffer, uint32_t length, uint32_t timeout)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 以轮询模式从 UART 读取数据。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |
| buffer | const uint8_t * | 存储接收数据的 Buffer | 不为 NULL |
| length | uint32_t | 存储接收数据的 Buffer 长度（字节） | - |
| timeout | uint32_t | 超时时间（ms） | - |

**返回值**

返回类型：int32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| >=0 | 实际读到的数据长度（字节） | 读取完成 |
| <0 | 错误码，参考[errcode_t](#errcode_t) | 读取失败 |

**参考案例**

- `src/application/samples/peripheral/uart/uart_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_RX | 特性宏 | 启用 UART 接收支持 | y |

### uapi_uart_update_rx_buff <a id="uapi_uart_update_rx_buff"></a>

```c
errcode_t uapi_uart_update_rx_buff(uart_bus_t bus, uint8_t *rx_buffer, uint16_t rx_buffer_size)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 更新 UART 接收 Buffer 的地址和长度。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | UART 总线号 | UART_BUS_0 ~ UART_BUS_2 |
| rx_buffer | uint8_t * | 新的接收 Buffer 地址 | 不为 NULL |
| rx_buffer_size | uint16_t | 新的接收 Buffer 长度（字节） | - |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 成功更新 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 更新失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_RX | 特性宏 | 启用 UART 接收支持 | y |

### uapi_uart_suspend <a id="uapi_uart_suspend"></a>

```c
errcode_t uapi_uart_suspend(uintptr_t arg)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 挂起所有 UART 通道，暂停 UART 操作。

**前置条件**

- 已调用 `uapi_uart_init` 完成初始化。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| arg | uintptr_t | 挂起所需要的参数 | - |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 挂起成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 挂起失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_LPM | 特性宏 | 启用 UART 低功耗管理（Low Power Management）支持 | y |

### uapi_uart_resume <a id="uapi_uart_resume"></a>

```c
errcode_t uapi_uart_resume(uintptr_t arg)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 恢复所有 UART 通道，从挂起状态恢复 UART 操作。

**前置条件**

- 已调用 `uapi_uart_suspend` 挂起 UART。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| arg | uintptr_t | 恢复所需要的参数 | - |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 恢复成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 恢复失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_LPM | 特性宏 | 启用 UART 低功耗管理（Low Power Management）支持 | y |

### uapi_uart_register_write_by_dma_callback <a id="uapi_uart_register_write_by_dma_callback"></a>

```c
errcode_t uapi_uart_register_write_by_dma_callback(uart_bus_t bus, uart_tx_by_dma_callback_t tx_dma_cb)
```

**声明头文件**

```c
#include "include/driver/uart.h"
```

**功能说明**

- 注册在 UART DMA 发送完成中断中直接进行 DMA 写的回调。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [uart_bus_t](#uart_bus_t) | 串口号 | 有效 UART 总线 |
| tx_dma_cb | uart_tx_by_dma_callback_t | DMA 发送完成回调 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| ---- | ---- | ---- |
| ERRCODE_SUCC：0 | 成功 | 成功注册 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 注册失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_UART_SUPPORT_SEND_IN_DMA_ISR | 特性宏 | 支持在 DMA 发送中断中回调功能（接口级，包裹接口声明） | n |

## Type definitions

### uart_pin_config_t <a id="uart_pin_config_t"></a>

```c
typedef hal_uart_pin_config_t uart_pin_config_t;
```

**使用说明**

- UART 引脚配置类型，等价于 [hal_uart_pin_config_t](#hal_uart_pin_config_t)。

### uart_attr_t <a id="uart_attr_t"></a>

```c
typedef hal_uart_attr_t uart_attr_t;
```

**使用说明**

- UART 基本属性定义类型，等价于 [hal_uart_attr_t](#hal_uart_attr_t)。

### uart_extra_attr_t <a id="uart_extra_attr_t"></a>

```c
typedef hal_uart_extra_attr_t uart_extra_attr_t;
```

**使用说明**

- UART 扩展属性定义类型，等价于 [hal_uart_extra_attr_t](#hal_uart_extra_attr_t)。

### uart_rx_callback_t <a id="uart_rx_callback_t"></a>

```c
typedef void (*uart_rx_callback_t)(const void *buffer, uint16_t length, bool error);
```

**使用说明**

- UART 接收数据回调函数类型。在中断上下文中执行，接收缓冲区在回调返回后会被释放。


- 参数 参数名：说明。
- 参数 buffer：读取数据时用于存储数据的 Buffer。
- 参数 length：Buffer 的长度。
- 参数 error：true 表示接收数据时产生了错误，false 表示正常。

### uart_tx_callback_t <a id="uart_tx_callback_t"></a>

```c
typedef void (*uart_tx_callback_t)(const void *buffer, uint32_t length, const void *params);
```

**使用说明**

- UART 发送数据回调函数类型，在中断上下文中执行。


- 参数 参数名：说明。
- 参数 buffer：发送时的数据缓存。
- 参数 length：发送时的数据长度。
- 参数 params：传递的参数。


### uart_error_callback_t <a id="uart_error_callback_t"></a>

```c
typedef void (*uart_error_callback_t)(uint32_t *err_info, uint32_t len);
```

**使用说明**

- UART 错误处理回调函数类型，在中断上下文中执行，执行完成后会自动释放内存。用于奇偶校验、帧、溢出错误回调注册。


- 参数 参数名：说明。
- 参数 err_info：错误信息，每一个成员都是 32-bit。
- 参数 len：错误信息的长度。

### uart_tx_by_dma_callback_t <a id="uart_tx_by_dma_callback_t"></a>

```c
typedef errcode_t (*uart_tx_by_dma_callback_t)(void);
```

**使用说明**

- UART DMA 发送完成回调函数类型，作为 [uapi_uart_register_write_by_dma_callback](#uapi_uart_register_write_by_dma_callback) 的入参类型。
- 回调在中断上下文中执行，返回 errcode_t。

### uart_idle_int_receive_cb_t <a id="uart_idle_int_receive_cb_t"></a>

```c
typedef bool (*uart_idle_int_receive_cb_t)(uint8_t *receive_buff, uint32_t receive_length, bool error);
```

**使用说明**

- UART DMA 不定长接收完成后的 IDLE 回调函数类型，作为 [uapi_uart_dma_recv_raw_data](#uapi_uart_dma_recv_raw_data) 的入参类型。
- 参数 receive_buff：接收数据缓冲区；参数 receive_length：接收数据长度；参数 error：接收是否出错。
- 返回 true 表示继续接收数据，false 表示停止接收数据。

### errcode_t <a id="errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

- 通用错误码类型，定义于 `errcode.h`。`ERRCODE_SUCC`（0）表示成功，其余非零值表示失败，具体含义参考 `errcode.h`

## Enumerations

### uart_bus_t <a id="uart_bus_t"></a>

```c
typedef enum {
    UART_BUS_0 = 0,  // !< UART L | UART H1
#if UART_BUS_MAX_NUMBER > 1
    UART_BUS_1 = 1,  // !< UART H | UART H0
#endif
#if UART_BUS_MAX_NUMBER > 2
    UART_BUS_2 = 2,  // !< M UART | UART L0
#endif
    UART_BUS_NONE = UART_BUS_MAX_NUMBER  // !< Value used as invalid/unused UART number
} uart_bus_t;
```

**使用说明**

- UART 总线号枚举，定义于 `platform_core.h`（`UART_BUS_MAX_NUMBER` 为 3）。

| 枚举成员 | 取值 | 描述 |
| ------ | ---- | ---- |
| UART_BUS_0 | 0 | UART 总线 0 |
| UART_BUS_1 | 1 | UART 总线 1 |
| UART_BUS_2 | 2 | UART 总线 2 |
| UART_BUS_NONE | 3 | 无效总线号（UART_BUS_MAX_NUMBER） |

### uart_rx_condition_t <a id="uart_rx_condition_t"></a>

```c
typedef enum uart_rx_condition {
    UART_RX_CONDITION_FULL_OR_IDLE = (UART_RX_CONDITION_MASK_FULL | UART_RX_CONDITION_MASK_IDLE),
    UART_RX_CONDITION_FULL_OR_SUFFICIENT_DATA = (UART_RX_CONDITION_MASK_FULL | UART_RX_CONDITION_MASK_SUFFICIENT_DATA),
    UART_RX_CONDITION_FULL_OR_SUFFICIENT_DATA_OR_IDLE = (UART_RX_CONDITION_MASK_FULL | UART_RX_CONDITION_MASK_SUFFICIENT_DATA | UART_RX_CONDITION_MASK_IDLE)
} uart_rx_condition_t;
```

**使用说明**

- UART 接收数据触发回调的条件枚举，定义于 `uart.h`

| 枚举成员 | 取值 | 描述 |
| ------ | ---- | ---- |
| UART_RX_CONDITION_FULL_OR_IDLE | 5 | 接收缓存已满或接收暂停时触发回调 |
| UART_RX_CONDITION_FULL_OR_SUFFICIENT_DATA | 6 | 接收缓存已满或接收数据量达到指定长度时触发回调 |
| UART_RX_CONDITION_FULL_OR_SUFFICIENT_DATA_OR_IDLE | 7 | 接收缓存已满、接收数据量达到指定长度或接收暂停时触发回调 |

## Structures

### hal_uart_pin_config_t <a id="hal_uart_pin_config_t"></a>

```c
typedef struct {
    pin_t tx_pin;
    pin_t rx_pin;
    pin_t cts_pin;
    pin_t rts_pin;
} hal_uart_pin_config_t;
```

**使用说明**

- UART 引脚配置结构体，定义于 `hal_uart.h`

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ---- | ---- | ---- |
| tx_pin | pin_t | 发送引脚 |
| rx_pin | pin_t | 接收引脚 |
| cts_pin | pin_t | 发送就绪引脚 |
| rts_pin | pin_t | 接收就绪引脚 |

### hal_uart_attr_t <a id="hal_uart_attr_t"></a>

```c
typedef struct uart_attr {
    uint32_t baud_rate;
    uint8_t data_bits;
    uint8_t stop_bits;
    uint8_t parity;
    uint8_t flow_ctrl;
} hal_uart_attr_t;
```

**使用说明**

- UART 基本属性配置结构体，定义于 `hal_uart.h`

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ---- | ---- | ---- |
| baud_rate | uint32_t | 波特率 |
| data_bits | uint8_t | 数据位，参考 uart_data_bit_t |
| stop_bits | uint8_t | 停止位，参考 uart_stop_bit_t |
| parity | uint8_t | 校验位，参考 uart_parity_t |
| flow_ctrl | uint8_t | 流控类型，参考 uart_flow_ctrl_t |

### hal_uart_extra_attr_t <a id="hal_uart_extra_attr_t"></a>

```c
typedef struct uart_extra_attr {
    bool tx_dma_enable;
    uint8_t tx_int_threshold;
    bool rx_dma_enable;
    uint8_t rx_int_threshold;
} hal_uart_extra_attr_t;
```

**使用说明**

- UART 扩展属性配置结构体，定义于 `hal_uart.h`

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ---- | ---- | ---- |
| tx_dma_enable | bool | TX 是否使用 DMA。false: 使用 uapi_uart_write 发送; true: 使用 uapi_uart_write_by_dma 发送 |
| tx_int_threshold | uint8_t | 触发中断的 TX FIFO 水线 |
| rx_dma_enable | bool | RX 是否使用 DMA。false: 使用 uapi_uart_read 接收; true: 使用 uapi_uart_read_by_dma 接收 |
| rx_int_threshold | uint8_t | 触发中断的 RX FIFO 水线 |

### uart_buffer_config_t <a id="uart_buffer_config_t"></a>

```c
typedef struct uart_buffer_config {
    void *rx_buffer;
    size_t rx_buffer_size;
} uart_buffer_config_t;
```

**使用说明**

- UART 缓冲区配置结构体，定义于 `uart.h`

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ---- | ---- | ---- |
| rx_buffer | void * | 接收数据 Buffer 指针 |
| rx_buffer_size | size_t | 接收 Buffer 的长度 |

### uart_write_dma_config_t <a id="uart_write_dma_config_t"></a>

```c
typedef struct uart_write_dma_config {
    uint8_t src_width;
    uint8_t dest_width;
    uint8_t burst_length;
    uint8_t priority;
} uart_write_dma_config_t;
```

**使用说明**

- UART DMA 发送配置结构体，定义于 `uart.h`

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ---- | ---- | ---- |
| src_width | uint8_t | 源端传输数据宽度：0-1 字节，1-2 字节，2-4 字节 |
| dest_width | uint8_t | 目的端传输数据宽度：0-1 字节，1-2 字节，2-4 字节 |
| burst_length | uint8_t | burst 长度：0-1，1-4，2-8，3-16 |
| priority | uint8_t | 传输通道优先级（最小 0，最大 3） |


## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```

### ERRCODE_FAIL <a id="ERRCODE_FAIL"></a>

```c
#define ERRCODE_FAIL                                        0xFFFFFFFF
```

### ERRCODE_INVALID_PARAM <a id="ERRCODE_INVALID_PARAM"></a>

```c
#define ERRCODE_INVALID_PARAM                               0x80000001
```
