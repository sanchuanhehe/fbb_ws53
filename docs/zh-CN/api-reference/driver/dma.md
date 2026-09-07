# DMA

DMA（Direct Memory Access）在无需 CPU 干预的情况下实现外设与内存之间的数据传输，支持内存到内存、内存到外设以及外设到内存的单次传输与链表（Linked List Item, LLI）传输模式。模块同时提供低功耗（Low Power Mode, LPM）场景下的挂起与恢复能力，并通过回调机制在传输完成或发生错误时通知调用方。

**模块公共头文件**

```c
#include "driver/dma.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_dma_init](#uapi_dma_init) | 初始化 DMA 模块 |
| [uapi_dma_deinit](#uapi_dma_deinit) | 去初始化 DMA 模块 |
| [uapi_dma_open](#uapi_dma_open) | 开启 DMA 模块 |
| [uapi_dma_close](#uapi_dma_close) | 关闭 DMA 模块 |
| [uapi_dma_start_transfer](#uapi_dma_start_transfer) | 启动指定通道的 DMA 传输 |
| [uapi_dma_end_transfer](#uapi_dma_end_transfer) | 停止指定通道的 DMA 传输 |
| [uapi_dma_get_block_ts](#uapi_dma_get_block_ts) | 获取 DMA 已传输的数据量 |
| [uapi_dma_transfer_memory_single](#uapi_dma_transfer_memory_single) | 以单次模式传输内存到内存的数据 |
| [uapi_dma_configure_peripheral_transfer_single](#uapi_dma_configure_peripheral_transfer_single) | 以单次模式配置内存到外设或外设到内存的传输 |
| [uapi_dma_get_lli_channel](#uapi_dma_get_lli_channel) | 获取 DMA 链表传输通道 |
| [uapi_dma_transfer_memory_lli](#uapi_dma_transfer_memory_lli) | 以链表模式传输内存到内存的数据 |
| [uapi_dma_configure_peripheral_transfer_lli](#uapi_dma_configure_peripheral_transfer_lli) | 以链表模式配置内存到外设或外设到内存的传输 |
| [uapi_dma_enable_lli](#uapi_dma_enable_lli) | 启用 DMA 链表传输 |
| [uapi_dma_resume](#uapi_dma_resume) | 恢复 DMA 模块 |
| [uapi_dma_suspend](#uapi_dma_suspend) | 挂起 DMA 模块 |

## Functions

### uapi_dma_init <a id="uapi_dma_init"></a>

```c
errcode_t uapi_dma_init(void)
```

**声明头文件**

```c
#include "driver/dma.h"
```

**功能说明**

- 初始化 DMA 模块。
- 为后续通道传输相关接口的调用建立可用前提。
- 模块已初始化时再次调用直接返回成功，不重复执行初始化动作。

**前置条件**

- 调用时序约束：在使用任何 DMA 通道传输接口之前，必须先调用本接口完成模块初始化。
- 依赖关系：当前接口依赖底层 HAL 函数表已可获取且成功初始化。

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 成功初始化或模块已初始化 |
| ERRCODE_DMA_NOT_INIT：0x80001100 | DMA 未初始化 | 底层 HAL 函数表获取失败 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层 HAL 初始化返回失败 |

**参考案例**

- `src/application/samples/peripheral/dma/dma_demo.c`

### uapi_dma_deinit <a id="uapi_dma_deinit"></a>

```c
void uapi_dma_deinit(void)
```

**声明头文件**

```c
#include "driver/dma.h"
```

**功能说明**

- 去初始化 DMA 模块，释放驱动层与 HAL 层的接口绑定。
- 将模块标记为未初始化状态，使后续接口调用不再生效。
- 模块未初始化时调用直接返回，不执行任何动作。

**前置条件**

- 调用时序约束：当前接口应在 [uapi_dma_init](#uapi_dma_init) 成功执行之后调用。
- 上下文限制：调用本接口后，需重新执行 [uapi_dma_init](#uapi_dma_init) 才能恢复模块可用状态。

**参考案例**

- `src/application/samples/peripheral/dma/dma_demo.c`

### uapi_dma_open <a id="uapi_dma_open"></a>

```c
errcode_t uapi_dma_open(void)
```

**声明头文件**

```c
#include "driver/dma.h"
```

**功能说明**

- 开启 DMA 模块，使能底层 DMA 设备。
- 为通道传输提供中断回调通路。
- 与 [uapi_dma_close](#uapi_dma_close) 配合使用，控制模块开启与关闭状态。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_dma_init](#uapi_dma_init) 成功返回后调用。
- 依赖关系：当前接口依赖模块已完成初始化，未初始化时返回错误码。

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 模块开启成功 |
| ERRCODE_DMA_NOT_INIT：0x80001100 | DMA 未初始化 | 模块未初始化即调用本接口 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**参考案例**

- `src/application/samples/peripheral/dma/dma_demo.c`

### uapi_dma_close <a id="uapi_dma_close"></a>

```c
void uapi_dma_close(void)
```

**声明头文件**

```c
#include "driver/dma.h"
```

**功能说明**

- 关闭 DMA 模块，去使能底层 DMA 设备。
- 注销 DMA 中断处理，停止中断回调通路。
- 与 [uapi_dma_open](#uapi_dma_open) 配合使用，控制模块开启与关闭状态。

**前置条件**

- 调用时序约束：当前接口应在 [uapi_dma_open](#uapi_dma_open) 之后调用，用于关闭已开启的模块。
- 上下文限制：调用本接口后，模块中断通路已注销，需重新调用 [uapi_dma_open](#uapi_dma_open) 才能恢复传输能力。

### uapi_dma_start_transfer <a id="uapi_dma_start_transfer"></a>

```c
errcode_t uapi_dma_start_transfer(uint8_t channel)
```

**声明头文件**

```c
#include "driver/dma.h"
```

**功能说明**

- 启动指定 DMA 通道上已完成配置的传输。
- 使目标通道按照此前配置的参数开始数据搬运。
- 与 [uapi_dma_end_transfer](#uapi_dma_end_transfer) 配合使用，控制单通道传输的起停。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_dma_init](#uapi_dma_init) 与 [uapi_dma_open](#uapi_dma_open) 成功返回后调用。
- 依赖关系：目标通道已完成传输配置（如调用 [uapi_dma_transfer_memory_single](#uapi_dma_transfer_memory_single) 等配置接口）。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | DMA 通道号 | 0 ~ [DMA_CHANNEL_MAX_NUM](#DMA_CHANNEL_MAX_NUM)：8 - 1 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 通道传输启动成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### uapi_dma_end_transfer <a id="uapi_dma_end_transfer"></a>

```c
errcode_t uapi_dma_end_transfer(uint8_t channel)
```

**声明头文件**

```c
#include "driver/dma.h"
```

**功能说明**

- 停止指定 DMA 通道上正在进行的传输。
- 终止目标通道的数据搬运动作。
- 与 [uapi_dma_start_transfer](#uapi_dma_start_transfer) 配合使用，控制单通道传输的起停。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_dma_init](#uapi_dma_init) 与 [uapi_dma_open](#uapi_dma_open) 成功返回后调用。
- 依赖关系：目标通道已处于传输中或已完成传输配置。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | DMA 通道号 | 0 ~ [DMA_CHANNEL_MAX_NUM](#DMA_CHANNEL_MAX_NUM)：8 - 1 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 通道传输停止成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**参考案例**

- `src/application/samples/peripheral/dma/dma_demo.c`

### uapi_dma_get_block_ts <a id="uapi_dma_get_block_ts"></a>

```c
uint32_t uapi_dma_get_block_ts(uint8_t channel)
```

**声明头文件**

```c
#include "driver/dma.h"
```

**功能说明**

- 获取指定 DMA 通道当前已传输的数据量。
- 返回值为底层硬件统计的传输块计数。
- 用于在传输过程中或完成后查询实际搬运进度。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_dma_init](#uapi_dma_init) 与 [uapi_dma_open](#uapi_dma_open) 成功返回后调用。
- 依赖关系：目标通道已完成传输配置或正处于传输中。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | DMA 通道号 | 0 ~ [DMA_CHANNEL_MAX_NUM](#DMA_CHANNEL_MAX_NUM)：8 - 1 |

**返回值**

- 返回类型：uint32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| uint32_t | 已传输的数据量 | 查询指定通道的传输块计数 |

### uapi_dma_transfer_memory_single <a id="uapi_dma_transfer_memory_single"></a>

```c
errcode_t uapi_dma_transfer_memory_single(const dma_ch_user_memory_config_t *user_cfg, dma_transfer_cb_t callback, uintptr_t arg)
```

**声明头文件**

```c
#include "driver/dma.h"
```

**功能说明**

- 以单次传输模式，发起内存到内存的 DMA 数据搬运。
- 由调用方通过配置结构体指定源地址、目的地址、传输数据量、优先级与数据宽度。
- 传输完成或发生错误时，通过回调函数通知调用方。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_dma_init](#uapi_dma_init) 与 [uapi_dma_open](#uapi_dma_open) 成功返回后调用。
- 依赖关系：入参 user_cfg 必须非空，且其指向的配置需满足字段约束。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| user_cfg | [dma_ch_user_memory_config_t](#dma_ch_user_memory_config_t) * | 用户的 DMA 通道内存到内存传输配置 | 不为 NULL |
| callback | [dma_transfer_cb_t](#dma_transfer_cb_t) | 通道传输完成/错误回调函数 | - |
| arg | uintptr_t | 用于存储自定义信息的私有参数指针，传输完成时回传给回调函数 | - |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 内存到内存单次传输配置成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**参考案例**

- `src/application/samples/peripheral/dma/dma_demo.c`

### uapi_dma_configure_peripheral_transfer_single <a id="uapi_dma_configure_peripheral_transfer_single"></a>

```c
errcode_t uapi_dma_configure_peripheral_transfer_single(const dma_ch_user_peripheral_config_t *user_cfg, uint8_t *channel, dma_transfer_cb_t callback, uintptr_t arg)
```

**声明头文件**

```c
#include "driver/dma.h"
```

**功能说明**

- 以单次传输模式，配置内存到外设或外设到内存的 DMA 数据搬运。
- 根据传输方向自动选取空闲 DMA 通道，并将选中的通道号通过出参返回给调用方。
- 传输完成或发生错误时，通过回调函数通知调用方。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_dma_init](#uapi_dma_init) 与 [uapi_dma_open](#uapi_dma_open) 成功返回后调用。
- 依赖关系：入参 user_cfg 必须非空，且其字段（握手号、传输类型、传输方向、优先级、数据宽度、burst 长度、地址增量、保护位）需满足合法性约束；当前接口需存在可用空闲通道，否则返回无可用通道错误码。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| user_cfg | [dma_ch_user_peripheral_config_t](#dma_ch_user_peripheral_config_t) * | 用户的 DMA 通道内存到外设或外设到内存传输配置 | 不为 NULL，且各字段满足合法性约束 |
| channel | uint8_t * | 出参，由本接口写入被选中的 DMA 通道号 | 不为 NULL |
| callback | [dma_transfer_cb_t](#dma_transfer_cb_t) | 通道传输完成/错误回调函数 | - |
| arg | uintptr_t | 用于存储自定义信息的私有参数指针，传输完成时回传给回调函数 | - |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| channel | uint8_t * | 本接口根据传输方向选取的空闲 DMA 通道号，由调用方分配内存、接口填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 内存到外设或外设到内存单次传输配置成功 |
| ERRCODE_DMA_NOT_INIT：0x80001100 | DMA 未初始化 | 模块未初始化即调用本接口 |
| ERRCODE_DMA_INVALID_PARAMETER：0x80001102 | 参数无效 | user_cfg 为空或其字段未通过合法性校验 |
| ERRCODE_DMA_RET_NO_AVAIL_CH：0x80001103 | 无可用通道 | 未找到满足握手号与 burst 长度要求的空闲 DMA 通道 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层配置返回其他失败 |

### uapi_dma_get_lli_channel <a id="uapi_dma_get_lli_channel"></a>

```c
uint8_t uapi_dma_get_lli_channel(uint8_t burst_length, uint8_t handshaking)
```

**声明头文件**

```c
#include "driver/dma.h"
```

**功能说明**

- 获取用于链表传输的 DMA 通道。
- 按照指定的 burst 传输长度与外设握手号匹配并返回空闲通道。
- 返回值用于后续链表传输配置接口（如 [uapi_dma_transfer_memory_lli](#uapi_dma_transfer_memory_lli)）的通道入参。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_dma_init](#uapi_dma_init) 与 [uapi_dma_open](#uapi_dma_open) 成功返回后调用。
- 依赖关系：当前接口依赖启用链表传输特性（CONFIG_DMA_SUPPORT_LLI）；需存在满足入参要求的空闲通道。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| burst_length | uint8_t | DMA 的 burst 传输长度 | 0 ~ 7（实现以 HAL_DMA_BURST_TRANSACTION_LENGTH_256(7) 为上界校验，burst_length ≤ 7） |
| handshaking | uint8_t | DMA 传输外设握手号，取值参考 [hal_dma_handshaking_source_t](#hal_dma_handshaking_source_t) | 0 ~ HAL_DMA_HANDSHAKING_MAX_NUM(33) - 1 |

**返回值**

- 返回类型：uint8_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| uint8_t | 选中的 DMA 通道号，取值范围参考 [dma_channel_t](#dma_channel_t) | 匹配到满足要求的空闲通道 |
| DMA_CHANNEL_NONE(8) | 无可用通道 | 未匹配到满足要求的空闲通道 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DMA_SUPPORT_LLI | 特性宏 | 支持 DMA 链表传输接口功能（接口级） | y |

### uapi_dma_transfer_memory_lli <a id="uapi_dma_transfer_memory_lli"></a>

```c
errcode_t uapi_dma_transfer_memory_lli(uint8_t channel, const dma_ch_user_memory_config_t *user_cfg, dma_transfer_cb_t callback)
```

**声明头文件**

```c
#include "driver/dma.h"
```

**功能说明**

- 以链表传输模式，配置内存到内存的 DMA 数据搬运。
- 将一组内存到内存传输配置追加到指定通道的链表项中，支持多段数据的连续传输。
- 传输完成或发生错误时，通过回调函数通知调用方。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_dma_init](#uapi_dma_init) 与 [uapi_dma_open](#uapi_dma_open) 成功返回后调用。
- 依赖关系：当前接口依赖启用链表传输特性（CONFIG_DMA_SUPPORT_LLI）；入参 channel 应来自 [uapi_dma_get_lli_channel](#uapi_dma_get_lli_channel) 的返回值；入参 user_cfg 必须非空。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | DMA 通道号，建议来自 [uapi_dma_get_lli_channel](#uapi_dma_get_lli_channel) 的返回值 | 0 ~ [DMA_CHANNEL_MAX_NUM](#DMA_CHANNEL_MAX_NUM)：8 - 1 |
| user_cfg | [dma_ch_user_memory_config_t](#dma_ch_user_memory_config_t) * | 用户的 DMA 通道内存到内存传输配置 | 不为 NULL |
| callback | [dma_transfer_cb_t](#dma_transfer_cb_t) | 通道传输完成/错误回调函数 | - |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 内存到内存链表传输配置成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**参考案例**

- `src/application/samples/peripheral/dma/dma_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DMA_SUPPORT_LLI | 特性宏 | 支持 DMA 链表传输接口功能（接口级） | y |

