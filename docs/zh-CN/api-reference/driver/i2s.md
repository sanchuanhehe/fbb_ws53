# I2S

I2S（Inter-IC Sound）提供集成电路间数字音频总线的数据收发能力，支持主从模式、多种数据位宽与通道数的配置，可工作在轮询、中断以及 DMA（Direct Memory Access）传输模式下。本模块对外接口以 SIO（Serial Input/Output）总线编号为索引对硬件 I2S 控制器进行操作。

**模块公共头文件**

```c
#include "include/driver/i2s.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_i2s_init](#uapi_i2s_init) | 初始化指定 SIO 总线上的 I2S 设备并注册接收回调 |
| [uapi_i2s_deinit](#uapi_i2s_deinit) | 去初始化指定 SIO 总线上的 I2S 设备 |
| [uapi_i2s_set_config](#uapi_i2s_set_config) | 设置 I2S 设备的工作模式、位宽、通道等配置 |
| [uapi_i2s_get_config](#uapi_i2s_get_config) | 获取 I2S 设备当前的配置参数 |
| [uapi_i2s_write_data](#uapi_i2s_write_data) | 轮询模式下向 I2S 设备写入发送数据 |
| [uapi_i2s_read_start](#uapi_i2s_read_start) | 中断模式下启动 I2S 设备的数据接收 |
| [uapi_i2s_set_crg_clock_enable](#uapi_i2s_set_crg_clock_enable) | 使能或关闭 I2S 的 BCLK/WS 时钟 |
| [uapi_i2s_loop_trans](#uapi_i2s_loop_trans) | I2S 回路自测发送数据 |
| [uapi_i2s_get_data](#uapi_i2s_get_data) | 获取中断模式下 I2S 设备接收到的数据 |
| [uapi_i2s_loopback](#uapi_i2s_loopback) | 打开或关闭 I2S 回环模式 |
| [uapi_i2s_dma_config](#uapi_i2s_dma_config) | 配置 I2S 使用 DMA 传输时的参数 |
| [uapi_i2s_merge_write_by_dma](#uapi_i2s_merge_write_by_dma) | merge 模式下通过 DMA 写数据到 I2S |
| [uapi_i2s_merge_read_by_dma](#uapi_i2s_merge_read_by_dma) | merge 模式下通过 DMA 从 I2S 读数据 |

## Functions

### uapi_i2s_init <a id="uapi_i2s_init"></a>

```c
errcode_t uapi_i2s_init(sio_bus_t bus, i2s_callback_t callback)
```

**声明头文件**

```c
#include "include/driver/i2s.h"
```

**功能说明**

- 初始化指定 SIO 总线上的 I2S 设备。
- 注册应用侧的接收数据回调函数。
- 当设备已初始化时重复调用直接返回成功。

**前置条件**

- 调用时序约束：当前接口需在调用本模块其它配置/收发接口之前首先调用。
- 依赖关系：当前接口依赖目标 SIO 总线的 HAL 函数已注册且 SIO 时钟可被使能。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | sio_bus_t | 指定的 SIO 总线编号，参考 sio_bus_t | SIO_BUS_0：0 |
| callback | [i2s_callback_t](#typedef_i2s_callback_t) | I2S 设备的接收数据回调函数 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 设备初始化或设备已初始成功化 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 总线编号超出有效范围 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2S_SUPPORT_DMA | 特性宏 | 支持 DMA 模式下初始化收发信号量（分支级） | n |

**参考案例**

- `src/application/samples/peripheral/i2s/i2s_master_demo.c`
- `src/application/samples/peripheral/i2s/i2s_slave_demo.c`

### uapi_i2s_deinit <a id="uapi_i2s_deinit"></a>

```c
errcode_t uapi_i2s_deinit(sio_bus_t bus)
```

**声明头文件**

```c
#include "include/driver/i2s.h"
```

**功能说明**

- 去初始化指定 SIO 总线上的 I2S 设备。
- 关闭接收使能并注销接收回调。
- 当设备未初始化时重复调用直接返回成功。

**前置条件**

- 调用时序约束：当前接口应在完成全部收发操作后调用。
- 依赖关系：当前接口依赖目标 SIO 总线已通过 uapi_i2s_init 完成初始化或处于可去初始化状态。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | sio_bus_t | 指定的 SIO 总线编号，参考 sio_bus_t | SIO_BUS_0：0 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 成功去初始化或设备未初始化 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 总线编号超出有效范围 |

### uapi_i2s_set_config <a id="uapi_i2s_set_config"></a>

```c
errcode_t uapi_i2s_set_config(sio_bus_t bus, const i2s_config_t *config)
```

**声明头文件**

```c
#include "include/driver/i2s.h"
```

**功能说明**

- 设置 I2S 设备的主从模式、传输路径模式、数据位宽、通道数、时序模式、时钟边沿、分频系数等配置。
- 按入参配置 SIO 传输参数。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_i2s_init 成功返回后调用。
- 依赖关系：当前接口依赖目标 SIO 总线 HAL 的配置接口已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | sio_bus_t | 指定的 SIO 总线编号，参考 sio_bus_t | SIO_BUS_0：0 |
| config | [i2s_config_t](#struct_i2s_config_t) * | I2S 设备的配置参数指针 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 配置下发成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 设备未初始化、总线编号超出有效范围或 config 为 NULL |

**参考案例**

- `src/application/samples/peripheral/i2s/i2s_master_demo.c`
- `src/application/samples/peripheral/i2s/i2s_slave_demo.c`

### uapi_i2s_get_config <a id="uapi_i2s_get_config"></a>

```c
errcode_t uapi_i2s_get_config(sio_bus_t bus, i2s_config_t *config)
```

**声明头文件**

```c
#include "include/driver/i2s.h"
```

**功能说明**

- 获取 I2S 设备当前的工作模式、传输路径模式、数据位宽、通道数、时序模式、时钟边沿、分频系数等配置。
- 通过出参 config 返回当前配置内容。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_i2s_init 成功返回后调用。
- 依赖关系：当前接口依赖目标 SIO 总线 HAL 的配置获取接口已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | sio_bus_t | 指定的 SIO 总线编号，参考 sio_bus_t | SIO_BUS_0：0 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| config | [i2s_config_t](#struct_i2s_config_t) * | 由调用方分配内存，接口填充当前 I2S 设备配置 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 成功配置获取 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 设备未初始化、总线编号超出有效范围或 config 为 NULL |

### uapi_i2s_write_data <a id="uapi_i2s_write_data"></a>

```c
errcode_t uapi_i2s_write_data(sio_bus_t bus, i2s_tx_data_t *data)
```

**声明头文件**

```c
#include "include/driver/i2s.h"
```

**功能说明**

- 在轮询模式下向 I2S 设备写入左右声道发送数据。
- 数据通过发送结构体的左右声道缓冲区与长度指定。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_i2s_init 与 uapi_i2s_set_config 成功返回后调用。
- 依赖关系：当前接口依赖目标 SIO 总线 HAL 的写接口已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | sio_bus_t | 指定的 SIO 总线编号，参考 sio_bus_t | SIO_BUS_0：0 |
| data | [i2s_tx_data_t](#struct_i2s_tx_data_t) * | 发送数据指针，含左右声道缓冲区与长度 | 不为 NULL；data->left_buff 与 data->right_buff 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 数据写入成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 设备未初始化、总线编号超出有效范围或 data 及其缓冲区为 NULL |

**参考案例**

- `src/application/samples/peripheral/i2s/i2s_master_demo.c`

### uapi_i2s_read_start <a id="uapi_i2s_read_start"></a>

```c
errcode_t uapi_i2s_read_start(sio_bus_t bus)
```

**声明头文件**

```c
#include "include/driver/i2s.h"
```

**功能说明**

- 在中断模式下启动 I2S 设备的数据接收。
- 当设备配置为主模式时同时打开 CRG（Clock Reset Generator）时钟。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_i2s_init 与 uapi_i2s_set_config 成功返回后调用。
- 依赖关系：当前接口依赖目标 SIO 总线 HAL 的接收使能接口已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | sio_bus_t | 指定的 SIO 总线编号，参考 sio_bus_t | SIO_BUS_0：0 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 成功接收启动 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 设备未初始化或总线编号超出有效范围 |

**参考案例**

- `src/application/samples/peripheral/i2s/i2s_slave_demo.c`

### uapi_i2s_set_crg_clock_enable <a id="uapi_i2s_set_crg_clock_enable"></a>

```c
void uapi_i2s_set_crg_clock_enable(sio_bus_t bus, bool enable)
```

**声明头文件**

```c
#include "include/driver/i2s.h"
```

**功能说明**

- 打开或关闭 I2S 的位时钟 BCLK 与采样时钟 WS。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_i2s_init 成功返回后调用。
- 依赖关系：当前接口依赖目标 SIO 总线 CRG 时钟使能接口已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | sio_bus_t | 指定的 SIO 总线编号，参考 sio_bus_t | SIO_BUS_0：0 |
| enable | bool | 打开或关闭 BCLK/WS 时钟 | - true<br>- false |

### uapi_i2s_loop_trans <a id="uapi_i2s_loop_trans"></a>

```c
errcode_t uapi_i2s_loop_trans(sio_bus_t bus, i2s_tx_data_t *data)
```

**声明头文件**

```c
#include "include/driver/i2s.h"
```

**功能说明**

- 在 I2S 回路上进行自测数据发送。
- 数据通过发送结构体的左右声道缓冲区与长度指定。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_i2s_init 与 uapi_i2s_set_config 成功返回后调用。
- 依赖关系：当前接口依赖目标 SIO 总线 HAL 的回路自测接口已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | sio_bus_t | 指定的 SIO 总线编号，参考 sio_bus_t | SIO_BUS_0：0 |
| data | [i2s_tx_data_t](#struct_i2s_tx_data_t) * | 自测发送数据指针，含左右声道缓冲区与长度 | 不为 NULL；data->left_buff 与 data->right_buff 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 回路自测发送成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 设备未初始化、总线编号超出有效范围或 data 及其缓冲区为 NULL |

### uapi_i2s_get_data <a id="uapi_i2s_get_data"></a>

```c
errcode_t uapi_i2s_get_data(sio_bus_t bus, i2s_rx_data_t *data)
```

**声明头文件**

```c
#include "include/driver/i2s.h"
```

**功能说明**

- 获取中断模式下 I2S 设备已接收的数据。
- 通过出参 data 返回左右声道接收数据与数据长度。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_i2s_init 与 uapi_i2s_read_start 成功返回后调用。
- 依赖关系：当前接口依赖目标 SIO 总线 HAL 的数据获取接口已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | sio_bus_t | 指定的 SIO 总线编号，参考 sio_bus_t | SIO_BUS_0：0 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| data | [i2s_rx_data_t](#struct_i2s_rx_data_t) * | 由调用方分配内存，接口填充左右声道接收数据及数据长度 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 数据获取成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 设备未初始化、总线编号超出有效范围或 data 为 NULL |

### uapi_i2s_loopback <a id="uapi_i2s_loopback"></a>

```c
errcode_t uapi_i2s_loopback(sio_bus_t bus, bool en)
```

**声明头文件**

```c
#include "include/driver/i2s.h"
```

**功能说明**

- 打开或关闭 I2S 的回环模式。
- 仅在启用 CONFIG_I2S_SUPPORT_LOOPBACK 配置时该接口对外可用。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_i2s_init 与 uapi_i2s_set_config 成功返回后调用。
- 依赖关系：当前接口依赖目标 SIO 总线 HAL 的回环接口已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | sio_bus_t | 指定的 SIO 总线编号，参考 sio_bus_t | SIO_BUS_0：0 |
| en | bool | 是否开启回环模式 | - true<br>- false |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 回环模式设置成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 设备未初始化或总线编号超出有效范围 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2S_SUPPORT_LOOPBACK | 特性宏 | 支持 I2S 回环接口功能（接口级） | y |

### uapi_i2s_dma_config <a id="uapi_i2s_dma_config"></a>

```c
int32_t uapi_i2s_dma_config(sio_bus_t bus, i2s_dma_attr_t *i2s_dma_cfg)
```

**声明头文件**

```c
#include "include/driver/i2s.h"
```

**功能说明**

- 配置 I2S 使用 DMA 传输时的参数，包括发送/接收是否使能 DMA 及其 FIFO（First In First Out）中断水线。
- 仅在启用 CONFIG_I2S_SUPPORT_DMA 配置时该接口对外可用。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_i2s_init 成功返回后调用。
- 依赖关系：当前接口依赖目标 SIO 总线 HAL 的 DMA 配置接口已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | sio_bus_t | 指定的 SIO 总线编号，参考 sio_bus_t | SIO_BUS_0：0 |
| i2s_dma_cfg | [i2s_dma_attr_t](#struct_i2s_dma_attr_t) * | I2S 使用 DMA 传输时的配置参数指针 | 不为 NULL |

**返回值**

返回类型：int32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | DMA 传输参数配置成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 设备未初始化或总线编号超出有效范围 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2S_SUPPORT_DMA | 特性宏 | 支持 I2S DMA 配置接口功能（接口级） | n |

### uapi_i2s_merge_write_by_dma <a id="uapi_i2s_merge_write_by_dma"></a>

```c
int32_t uapi_i2s_merge_write_by_dma(sio_bus_t bus, const void *buffer, uint32_t length, i2s_dma_config_t *dma_cfg, uintptr_t arg, bool block)
```

**声明头文件**

```c
#include "include/driver/i2s.h"
```

**功能说明**

- 在 merge 模式下通过 DMA 向 I2S 写入数据。
- 支持阻塞与非阻塞两种传输方式。
- 仅在启用 CONFIG_I2S_SUPPORT_DMA 配置时该接口对外可用。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_i2s_init 与 uapi_i2s_dma_config 成功返回后调用。
- 依赖关系：当前接口依赖目标 SIO 总线的 DMA 合并发送地址及 DMA 通道资源已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | sio_bus_t | 指定的 SIO 总线编号，参考 sio_bus_t | SIO_BUS_0：0 |
| buffer | const void * | 待写入的数据缓冲区指针 | 不为 NULL |
| length | uint32_t | 需要写入的数据长度 | 大于 0 |
| dma_cfg | [i2s_dma_config_t](#struct_i2s_dma_config_t) * | DMA 传输配置参数指针 | 不为 NULL |
| arg | uintptr_t | 自定义参数，可被传递到中断处理函数 | 无约束 |
| block | bool | 是否阻塞传输 | - true<br>- false |

**返回值**

返回类型：int32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 非阻塞模式发起传输成功 |
| 正整数 | 实际传输的数据块大小 | 阻塞模式传输成功，返回 DMA 实际传输的 block_ts |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 设备未初始化、总线编号超出有效范围、dma_cfg/buffer 为 NULL、length 为 0、DMA 握手号不支持、或 DMA 配置/启动失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2S_SUPPORT_DMA | 特性宏 | 支持 I2S DMA 合并写接口功能（接口级） | n |

### uapi_i2s_merge_read_by_dma <a id="uapi_i2s_merge_read_by_dma"></a>

```c
int32_t uapi_i2s_merge_read_by_dma(sio_bus_t bus, const void *buffer, uint32_t length, i2s_dma_config_t *dma_cfg, uintptr_t arg, bool block)
```

**声明头文件**

```c
#include "include/driver/i2s.h"
```

**功能说明**

- 在 merge 模式下通过 DMA 从 I2S 读取数据到指定缓冲区。
- 支持阻塞与非阻塞两种传输方式。
- 仅在启用 CONFIG_I2S_SUPPORT_DMA 配置时该接口对外可用。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_i2s_init 与 uapi_i2s_dma_config 成功返回后调用。
- 依赖关系：当前接口依赖目标 SIO 总线的 DMA 合并接收地址及 DMA 通道资源已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | sio_bus_t | 指定的 SIO 总线编号，参考 sio_bus_t | SIO_BUS_0：0 |
| buffer | const void * | 存储读取数据的缓冲区指针 | 不为 NULL |
| length | uint32_t | 需要读取的数据长度 | 大于 0 |
| dma_cfg | [i2s_dma_config_t](#struct_i2s_dma_config_t) * | DMA 传输配置参数指针 | 不为 NULL |
| arg | uintptr_t | 自定义参数，可被传递到中断处理函数 | 无约束 |
| block | bool | 是否阻塞传输 | - true<br>- false |

**返回值**

返回类型：int32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 非阻塞模式发起传输成功 |
| 正整数 | 实际传输的数据块大小 | 阻塞模式传输成功，返回 DMA 实际传输的 block_ts |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 设备未初始化、总线编号超出有效范围、dma_cfg/buffer 为 NULL、length 为 0、DMA 握手号不支持、或 DMA 配置/启动失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2S_SUPPORT_DMA | 特性宏 | 支持 I2S DMA 合并读接口功能（接口级） | n |

## Type definitions

### errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块对外接口的返回值类型，用于表示接口执行结果。

### typedef_i2s_callback_t <a id="typedef_i2s_callback_t"></a>

```c
typedef void (*i2s_callback_t)(uint32_t *left_buff, uint32_t *right_buff, uint32_t length);
```

**使用说明**

I2S 设备的接收数据回调函数类型，由 uapi_i2s_init 注册；在中断模式下设备接收到数据时被调用，传入左右声道数据缓冲区指针与数据长度。回调返回值为 void，当前实现中不对回调返回值做处理。

## Structures

### struct_i2s_rx_data_t <a id="struct_i2s_rx_data_t"></a>

```c
typedef struct i2s_rx_data {
    uint32_t left_buff[CONFIG_DATA_LEN_MAX];    /*!< @if Eng Left data.
                                                     @else   左声道数据。 @endif */
    uint32_t right_buff[CONFIG_DATA_LEN_MAX];   /*!< @if Eng Right data.
                                                     @else   右声道数据。 @endif */
    uint32_t length;                            /*!< @if Eng Data length.
                                                     @else   数据长度。 @endif */
} i2s_rx_data_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| left_buff | uint32_t[CONFIG_DATA_LEN_MAX] | 左声道接收数据缓冲区 |
| right_buff | uint32_t[CONFIG_DATA_LEN_MAX] | 右声道接收数据缓冲区 |
| length | uint32_t | 数据长度 |

