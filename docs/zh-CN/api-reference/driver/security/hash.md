# Hash

Hash 提供 SHA-256（Secure Hash Algorithm 256-bit）哈希计算接口，基于安全硬件加速器对外提供单次计算与流式（start/update/finish）分块计算两种使用方式，输出 256 位（32 字节）摘要。

**模块公共头文件**

```c
#include "include/driver/security_unified/security_sha256.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_drv_cipher_sha256_start](#uapi_drv_cipher_sha256_start) | 创建 SHA-256 计算通道并返回通道句柄 |
| [uapi_drv_cipher_sha256_update](#uapi_drv_cipher_sha256_update) | 向已创建的 SHA-256 通道追加待计算数据 |
| [uapi_drv_cipher_sha256_finish](#uapi_drv_cipher_sha256_finish) | 结束 SHA-256 计算并输出摘要，成功时销毁句柄 |
| [uapi_drv_cipher_sha256](#uapi_drv_cipher_sha256) | 单次完成一段数据的完整 SHA-256 计算并输出摘要 |

## Functions

### uapi_drv_cipher_sha256_start <a id="uapi_drv_cipher_sha256_start"></a>

```c
errcode_t uapi_drv_cipher_sha256_start(uint32_t *hash_handle)
```

**声明头文件**

```c
#include "include/driver/security_unified/security_sha256.h"
```

**功能说明**

- 创建一个 SHA-256 计算通道。
- 通过出参返回通道句柄，用于后续 update/finish 调用。
- 成功创建后进入待输入数据的初始状态。

**前置条件**

- 调用时序约束：当前接口为流式 SHA-256 计算的入口，必须在使用 update/finish 之前成功调用。
- 依赖关系：当前接口依赖安全硬件加速模块已初始化就绪。
- 上下文限制：当前接口需在任务上下文调用，禁止在中断上下文调用。

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| hash_handle | uint32_t * | 由调用方分配内存，函数填充创建成功的 SHA-256 通道句柄，供后续 update/finish 接口使用 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 通道创建成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**参考案例**

- `src/middleware/chips/ws53/nv/nv_porting/nv_crypto.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SECURITY_UNIFIED_SUPPORT_HASH | 特性宏 | 支持哈希计算接口功能（宏在构建系统中无引用，按特性宏归类） | n |

### uapi_drv_cipher_sha256_update <a id="uapi_drv_cipher_sha256_update"></a>

```c
errcode_t uapi_drv_cipher_sha256_update(uint32_t hash_handle, const uint8_t *buf, uint32_t len)
```

**声明头文件**

```c
#include "include/driver/security_unified/security_sha256.h"
```

**功能说明**

- 向已创建的 SHA-256 通道追加一段待计算的数据。
- 支持将一段长数据拆分为多段多次调用，多次分块与单次整段输入得到相同的摘要结果。
- 一旦已调用 finish 获取摘要信息，该通道不可再进行追加计算。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_drv_cipher_sha256_start](#uapi_drv_cipher_sha256_start) 成功返回后、且尚未对该通道调用 finish 之前使用。
- 依赖关系：当前接口依赖入参 hash_handle 为已创建的有效 SHA-256 通道句柄。
- 上下文限制：当前接口需在任务上下文调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| hash_handle | uint32_t | 已创建的 SHA-256 通道句柄 | 由 uapi_drv_cipher_sha256_start 返回的有效句柄 |
| buf | const uint8_t * | 待追加计算的源数据缓冲区指针 | 不为NULL |
| len | uint32_t | 待追加计算的源数据缓冲区大小，单位字节 | 0 ~ 0xFFFFFFFF |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 数据追加成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**参考案例**

- `src/middleware/chips/ws53/nv/nv_porting/nv_crypto.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SECURITY_UNIFIED_SUPPORT_HASH | 特性宏 | 支持哈希计算接口功能（宏在构建系统中无引用，按特性宏归类） | n |

### uapi_drv_cipher_sha256_finish <a id="uapi_drv_cipher_sha256_finish"></a>

```c
errcode_t uapi_drv_cipher_sha256_finish(uint32_t hash_handle, uint8_t *out, uint32_t *out_len)
```

**声明头文件**

```c
#include "include/driver/security_unified/security_sha256.h"
```

**功能说明**

- 结束当前 SHA-256 通道的计算并输出摘要信息。
- 计算成功时销毁该通道句柄，释放对应资源。
- 通过 out_len 出参返回实际写入的摘要长度。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_drv_cipher_sha256_start](#uapi_drv_cipher_sha256_start) 成功返回后、且对该通道至少组织好计算流程后调用。
- 依赖关系：当前接口依赖入参 hash_handle 为已创建的有效 SHA-256 通道句柄。
- 上下文限制：当前接口需在任务上下文调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| hash_handle | uint32_t | 已创建的 SHA-256 通道句柄 | 由 uapi_drv_cipher_sha256_start 返回的有效句柄 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| out | uint8_t * | 由调用方分配的摘要缓冲区地址指针，函数填充计算得到的摘要数据 |
| out_len | uint32_t * | 输入为缓冲区容量，输出为实际写入的摘要字节数 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 计算成功并销毁通道句柄 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**参考案例**

- `src/middleware/chips/ws53/nv/nv_porting/nv_crypto.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SECURITY_UNIFIED_SUPPORT_HASH | 特性宏 | 支持哈希计算接口功能（宏在构建系统中无引用，按特性宏归类） | n |

### uapi_drv_cipher_sha256 <a id="uapi_drv_cipher_sha256"></a>

```c
errcode_t uapi_drv_cipher_sha256(const uint8_t *buf, uint32_t len, uint8_t *out, uint32_t out_len)
```

**声明头文件**

```c
#include "include/driver/security_unified/security_sha256.h"
```

**功能说明**

- 对一段完整数据一次性完成 SHA-256 计算并输出摘要。
- 调用方无需自行管理通道句柄。
- 摘要固定写入 32 字节。

**前置条件**

- 调用时序约束：当前接口为单次完整计算入口，调用前无需手动创建句柄。
- 依赖关系：当前接口依赖安全硬件加速模块已初始化就绪。
- 上下文限制：当前接口需在任务上下文调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| buf | const uint8_t * | 待计算摘要的源数据缓冲区指针 | 不为NULL |
| len | uint32_t | 待计算摘要的源数据缓冲区大小，单位字节 | 0 ~ 0xFFFFFFFF |
| out_len | uint32_t | 存储摘要的缓冲区容量，单位字节；实际写入固定为 32 字节摘要 | [SHA256_HASH_SIZE](#SHA256_HASH_SIZE)：32 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| out | uint8_t * | 计算得到的 32 字节摘要，由函数写入调用方分配的缓冲区 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 单次计算成功并输出摘要 |
| ERRCODE_INVALID_PARAM：0x80000001 | 参数无效 | out_len 不等于 SHA256_HASH_SIZE(32) |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SECURITY_UNIFIED_SUPPORT_HASH | 特性宏 | 支持哈希计算接口功能（宏在构建系统中无引用，按特性宏归类） | n |

## Type definitions

### typedef_errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块返回类型为 errcode_t 的对外接口的返回值类型。

## Macros

### SHA256_HASH_SIZE <a id="SHA256_HASH_SIZE"></a>

```c
#define SHA256_HASH_SIZE    32
```
