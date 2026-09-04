# TRNG

TRNG（True Random Number Generator）提供硬件真随机数生成能力，支持获取单个 uint32_t 随机数和指定字节长度的随机数据，供加密运算、密钥派生等安全场景使用。

**模块公共头文件**

```c
#include "include/driver/security_unified/trng.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_drv_cipher_trng_get_random](#uapi_drv_cipher_trng_get_random) | 获取单个 uint32_t 大小的硬件随机数 |
| [uapi_drv_cipher_trng_get_random_bytes](#uapi_drv_cipher_trng_get_random_bytes) | 获取指定字节长度的硬件随机数 |

## Functions

### uapi_drv_cipher_trng_get_random <a id="uapi_drv_cipher_trng_get_random"></a>

```c
errcode_t uapi_drv_cipher_trng_get_random(uint32_t *randnum)
```

**声明头文件**

```c
#include "include/driver/security_unified/trng.h"
```

**功能说明**

- 获取单个 uint32_t（4 Bytes）大小的硬件随机数。
- 将生成的随机数写入调用方提供的缓冲区。
- 用于需要单个随机数的场景。

**前置条件**

- 调用时序约束：TRNG 驱动完成初始化后调用，未初始化时接口返回错误。

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| randnum | uint32_t * | 调用方分配内存，接口写入生成的 uint32_t 硬件随机数，约束：不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 成功获取硬件随机数 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**参考案例**

- `src/middleware/chips/ws53/nv/nv_porting/nv_crypto.c`

### uapi_drv_cipher_trng_get_random_bytes <a id="uapi_drv_cipher_trng_get_random_bytes"></a>

```c
errcode_t uapi_drv_cipher_trng_get_random_bytes(uint8_t *randnum, uint32_t size)
```

**声明头文件**

```c
#include "include/driver/security_unified/trng.h"
```

**功能说明**

- 获取指定字节长度的硬件随机数。
- 将生成的随机字节序列写入调用方提供的缓冲区。
- 用于需要任意长度随机数据的场景。

**前置条件**

- 调用时序约束：TRNG 驱动完成初始化后调用，未初始化时接口返回错误。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| size | uint32_t | 待生成的随机数字节长度，randnum 缓冲区容量需不小于该值 | 按需指定，单位 Bytes |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| randnum | uint8_t * | 调用方分配内存，接口写入 size 字节的硬件随机数序列，约束：不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 成功获取指定长度的硬件随机数 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**参考案例**

- `src/middleware/chips/ws53/mac_addr/mac_addr.c`
- `src/open_source/wpa_supplicant/liteos_wpa_src/crypto_mbedtls.c`

## Type definitions

### errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块两个接口的返回值类型，用于表示接口执行结果。

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```