### struct_i2s_tx_data_t <a id="struct_i2s_tx_data_t"></a>

```c
typedef struct i2s_tx_data {
    uint32_t *left_buff;                        /*!< @if Eng Data send through tx left FIFO.
                                                     @else   通过TX 左FIFO发送的数据。 @endif */
    uint32_t *right_buff;                       /*!< @if Eng Data send through tx right FIFO.
                                                     @else   通过TX 右FIFO发送的数据。 @endif */
    uint32_t length;                            /*!< @if Eng Bytes of data need to send.
                                                     @else   发送数据的个数。 @endif */
} i2s_tx_data_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| left_buff | uint32_t * | 通过 TX 左 FIFO 发送的数据指针 |
| right_buff | uint32_t * | 通过 TX 右 FIFO 发送的数据指针 |
| length | uint32_t | 发送数据的个数 |

### struct_i2s_config_t <a id="struct_i2s_config_t"></a>

```c
typedef struct i2s_config {
    uint8_t drive_mode;                         /*!< @if Eng I2S divice modes:
                                                 *           - 0: SLAVE
                                                 *           - 1: MASTER
                                                 *   @else   I2S 设备模式：
                                                 *           - 0: 从模式
                                                 *           - 1: 主模式
                                                 *   @endif */
    uint8_t transfer_mode;                      /*!< @if Eng I2S transmission path modes:
                                                 *           - 0: Standard mode
                                                 *           - 1: Multichannel mode
                                                 *   @else   I2S 传输路径模式：
                                                 *           - 0: 标准模式
                                                 *           - 1: 多路模式
                                                 *   @endif */
    uint8_t data_width;                         /*!< @if Eng I2S data width:
                                                 *           - 0: RESERVED
                                                 *           - 1: 16 Bits
                                                 *           - 2: 18 Bits
                                                 *           - 3: 20 Bits
                                                 *           - 4: 24 Bits
                                                 *           - 5: 32 Bits
                                                 *   @else   I2S 数据宽度：
                                                 *           - 0: 保留
                                                 *           - 1: 16位
                                                 *           - 2: 18位
                                                 *           - 3: 20位
                                                 *           - 4: 24位
                                                 *           - 5: 32位
                                                 *   @endif */
    uint8_t channels_num;                       /*!< @if Eng I2S transmission Channels Number:
                                                 *           - 0: 2 Channels
                                                 *           - 1: 4 Channels
                                                 *           - 2: 8 Channels
                                                 *           - 3: 16 Channels
                                                 *   @else   I2S 传输通道数：
                                                 *           - 0: 2通道
                                                 *           - 1: 4通道
                                                 *           - 2: 8通道
                                                 *           - 3: 16通道
                                                 *   @endif */
    uint8_t timing;                             /*!< @if Eng I2S timing mode:
                                                 *           - 0: Standard timing mode
                                                 *           - 1: User-defined timing mode
                                                 *   @else   I2S 时序模式：
                                                 *           - 0: 标准时序模式
                                                 *           - 1: 自定义时序模式
                                                 *   @endif */
    uint8_t clk_edge;                           /*!< @if Eng I2S clock edge mode:
                                                 *           - 0: Falling edge
                                                 *           - 1: Rising edge
                                                 *   @else   I2S 时钟边沿模式：
                                                 *           - 0: 下降沿
                                                 *           - 1: 上升沿
                                                 *   @endif */
    uint8_t div_number;                         /*!< @if Eng Div number, see @ref i2s_config.data_width.
                                                     @else   分频系数，见 @ref i2s_config.data_width 成员。 @endif */
    uint8_t number_of_channels;                 /*!< @if Eng Number of channels, see @ref i2s_config.channels_num.
                                                     @else   通道数，见 @ref i2s_config.channels_num 成员。 @endif */
} i2s_config_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| drive_mode | uint8_t | I2S 设备模式，取值 0 表示从模式；<br>1 表示主模式。 |
| transfer_mode | uint8_t | I2S 传输路径模式，取值 0 表示标准模式；<br>1 表示多路模式。 |
| data_width | uint8_t | I2S 数据宽度，取值 0 保留；<br>1 表示 16 位；<br>2 表示 18 位；<br>3 表示 20 位；<br>4 表示 24 位；<br>5 表示 32 位。 |
| channels_num | uint8_t | I2S 传输通道数，取值 0 表示 2 通道；<br>1 表示 4 通道；<br>2 表示 8 通道；<br>3 表示 16 通道。 |
| timing | uint8_t | I2S 时序模式，取值 0 表示标准时序模式；<br>1 表示自定义时序模式。 |
| clk_edge | uint8_t | I2S 时钟边沿模式，取值 0 表示下降沿；<br>1 表示上升沿。 |
| div_number | uint8_t | 分频系数 |
| number_of_channels | uint8_t | 通道数 |

