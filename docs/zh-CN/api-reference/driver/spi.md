# SPI

SPI (Serial Peripheral Interface) 提供串行外设接口的主机与从机模式数据收发能力，支持轮询、DMA (Direct Memory Access)、中断三种传输模式以及轮询与 DMA 自动切换模式，并支持 QSPI (Quad SPI) 帧格式、CRC (Cyclic Redundancy Check) 校验、环回测试与低功耗挂起恢复等配置。

**模块公共头文件**

```c
#include "include/driver/spi.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_spi_init](#uapi_spi_init) | 初始化指定的 SPI 总线 |
| [uapi_spi_deinit](#uapi_spi_deinit) | 去初始化指定的 SPI 总线 |
| [uapi_spi_set_tmod](#uapi_spi_set_tmod) | 设置 SPI 传输模式及接收数据帧数 |
| [uapi_spi_set_attr](#uapi_spi_set_attr) | 设置 SPI 基础配置参数 |
| [uapi_spi_get_attr](#uapi_spi_get_attr) | 读取 SPI 基础配置参数 |
| [uapi_spi_set_extra_attr](#uapi_spi_set_extra_attr) | 设置 SPI 高级配置参数 |
| [uapi_spi_get_extra_attr](#uapi_spi_get_extra_attr) | 读取 SPI 高级配置参数 |
| [uapi_spi_select_slave](#uapi_spi_select_slave) | 主机模式下选择对通的从机设备 |
| [uapi_spi_master_write](#uapi_spi_master_write) | 主机模式向从机写入数据 |
| [uapi_spi_master_read](#uapi_spi_master_read) | 主机模式从从机读取数据 |
| [uapi_spi_master_writeread](#uapi_spi_master_writeread) | 主机模式同时写入与读取数据 |
| [uapi_spi_slave_write](#uapi_spi_slave_write) | 从机模式向主机写入数据 |
| [uapi_spi_slave_read](#uapi_spi_slave_read) | 从机模式从主机读取数据 |
| [uapi_spi_slave_writeread](#uapi_spi_slave_writeread) | 从机模式同时写入与读取数据 |
| [uapi_spi_set_dma_mode](#uapi_spi_set_dma_mode) | 使能或去使能 DMA 模式传输 |
| [uapi_spi_set_irq_mode](#uapi_spi_set_irq_mode) | 使能或去使能中断模式传输并注册回调 |
| [uapi_spi_set_loop_back_mode](#uapi_spi_set_loop_back_mode) | 使能或去使能环回测试模式 |
| [uapi_spi_set_crc_mode](#uapi_spi_set_crc_mode) | 设置 SPI 收发 CRC 校验模式 |
| [uapi_spi_suspend](#uapi_spi_suspend) | 挂起所有 SPI 通道 |
| [uapi_spi_resume](#uapi_spi_resume) | 恢复所有 SPI 通道 |

## Functions

### uapi_spi_init <a id="uapi_spi_init"></a>

```c
errcode_t uapi_spi_init(spi_bus_t bus, spi_attr_t *attr, spi_extra_attr_t *extra_attr)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 初始化指定 SPI 总线，按入参应用基础与高级配置参数
- 对已初始化的总线重复调用时直接返回成功，不重复执行初始化流程

**前置条件**

- 调用时序约束：调用本模块其他接口前必须先调用本接口成功返回
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待初始化的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| attr | spi_attr_t * | SPI 基础配置参数指针 | 不为NULL |
| extra_attr | spi_extra_attr_t * | SPI 高级配置参数指针 | - |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 参数合法且初始化成功，或总线已初始化 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM):0x80000001 | 参数无效 | bus 大于等于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) 或 attr 为空 |
| Other | 其他错误码，参考errcode_t | HAL 初始化失败 |

**参考案例**

- `src/application/samples/peripheral/spi/spi_master_demo.c`
- `src/application/samples/peripheral/spi/spi_slave_demo.c`

### uapi_spi_deinit <a id="uapi_spi_deinit"></a>

```c
errcode_t uapi_spi_deinit(spi_bus_t bus)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 去初始化指定 SPI 总线，释放相关资源
- 对未初始化的总线调用时直接返回成功

**前置条件**

- 调用时序约束：应在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待去初始化的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 参数合法且去初始化成功，或总线未初始化 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM):0x80000001 | 参数无效 | bus 大于等于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| Other | 其他错误码，参考errcode_t | HAL 去初始化失败 |

### uapi_spi_set_tmod <a id="uapi_spi_set_tmod"></a>

```c
errcode_t uapi_spi_set_tmod(spi_bus_t bus, hal_spi_trans_mode_t tmod, uint8_t data_frame_num)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 设置指定 SPI 总线的传输模式与接收数据帧数
- 传输模式与接收数据帧数通过属性结构体配置
- 用于在运行时切换收发模式、发送模式、接收模式、EEPROM 读模式

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待设置的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| tmod | hal_spi_trans_mode_t | SPI 传输模式 | [HAL_SPI_TRANS_MODE_TXRX](#hal_spi_trans_mode_t):0 / [HAL_SPI_TRANS_MODE_TX](#hal_spi_trans_mode_t):1 / [HAL_SPI_TRANS_MODE_RX](#hal_spi_trans_mode_t):2 / [HAL_SPI_TRANS_MODE_EEPROM](#hal_spi_trans_mode_t):3 |
| data_frame_num | uint8_t | SPI 接收数据帧数量 | 0 ~ 255 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 参数合法且设置成功 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM):0x80000001 | 参数无效 | bus 大于等于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) 或 tmod 大于等于 HAL_SPI_TRANS_MODE_MAX |
| Other | 其他错误码，参考errcode_t | HAL 控制接口执行失败 |

### uapi_spi_set_attr <a id="uapi_spi_set_attr"></a>

```c
errcode_t uapi_spi_set_attr(spi_bus_t bus, spi_attr_t *attr)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 设置指定 SPI 总线的基础配置参数
- 基础配置参数通过硬件控制接口下发
- 用于运行时更新主机从机模式、时钟极性相位、帧格式、帧长度等参数

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待设置的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| attr | spi_attr_t * | SPI 基础配置参数指针 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 参数合法且设置成功 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM):0x80000001 | 参数无效 | bus 大于等于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) 或 attr 为空 |
| Other | 其他错误码，参考errcode_t | HAL 控制接口执行失败 |

### uapi_spi_get_attr <a id="uapi_spi_get_attr"></a>

```c
errcode_t uapi_spi_get_attr(spi_bus_t bus, spi_attr_t *attr)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 读取指定 SPI 总线的基础配置参数
- 参数由硬件控制接口拷贝到调用方提供的结构体
- 用于运行时获取当前主机从机模式、时钟极性相位、帧格式、帧长度等参数

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待读取的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| attr | spi_attr_t * | 输出当前 SPI 基础配置参数，由调用方分配内存、接口填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 参数合法且读取成功 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM):0x80000001 | 参数无效 | bus 大于等于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) 或 attr 为空 |
| Other | 其他错误码，参考errcode_t | HAL 控制接口执行失败 |

### uapi_spi_set_extra_attr <a id="uapi_spi_set_extra_attr"></a>

```c
errcode_t uapi_spi_set_extra_attr(spi_bus_t bus, spi_extra_attr_t *extra_attr)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 设置指定 SPI 总线的高级配置参数
- 高级配置参数通过硬件控制接口下发
- 用于运行时更新 DMA 收发使用、QSPI 参数、Single SPI 参数等配置

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待设置的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| extra_attr | spi_extra_attr_t * | SPI 高级配置参数指针 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 参数合法且设置成功 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM):0x80000001 | 参数无效 | bus 大于等于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) 或 extra_attr 为空 |
| Other | 其他错误码，参考errcode_t | HAL 控制接口执行失败 |

### uapi_spi_get_extra_attr <a id="uapi_spi_get_extra_attr"></a>

```c
errcode_t uapi_spi_get_extra_attr(spi_bus_t bus, spi_extra_attr_t *extra_attr)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 读取指定 SPI 总线的高级配置参数
- 参数由硬件控制接口拷贝到调用方提供的结构体
- 用于运行时获取当前 DMA 收发使用、QSPI 参数、Single SPI 参数等配置

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待读取的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| extra_attr | spi_extra_attr_t * | 输出当前 SPI 高级配置参数，由调用方分配内存、接口填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 参数合法且读取成功 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM):0x80000001 | 参数无效 | bus 大于等于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) 或 extra_attr 为空 |
| Other | 其他错误码，参考errcode_t | HAL 控制接口执行失败 |

### uapi_spi_select_slave <a id="uapi_spi_select_slave"></a>

