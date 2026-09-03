# eFuse Core

eFuse（electronic Fuse）提供一次性可编程（One-Time Programmable, OTP）熔丝的读写访问能力，支持按位与按字节的数据读取和烧写，并可用于获取 Die-ID、SoC-ID（System on Chip ID）等芯片标识。本子模块为 efuse 核心接口集，来源头文件 include/driver/efuse.h。

**模块公共头文件**

```c
#include "include/driver/efuse.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_efuse_init](#uapi_efuse_init) | 初始化 eFuse 驱动 |
| [uapi_efuse_deinit](#uapi_efuse_deinit) | 去初始化 eFuse 驱动 |
| [uapi_efuse_read_bit](#uapi_efuse_read_bit) | 从 eFuse 中读取一位 |
| [uapi_efuse_read_buffer](#uapi_efuse_read_buffer) | 从 eFuse 中读取多个字节到缓冲区 |
| [uapi_efuse_write_bit](#uapi_efuse_write_bit) | 向 eFuse 写入一位 |
| [uapi_efuse_write_bit_with_flag](#uapi_efuse_write_bit_with_flag) | 在保护标志正确的情况下向 eFuse 写入一位 |
| [uapi_efuse_write_buffer](#uapi_efuse_write_buffer) | 从缓冲区向 eFuse 写入多个字节 |
| [uapi_efuse_write_buffer_with_flag](#uapi_efuse_write_buffer_with_flag) | 在保护标志正确的情况下从缓冲区向 eFuse 写入多个字节 |
| [uapi_efuse_get_die_id](#uapi_efuse_get_die_id) | 获取 eFuse 的 Die-ID |
| [uapi_efuse_calc_crc](#uapi_efuse_calc_crc) | 计算数据块的零计数 CRC（Cyclic Redundancy Check） |
| [uapi_soc_read_id](#uapi_soc_read_id) | 获取 SoC-ID |

## Functions

### uapi_efuse_init <a id="uapi_efuse_init"></a>

```c
errcode_t uapi_efuse_init(void)
```

**声明头文件**

```c
#include "include/driver/efuse.h"
```

**功能说明**

- 初始化 eFuse 驱动。
- 作为按位/按字节读写与芯片标识读取接口的初始化入口。
- 返回初始化执行结果。

**前置条件**

- 调用时序约束：在使用其它 eFuse 读写接口之前调用本接口完成驱动初始化。
- 依赖关系：当前接口依赖 eFuse HAL 函数表注册函数与底层初始化函数已就绪。

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 执行成功 | 底层初始化成功返回 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层初始化失败 |

**参考案例**

- `src/application/ws53/ws53_application/main.c`
- `src/bootloader/flashboot_ws53/startup/main.c`

### uapi_efuse_deinit <a id="uapi_efuse_deinit"></a>

```c
errcode_t uapi_efuse_deinit(void)
```

**声明头文件**

```c
#include "include/driver/efuse.h"
```

**功能说明**

- 去初始化 eFuse 驱动。
- 释放驱动占用的资源。
- 无论 eFuse 是否已初始化均返回执行成功。

**前置条件**

- 调用时序约束：当前接口应在 uapi_efuse_init 成功返回之后调用。
- 依赖关系：当前接口依赖 HAL 函数表获取函数可用。

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 执行成功 | 去初始化流程执行完成 |

### uapi_efuse_read_bit <a id="uapi_efuse_read_bit"></a>

```c
errcode_t uapi_efuse_read_bit(uint8_t *value, uint32_t byte_number, uint8_t bit_pos)
```

**声明头文件**

```c
#include "include/driver/efuse.h"
```

**功能说明**

- 从 eFuse 指定字节的指定位读取一位。
- 通过位偏移定位目标位并将结果写入输出参数。
- 读取结果取值 0 或 1。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_efuse_init 成功返回后调用。
- 依赖关系：当前接口依赖 eFuse HAL 字节读取接口已就绪。
- 上下文限制：当前接口内部会执行关中断与恢复中断操作。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| byte_number | uint32_t | 要读取位所在的目标字节地址 | 0 ~ 255 |
| bit_pos | uint8_t | 目标字节内的位位置 | 0 ~ 7 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| value | uint8_t * | 读取到的目标位值，取值 0 或 1，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 执行成功 | 字节读取成功并取位完成 |
| ERRCODE_FAIL：0xFFFFFFFF | 执行失败 | 参数非法或字节读取失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| EFUSE_BIT_OPERATION | 特性宏 | 支持按位读写功能（无前缀注入宏，接口级） | 由构建目标决定 |

**参考案例**

- `src/middleware/utils/at/at_plt_cmd/at/at_plt.c`

### uapi_efuse_read_buffer <a id="uapi_efuse_read_buffer"></a>

```c
errcode_t uapi_efuse_read_buffer(uint8_t *buffer, uint32_t byte_number, uint16_t length)
```

**声明头文件**

```c
#include "include/driver/efuse.h"
```

**功能说明**

- 从 eFuse 指定字节地址起连续读取多个字节。
- 将读取的数据写入调用方提供的缓冲区。
- 读取的字节数由入参 length 指定。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_efuse_init 成功返回后调用。
- 依赖关系：当前接口依赖 eFuse HAL 字节读取接口已就绪。
- 上下文限制：当前接口内部会执行关中断与恢复中断操作。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| byte_number | uint32_t | 读取数据的起始字节地址 | 0 ~ 255 |
| length | uint16_t | 读取数据的长度，以字节为单位 | 1 ~ 256，且 byte_number + length ≤ 256 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| buffer | uint8_t * | 从 eFuse 读取的字节序列，长度为 length，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 执行成功 | 全部字节读取成功 |
| ERRCODE_FAIL：0xFFFFFFFF | 执行失败 | 参数非法或任一字节读取失败 |

**参考案例**

- `src/middleware/chips/ws53/update/common/upg_common_porting.c`
- `src/middleware/utils/at/at_plt_cmd/at/at_plt.c`

### uapi_efuse_write_bit <a id="uapi_efuse_write_bit"></a>

```c
errcode_t uapi_efuse_write_bit(uint32_t byte_number, uint8_t bit_pos)
```

**声明头文件**

```c
#include "include/driver/efuse.h"
```

**功能说明**

- 向 eFuse 指定字节的指定位写入一位（置位）。
- 写入前先校验目标位当前是否为 0。
- 仅支持将位从 0 置为 1。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_efuse_init 成功返回后调用。
- 依赖关系：当前接口依赖 eFuse HAL 字节读取与位写入接口已就绪。
- 上下文限制：当前接口内部会执行关中断与恢复中断操作。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| byte_number | uint32_t | 要写入位所在的目标字节地址 | 0 ~ 255 |
| bit_pos | uint8_t | 目标字节内的位位置 | 0 ~ 7 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 执行成功 | 位写入成功 |
| ERRCODE_INVALID_PARAM：0x80000001 | 参数无效 | 目标位当前值非 0 |
| ERRCODE_FAIL：0xFFFFFFFF | 执行失败 | 参数非法、字节读取失败或位写入失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| EFUSE_BIT_OPERATION | 特性宏 | 支持按位读写功能（无前缀注入宏，接口级） | 由构建目标决定 |

**参考案例**

- `src/middleware/utils/at/at_plt_cmd/at/at_plt.c`

### uapi_efuse_write_bit_with_flag <a id="uapi_efuse_write_bit_with_flag"></a>

```c
errcode_t uapi_efuse_write_bit_with_flag(uint32_t byte_number, uint8_t bit_pos, uint32_t flag)
```

**声明头文件**

```c
#include "include/driver/efuse.h"
```

**功能说明**

- 在保护标志校验通过的前提下向 eFuse 指定位写入一位（置位）。
- 写入前先校验目标位当前是否为 0。
- 仅支持将位从 0 置为 1。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_efuse_init 成功返回后调用。
- 依赖关系：当前接口依赖 eFuse HAL 字节读取与位写入接口已就绪。
- 上下文限制：当前接口内部会执行关中断与恢复中断操作。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| byte_number | uint32_t | 要写入位所在的目标字节地址 | 0 ~ 255 |
| bit_pos | uint8_t | 目标字节内的位位置 | 0 ~ 7 |
| flag | uint32_t | 写入保护标志 | [EFUSE_WRITE_PROTECT_FLAG](#EFUSE_WRITE_PROTECT_FLAG)：0x5A5A5A5A |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 执行成功 | 位写入成功 |
| ERRCODE_INVALID_PARAM：0x80000001 | 参数无效 | 目标位当前值非 0 |
| ERRCODE_EFUSE_INVALID_PARAM：0x80001390 | 参数无效 | 保护标志不正确 |
| ERRCODE_FAIL：0xFFFFFFFF | 执行失败 | 参数非法、字节读取失败或位写入失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| EFUSE_BIT_OPERATION | 特性宏 | 支持按位读写功能（无前缀注入宏，接口级） | 由构建目标决定 |

### uapi_efuse_write_buffer <a id="uapi_efuse_write_buffer"></a>

```c
errcode_t uapi_efuse_write_buffer(uint32_t byte_number, const uint8_t *buffer, uint16_t length)
```

**声明头文件**

```c
#include "include/driver/efuse.h"
```

**功能说明**

- 从缓冲区向 eFuse 指定字节地址起连续写入多个字节。
- 写入前校验参数合法性。
- 写入的字节数由入参 length 指定。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_efuse_init 成功返回后调用。
- 依赖关系：当前接口依赖 eFuse HAL 缓冲区写入接口已就绪。
- 上下文限制：当前接口内部会执行关中断与恢复中断操作。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| byte_number | uint32_t | 写入数据的起始目的字节地址 | 0 ~ 255 |
| buffer | const uint8_t * | 包含待写入数据的缓冲区 | 不为NULL |
| length | uint16_t | 写入数据的长度，以字节为单位 | 1 ~ 256，且 byte_number + length ≤ 256 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 执行成功 | 缓冲区写入成功 |
| ERRCODE_EFUSE_INVALID_PARAM：0x80001390 | 参数无效 | 参数合法性校验未通过 |
| ERRCODE_FAIL：0xFFFFFFFF | 执行失败 | 缓冲区写入操作失败 |

**参考案例**

- `src/middleware/chips/ws53/update/common/upg_common_porting.c`

### uapi_efuse_write_buffer_with_flag <a id="uapi_efuse_write_buffer_with_flag"></a>

```c
errcode_t uapi_efuse_write_buffer_with_flag(uint32_t byte_number, const uint8_t *buffer, uint16_t length, uint32_t flag)
```

**声明头文件**

```c
#include "include/driver/efuse.h"
```

**功能说明**

- 在保护标志校验通过的前提下从缓冲区向 eFuse 连续写入多个字节。
- 写入前校验保护标志与参数合法性。
- 写入的字节数由入参 length 指定。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_efuse_init 成功返回后调用。
- 依赖关系：当前接口依赖 eFuse HAL 缓冲区写入接口已就绪。
- 上下文限制：当前接口内部会执行关中断与恢复中断操作。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| byte_number | uint32_t | 写入数据的起始目的字节地址 | 0 ~ 255 |
| buffer | const uint8_t * | 包含待写入数据的缓冲区 | 不为NULL |
| length | uint16_t | 写入数据的长度，以字节为单位 | 1 ~ 256，且 byte_number + length ≤ 256 |
| flag | uint32_t | 写入保护标志 | [EFUSE_WRITE_PROTECT_FLAG](#EFUSE_WRITE_PROTECT_FLAG)：0x5A5A5A5A |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 执行成功 | 缓冲区写入成功 |
| ERRCODE_EFUSE_INVALID_PARAM：0x80001390 | 参数无效 | 保护标志不正确或参数合法性校验未通过 |
| ERRCODE_FAIL：0xFFFFFFFF | 执行失败 | 缓冲区写入操作失败 |

### uapi_efuse_get_die_id <a id="uapi_efuse_get_die_id"></a>

```c
errcode_t uapi_efuse_get_die_id(uint8_t *buffer, uint16_t length)
```

**声明头文件**

```c
#include "include/driver/efuse.h"
```

**功能说明**

- 获取 eFuse 中的 Die-ID。
- 将 Die-ID 字节序列写入调用方提供的缓冲区。
- 缓冲区容量由入参 length 指定。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_efuse_init 成功返回后调用。
- 依赖关系：当前接口依赖 eFuse HAL Die-ID 获取接口已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| length | uint16_t | Die-ID 数据的长度，以字节为单位 | 不为0 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| buffer | uint8_t * | Die-ID 字节序列，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 执行成功 | Die-ID 获取成功 |
| ERRCODE_FAIL：0xFFFFFFFF | 执行失败 | 参数非法 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层获取失败 |

**参考案例**

- `src/middleware/chips/ws53/nv/nv_porting/nv_crypto.c`

### uapi_efuse_calc_crc <a id="uapi_efuse_calc_crc"></a>

```c
errcode_t uapi_efuse_calc_crc(const uint8_t *buffer, uint8_t length, uint8_t *crc)
```

**声明头文件**

```c
#include "include/driver/efuse.h"
```

**功能说明**

- 计算给定数据块的零计数 CRC。
- 逐字节统计数据块中 0 位的个数并累加输出。
- 计算结果写入调用方提供的 CRC 缓冲区。

**前置条件**

- 调用时序约束：无特定调用时序约束。
- 依赖关系：当前接口为纯计算接口，不依赖硬件资源。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| buffer | const uint8_t * | 待计算 CRC 的数据缓冲区 | 不为NULL |
| length | uint8_t | 数据长度，以字节为单位 | 0 ~ 32 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| crc | uint8_t * | 零计数 CRC 结果（数据块中 0 位的总个数），由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 执行成功 | CRC 计算完成 |
| ERRCODE_EFUSE_INVALID_PARAM：0x80001390 | 参数无效 | buffer 或 crc 为空，或长度超过上限 |

### uapi_soc_read_id <a id="uapi_soc_read_id"></a>

```c
errcode_t uapi_soc_read_id(uint8_t *id, uint16_t id_length)
```

**声明头文件**

```c
#include "include/driver/efuse.h"
```

**功能说明**

- 获取 SoC-ID。
- 将 SoC-ID 字节序列写入调用方提供的缓冲区。
- SoC-ID 固定为 20 字节序列。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_efuse_init 成功返回后调用。
- 依赖关系：当前接口依赖 eFuse HAL Die-ID 获取接口已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| id_length | uint16_t | id 缓冲区的容量，以字节为单位 | 容量 ≥ 20（实际写入固定 20 字节） |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| id | uint8_t * | SoC-ID 字节序列（长度 20 字节），由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 执行成功 | SoC-ID 获取成功 |
| ERRCODE_FAIL：0xFFFFFFFF | 执行失败 | 参数非法 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层获取失败 |

## Type definitions

### errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块对外接口的返回值类型，用于表示接口执行结果。

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```

### EFUSE_WRITE_PROTECT_FLAG <a id="EFUSE_WRITE_PROTECT_FLAG"></a>

```c
#define EFUSE_WRITE_PROTECT_FLAG            0x5A5A5A5A
```
