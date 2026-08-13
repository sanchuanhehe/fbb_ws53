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

- 初始化指定 SPI 总线，将基础配置参数与高级配置参数下发到硬件
- 对已初始化的总线重复调用时直接返回成功，不重复执行初始化流程
- 返回前完成初始化状态标记的置位

**前置条件**

- 调用时序约束：调用本模块其他接口前必须先调用本接口成功返回
- 依赖关系：传入的 bus 必须小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM)，attr 不能为空
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待初始化的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
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
- 返回前完成初始化状态标记的清零

**前置条件**

- 调用时序约束：应在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 依赖关系：传入的 bus 必须小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM)
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待去初始化的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |

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
- 传输模式与接收数据帧数通过属性结构体下发到硬件控制接口
- 用于在运行时切换收发模式、发送模式、接收模式、EEPROM 读模式

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 依赖关系：传入的 bus 必须小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM)，tmod 必须小于 HAL_SPI_TRANS_MODE_MAX
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待设置的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| tmod | hal_spi_trans_mode_t | SPI 传输模式 | [HAL_SPI_TRANS_MODE_TXRX](#hal_spi_trans_mode_t)(0) / [HAL_SPI_TRANS_MODE_TX](#hal_spi_trans_mode_t)(1) / [HAL_SPI_TRANS_MODE_RX](#hal_spi_trans_mode_t)(2) / [HAL_SPI_TRANS_MODE_EEPROM](#hal_spi_trans_mode_t)(3) |
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
- 依赖关系：传入的 bus 必须小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM)，attr 不能为空
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待设置的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
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
- 依赖关系：传入的 bus 必须小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM)，attr 不能为空
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待读取的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| attr | spi_attr_t * | 用于接收基础配置参数的结构体指针 | 不为NULL |

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
- 依赖关系：传入的 bus 必须小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM)，extra_attr 不能为空
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待设置的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
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
- 依赖关系：传入的 bus 必须小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM)，extra_attr 不能为空
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待读取的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| extra_attr | spi_extra_attr_t * | 用于接收高级配置参数的结构体指针 | 不为NULL |

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
- 依赖关系：传入的 bus 必须小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM)，cs 必须小于 SPI_SLAVE_MAX_NUM，且总线必须配置为主机模式
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待操作的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
| cs | spi_slave_t | 被选中的从机设备 | 小于 SPI_SLAVE_MAX_NUM |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 参数合法且选择成功 |
| [ERRCODE_INVALID_PARAM](#ERRCODE_INVALID_PARAM):0x80000001 | 参数无效 | bus 大于等于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) 或 cs 大于等于 SPI_SLAVE_MAX_NUM |
| [ERRCODE_SPI_MODE_MISMATCH](#ERRCODE_SPI_MODE_MISMATCH):0x80001332 | 模式不匹配 | 总线未配置为主机模式 |
| Other | 其他错误码，参考errcode_t | HAL 控制接口执行失败 |

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
- 依赖关系：总线必须配置为主机模式，data 不能为空，传输模式不能与读取模式冲突
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待操作的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
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
- 依赖关系：总线必须配置为主机模式，data、rx_buff 不能为空且 rx_bytes 不为 0，传输模式不能与发送模式冲突
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待操作的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
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
- 依赖关系：总线必须配置为主机模式，data、rx_buff 不能为空且 rx_bytes 不为 0，传输模式不能与发送模式冲突
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待操作的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
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
- 依赖关系：总线必须配置为从机模式，data、tx_buff 不能为空且 tx_bytes 不为 0，传输模式不能与读取模式冲突
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待操作的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
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
- 依赖关系：总线必须配置为从机模式，data、rx_buff 不能为空且 rx_bytes 不为 0，传输模式不能与发送模式冲突
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待操作的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
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
- 依赖关系：总线必须配置为从机模式，data、rx_buff 不能为空且 rx_bytes 不为 0，传输模式不能与发送模式冲突
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待操作的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
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
- 使能时将 DMA 数据电平与配置参数下发到硬件控制接口
- 去使能时清零 DMA 收发数据电平

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用，使能 DMA 模式前需完成 DMA 初始化与打开
- 依赖关系：传入的 bus 必须小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM)，使能时 dma_cfg 不能为空；中断模式下使能 DMA 会被拒绝
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待设置的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
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
- 依赖关系：传入的 bus 必须小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM)，DMA 模式已使能时使能中断会被拒绝
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待设置的 SPI 总线编号 | 小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM) |
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
- 当前实现未对参数进行硬件操作，直接返回成功
- 用于预留环回测试能力

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 依赖关系：需开启 CONFIG_SPI_SUPPORT_LOOPBACK 配置项接口才可见
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待设置的 SPI 总线编号 | - |
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
- 当前实现未对参数进行硬件操作，直接返回成功

