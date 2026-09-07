# I2C

I2C（Inter-Integrated Circuit）提供集成电路间串行总线的初始化、去初始化、波特率配置与主从机数据收发能力，支持轮询、中断和 DMA（Direct Memory Access）三种传输模式以及低功耗挂起/恢复。来源 `include/driver/i2c.h`。

**模块公共头文件**

```c
#include "include/driver/i2c.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_i2c_master_init](#uapi_i2c_master_init) | 按指定参数将该 I2C 初始化为主机 |
| [uapi_i2c_master_write](#uapi_i2c_master_write) | 主机向目标从机写入数据 |
| [uapi_i2c_master_read](#uapi_i2c_master_read) | 主机从目标从机读取数据 |
| [uapi_i2c_master_writeread](#uapi_i2c_master_writeread) | 主机向从机写入数据后再从该从机读取数据 |
| [uapi_i2c_slave_init](#uapi_i2c_slave_init) | 按指定参数将该 I2C 初始化为从机 |
| [uapi_i2c_slave_write](#uapi_i2c_slave_write) | 从机向主机写入数据 |
| [uapi_i2c_slave_read](#uapi_i2c_slave_read) | 从机从主机读取数据 |
| [uapi_i2c_set_irq_mode](#uapi_i2c_set_irq_mode) | 设置是否使用中断模式传输数据 |
| [uapi_i2c_register_irq_callback](#uapi_i2c_register_irq_callback) | 注册 I2C 中断事件回调函数 |
| [uapi_i2c_unregister_irq_callback](#uapi_i2c_unregister_irq_callback) | 取消注册 I2C 中断事件回调函数 |
| [uapi_i2c_set_dma_mode](#uapi_i2c_set_dma_mode) | 使能或去使能 DMA 模式的数据传输 |
| [uapi_i2c_deinit](#uapi_i2c_deinit) | 去初始化 I2C，支持主从机 |
| [uapi_i2c_set_baudrate](#uapi_i2c_set_baudrate) | 对已初始化的 I2C 重置波特率，支持主从机 |
| [uapi_i2c_suspend](#uapi_i2c_suspend) | 挂起所有 I2C 通道 |
| [uapi_i2c_resume](#uapi_i2c_resume) | 恢复所有 I2C 通道 |

## Functions

### uapi_i2c_master_init <a id="uapi_i2c_master_init"></a>

```c
errcode_t uapi_i2c_master_init(i2c_bus_t bus, uint32_t baudrate, uint8_t hscode)
```

**声明头文件**

```c
#include "include/driver/i2c.h"
```

**功能说明**

- 按指定参数将所选 I2C 总线初始化为主机模式。
- 配置 I2C 波特率与高速模式主机码。
- 成功初始化后总线即可进行主机数据收发。

**前置条件**

- 调用时序约束：调用本模块数据收发接口之前必须先成功调用本接口。
- 依赖关系：对应 I2C 总线时钟与引脚复用已就绪。
- 上下文限制：需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [i2c_bus_t](#i2c_bus_t) | 待初始化的 I2C 总线编号 | [i2c_bus_t](#i2c_bus_t) 全体成员 |
| baudrate | uint32_t | I2C 波特率，受 IP 上限约束 | 1 ~ [I2C_HS_MODE_BAUDRATE_HIGH_LIMIT](#I2C_HS_MODE_BAUDRATE_HIGH_LIMIT)：3400000（实现拒绝 baudrate 为 0） |
| hscode | uint8_t | 高速模式主机码，每个主机有唯一主机码，仅在高速模式下需配置 | 0 ~ [I2C_HS_MODE_MASTER_CODE_MAX](#I2C_HS_MODE_MASTER_CODE_MAX)：7 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 参数合法，成功初始化 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2C_SUPPORT_MASTER | 特性宏 | 支持 I2C 主机功能（接口级，包裹主机接口声明与实现） | y |
| CONFIG_I2C_SUPPORT_LPM | 特性宏 | 支持低功耗挂起状态记录特性（分支级） | n |
| CONFIG_I2C_SUPPORT_LPC | 特性宏 | 支持低功耗控制（电源与时钟）特性（分支级） | n |
| CONFIG_I2C_SUPPORT_INT | 特性宏 | 支持中断模式初始化特性（分支级） | n |

**参考案例**

- `src/application/samples/peripheral/i2c/i2c_master_demo.c`

### uapi_i2c_master_write <a id="uapi_i2c_master_write"></a>

```c
errcode_t uapi_i2c_master_write(i2c_bus_t bus, uint16_t dev_addr, i2c_data_t *data)
```

**声明头文件**

```c
#include "include/driver/i2c.h"
```

**功能说明**

- 主机向目标从机地址写入数据。
- 依据配置的传输模式（轮询/中断/DMA）执行发送。
- 支持手动切换模式与按阈值自动切换轮询和 DMA 的模式。

**前置条件**

- 调用时序约束：必须在 [uapi_i2c_master_init](#uapi_i2c_master_init) 成功返回后调用。
- 依赖关系：目标从机地址可达，发送缓冲区已准备好待发送数据。
- 上下文限制：需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [i2c_bus_t](#i2c_bus_t) | 待执行写操作的 I2C 总线编号 | [i2c_bus_t](#i2c_bus_t) 全体成员 |
| dev_addr | uint16_t | 主机发送数据的目标从机地址 | 0 ~ 0x7F（7 位从机地址；实现未做额外边界校验） |
| data | [i2c_data_t](#struct_i2c_data_t) * | 发送数据的信息指针，包含发送缓冲区及长度 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 成功发送 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2C_SUPPORT_MASTER | 特性宏 | 支持 I2C 主机功能（接口级，包裹主机接口声明与实现） | y |
| CONFIG_I2C_SUPPORT_DMA | 特性宏 | 支持 DMA 模式发送特性（分支级） | n |
| CONFIG_I2C_SUPPORT_INT | 特性宏 | 支持中断模式发送特性（分支级） | n |
| CONFIG_I2C_SUPPORT_POLL_AND_DMA_AUTO_SWITCH | 特性宏 | 支持轮询与 DMA 自动切换特性（分支级） | n |

**参考案例**

- `src/application/samples/peripheral/i2c/i2c_master_demo.c`

### uapi_i2c_master_read <a id="uapi_i2c_master_read"></a>

```c
errcode_t uapi_i2c_master_read(i2c_bus_t bus, uint16_t dev_addr, i2c_data_t *data)
```

**声明头文件**

```c
#include "include/driver/i2c.h"
```

**功能说明**

- 主机从目标从机地址读取数据。
- 依据配置的传输模式（轮询/中断/DMA）执行接收。
- 支持手动切换模式与按阈值自动切换轮询和 DMA 的模式。

**前置条件**

- 调用时序约束：必须在 [uapi_i2c_master_init](#uapi_i2c_master_init) 成功返回后调用。
- 依赖关系：目标从机地址可达，接收缓冲区已分配且长度满足接收需求。
- 上下文限制：需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [i2c_bus_t](#i2c_bus_t) | 待执行读操作的 I2C 总线编号 | [i2c_bus_t](#i2c_bus_t) 全体成员 |
| dev_addr | uint16_t | 主机接收数据的目标从机地址 | 0 ~ 0x7F（7 位从机地址；实现未做额外边界校验） |
| data | [i2c_data_t](#struct_i2c_data_t) * | 接收数据的信息指针，包含接收缓冲区及长度 | 不为 NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| data | [i2c_data_t](#struct_i2c_data_t) * | 接收到的数据由函数写入其 receive_buf 成员指向的缓冲区 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 成功接收 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2C_SUPPORT_MASTER | 特性宏 | 支持 I2C 主机功能（接口级，包裹主机接口声明与实现） | y |
| CONFIG_I2C_SUPPORT_DMA | 特性宏 | 支持 DMA 模式接收特性（分支级） | n |
| CONFIG_I2C_SUPPORT_INT | 特性宏 | 支持中断模式接收特性（分支级） | n |
| CONFIG_I2C_SUPPORT_POLL_AND_DMA_AUTO_SWITCH | 特性宏 | 支持轮询与 DMA 自动切换特性（分支级） | n |

**参考案例**

- `src/application/samples/peripheral/i2c/i2c_master_demo.c`

### uapi_i2c_master_writeread <a id="uapi_i2c_master_writeread"></a>

```c
errcode_t uapi_i2c_master_writeread(i2c_bus_t bus, uint16_t dev_addr, i2c_data_t *data)
```

**声明头文件**

```c
#include "include/driver/i2c.h"
```

**功能说明**

- 主机向目标从机写入数据后再从该从机读取数据。
- 写入与读取复用同一 [i2c_data_t](#struct_i2c_data_t) 数据结构承载。
- 依据配置的传输模式（轮询/中断/DMA）执行发送与接收。

**前置条件**

- 调用时序约束：必须在 [uapi_i2c_master_init](#uapi_i2c_master_init) 成功返回后调用。
- 依赖关系：目标从机地址可达，发送缓冲区与接收缓冲区均已准备好。
- 上下文限制：需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [i2c_bus_t](#i2c_bus_t) | 待执行写读操作的 I2C 总线编号 | [i2c_bus_t](#i2c_bus_t) 全体成员 |
| dev_addr | uint16_t | 主机写读数据的目标从机地址 | 0 ~ 0x7F（7 位从机地址；实现未做额外边界校验） |
| data | [i2c_data_t](#struct_i2c_data_t) * | 收发数据的信息指针，同时包含发送缓冲区与接收缓冲区 | 不为 NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| data | [i2c_data_t](#struct_i2c_data_t) * | 读取阶段的数据由函数写入其 receive_buf 成员指向的缓冲区 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 写读成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2C_SUPPORT_MASTER | 特性宏 | 支持 I2C 主机功能（接口级，包裹主机接口声明与实现） | y |
| CONFIG_I2C_SUPPORT_DMA | 特性宏 | 支持 DMA 模式收发特性（分支级） | n |
| CONFIG_I2C_SUPPORT_INT | 特性宏 | 支持中断模式收发特性（分支级） | n |

**参考案例**

- `src/application/samples/peripheral/i2c/i2c_master_demo.c`

### uapi_i2c_slave_init <a id="uapi_i2c_slave_init"></a>

```c
errcode_t uapi_i2c_slave_init(i2c_bus_t bus, uint32_t baudrate, uint16_t addr)
```

**声明头文件**

```c
#include "include/driver/i2c.h"
```

**功能说明**

- 按指定参数将所选 I2C 总线初始化为从机模式。
- 配置 I2C 波特率与从机地址。
- 成功初始化后总线即可进行从机数据收发。

**前置条件**

- 调用时序约束：调用从机数据收发接口之前必须先成功调用本接口。
- 依赖关系：对应 I2C 总线时钟与引脚复用已就绪，波特率需与主机保持一致。
- 上下文限制：需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [i2c_bus_t](#i2c_bus_t) | 待初始化的 I2C 总线编号 | [i2c_bus_t](#i2c_bus_t) 全体成员 |
| baudrate | uint32_t | I2C 波特率，需与主机保持一致，受 IP 上限约束 | 1 ~ [I2C_HS_MODE_BAUDRATE_HIGH_LIMIT](#I2C_HS_MODE_BAUDRATE_HIGH_LIMIT)：3400000（实现拒绝 baudrate 为 0） |
| addr | uint16_t | I2C 作为从机工作时的从机地址 | 7 比特地址 [8, 0x77]；<br>10 比特地址 [0x7800, 0x7BFF]。 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 参数合法，成功初始化 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2C_SUPPORT_SLAVE | 特性宏 | 支持 I2C 从机功能（接口级，包裹从机接口声明与实现） | y |
| CONFIG_I2C_SUPPORT_LPM | 特性宏 | 支持低功耗挂起状态记录特性（分支级） | n |
| CONFIG_I2C_SUPPORT_LPC | 特性宏 | 支持低功耗控制（电源与时钟）特性（分支级） | n |
| CONFIG_I2C_SUPPORT_INT | 特性宏 | 支持中断模式初始化特性（分支级） | n |

**参考案例**

- `src/application/samples/peripheral/i2c/i2c_slave_demo.c`

### uapi_i2c_slave_write <a id="uapi_i2c_slave_write"></a>

```c
errcode_t uapi_i2c_slave_write(i2c_bus_t bus, i2c_data_t *data)
```

**声明头文件**

```c
#include "include/driver/i2c.h"
```

**功能说明**

- 从机向主机写入数据。
- 依据配置的传输模式（轮询/中断/DMA）执行发送。
- 支持手动切换模式与按阈值自动切换轮询和 DMA 的模式。

**前置条件**

- 调用时序约束：必须在 [uapi_i2c_slave_init](#uapi_i2c_slave_init) 成功返回后调用。
- 依赖关系：主机已发起读取请求，发送缓冲区已准备好待发送数据。
- 上下文限制：需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [i2c_bus_t](#i2c_bus_t) | 待执行写操作的 I2C 总线编号 | [i2c_bus_t](#i2c_bus_t) 全体成员 |
| data | [i2c_data_t](#struct_i2c_data_t) * | 发送数据的信息指针，包含发送缓冲区及长度 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 成功发送 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2C_SUPPORT_SLAVE | 特性宏 | 支持 I2C 从机功能（接口级，包裹从机接口声明与实现） | y |
| CONFIG_I2C_SUPPORT_DMA | 特性宏 | 支持 DMA 模式发送特性（分支级） | n |
| CONFIG_I2C_SUPPORT_INT | 特性宏 | 支持中断模式发送特性（分支级） | n |
| CONFIG_I2C_SUPPORT_POLL_AND_DMA_AUTO_SWITCH | 特性宏 | 支持轮询与 DMA 自动切换特性（分支级） | n |

**参考案例**

- `src/application/samples/peripheral/i2c/i2c_slave_demo.c`

### uapi_i2c_slave_read <a id="uapi_i2c_slave_read"></a>

```c
errcode_t uapi_i2c_slave_read(i2c_bus_t bus, i2c_data_t *data)
```

**声明头文件**

```c
#include "include/driver/i2c.h"
```

**功能说明**

- 从机从主机读取数据。
- 依据配置的传输模式（轮询/中断/DMA）执行接收。
- 支持手动切换模式与按阈值自动切换轮询和 DMA 的模式。

**前置条件**

- 调用时序约束：必须在 [uapi_i2c_slave_init](#uapi_i2c_slave_init) 成功返回后调用。
- 依赖关系：主机已发起写入操作，接收缓冲区已分配且长度满足接收需求。
- 上下文限制：需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [i2c_bus_t](#i2c_bus_t) | 待执行读操作的 I2C 总线编号 | [i2c_bus_t](#i2c_bus_t) 全体成员 |
| data | [i2c_data_t](#struct_i2c_data_t) * | 接收数据的信息指针，包含接收缓冲区及长度 | 不为 NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| data | [i2c_data_t](#struct_i2c_data_t) * | 接收到的数据由函数写入其 receive_buf 成员指向的缓冲区 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 成功接收 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2C_SUPPORT_SLAVE | 特性宏 | 支持 I2C 从机功能（接口级，包裹从机接口声明与实现） | y |
| CONFIG_I2C_SUPPORT_DMA | 特性宏 | 支持 DMA 模式接收特性（分支级） | n |
| CONFIG_I2C_SUPPORT_INT | 特性宏 | 支持中断模式接收特性（分支级） | n |
| CONFIG_I2C_SUPPORT_POLL_AND_DMA_AUTO_SWITCH | 特性宏 | 支持轮询与 DMA 自动切换特性（分支级） | n |

**参考案例**

- `src/application/samples/peripheral/i2c/i2c_slave_demo.c`

### uapi_i2c_set_irq_mode <a id="uapi_i2c_set_irq_mode"></a>

```c
errcode_t uapi_i2c_set_irq_mode(i2c_bus_t bus, bool irq_en)
```

**声明头文件**

```c
#include "include/driver/i2c.h"
```

**功能说明**

- 设置是否使用中断模式传输数据。
- 使能时将数据操作类型置为中断模式，去使能时恢复为轮询模式。
- 仅控制后续数据收发的传输模式选择。

**前置条件**

- 调用时序约束：必须在 [uapi_i2c_master_init](#uapi_i2c_master_init) 或 [uapi_i2c_slave_init](#uapi_i2c_slave_init) 成功返回后调用。
- 依赖关系：对应 I2C 总线中断已注册且中断资源可用。
- 上下文限制：需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [i2c_bus_t](#i2c_bus_t) | 待配置的 I2C 总线编号 | [i2c_bus_t](#i2c_bus_t) 全体成员 |
| irq_en | bool | 是否使用中断模式传输数据 | true；<br>false。 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 参数合法，模式设置成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2C_SUPPORT_INT | 特性宏 | 支持 I2C 中断模式传输功能（接口级，包裹接口声明与实现） | n |

**参考案例**

- `src/application/samples/peripheral/i2c/i2c_master_demo.c`
- `src/application/samples/peripheral/i2c/i2c_slave_demo.c`

### uapi_i2c_register_irq_callback <a id="uapi_i2c_register_irq_callback"></a>

```c
errcode_t uapi_i2c_register_irq_callback(i2c_bus_t bus, i2c_irq_callback_t callback)
```

**声明头文件**

```c
#include "include/driver/i2c.h"
```

**功能说明**

- 注册 I2C 中断事件回调函数。
- 注册的回调在中断上下文中被调用，用于通知 I2C 中断事件。
- 同一总线上仅保留最后一次注册的回调。

**前置条件**

- 调用时序约束：必须在 [uapi_i2c_master_init](#uapi_i2c_master_init) 或 [uapi_i2c_slave_init](#uapi_i2c_slave_init) 成功返回后调用。
- 依赖关系：对应 I2C 总线中断已使能。
- 上下文限制：需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [i2c_bus_t](#i2c_bus_t) | 待注册回调的 I2C 总线编号 | [i2c_bus_t](#i2c_bus_t) 全体成员 |
| callback | [i2c_irq_callback_t](#typedef_i2c_irq_callback_t) | I2C 中断事件回调函数指针，回调在中断上下文中执行 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 回调注册成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2C_SUPPORT_INT | 特性宏 | 支持 I2C 中断模式传输功能（接口级，包裹接口声明与实现） | n |

### uapi_i2c_unregister_irq_callback <a id="uapi_i2c_unregister_irq_callback"></a>

```c
errcode_t uapi_i2c_unregister_irq_callback(i2c_bus_t bus)
```

**声明头文件**

```c
#include "include/driver/i2c.h"
```

**功能说明**

- 取消注册 I2C 中断事件回调函数。
- 取消后该总线不再触发用户中断事件回调。
- 仅清除已注册的回调指针，不影响总线本身的初始化状态。

**前置条件**

- 调用时序约束：必须已通过 [uapi_i2c_register_irq_callback](#uapi_i2c_register_irq_callback) 注册过回调。
- 依赖关系：对应 I2C 总线已初始化。
- 上下文限制：需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [i2c_bus_t](#i2c_bus_t) | 待取消注册回调的 I2C 总线编号 | [i2c_bus_t](#i2c_bus_t) 全体成员 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 回调取消注册成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2C_SUPPORT_INT | 特性宏 | 支持 I2C 中断模式传输功能（接口级，包裹接口声明与实现） | n |

### uapi_i2c_set_dma_mode <a id="uapi_i2c_set_dma_mode"></a>

```c
errcode_t uapi_i2c_set_dma_mode(i2c_bus_t bus, bool en)
```

**声明头文件**

```c
#include "include/driver/i2c.h"
```

**功能说明**

- 使能或去使能 I2C 在 DMA 模式下传输数据。
- 使能时将数据操作类型置为 DMA 模式，去使能时恢复为轮询模式。
- 仅控制后续数据收发的传输模式选择。

**前置条件**

- 调用时序约束：必须在 [uapi_i2c_master_init](#uapi_i2c_master_init) 或 [uapi_i2c_slave_init](#uapi_i2c_slave_init) 成功返回后调用。
- 依赖关系：DMA 控制器已初始化且对应 I2C 的 DMA 握手通道可用。
- 上下文限制：需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [i2c_bus_t](#i2c_bus_t) | 待配置的 I2C 总线编号 | [i2c_bus_t](#i2c_bus_t) 全体成员 |
| en | bool | 是否使能 DMA 模式传输 | true；<br>false。 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 参数合法，模式设置成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2C_SUPPORT_DMA | 特性宏 | 支持 I2C DMA 模式传输功能（接口级，包裹接口声明与实现） | n |

**参考案例**

- `src/application/samples/peripheral/i2c/i2c_master_demo.c`
- `src/application/samples/peripheral/i2c/i2c_slave_demo.c`

### uapi_i2c_deinit <a id="uapi_i2c_deinit"></a>

```c
errcode_t uapi_i2c_deinit(i2c_bus_t bus)
```

**声明头文件**

```c
#include "include/driver/i2c.h"
```

**功能说明**

- 去初始化指定 I2C 总线，对主机和从机模式均有效。
- 释放初始化阶段申请的中断、DMA 与互斥相关资源。
- 清除该总线的初始化与主机/从机标记。

**前置条件**

- 调用时序约束：必须在 [uapi_i2c_master_init](#uapi_i2c_master_init) 或 [uapi_i2c_slave_init](#uapi_i2c_slave_init) 成功返回后调用。
- 依赖关系：对应 I2C 总线无正在进行的传输任务。
- 上下文限制：需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [i2c_bus_t](#i2c_bus_t) | 待去初始化的 I2C 总线编号 | [i2c_bus_t](#i2c_bus_t) 全体成员 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 成功去初始化 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2C_SUPPORT_INT | 特性宏 | 支持中断资源去初始化分支（分支级） | n |
| CONFIG_I2C_SUPPORT_LPC | 特性宏 | 支持低功耗控制资源去初始化分支（分支级） | n |

### uapi_i2c_set_baudrate <a id="uapi_i2c_set_baudrate"></a>

```c
errcode_t uapi_i2c_set_baudrate(i2c_bus_t bus, uint32_t baudrate)
```

**声明头文件**

```c
#include "include/driver/i2c.h"
```

**功能说明**

- 对已初始化的 I2C 重新配置波特率，对主机和从机模式均有效。
- 依据总线当前是主机还是从机模式分别重新初始化底层控制器。
- 重新配置的波特率受 IP 上限约束。

**前置条件**

- 调用时序约束：必须在 [uapi_i2c_master_init](#uapi_i2c_master_init) 或 [uapi_i2c_slave_init](#uapi_i2c_slave_init) 成功返回后调用。
- 依赖关系：对应 I2C 总线无正在进行的传输任务。
- 上下文限制：需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| bus | [i2c_bus_t](#i2c_bus_t) | 待重置波特率的 I2C 总线编号 | [i2c_bus_t](#i2c_bus_t) 全体成员 |
| baudrate | uint32_t | 重置后的 I2C 波特率，受 IP 上限约束 | 1 ~ [I2C_HS_MODE_BAUDRATE_HIGH_LIMIT](#I2C_HS_MODE_BAUDRATE_HIGH_LIMIT)：3400000（实现拒绝 baudrate 为 0） |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 参数合法，波特率重置成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2C_SUPPORT_LPM | 特性宏 | 支持低功耗挂起状态下的波特率重置分支（分支级） | n |

### uapi_i2c_suspend <a id="uapi_i2c_suspend"></a>

```c
errcode_t uapi_i2c_suspend(uintptr_t arg)
```

**声明头文件**

```c
#include "include/driver/i2c.h"
```

**功能说明**

- 挂起所有已初始化的 I2C 通道。
- 标记各 I2C 通道的挂起状态供恢复使用。
- 调用后各通道处于挂起状态，可经 [uapi_i2c_resume](#uapi_i2c_resume) 恢复。

**前置条件**

- 调用时序约束：必须在系统进入低功耗流程时调用。
- 依赖关系：需对应 I2C 通道已完成初始化。
- 上下文限制：需在主线程或低功耗管理流程中调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| arg | uintptr_t | 挂起操作所需参数 | 由调用方传入 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 挂起成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2C_SUPPORT_LPM | 特性宏 | 支持 I2C 低功耗挂起与恢复功能（接口级，包裹接口声明与实现） | n |

**参考案例**

- `src/middleware/chips/ws53/pm/pm_sleep/pm_sleep_porting.c`

### uapi_i2c_resume <a id="uapi_i2c_resume"></a>

```c
errcode_t uapi_i2c_resume(uintptr_t arg)
```

**声明头文件**

```c
#include "include/driver/i2c.h"
```

**功能说明**

- 恢复所有处于挂起状态的 I2C 通道。
- 依据各通道挂起前的主机或从机模式重新初始化底层控制器。
- 恢复完成后清除挂起标志。

**前置条件**

- 调用时序约束：必须在 [uapi_i2c_suspend](#uapi_i2c_suspend) 已执行后调用。
- 依赖关系：需对应 I2C 通道挂起前已完成初始化。
- 上下文限制：需在主线程或低功耗管理流程中调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| arg | uintptr_t | 恢复操作所需参数 | 由调用方传入 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 恢复成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_I2C_SUPPORT_LPM | 特性宏 | 支持 I2C 低功耗挂起与恢复功能（接口级，包裹接口声明与实现） | n |
| CONFIG_I2C_SUPPORT_MASTER | 特性宏 | 支持主机模式恢复分支（分支级） | y |
| CONFIG_I2C_SUPPORT_SLAVE | 特性宏 | 支持从机模式恢复分支（分支级） | y |

**参考案例**

- `src/middleware/chips/ws53/pm/pm_sleep/pm_sleep_porting.c`

## Type definitions

### typedef_errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块全部对外接口的返回值类型，承载 I2C 操作结果错误码。

### typedef_i2c_irq_callback_t <a id="typedef_i2c_irq_callback_t"></a>

```c
// i2c irq event callback to be called when irq callback set
// @ref uapi_i2c_register_irq_callback is invoked.
// This callback is invoked in an interrupt context.
typedef void (*i2c_irq_callback_t)(i2c_bus_t bus, uint8_t event);
```

**使用说明**

- 用于 [uapi_i2c_register_irq_callback](#uapi_i2c_register_irq_callback) 的入参，作为 I2C 中断事件回调函数指针类型。
- 回调在中断上下文中被调用。
- 参数 `bus` 为触发中断的 I2C 总线编号。
- 参数 `event` 为 I2C 中断事件，取值对应 i2c_irq_event_t 枚举成员（接收完成、发送完成、总线忙、错误等）。
- 回调返回类型为 void，无返回值。

## Enumerations

### enum i2c_bus_t <a id="i2c_bus_t"></a>

```c
typedef enum {
    I2C_BUS_0,               // !< I2C0
    I2C_BUS_1,               // !< I2C1
    I2C_BUS_NONE = I2C_BUS_MAX_NUMBER
} i2c_bus_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| I2C_BUS_0 | 0 | I2C 总线 0 |
| I2C_BUS_1 | 1 | I2C 总线 1 |
| I2C_BUS_NONE | 2 | 无效/未指定的 I2C 总线编号（等同 I2C_BUS_MAX_NUMBER） |

