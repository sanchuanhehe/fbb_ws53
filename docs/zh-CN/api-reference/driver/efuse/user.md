# eFuse User

eFuse User（Electronic Fuse）提供用户预留区域的读写访问接口，支持按字节缓冲区的批量读取与写入，以及按位读取与按位写 1 操作。位操作接口的可用性受构建系统注入宏 EFUSE_BIT_OPERATION 控制。

**模块公共头文件**

```c
#include "include/driver/efuse_user.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_efuse_user_read_buffer](#uapi_efuse_user_read_buffer) | 从用户预留的 eFuse 区域按字节批量读取数据到缓冲区 |
| [uapi_efuse_user_write_buffer](#uapi_efuse_user_write_buffer) | 将缓冲区数据按字节批量写入用户预留的 eFuse 区域 |
| [uapi_efuse_user_write_bit](#uapi_efuse_user_write_bit) | 向用户预留 eFuse 区域中的对应位写 1 |
| [uapi_efuse_user_read_bit](#uapi_efuse_user_read_bit) | 从用户预留的 eFuse 区域中读取单个位的值 |

## Functions

### uapi_efuse_user_read_buffer <a id="uapi_efuse_user_read_buffer"></a>

```c
errcode_t uapi_efuse_user_read_buffer(uint32_t offset, uint8_t *buffer, uint16_t length)
```

**声明头文件**

```c
#include "include/driver/efuse_user.h"
```

**功能说明**

- 从用户预留的 eFuse 区域中读取连续多字节数据，写入调用方提供的缓冲区。
- 读取起始位置由字节偏移地址与读取长度共同确定，访问范围限定在用户预留区域内。
- 接口对外提供 eFuse 用户区的批量读取能力。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_efuse_init 成功返回后调用。
- 依赖关系：当前接口依赖用户预留 eFuse 区域的起始位与位长度已在构建配置中定义（CUSTOMER_RSVD_EFUSE_START_BIT、CUSTOMER_RSVD_EFUSE_BIT_LEN）。
- 上下文限制：建议在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| offset | uint32_t | 待读取区域在用户预留 eFuse 区域中的起始字节偏移地址 | offset 与 length 之和对应位宽不超出用户预留区域位长度，即(offset + length) * 8 ≤ CUSTOMER_RSVD_EFUSE_BIT_LEN |
| length | uint16_t | 待读取数据的长度，以字节为单位 | length ≥ 1 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| buffer | uint8_t * | 从用户预留 eFuse 区域读取到的 length 字节数据，由调用方分配内存、接口填充 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 成功读取 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### uapi_efuse_user_write_buffer <a id="uapi_efuse_user_write_buffer"></a>

```c
errcode_t uapi_efuse_user_write_buffer(uint32_t offset, const uint8_t *buffer, uint16_t length)
```

**声明头文件**

```c
#include "include/driver/efuse_user.h"
```

**功能说明**

- 将调用方缓冲区中的多字节数据写入用户预留的 eFuse 区域。
- 写入起始位置由字节偏移地址与写入长度共同确定，访问范围限定在用户预留区域内。
- 接口对外提供 eFuse 用户区的批量写入能力。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_efuse_init 成功返回后调用。
- 依赖关系：当前接口依赖用户预留 eFuse 区域的起始位与位长度已在构建配置中定义（CUSTOMER_RSVD_EFUSE_START_BIT、CUSTOMER_RSVD_EFUSE_BIT_LEN）。
- 上下文限制：建议在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| offset | uint32_t | 待写入区域在用户预留 eFuse 区域中的起始字节偏移地址 | offset 与 length 之和对应位宽不超出用户预留区域位长度，即(offset + length) * 8 ≤ CUSTOMER_RSVD_EFUSE_BIT_LEN |
| buffer | const uint8_t * | 包含待写入数据的缓冲区，由调用方提供 | 不为 NULL |
| length | uint16_t | 待写入数据的长度，以字节为单位 | length ≥ 1 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 成功写入 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### uapi_efuse_user_write_bit <a id="uapi_efuse_user_write_bit"></a>

```c
errcode_t uapi_efuse_user_write_bit(uint32_t byte_offset, uint8_t bit_pos)
```

**声明头文件**

```c
#include "include/driver/efuse_user.h"
```

**功能说明**

- 向用户预留 eFuse 区域中对应字节内的指定位写 1。
- 写入位置由字节偏移地址与位位置共同确定，访问范围限定在用户预留区域内。
- 接口对外提供 eFuse 用户区的按位写 1 能力。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_efuse_init 成功返回后调用。
- 依赖关系：当前接口依赖用户预留 eFuse 区域的起始位与位长度已在构建配置中定义（CUSTOMER_RSVD_EFUSE_START_BIT、CUSTOMER_RSVD_EFUSE_BIT_LEN）。
- 上下文限制：建议在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| byte_offset | uint32_t | 待写入位所在字节在用户预留 eFuse 区域中的字节偏移地址 | byte_offset 与 bit_pos 对应位不超出用户预留区域位长度，即 byte_offset * 8 + bit_pos ≤ CUSTOMER_RSVD_EFUSE_BIT_LEN |
| bit_pos | uint8_t | 待写入位在对应字节中的位位置 | 0 ~ 7 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 写 1 成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| EFUSE_BIT_OPERATION | 特性宏 | 支持 eFuse 位操作接口功能（接口级，无前缀注入宏，包裹函数声明） | 由构建目标决定 |

### uapi_efuse_user_read_bit <a id="uapi_efuse_user_read_bit"></a>

```c
errcode_t uapi_efuse_user_read_bit(uint32_t byte_offset, uint8_t bit_pos, uint8_t *value)
```

**声明头文件**

```c
#include "include/driver/efuse_user.h"
```

**功能说明**

- 从用户预留的 eFuse 区域中读取对应字节内单个位的值。
- 读取位置由字节偏移地址与位位置共同确定，访问范围限定在用户预留区域内。
- 接口对外提供 eFuse 用户区的按位读取能力。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_efuse_init 成功返回后调用。
- 依赖关系：当前接口依赖用户预留 eFuse 区域的起始位与位长度已在构建配置中定义（CUSTOMER_RSVD_EFUSE_START_BIT、CUSTOMER_RSVD_EFUSE_BIT_LEN）。
- 上下文限制：建议在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| byte_offset | uint32_t | 待读取位所在字节在用户预留 eFuse 区域中的字节偏移地址 | byte_offset 与 bit_pos 对应位不超出用户预留区域位长度，即 byte_offset * 8 + bit_pos ≤ CUSTOMER_RSVD_EFUSE_BIT_LEN |
| bit_pos | uint8_t | 待读取位在对应字节中的位位置 | 0 ~ 7 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| value | uint8_t * | 读取到的位值（0 或 1），由调用方分配内存、接口填充 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 成功读取 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| EFUSE_BIT_OPERATION | 特性宏 | 支持 eFuse 位操作接口功能（接口级，无前缀注入宏，包裹函数声明） | 由构建目标决定 |

## Type definitions

### errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块全部对外接口的返回值类型，表示接口执行结果。

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```