**前置条件**

- 调用时序约束：必须在 [uapi_spi_init](#uapi_spi_init) 成功返回后调用
- 依赖关系：需开启 CONFIG_SPI_SUPPORT_CRC 配置项接口才可见
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | spi_bus_t | 指定待设置的 SPI 总线编号 | - |
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
- 依赖关系：需开启 CONFIG_SPI_SUPPORT_LPM 配置项接口才可见；arg 作为总线编号使用，必须小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM)
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
- 依赖关系：需开启 CONFIG_SPI_SUPPORT_LPM 配置项接口才可见；arg 作为总线编号使用，必须小于 [SPI_BUS_MAX_NUM](#SPI_BUS_MAX_NUM)
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
// 源码原始定义
typedef hal_spi_attr_t spi_attr_t;
```

**使用说明**

用于 [uapi_spi_init](#uapi_spi_init)、[uapi_spi_set_attr](#uapi_spi_set_attr)、[uapi_spi_get_attr](#uapi_spi_get_attr) 的基础配置参数载体。

### spi_extra_attr_t <a id="spi_extra_attr_t"></a>

```c
// 源码原始定义
typedef hal_spi_extra_attr_t spi_extra_attr_t;
```

**使用说明**

用于 [uapi_spi_init](#uapi_spi_init)、[uapi_spi_set_extra_attr](#uapi_spi_set_extra_attr)、[uapi_spi_get_extra_attr](#uapi_spi_get_extra_attr) 的高级配置参数载体。

### spi_xfer_data_t <a id="spi_xfer_data_t"></a>

```c
// 源码原始定义
typedef hal_spi_xfer_data_t spi_xfer_data_t;
```

**使用说明**

用于主从机读写接口的数据传输结构体载体。

### spi_rx_callback_t <a id="spi_rx_callback_t"></a>

```c
// 源码原始定义
typedef void (*spi_rx_callback_t)(const void *buffer, uint32_t length, bool error);
```

**使用说明**

通过 [uapi_spi_set_irq_mode](#uapi_spi_set_irq_mode) 注册，在中断上下文中被调用。buffer 指向接收缓冲区，由读取接口的参数传入；length 为已接收的数据长度；error 表示 SPI 传输是否存在错误，包括接收上限溢出错误与接收下限溢出错误。

### spi_tx_callback_t <a id="spi_tx_callback_t"></a>

```c
// 源码原始定义
typedef void (*spi_tx_callback_t)(const void *buffer, uint32_t length);
```

**使用说明**

通过 [uapi_spi_set_irq_mode](#uapi_spi_set_irq_mode) 注册，在中断上下文中被调用。buffer 指向写入缓冲区，由写接口的参数传入；length 为已写入的数据长度。

### spi_crc_err_callback_t <a id="spi_crc_err_callback_t"></a>

```c
// 源码原始定义
typedef void (*spi_crc_err_callback_t)(spi_bus_t bus);
```

**使用说明**

通过 [uapi_spi_set_crc_mode](#uapi_spi_set_crc_mode) 注册，用于 CRC 校验错误时的回调通知，参数 bus 为发生错误的 SPI 总线编号。

## Structures

### spi_dma_config_t <a id="spi_dma_config_t"></a>

```c
// 源码原始定义
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
// 源码原始定义
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

## Enumerations

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

## Macros

### SPI_BUS_MAX_NUM <a id="SPI_BUS_MAX_NUM"></a> [SDK公共共享宏]

```c
#define SPI_BUS_MAX_NUM SPI_BUS_MAX_NUMBER
```

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a> [SDK公共共享宏]

```c
#define ERRCODE_SUCC                                        0UL
```

### ERRCODE_INVALID_PARAM <a id="ERRCODE_INVALID_PARAM"></a> [SDK公共共享宏]

```c
#define ERRCODE_INVALID_PARAM                               0x80000001
```

### ERRCODE_FAIL <a id="ERRCODE_FAIL"></a> [SDK公共共享宏]

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