### struct_i2s_dma_config_t <a id="struct_i2s_dma_config_t"></a>

```c
typedef struct i2s_dma_config {
    uint8_t src_width;          /*!< @if Eng Transfer data width of the source.
                                 *           - 0: 1byte
                                 *           - 1: 2byte
                                 *           - 2: 4byte
                                 *   @else   源端传输数据宽度 \n
                                 *           - 0: 1字节
                                 *           - 1: 2字节
                                 *           - 2: 4字节
                                 *   @endif */
    uint8_t dest_width;         /*!< @if Eng Transfer data width of the destination.
                                 *            - 0: 1byte
                                 *            - 1: 2byte
                                 *            - 2: 4byte
                                 *   @else   目的端传输数据宽度 \n
                                 *           - 0: 1字节
                                 *           - 1: 2字节
                                 *           - 2: 4字节
                                 *   @endif */
    uint8_t burst_length;       /*!< @if Eng Number of data items, to be written to the destination every time
                                 *           a destination burst transaction request is made from
                                 *           either the corresponding hardware or software handshaking interface.
                                 *           - 0: burst length is 1
                                 *           - 1: burst length is 4
                                 *           - 2: burst length is 8
                                 *           - 3: burst length is 16
                                 *   @else   每次从相应的硬件或软件握手接口发出目的burst请求时,要写入目的端数据量
                                 *           - 0: burst长度是1
                                 *           - 1: burst长度是4
                                 *           - 2: burst长度是8
                                 *           - 3: burst长度是16
                                 *   @endif */
    uint8_t priority;           /*!< @if Eng Transfer channel priority(Minimum: 0 and Maximum: 3).
                                 *   @else   传输通道优先级(最小为0以及最大为3)  @endif */
} i2s_dma_config_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| src_width | uint8_t | 源端传输数据宽度，取值 0 表示 1 Bytes；<br>1 表示 2 Bytes；<br>2 表示 4 Bytes。 |
| dest_width | uint8_t | 目的端传输数据宽度，取值 0 表示 1 Bytes；<br>1 表示 2 Bytes；<br>2 表示 4 Bytes。 |
| burst_length | uint8_t | 每次目的 burst 请求写入目的端的数据量，取值 0 表示 1；<br>1 表示 4；<br>2 表示 8；<br>3 表示 16。 |
| priority | uint8_t | 传输通道优先级，取值范围 0 ~ 3 |

### struct_i2s_dma_attr_t <a id="struct_i2s_dma_attr_t"></a>

```c
typedef struct i2s_dma_attr {
    bool tx_dma_enable;                     /*!< @if Eng false: tx not use dma @ref uapi_i2s_write can be used. \n
                                                     true:  tx use dma @ref uapi_i2s_write_by_dma can be used.
                                             @else   false: TX没有使用DMA，使用 @ref uapi_i2s_write 发送数据 \n
                                                     true:  TX使用DMA，使用 @ref uapi_i2s_write_by_dma 发送数据 @endif */
    uint8_t tx_int_threshold;               /*!< @if Eng i2s tx fifo level to trigger interrupt.
                                             @else 触发中断的txfifo水线 @endif */
    bool rx_dma_enable;                     /*!< @if Eng false: rx not use dma @ref uapi_i2s_write can be used. \n
                                                     true:  rx use dma @ref uapi_i2s_write_by_dma can be used.
                                             @else   false: RX没有使用DMA，使用 @ref uapi_i2s_write 发送数据 \n
                                                     true:  RX使用DMA，使用 @ref uapi_i2s_write_by_dma 发送数据 @endif */
    uint8_t rx_int_threshold;               /*!< @if Eng i2s rx fifo level to trigger interrupt.
                                             @else 触发中断的rxfifo水线 @endif */
} i2s_dma_attr_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| tx_dma_enable | bool | 发送是否使用 DMA，true 表示 TX 使用 DMA、false 表示不使用 DMA |
| tx_int_threshold | uint8_t | 触发中断的 TX FIFO 水线 |
| rx_dma_enable | bool | 接收是否使用 DMA，true 表示 RX 使用 DMA、false 表示不使用 DMA |
| rx_int_threshold | uint8_t | 触发中断的 RX FIFO 水线 |

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```
