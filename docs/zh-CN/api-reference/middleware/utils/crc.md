# CRC

CRC（Cyclic Redundancy Check）提供 16 位与 32 位 CRC 校验值计算能力，用于对数据缓冲区进行完整性校验。模块基于固定多项式（CRC-16 采用 x<sup>16</sup> + x<sup>12</sup> + x<sup>5</sup> + 1，即 0x1021；CRC-32 符合 IEEE 802.3 标准，即 0x04C11DB7）实现逐段计算，前一段计算结果可作为后一段计算的初始值传入，支持分段连续校验。

**模块公共头文件**

```c
#include "include/middleware/utils/uapi_crc.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_crc16](#uapi_crc16) | 基于多项式 x<sup>16</sup> + x<sup>12</sup> + x<sup>5</sup> + 1（0x1021）计算 16 位 CRC 校验值 |
| [uapi_crc32](#uapi_crc32) | 基于 IEEE 802.3 标准（0x04C11DB7）计算 32 位 CRC 校验值（含补码） |
| [uapi_crc32_no_comp](#uapi_crc32_no_comp) | 基于 IEEE 802.3 标准（0x04C11DB7）计算 32 位 CRC 校验值（无补码） |

## Functions

### uapi_crc16 <a id="uapi_crc16"></a>

```c
uint16_t uapi_crc16(uint16_t crc_start, const uint8_t *buf, uint32_t length)
```

**声明头文件**

```c
#include "include/middleware/utils/uapi_crc.h"
```

**功能说明**

- 基于多项式 x<sup>16</sup> + x<sup>12</sup> + x<sup>5</sup> + 1（0x1021）计算输入数据缓冲区的 16 位 CRC 校验值。
- 支持分段计算：前一段计算结果作为后一段计算的初始值传入，实现连续多段数据的累积校验。
- 输入缓冲区指针为 NULL 时，直接返回传入的初始值。

**前置条件**

- 调用时序约束：无初始化依赖，可直接调用。
- 依赖关系：传入的缓冲区内存由调用方分配并保证有效（为 NULL 时函数直接返回初始值）。
- 上下文限制：本接口为纯计算函数，可在任意上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| crc_start | uint16_t | CRC 计算初始值；分段计算时传入前一段计算结果 | 0 ~ 65535 |
| buf | const uint8_t * | 指向待计算数据缓冲区的指针，由调用方分配 | 不为 NULL（为 NULL 时函数直接返回 crc_start） |
| length | uint32_t | 待计算数据长度，单位 Bytes | 0 ~ 4294967295 |

**返回值**

返回类型：uint16_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 ~ 65535 | CRC 计算结果 | 正常计算返回 16 位 CRC 值；buf 为 NULL 时返回传入的 crc_start |

**参考案例**

- `middleware/utils/nv/nv_storage_lib/nv_key.c`
- `middleware/utils/dfx/log_file/log_file.c`

### uapi_crc32 <a id="uapi_crc32"></a>

```c
uint32_t uapi_crc32(uint32_t crc_start, const uint8_t *buf, uint32_t length)
```

**声明头文件**

```c
#include "include/middleware/utils/uapi_crc.h"
```

**功能说明**

- 基于符合 IEEE 802.3 CRC-32 标准的多项式 0x04C11DB7 计算输入数据缓冲区的 32 位 CRC 校验值。
- 内部对初始值与结果进行按位取反（补码）处理，符合 IEEE 802.3 标准定义的完整 CRC-32 算法。
- 支持分段计算：前一段计算结果作为后一段计算的初始值传入，实现连续多段数据的累积校验。

**前置条件**

- 调用时序约束：无初始化依赖，可直接调用。
- 依赖关系：传入的缓冲区内存由调用方分配并保证有效（为 NULL 时函数直接返回初始值的按位取反结果）。
- 上下文限制：本接口为纯计算函数，可在任意上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| crc_start | uint32_t | CRC 计算初始值；分段计算时传入前一段计算结果 | 0 ~ 4294967295 |
| buf | const uint8_t * | 指向待计算数据缓冲区的指针，由调用方分配 | 不为 NULL（为 NULL 时函数直接返回对 crc_start 处理后的结果） |
| length | uint32_t | 待计算数据长度，单位 Bytes | 0 ~ 4294967295 |

**返回值**

返回类型：uint32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 ~ 4294967295 | CRC 计算结果 | 正常计算返回 32 位 CRC 值（含补码处理） |

**参考案例**

- `middleware/utils/nv/nv_storage_lib/nv_key.c`
- `middleware/utils/nv/nv_storage_lib/nv_update.c`

### uapi_crc32_no_comp <a id="uapi_crc32_no_comp"></a>

```c
uint32_t uapi_crc32_no_comp(uint32_t crc_start, const uint8_t *buf, uint32_t length)
```

**声明头文件**

```c
#include "include/middleware/utils/uapi_crc.h"
```

**功能说明**

- 基于符合 IEEE 802.3 CRC-32 标准的多项式 0x04C11DB7 计算输入数据缓冲区的 32 位 CRC 校验值。
- 与 uapi_crc32 相比不对初始值与结果进行按位取反（无补码）处理，仅做表驱动 CRC 计算。
- 支持分段计算：前一段计算结果作为后一段计算的初始值传入，实现连续多段数据的累积校验。
- 输入缓冲区指针为 NULL 时，直接返回传入的初始值。

**前置条件**

- 调用时序约束：无初始化依赖，可直接调用。
- 依赖关系：传入的缓冲区内存由调用方分配并保证有效（为 NULL 时函数直接返回初始值）。
- 上下文限制：本接口为纯计算函数，可在任意上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| crc_start | uint32_t | CRC 计算初始值；分段计算时传入前一段计算结果 | 0 ~ 4294967295 |
| buf | const uint8_t * | 指向待计算数据缓冲区的指针，由调用方分配 | 不为 NULL（为 NULL 时函数直接返回 crc_start） |
| length | uint32_t | 待计算数据长度，单位 Bytes | 0 ~ 4294967295 |

**返回值**

返回类型：uint32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 ~ 4294967295 | CRC 计算结果 | 正常计算返回 32 位 CRC 值（无补码）；buf 为 NULL 时返回传入的 crc_start |