## Structures

### struct_i2c_data_t <a id="struct_i2c_data_t"></a>

```c
// Definition of I2C TX/RX data.
typedef struct i2c_data {
    uint8_t *send_buf;              /*!< Send buffer pointer. */
    uint32_t send_len;              /*!< Send buffer len. */
    uint8_t *receive_buf;           /*!< Receive buffer pointer. */
    uint32_t receive_len;           /*!< Receive buffer len. */
} i2c_data_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| send_buf | uint8_t * | 发送数据的 buffer 指针 |
| send_len | uint32_t | 发送数据的 buffer 长度 |
| receive_buf | uint8_t * | 接收数据的 buffer 指针 |
| receive_len | uint32_t | 接收数据的 buffer 长度 |

## Macros

### I2C_HS_MODE_BAUDRATE_HIGH_LIMIT <a id="I2C_HS_MODE_BAUDRATE_HIGH_LIMIT"></a>

```c
#define I2C_HS_MODE_BAUDRATE_HIGH_LIMIT  (3400 * 1000)   /*!< I2C baudrate high limit in high speed mode. */
```

### I2C_HS_MODE_MASTER_CODE_MAX <a id="I2C_HS_MODE_MASTER_CODE_MAX"></a>

```c
#define I2C_HS_MODE_MASTER_CODE_MAX  7   /*!< I2C max master code in high speed mode. */
```