### uapi_dma_configure_peripheral_transfer_lli <a id="uapi_dma_configure_peripheral_transfer_lli"></a>

```c
errcode_t uapi_dma_configure_peripheral_transfer_lli(uint8_t channel, const dma_ch_user_peripheral_config_t *user_cfg, dma_transfer_cb_t callback)
```

**声明头文件**

```c
#include "driver/dma.h"
```

**功能说明**

- 以链表传输模式，配置内存到外设或外设到内存的 DMA 数据搬运。
- 将一组外设相关传输配置追加到指定通道的链表项中，支持多段数据的连续传输。
- 传输完成或发生错误时，通过回调函数通知调用方。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_dma_init](#uapi_dma_init) 与 [uapi_dma_open](#uapi_dma_open) 成功返回后调用。
- 依赖关系：当前接口依赖启用链表传输特性（CONFIG_DMA_SUPPORT_LLI）；入参 channel 需合法；入参 user_cfg 必须非空，且其字段（握手号、传输类型、传输方向、优先级、数据宽度、burst 长度、地址增量、保护位）需满足合法性约束。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | DMA 通道号 | < [DMA_CHANNEL_MAX_NUM](#DMA_CHANNEL_MAX_NUM)：8 |
| user_cfg | [dma_ch_user_peripheral_config_t](#dma_ch_user_peripheral_config_t) * | 用户的 DMA 通道内存到外设或外设到内存传输配置 | 不为 NULL，且各字段满足合法性约束 |
| callback | [dma_transfer_cb_t](#dma_transfer_cb_t) | 通道传输完成/错误回调函数 | - |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 内存到外设或外设到内存链表传输配置成功 |
| ERRCODE_DMA_INVALID_PARAMETER：0x80001102 | 参数无效 | channel 超出范围、user_cfg 为空或其字段未通过合法性校验 |
| ERRCODE_DMA_NOT_INIT：0x80001100 | DMA 未初始化 | 模块未初始化即调用本接口 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层链表配置返回其他失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DMA_SUPPORT_LLI | 特性宏 | 支持 DMA 链表传输接口功能（接口级） | y |

### uapi_dma_enable_lli <a id="uapi_dma_enable_lli"></a>

```c
errcode_t uapi_dma_enable_lli(uint8_t channel, dma_transfer_cb_t callback, uintptr_t arg)
```

**声明头文件**

```c
#include "driver/dma.h"
```

**功能说明**

- 启用指定 DMA 通道上已完成配置的链表传输。
- 使目标通道按照此前追加的链表项开始连续数据搬运。
- 传输完成或发生错误时，通过回调函数通知调用方。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_dma_init](#uapi_dma_init) 与 [uapi_dma_open](#uapi_dma_open) 成功返回后调用。
- 依赖关系：当前接口依赖启用链表传输特性（CONFIG_DMA_SUPPORT_LLI）；目标通道应已通过 [uapi_dma_transfer_memory_lli](#uapi_dma_transfer_memory_lli) 或 [uapi_dma_configure_peripheral_transfer_lli](#uapi_dma_configure_peripheral_transfer_lli) 完成链表项配置。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | DMA 通道号 | 0 ~ [DMA_CHANNEL_MAX_NUM](#DMA_CHANNEL_MAX_NUM)：8 - 1 |
| callback | [dma_transfer_cb_t](#dma_transfer_cb_t) | 通道传输完成/错误回调函数 | - |
| arg | uintptr_t | 用于存储自定义信息的私有参数指针，传输完成时回传给回调函数 | - |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 链表传输启用成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**参考案例**

- `src/application/samples/peripheral/dma/dma_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DMA_SUPPORT_LLI | 特性宏 | 支持 DMA 链表传输接口功能（接口级） | y |

### uapi_dma_resume <a id="uapi_dma_resume"></a>

```c
errcode_t uapi_dma_resume(uintptr_t arg)
```

**声明头文件**

```c
#include "driver/dma.h"
```

**功能说明**

- 恢复 DMA 模块，使其从挂起状态回到正常工作状态。
- 通过重新打开底层 DMA 设备恢复传输能力。
- 用于低功耗场景下，模块从挂起状态恢复时的处理。

**前置条件**

- 调用时序约束：当前接口应在 [uapi_dma_suspend](#uapi_dma_suspend) 之后调用，用于恢复已挂起的模块。
- 依赖关系：当前接口依赖启用低功耗特性（CONFIG_DMA_SUPPORT_LPM）；模块需处于已初始化状态。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| arg | uintptr_t | 恢复操作传入的参数 | - |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 模块恢复成功 |
| ERRCODE_DMA_NOT_INIT：0x80001100 | DMA 未初始化 | 模块未初始化即调用本接口 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DMA_SUPPORT_LPM | 特性宏 | 支持 DMA 低功耗挂起/恢复接口功能（接口级） | y |

### uapi_dma_suspend <a id="uapi_dma_suspend"></a>

```c
errcode_t uapi_dma_suspend(uintptr_t arg)
```

**声明头文件**

```c
#include "driver/dma.h"
```

**功能说明**

- 低功耗场景下的挂起入口，当前版本调用后直接返回成功，不改变 DMA 硬件状态。
- 用于低功耗场景下，模块进入挂起状态时的处理。
- 与 [uapi_dma_resume](#uapi_dma_resume) 配合使用，构成挂起与恢复的调用对。

**前置条件**

- 调用时序约束：当前接口应在模块已完成初始化后调用；恢复时需调用 [uapi_dma_resume](#uapi_dma_resume)。
- 依赖关系：当前接口依赖启用低功耗特性（CONFIG_DMA_SUPPORT_LPM）。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| arg | uintptr_t | 挂起操作传入的参数 | - |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 模块挂起成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DMA_SUPPORT_LPM | 特性宏 | 支持 DMA 低功耗挂起/恢复接口功能（接口级） | y |

## Type definitions

### errcode_t <a id="typedef_errcode_t"></a>

```c
// 源码原始定义
typedef uint32_t errcode_t;
```

**使用说明**

本模块对外接口的返回值类型，用于表示接口执行结果。

### dma_transfer_cb_t <a id="dma_transfer_cb_t"></a>

```c
// 源码原始定义
typedef void (*dma_transfer_cb_t)(uint8_t intr, uint8_t channel, uintptr_t arg);
```

**使用说明**

DMA 通道传输完成/错误所触发的回调函数指针类型。

回调说明：

- 调用时机：在传输完成或发生错误时，由 DMA 中断处理路径调用。
- 回调参数 intr：DMA 中断类型，标识触发本次回调的事件类别。
- 回调参数 channel：触发本次回调的 DMA 通道号。
- 回调参数 arg：调用方在发起传输时透传的私有参数指针。

## Enumerations

### dma_channel_t <a id="dma_channel_t"></a>

```c
// 源码原始定义
typedef enum {
    DMA_CHANNEL_0,    /*!< DMA channel 0. */
    DMA_CHANNEL_1,    /*!< DMA channel 1. */
    DMA_CHANNEL_2,    /*!< DMA channel 2. */
    DMA_CHANNEL_3,    /*!< DMA channel 3. */
    DMA_CHANNEL_4,    /*!< DMA channel 4. */
    DMA_CHANNEL_5,    /*!< DMA channel 5. */
    DMA_CHANNEL_6,    /*!< DMA channel 6. */
    DMA_CHANNEL_7,    /*!< DMA channel 7. */
    DMA_CHANNEL_NONE = DMA_CHANNEL_MAX_NUM
} dma_channel_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| DMA_CHANNEL_0 | 0 | DMA 通道 0 |
| DMA_CHANNEL_1 | 1 | DMA 通道 1 |
| DMA_CHANNEL_2 | 2 | DMA 通道 2 |
| DMA_CHANNEL_3 | 3 | DMA 通道 3 |
| DMA_CHANNEL_4 | 4 | DMA 通道 4 |
| DMA_CHANNEL_5 | 5 | DMA 通道 5 |
| DMA_CHANNEL_6 | 6 | DMA 通道 6 |
| DMA_CHANNEL_7 | 7 | DMA 通道 7 |
| DMA_CHANNEL_NONE | 8 | 无可用通道，取值为 DMA_CHANNEL_MAX_NUM |

### hal_dma_handshaking_source_t <a id="hal_dma_handshaking_source_t"></a>

```c
// 源码原始定义
typedef enum {
    HAL_DMA_HANDSHAKING_I2C0_TX,
    HAL_DMA_HANDSHAKING_I2C0_RX,
    HAL_DMA_HANDSHAKING_I2C1_TX,
    HAL_DMA_HANDSHAKING_I2C1_RX,
    HAL_DMA_HANDSHAKING_QSPI0_2CS_TX,
    HAL_DMA_HANDSHAKING_QSPI0_2CS_RX,
    HAL_DMA_HANDSHAKING_SPI_M_TX,
    HAL_DMA_HANDSHAKING_SPI_M_RX,
    HAL_DMA_HANDSHAKING_UART_H0_TX,    /* uart1 */
    HAL_DMA_HANDSHAKING_UART_H0_RX,
    HAL_DMA_HANDSHAKING_UART_H1_TX,    /* uart0 */
    HAL_DMA_HANDSHAKING_UART_H1_RX,
    HAL_DMA_HANDSHAKING_I2S_TX,
    HAL_DMA_HANDSHAKING_I2S_RX,
    HAL_DMA_HANDSHAKING_PWM,
    HAL_DMA_HANDSHAKING_SPWM,
    HAL_DMA_HANDSHAKING_TIE0,    /* 此握手号及其之后的握手号不存在 */
    HAL_DMA_HANDSHAKING_SPI_MS0_TX,
    HAL_DMA_HANDSHAKING_SPI_MS0_RX,
    HAL_DMA_HANDSHAKING_SPI_MS1_TX,
    HAL_DMA_HANDSHAKING_SPI_MS1_RX,
    HAL_DMA_HANDSHAKING_OPI_TX,
    HAL_DMA_HANDSHAKING_OPI_RX,
    HAL_DMA_HANDSHAKING_QSPI1_2CS_TX,
    HAL_DMA_HANDSHAKING_QSPI1_2CS_RX,
    HAL_DMA_HANDSHAKING_QSPI2_1CS_TX,
    HAL_DMA_HANDSHAKING_QSPI2_1CS_RX,
    HAL_DMA_HANDSHAKING_SPI3_M_TX,
    HAL_DMA_HANDSHAKING_SPI3_M_RX,
    HAL_DMA_HANDSHAKING_QSPI3_1CS_TX,
    HAL_DMA_HANDSHAKING_QSPI3_1CS_RX,
    HAL_DMA_HANDSHAKING_SPI4_S_RX,
    HAL_DMA_HANDSHAKING_SPI4_S_TX,
    HAL_DMA_HANDSHAKING_MAX_NUM
} hal_dma_handshaking_source_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| HAL_DMA_HANDSHAKING_I2C0_TX | 0 | I2C0 发送握手号 |
| HAL_DMA_HANDSHAKING_I2C0_RX | 1 | I2C0 接收握手号 |
| HAL_DMA_HANDSHAKING_I2C1_TX | 2 | I2C1 发送握手号 |
| HAL_DMA_HANDSHAKING_I2C1_RX | 3 | I2C1 接收握手号 |
| HAL_DMA_HANDSHAKING_QSPI0_2CS_TX | 4 | QSPI0 2CS 发送握手号 |
| HAL_DMA_HANDSHAKING_QSPI0_2CS_RX | 5 | QSPI0 2CS 接收握手号 |
| HAL_DMA_HANDSHAKING_SPI_M_TX | 6 | SPI 主机发送握手号 |
| HAL_DMA_HANDSHAKING_SPI_M_RX | 7 | SPI 主机接收握手号 |
| HAL_DMA_HANDSHAKING_UART_H0_TX | 8 | UART H0 发送握手号（uart1） |
| HAL_DMA_HANDSHAKING_UART_H0_RX | 9 | UART H0 接收握手号 |
| HAL_DMA_HANDSHAKING_UART_H1_TX | 10 | UART H1 发送握手号（uart0） |
| HAL_DMA_HANDSHAKING_UART_H1_RX | 11 | UART H1 接收握手号 |
| HAL_DMA_HANDSHAKING_I2S_TX | 12 | I2S 发送握手号 |
| HAL_DMA_HANDSHAKING_I2S_RX | 13 | I2S 接收握手号 |
| HAL_DMA_HANDSHAKING_PWM | 14 | PWM 握手号 |
| HAL_DMA_HANDSHAKING_SPWM | 15 | SPWM 握手号 |
| HAL_DMA_HANDSHAKING_TIE0 | 16 | TIE0 握手号（此握手号及其之后的握手号不存在） |
| HAL_DMA_HANDSHAKING_SPI_MS0_TX | 17 | SPI MS0 发送握手号 |
| HAL_DMA_HANDSHAKING_SPI_MS0_RX | 18 | SPI MS0 接收握手号 |
| HAL_DMA_HANDSHAKING_SPI_MS1_TX | 19 | SPI MS1 发送握手号 |
| HAL_DMA_HANDSHAKING_SPI_MS1_RX | 20 | SPI MS1 接收握手号 |
| HAL_DMA_HANDSHAKING_OPI_TX | 21 | OPI 发送握手号 |
| HAL_DMA_HANDSHAKING_OPI_RX | 22 | OPI 接收握手号 |
| HAL_DMA_HANDSHAKING_QSPI1_2CS_TX | 23 | QSPI1 2CS 发送握手号 |
| HAL_DMA_HANDSHAKING_QSPI1_2CS_RX | 24 | QSPI1 2CS 接收握手号 |
| HAL_DMA_HANDSHAKING_QSPI2_1CS_TX | 25 | QSPI2 1CS 发送握手号 |
| HAL_DMA_HANDSHAKING_QSPI2_1CS_RX | 26 | QSPI2 1CS 接收握手号 |
| HAL_DMA_HANDSHAKING_SPI3_M_TX | 27 | SPI3 主机发送握手号 |
| HAL_DMA_HANDSHAKING_SPI3_M_RX | 28 | SPI3 主机接收握手号 |
| HAL_DMA_HANDSHAKING_QSPI3_1CS_TX | 29 | QSPI3 1CS 发送握手号 |
| HAL_DMA_HANDSHAKING_QSPI3_1CS_RX | 30 | QSPI3 1CS 接收握手号 |
| HAL_DMA_HANDSHAKING_SPI4_S_RX | 31 | SPI4 从机接收握手号 |
| HAL_DMA_HANDSHAKING_SPI4_S_TX | 32 | SPI4 从机发送握手号 |
| HAL_DMA_HANDSHAKING_MAX_NUM | 33 | 握手号总数，作为合法性校验上界 |

## Structures

### dma_ch_user_memory_config_t <a id="dma_ch_user_memory_config_t"></a>

```c
// 源码原始定义
typedef struct dma_ch_user_memory_config {
    /** @if Eng  The source address of this transfer.
     *  @else    传输源地址。
     *  @endif */
    uint32_t src;
    /** @if Eng  The destination address of this transfer.
     *  @else    传输目的地址。
     *  @endif */
    uint32_t dest;
    /** @if Eng  Transfer number.
     *  @else    传输数据量。
     *  @endif */
    uint16_t transfer_num;
    /** @if Eng  Transfer priority of channel(Lowest: 0 and Highest: 3).
     *  @else    传输通道优先级(最低为0以及最高为3)。
     *  @endif */
    uint8_t priority;
    /** @if Eng  Transfer data width:
     *           - 0: 1byte
     *           - 1: 2byte
     *           - 2: 4byte
     *  @else    传输数据宽度：
     *           - 0: 1字节
     *           - 1: 2字节
     *           - 2: 4字节
     *  @endif */
    uint8_t width;
} dma_ch_user_memory_config_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| src | uint32_t | 传输源地址 |
| dest | uint32_t | 传输目的地址 |
| transfer_num | uint16_t | 传输数据量 |
| priority | uint8_t | 传输通道优先级，最低为 0、最高为 3 |
| width | uint8_t | 传输数据宽度：0 表示 1 Bytes；<br>1 表示 2 Bytes；<br>2 表示 4 Bytes。 |

### dma_ch_user_peripheral_config_t <a id="dma_ch_user_peripheral_config_t"></a>

```c
// 源码原始定义
typedef struct dma_ch_user_peripheral_config {
    /** @if Eng  The source address of this transfer.
     *  @else    传输源地址。
     *  @endif */
    uint32_t src;
    /** @if Eng  The destination address of this transfer.
     *  @else    传输目的地址。
     *  @endif */
    uint32_t dest;
    /** @if Eng  Transfer number.
     *  @else    传输数据量。
     *  @endif */
    uint16_t transfer_num;
    /** @if Eng  Hardware handshaking ID of the source. see @ref hal_dma_handshaking_source_t.
     *  @else    源端硬件握手号。 参考 @ref hal_dma_handshaking_source_t 。
     *  @endif */
    uint16_t src_handshaking;
    /** @if Eng  Hardware handshaking ID of the destination. see @ref hal_dma_handshaking_source_t.
     *  @else    目的端硬件握手号。 参考 @ref hal_dma_handshaking_source_t 。
     *  @endif */
    uint16_t dest_handshaking;
    /** @if Eng  Transfer type:
     *           - 0: memory to memory and DMA is flow controller
     *           - 1: memory to periph and DMA is flow controller
     *           - 2: periph to memory and DMA is flow controller
     *           - 3: periph to periph and DMA is flow controller
     *           - 4: periph to memory and periph is flow controller
     *           - 5: periph to periph and source periph is flow controller
     *           - 6: memory to periph and periph is flow controller
     *           - 7: periph to periph and destination periph is flow controller
     *  @else    传输类型：
     *           - 0: 内存到内存并且由DMA流控
     *           - 1: 内存到外设并且由DMA流控
     *           - 2: 外设到内存并且由DMA流控
     *           - 3: 外设到外设并且由DMA流控
     *           - 4: 外设到内存并且由外设流控
     *           - 5: 外设到外设并且由源端外设流控
     *           - 6: 内存到外设并且由外设流控
     *           - 7: 外设到外设并且由目的端外设流控
     *  @endif */
    uint8_t trans_type;
    /** @if Eng  Transfer direction:
     *           - 0: memory to periph
     *           - 1: periph to memory
     *           - 2: periph to periph
     *  @else    传输方向：
     *           - 0: 内存到外设
     *           - 1: 外设到内存
     *           - 2: 外设到外设
     *  @endif */
    uint8_t trans_dir;
    /** @if Eng  Transfer priority of channel(Lowest: 0 and Highest: 3).
     *  @else    传输通道优先级(最低为0以及最高为3)。
     *  @endif */
    uint8_t priority;
    /** @if Eng  Transfer data width of the source:
     *           - 0: 1byte
     *           - 1: 2byte
     *           - 2: 4byte
     *  @else    源端传输数据宽度：
     *           - 0: 1字节
     *           - 1: 2字节
     *           - 2: 4字节
     *  @endif */
    uint8_t src_width;
    /** @if Eng  Transfer data width of the destination:
     *           - 0: 1byte
     *           - 1: 2byte
     *           - 2: 4byte
     *  @else    目的端传输数据宽度：
     *           - 0: 1字节
     *           - 1: 2字节
     *           - 2: 4字节
     *  @endif */
    uint8_t dest_width;
    /** @if Eng  Transfer burst length:
     *           - 0: burst length is 1
     *           - 1: burst length is 4
     *           - 2: burst length is 8
     *           - 3: burst length is 16
     *  @else    传输burst长度：
     *           - 0: burst长度是1
     *           - 1: burst长度是4
     *           - 2: burst长度是8
     *           - 3: burst长度是16
     *  @endif */
    uint8_t burst_length;
    /** @if Eng  Source address incremental mode：
     *           - 0: increment
     *           - 1: decrement
     *           - 2: no change
     *  @else    源端地址增量模式：
     *           - 0: 递增
     *           - 1: 递减
     *           - 2: 不变
     *  @endif */
    uint8_t src_increment;
    /** @if Eng  Destination address incremental mode:
     *           - 0: increment
     *           - 1: decrement
     *           - 2: no change
     *  @else    目的端地址增量模式：
     *           - 0: 递增
     *           - 1: 递减
     *           - 2: 不变
     *  @endif */
    uint8_t dest_increment;
    /** @if Eng  DMA protection control bits used to drive the AHB HPROT[3:1] bus:
     *           - 0: HPROT[1]
     *           - 1: HPROT[2]
     *           - 2: HPROT[3]
     *  @else    保护控制位，用于驱动AHB HPRO[3:1]总线：
     *           - 0: HPROT[1]
     *           - 1: HPROT[2]
     *           - 2: HPROT[3]
     *  @endif */
    uint8_t protection;
} dma_ch_user_peripheral_config_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| src | uint32_t | 传输源地址 |
| dest | uint32_t | 传输目的地址 |
| transfer_num | uint16_t | 传输数据量 |
| src_handshaking | uint16_t | 源端硬件握手号，参考 [hal_dma_handshaking_source_t](#hal_dma_handshaking_source_t) |
| dest_handshaking | uint16_t | 目的端硬件握手号，参考 [hal_dma_handshaking_source_t](#hal_dma_handshaking_source_t) |
| trans_type | uint8_t | 传输类型：0 表示内存到内存且由 DMA 流控；<br>1 表示内存到外设且由 DMA 流控；<br>2 表示外设到内存且由 DMA 流控；<br>3 表示外设到外设且由 DMA 流控；<br>4 表示外设到内存且由外设流控；<br>5 表示外设到外设且由源端外设流控；<br>6 表示内存到外设且由外设流控；<br>7 表示外设到外设且由目的端外设流控。 |
| trans_dir | uint8_t | 传输方向：0 表示内存到外设；<br>1 表示外设到内存；<br>2 表示外设到外设。 |
| priority | uint8_t | 传输通道优先级，最低为 0、最高为 3 |
| src_width | uint8_t | 源端传输数据宽度：0 表示 1 Bytes；<br>1 表示 2 Bytes；<br>2 表示 4 Bytes。 |
| dest_width | uint8_t | 目的端传输数据宽度：0 表示 1 Bytes；<br>1 表示 2 Bytes；<br>2 表示 4 Bytes。 |
| burst_length | uint8_t | 传输 burst 长度：0 表示 burst 长度为 1；<br>1 表示 4；<br>2 表示 8；<br>3 表示 16。 |
| src_increment | uint8_t | 源端地址增量模式：0 表示递增；<br>1 表示递减；<br>2 表示不变。 |
| dest_increment | uint8_t | 目的端地址增量模式：0 表示递增；<br>1 表示递减；<br>2 表示不变。 |
| protection | uint8_t | DMA 保护控制位，用于驱动 AHB HPROT[3:1] 总线：0 表示 HPROT[1]；<br>1 表示 HPROT[2]；<br>2 表示 HPROT[3]。 |

## Macros

### DMA_CHANNEL_MAX_NUM <a id="DMA_CHANNEL_MAX_NUM"></a>

```c
#define DMA_CHANNEL_MAX_NUM         B_DMA_CHANNEL_MAX_NUM
```

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```

### ERRCODE_DMA_NOT_INIT <a id="ERRCODE_DMA_NOT_INIT"></a>

```c
#define ERRCODE_DMA_NOT_INIT                                0x80001100
```

### ERRCODE_DMA_INVALID_PARAMETER <a id="ERRCODE_DMA_INVALID_PARAMETER"></a>

```c
#define ERRCODE_DMA_INVALID_PARAMETER                       0x80001102
```

### ERRCODE_DMA_RET_NO_AVAIL_CH <a id="ERRCODE_DMA_RET_NO_AVAIL_CH"></a>

```c
#define ERRCODE_DMA_RET_NO_AVAIL_CH                         0x80001103
```