```c
errcode_t uapi_spi_select_slave(spi_bus_t bus, spi_slave_t cs)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 主机模式下选择指定 SPI 总线需要对通的从机设备
- 通过硬件控制接口完成从机选择
- 仅在主机模式下有效

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 依赖关系：总线必须配置为主机模式
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待操作的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| cs | [spi_slave_t](#spi_slave_t) | 被选中的从机设备 | [SPI_SLAVE0](#spi_slave_t):0（有效值小于 [SPI_SLAVE_MAX_NUM](#spi_slave_t):1） |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 参数合法且选择成功 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM):0x80000001 | 参数无效 | bus 大于等于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) 或 cs 大于等于 SPI_SLAVE_MAX_NUM |
| [ERRCODE_SPI_MODE_MISMATCH](#ERRCODE_SPI_MODE_MISMATCH):0x80001332 | 模式不匹配 | 总线未配置为主机模式 |
| Other | 其他错误码，参考errcode_t | HAL 控制接口执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SPI_SUPPORT_MASTER | 特性宏 | 支持 SPI 主机功能（接口级，包裹接口声明与实现） | y |

### uapi_spi_master_write <a id="uapi_spi_master_write"></a>

```c
errcode_t uapi_spi_master_write(spi_bus_t bus, const spi_xfer_data_t *data, uint32_t timeout)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 主机模式下将数据写入到从机
- 支持轮询、DMA、中断三种手动切换传输模式以及轮询与 DMA 自动切换模式
- 自动切换模式下根据数据长度与阈值比较结果选择轮询或 DMA 模式

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 依赖关系：总线必须配置为主机模式，传输模式不能与读取模式冲突
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待操作的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| data | const spi_xfer_data_t * | 数据传输结构体指针，包含发送缓冲区与字节数 | 不为NULL |
| timeout | uint32_t | 当前传输的超时时间，轮询模式下为轮询次数，DMA 模式下为超时时间，单位 ms，中断模式下不生效 | - |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 参数合法且写入成功 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM):0x80000001 | 参数无效 | bus 越界、data 为空、DMA 下发送缓冲区为空或字节数对齐不合法 |
| [ERRCODE_SPI_MODE_MISMATCH](#ERRCODE_SPI_MODE_MISMATCH):0x80001332 | 模式不匹配 | 总线未配置为主机模式 |
| [ERRCODE_SPI_INVALID_TMODE](#ERRCODE_SPI_INVALID_TMODE):0x8000133E | 传输模式无效 | 当前传输模式与读取模式相同 |
| [ERRCODE_SPI_TIMEOUT](#ERRCODE_SPI_TIMEOUT):0x80001333 | 传输超时 | FIFO 忙碌检查或并发锁等待超时 |
| [ERRCODE_SPI_DMA_CONFIG_ERROR](#ERRCODE_SPI_DMA_CONFIG_ERROR):0x80001336 | DMA 配置错误 | DMA 通道配置或握手选择失败 |
| [ERRCODE_SPI_DMA_TRANSFER_ERROR](#ERRCODE_SPI_DMA_TRANSFER_ERROR):0x80001337 | DMA 传输错误 | DMA 传输超时或传输未成功 |
| [ERRCODE_SPI_ADD_QUEUE_FAIL](#ERRCODE_SPI_ADD_QUEUE_FAIL):0x8000133B | 入队失败 | 中断模式下发送片段队列已满 |
| Other | 其他错误码，参考errcode_t | HAL 写入接口执行失败 |

**参考案例**

- `src/application/samples/peripheral/spi/spi_master_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SPI_SUPPORT_MASTER | 特性宏 | 支持 SPI 主机功能（接口级，包裹接口声明与实现） | y |

### uapi_spi_master_read <a id="uapi_spi_master_read"></a>

```c
errcode_t uapi_spi_master_read(spi_bus_t bus, const spi_xfer_data_t *data, uint32_t timeout)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 主机模式下从从机读取数据
- 支持轮询、DMA、中断三种手动切换传输模式以及轮询与 DMA 自动切换模式
- 自动切换模式下根据数据长度与阈值比较结果选择轮询或 DMA 模式

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 依赖关系：总线必须配置为主机模式，传输模式不能与发送模式冲突
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待操作的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| data | const spi_xfer_data_t * | 数据传输结构体指针，包含接收缓冲区与字节数 | 不为NULL，且 rx_buff 不为NULL、rx_bytes 大于0 |
| timeout | uint32_t | 当前传输的超时时间，轮询模式下为轮询次数，DMA 模式下为超时时间，单位 ms，中断模式下不生效 | - |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 参数合法且读取成功 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM):0x80000001 | 参数无效 | bus 越界、data 为空、rx_buff 为空、rx_bytes 为 0，或 DMA 下字节数对齐不合法 |
| [ERRCODE_SPI_MODE_MISMATCH](#ERRCODE_SPI_MODE_MISMATCH):0x80001332 | 模式不匹配 | 总线未配置为主机模式 |
| [ERRCODE_SPI_INVALID_TMODE](#ERRCODE_SPI_INVALID_TMODE):0x8000133E | 传输模式无效 | 当前传输模式与发送模式相同 |
| [ERRCODE_SPI_TIMEOUT](#ERRCODE_SPI_TIMEOUT):0x80001333 | 传输超时 | FIFO 忙碌检查或并发锁等待超时 |
| [ERRCODE_SPI_CONFIG_FAIL](#ERRCODE_SPI_CONFIG_FAIL):0x80001330 | 配置失败 | DMA 读路径下帧字节数为 0 或属性设置失败 |
| [ERRCODE_SPI_DMA_CONFIG_ERROR](#ERRCODE_SPI_DMA_CONFIG_ERROR):0x80001336 | DMA 配置错误 | DMA 通道配置或握手选择失败 |
| [ERRCODE_SPI_DMA_TRANSFER_ERROR](#ERRCODE_SPI_DMA_TRANSFER_ERROR):0x80001337 | DMA 传输错误 | DMA 传输超时或传输未成功 |
| Other | 其他错误码，参考errcode_t | HAL 读取接口执行失败 |

**参考案例**

- `src/application/samples/peripheral/spi/spi_master_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SPI_SUPPORT_MASTER | 特性宏 | 支持 SPI 主机功能（接口级，包裹接口声明与实现） | y |

### uapi_spi_master_writeread <a id="uapi_spi_master_writeread"></a>

```c
errcode_t uapi_spi_master_writeread(spi_bus_t bus, const spi_xfer_data_t *data, uint32_t timeout)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 主机模式下同时写入与读取数据
- 支持轮询、DMA 两种传输模式以及轮询与 DMA 自动切换模式
- 自动切换模式下根据数据长度与阈值比较结果选择轮询或 DMA 模式

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 依赖关系：总线必须配置为主机模式，传输模式不能与发送模式冲突
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待操作的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| data | const spi_xfer_data_t * | 数据传输结构体指针，同时承载发送与接收缓冲区及字节数 | 不为NULL，且 rx_buff 不为NULL、rx_bytes 大于0 |
| timeout | uint32_t | 当前传输的超时时间，轮询模式下为轮询次数，DMA 模式下为超时时间，单位 ms，中断模式下不生效 | - |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 参数合法且写入读取成功 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM):0x80000001 | 参数无效 | bus 越界、data 为空、rx_buff 为空、rx_bytes 为 0，或 DMA 下发送缓冲区为空、字节数对齐不合法 |
| [ERRCODE_SPI_MODE_MISMATCH](#ERRCODE_SPI_MODE_MISMATCH):0x80001332 | 模式不匹配 | 总线未配置为主机模式 |
| [ERRCODE_SPI_INVALID_TMODE](#ERRCODE_SPI_INVALID_TMODE):0x8000133E | 传输模式无效 | 当前传输模式与发送模式相同 |
| [ERRCODE_SPI_TIMEOUT](#ERRCODE_SPI_TIMEOUT):0x80001333 | 传输超时 | FIFO 忙碌检查或并发锁等待超时 |
| [ERRCODE_SPI_DMA_CONFIG_ERROR](#ERRCODE_SPI_DMA_CONFIG_ERROR):0x80001336 | DMA 配置错误 | DMA 通道配置或握手选择失败 |
| [ERRCODE_SPI_DMA_TRANSFER_ERROR](#ERRCODE_SPI_DMA_TRANSFER_ERROR):0x80001337 | DMA 传输错误 | DMA 传输超时或传输未成功 |
| Other | 其他错误码，参考errcode_t | HAL 写入或读取接口执行失败 |

**参考案例**

- `src/application/samples/peripheral/spi/spi_master_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SPI_SUPPORT_MASTER | 特性宏 | 支持 SPI 主机功能（接口级，包裹接口声明与实现） | y |

### uapi_spi_slave_write <a id="uapi_spi_slave_write"></a>

```c
errcode_t uapi_spi_slave_write(spi_bus_t bus, const spi_xfer_data_t *data, uint32_t timeout)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 从机模式下向主机写入数据
- 支持轮询、DMA、中断三种手动切换传输模式以及轮询与 DMA 自动切换模式
- 自动切换模式下根据数据长度与阈值比较结果选择轮询或 DMA 模式

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 依赖关系：总线必须配置为从机模式，传输模式不能与读取模式冲突
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待操作的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| data | const spi_xfer_data_t * | 数据传输结构体指针，包含发送缓冲区与字节数 | 不为NULL，且 tx_buff 不为NULL、tx_bytes 大于0 |
| timeout | uint32_t | 当前传输的超时时间，轮询模式下为轮询次数，DMA 模式下为超时时间，单位 ms，中断模式下不生效 | - |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 参数合法且写入成功 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM):0x80000001 | 参数无效 | data 为空、tx_buff 为空、tx_bytes 为 0，或 DMA 下字节数对齐不合法 |
| [ERRCODE_SPI_MODE_MISMATCH](#ERRCODE_SPI_MODE_MISMATCH):0x80001332 | 模式不匹配 | 总线未配置为从机模式 |
| [ERRCODE_SPI_INVALID_TMODE](#ERRCODE_SPI_INVALID_TMODE):0x8000133E | 传输模式无效 | 当前传输模式与读取模式相同 |
| [ERRCODE_SPI_TIMEOUT](#ERRCODE_SPI_TIMEOUT):0x80001333 | 传输超时 | FIFO 忙碌检查或并发锁等待超时 |
| [ERRCODE_SPI_DMA_CONFIG_ERROR](#ERRCODE_SPI_DMA_CONFIG_ERROR):0x80001336 | DMA 配置错误 | DMA 通道配置或握手选择失败 |
| [ERRCODE_SPI_DMA_TRANSFER_ERROR](#ERRCODE_SPI_DMA_TRANSFER_ERROR):0x80001337 | DMA 传输错误 | DMA 传输超时或传输未成功 |
| [ERRCODE_SPI_ADD_QUEUE_FAIL](#ERRCODE_SPI_ADD_QUEUE_FAIL):0x8000133B | 入队失败 | 中断模式下发送片段队列已满 |
| Other | 其他错误码，参考errcode_t | HAL 写入接口执行失败 |

**参考案例**

- `src/application/samples/peripheral/spi/spi_slave_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SPI_SUPPORT_SLAVE | 特性宏 | 支持 SPI 从机功能（接口级，包裹接口声明与实现） | y |

### uapi_spi_slave_read <a id="uapi_spi_slave_read"></a>

```c
errcode_t uapi_spi_slave_read(spi_bus_t bus, const spi_xfer_data_t *data, uint32_t timeout)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 从机模式下从主机读取数据
- 支持轮询、DMA、中断三种手动切换传输模式以及轮询与 DMA 自动切换模式
- 自动切换模式下根据数据长度与阈值比较结果选择轮询或 DMA 模式

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 依赖关系：总线必须配置为从机模式，传输模式不能与发送模式冲突
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待操作的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| data | const spi_xfer_data_t * | 数据传输结构体指针，包含接收缓冲区与字节数 | 不为NULL，且 rx_buff 不为NULL、rx_bytes 大于0 |
| timeout | uint32_t | 当前传输的超时时间，轮询模式下为轮询次数，DMA 模式下为超时时间，单位 ms，中断模式下不生效 | - |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 参数合法且读取成功 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM):0x80000001 | 参数无效 | bus 越界、data 为空、rx_buff 为空、rx_bytes 为 0，或 DMA 下字节数对齐不合法 |
| [ERRCODE_SPI_MODE_MISMATCH](#ERRCODE_SPI_MODE_MISMATCH):0x80001332 | 模式不匹配 | 总线未配置为从机模式 |
| [ERRCODE_SPI_INVALID_TMODE](#ERRCODE_SPI_INVALID_TMODE):0x8000133E | 传输模式无效 | 当前传输模式与发送模式相同 |
| [ERRCODE_SPI_TIMEOUT](#ERRCODE_SPI_TIMEOUT):0x80001333 | 传输超时 | FIFO 忙碌检查或并发锁等待超时 |
| [ERRCODE_SPI_DMA_CONFIG_ERROR](#ERRCODE_SPI_DMA_CONFIG_ERROR):0x80001336 | DMA 配置错误 | DMA 通道配置或握手选择失败 |
| [ERRCODE_SPI_DMA_TRANSFER_ERROR](#ERRCODE_SPI_DMA_TRANSFER_ERROR):0x80001337 | DMA 传输错误 | DMA 传输超时或传输未成功 |
| Other | 其他错误码，参考errcode_t | HAL 读取接口执行失败 |

**参考案例**

- `src/application/samples/peripheral/spi/spi_slave_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SPI_SUPPORT_SLAVE | 特性宏 | 支持 SPI 从机功能（接口级，包裹接口声明与实现） | y |

### uapi_spi_slave_writeread <a id="uapi_spi_slave_writeread"></a>

```c
errcode_t uapi_spi_slave_writeread(spi_bus_t bus, const spi_xfer_data_t *data, uint32_t timeout)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 从机模式下同时写入与读取数据
- 支持轮询、DMA 两种传输模式以及轮询与 DMA 自动切换模式
- 自动切换模式下根据数据长度与阈值比较结果选择轮询或 DMA 模式

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 依赖关系：总线必须配置为从机模式，传输模式不能与发送模式冲突
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待操作的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| data | const spi_xfer_data_t * | 数据传输结构体指针，同时承载发送与接收缓冲区及字节数 | 不为NULL，且 rx_buff 不为NULL、rx_bytes 大于0 |
| timeout | uint32_t | 当前传输的超时时间，轮询模式下为轮询次数，DMA 模式下为超时时间，单位 ms，中断模式下不生效 | - |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 参数合法且写入读取成功 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM):0x80000001 | 参数无效 | bus 越界、data 为空、rx_buff 为空、rx_bytes 为 0，或 DMA 下字节数对齐不合法 |
| [ERRCODE_SPI_MODE_MISMATCH](#ERRCODE_SPI_MODE_MISMATCH):0x80001332 | 模式不匹配 | 总线未配置为从机模式 |
| [ERRCODE_SPI_INVALID_TMODE](#ERRCODE_SPI_INVALID_TMODE):0x8000133E | 传输模式无效 | 当前传输模式与发送模式相同 |
| [ERRCODE_SPI_TIMEOUT](#ERRCODE_SPI_TIMEOUT):0x80001333 | 传输超时 | FIFO 忙碌检查或并发锁等待超时 |
| [ERRCODE_SPI_DMA_CONFIG_ERROR](#ERRCODE_SPI_DMA_CONFIG_ERROR):0x80001336 | DMA 配置错误 | DMA 通道配置或握手选择失败 |
| [ERRCODE_SPI_DMA_TRANSFER_ERROR](#ERRCODE_SPI_DMA_TRANSFER_ERROR):0x80001337 | DMA 传输错误 | DMA 传输超时或传输未成功 |
| Other | 其他错误码，参考errcode_t | HAL 写入或读取接口执行失败 |

**参考案例**

- `src/application/samples/peripheral/spi/spi_slave_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SPI_SUPPORT_SLAVE | 特性宏 | 支持 SPI 从机功能（接口级，包裹接口声明与实现） | y |

### uapi_spi_set_dma_mode <a id="uapi_spi_set_dma_mode"></a>

```c
errcode_t uapi_spi_set_dma_mode(spi_bus_t bus, bool en, const spi_dma_config_t *dma_cfg)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 使能或去使能指定 SPI 总线的 DMA 模式传输
- 使能时按入参 DMA 配置生效
- 去使能时清零 DMA 收发数据电平

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用，使能 DMA 模式前需完成 DMA 初始化与打开
- 依赖关系：中断模式下使能 DMA 会被拒绝
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待设置的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| en | bool | 是否使能 DMA 传输 | true / false |
| dma_cfg | const spi_dma_config_t * | DMA 配置结构体指针，去使能时配置为 NULL | 使能时不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 参数合法且设置成功 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM):0x80000001 | 参数无效 | bus 大于等于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| [ERRCODE_SPI_DMA_IRQ_MODE_MUTEX](#ERRCODE_SPI_DMA_IRQ_MODE_MUTEX):0x8000133C | DMA 与中断模式互斥 | 中断模式已使能时使能 DMA |

**参考案例**

- `src/application/samples/peripheral/spi/spi_master_demo.c`
- `src/application/samples/peripheral/spi/spi_slave_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SPI_SUPPORT_DMA | 特性宏 | 支持 SPI DMA 模式传输功能（接口级，包裹接口声明） | n |
| CONFIG_SPI_SUPPORT_POLL_AND_DMA_AUTO_SWITCH | 特性宏 | 支持轮询与 DMA 自动切换特性（接口级，取反条件：未启用时接口可用） | n |

### uapi_spi_set_irq_mode <a id="uapi_spi_set_irq_mode"></a>

```c
errcode_t uapi_spi_set_irq_mode(spi_bus_t bus, bool irq_en, spi_rx_callback_t rx_callback, spi_tx_callback_t tx_callback)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 使能或去使能指定 SPI 总线的中断模式传输
- 使能时注册接收完成回调与发送完成回调
- 去使能时清空已注册的接收与发送回调

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 依赖关系：DMA 模式已使能时使能中断会被拒绝
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待设置的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| irq_en | bool | 是否使用中断模式 | true / false |
| rx_callback | spi_rx_callback_t | 接收完成回调函数，在中断上下文中调用 | 使能时不为NULL |
| tx_callback | spi_tx_callback_t | 发送完成回调函数，在中断上下文中调用 | 使能时不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 参数合法且设置成功 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM):0x80000001 | 参数无效 | bus 大于等于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| [ERRCODE_SPI_DMA_IRQ_MODE_MUTEX](#ERRCODE_SPI_DMA_IRQ_MODE_MUTEX):0x8000133C | DMA 与中断模式互斥 | DMA 模式已使能时使能中断 |

**参考案例**

- `src/application/samples/peripheral/spi/spi_master_demo.c`
- `src/application/samples/peripheral/spi/spi_slave_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SPI_SUPPORT_INTERRUPT | 特性宏 | 支持 SPI 中断模式传输功能（接口级，包裹接口声明） | n |
| CONFIG_SPI_SUPPORT_POLL_AND_DMA_AUTO_SWITCH | 特性宏 | 支持轮询与 DMA 自动切换特性（接口级，取反条件：未启用时接口可用） | n |

### uapi_spi_set_loop_back_mode <a id="uapi_spi_set_loop_back_mode"></a>

```c
errcode_t uapi_spi_set_loop_back_mode(spi_bus_t bus, bool loopback_en)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 设置指定 SPI 总线是否进入环回测试模式
- 调用后直接返回成功，不改变硬件配置
- 用于预留环回测试能力

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 依赖关系：需开启 CONFIG_SPI_SUPPORT_LOOPBACK 配置项接口才可见
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待设置的 SPI 总线编号 | - |
| loopback_en | bool | 环回模式使能或去使能 | true / false |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 调用即返回成功 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SPI_SUPPORT_LOOPBACK | 特性宏 | 支持环回测试模式（接口级，包裹函数声明与实现体） | n |

### uapi_spi_set_crc_mode <a id="uapi_spi_set_crc_mode"></a>

```c
errcode_t uapi_spi_set_crc_mode(spi_bus_t bus, const spi_crc_config_t *crc_config, spi_crc_err_callback_t cb)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 设置指定 SPI 总线的发送与接收 CRC 校验模式
- 注册 CRC 校验错误回调函数
- 调用后直接返回成功，不改变硬件配置

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 依赖关系：需开启 CONFIG_SPI_SUPPORT_CRC 配置项接口才可见
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [spi_bus_t](#spi_bus_t) | 指定待设置的 SPI 总线编号 | - |
| crc_config | const spi_crc_config_t * | CRC 配置参数指针 | - |
| cb | spi_crc_err_callback_t | CRC 校验错误回调函数 | - |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 调用即返回成功 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SPI_SUPPORT_CRC | 特性宏 | 支持 CRC 校验（接口级，包裹函数声明与实现体） | n |

### uapi_spi_suspend <a id="uapi_spi_suspend"></a>

```c
errcode_t uapi_spi_suspend(uintptr_t arg)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 挂起所有 SPI 通道
- 通过硬件控制接口完成挂起操作
- 在开启低功耗时钟控制或 DMA 时联动执行对应的关闭动作

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 依赖关系：需开启 CONFIG_SPI_SUPPORT_LPM 配置项接口才可见
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| arg | uintptr_t | 挂起参数，实际作为 SPI 总线编号使用 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 总线未初始化或挂起成功 |
| [ERRCODE_FAIL](#ERRCODE_FAIL):0xFFFFFFFF | 执行失败 | HAL 挂起控制接口执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SPI_SUPPORT_LPM | 特性宏 | 支持低功耗模式挂起与恢复（接口级，包裹函数声明与实现体） | n |

### uapi_spi_resume <a id="uapi_spi_resume"></a>

```c
errcode_t uapi_spi_resume(uintptr_t arg)
```

**声明头文件**

```c
#include "include/driver/spi.h"
```

**功能说明**

- 恢复所有 SPI 通道
- 通过硬件控制接口完成恢复操作
- 在开启低功耗时钟控制或 DMA 时联动执行对应的恢复动作

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用，且应先调用过 [uapi_spi_suspend](#uapi_spi_suspend)
- 依赖关系：需开启 CONFIG_SPI_SUPPORT_LPM 配置项接口才可见
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| arg | uintptr_t | 恢复参数，实际作为 SPI 总线编号使用 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 总线未初始化或恢复成功 |
| [ERRCODE_FAIL](#ERRCODE_FAIL):0xFFFFFFFF | 执行失败 | HAL 恢复控制接口执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SPI_SUPPORT_LPM | 特性宏 | 支持低功耗模式挂起与恢复（接口级，包裹函数声明与实现体） | n |

## Type definitions

### spi_attr_t <a id="spi_attr_t"></a>

```c
typedef hal_spi_attr_t spi_attr_t;
```

**使用说明**

用于 [uapi_spi_init](#uapi_spi_init)、[uapi_spi_set_attr](#uapi_spi_set_attr)、[uapi_spi_get_attr](#uapi_spi_get_attr) 的基础配置参数载体。

### spi_extra_attr_t <a id="spi_extra_attr_t"></a>

```c
typedef hal_spi_extra_attr_t spi_extra_attr_t;
```

**使用说明**

用于 [uapi_spi_init](#uapi_spi_init)、[uapi_spi_set_extra_attr](#uapi_spi_set_extra_attr)、[uapi_spi_get_extra_attr](#uapi_spi_get_extra_attr) 的高级配置参数载体。

### spi_xfer_data_t <a id="spi_xfer_data_t"></a>

```c
typedef hal_spi_xfer_data_t spi_xfer_data_t;
```

**使用说明**

用于主从机读写接口的数据传输结构体载体。

### spi_rx_callback_t <a id="spi_rx_callback_t"></a>

```c
typedef void (*spi_rx_callback_t)(const void *buffer, uint32_t length, bool error);
```

**使用说明**

通过 [uapi_spi_set_irq_mode](#uapi_spi_set_irq_mode) 注册，在中断上下文中被调用。buffer 指向接收缓冲区，由读取接口的参数传入；length 为已接收的数据长度；error 表示 SPI 传输是否存在错误，包括接收上限溢出错误与接收下限溢出错误。

### spi_tx_callback_t <a id="spi_tx_callback_t"></a>

```c
typedef void (*spi_tx_callback_t)(const void *buffer, uint32_t length);
```

**使用说明**

通过 [uapi_spi_set_irq_mode](#uapi_spi_set_irq_mode) 注册，在中断上下文中被调用。buffer 指向写入缓冲区，由写接口的参数传入；length 为已写入的数据长度。

### spi_crc_err_callback_t <a id="spi_crc_err_callback_t"></a>

```c
typedef void (*spi_crc_err_callback_t)(spi_bus_t bus);
```

**使用说明**

通过 [uapi_spi_set_crc_mode](#uapi_spi_set_crc_mode) 注册，用于 CRC 校验错误时的回调通知，参数 bus 为发生错误的 SPI 总线编号。

### typedef_errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块返回类型为 errcode_t 的对外接口的返回值类型。

## Enumerations

### enum spi_bus_t <a id="spi_bus_t"></a>

```c
typedef enum {
    I2C_BUS_0,               // !< I2C0
    I2C_BUS_1,               // !< I2C1
    I2C_BUS_NONE = I2C_BUS_MAX_NUMBER
} i2c_bus_t;


/**
 * @brief  Definition of SPI bus index.
 */
typedef enum {
    SPI_BUS_0 = 0,         // SPI
    SPI_BUS_MAX = SPI_BUS_0,
    SPI_BUS_1 = 1,         // QSPI
    QSPI_BUS_1 = SPI_BUS_1,
    SPI_BUS_NONE = SPI_BUS_MAX_NUMBER
} spi_bus_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SPI_BUS_0 | 0 | SPI 总线 0 |
| SPI_BUS_MAX | 0 | SPI 总线数量上限（等同 SPI_BUS_0） |
| SPI_BUS_1 | 1 | QSPI 总线 1 |
| QSPI_BUS_1 | 1 | QSPI 总线 1（等同 SPI_BUS_1） |
| SPI_BUS_NONE | 2 | 无效/未指定的 SPI 总线编号（等同 SPI_BUS_MAX_NUMBER） |

### enum spi_slave_t <a id="spi_slave_t"></a>

```c
typedef enum {
    HAL_SPI_DMA_CONTROL_DISABLE = 0,        //!< Disables the transmit fifo and the receive fifo dma channel.
    HAL_SPI_DMA_CONTROL_RX_ENABLE = 1,      //!< Enables the receive fifo dma channel.
    HAL_SPI_DMA_CONTROL_TX_ENABLE = 2,      //!< Enables the transmit fifo dma channel.
    HAL_SPI_DMA_CONTROL_TXRX_ENABLE = 3,    //!< Enables the transmit fifo and the receive fifo dma channel.
    HAL_SPI_DMA_CONTROL_MAX_NUM,
    HAL_SPI_DMA_CONTROL_NONE = HAL_SPI_DMA_CONTROL_MAX_NUM,
} hal_spi_dma_control_t;

/**
 * @brief  SPI mode.
 */
typedef enum spi_mode {
    SPI_MODE_SLAVE,         /*!< SPI Slave mode. */
    SPI_MODE_MASTER,        /*!< SPI Master mode. */
    SPI_MODE_MAX_NUM,
    SPI_MODE_NONE = SPI_MODE_MAX_NUM
} spi_mode_t;

/**
 * @brief  SPI slave select.
 */
typedef enum spi_slave {
    SPI_SLAVE0 = 0,         /*!< SPI Slave index 0. */
    SPI_SLAVE_MAX_NUM,
    SPI_SLAVE_NONE = SPI_SLAVE_MAX_NUM
} spi_slave_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SPI_SLAVE0 | 0 | SPI 从机索引 0 |
| SPI_SLAVE_MAX_NUM | 1 | SPI 从机数量上限 |
| SPI_SLAVE_NONE | 1 | 无效/未指定的从机编号（等同 SPI_SLAVE_MAX_NUM） |

### hal_spi_trans_mode_t <a id="hal_spi_trans_mode_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum hal_spi_trans_mode {
    HAL_SPI_TRANS_MODE_TXRX = 0,
    HAL_SPI_TRANS_MODE_TX,
    HAL_SPI_TRANS_MODE_RX,
    HAL_SPI_TRANS_MODE_EEPROM,
    HAL_SPI_TRANS_MODE_MAX
} hal_spi_trans_mode_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| HAL_SPI_TRANS_MODE_TXRX | 0 | 收发模式 |
| HAL_SPI_TRANS_MODE_TX | 1 | 发送模式 |
| HAL_SPI_TRANS_MODE_RX | 2 | 接收模式 |
| HAL_SPI_TRANS_MODE_EEPROM | 3 | EEPROM 读模式 |
| HAL_SPI_TRANS_MODE_MAX | 4 | 传输模式上限值 |

## Structures

### spi_dma_config_t <a id="spi_dma_config_t"></a>

```c
typedef struct spi_dma_config {
    uint8_t src_width;
    uint8_t dest_width;
    uint8_t burst_length;
    uint8_t priority;
} spi_dma_config_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| src_width | uint8_t | 源端传输数据宽度，0 为 1 字节、1 为 2 字节、2 为 4 字节 |
| dest_width | uint8_t | 目的端传输数据宽度，0 为 1 字节、1 为 2 字节、2 为 4 字节 |
| burst_length | uint8_t | 每次目的 burst 请求写入的数据量，0 为 1、1 为 4、2 为 8、3 为 16 |
| priority | uint8_t | 传输通道优先级，范围为 0 ~ 3 |

### spi_crc_config_t <a id="spi_crc_config_t"></a>

```c
typedef struct spi_crc_config {
    uint32_t  tx_crc_len;
    uint32_t  rx_crc_len;
    uint32_t  tx_crc_ini;
    uint32_t  rx_crc_ini;
    uint32_t  tx_crc_poly;
    uint32_t  rx_crc_poly;
    uint32_t  tx_crc_xor_out;
    uint32_t  rx_crc_xor_out;
    bool      tx_crc_refin;
    bool      tx_crc_refout;
    bool      rx_crc_refin;
    bool      rx_crc_refout;
} spi_crc_config_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| tx_crc_len | uint32_t | 发送方向在此长度之前发送 CRC 校验数据 |
| rx_crc_len | uint32_t | 接收方向在此长度之前接收 CRC 校验数据 |
| tx_crc_ini | uint32_t | 发送方向 CRC 初始化值 |
| rx_crc_ini | uint32_t | 接收方向 CRC 初始化值 |
| tx_crc_poly | uint32_t | 发送方向 CRC 多项式 |
| rx_crc_poly | uint32_t | 接收方向 CRC 多项式 |
| tx_crc_xor_out | uint32_t | 发送方向 CRC 结果异或配置 |
| rx_crc_xor_out | uint32_t | 接收方向 CRC 结果异或配置 |
| tx_crc_refin | bool | 发送方向 CRC 输入值翻转配置 |
| tx_crc_refout | bool | 发送方向 CRC 输出值翻转配置 |
| rx_crc_refin | bool | 接收方向 CRC 输入值翻转配置 |
| rx_crc_refout | bool | 接收方向 CRC 输出值翻转配置 |

### struct hal_spi_attr_t <a id="hal_spi_attr_t"></a>

```c
typedef enum hal_spi_ctrl_id {
    SPI_CTRL_SET_ATTR,                  /*!< @if Eng Set SPI basic attribute.
                                             @else   设置基础参数。 @endif */

    SPI_CTRL_GET_ATTR,                  /*!< @if Eng Get SPI basic attribute.
                                             @else   获取基础参数。 @endif */

    SPI_CTRL_SET_EXTRA_ATTR,            /*!< @if Eng Set SPI extral attribute.
                                             @else   设置高级参数。 @endif */

    SPI_CTRL_GET_EXTRA_ATTR,            /*!< @if Eng Get SPI extral attribute.
                                             @else   获取高级参数。 @endif */

    SPI_CTRL_SELECT_SLAVE,              /*!< @if Eng Select the slave.
                                             @else   选择指定的设备。 @endif */

    SPI_CTRL_CHECK_FIFO_BUSY,           /*!< @if Eng Check whether the SPI is busy.
                                             @else   检查SPI是否忙碌状态。 @endif */
#if defined(CONFIG_SPI_SUPPORT_DMA) && (CONFIG_SPI_SUPPORT_DMA == 1)
    SPI_CTRL_SET_DMA_CFG,               /*!< @if Eng Set the DMA transfer enable/disable and datalevel.
                                             @else   设置DMA的传输使能和数据level。 @endif */

    SPI_CTRL_GET_DMA_DATA_ADDR,         /*!< @if Eng Get the DMA transfer data address.
                                             @else   获取DMA的传输数据地址。 @endif */
#endif  /* CONFIG_SPI_SUPPORT_DMA */

#if defined(CONFIG_SPI_SUPPORT_INTERRUPT) && (CONFIG_SPI_SUPPORT_INTERRUPT == 1)
    SPI_CTRL_EN_RXFI_INT,               /*!< @if Eng Enable the Receive FIFO full interrupt.
                                             @else   使能RX FIFO是否已满中断。 @endif */

    SPI_CTRL_CHECK_RX_FIFO_EMPTY,       /*!< @if Eng Check if rx fifo is empty or not.
                                             @else   判断RX FIFO是否为空。 @endif */

    SPI_CTRL_EN_TXEI_INT,               /*!< @if Eng Enable the transmit FIFO empty interrupt.
                                             @else   使能TX FIFO是否为空中断。 @endif */

    SPI_CTRL_CHECK_TX_FIFO_FULL,        /*!< @if Eng Check if tx fifo is full or not.
                                             @else   判断RX FIFO是否已满。 @endif */

    SPI_CTRL_EN_MULTI_MASTER_ERR_INT,   /*!< @if Eng Enable the Multi-Master contention interrupt.
                                             @else   使能双主机竞争中断。 @endif */
#endif  /* CONFIG_SPI_SUPPORT_INTERRUPT */

#if defined(CONFIG_SPI_SUPPORT_LPM) && (CONFIG_SPI_SUPPORT_LPM == 1)
    SPI_CTRL_SUSPEND,                   /*!< @if Eng Suspend all of the spi channels.
                                             @else   挂起所有spi通道。 @endif */
    SPI_CTRL_RESUME,                    /*!< @if Eng Resume all of the spi channels.
                                             @else   挂起所有spi通道。 @endif */
#endif  /* CONFIG_SPI_SUPPORT_LPM */
    SPI_CTRL_SET_TMOD,                  /*!< @if Eng Set SPI transfer mode.
                                             @else   设置SPI传输模式。 @endif */
    SPI_CTRL_MAX,
    SPI_CTRL_ID_INVALID = 0xFF
} hal_spi_ctrl_id_t;

/**
 * @if Eng
 * @brief  Frame Format.
 * @else
 * @brief  帧格式。
 * @endif
 */
typedef enum hal_spi_cfg_frame_format {
    SPI_CFG_FRAME_FORMAT_MOTOROLA_SPI,      /*!< @if Eng Motorolla SPI Frame Format.
                                                 @else   摩托罗拉SPI帧格式。 @endif */

    SPI_CFG_FRAME_FORMAT_TEXAS_SSP,         /*!< @if Eng Texas Instruments SSP Frame Format.
                                                 @else   德州仪器SSP帧格式。 @endif */

    SPI_CFG_FRAME_FORMAT_NS_MICROWIRE,      /*!< @if Eng National Microwire Frame Format.
                                                 @else   国家微线帧格式。 @endif */
    SPI_CFG_FRAME_FORMAT_MAX
} hal_spi_cfg_frame_format_t;

/**
 * @if Eng
 * @brief  Clock polarity.
 * @else
 * @brief  时钟极性。
 * @endif
 */
typedef enum hal_spi_cfg_clk_cpol {
    SPI_CFG_CLK_CPOL_0,                     /*!< @if Eng Inactive state of serial clock is low.
                                                 @else   SPI的非激活状态为低电平。 @endif */

    SPI_CFG_CLK_CPOL_1,                     /*!< @if Eng Inactive state of serial clock is high.
                                                 @else   SPI的非激活状态为高电平。 @endif */
    SPI_CFG_CLK_CPOL_MAX
} hal_spi_cfg_clk_cpol_t;

/**
 * @if Eng
 * @brief  Clock phase.
 * @else
 * @brief  时钟相位。
 * @endif
 */
typedef enum hal_spi_cfg_clk_cpha {
    SPI_CFG_CLK_CPHA_0,                     /*!< @if Eng Serial clock toggles in middle of first data bit.
                                                 @else   SPI时钟在第一个数据位中间切换。 @endif */

    SPI_CFG_CLK_CPHA_1,                     /*!< @if Eng Serial clock toggles at start of first data bit.
                                                 @else   SPI时钟在第一个数据位开始时切换。 @endif */
    SPI_CFG_CLK_CPHA_MAX
} hal_spi_cfg_clk_cpha_t;

/**
 * @if Eng
 * @brief  SPI slave select toggle enable.
 * @else
 * @brief  SPI 从机选择切换使能
 * @endif
 */
typedef enum hal_spi_cfg_sste {
    SPI_CFG_SSTE_DISABLE,                   /*!< @if Eng SPI slave select toggle disable.
                                                         When disable, master should reed all data in slave tx_queue
                                                         at ONE time when reading data from slave device. Otherwise,
                                                         data loss occurs.
                                                 @else   SPI 从机选择切换不使能。
                                                         当此配置不使能，主机从从机读取数据时，需要一次性将从机发送
                                                         队列中的数据读完，否则会出现丢失数据问题。@endif */
    SPI_CFG_SSTE_ENABLE,                    /*!< @if Eng SPI slave select toggle enable.
                                                 @else   SPI 从机选择切换使能 @endif */
    SPI_CFG_SSTE_MAX
} hal_spi_cfg_sste_t;

/**
 * @if Eng
 * @brief  Transfer Mode.
 * @else
 * @brief  传输模式。
 * @endif
 */
typedef enum hal_spi_trans_mode {
    HAL_SPI_TRANS_MODE_TXRX = 0,            /*!< @if Eng Transmit and receive mode.
                                                 @else   收发模式。 @endif */

    HAL_SPI_TRANS_MODE_TX,                  /*!< @if Eng Transmit only / Transmit mode.
                                                 @else   发送模式。 @endif */

    HAL_SPI_TRANS_MODE_RX,                  /*!< @if Eng Receive only / Receive mode.
                                                 @else   接收模式。 @endif */

    HAL_SPI_TRANS_MODE_EEPROM,              /*!< @if Eng EEPROM read mode.
                                                 @else   EEPROM模式。 @endif */
    HAL_SPI_TRANS_MODE_MAX
} hal_spi_trans_mode_t;

/**
 * @if Eng
 * @brief  Data Frame Size.
 * @else
 * @brief  数据帧长度。
 * @endif
 */
typedef enum hal_spi_frame_size {
    HAL_SPI_FRAME_SIZE_8    = 0x07,         /*!< @if Eng 8-bit serial data transfer.
                                                 @else   8-位串行数据传输。 @endif */

    HAL_SPI_FRAME_SIZE_16   = 0x0F,         /*!< @if Eng 16-bit serial data transfer(Not supported now).
                                                 @else   16-位串行数据传输（暂不支持）。 @endif */

    HAL_SPI_FRAME_SIZE_24   = 0x17,         /*!< @if Eng 24-bit serial data transfer(Not supported now).
                                                 @else   24-位串行数据传输（暂不支持）。 @endif */

    HAL_SPI_FRAME_SIZE_32   = 0x1F          /*!< @if Eng 32-bit serial data transfer.
                                                 @else   32-位串行数据传输。 @endif */
} hal_spi_frame_size_t;

/**
 * @if Eng
 * @brief  SPI Frame Format.
 * @else
 * @brief  SPI数据帧格式。
 * @endif
 */
typedef enum hal_spi_frame_format {
    HAL_SPI_FRAME_FORMAT_STANDARD = 0,      /*!< @if Eng SPI Standard frame format.
                                                 @else   标准的单线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_DUAL,              /*!< @if Eng SPI Dual frame format.
                                                 @else   双线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_QUAD,              /*!< @if Eng SPI Quad frame format.
                                                 @else   4线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_OCTAL,             /*!< @if Eng SPI Octal frame format.
                                                 @else   8线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_DOUBLE_OCTAL,      /*!< @if Eng SPI Double Octal frame format.
                                                 @else   16线SPI帧格式。 @endif */
    HAL_SPI_FRAME_FORMAT_SIXT,
    HAL_SPI_FRAME_FORMAT_MAX_NUM,
    HAL_SPI_FRAME_FORMAT_NONE = HAL_SPI_FRAME_FORMAT_MAX_NUM
} hal_spi_frame_format_t;

/**
 * @if Eng
 * @brief  SPI Transfer Types.
 * @else
 * @brief  SPI传输类型。
 * @endif
 */
typedef enum hal_spi_trans_type {
    HAL_SPI_TRANS_TYPE_INST_S_ADDR_S = 0,   /*!< @if Eng Instruction and Address will be sent in standard SPI mode.
                                                 @else   指令和地址使用单线SPI传输。 @endif */

    HAL_SPI_TRANS_TYPE_INST_S_ADDR_Q,       /*!< @if Eng Instruction will be sent in standard mode and address will
                                                         be sent in mode specified by frame format register.
                                                 @else   指令使用单线SPI传输，
                                                         地址按照帧格式寄存器的配置传输。 @endif */

    HAL_SPI_TRANS_TYPE_INST_Q_ADDR_Q,       /*!< @if Eng Both instruction and address will be sent in
                                                         the mode specified by frame format register.
                                                 @else   指令和地址都按照帧格式寄存器的配置传输。 @endif */
    HAL_SPI_TRANS_TYPE_MAX = HAL_SPI_TRANS_TYPE_INST_Q_ADDR_Q
} hal_spi_trans_type_t;

/**
 * @if Eng
 * @brief  SPI length of instruction.
 * @else
 * @brief  SPI指令长度定义。
 * @endif
 */
typedef enum hal_spi_inst_len {
    HAL_SPI_INST_LEN_0 = 0,                 /*!< @if Eng 0-bit (no instruction).
                                                 @else   不携带指令。 @endif */

    HAL_SPI_INST_LEN_4,                     /*!< @if Eng 4-bit instruction.
                                                 @else   4-位指令。 @endif */

    HAL_SPI_INST_LEN_8,                     /*!< @if Eng 8-bit instruction.
                                                 @else   8-位指令。 @endif */

    HAL_SPI_INST_LEN_16,                    /*!< @if Eng 16-bit instruction.
                                                 @else   16-位指令。 @endif */
    HAL_SPI_INST_LEN_MAX = HAL_SPI_INST_LEN_16
} hal_spi_inst_len_t;

/**
 * @if Eng
 * @brief  SPI length of address.
 * @else
 * @brief  SPI地址长度定义。
 * @endif
 */
typedef enum hal_spi_addr_len {
    HAL_SPI_ADDR_LEN_0 = 0,                 /*!< @if Eng 0-bit address length.
                                                 @else   0-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_4,                     /*!< @if Eng 4-bit address length.
                                                 @else   4-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_8,                     /*!< @if Eng 8-bit address length.
                                                 @else   8-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_12,                    /*!< @if Eng 12-bit address length.
                                                 @else   12-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_16,                    /*!< @if Eng 16-bit address length.
                                                 @else   16-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_20,                    /*!< @if Eng 20-bit address length.
                                                 @else   20-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_24,                    /*!< @if Eng 24-bit address length.
                                                 @else   24-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_28,                    /*!< @if Eng 28-bit address length.
                                                 @else   28-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_32,                    /*!< @if Eng 32-bit address length.
                                                 @else   32-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_36,                    /*!< @if Eng 36-bit address length.
                                                 @else   36-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_40,                    /*!< @if Eng 40-bit address length.
                                                 @else   40-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_44,                    /*!< @if Eng 44-bit address length.
                                                 @else   44-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_48,                    /*!< @if Eng 48-bit address length.
                                                 @else   48-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_52,                    /*!< @if Eng 52-bit address length.
                                                 @else   52-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_56,                    /*!< @if Eng 56-bit address length.
                                                 @else   56-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_60,                    /*!< @if Eng 60-bit address length.
                                                 @else   60-位地址长度。 @endif */
    HAL_SPI_ADDR_LEN_MAX = HAL_SPI_ADDR_LEN_60
} hal_spi_addr_len_t;

/**
 * @if Eng
 * @brief  Definition of the event ID of hal spi.
 * @else
 * @brief  HAL层SPI事件ID的定义
 * @endif
 */
typedef enum hal_spi_evt_id {
    SPI_EVT_RX_FULL_ISR,           /*!< @if Eng Rx full isr triggered.
                                        @else   接收满中断触发 @endif */
    SPI_EVT_RX_OVERFLOW_ISR,       /*!< @if Eng Rx overflow isr triggered.
                                        @else   接收溢出中断触发 @endif */
    SPI_EVT_RX_UNDERFLOW_ISR,      /*!< @if Eng Rx underflow isr triggered.
                                        @else   接收空读中断触发 @endif */
    SPI_EVT_TX_EMPTY_ISR,          /*!< @if Eng Tx empty isr triggered.
                                        @else   TX空中断被触发 @endif */
    SPI_EVT_TX_OVERFLOW_ISR,       /*!< @if Eng Tx overflow isr triggered.
                                        @else   TX溢出中断被触发 @endif */
    SPI_EVT_MULTI_MASTER_ISR       /*!< @if Eng Multi-master contention isr triggered.
                                        @else   双主机竞争中断被触发 @endif */
} hal_spi_evt_id_t;

/**
 * @if Eng
 * @brief  QSPI parameters of SPI transfer.
 * @else
 * @brief  SPI传输中QSPI的参数。
 * @endif
 */
typedef struct hal_spi_xfer_qspi_param {
    hal_spi_trans_type_t trans_type;  /*!< @if Eng SPI frame format for instruction and address.
                                           @else   传输类型，用于指定指令和地址的长度。 @endif */

    hal_spi_inst_len_t   inst_len;    /*!< @if Eng Instruction length, support 0, 4, 8, 16bits.
                                           @else   指令长度，支持0、4、8、16位。 @endif */

    hal_spi_addr_len_t   addr_len;    /*!< @if Eng Address length, support 0, 8, 16, 24, 32bits.
                                           @else   地址长度，支持0、8、16、24、32位。 @endif */

    uint32_t             wait_cycles; /*!< @if Eng Indicates the wait cycles.
                                           @else   等待的周期数。 @endif */
} hal_spi_xfer_qspi_param_t;

/**
 * @if Eng
 * @brief  Single SPI parameters of SPI transfer.
 * @else
 * @brief  SPI传输中Single SPI的参数。
 * @endif
 */
typedef struct hal_spi_xfer_sspi_param {
    uint32_t             wait_cycles; /*!< @if Eng Indicates the wait cycles.
                                           @else   等待的周期数。 @endif */
} hal_spi_xfer_sspi_param_t;

/**
 * @if Eng
 * @brief  Definition of SPI basic attributes.
 * @else
 * @brief  SPI基础配置参数定义。
 * @endif
 */
typedef struct hal_spi_attr {
    bool is_slave;                      /*!< @if Eng Indicates if SPI work in slave mode or not.
                                             @else   SPI工作在Master/Slave模式。 @endif */

    uint32_t slave_num;                 /*!< @if Eng Index when selecting a slave.
                                                     - 0: Not select.
                                                     - 1: slave index 0.
                                                     - 2: slave index 1.
                                                     - ...
                                             @else   选择从机时的索引
                                                     - 0：不选择。
                                                     - 1：从机索引0。
                                                     - 2：从机索引1。
                                                     - ...
                                             @endif */

    uint32_t bus_clk;                   /*!< @if Eng Provide ssi_clk for clock freq division calculation.
                                             @else   用于计算SPI的时钟分频系数。 @endif */

    uint32_t freq_mhz;                  /*!< @if Eng Indicates the frequency of SPI.
                                             @else   SPI的工作频率。 @endif */

    uint32_t clk_polarity;              /*!< @if Eng Indicates the clock polarity of SPI.
                                                     For details, see @ref hal_spi_cfg_clk_cpol_t
                                             @else   SPI的时钟极性。参考 @ref hal_spi_cfg_clk_cpol_t @endif */

    uint32_t clk_phase;                 /*!< @if Eng Indicates the clock phase of SPI.
                                                     For details, see @ref hal_spi_cfg_clk_cpha_t
                                             @else   SPI的时钟相位。参考 @ref hal_spi_cfg_clk_cpha_t @endif */

    uint32_t frame_format;              /*!< @if Eng Indicates the which serial protocol transfers the data.
                                                     For details, see @ref hal_spi_cfg_frame_format_t
                                             @else   选择串行传输的协议。参考 @ref hal_spi_cfg_frame_format_t @endif */

    uint32_t spi_frame_format;          /*!< @if Eng Indicates the frame format of SPI.
                                                     For details, see @ref hal_spi_frame_format_t
                                             @else   SPI的帧格式。参考 @ref hal_spi_frame_format_t @endif */

    uint32_t frame_size;                /*!< @if Eng Indicates the frame size of SPI.
                                                     For details, see @ref hal_spi_frame_size_t
                                             @else   SPI的帧长度。参考 @ref hal_spi_frame_size_t @endif */

    uint32_t tmod;                      /*!< @if Eng Indicates the transfer mode.
                                                     For details, see @ref hal_spi_trans_mode_t
                                             @else   SPI的传输模式。参考 @ref hal_spi_trans_mode_t @endif */

    uint32_t ndf;                       /*!< @if Eng Indicates the number of data frames.
                                             @else   SPI的数据帧数。 @endif */

    uint32_t sste;                      /*!< @if Eng Indicates if SPI slave select toggle enable or not.
                                                     When disable, master should reed all data in slave tx_queue
                                                     at ONE time when reading data from slave device. Otherwise,
                                                     data loss occurs.
                                                     For details, see @ref hal_spi_cfg_sste_t
                                             @else   SPI从机选择切换使能/不使能。
                                                     当此配置不使能，主机从从机读取数据时，需要一次性将从机发送
                                                     队列中的数据读完，否则会出现丢失数据问题。
                                                     参考 @ref hal_spi_cfg_sste_t @endif */
} hal_spi_attr_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| is_slave | bool | SPI 工作模式（true 为从机模式，false 为主机模式） |
| slave_num | uint32_t | 选择从机时的索引（0 表示不选择，1 表示从机索引 0，依此类推） |
| bus_clk | uint32_t | 用于计算 SPI 时钟分频系数的时钟 |
| freq_mhz | uint32_t | SPI 的工作频率 |
| clk_polarity | uint32_t | SPI 的时钟极性 |
| clk_phase | uint32_t | SPI 的时钟相位 |
| frame_format | uint32_t | 选择的串行传输协议 |
| spi_frame_format | uint32_t | SPI 的帧格式 |
| frame_size | uint32_t | SPI 的帧大小 |
| tmod | uint32_t | SPI 的传输模式 |
| ndf | uint32_t | 接收数据帧的数量 |
| sste | uint32_t | 从机片选翻转是否使能 |

### struct hal_spi_extra_attr_t <a id="hal_spi_extra_attr_t"></a>

```c
typedef enum hal_spi_ctrl_id {
    SPI_CTRL_SET_ATTR,                  /*!< @if Eng Set SPI basic attribute.
                                             @else   设置基础参数。 @endif */

    SPI_CTRL_GET_ATTR,                  /*!< @if Eng Get SPI basic attribute.
                                             @else   获取基础参数。 @endif */

    SPI_CTRL_SET_EXTRA_ATTR,            /*!< @if Eng Set SPI extral attribute.
                                             @else   设置高级参数。 @endif */

    SPI_CTRL_GET_EXTRA_ATTR,            /*!< @if Eng Get SPI extral attribute.
                                             @else   获取高级参数。 @endif */

    SPI_CTRL_SELECT_SLAVE,              /*!< @if Eng Select the slave.
                                             @else   选择指定的设备。 @endif */

    SPI_CTRL_CHECK_FIFO_BUSY,           /*!< @if Eng Check whether the SPI is busy.
                                             @else   检查SPI是否忙碌状态。 @endif */
#if defined(CONFIG_SPI_SUPPORT_DMA) && (CONFIG_SPI_SUPPORT_DMA == 1)
    SPI_CTRL_SET_DMA_CFG,               /*!< @if Eng Set the DMA transfer enable/disable and datalevel.
                                             @else   设置DMA的传输使能和数据level。 @endif */

    SPI_CTRL_GET_DMA_DATA_ADDR,         /*!< @if Eng Get the DMA transfer data address.
                                             @else   获取DMA的传输数据地址。 @endif */
#endif  /* CONFIG_SPI_SUPPORT_DMA */

#if defined(CONFIG_SPI_SUPPORT_INTERRUPT) && (CONFIG_SPI_SUPPORT_INTERRUPT == 1)
    SPI_CTRL_EN_RXFI_INT,               /*!< @if Eng Enable the Receive FIFO full interrupt.
                                             @else   使能RX FIFO是否已满中断。 @endif */

    SPI_CTRL_CHECK_RX_FIFO_EMPTY,       /*!< @if Eng Check if rx fifo is empty or not.
                                             @else   判断RX FIFO是否为空。 @endif */

    SPI_CTRL_EN_TXEI_INT,               /*!< @if Eng Enable the transmit FIFO empty interrupt.
                                             @else   使能TX FIFO是否为空中断。 @endif */

    SPI_CTRL_CHECK_TX_FIFO_FULL,        /*!< @if Eng Check if tx fifo is full or not.
                                             @else   判断RX FIFO是否已满。 @endif */

    SPI_CTRL_EN_MULTI_MASTER_ERR_INT,   /*!< @if Eng Enable the Multi-Master contention interrupt.
                                             @else   使能双主机竞争中断。 @endif */
#endif  /* CONFIG_SPI_SUPPORT_INTERRUPT */

#if defined(CONFIG_SPI_SUPPORT_LPM) && (CONFIG_SPI_SUPPORT_LPM == 1)
    SPI_CTRL_SUSPEND,                   /*!< @if Eng Suspend all of the spi channels.
                                             @else   挂起所有spi通道。 @endif */
    SPI_CTRL_RESUME,                    /*!< @if Eng Resume all of the spi channels.
                                             @else   挂起所有spi通道。 @endif */
#endif  /* CONFIG_SPI_SUPPORT_LPM */
    SPI_CTRL_SET_TMOD,                  /*!< @if Eng Set SPI transfer mode.
                                             @else   设置SPI传输模式。 @endif */
    SPI_CTRL_MAX,
    SPI_CTRL_ID_INVALID = 0xFF
} hal_spi_ctrl_id_t;

/**
 * @if Eng
 * @brief  Frame Format.
 * @else
 * @brief  帧格式。
 * @endif
 */
typedef enum hal_spi_cfg_frame_format {
    SPI_CFG_FRAME_FORMAT_MOTOROLA_SPI,      /*!< @if Eng Motorolla SPI Frame Format.
                                                 @else   摩托罗拉SPI帧格式。 @endif */

    SPI_CFG_FRAME_FORMAT_TEXAS_SSP,         /*!< @if Eng Texas Instruments SSP Frame Format.
                                                 @else   德州仪器SSP帧格式。 @endif */

    SPI_CFG_FRAME_FORMAT_NS_MICROWIRE,      /*!< @if Eng National Microwire Frame Format.
                                                 @else   国家微线帧格式。 @endif */
    SPI_CFG_FRAME_FORMAT_MAX
} hal_spi_cfg_frame_format_t;

/**
 * @if Eng
 * @brief  Clock polarity.
 * @else
 * @brief  时钟极性。
 * @endif
 */
typedef enum hal_spi_cfg_clk_cpol {
    SPI_CFG_CLK_CPOL_0,                     /*!< @if Eng Inactive state of serial clock is low.
                                                 @else   SPI的非激活状态为低电平。 @endif */

    SPI_CFG_CLK_CPOL_1,                     /*!< @if Eng Inactive state of serial clock is high.
                                                 @else   SPI的非激活状态为高电平。 @endif */
    SPI_CFG_CLK_CPOL_MAX
} hal_spi_cfg_clk_cpol_t;

/**
 * @if Eng
 * @brief  Clock phase.
 * @else
 * @brief  时钟相位。
 * @endif
 */
typedef enum hal_spi_cfg_clk_cpha {
    SPI_CFG_CLK_CPHA_0,                     /*!< @if Eng Serial clock toggles in middle of first data bit.
                                                 @else   SPI时钟在第一个数据位中间切换。 @endif */

    SPI_CFG_CLK_CPHA_1,                     /*!< @if Eng Serial clock toggles at start of first data bit.
                                                 @else   SPI时钟在第一个数据位开始时切换。 @endif */
    SPI_CFG_CLK_CPHA_MAX
} hal_spi_cfg_clk_cpha_t;

/**
 * @if Eng
 * @brief  SPI slave select toggle enable.
 * @else
 * @brief  SPI 从机选择切换使能
 * @endif
 */
typedef enum hal_spi_cfg_sste {
    SPI_CFG_SSTE_DISABLE,                   /*!< @if Eng SPI slave select toggle disable.
                                                         When disable, master should reed all data in slave tx_queue
                                                         at ONE time when reading data from slave device. Otherwise,
                                                         data loss occurs.
                                                 @else   SPI 从机选择切换不使能。
                                                         当此配置不使能，主机从从机读取数据时，需要一次性将从机发送
                                                         队列中的数据读完，否则会出现丢失数据问题。@endif */
    SPI_CFG_SSTE_ENABLE,                    /*!< @if Eng SPI slave select toggle enable.
                                                 @else   SPI 从机选择切换使能 @endif */
    SPI_CFG_SSTE_MAX
} hal_spi_cfg_sste_t;

/**
 * @if Eng
 * @brief  Transfer Mode.
 * @else
 * @brief  传输模式。
 * @endif
 */
typedef enum hal_spi_trans_mode {
    HAL_SPI_TRANS_MODE_TXRX = 0,            /*!< @if Eng Transmit and receive mode.
                                                 @else   收发模式。 @endif */

    HAL_SPI_TRANS_MODE_TX,                  /*!< @if Eng Transmit only / Transmit mode.
                                                 @else   发送模式。 @endif */

    HAL_SPI_TRANS_MODE_RX,                  /*!< @if Eng Receive only / Receive mode.
                                                 @else   接收模式。 @endif */

    HAL_SPI_TRANS_MODE_EEPROM,              /*!< @if Eng EEPROM read mode.
                                                 @else   EEPROM模式。 @endif */
    HAL_SPI_TRANS_MODE_MAX
} hal_spi_trans_mode_t;

/**
 * @if Eng
 * @brief  Data Frame Size.
 * @else
 * @brief  数据帧长度。
 * @endif
 */
typedef enum hal_spi_frame_size {
    HAL_SPI_FRAME_SIZE_8    = 0x07,         /*!< @if Eng 8-bit serial data transfer.
                                                 @else   8-位串行数据传输。 @endif */

    HAL_SPI_FRAME_SIZE_16   = 0x0F,         /*!< @if Eng 16-bit serial data transfer(Not supported now).
                                                 @else   16-位串行数据传输（暂不支持）。 @endif */

    HAL_SPI_FRAME_SIZE_24   = 0x17,         /*!< @if Eng 24-bit serial data transfer(Not supported now).
                                                 @else   24-位串行数据传输（暂不支持）。 @endif */

    HAL_SPI_FRAME_SIZE_32   = 0x1F          /*!< @if Eng 32-bit serial data transfer.
                                                 @else   32-位串行数据传输。 @endif */
} hal_spi_frame_size_t;

/**
 * @if Eng
 * @brief  SPI Frame Format.
 * @else
 * @brief  SPI数据帧格式。
 * @endif
 */
typedef enum hal_spi_frame_format {
    HAL_SPI_FRAME_FORMAT_STANDARD = 0,      /*!< @if Eng SPI Standard frame format.
                                                 @else   标准的单线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_DUAL,              /*!< @if Eng SPI Dual frame format.
                                                 @else   双线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_QUAD,              /*!< @if Eng SPI Quad frame format.
                                                 @else   4线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_OCTAL,             /*!< @if Eng SPI Octal frame format.
                                                 @else   8线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_DOUBLE_OCTAL,      /*!< @if Eng SPI Double Octal frame format.
                                                 @else   16线SPI帧格式。 @endif */
    HAL_SPI_FRAME_FORMAT_SIXT,
    HAL_SPI_FRAME_FORMAT_MAX_NUM,
    HAL_SPI_FRAME_FORMAT_NONE = HAL_SPI_FRAME_FORMAT_MAX_NUM
} hal_spi_frame_format_t;

/**
 * @if Eng
 * @brief  SPI Transfer Types.
 * @else
 * @brief  SPI传输类型。
 * @endif
 */
typedef enum hal_spi_trans_type {
    HAL_SPI_TRANS_TYPE_INST_S_ADDR_S = 0,   /*!< @if Eng Instruction and Address will be sent in standard SPI mode.
                                                 @else   指令和地址使用单线SPI传输。 @endif */

    HAL_SPI_TRANS_TYPE_INST_S_ADDR_Q,       /*!< @if Eng Instruction will be sent in standard mode and address will
                                                         be sent in mode specified by frame format register.
                                                 @else   指令使用单线SPI传输，
                                                         地址按照帧格式寄存器的配置传输。 @endif */

    HAL_SPI_TRANS_TYPE_INST_Q_ADDR_Q,       /*!< @if Eng Both instruction and address will be sent in
                                                         the mode specified by frame format register.
                                                 @else   指令和地址都按照帧格式寄存器的配置传输。 @endif */
    HAL_SPI_TRANS_TYPE_MAX = HAL_SPI_TRANS_TYPE_INST_Q_ADDR_Q
} hal_spi_trans_type_t;

/**
 * @if Eng
 * @brief  SPI length of instruction.
 * @else
 * @brief  SPI指令长度定义。
 * @endif
 */
typedef enum hal_spi_inst_len {
    HAL_SPI_INST_LEN_0 = 0,                 /*!< @if Eng 0-bit (no instruction).
                                                 @else   不携带指令。 @endif */

    HAL_SPI_INST_LEN_4,                     /*!< @if Eng 4-bit instruction.
                                                 @else   4-位指令。 @endif */

    HAL_SPI_INST_LEN_8,                     /*!< @if Eng 8-bit instruction.
                                                 @else   8-位指令。 @endif */

    HAL_SPI_INST_LEN_16,                    /*!< @if Eng 16-bit instruction.
                                                 @else   16-位指令。 @endif */
    HAL_SPI_INST_LEN_MAX = HAL_SPI_INST_LEN_16
} hal_spi_inst_len_t;

/**
 * @if Eng
 * @brief  SPI length of address.
 * @else
 * @brief  SPI地址长度定义。
 * @endif
 */
typedef enum hal_spi_addr_len {
    HAL_SPI_ADDR_LEN_0 = 0,                 /*!< @if Eng 0-bit address length.
                                                 @else   0-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_4,                     /*!< @if Eng 4-bit address length.
                                                 @else   4-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_8,                     /*!< @if Eng 8-bit address length.
                                                 @else   8-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_12,                    /*!< @if Eng 12-bit address length.
                                                 @else   12-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_16,                    /*!< @if Eng 16-bit address length.
                                                 @else   16-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_20,                    /*!< @if Eng 20-bit address length.
                                                 @else   20-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_24,                    /*!< @if Eng 24-bit address length.
                                                 @else   24-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_28,                    /*!< @if Eng 28-bit address length.
                                                 @else   28-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_32,                    /*!< @if Eng 32-bit address length.
                                                 @else   32-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_36,                    /*!< @if Eng 36-bit address length.
                                                 @else   36-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_40,                    /*!< @if Eng 40-bit address length.
                                                 @else   40-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_44,                    /*!< @if Eng 44-bit address length.
                                                 @else   44-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_48,                    /*!< @if Eng 48-bit address length.
                                                 @else   48-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_52,                    /*!< @if Eng 52-bit address length.
                                                 @else   52-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_56,                    /*!< @if Eng 56-bit address length.
                                                 @else   56-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_60,                    /*!< @if Eng 60-bit address length.
                                                 @else   60-位地址长度。 @endif */
    HAL_SPI_ADDR_LEN_MAX = HAL_SPI_ADDR_LEN_60
} hal_spi_addr_len_t;

/**
 * @if Eng
 * @brief  Definition of the event ID of hal spi.
 * @else
 * @brief  HAL层SPI事件ID的定义
 * @endif
 */
typedef enum hal_spi_evt_id {
    SPI_EVT_RX_FULL_ISR,           /*!< @if Eng Rx full isr triggered.
                                        @else   接收满中断触发 @endif */
    SPI_EVT_RX_OVERFLOW_ISR,       /*!< @if Eng Rx overflow isr triggered.
                                        @else   接收溢出中断触发 @endif */
    SPI_EVT_RX_UNDERFLOW_ISR,      /*!< @if Eng Rx underflow isr triggered.
                                        @else   接收空读中断触发 @endif */
    SPI_EVT_TX_EMPTY_ISR,          /*!< @if Eng Tx empty isr triggered.
                                        @else   TX空中断被触发 @endif */
    SPI_EVT_TX_OVERFLOW_ISR,       /*!< @if Eng Tx overflow isr triggered.
                                        @else   TX溢出中断被触发 @endif */
    SPI_EVT_MULTI_MASTER_ISR       /*!< @if Eng Multi-master contention isr triggered.
                                        @else   双主机竞争中断被触发 @endif */
} hal_spi_evt_id_t;

/**
 * @if Eng
 * @brief  QSPI parameters of SPI transfer.
 * @else
 * @brief  SPI传输中QSPI的参数。
 * @endif
 */
typedef struct hal_spi_xfer_qspi_param {
    hal_spi_trans_type_t trans_type;  /*!< @if Eng SPI frame format for instruction and address.
                                           @else   传输类型，用于指定指令和地址的长度。 @endif */

    hal_spi_inst_len_t   inst_len;    /*!< @if Eng Instruction length, support 0, 4, 8, 16bits.
                                           @else   指令长度，支持0、4、8、16位。 @endif */

    hal_spi_addr_len_t   addr_len;    /*!< @if Eng Address length, support 0, 8, 16, 24, 32bits.
                                           @else   地址长度，支持0、8、16、24、32位。 @endif */

    uint32_t             wait_cycles; /*!< @if Eng Indicates the wait cycles.
                                           @else   等待的周期数。 @endif */
} hal_spi_xfer_qspi_param_t;

/**
 * @if Eng
 * @brief  Single SPI parameters of SPI transfer.
 * @else
 * @brief  SPI传输中Single SPI的参数。
 * @endif
 */
typedef struct hal_spi_xfer_sspi_param {
    uint32_t             wait_cycles; /*!< @if Eng Indicates the wait cycles.
                                           @else   等待的周期数。 @endif */
} hal_spi_xfer_sspi_param_t;

/**
 * @if Eng
 * @brief  Definition of SPI basic attributes.
 * @else
 * @brief  SPI基础配置参数定义。
 * @endif
 */
typedef struct hal_spi_attr {
    bool is_slave;                      /*!< @if Eng Indicates if SPI work in slave mode or not.
                                             @else   SPI工作在Master/Slave模式。 @endif */

    uint32_t slave_num;                 /*!< @if Eng Index when selecting a slave.
                                                     - 0: Not select.
                                                     - 1: slave index 0.
                                                     - 2: slave index 1.
                                                     - ...
                                             @else   选择从机时的索引
                                                     - 0：不选择。
                                                     - 1：从机索引0。
                                                     - 2：从机索引1。
                                                     - ...
                                             @endif */

    uint32_t bus_clk;                   /*!< @if Eng Provide ssi_clk for clock freq division calculation.
                                             @else   用于计算SPI的时钟分频系数。 @endif */

    uint32_t freq_mhz;                  /*!< @if Eng Indicates the frequency of SPI.
                                             @else   SPI的工作频率。 @endif */

    uint32_t clk_polarity;              /*!< @if Eng Indicates the clock polarity of SPI.
                                                     For details, see @ref hal_spi_cfg_clk_cpol_t
                                             @else   SPI的时钟极性。参考 @ref hal_spi_cfg_clk_cpol_t @endif */

    uint32_t clk_phase;                 /*!< @if Eng Indicates the clock phase of SPI.
                                                     For details, see @ref hal_spi_cfg_clk_cpha_t
                                             @else   SPI的时钟相位。参考 @ref hal_spi_cfg_clk_cpha_t @endif */

    uint32_t frame_format;              /*!< @if Eng Indicates the which serial protocol transfers the data.
                                                     For details, see @ref hal_spi_cfg_frame_format_t
                                             @else   选择串行传输的协议。参考 @ref hal_spi_cfg_frame_format_t @endif */

    uint32_t spi_frame_format;          /*!< @if Eng Indicates the frame format of SPI.
                                                     For details, see @ref hal_spi_frame_format_t
                                             @else   SPI的帧格式。参考 @ref hal_spi_frame_format_t @endif */

    uint32_t frame_size;                /*!< @if Eng Indicates the frame size of SPI.
                                                     For details, see @ref hal_spi_frame_size_t
                                             @else   SPI的帧长度。参考 @ref hal_spi_frame_size_t @endif */

    uint32_t tmod;                      /*!< @if Eng Indicates the transfer mode.
                                                     For details, see @ref hal_spi_trans_mode_t
                                             @else   SPI的传输模式。参考 @ref hal_spi_trans_mode_t @endif */

    uint32_t ndf;                       /*!< @if Eng Indicates the number of data frames.
                                             @else   SPI的数据帧数。 @endif */

    uint32_t sste;                      /*!< @if Eng Indicates if SPI slave select toggle enable or not.
                                                     When disable, master should reed all data in slave tx_queue
                                                     at ONE time when reading data from slave device. Otherwise,
                                                     data loss occurs.
                                                     For details, see @ref hal_spi_cfg_sste_t
                                             @else   SPI从机选择切换使能/不使能。
                                                     当此配置不使能，主机从从机读取数据时，需要一次性将从机发送
                                                     队列中的数据读完，否则会出现丢失数据问题。
                                                     参考 @ref hal_spi_cfg_sste_t @endif */
} hal_spi_attr_t;

/**
 * @if Eng
 * @brief  Definition of SPI extra attributes.
 * @else
 * @brief  SPI扩展配置参数定义。
 * @endif
 */
typedef struct hal_spi_extra_attr {
    bool tx_use_dma;                        /*!< @if Eng Indicates if SPI use dma or not in TX.
                                                 @else   SPI是否使用DMA发送数据。 @endif */

    bool rx_use_dma;                        /*!< @if Eng Indicates if SPI use dma or not in RX.
                                                 @else   SPI是否使用DMA接收数据。 @endif */

    hal_spi_xfer_qspi_param_t qspi_param;   /*!< @if Eng Indicates the qspi parameters.
                                                 @else   QSPI参数。 @endif */

    hal_spi_xfer_sspi_param_t sspi_param;   /*!< @if Eng Indicates the single spi parameters.
                                                 @else   Single SPI参数。 @endif */
} hal_spi_extra_attr_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| tx_use_dma | bool | SPI 发送数据是否使用 DMA |
| rx_use_dma | bool | SPI 接收数据是否使用 DMA |
| qspi_param | hal_spi_xfer_qspi_param_t | QSPI 参数 |
| sspi_param | hal_spi_xfer_sspi_param_t | Single SPI 参数 |

### struct hal_spi_xfer_data_t <a id="hal_spi_xfer_data_t"></a>

```c
typedef enum hal_spi_ctrl_id {
    SPI_CTRL_SET_ATTR,                  /*!< @if Eng Set SPI basic attribute.
                                             @else   设置基础参数。 @endif */

    SPI_CTRL_GET_ATTR,                  /*!< @if Eng Get SPI basic attribute.
                                             @else   获取基础参数。 @endif */

    SPI_CTRL_SET_EXTRA_ATTR,            /*!< @if Eng Set SPI extral attribute.
                                             @else   设置高级参数。 @endif */

    SPI_CTRL_GET_EXTRA_ATTR,            /*!< @if Eng Get SPI extral attribute.
                                             @else   获取高级参数。 @endif */

    SPI_CTRL_SELECT_SLAVE,              /*!< @if Eng Select the slave.
                                             @else   选择指定的设备。 @endif */

    SPI_CTRL_CHECK_FIFO_BUSY,           /*!< @if Eng Check whether the SPI is busy.
                                             @else   检查SPI是否忙碌状态。 @endif */
#if defined(CONFIG_SPI_SUPPORT_DMA) && (CONFIG_SPI_SUPPORT_DMA == 1)
    SPI_CTRL_SET_DMA_CFG,               /*!< @if Eng Set the DMA transfer enable/disable and datalevel.
                                             @else   设置DMA的传输使能和数据level。 @endif */

    SPI_CTRL_GET_DMA_DATA_ADDR,         /*!< @if Eng Get the DMA transfer data address.
                                             @else   获取DMA的传输数据地址。 @endif */
#endif  /* CONFIG_SPI_SUPPORT_DMA */

#if defined(CONFIG_SPI_SUPPORT_INTERRUPT) && (CONFIG_SPI_SUPPORT_INTERRUPT == 1)
    SPI_CTRL_EN_RXFI_INT,               /*!< @if Eng Enable the Receive FIFO full interrupt.
                                             @else   使能RX FIFO是否已满中断。 @endif */

    SPI_CTRL_CHECK_RX_FIFO_EMPTY,       /*!< @if Eng Check if rx fifo is empty or not.
                                             @else   判断RX FIFO是否为空。 @endif */

    SPI_CTRL_EN_TXEI_INT,               /*!< @if Eng Enable the transmit FIFO empty interrupt.
                                             @else   使能TX FIFO是否为空中断。 @endif */

    SPI_CTRL_CHECK_TX_FIFO_FULL,        /*!< @if Eng Check if tx fifo is full or not.
                                             @else   判断RX FIFO是否已满。 @endif */

    SPI_CTRL_EN_MULTI_MASTER_ERR_INT,   /*!< @if Eng Enable the Multi-Master contention interrupt.
                                             @else   使能双主机竞争中断。 @endif */
#endif  /* CONFIG_SPI_SUPPORT_INTERRUPT */

#if defined(CONFIG_SPI_SUPPORT_LPM) && (CONFIG_SPI_SUPPORT_LPM == 1)
    SPI_CTRL_SUSPEND,                   /*!< @if Eng Suspend all of the spi channels.
                                             @else   挂起所有spi通道。 @endif */
    SPI_CTRL_RESUME,                    /*!< @if Eng Resume all of the spi channels.
                                             @else   挂起所有spi通道。 @endif */
#endif  /* CONFIG_SPI_SUPPORT_LPM */
    SPI_CTRL_SET_TMOD,                  /*!< @if Eng Set SPI transfer mode.
                                             @else   设置SPI传输模式。 @endif */
    SPI_CTRL_MAX,
    SPI_CTRL_ID_INVALID = 0xFF
} hal_spi_ctrl_id_t;

/**
 * @if Eng
 * @brief  Frame Format.
 * @else
 * @brief  帧格式。
 * @endif
 */
typedef enum hal_spi_cfg_frame_format {
    SPI_CFG_FRAME_FORMAT_MOTOROLA_SPI,      /*!< @if Eng Motorolla SPI Frame Format.
                                                 @else   摩托罗拉SPI帧格式。 @endif */

    SPI_CFG_FRAME_FORMAT_TEXAS_SSP,         /*!< @if Eng Texas Instruments SSP Frame Format.
                                                 @else   德州仪器SSP帧格式。 @endif */

    SPI_CFG_FRAME_FORMAT_NS_MICROWIRE,      /*!< @if Eng National Microwire Frame Format.
                                                 @else   国家微线帧格式。 @endif */
    SPI_CFG_FRAME_FORMAT_MAX
} hal_spi_cfg_frame_format_t;

/**
 * @if Eng
 * @brief  Clock polarity.
 * @else
 * @brief  时钟极性。
 * @endif
 */
typedef enum hal_spi_cfg_clk_cpol {
    SPI_CFG_CLK_CPOL_0,                     /*!< @if Eng Inactive state of serial clock is low.
                                                 @else   SPI的非激活状态为低电平。 @endif */

    SPI_CFG_CLK_CPOL_1,                     /*!< @if Eng Inactive state of serial clock is high.
                                                 @else   SPI的非激活状态为高电平。 @endif */
    SPI_CFG_CLK_CPOL_MAX
} hal_spi_cfg_clk_cpol_t;

/**
 * @if Eng
 * @brief  Clock phase.
 * @else
 * @brief  时钟相位。
 * @endif
 */
typedef enum hal_spi_cfg_clk_cpha {
    SPI_CFG_CLK_CPHA_0,                     /*!< @if Eng Serial clock toggles in middle of first data bit.
                                                 @else   SPI时钟在第一个数据位中间切换。 @endif */

    SPI_CFG_CLK_CPHA_1,                     /*!< @if Eng Serial clock toggles at start of first data bit.
                                                 @else   SPI时钟在第一个数据位开始时切换。 @endif */
    SPI_CFG_CLK_CPHA_MAX
} hal_spi_cfg_clk_cpha_t;

/**
 * @if Eng
 * @brief  SPI slave select toggle enable.
 * @else
 * @brief  SPI 从机选择切换使能
 * @endif
 */
typedef enum hal_spi_cfg_sste {
    SPI_CFG_SSTE_DISABLE,                   /*!< @if Eng SPI slave select toggle disable.
                                                         When disable, master should reed all data in slave tx_queue
                                                         at ONE time when reading data from slave device. Otherwise,
                                                         data loss occurs.
                                                 @else   SPI 从机选择切换不使能。
                                                         当此配置不使能，主机从从机读取数据时，需要一次性将从机发送
                                                         队列中的数据读完，否则会出现丢失数据问题。@endif */
    SPI_CFG_SSTE_ENABLE,                    /*!< @if Eng SPI slave select toggle enable.
                                                 @else   SPI 从机选择切换使能 @endif */
    SPI_CFG_SSTE_MAX
} hal_spi_cfg_sste_t;

/**
 * @if Eng
 * @brief  Transfer Mode.
 * @else
 * @brief  传输模式。
 * @endif
 */
typedef enum hal_spi_trans_mode {
    HAL_SPI_TRANS_MODE_TXRX = 0,            /*!< @if Eng Transmit and receive mode.
                                                 @else   收发模式。 @endif */

    HAL_SPI_TRANS_MODE_TX,                  /*!< @if Eng Transmit only / Transmit mode.
                                                 @else   发送模式。 @endif */

    HAL_SPI_TRANS_MODE_RX,                  /*!< @if Eng Receive only / Receive mode.
                                                 @else   接收模式。 @endif */

    HAL_SPI_TRANS_MODE_EEPROM,              /*!< @if Eng EEPROM read mode.
                                                 @else   EEPROM模式。 @endif */
    HAL_SPI_TRANS_MODE_MAX
} hal_spi_trans_mode_t;

/**
 * @if Eng
 * @brief  Data Frame Size.
 * @else
 * @brief  数据帧长度。
 * @endif
 */
typedef enum hal_spi_frame_size {
    HAL_SPI_FRAME_SIZE_8    = 0x07,         /*!< @if Eng 8-bit serial data transfer.
                                                 @else   8-位串行数据传输。 @endif */

    HAL_SPI_FRAME_SIZE_16   = 0x0F,         /*!< @if Eng 16-bit serial data transfer(Not supported now).
                                                 @else   16-位串行数据传输（暂不支持）。 @endif */

    HAL_SPI_FRAME_SIZE_24   = 0x17,         /*!< @if Eng 24-bit serial data transfer(Not supported now).
                                                 @else   24-位串行数据传输（暂不支持）。 @endif */

    HAL_SPI_FRAME_SIZE_32   = 0x1F          /*!< @if Eng 32-bit serial data transfer.
                                                 @else   32-位串行数据传输。 @endif */
} hal_spi_frame_size_t;

/**
 * @if Eng
 * @brief  SPI Frame Format.
 * @else
 * @brief  SPI数据帧格式。
 * @endif
 */
typedef enum hal_spi_frame_format {
    HAL_SPI_FRAME_FORMAT_STANDARD = 0,      /*!< @if Eng SPI Standard frame format.
                                                 @else   标准的单线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_DUAL,              /*!< @if Eng SPI Dual frame format.
                                                 @else   双线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_QUAD,              /*!< @if Eng SPI Quad frame format.
                                                 @else   4线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_OCTAL,             /*!< @if Eng SPI Octal frame format.
                                                 @else   8线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_DOUBLE_OCTAL,      /*!< @if Eng SPI Double Octal frame format.
                                                 @else   16线SPI帧格式。 @endif */
    HAL_SPI_FRAME_FORMAT_SIXT,
    HAL_SPI_FRAME_FORMAT_MAX_NUM,
    HAL_SPI_FRAME_FORMAT_NONE = HAL_SPI_FRAME_FORMAT_MAX_NUM
} hal_spi_frame_format_t;

/**
 * @if Eng
 * @brief  SPI Transfer Types.
 * @else
 * @brief  SPI传输类型。
 * @endif
 */
typedef enum hal_spi_trans_type {
    HAL_SPI_TRANS_TYPE_INST_S_ADDR_S = 0,   /*!< @if Eng Instruction and Address will be sent in standard SPI mode.
                                                 @else   指令和地址使用单线SPI传输。 @endif */

    HAL_SPI_TRANS_TYPE_INST_S_ADDR_Q,       /*!< @if Eng Instruction will be sent in standard mode and address will
                                                         be sent in mode specified by frame format register.
                                                 @else   指令使用单线SPI传输，
                                                         地址按照帧格式寄存器的配置传输。 @endif */

    HAL_SPI_TRANS_TYPE_INST_Q_ADDR_Q,       /*!< @if Eng Both instruction and address will be sent in
                                                         the mode specified by frame format register.
                                                 @else   指令和地址都按照帧格式寄存器的配置传输。 @endif */
    HAL_SPI_TRANS_TYPE_MAX = HAL_SPI_TRANS_TYPE_INST_Q_ADDR_Q
} hal_spi_trans_type_t;

/**
 * @if Eng
 * @brief  SPI length of instruction.
 * @else
 * @brief  SPI指令长度定义。
 * @endif
 */
typedef enum hal_spi_inst_len {
    HAL_SPI_INST_LEN_0 = 0,                 /*!< @if Eng 0-bit (no instruction).
                                                 @else   不携带指令。 @endif */

    HAL_SPI_INST_LEN_4,                     /*!< @if Eng 4-bit instruction.
                                                 @else   4-位指令。 @endif */

    HAL_SPI_INST_LEN_8,                     /*!< @if Eng 8-bit instruction.
                                                 @else   8-位指令。 @endif */

    HAL_SPI_INST_LEN_16,                    /*!< @if Eng 16-bit instruction.
                                                 @else   16-位指令。 @endif */
    HAL_SPI_INST_LEN_MAX = HAL_SPI_INST_LEN_16
} hal_spi_inst_len_t;

/**
 * @if Eng
 * @brief  SPI length of address.
 * @else
 * @brief  SPI地址长度定义。
 * @endif
 */
typedef enum hal_spi_addr_len {
    HAL_SPI_ADDR_LEN_0 = 0,                 /*!< @if Eng 0-bit address length.
                                                 @else   0-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_4,                     /*!< @if Eng 4-bit address length.
                                                 @else   4-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_8,                     /*!< @if Eng 8-bit address length.
                                                 @else   8-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_12,                    /*!< @if Eng 12-bit address length.
                                                 @else   12-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_16,                    /*!< @if Eng 16-bit address length.
                                                 @else   16-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_20,                    /*!< @if Eng 20-bit address length.
                                                 @else   20-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_24,                    /*!< @if Eng 24-bit address length.
                                                 @else   24-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_28,                    /*!< @if Eng 28-bit address length.
                                                 @else   28-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_32,                    /*!< @if Eng 32-bit address length.
                                                 @else   32-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_36,                    /*!< @if Eng 36-bit address length.
                                                 @else   36-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_40,                    /*!< @if Eng 40-bit address length.
                                                 @else   40-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_44,                    /*!< @if Eng 44-bit address length.
                                                 @else   44-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_48,                    /*!< @if Eng 48-bit address length.
                                                 @else   48-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_52,                    /*!< @if Eng 52-bit address length.
                                                 @else   52-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_56,                    /*!< @if Eng 56-bit address length.
                                                 @else   56-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_60,                    /*!< @if Eng 60-bit address length.
                                                 @else   60-位地址长度。 @endif */
    HAL_SPI_ADDR_LEN_MAX = HAL_SPI_ADDR_LEN_60
} hal_spi_addr_len_t;

/**
 * @if Eng
 * @brief  Definition of the event ID of hal spi.
 * @else
 * @brief  HAL层SPI事件ID的定义
 * @endif
 */
typedef enum hal_spi_evt_id {
    SPI_EVT_RX_FULL_ISR,           /*!< @if Eng Rx full isr triggered.
                                        @else   接收满中断触发 @endif */
    SPI_EVT_RX_OVERFLOW_ISR,       /*!< @if Eng Rx overflow isr triggered.
                                        @else   接收溢出中断触发 @endif */
    SPI_EVT_RX_UNDERFLOW_ISR,      /*!< @if Eng Rx underflow isr triggered.
                                        @else   接收空读中断触发 @endif */
    SPI_EVT_TX_EMPTY_ISR,          /*!< @if Eng Tx empty isr triggered.
                                        @else   TX空中断被触发 @endif */
    SPI_EVT_TX_OVERFLOW_ISR,       /*!< @if Eng Tx overflow isr triggered.
                                        @else   TX溢出中断被触发 @endif */
    SPI_EVT_MULTI_MASTER_ISR       /*!< @if Eng Multi-master contention isr triggered.
                                        @else   双主机竞争中断被触发 @endif */
} hal_spi_evt_id_t;

/**
 * @if Eng
 * @brief  QSPI parameters of SPI transfer.
 * @else
 * @brief  SPI传输中QSPI的参数。
 * @endif
 */
typedef struct hal_spi_xfer_qspi_param {
    hal_spi_trans_type_t trans_type;  /*!< @if Eng SPI frame format for instruction and address.
                                           @else   传输类型，用于指定指令和地址的长度。 @endif */

    hal_spi_inst_len_t   inst_len;    /*!< @if Eng Instruction length, support 0, 4, 8, 16bits.
                                           @else   指令长度，支持0、4、8、16位。 @endif */

    hal_spi_addr_len_t   addr_len;    /*!< @if Eng Address length, support 0, 8, 16, 24, 32bits.
                                           @else   地址长度，支持0、8、16、24、32位。 @endif */

    uint32_t             wait_cycles; /*!< @if Eng Indicates the wait cycles.
                                           @else   等待的周期数。 @endif */
} hal_spi_xfer_qspi_param_t;

/**
 * @if Eng
 * @brief  Single SPI parameters of SPI transfer.
 * @else
 * @brief  SPI传输中Single SPI的参数。
 * @endif
 */
typedef struct hal_spi_xfer_sspi_param {
    uint32_t             wait_cycles; /*!< @if Eng Indicates the wait cycles.
                                           @else   等待的周期数。 @endif */
} hal_spi_xfer_sspi_param_t;

/**
 * @if Eng
 * @brief  Definition of SPI basic attributes.
 * @else
 * @brief  SPI基础配置参数定义。
 * @endif
 */
typedef struct hal_spi_attr {
    bool is_slave;                      /*!< @if Eng Indicates if SPI work in slave mode or not.
                                             @else   SPI工作在Master/Slave模式。 @endif */

    uint32_t slave_num;                 /*!< @if Eng Index when selecting a slave.
                                                     - 0: Not select.
                                                     - 1: slave index 0.
                                                     - 2: slave index 1.
                                                     - ...
                                             @else   选择从机时的索引
                                                     - 0：不选择。
                                                     - 1：从机索引0。
                                                     - 2：从机索引1。
                                                     - ...
                                             @endif */

    uint32_t bus_clk;                   /*!< @if Eng Provide ssi_clk for clock freq division calculation.
                                             @else   用于计算SPI的时钟分频系数。 @endif */

    uint32_t freq_mhz;                  /*!< @if Eng Indicates the frequency of SPI.
                                             @else   SPI的工作频率。 @endif */

    uint32_t clk_polarity;              /*!< @if Eng Indicates the clock polarity of SPI.
                                                     For details, see @ref hal_spi_cfg_clk_cpol_t
                                             @else   SPI的时钟极性。参考 @ref hal_spi_cfg_clk_cpol_t @endif */

    uint32_t clk_phase;                 /*!< @if Eng Indicates the clock phase of SPI.
                                                     For details, see @ref hal_spi_cfg_clk_cpha_t
                                             @else   SPI的时钟相位。参考 @ref hal_spi_cfg_clk_cpha_t @endif */

    uint32_t frame_format;              /*!< @if Eng Indicates the which serial protocol transfers the data.
                                                     For details, see @ref hal_spi_cfg_frame_format_t
                                             @else   选择串行传输的协议。参考 @ref hal_spi_cfg_frame_format_t @endif */

    uint32_t spi_frame_format;          /*!< @if Eng Indicates the frame format of SPI.
                                                     For details, see @ref hal_spi_frame_format_t
                                             @else   SPI的帧格式。参考 @ref hal_spi_frame_format_t @endif */

    uint32_t frame_size;                /*!< @if Eng Indicates the frame size of SPI.
                                                     For details, see @ref hal_spi_frame_size_t
                                             @else   SPI的帧长度。参考 @ref hal_spi_frame_size_t @endif */

    uint32_t tmod;                      /*!< @if Eng Indicates the transfer mode.
                                                     For details, see @ref hal_spi_trans_mode_t
                                             @else   SPI的传输模式。参考 @ref hal_spi_trans_mode_t @endif */

    uint32_t ndf;                       /*!< @if Eng Indicates the number of data frames.
                                             @else   SPI的数据帧数。 @endif */

    uint32_t sste;                      /*!< @if Eng Indicates if SPI slave select toggle enable or not.
                                                     When disable, master should reed all data in slave tx_queue
                                                     at ONE time when reading data from slave device. Otherwise,
                                                     data loss occurs.
                                                     For details, see @ref hal_spi_cfg_sste_t
                                             @else   SPI从机选择切换使能/不使能。
                                                     当此配置不使能，主机从从机读取数据时，需要一次性将从机发送
                                                     队列中的数据读完，否则会出现丢失数据问题。
                                                     参考 @ref hal_spi_cfg_sste_t @endif */
} hal_spi_attr_t;

/**
 * @if Eng
 * @brief  Definition of SPI extra attributes.
 * @else
 * @brief  SPI扩展配置参数定义。
 * @endif
 */
typedef struct hal_spi_extra_attr {
    bool tx_use_dma;                        /*!< @if Eng Indicates if SPI use dma or not in TX.
                                                 @else   SPI是否使用DMA发送数据。 @endif */

    bool rx_use_dma;                        /*!< @if Eng Indicates if SPI use dma or not in RX.
                                                 @else   SPI是否使用DMA接收数据。 @endif */

    hal_spi_xfer_qspi_param_t qspi_param;   /*!< @if Eng Indicates the qspi parameters.
                                                 @else   QSPI参数。 @endif */

    hal_spi_xfer_sspi_param_t sspi_param;   /*!< @if Eng Indicates the single spi parameters.
                                                 @else   Single SPI参数。 @endif */
} hal_spi_extra_attr_t;

/**
 * @if Eng
 * @brief  SPI transfer data structure.
 * @else
 * @brief  SPI传输结构体。
 * @endif
 */
typedef struct hal_spi_xfer_data {
    uint8_t *tx_buff;       /*!< @if Eng Buff to send data through tx fifo.
                                 @else   通过tx fifo发送数据的Buff。 @endif */
    uint32_t tx_bytes;      /*!< @if Eng Bytes of data need to send. For details, see @ref hal_spi_attr_t.frame_size.
                                         when frame_size is HAL_SPI_FRAME_SIZE_8, The value must be a multiple of 1.
                                         when frame_size is HAL_SPI_FRAME_SIZE_16, The value must be a multiple of 2.
                                         when frame_size is HAL_SPI_FRAME_SIZE_24, The value must be a multiple of 3.
                                         when frame_size is HAL_SPI_FRAME_SIZE_32, The value must be a multiple of 4.
                                 @else   发送数据的个数。参考 @ref hal_spi_attr_t.frame_size.
                                         如果frame_size为HAL_SPI_FRAME_SIZE_8，则需设定为1的倍数
                                         如果frame_size为HAL_SPI_FRAME_SIZE_16，则需设定为2的倍数
                                         如果frame_size为HAL_SPI_FRAME_SIZE_24，则需设定为3的倍数
                                         如果frame_size为HAL_SPI_FRAME_SIZE_32，则需设定为4的倍数
                                 @endif */
    uint8_t *rx_buff;       /*!< @if Eng Buff to receive data from rx fifo.
                                 @else   通过rx fifo接收数据的Buff。 @endif */
    uint32_t rx_bytes;      /*!< @if Eng Bytes of data need to receive, For details, see @ref hal_spi_attr_t.frame_size.
                                         when frame_size is HAL_SPI_FRAME_SIZE_8, The value must be a multiple of 1.
                                         when frame_size is HAL_SPI_FRAME_SIZE_16, The value must be a multiple of 2.
                                         when frame_size is HAL_SPI_FRAME_SIZE_24, The value must be a multiple of 3.
                                         when frame_size is HAL_SPI_FRAME_SIZE_32, The value must be a multiple of 4.
                                 @else   接收数据的个数。参考 @ref hal_spi_attr_t.frame_size.
                                         如果frame_size为HAL_SPI_FRAME_SIZE_8，则需设定为1的倍数
                                         如果frame_size为HAL_SPI_FRAME_SIZE_16，则需设定为2的倍数
                                         如果frame_size为HAL_SPI_FRAME_SIZE_24，则需设定为3的倍数
                                         如果frame_size为HAL_SPI_FRAME_SIZE_32，则需设定为4的倍数
                                 @endif */
    uint8_t cmd;            /*!< @if Eng Command for QSPI mode.
                                 @else   QSPI模式下的命令。 @endif */
    uint8_t reserved[3];    /*!< @if Eng Reserved.
                                 @else   保留。 @endif */
    uint32_t addr;          /*!< @if Eng Address for QSPI mode.
                                 @else   QSPI模式下的地址。 @endif */
} hal_spi_xfer_data_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| tx_buff | uint8_t * | 通过 TX FIFO 发送数据的缓冲区 |
| tx_bytes | uint32_t | 发送数据的字节数（须为帧大小对应字节数的整数倍） |
| rx_buff | uint8_t * | 从 RX FIFO 接收数据的缓冲区 |
| rx_bytes | uint32_t | 接收数据的字节数（须为帧大小对应字节数的整数倍） |
| cmd | uint8_t | QSPI 模式的指令 |
| reserved | uint8_t[3] | 保留 |
| addr | uint32_t | QSPI 模式的地址 |

### struct hal_spi_xfer_qspi_param_t <a id="hal_spi_xfer_qspi_param_t"></a>

```c
typedef enum hal_spi_ctrl_id {
    SPI_CTRL_SET_ATTR,                  /*!< @if Eng Set SPI basic attribute.
                                             @else   设置基础参数。 @endif */

    SPI_CTRL_GET_ATTR,                  /*!< @if Eng Get SPI basic attribute.
                                             @else   获取基础参数。 @endif */

    SPI_CTRL_SET_EXTRA_ATTR,            /*!< @if Eng Set SPI extral attribute.
                                             @else   设置高级参数。 @endif */

    SPI_CTRL_GET_EXTRA_ATTR,            /*!< @if Eng Get SPI extral attribute.
                                             @else   获取高级参数。 @endif */

    SPI_CTRL_SELECT_SLAVE,              /*!< @if Eng Select the slave.
                                             @else   选择指定的设备。 @endif */

    SPI_CTRL_CHECK_FIFO_BUSY,           /*!< @if Eng Check whether the SPI is busy.
                                             @else   检查SPI是否忙碌状态。 @endif */
#if defined(CONFIG_SPI_SUPPORT_DMA) && (CONFIG_SPI_SUPPORT_DMA == 1)
    SPI_CTRL_SET_DMA_CFG,               /*!< @if Eng Set the DMA transfer enable/disable and datalevel.
                                             @else   设置DMA的传输使能和数据level。 @endif */

    SPI_CTRL_GET_DMA_DATA_ADDR,         /*!< @if Eng Get the DMA transfer data address.
                                             @else   获取DMA的传输数据地址。 @endif */
#endif  /* CONFIG_SPI_SUPPORT_DMA */

#if defined(CONFIG_SPI_SUPPORT_INTERRUPT) && (CONFIG_SPI_SUPPORT_INTERRUPT == 1)
    SPI_CTRL_EN_RXFI_INT,               /*!< @if Eng Enable the Receive FIFO full interrupt.
                                             @else   使能RX FIFO是否已满中断。 @endif */

    SPI_CTRL_CHECK_RX_FIFO_EMPTY,       /*!< @if Eng Check if rx fifo is empty or not.
                                             @else   判断RX FIFO是否为空。 @endif */

    SPI_CTRL_EN_TXEI_INT,               /*!< @if Eng Enable the transmit FIFO empty interrupt.
                                             @else   使能TX FIFO是否为空中断。 @endif */

    SPI_CTRL_CHECK_TX_FIFO_FULL,        /*!< @if Eng Check if tx fifo is full or not.
                                             @else   判断RX FIFO是否已满。 @endif */

    SPI_CTRL_EN_MULTI_MASTER_ERR_INT,   /*!< @if Eng Enable the Multi-Master contention interrupt.
                                             @else   使能双主机竞争中断。 @endif */
#endif  /* CONFIG_SPI_SUPPORT_INTERRUPT */

#if defined(CONFIG_SPI_SUPPORT_LPM) && (CONFIG_SPI_SUPPORT_LPM == 1)
    SPI_CTRL_SUSPEND,                   /*!< @if Eng Suspend all of the spi channels.
                                             @else   挂起所有spi通道。 @endif */
    SPI_CTRL_RESUME,                    /*!< @if Eng Resume all of the spi channels.
                                             @else   挂起所有spi通道。 @endif */
#endif  /* CONFIG_SPI_SUPPORT_LPM */
    SPI_CTRL_SET_TMOD,                  /*!< @if Eng Set SPI transfer mode.
                                             @else   设置SPI传输模式。 @endif */
    SPI_CTRL_MAX,
    SPI_CTRL_ID_INVALID = 0xFF
} hal_spi_ctrl_id_t;

/**
 * @if Eng
 * @brief  Frame Format.
 * @else
 * @brief  帧格式。
 * @endif
 */
typedef enum hal_spi_cfg_frame_format {
    SPI_CFG_FRAME_FORMAT_MOTOROLA_SPI,      /*!< @if Eng Motorolla SPI Frame Format.
                                                 @else   摩托罗拉SPI帧格式。 @endif */

    SPI_CFG_FRAME_FORMAT_TEXAS_SSP,         /*!< @if Eng Texas Instruments SSP Frame Format.
                                                 @else   德州仪器SSP帧格式。 @endif */

    SPI_CFG_FRAME_FORMAT_NS_MICROWIRE,      /*!< @if Eng National Microwire Frame Format.
                                                 @else   国家微线帧格式。 @endif */
    SPI_CFG_FRAME_FORMAT_MAX
} hal_spi_cfg_frame_format_t;

/**
 * @if Eng
 * @brief  Clock polarity.
 * @else
 * @brief  时钟极性。
 * @endif
 */
typedef enum hal_spi_cfg_clk_cpol {
    SPI_CFG_CLK_CPOL_0,                     /*!< @if Eng Inactive state of serial clock is low.
                                                 @else   SPI的非激活状态为低电平。 @endif */

    SPI_CFG_CLK_CPOL_1,                     /*!< @if Eng Inactive state of serial clock is high.
                                                 @else   SPI的非激活状态为高电平。 @endif */
    SPI_CFG_CLK_CPOL_MAX
} hal_spi_cfg_clk_cpol_t;

/**
 * @if Eng
 * @brief  Clock phase.
 * @else
 * @brief  时钟相位。
 * @endif
 */
typedef enum hal_spi_cfg_clk_cpha {
    SPI_CFG_CLK_CPHA_0,                     /*!< @if Eng Serial clock toggles in middle of first data bit.
                                                 @else   SPI时钟在第一个数据位中间切换。 @endif */

    SPI_CFG_CLK_CPHA_1,                     /*!< @if Eng Serial clock toggles at start of first data bit.
                                                 @else   SPI时钟在第一个数据位开始时切换。 @endif */
    SPI_CFG_CLK_CPHA_MAX
} hal_spi_cfg_clk_cpha_t;

/**
 * @if Eng
 * @brief  SPI slave select toggle enable.
 * @else
 * @brief  SPI 从机选择切换使能
 * @endif
 */
typedef enum hal_spi_cfg_sste {
    SPI_CFG_SSTE_DISABLE,                   /*!< @if Eng SPI slave select toggle disable.
                                                         When disable, master should reed all data in slave tx_queue
                                                         at ONE time when reading data from slave device. Otherwise,
                                                         data loss occurs.
                                                 @else   SPI 从机选择切换不使能。
                                                         当此配置不使能，主机从从机读取数据时，需要一次性将从机发送
                                                         队列中的数据读完，否则会出现丢失数据问题。@endif */
    SPI_CFG_SSTE_ENABLE,                    /*!< @if Eng SPI slave select toggle enable.
                                                 @else   SPI 从机选择切换使能 @endif */
    SPI_CFG_SSTE_MAX
} hal_spi_cfg_sste_t;

/**
 * @if Eng
 * @brief  Transfer Mode.
 * @else
 * @brief  传输模式。
 * @endif
 */
typedef enum hal_spi_trans_mode {
    HAL_SPI_TRANS_MODE_TXRX = 0,            /*!< @if Eng Transmit and receive mode.
                                                 @else   收发模式。 @endif */

    HAL_SPI_TRANS_MODE_TX,                  /*!< @if Eng Transmit only / Transmit mode.
                                                 @else   发送模式。 @endif */

    HAL_SPI_TRANS_MODE_RX,                  /*!< @if Eng Receive only / Receive mode.
                                                 @else   接收模式。 @endif */

    HAL_SPI_TRANS_MODE_EEPROM,              /*!< @if Eng EEPROM read mode.
                                                 @else   EEPROM模式。 @endif */
    HAL_SPI_TRANS_MODE_MAX
} hal_spi_trans_mode_t;

/**
 * @if Eng
 * @brief  Data Frame Size.
 * @else
 * @brief  数据帧长度。
 * @endif
 */
typedef enum hal_spi_frame_size {
    HAL_SPI_FRAME_SIZE_8    = 0x07,         /*!< @if Eng 8-bit serial data transfer.
                                                 @else   8-位串行数据传输。 @endif */

    HAL_SPI_FRAME_SIZE_16   = 0x0F,         /*!< @if Eng 16-bit serial data transfer(Not supported now).
                                                 @else   16-位串行数据传输（暂不支持）。 @endif */

    HAL_SPI_FRAME_SIZE_24   = 0x17,         /*!< @if Eng 24-bit serial data transfer(Not supported now).
                                                 @else   24-位串行数据传输（暂不支持）。 @endif */

    HAL_SPI_FRAME_SIZE_32   = 0x1F          /*!< @if Eng 32-bit serial data transfer.
                                                 @else   32-位串行数据传输。 @endif */
} hal_spi_frame_size_t;

/**
 * @if Eng
 * @brief  SPI Frame Format.
 * @else
 * @brief  SPI数据帧格式。
 * @endif
 */
typedef enum hal_spi_frame_format {
    HAL_SPI_FRAME_FORMAT_STANDARD = 0,      /*!< @if Eng SPI Standard frame format.
                                                 @else   标准的单线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_DUAL,              /*!< @if Eng SPI Dual frame format.
                                                 @else   双线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_QUAD,              /*!< @if Eng SPI Quad frame format.
                                                 @else   4线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_OCTAL,             /*!< @if Eng SPI Octal frame format.
                                                 @else   8线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_DOUBLE_OCTAL,      /*!< @if Eng SPI Double Octal frame format.
                                                 @else   16线SPI帧格式。 @endif */
    HAL_SPI_FRAME_FORMAT_SIXT,
    HAL_SPI_FRAME_FORMAT_MAX_NUM,
    HAL_SPI_FRAME_FORMAT_NONE = HAL_SPI_FRAME_FORMAT_MAX_NUM
} hal_spi_frame_format_t;

/**
 * @if Eng
 * @brief  SPI Transfer Types.
 * @else
 * @brief  SPI传输类型。
 * @endif
 */
typedef enum hal_spi_trans_type {
    HAL_SPI_TRANS_TYPE_INST_S_ADDR_S = 0,   /*!< @if Eng Instruction and Address will be sent in standard SPI mode.
                                                 @else   指令和地址使用单线SPI传输。 @endif */

    HAL_SPI_TRANS_TYPE_INST_S_ADDR_Q,       /*!< @if Eng Instruction will be sent in standard mode and address will
                                                         be sent in mode specified by frame format register.
                                                 @else   指令使用单线SPI传输，
                                                         地址按照帧格式寄存器的配置传输。 @endif */

    HAL_SPI_TRANS_TYPE_INST_Q_ADDR_Q,       /*!< @if Eng Both instruction and address will be sent in
                                                         the mode specified by frame format register.
                                                 @else   指令和地址都按照帧格式寄存器的配置传输。 @endif */
    HAL_SPI_TRANS_TYPE_MAX = HAL_SPI_TRANS_TYPE_INST_Q_ADDR_Q
} hal_spi_trans_type_t;

/**
 * @if Eng
 * @brief  SPI length of instruction.
 * @else
 * @brief  SPI指令长度定义。
 * @endif
 */
typedef enum hal_spi_inst_len {
    HAL_SPI_INST_LEN_0 = 0,                 /*!< @if Eng 0-bit (no instruction).
                                                 @else   不携带指令。 @endif */

    HAL_SPI_INST_LEN_4,                     /*!< @if Eng 4-bit instruction.
                                                 @else   4-位指令。 @endif */

    HAL_SPI_INST_LEN_8,                     /*!< @if Eng 8-bit instruction.
                                                 @else   8-位指令。 @endif */

    HAL_SPI_INST_LEN_16,                    /*!< @if Eng 16-bit instruction.
                                                 @else   16-位指令。 @endif */
    HAL_SPI_INST_LEN_MAX = HAL_SPI_INST_LEN_16
} hal_spi_inst_len_t;

/**
 * @if Eng
 * @brief  SPI length of address.
 * @else
 * @brief  SPI地址长度定义。
 * @endif
 */
typedef enum hal_spi_addr_len {
    HAL_SPI_ADDR_LEN_0 = 0,                 /*!< @if Eng 0-bit address length.
                                                 @else   0-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_4,                     /*!< @if Eng 4-bit address length.
                                                 @else   4-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_8,                     /*!< @if Eng 8-bit address length.
                                                 @else   8-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_12,                    /*!< @if Eng 12-bit address length.
                                                 @else   12-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_16,                    /*!< @if Eng 16-bit address length.
                                                 @else   16-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_20,                    /*!< @if Eng 20-bit address length.
                                                 @else   20-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_24,                    /*!< @if Eng 24-bit address length.
                                                 @else   24-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_28,                    /*!< @if Eng 28-bit address length.
                                                 @else   28-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_32,                    /*!< @if Eng 32-bit address length.
                                                 @else   32-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_36,                    /*!< @if Eng 36-bit address length.
                                                 @else   36-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_40,                    /*!< @if Eng 40-bit address length.
                                                 @else   40-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_44,                    /*!< @if Eng 44-bit address length.
                                                 @else   44-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_48,                    /*!< @if Eng 48-bit address length.
                                                 @else   48-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_52,                    /*!< @if Eng 52-bit address length.
                                                 @else   52-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_56,                    /*!< @if Eng 56-bit address length.
                                                 @else   56-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_60,                    /*!< @if Eng 60-bit address length.
                                                 @else   60-位地址长度。 @endif */
    HAL_SPI_ADDR_LEN_MAX = HAL_SPI_ADDR_LEN_60
} hal_spi_addr_len_t;

/**
 * @if Eng
 * @brief  Definition of the event ID of hal spi.
 * @else
 * @brief  HAL层SPI事件ID的定义
 * @endif
 */
typedef enum hal_spi_evt_id {
    SPI_EVT_RX_FULL_ISR,           /*!< @if Eng Rx full isr triggered.
                                        @else   接收满中断触发 @endif */
    SPI_EVT_RX_OVERFLOW_ISR,       /*!< @if Eng Rx overflow isr triggered.
                                        @else   接收溢出中断触发 @endif */
    SPI_EVT_RX_UNDERFLOW_ISR,      /*!< @if Eng Rx underflow isr triggered.
                                        @else   接收空读中断触发 @endif */
    SPI_EVT_TX_EMPTY_ISR,          /*!< @if Eng Tx empty isr triggered.
                                        @else   TX空中断被触发 @endif */
    SPI_EVT_TX_OVERFLOW_ISR,       /*!< @if Eng Tx overflow isr triggered.
                                        @else   TX溢出中断被触发 @endif */
    SPI_EVT_MULTI_MASTER_ISR       /*!< @if Eng Multi-master contention isr triggered.
                                        @else   双主机竞争中断被触发 @endif */
} hal_spi_evt_id_t;

/**
 * @if Eng
 * @brief  QSPI parameters of SPI transfer.
 * @else
 * @brief  SPI传输中QSPI的参数。
 * @endif
 */
typedef struct hal_spi_xfer_qspi_param {
    hal_spi_trans_type_t trans_type;  /*!< @if Eng SPI frame format for instruction and address.
                                           @else   传输类型，用于指定指令和地址的长度。 @endif */

    hal_spi_inst_len_t   inst_len;    /*!< @if Eng Instruction length, support 0, 4, 8, 16bits.
                                           @else   指令长度，支持0、4、8、16位。 @endif */

    hal_spi_addr_len_t   addr_len;    /*!< @if Eng Address length, support 0, 8, 16, 24, 32bits.
                                           @else   地址长度，支持0、8、16、24、32位。 @endif */

    uint32_t             wait_cycles; /*!< @if Eng Indicates the wait cycles.
                                           @else   等待的周期数。 @endif */
} hal_spi_xfer_qspi_param_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| trans_type | hal_spi_trans_type_t | 传输类型，用于指定指令和地址的长度 |
| inst_len | hal_spi_inst_len_t | 指令长度，支持 0、4、8、16 位 |
| addr_len | hal_spi_addr_len_t | 地址长度，支持 0、8、16、24、32 位 |

### struct hal_spi_xfer_sspi_param_t <a id="hal_spi_xfer_sspi_param_t"></a>

```c
typedef enum hal_spi_ctrl_id {
    SPI_CTRL_SET_ATTR,                  /*!< @if Eng Set SPI basic attribute.
                                             @else   设置基础参数。 @endif */

    SPI_CTRL_GET_ATTR,                  /*!< @if Eng Get SPI basic attribute.
                                             @else   获取基础参数。 @endif */

    SPI_CTRL_SET_EXTRA_ATTR,            /*!< @if Eng Set SPI extral attribute.
                                             @else   设置高级参数。 @endif */

    SPI_CTRL_GET_EXTRA_ATTR,            /*!< @if Eng Get SPI extral attribute.
                                             @else   获取高级参数。 @endif */

    SPI_CTRL_SELECT_SLAVE,              /*!< @if Eng Select the slave.
                                             @else   选择指定的设备。 @endif */

    SPI_CTRL_CHECK_FIFO_BUSY,           /*!< @if Eng Check whether the SPI is busy.
                                             @else   检查SPI是否忙碌状态。 @endif */
#if defined(CONFIG_SPI_SUPPORT_DMA) && (CONFIG_SPI_SUPPORT_DMA == 1)
    SPI_CTRL_SET_DMA_CFG,               /*!< @if Eng Set the DMA transfer enable/disable and datalevel.
                                             @else   设置DMA的传输使能和数据level。 @endif */

    SPI_CTRL_GET_DMA_DATA_ADDR,         /*!< @if Eng Get the DMA transfer data address.
                                             @else   获取DMA的传输数据地址。 @endif */
#endif  /* CONFIG_SPI_SUPPORT_DMA */

#if defined(CONFIG_SPI_SUPPORT_INTERRUPT) && (CONFIG_SPI_SUPPORT_INTERRUPT == 1)
    SPI_CTRL_EN_RXFI_INT,               /*!< @if Eng Enable the Receive FIFO full interrupt.
                                             @else   使能RX FIFO是否已满中断。 @endif */

    SPI_CTRL_CHECK_RX_FIFO_EMPTY,       /*!< @if Eng Check if rx fifo is empty or not.
                                             @else   判断RX FIFO是否为空。 @endif */

    SPI_CTRL_EN_TXEI_INT,               /*!< @if Eng Enable the transmit FIFO empty interrupt.
                                             @else   使能TX FIFO是否为空中断。 @endif */

    SPI_CTRL_CHECK_TX_FIFO_FULL,        /*!< @if Eng Check if tx fifo is full or not.
                                             @else   判断RX FIFO是否已满。 @endif */

    SPI_CTRL_EN_MULTI_MASTER_ERR_INT,   /*!< @if Eng Enable the Multi-Master contention interrupt.
                                             @else   使能双主机竞争中断。 @endif */
#endif  /* CONFIG_SPI_SUPPORT_INTERRUPT */

#if defined(CONFIG_SPI_SUPPORT_LPM) && (CONFIG_SPI_SUPPORT_LPM == 1)
    SPI_CTRL_SUSPEND,                   /*!< @if Eng Suspend all of the spi channels.
                                             @else   挂起所有spi通道。 @endif */
    SPI_CTRL_RESUME,                    /*!< @if Eng Resume all of the spi channels.
                                             @else   挂起所有spi通道。 @endif */
#endif  /* CONFIG_SPI_SUPPORT_LPM */
    SPI_CTRL_SET_TMOD,                  /*!< @if Eng Set SPI transfer mode.
                                             @else   设置SPI传输模式。 @endif */
    SPI_CTRL_MAX,
    SPI_CTRL_ID_INVALID = 0xFF
} hal_spi_ctrl_id_t;

/**
 * @if Eng
 * @brief  Frame Format.
 * @else
 * @brief  帧格式。
 * @endif
 */
typedef enum hal_spi_cfg_frame_format {
    SPI_CFG_FRAME_FORMAT_MOTOROLA_SPI,      /*!< @if Eng Motorolla SPI Frame Format.
                                                 @else   摩托罗拉SPI帧格式。 @endif */

    SPI_CFG_FRAME_FORMAT_TEXAS_SSP,         /*!< @if Eng Texas Instruments SSP Frame Format.
                                                 @else   德州仪器SSP帧格式。 @endif */

    SPI_CFG_FRAME_FORMAT_NS_MICROWIRE,      /*!< @if Eng National Microwire Frame Format.
                                                 @else   国家微线帧格式。 @endif */
    SPI_CFG_FRAME_FORMAT_MAX
} hal_spi_cfg_frame_format_t;

/**
 * @if Eng
 * @brief  Clock polarity.
 * @else
 * @brief  时钟极性。
 * @endif
 */
typedef enum hal_spi_cfg_clk_cpol {
    SPI_CFG_CLK_CPOL_0,                     /*!< @if Eng Inactive state of serial clock is low.
                                                 @else   SPI的非激活状态为低电平。 @endif */

    SPI_CFG_CLK_CPOL_1,                     /*!< @if Eng Inactive state of serial clock is high.
                                                 @else   SPI的非激活状态为高电平。 @endif */
    SPI_CFG_CLK_CPOL_MAX
} hal_spi_cfg_clk_cpol_t;

/**
 * @if Eng
 * @brief  Clock phase.
 * @else
 * @brief  时钟相位。
 * @endif
 */
typedef enum hal_spi_cfg_clk_cpha {
    SPI_CFG_CLK_CPHA_0,                     /*!< @if Eng Serial clock toggles in middle of first data bit.
                                                 @else   SPI时钟在第一个数据位中间切换。 @endif */

    SPI_CFG_CLK_CPHA_1,                     /*!< @if Eng Serial clock toggles at start of first data bit.
                                                 @else   SPI时钟在第一个数据位开始时切换。 @endif */
    SPI_CFG_CLK_CPHA_MAX
} hal_spi_cfg_clk_cpha_t;

/**
 * @if Eng
 * @brief  SPI slave select toggle enable.
 * @else
 * @brief  SPI 从机选择切换使能
 * @endif
 */
typedef enum hal_spi_cfg_sste {
    SPI_CFG_SSTE_DISABLE,                   /*!< @if Eng SPI slave select toggle disable.
                                                         When disable, master should reed all data in slave tx_queue
                                                         at ONE time when reading data from slave device. Otherwise,
                                                         data loss occurs.
                                                 @else   SPI 从机选择切换不使能。
                                                         当此配置不使能，主机从从机读取数据时，需要一次性将从机发送
                                                         队列中的数据读完，否则会出现丢失数据问题。@endif */
    SPI_CFG_SSTE_ENABLE,                    /*!< @if Eng SPI slave select toggle enable.
                                                 @else   SPI 从机选择切换使能 @endif */
    SPI_CFG_SSTE_MAX
} hal_spi_cfg_sste_t;

/**
 * @if Eng
 * @brief  Transfer Mode.
 * @else
 * @brief  传输模式。
 * @endif
 */
typedef enum hal_spi_trans_mode {
    HAL_SPI_TRANS_MODE_TXRX = 0,            /*!< @if Eng Transmit and receive mode.
                                                 @else   收发模式。 @endif */

    HAL_SPI_TRANS_MODE_TX,                  /*!< @if Eng Transmit only / Transmit mode.
                                                 @else   发送模式。 @endif */

    HAL_SPI_TRANS_MODE_RX,                  /*!< @if Eng Receive only / Receive mode.
                                                 @else   接收模式。 @endif */

    HAL_SPI_TRANS_MODE_EEPROM,              /*!< @if Eng EEPROM read mode.
                                                 @else   EEPROM模式。 @endif */
    HAL_SPI_TRANS_MODE_MAX
} hal_spi_trans_mode_t;

/**
 * @if Eng
 * @brief  Data Frame Size.
 * @else
 * @brief  数据帧长度。
 * @endif
 */
typedef enum hal_spi_frame_size {
    HAL_SPI_FRAME_SIZE_8    = 0x07,         /*!< @if Eng 8-bit serial data transfer.
                                                 @else   8-位串行数据传输。 @endif */

    HAL_SPI_FRAME_SIZE_16   = 0x0F,         /*!< @if Eng 16-bit serial data transfer(Not supported now).
                                                 @else   16-位串行数据传输（暂不支持）。 @endif */

    HAL_SPI_FRAME_SIZE_24   = 0x17,         /*!< @if Eng 24-bit serial data transfer(Not supported now).
                                                 @else   24-位串行数据传输（暂不支持）。 @endif */

    HAL_SPI_FRAME_SIZE_32   = 0x1F          /*!< @if Eng 32-bit serial data transfer.
                                                 @else   32-位串行数据传输。 @endif */
} hal_spi_frame_size_t;

/**
 * @if Eng
 * @brief  SPI Frame Format.
 * @else
 * @brief  SPI数据帧格式。
 * @endif
 */
typedef enum hal_spi_frame_format {
    HAL_SPI_FRAME_FORMAT_STANDARD = 0,      /*!< @if Eng SPI Standard frame format.
                                                 @else   标准的单线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_DUAL,              /*!< @if Eng SPI Dual frame format.
                                                 @else   双线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_QUAD,              /*!< @if Eng SPI Quad frame format.
                                                 @else   4线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_OCTAL,             /*!< @if Eng SPI Octal frame format.
                                                 @else   8线SPI帧格式。 @endif */

    HAL_SPI_FRAME_FORMAT_DOUBLE_OCTAL,      /*!< @if Eng SPI Double Octal frame format.
                                                 @else   16线SPI帧格式。 @endif */
    HAL_SPI_FRAME_FORMAT_SIXT,
    HAL_SPI_FRAME_FORMAT_MAX_NUM,
    HAL_SPI_FRAME_FORMAT_NONE = HAL_SPI_FRAME_FORMAT_MAX_NUM
} hal_spi_frame_format_t;

/**
 * @if Eng
 * @brief  SPI Transfer Types.
 * @else
 * @brief  SPI传输类型。
 * @endif
 */
typedef enum hal_spi_trans_type {
    HAL_SPI_TRANS_TYPE_INST_S_ADDR_S = 0,   /*!< @if Eng Instruction and Address will be sent in standard SPI mode.
                                                 @else   指令和地址使用单线SPI传输。 @endif */

    HAL_SPI_TRANS_TYPE_INST_S_ADDR_Q,       /*!< @if Eng Instruction will be sent in standard mode and address will
                                                         be sent in mode specified by frame format register.
                                                 @else   指令使用单线SPI传输，
                                                         地址按照帧格式寄存器的配置传输。 @endif */

    HAL_SPI_TRANS_TYPE_INST_Q_ADDR_Q,       /*!< @if Eng Both instruction and address will be sent in
                                                         the mode specified by frame format register.
                                                 @else   指令和地址都按照帧格式寄存器的配置传输。 @endif */
    HAL_SPI_TRANS_TYPE_MAX = HAL_SPI_TRANS_TYPE_INST_Q_ADDR_Q
} hal_spi_trans_type_t;

/**
 * @if Eng
 * @brief  SPI length of instruction.
 * @else
 * @brief  SPI指令长度定义。
 * @endif
 */
typedef enum hal_spi_inst_len {
    HAL_SPI_INST_LEN_0 = 0,                 /*!< @if Eng 0-bit (no instruction).
                                                 @else   不携带指令。 @endif */

    HAL_SPI_INST_LEN_4,                     /*!< @if Eng 4-bit instruction.
                                                 @else   4-位指令。 @endif */

    HAL_SPI_INST_LEN_8,                     /*!< @if Eng 8-bit instruction.
                                                 @else   8-位指令。 @endif */

    HAL_SPI_INST_LEN_16,                    /*!< @if Eng 16-bit instruction.
                                                 @else   16-位指令。 @endif */
    HAL_SPI_INST_LEN_MAX = HAL_SPI_INST_LEN_16
} hal_spi_inst_len_t;

/**
 * @if Eng
 * @brief  SPI length of address.
 * @else
 * @brief  SPI地址长度定义。
 * @endif
 */
typedef enum hal_spi_addr_len {
    HAL_SPI_ADDR_LEN_0 = 0,                 /*!< @if Eng 0-bit address length.
                                                 @else   0-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_4,                     /*!< @if Eng 4-bit address length.
                                                 @else   4-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_8,                     /*!< @if Eng 8-bit address length.
                                                 @else   8-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_12,                    /*!< @if Eng 12-bit address length.
                                                 @else   12-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_16,                    /*!< @if Eng 16-bit address length.
                                                 @else   16-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_20,                    /*!< @if Eng 20-bit address length.
                                                 @else   20-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_24,                    /*!< @if Eng 24-bit address length.
                                                 @else   24-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_28,                    /*!< @if Eng 28-bit address length.
                                                 @else   28-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_32,                    /*!< @if Eng 32-bit address length.
                                                 @else   32-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_36,                    /*!< @if Eng 36-bit address length.
                                                 @else   36-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_40,                    /*!< @if Eng 40-bit address length.
                                                 @else   40-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_44,                    /*!< @if Eng 44-bit address length.
                                                 @else   44-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_48,                    /*!< @if Eng 48-bit address length.
                                                 @else   48-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_52,                    /*!< @if Eng 52-bit address length.
                                                 @else   52-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_56,                    /*!< @if Eng 56-bit address length.
                                                 @else   56-位地址长度。 @endif */

    HAL_SPI_ADDR_LEN_60,                    /*!< @if Eng 60-bit address length.
                                                 @else   60-位地址长度。 @endif */
    HAL_SPI_ADDR_LEN_MAX = HAL_SPI_ADDR_LEN_60
} hal_spi_addr_len_t;

/**
 * @if Eng
 * @brief  Definition of the event ID of hal spi.
 * @else
 * @brief  HAL层SPI事件ID的定义
 * @endif
 */
typedef enum hal_spi_evt_id {
    SPI_EVT_RX_FULL_ISR,           /*!< @if Eng Rx full isr triggered.
                                        @else   接收满中断触发 @endif */
    SPI_EVT_RX_OVERFLOW_ISR,       /*!< @if Eng Rx overflow isr triggered.
                                        @else   接收溢出中断触发 @endif */
    SPI_EVT_RX_UNDERFLOW_ISR,      /*!< @if Eng Rx underflow isr triggered.
                                        @else   接收空读中断触发 @endif */
    SPI_EVT_TX_EMPTY_ISR,          /*!< @if Eng Tx empty isr triggered.
                                        @else   TX空中断被触发 @endif */
    SPI_EVT_TX_OVERFLOW_ISR,       /*!< @if Eng Tx overflow isr triggered.
                                        @else   TX溢出中断被触发 @endif */
    SPI_EVT_MULTI_MASTER_ISR       /*!< @if Eng Multi-master contention isr triggered.
                                        @else   双主机竞争中断被触发 @endif */
} hal_spi_evt_id_t;

/**
 * @if Eng
 * @brief  QSPI parameters of SPI transfer.
 * @else
 * @brief  SPI传输中QSPI的参数。
 * @endif
 */
typedef struct hal_spi_xfer_qspi_param {
    hal_spi_trans_type_t trans_type;  /*!< @if Eng SPI frame format for instruction and address.
                                           @else   传输类型，用于指定指令和地址的长度。 @endif */

    hal_spi_inst_len_t   inst_len;    /*!< @if Eng Instruction length, support 0, 4, 8, 16bits.
                                           @else   指令长度，支持0、4、8、16位。 @endif */

    hal_spi_addr_len_t   addr_len;    /*!< @if Eng Address length, support 0, 8, 16, 24, 32bits.
                                           @else   地址长度，支持0、8、16、24、32位。 @endif */

    uint32_t             wait_cycles; /*!< @if Eng Indicates the wait cycles.
                                           @else   等待的周期数。 @endif */
} hal_spi_xfer_qspi_param_t;

/**
 * @if Eng
 * @brief  Single SPI parameters of SPI transfer.
 * @else
 * @brief  SPI传输中Single SPI的参数。
 * @endif
 */
typedef struct hal_spi_xfer_sspi_param {
    uint32_t             wait_cycles; /*!< @if Eng Indicates the wait cycles.
                                           @else   等待的周期数。 @endif */
} hal_spi_xfer_sspi_param_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| wait_cycles | uint32_t | 等待的周期数 |


## Macros

### SPI_BUS_MAX_NUM <a id="SPI_BUS_MAX_NUM"></a>

```c
#define SPI_BUS_MAX_NUM SPI_BUS_MAX_NUMBER
```

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```

### ERRCODE_INVALID_PARAM <a id="ERRCODE_INVALID_PARAM"></a>

```c
#define ERRCODE_INVALID_PARAM                               0x80000001
```

### ERRCODE_FAIL <a id="ERRCODE_FAIL"></a>

```c
#define ERRCODE_FAIL                                        0xFFFFFFFF
```

### ERRCODE_SPI_CONFIG_FAIL <a id="ERRCODE_SPI_CONFIG_FAIL"></a>

```c
#define ERRCODE_SPI_CONFIG_FAIL                             0x80001330
```

### ERRCODE_SPI_MODE_MISMATCH <a id="ERRCODE_SPI_MODE_MISMATCH"></a>

```c
#define ERRCODE_SPI_MODE_MISMATCH                           0x80001332
```

### ERRCODE_SPI_TIMEOUT <a id="ERRCODE_SPI_TIMEOUT"></a>

```c
#define ERRCODE_SPI_TIMEOUT                                 0x80001333
```

### ERRCODE_SPI_DMA_CONFIG_ERROR <a id="ERRCODE_SPI_DMA_CONFIG_ERROR"></a>

```c
#define ERRCODE_SPI_DMA_CONFIG_ERROR                        0x80001336
```

### ERRCODE_SPI_DMA_TRANSFER_ERROR <a id="ERRCODE_SPI_DMA_TRANSFER_ERROR"></a>

```c
#define ERRCODE_SPI_DMA_TRANSFER_ERROR                      0x80001337
```

### ERRCODE_SPI_ADD_QUEUE_FAIL <a id="ERRCODE_SPI_ADD_QUEUE_FAIL"></a>

```c
#define ERRCODE_SPI_ADD_QUEUE_FAIL                          0x8000133B
```

### ERRCODE_SPI_DMA_IRQ_MODE_MUTEX <a id="ERRCODE_SPI_DMA_IRQ_MODE_MUTEX"></a>

```c
#define ERRCODE_SPI_DMA_IRQ_MODE_MUTEX                      0x8000133C
```

### ERRCODE_SPI_INVALID_TMODE <a id="ERRCODE_SPI_INVALID_TMODE"></a>

```c
#define ERRCODE_SPI_INVALID_TMODE                           0x8000133E
```
