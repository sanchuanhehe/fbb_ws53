# Cipher

Cipher 提供 security_unified 模块下对称加解密、消息认证码、哈希与 KDF（Key Derivation Function）的统一密码服务接口。支持 AES（Advanced Encryption Standard）/SM4/TDES（Triple Data Encryption Standard）等对称算法的 ECB/CBC/CTR/CCM/GCM 等工作模式，以及 SHA（Secure Hash Algorithm）/SM3 哈希与 PBKDF2/HKDF 密钥派生。

**模块公共头文件**

```c
#include "driver/security_unified/cipher.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_drv_cipher_symc_init](#uapi_drv_cipher_symc_init) | 对称加解密模块初始化 |
| [uapi_drv_cipher_symc_deinit](#uapi_drv_cipher_symc_deinit) | 对称加解密模块去初始化 |
| [uapi_drv_cipher_symc_create](#uapi_drv_cipher_symc_create) | 创建对称加解密通道并设置通道属性 |
| [uapi_drv_cipher_symc_destroy](#uapi_drv_cipher_symc_destroy) | 销毁对称加解密通道 |
| [uapi_drv_cipher_symc_set_config](#uapi_drv_cipher_symc_set_config) | 设置对称加解密算法参数 |
| [uapi_drv_cipher_symc_get_config](#uapi_drv_cipher_symc_get_config) | 获取对称加解密算法参数 |
| [uapi_drv_cipher_symc_attach](#uapi_drv_cipher_symc_attach) | 将 keyslot 句柄关联到加解密通道 |
| [uapi_drv_cipher_symc_detach](#uapi_drv_cipher_symc_detach) | 将 keyslot 句柄与加解密通道解除关联 |
| [uapi_drv_cipher_symc_encrypt](#uapi_drv_cipher_symc_encrypt) | 将源地址数据加密输出到目的地址 |
| [uapi_drv_cipher_symc_decrypt](#uapi_drv_cipher_symc_decrypt) | 将源地址数据解密输出到目的地址 |
| [uapi_drv_cipher_symc_get_tag](#uapi_drv_cipher_symc_get_tag) | 获取 CCM 或 GCM 模式的认证标签值 |
| [uapi_drv_cipher_mac_start](#uapi_drv_cipher_mac_start) | 创建 MAC 计算通道并设置算法参数 |
| [uapi_drv_cipher_mac_update](#uapi_drv_cipher_mac_update) | 输入数据进行 MAC 计算 |
| [uapi_drv_cipher_mac_finish](#uapi_drv_cipher_mac_finish) | 获取 MAC 计算结果并销毁通道 |
| [uapi_drv_cipher_hash_init](#uapi_drv_cipher_hash_init) | 哈希计算模块初始化 |
| [uapi_drv_cipher_hash_deinit](#uapi_drv_cipher_hash_deinit) | 哈希计算模块去初始化 |
| [uapi_drv_cipher_hash_start](#uapi_drv_cipher_hash_start) | 创建哈希通道并设置算法参数 |
| [uapi_drv_cipher_hash_update](#uapi_drv_cipher_hash_update) | 输入数据进行哈希计算 |
| [uapi_drv_cipher_hash_finish](#uapi_drv_cipher_hash_finish) | 获取哈希摘要并销毁通道 |
| [uapi_drv_cipher_hash_get](#uapi_drv_cipher_hash_get) | 获取哈希计算的中间结果 |
| [uapi_drv_cipher_hash_set](#uapi_drv_cipher_hash_set) | 设置哈希计算的中间结果 |
| [uapi_drv_cipher_hash_destroy](#uapi_drv_cipher_hash_destroy) | 销毁哈希通道 |
| [uapi_drv_cipher_pbkdf2](#uapi_drv_cipher_pbkdf2) | 使用 PBKDF2 算法派生密钥 |
| [uapi_drv_cipher_hkdf_extract](#uapi_drv_cipher_hkdf_extract) | HKDF 提取阶段，从原始密钥材料提取伪随机密钥 |
| [uapi_drv_cipher_hkdf_expand](#uapi_drv_cipher_hkdf_expand) | HKDF 拓展阶段，由伪随机密钥拓展输出密钥材料 |
| [uapi_drv_cipher_hkdf](#uapi_drv_cipher_hkdf) | 执行完整 HKDF 流程，包含提取与拓展两步 |
| [uapi_drv_cipher_symc_crypt](#uapi_drv_cipher_symc_crypt) | 一步式对称加解密，支持多种算法与工作模式 |

## Functions

### uapi_drv_cipher_symc_init <a id="uapi_drv_cipher_symc_init"></a>

```c
errcode_t uapi_drv_cipher_symc_init(void)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 初始化对称加密（SYMC）模块，完成安全引擎通道资源分配。
- 成功初始化后本模块 symc 接口方可使用。
- 支持后续创建与管理加解密通道。

**前置条件**

- 调用时序约束：作为 symc 模块入口，须在其他 symc 接口之前调用。
- 依赖关系：安全引擎硬件已上电就绪。
- 未重复调用本接口，重复调用可能导致 ERROR_SECURITY_COUNT_OVERFLOW。

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 成功初始化 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_SYMC | 特性宏 | 支持对称加密功能 | n |

### uapi_drv_cipher_symc_deinit <a id="uapi_drv_cipher_symc_deinit"></a>

```c
errcode_t uapi_drv_cipher_symc_deinit(void)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 对称加密模块去初始化，释放 symc 通道资源与全局状态。
- 调用本接口后，所有已创建的 symc 通道不再可用，需重新初始化后方可使用。
- 返回去初始化执行结果。

**前置条件**

- 已通过 uapi_drv_cipher_symc_init() 完成初始化。
- 调用时序约束：应确保所有 symc 通道已销毁后再调用本接口。

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 成功去初始化 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_SYMC | 特性宏 | 支持对称加密功能 | n |

### uapi_drv_cipher_symc_create <a id="uapi_drv_cipher_symc_create"></a>

```c
errcode_t uapi_drv_cipher_symc_create(uint32_t *symc_handle, const uapi_drv_cipher_symc_attr_t *symc_attr)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 创建 symc 通道，并根据传入的属性参数设置通道类型、算法、工作模式及通道占用周期。
- 成功创建后返回通道句柄，后续加解密操作均通过该句柄进行。
- 支持长期通道与短期通道，长期通道占用资源直到显式销毁。

**前置条件**

- 已通过 uapi_drv_cipher_symc_init() 完成初始化，返回成功状态。
- symc_attr 指针不为 NULL，且指向合法的属性结构体。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| symc_attr | const [uapi_drv_cipher_symc_attr_t](#struct_uapi_drv_cipher_symc_attr_t) * | 指向 symc 通道属性结构体的指针 | 不为 NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| symc_handle | uint32_t * | 创建的 symc 通道句柄，由函数填充 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 通道创建成功 |
| ERRCODE_INVALID_PARAM：0x80000001 | 参数无效 | symc_attr 为 NULL |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_SYMC | 特性宏 | 支持对称加密功能 | n |

### uapi_drv_cipher_symc_destroy <a id="uapi_drv_cipher_symc_destroy"></a>

```c
errcode_t uapi_drv_cipher_symc_destroy(uint32_t symc_handle)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 销毁指定的 symc 通道，释放通道资源。
- 销毁后该句柄不再可用，后续操作需重新创建通道。
- 销毁时自动移除安全模块的睡眠否决，允许系统进入低功耗。

**前置条件**

- 已通过 uapi_drv_cipher_symc_init() 完成初始化。
- symc_handle 为已通过 uapi_drv_cipher_symc_create() 创建的有效通道句柄。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| symc_handle | uint32_t | 要销毁的 symc 通道号 | 有效的已创建通道句柄 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 通道销毁成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_SYMC | 特性宏 | 支持对称加密功能 | n |

### uapi_drv_cipher_symc_set_config <a id="uapi_drv_cipher_symc_set_config"></a>

```c
errcode_t uapi_drv_cipher_symc_set_config(uint32_t symc_handle, const uapi_drv_cipher_symc_ctrl_t *symc_ctrl)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 设置指定 symc 通道的算法参数，包括算法类型、工作模式、密钥长度、IV（Initialization Vector）等。
- 对于 CCM/GCM 工作模式，还需通过 param 字段配置附加参数。
- 成功配置后通道按所设参数执行加解密。

**前置条件**

- 已通过 uapi_drv_cipher_symc_init() 完成初始化。
- symc_handle 为已创建的有效通道句柄。
- symc_ctrl 指针不为 NULL。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| symc_handle | uint32_t | 要设置的通道号 | 有效的已创建通道句柄 |
| symc_ctrl | const [uapi_drv_cipher_symc_ctrl_t](#struct_uapi_drv_cipher_symc_ctrl_t) * | 对称加密算法的参数 | 不为 NULL |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 成功设置 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_SYMC | 特性宏 | 支持对称加密功能 | n |

### uapi_drv_cipher_symc_get_config <a id="uapi_drv_cipher_symc_get_config"></a>

```c
errcode_t uapi_drv_cipher_symc_get_config(uint32_t symc_handle, const uapi_drv_cipher_symc_ctrl_t *symc_ctrl)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 获取指定 symc 通道的当前算法参数配置。
- 返回的参数包括算法类型、工作模式、密钥长度、IV 及其长度等。
- 可用于确认当前通道配置状态。

**前置条件**

- 已通过 uapi_drv_cipher_symc_init() 完成初始化。
- symc_handle 为已创建的有效通道句柄。
- 已通过 uapi_drv_cipher_symc_set_config() 完成参数配置。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| symc_handle | uint32_t | 要获取算法参数的通道号 | 有效的已创建通道句柄 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| symc_ctrl | const [uapi_drv_cipher_symc_ctrl_t](#struct_uapi_drv_cipher_symc_ctrl_t) * | 对称加密算法的当前配置参数 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 成功获取 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_SYMC | 特性宏 | 支持对称加密功能 | n |

### uapi_drv_cipher_symc_attach <a id="uapi_drv_cipher_symc_attach"></a>

```c
errcode_t uapi_drv_cipher_symc_attach(uint32_t symc_handle, uint32_t keyslot_handle)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 将 keyslot 句柄关联到加解密句柄，使加解密操作使用指定 keyslot 中的密钥。
- 关联后，加解密操作使用 keyslot 中存储的密钥而非明文密钥。
- 返回关联执行结果。

**前置条件**

- 已通过 uapi_drv_cipher_symc_init() 完成初始化。
- 调用时序约束：加密/解密操作前须先完成 keyslot 关联。
- symc_handle 为已创建且已配置算法参数的通道句柄。
- keyslot_handle 为已创建的有效 keyslot 句柄。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| symc_handle | uint32_t | 加解密句柄 | 有效的已创建通道句柄 |
| keyslot_handle | uint32_t | key 的句柄 | 有效的 keyslot 句柄 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 关联成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_SYMC | 特性宏 | 支持对称加密功能 | n |

### uapi_drv_cipher_symc_detach <a id="uapi_drv_cipher_symc_detach"></a>

```c
errcode_t uapi_drv_cipher_symc_detach(uint32_t symc_handle, uint32_t keyslot_handle)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 将 keyslot 句柄与加解密句柄解关联。
- 解关联后，加解密操作不再使用该 keyslot 中的密钥。
- 返回解关联执行结果。

**前置条件**

- 已通过 uapi_drv_cipher_symc_init() 完成初始化。
- 调用时序约束：通常在加解密操作完成后调用。
- symc_handle 为已创建的有效通道句柄。
- keyslot_handle 为已关联到该通道的有效 keyslot 句柄。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| symc_handle | uint32_t | 加解密句柄 | 有效的已创建通道句柄 |
| keyslot_handle | uint32_t | key 的句柄 | 有效的 keyslot 句柄 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 解关联成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_SYMC | 特性宏 | 支持对称加密功能 | n |

### uapi_drv_cipher_symc_encrypt <a id="uapi_drv_cipher_symc_encrypt"></a>

```c
errcode_t uapi_drv_cipher_symc_encrypt(uint32_t symc_handle, const uapi_drv_cipher_buf_attr_t *src_buf, const uapi_drv_cipher_buf_attr_t *dst_buf, uint32_t length)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 将源地址数据加密，输出到目的地址。
- 支持 AES/SM4/TDES/LEA 等对称加密算法，具体算法由通道配置决定。
- 加密数据长度需满足算法对齐要求（除 CTR/CCM/GCM 模式外需 16 Bytes 对齐）。

**前置条件**

- 已通过 uapi_drv_cipher_symc_init() 完成初始化。
- symc_handle 为已创建、已配置算法参数、已关联 keyslot 的通道句柄。
- src_buf 和 dst_buf 指向的缓冲区地址有效且长度不小于 length。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| symc_handle | uint32_t | 加密句柄 | 有效的已创建且已配置通道句柄 |
| src_buf | const [uapi_drv_cipher_buf_attr_t](#struct_uapi_drv_cipher_buf_attr_t) * | 源缓冲区属性 | 不为 NULL |
| dst_buf | const [uapi_drv_cipher_buf_attr_t](#struct_uapi_drv_cipher_buf_attr_t) * | 目的缓冲区属性 | 不为 NULL |
| length | uint32_t | 加密数据长度 | 大于 0，满足算法对齐要求 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| dst_buf | [uapi_drv_cipher_buf_attr_t](#struct_uapi_drv_cipher_buf_attr_t) | 加密后的密文数据写入目的缓冲区 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 加密成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_SYMC | 特性宏 | 支持对称加密功能 | n |

### uapi_drv_cipher_symc_decrypt <a id="uapi_drv_cipher_symc_decrypt"></a>

```c
errcode_t uapi_drv_cipher_symc_decrypt(uint32_t symc_handle, const uapi_drv_cipher_buf_attr_t *src_buf, const uapi_drv_cipher_buf_attr_t *dst_buf, uint32_t length)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 将源地址数据解密，输出到目的地址。
- 支持 AES/SM4/TDES/LEA 等对称解密算法，具体算法由通道配置决定。
- 解密数据长度需满足算法对齐要求（除 CTR/CCM/GCM 模式外需 16 Bytes 对齐）。

**前置条件**

- 已通过 uapi_drv_cipher_symc_init() 完成初始化。
- symc_handle 为已创建、已配置算法参数、已关联 keyslot 的通道句柄。
- src_buf 和 dst_buf 指向的缓冲区地址有效且长度不小于 length。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| symc_handle | uint32_t | 解密句柄 | 有效的已创建且已配置通道句柄 |
| src_buf | const [uapi_drv_cipher_buf_attr_t](#struct_uapi_drv_cipher_buf_attr_t) * | 源缓冲区属性 | 不为 NULL |
| dst_buf | const [uapi_drv_cipher_buf_attr_t](#struct_uapi_drv_cipher_buf_attr_t) * | 目的缓冲区属性 | 不为 NULL |
| length | uint32_t | 解密数据长度 | 大于 0，满足算法对齐要求 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| dst_buf | [uapi_drv_cipher_buf_attr_t](#struct_uapi_drv_cipher_buf_attr_t) | 解密后的明文数据写入目的缓冲区 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 解密成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_SYMC | 特性宏 | 支持对称加密功能 | n |

### uapi_drv_cipher_symc_get_tag <a id="uapi_drv_cipher_symc_get_tag"></a>

```c
errcode_t uapi_drv_cipher_symc_get_tag(uint32_t symc_handle, uint8_t *tag, uint32_t tag_length)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 获取 CCM 或 GCM 模式的认证标签值。
- 获取的认证标签用于数据完整性校验。
- 标签长度由算法配置决定，GCM 模式典型标签长度为 16 Bytes。

**前置条件**

- 已通过 uapi_drv_cipher_symc_init() 完成初始化。
- symc_handle 为已创建且工作模式为 CCM/GCM 的通道句柄。
- 已完成加密操作。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| symc_handle | uint32_t | 加解密句柄 | 有效的 CCM/GCM 通道句柄 |
| tag_length | uint32_t | 标签值缓冲区长度 | 大于 0，与算法配置的 tag_len 一致 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| tag | uint8_t * | CCM/GCM 认证标签值 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 获取标签成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_SYMC | 特性宏 | 支持对称加密功能 | n |

### uapi_drv_cipher_mac_start <a id="uapi_drv_cipher_mac_start"></a>

```c
errcode_t uapi_drv_cipher_mac_start(uint32_t *symc_handle, const uapi_drv_cipher_symc_mac_attr_t *mac_attr)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 创建 symc 通道并设置 MAC 算法参数，启动 MAC 计算流程。
- 支持 CBC-MAC 和 CMAC（Cipher-based Message Authentication Code）工作模式。
- 成功创建后返回通道句柄，后续通过 uapi_drv_cipher_mac_update 输入数据，通过 uapi_drv_cipher_mac_finish 获取结果。

**前置条件**

- 已通过 uapi_drv_cipher_symc_init() 完成初始化，返回成功状态。
- mac_attr 指针不为 NULL，且指向合法的 MAC 属性结构体。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| mac_attr | const [uapi_drv_cipher_symc_mac_attr_t](#struct_uapi_drv_cipher_symc_mac_attr_t) * | 指向 MAC 算法参数结构体的指针 | 不为 NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| symc_handle | uint32_t * | 创建的 symc 通道句柄，由调用方分配内存、函数填充 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 通道创建成功 |
| ERRCODE_INVALID_PARAM：0x80000001 | 参数无效 | mac_attr 为 NULL |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_SYMC | 特性宏 | 支持对称加密功能 | n |

### uapi_drv_cipher_mac_update <a id="uapi_drv_cipher_mac_update"></a>

```c
errcode_t uapi_drv_cipher_mac_update(uint32_t symc_handle, const uapi_drv_cipher_buf_attr_t *src_buf, uint32_t length)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 向 MAC 计算通道输入数据，进行 MAC 计算。
- 支持多次调用，将数据分批输入，最终结果与一次性输入相同。
- 输入数据长度需满足算法对齐要求。

**前置条件**

- 已通过 uapi_drv_cipher_mac_start() 成功创建 MAC 通道。
- src_buf 指向的缓冲区有效且长度不小于 length。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| symc_handle | uint32_t | 计算 MAC 值的通道句柄 | 有效的 MAC 通道句柄 |
| src_buf | const [uapi_drv_cipher_buf_attr_t](#struct_uapi_drv_cipher_buf_attr_t) * | 输入数据的缓冲区 | 不为 NULL |
| length | uint32_t | 输入数据的缓冲区长度 | 大于 0 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | MAC 计算更新成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_SYMC | 特性宏 | 支持对称加密功能 | n |

### uapi_drv_cipher_mac_finish <a id="uapi_drv_cipher_mac_finish"></a>

```c
errcode_t uapi_drv_cipher_mac_finish(uint32_t symc_handle, uint8_t *mac, uint32_t *mac_length)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 获取 MAC 计算结果，并在计算成功时销毁 MAC 通道。
- 输出 MAC 值到指定缓冲区，同时返回实际 MAC 长度。
- 调用后通道句柄不再可用。

**前置条件**

- 已通过 uapi_drv_cipher_mac_start() 成功创建 MAC 通道。
- 已通过 uapi_drv_cipher_mac_update() 完成数据输入。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| symc_handle | uint32_t | 计算 MAC 值的通道句柄 | 有效的 MAC 通道句柄 |
| mac | uint8_t * | 输出结果的缓冲区 | 不为 NULL，空间不小于 MAC 长度 |
| mac_length | uint32_t * | 输出结果的缓冲区长度 | 不为 NULL，输入为缓冲区长度，输出为实际 MAC 长度 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| mac | uint8_t * | MAC 计算结果 |
| mac_length | uint32_t * | 实际 MAC 长度 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 获取 MAC 结果成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_SYMC | 特性宏 | 支持对称加密功能 | n |

### uapi_drv_cipher_hash_init <a id="uapi_drv_cipher_hash_init"></a>

```c
errcode_t uapi_drv_cipher_hash_init(void)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- Hash 计算模块初始化，完成 Hash 通道资源分配。
- 成功初始化后本模块 Hash 接口方可使用。
- 支持后续创建与管理 Hash 通道。

**前置条件**

- 安全引擎硬件已上电就绪。
- 未重复调用本接口。

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 成功初始化 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_HASH | 特性宏 | 支持 Hash 计算功能 | n |

### uapi_drv_cipher_hash_deinit <a id="uapi_drv_cipher_hash_deinit"></a>

```c
errcode_t uapi_drv_cipher_hash_deinit(void)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- Hash 计算模块去初始化，释放 Hash 通道资源与全局状态。
- 调用后所有已创建的 Hash 通道不再可用。
- 返回去初始化执行结果。

**前置条件**

- 已通过 uapi_drv_cipher_hash_init() 完成初始化。
- 调用时序约束：应确保所有 Hash 通道已销毁后再调用本接口。

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 成功去初始化 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_HASH | 特性宏 | 支持 Hash 计算功能 | n |

### uapi_drv_cipher_hash_start <a id="uapi_drv_cipher_hash_start"></a>

```c
errcode_t uapi_drv_cipher_hash_start(uint32_t *hash_handle, const uapi_drv_cipher_hash_attr_t *hash_attr)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 创建 Hash 通道，并根据传入的属性参数设置 Hash 算法类型、密钥等。
- 支持 SHA1/SHA224/SHA256/SHA384/SHA512/SM3 及对应 HMAC（Hash-based Message Authentication Code）算法。
- 支持长期通道与短期通道，最大支持 2 个长期通道和 8 个短期通道。

**前置条件**

- 已通过 uapi_drv_cipher_hash_init() 完成初始化，返回成功状态。
- hash_attr 指针不为 NULL，且指向合法的 Hash 属性结构体。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| hash_attr | const [uapi_drv_cipher_hash_attr_t](#struct_uapi_drv_cipher_hash_attr_t) * | 指向 Hash 属性结构体的指针 | 不为 NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| hash_handle | uint32_t * | 创建的 Hash 通道句柄，由调用方分配内存、函数填充 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 通道创建成功 |
| ERRCODE_INVALID_PARAM：0x80000001 | 参数无效 | hash_attr 为 NULL |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_HASH | 特性宏 | 支持 Hash 计算功能 | n |

### uapi_drv_cipher_hash_update <a id="uapi_drv_cipher_hash_update"></a>

```c
errcode_t uapi_drv_cipher_hash_update(uint32_t hash_handle, const uapi_drv_cipher_buf_attr_t *src_buf, const uint32_t len)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 向 Hash 通道输入数据，进行 Hash 计算。
- 支持多次调用，将数据分批输入，最终结果与一次性输入相同。
- 已调用 uapi_drv_cipher_hash_finish 获取摘要后，不能再调用本接口。

**前置条件**

- 已通过 uapi_drv_cipher_hash_start() 成功创建 Hash 通道。
- 调用时序约束：已调用 uapi_drv_cipher_hash_finish 获取摘要后不可再调用本接口。
- src_buf 指向的缓冲区有效。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| hash_handle | uint32_t | 已创建的 Hash 通道句柄 | 有效的 Hash 通道句柄 |
| src_buf | const [uapi_drv_cipher_buf_attr_t](#struct_uapi_drv_cipher_buf_attr_t) * | 源缓冲区属性，包括缓冲区地址与缓冲区安全类型 | 不为 NULL |
| len | const uint32_t | 缓冲区大小 | 大于 0 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | Hash 计算更新成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_HASH | 特性宏 | 支持 Hash 计算功能 | n |

### uapi_drv_cipher_hash_finish <a id="uapi_drv_cipher_hash_finish"></a>

```c
errcode_t uapi_drv_cipher_hash_finish(uint32_t hash_handle, uint8_t *out, uint32_t *out_len)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- Hash 计算获取摘要信息，并在计算成功时销毁 hash 句柄。
- 输入为缓冲区长度，输出为实际摘要长度。
- 调用成功后 hash 句柄不再可用。

**前置条件**

- 已通过 uapi_drv_cipher_hash_start() 成功创建 Hash 通道。
- 已通过 uapi_drv_cipher_hash_update() 完成数据输入。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| hash_handle | uint32_t | 已创建的 Hash 通道句柄 | 有效的 Hash 通道句柄 |
| out_len | uint32_t * | 存储摘要信息的缓冲区大小指针 | 不为 NULL，输入为缓冲区长度，输出为实际摘要长度 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| out | uint8_t * | Hash 摘要信息 |
| out_len | uint32_t * | 实际摘要长度 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 获取摘要成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_HASH | 特性宏 | 支持 Hash 计算功能 | n |

### uapi_drv_cipher_hash_get <a id="uapi_drv_cipher_hash_get"></a>

```c
errcode_t uapi_drv_cipher_hash_get(uint32_t hash_handle, uapi_drv_cipher_hash_clone_ctx_t *hash_clone_ctx)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 获取 Hash 计算中间结果。
- 中间结果通过 uapi_drv_cipher_hash_set 接口可恢复到其他 Hash 通道。
- 该结构体无需用户构造，由接口自动填充。

**前置条件**

- 已通过 uapi_drv_cipher_hash_start() 成功创建 Hash 通道。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| hash_handle | uint32_t | 已创建的 Hash 通道句柄 | 有效的 Hash 通道句柄 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| hash_clone_ctx | [uapi_drv_cipher_hash_clone_ctx_t](#struct_uapi_drv_cipher_hash_clone_ctx_t) | Hash 计算中间结果 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 获取中间结果成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_HASH | 特性宏 | 支持 Hash 计算功能 | n |

### uapi_drv_cipher_hash_set <a id="uapi_drv_cipher_hash_set"></a>

```c
errcode_t uapi_drv_cipher_hash_set(uint32_t hash_handle, const uapi_drv_cipher_hash_clone_ctx_t *hash_clone_ctx)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 设置 Hash 计算中间结果，将之前通过 uapi_drv_cipher_hash_get 获取的中间状态恢复到 Hash 通道。
- 可用于在不同通道间迁移 Hash 计算状态。
- 设置后可继续调用 uapi_drv_cipher_hash_update 进行后续计算。

**前置条件**

- 已通过 uapi_drv_cipher_hash_start() 成功创建 Hash 通道。
- hash_clone_ctx 为由 uapi_drv_cipher_hash_get 获取的有效中间结果。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| hash_handle | uint32_t | 已创建的 Hash 通道句柄 | 有效的 Hash 通道句柄 |
| hash_clone_ctx | const [uapi_drv_cipher_hash_clone_ctx_t](#struct_uapi_drv_cipher_hash_clone_ctx_t) * | 指向 Hash 计算中间结果结构体的指针 | 不为 NULL |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 设置中间结果成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_HASH | 特性宏 | 支持 Hash 计算功能 | n |

### uapi_drv_cipher_hash_destroy <a id="uapi_drv_cipher_hash_destroy"></a>

```c
errcode_t uapi_drv_cipher_hash_destroy(uint32_t hash_handle)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 销毁 hash 通道，释放通道资源。
- 该接口只销毁 hash 通道，不启动计算和获取摘要结果。
- 销毁时自动移除安全模块的睡眠否决，允许系统进入低功耗。

**前置条件**

- 已通过 uapi_drv_cipher_hash_start() 成功创建 Hash 通道。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| hash_handle | uint32_t | 已创建的 Hash 通道句柄 | 有效的 Hash 通道句柄 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 通道销毁成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_HASH | 特性宏 | 支持 Hash 计算功能 | n |

### uapi_drv_cipher_pbkdf2 <a id="uapi_drv_cipher_pbkdf2"></a>

```c
errcode_t uapi_drv_cipher_pbkdf2(const uapi_drv_cipher_kdf_pbkdf2_param_t *param, uint8_t *out, const uint32_t out_len)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 使用 PBKDF2 算法派生密钥。
- 支持基于口令的密钥派生，输入口令和盐值，输出派生密钥。
- 迭代次数由参数结构体中的 count 字段指定。

**前置条件**

- Hash 模块已通过 uapi_drv_cipher_hash_init() 完成初始化。
- param 指针不为 NULL，且各字段合法。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| param | const [uapi_drv_cipher_kdf_pbkdf2_param_t](#struct_uapi_drv_cipher_kdf_pbkdf2_param_t) * | PBKDF2 算法的参数结构体 | 不为 NULL |
| out | uint8_t * | 输出密钥缓冲区 | 不为 NULL |
| out_len | const uint32_t | 输出密钥缓冲区长度 | 大于 0 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| out | uint8_t * | PBKDF2 派生的密钥 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 密钥派生成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_HASH | 特性宏 | 支持 Hash 计算功能 | n |

### uapi_drv_cipher_hkdf_extract <a id="uapi_drv_cipher_hkdf_extract"></a>

```c
errcode_t uapi_drv_cipher_hkdf_extract(uapi_drv_cipher_hkdf_extract_t *extract_param, uint8_t *prk, uint32_t *prk_length)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 提取密钥，执行 HKDF-Extract 阶段。
- 使用 HMAC 算法和盐值对输入密钥材料进行提取，输出伪随机密钥。
- 提取结果可作为 uapi_drv_cipher_hkdf_expand 的输入。

**前置条件**

- Hash 模块已通过 uapi_drv_cipher_hash_init() 完成初始化。
- extract_param 指针不为 NULL，且各字段合法。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| extract_param | [uapi_drv_cipher_hkdf_extract_t](#struct_uapi_drv_cipher_hkdf_extract_t) * | 密钥提取的参数结构体 | 不为 NULL |
| prk_length | uint32_t * | 拓展密钥的伪随机密钥长度 | 不为 NULL，输入为缓冲区长度，输出为实际长度 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| prk | uint8_t * | HKDF-Extract 输出的伪随机密钥 |
| prk_length | uint32_t * | 伪随机密钥的实际长度 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 密钥提取成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_HASH | 特性宏 | 支持 Hash 计算功能 | n |

### uapi_drv_cipher_hkdf_expand <a id="uapi_drv_cipher_hkdf_expand"></a>

```c
errcode_t uapi_drv_cipher_hkdf_expand(const uapi_drv_cipher_hkdf_expand_t *expand_param, uint8_t *okm, uint32_t okm_length)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 拓展密钥，执行 HKDF-Expand 阶段。
- 使用伪随机密钥和信息参数进行密钥拓展，输出指定长度的密钥材料。
- 通常与 uapi_drv_cipher_hkdf_extract 配合使用。

**前置条件**

- Hash 模块已通过 uapi_drv_cipher_hash_init() 完成初始化。
- expand_param 指针不为 NULL，且各字段合法。
- prk 为 uapi_drv_cipher_hkdf_extract 输出的有效伪随机密钥。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| expand_param | const [uapi_drv_cipher_hkdf_expand_t](#struct_uapi_drv_cipher_hkdf_expand_t) * | 密钥拓展的参数结构体 | 不为 NULL |
| okm_length | uint32_t | 输出密钥材料长度 | 大于 0 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| okm | uint8_t * | HKDF-Expand 输出的密钥材料 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 密钥拓展成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_HASH | 特性宏 | 支持 Hash 计算功能 | n |

### uapi_drv_cipher_hkdf <a id="uapi_drv_cipher_hkdf"></a>

```c
errcode_t uapi_drv_cipher_hkdf(uapi_drv_cipher_hkdf_t *hkdf_param, uint8_t *okm, uint32_t okm_length)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- HKDF 密钥派生，包含提取密钥和拓展密钥两步。
- 输入原始密钥材料、盐值和信息参数，直接输出指定长度的密钥材料。
- 等效于依次调用 uapi_drv_cipher_hkdf_extract 和 uapi_drv_cipher_hkdf_expand。

**前置条件**

- Hash 模块已通过 uapi_drv_cipher_hash_init() 完成初始化。
- hkdf_param 指针不为 NULL，且各字段合法。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| hkdf_param | [uapi_drv_cipher_hkdf_t](#struct_uapi_drv_cipher_hkdf_t) * | HKDF 的参数结构体 | 不为 NULL |
| okm_length | uint32_t | 输出密钥材料长度 | 大于 0 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| okm | uint8_t * | HKDF 输出的密钥材料 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功 | 密钥派生成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_HASH | 特性宏 | 支持 Hash 计算功能 | n |

### uapi_drv_cipher_symc_crypt <a id="uapi_drv_cipher_symc_crypt"></a>

```c
errcode_t uapi_drv_cipher_symc_crypt(uapi_drv_cipher_symc_alg_t alg, uapi_drv_cipher_symc_work_mode_t work_mode,
    uapi_drv_cipher_symc_bit_width_t bit_width,
    const uint8_t *src, uint8_t *dst, uint32_t data_len,
    uint8_t iv[16], const uint8_t *key, uint32_t key_len, uint32_t keyslot_handle,
    bool is_encrypt
)
```

**声明头文件**

```c
#include "include/driver/security_unified/cipher.h"
```

**功能说明**

- 一步式对称加解密，支持多种算法与工作模式。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| alg | [uapi_drv_cipher_symc_alg_t](#enum_uapi_drv_cipher_symc_alg_t) | 对称加密算法 | 有效枚举值 |
| work_mode | [uapi_drv_cipher_symc_work_mode_t](#enum_uapi_drv_cipher_symc_work_mode_t) | 对称加密工作模式 | 有效枚举值 |
| bit_width | [uapi_drv_cipher_symc_bit_width_t](#enum_uapi_drv_cipher_symc_bit_width_t) | 加密位宽 | 有效枚举值 |
| src | const uint8_t * | 输入数据缓冲区 | 不为 NULL |
| data_len | uint32_t | 输入数据长度 | 大于 0 |
| iv | uint8_t[16] | 初始向量；运算后更新为最新 IV（inout） | 长度为 16 Bytes |
| key | const uint8_t * | 明文密钥；为 NULL 时使用 keyslot_handle 指定的密钥槽 | 明文密钥或有效密钥槽二选一 |
| key_len | uint32_t | 明文密钥长度 | 与算法要求一致 |
| keyslot_handle | uint32_t | 密钥槽句柄 | key 为 NULL 时必须有效 |
| is_encrypt | bool | 加解密选择 | true：加密；false：解密 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| dst | uint8_t * | 输出数据缓冲区（空间不小于 data_len），由函数写入加解密结果 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| ---- | ---- | ---- |
| ERRCODE_SUCC：0 | 成功 | 加解密完成 |
| ERRCODE_INVALID_PARAM：0x80000001 | 参数无效 | 输入参数不满足约束 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 驱动模块参与编译 | y |
| CONFIG_SECURITY_UNIFIED_SUPPORT_SYMC | 特性宏 | 支持对称加密功能 | n |

## Type definitions

### typedef_errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块返回类型为 errcode_t 的对外接口的返回值类型。

## Enumerations

### uapi_drv_cipher_symc_type_t <a id="enum_uapi_drv_cipher_symc_type_t"></a>

```c
typedef enum {
    UAPI_DRV_CIPHER_SYMC_TYPE_NORMAL = 0x0,
    UAPI_DRV_CIPHER_SYMC_TYPE_REG,
    UAPI_DRV_CIPHER_SYMC_TYPE_MAX,
    UAPI_DRV_CIPHER_SYMC_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_symc_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_CIPHER_SYMC_TYPE_NORMAL | 0x0 | 普通通道类型 |
| UAPI_DRV_CIPHER_SYMC_TYPE_REG | 0x1 | 寄存器通道类型 |
| UAPI_DRV_CIPHER_SYMC_TYPE_MAX | 0x2 | 通道类型上限值 |
| UAPI_DRV_CIPHER_SYMC_TYPE_INVALID | 0xffffffff | 无效通道类型 |

### uapi_drv_cipher_symc_alg_t <a id="enum_uapi_drv_cipher_symc_alg_t"></a>

```c
// TDES is not secure, and we advise not to use it.
typedef enum {
    UAPI_DRV_CIPHER_SYMC_ALG_TDES = 0x0,
    UAPI_DRV_CIPHER_SYMC_ALG_AES = 0x1,
    UAPI_DRV_CIPHER_SYMC_ALG_SM4 = 0x2,
    UAPI_DRV_CIPHER_SYMC_ALG_LEA = 0x3,
    UAPI_DRV_CIPHER_SYMC_ALG_DMA = 0x4,
    UAPI_DRV_CIPHER_SYMC_ALG_MAX,
    UAPI_DRV_CIPHER_SYMC_ALG_INVALID = 0xffffffff,
} uapi_drv_cipher_symc_alg_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_CIPHER_SYMC_ALG_TDES | 0x0 | TDES（Triple Data Encryption Standard）算法，不建议使用 |
| UAPI_DRV_CIPHER_SYMC_ALG_AES | 0x1 | AES 算法 |
| UAPI_DRV_CIPHER_SYMC_ALG_SM4 | 0x2 | SM4（SM4 Block Cipher）算法 |
| UAPI_DRV_CIPHER_SYMC_ALG_LEA | 0x3 | LEA（Lightweight Encryption Algorithm）算法 |
| UAPI_DRV_CIPHER_SYMC_ALG_DMA | 0x4 | DMA（Direct Memory Access）模式 |
| UAPI_DRV_CIPHER_SYMC_ALG_MAX | 0x5 | 算法类型上限值 |
| UAPI_DRV_CIPHER_SYMC_ALG_INVALID | 0xffffffff | 无效算法类型 |

### uapi_drv_cipher_symc_work_mode_t <a id="enum_uapi_drv_cipher_symc_work_mode_t"></a>

```c
// ECB is not secure, and we advise not to use it.
typedef enum {
    UAPI_DRV_CIPHER_SYMC_WORK_MODE_ECB = 0x0,
    UAPI_DRV_CIPHER_SYMC_WORK_MODE_CBC,
    UAPI_DRV_CIPHER_SYMC_WORK_MODE_CTR,
    UAPI_DRV_CIPHER_SYMC_WORK_MODE_OFB,
    UAPI_DRV_CIPHER_SYMC_WORK_MODE_CFB,
    UAPI_DRV_CIPHER_SYMC_WORK_MODE_CCM,
    UAPI_DRV_CIPHER_SYMC_WORK_MODE_GCM,
    UAPI_DRV_CIPHER_SYMC_WORK_MODE_CBC_MAC,
    UAPI_DRV_CIPHER_SYMC_WORK_MODE_CMAC,
    UAPI_DRV_CIPHER_SYMC_WORK_MODE_MAX,
    UAPI_DRV_CIPHER_SYMC_WORK_MODE_INVALID = 0xffffffff,
} uapi_drv_cipher_symc_work_mode_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_CIPHER_SYMC_WORK_MODE_ECB | 0x0 | ECB（Electronic Codebook）模式，不建议使用 |
| UAPI_DRV_CIPHER_SYMC_WORK_MODE_CBC | 0x1 | CBC（Cipher Block Chaining）模式 |
| UAPI_DRV_CIPHER_SYMC_WORK_MODE_CTR | 0x2 | CTR（Counter Mode）模式 |
| UAPI_DRV_CIPHER_SYMC_WORK_MODE_OFB | 0x3 | OFB（Output Feedback）模式 |
| UAPI_DRV_CIPHER_SYMC_WORK_MODE_CFB | 0x4 | CFB（Cipher Feedback）模式 |
| UAPI_DRV_CIPHER_SYMC_WORK_MODE_CCM | 0x5 | CCM 模式 |
| UAPI_DRV_CIPHER_SYMC_WORK_MODE_GCM | 0x6 | GCM 模式 |
| UAPI_DRV_CIPHER_SYMC_WORK_MODE_CBC_MAC | 0x7 | CBC-MAC 模式 |
| UAPI_DRV_CIPHER_SYMC_WORK_MODE_CMAC | 0x8 | CMAC 模式 |
| UAPI_DRV_CIPHER_SYMC_WORK_MODE_MAX | 0x9 | 工作模式上限值 |
| UAPI_DRV_CIPHER_SYMC_WORK_MODE_INVALID | 0xffffffff | 无效工作模式 |

### uapi_drv_cipher_symc_key_length_t <a id="enum_uapi_drv_cipher_symc_key_length_t"></a>

```c
typedef enum {
    UAPI_DRV_CIPHER_SYMC_KEY_64BIT =  0x0,
    UAPI_DRV_CIPHER_SYMC_KEY_128BIT = 0x1,
    UAPI_DRV_CIPHER_SYMC_KEY_192BIT = 0x2,
    UAPI_DRV_CIPHER_SYMC_KEY_256BIT = 0x3,
    UAPI_DRV_CIPHER_SYMC_KEY_LENGTH_MAX,
    UAPI_DRV_CIPHER_SYMC_KEY_LENGTH_INVALID = 0xffffffff,
} uapi_drv_cipher_symc_key_length_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_CIPHER_SYMC_KEY_64BIT | 0x0 | 64 位密钥长度 |
| UAPI_DRV_CIPHER_SYMC_KEY_128BIT | 0x1 | 128 位密钥长度 |
| UAPI_DRV_CIPHER_SYMC_KEY_192BIT | 0x2 | 192 位密钥长度 |
| UAPI_DRV_CIPHER_SYMC_KEY_256BIT | 0x3 | 256 位密钥长度 |
| UAPI_DRV_CIPHER_SYMC_KEY_LENGTH_MAX | 0x4 | 密钥长度上限值 |
| UAPI_DRV_CIPHER_SYMC_KEY_LENGTH_INVALID | 0xffffffff | 无效密钥长度 |

### uapi_drv_cipher_symc_key_parity_t <a id="enum_uapi_drv_cipher_symc_key_parity_t"></a>

```c
typedef enum {
    UAPI_DRV_CIPHER_SYMC_KEY_EVEN =  0x0,
    UAPI_DRV_CIPHER_SYMC_KEY_ODD  =  0x1,
    UAPI_DRV_CIPHER_SYMC_KEY_PARITY_MAX,
    UAPI_DRV_CIPHER_SYMC_KEY_PARITY_INVALID = 0xffffffff,
} uapi_drv_cipher_symc_key_parity_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_CIPHER_SYMC_KEY_EVEN | 0x0 | 偶密钥 |
| UAPI_DRV_CIPHER_SYMC_KEY_ODD | 0x1 | 奇密钥 |
| UAPI_DRV_CIPHER_SYMC_KEY_PARITY_MAX | 0x2 | 密钥奇偶性上限值 |
| UAPI_DRV_CIPHER_SYMC_KEY_PARITY_INVALID | 0xffffffff | 无效密钥奇偶性 |

### uapi_drv_cipher_symc_bit_width_t <a id="enum_uapi_drv_cipher_symc_bit_width_t"></a>

```c
typedef enum {
    UAPI_DRV_CIPHER_SYMC_BIT_WIDTH_1BIT = 0x0,
    UAPI_DRV_CIPHER_SYMC_BIT_WIDTH_8BIT = 0x1,
    UAPI_DRV_CIPHER_SYMC_BIT_WIDTH_64BIT = 0x2,
    UAPI_DRV_CIPHER_SYMC_BIT_WIDTH_128BIT = 0x3,
    UAPI_DRV_CIPHER_SYMC_BIT_WIDTH_MAX,
    UAPI_DRV_CIPHER_SYMC_BIT_WIDTH_INVALID = 0xffffffff,
} uapi_drv_cipher_symc_bit_width_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_CIPHER_SYMC_BIT_WIDTH_1BIT | 0x0 | 1 位宽 |
| UAPI_DRV_CIPHER_SYMC_BIT_WIDTH_8BIT | 0x1 | 8 位宽 |
| UAPI_DRV_CIPHER_SYMC_BIT_WIDTH_64BIT | 0x2 | 64 位宽 |
| UAPI_DRV_CIPHER_SYMC_BIT_WIDTH_128BIT | 0x3 | 128 位宽 |
| UAPI_DRV_CIPHER_SYMC_BIT_WIDTH_MAX | 0x4 | 位宽上限值 |
| UAPI_DRV_CIPHER_SYMC_BIT_WIDTH_INVALID | 0xffffffff | 无效位宽 |

### uapi_drv_cipher_symc_iv_change_type_t <a id="enum_uapi_drv_cipher_symc_iv_change_type_t"></a>

```c
typedef enum {
    UAPI_DRV_CIPHER_SYMC_IV_DO_NOT_CHANGE = 0,
    UAPI_DRV_CIPHER_SYMC_IV_CHANGE_ONE_PKG,
    UAPI_DRV_CIPHER_SYMC_IV_CHANGE_ALL_PKG,
    /* GCM. */
    UAPI_DRV_CIPHER_SYMC_GCM_IV_DO_NOT_CHANGE,
    UAPI_DRV_CIPHER_SYMC_GCM_IV_CHANGE_START,
    UAPI_DRV_CIPHER_SYMC_GCM_IV_CHANGE_UPDATE,
    UAPI_DRV_CIPHER_SYMC_GCM_IV_CHANGE_FINISH,
    /* CCM. */
    UAPI_DRV_CIPHER_SYMC_CCM_IV_DO_NOT_CHANGE,
    UAPI_DRV_CIPHER_SYMC_CCM_IV_CHANGE_START,
    UAPI_DRV_CIPHER_SYMC_CCM_IV_CHANGE_UPDATE,
    UAPI_DRV_CIPHER_SYMC_CCM_IV_CHANGE_FINISH,
    UAPI_DRV_CIPHER_SYMC_IV_CHANGE_MAX,
    UAPI_DRV_CIPHER_SYMC_IV_CHANGE_INVALID = 0xffffffff,
} uapi_drv_cipher_symc_iv_change_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_CIPHER_SYMC_IV_DO_NOT_CHANGE | 0 | IV 不变 |
| UAPI_DRV_CIPHER_SYMC_IV_CHANGE_ONE_PKG | 1 | IV 单包变化 |
| UAPI_DRV_CIPHER_SYMC_IV_CHANGE_ALL_PKG | 2 | IV 所有包变化 |
| UAPI_DRV_CIPHER_SYMC_GCM_IV_DO_NOT_CHANGE | 3 | GCM 模式 IV 不变 |
| UAPI_DRV_CIPHER_SYMC_GCM_IV_CHANGE_START | 4 | GCM 模式 IV 起始变化 |
| UAPI_DRV_CIPHER_SYMC_GCM_IV_CHANGE_UPDATE | 5 | GCM 模式 IV 更新变化 |
| UAPI_DRV_CIPHER_SYMC_GCM_IV_CHANGE_FINISH | 6 | GCM 模式 IV 结束变化 |
| UAPI_DRV_CIPHER_SYMC_CCM_IV_DO_NOT_CHANGE | 7 | CCM 模式 IV 不变 |
| UAPI_DRV_CIPHER_SYMC_CCM_IV_CHANGE_START | 8 | CCM 模式 IV 起始变化 |
| UAPI_DRV_CIPHER_SYMC_CCM_IV_CHANGE_UPDATE | 9 | CCM 模式 IV 更新变化 |
| UAPI_DRV_CIPHER_SYMC_CCM_IV_CHANGE_FINISH | 10 | CCM 模式 IV 结束变化 |
| UAPI_DRV_CIPHER_SYMC_IV_CHANGE_MAX | 11 | IV 变化标志上限值 |
| UAPI_DRV_CIPHER_SYMC_IV_CHANGE_INVALID | 0xffffffff | 无效 IV 变化标志 |

### uapi_drv_cipher_buffer_secure_t <a id="enum_uapi_drv_cipher_buffer_secure_t"></a>

```c
typedef enum uapi_drv_cipher_buffer_secure {
    UAPI_DRV_CIPHER_BUF_SECURE,
    UAPI_DRV_CIPHER_BUF_NONSECURE,
} uapi_drv_cipher_buffer_secure_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_CIPHER_BUF_SECURE | 0 | 安全缓冲区 |
| UAPI_DRV_CIPHER_BUF_NONSECURE | 1 | 非安全缓冲区 |

### uapi_drv_cipher_hash_type_t <a id="enum_uapi_drv_cipher_hash_type_t"></a>

```c
typedef enum uapi_drv_hash_type {
    UAPI_DRV_CIPHER_HASH_TYPE_SHA1 = 0xf690a0,
    UAPI_DRV_CIPHER_HASH_TYPE_SHA224 = 0x10690e0,
    UAPI_DRV_CIPHER_HASH_TYPE_SHA256 = 0x1169100,
    UAPI_DRV_CIPHER_HASH_TYPE_SHA384 = 0x127a180,
    UAPI_DRV_CIPHER_HASH_TYPE_SHA512 = 0x137a200,
    UAPI_DRV_CIPHER_HASH_TYPE_SM3 = 0x2169100,
    UAPI_DRV_CIPHER_HASH_TYPE_HMAC_SHA1 = 0x10f690a0,
    UAPI_DRV_CIPHER_HASH_TYPE_HMAC_SHA224 = 0x110690e0,
    UAPI_DRV_CIPHER_HASH_TYPE_HMAC_SHA256 = 0x11169100,
    UAPI_DRV_CIPHER_HASH_TYPE_HMAC_SHA384 = 0x1127a180,
    UAPI_DRV_CIPHER_HASH_TYPE_HMAC_SHA512 = 0x1137a200,
    UAPI_DRV_CIPHER_HASH_TYPE_HMAC_SM3 = 0x12169100,
    UAPI_DRV_CIPHER_HASH_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_hash_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_CIPHER_HASH_TYPE_SHA1 | 0xf690a0 | SHA1（Secure Hash Algorithm 1）算法，不建议使用 |
| UAPI_DRV_CIPHER_HASH_TYPE_SHA224 | 0x10690e0 | SHA224（Secure Hash Algorithm 224-bit）算法，不建议使用 |
| UAPI_DRV_CIPHER_HASH_TYPE_SHA256 | 0x1169100 | SHA256（Secure Hash Algorithm 256-bit）算法 |
| UAPI_DRV_CIPHER_HASH_TYPE_SHA384 | 0x127a180 | SHA384（Secure Hash Algorithm 384-bit）算法 |
| UAPI_DRV_CIPHER_HASH_TYPE_SHA512 | 0x137a200 | SHA512（Secure Hash Algorithm 512-bit）算法 |
| UAPI_DRV_CIPHER_HASH_TYPE_SM3 | 0x2169100 | SM3（SM3 Cryptographic Hash Algorithm）算法 |
| UAPI_DRV_CIPHER_HASH_TYPE_HMAC_SHA1 | 0x10f690a0 | HMAC-SHA1 算法，不建议使用 |
| UAPI_DRV_CIPHER_HASH_TYPE_HMAC_SHA224 | 0x110690e0 | HMAC-SHA224 算法，不建议使用 |
| UAPI_DRV_CIPHER_HASH_TYPE_HMAC_SHA256 | 0x11169100 | HMAC-SHA256 算法 |
| UAPI_DRV_CIPHER_HASH_TYPE_HMAC_SHA384 | 0x1127a180 | HMAC-SHA384 算法 |
| UAPI_DRV_CIPHER_HASH_TYPE_HMAC_SHA512 | 0x1137a200 | HMAC-SHA512 算法 |
| UAPI_DRV_CIPHER_HASH_TYPE_HMAC_SM3 | 0x12169100 | HMAC-SM3 算法 |
| UAPI_DRV_CIPHER_HASH_TYPE_INVALID | 0xffffffff | 无效 hash 算法类型 |

## Structures

### uapi_drv_cipher_buf_attr_t <a id="struct_uapi_drv_cipher_buf_attr_t"></a>

```c
typedef struct uapi_drv_cipher_buf_attr {
    uint64_t uapi_mem_handle;
    uint64_t addr_offset;
    void *kapi_mem_handle;
    uintptr_t phys_addr;
    void *virt_addr;
    uapi_drv_cipher_buffer_secure_t buf_sec;
} uapi_drv_cipher_buf_attr_t;
```

| 成员 | 类型 | 描述 |
| ---- | ---- | ---- |
| uapi_mem_handle | uint64_t | 该参数未使用 |
| addr_offset | uint64_t | 该参数未使用 |
| kapi_mem_handle | void * | 该参数未使用 |
| phys_addr | uintptr_t | 缓冲区的物理地址 |
| virt_addr | void * | 缓冲区的 CPU 地址 |
| buf_sec | uapi_drv_cipher_buffer_secure_t | 缓冲区安全属性 |

### uapi_drv_cipher_symc_attr_t <a id="struct_uapi_drv_cipher_symc_attr_t"></a>

```c
typedef struct {
    uapi_drv_cipher_symc_alg_t symc_alg;
    uapi_drv_cipher_symc_work_mode_t work_mode;
    uapi_drv_cipher_symc_type_t symc_type;
    bool is_long_term;
} uapi_drv_cipher_symc_attr_t;
```

| 成员 | 类型 | 描述 |
| ---- | ---- | ---- |
| symc_alg | uapi_drv_cipher_symc_alg_t | 对称加密算法 |
| work_mode | uapi_drv_cipher_symc_work_mode_t | 对称加密算法工作模式 |
| symc_type | uapi_drv_cipher_symc_type_t | 对称加密通道类型 |
| is_long_term | bool | 长短期通道占用标志 |

### uapi_drv_cipher_symc_config_aes_ccm_gcm_t <a id="struct_uapi_drv_cipher_symc_config_aes_ccm_gcm_t"></a>

```c
typedef struct {
    uapi_drv_cipher_buf_attr_t aad_buf;
    uint32_t aad_len;
    uint32_t data_len;
    uint32_t tag_len;
} uapi_drv_cipher_symc_config_aes_ccm_gcm_t;
```

| 成员 | 类型 | 描述 |
| ---- | ---- | ---- |
| aad_buf | uapi_drv_cipher_buf_attr_t | 附加信息的缓冲区属性结构体 |
| aad_len | uint32_t | 附加信息的长度（Bytes） |
| data_len | uint32_t | 加密数据的长度（Bytes） |
| tag_len | uint32_t | 标签的长度（Bytes） |

### uapi_drv_cipher_symc_ctrl_t <a id="struct_uapi_drv_cipher_symc_ctrl_t"></a>

```c
typedef struct {
    uapi_drv_cipher_symc_alg_t symc_alg;
    uapi_drv_cipher_symc_work_mode_t work_mode;
    uapi_drv_cipher_symc_key_length_t symc_key_length;
    uapi_drv_cipher_symc_key_parity_t key_parity;
    uapi_drv_cipher_symc_bit_width_t symc_bit_width;
    uapi_drv_cipher_symc_iv_change_type_t iv_change_flag;
    uint8_t iv[UAPI_DRV_CIPHER_IV_LEN_IN_BYTES];
    uint32_t iv_length;
    void *param;
} uapi_drv_cipher_symc_ctrl_t;
```

| 成员 | 类型 | 描述 |
| ---- | ---- | ---- |
| symc_alg | uapi_drv_cipher_symc_alg_t | 对称加密算法 |
| work_mode | uapi_drv_cipher_symc_work_mode_t | 对称加密算法工作模式 |
| symc_key_length | uapi_drv_cipher_symc_key_length_t | 对称加密密钥长度 |
| key_parity | uapi_drv_cipher_symc_key_parity_t | 对称算法密钥奇偶性 |
| symc_bit_width | uapi_drv_cipher_symc_bit_width_t | 对称算法密钥位宽 |
| iv_change_flag | uapi_drv_cipher_symc_iv_change_type_t | 对称算法初始值标志 |
| iv | uint8_t[16] | 对称加密算法初始值 |
| iv_length | uint32_t | 对称加密算法初始值长度 |
| param | void * | 对称加密 CCM 和 GCM 工作模式的参数 |

### uapi_drv_cipher_symc_mac_attr_t <a id="struct_uapi_drv_cipher_symc_mac_attr_t"></a>

```c
typedef struct {
    bool is_long_term;
    uapi_drv_cipher_symc_alg_t symc_alg;
    uapi_drv_cipher_symc_work_mode_t work_mode;
    uapi_drv_cipher_symc_key_length_t symc_key_length;
    uint32_t keyslot_chn;
} uapi_drv_cipher_symc_mac_attr_t;
```

| 成员 | 类型 | 描述 |
| ---- | ---- | ---- |
| is_long_term | bool | 长短期通道占用标志 |
| symc_alg | uapi_drv_cipher_symc_alg_t | 对称加密算法 |
| work_mode | uapi_drv_cipher_symc_work_mode_t | 对称加密算法工作模式 |
| symc_key_length | uapi_drv_cipher_symc_key_length_t | 对称加密密钥长度 |
| keyslot_chn | uint32_t | Key 槽 ID |

### uapi_drv_cipher_hash_attr_t <a id="struct_uapi_drv_cipher_hash_attr_t"></a>

```c
typedef struct uapi_drv_hash_attr {
    uint8_t *key;
    uint32_t key_len;
    uint32_t keyslot_handle;
    uapi_drv_cipher_hash_type_t hash_type;
    bool is_keyslot;
    bool is_long_term;
} uapi_drv_cipher_hash_attr_t;
```

| 成员 | 类型 | 描述 |
| ---- | ---- | ---- |
| key | uint8_t * | 指向 HMAC 算法使用密钥的指针，当使用 HMAC 算法且 is_keyslot 为 false 时该参数生效 |
| key_len | uint32_t | 密钥长度（Bytes），HMAC-SHA1/SHA224/SHA256/SM3 不超过 64 Bytes，HMAC-SHA384/SHA512 不超过 128 Bytes |
| keyslot_handle | uint32_t | HMAC 算法使用的 keyslot 通道句柄，当 is_keyslot 为 true 时该参数生效 |
| hash_type | uapi_drv_cipher_hash_type_t | hash 算法类型 |
| is_keyslot | bool | 指示 HMAC 算法是否使用 keyslot |
| is_long_term | bool | 指示创建的通道为长期通道还是短期通道，最大支持创建 2 个长期通道和 8 个短期通道 |

### uapi_drv_cipher_hash_clone_ctx_t <a id="struct_uapi_drv_cipher_hash_clone_ctx_t"></a>

```c
typedef struct uapi_drv_cipher_hash_clone_ctx {
    uint32_t length[2];
    uint32_t state[UAPI_DRV_CIPHER_HASH_RESULT_SIZE_MAX_IN_WORD];
    uint32_t tail_len;
    uapi_drv_cipher_hash_type_t hash_type;
    uint8_t o_key_pad[UAPI_DRV_CIPHER_HASH_BLOCK_SIZE_MAX];
    uint8_t i_key_pad[UAPI_DRV_CIPHER_HASH_BLOCK_SIZE_MAX];
    uint8_t tail[UAPI_DRV_CIPHER_HASH_BLOCK_SIZE_MAX];
} uapi_drv_cipher_hash_clone_ctx_t;
```

| 成员 | 类型 | 描述 |
| ---- | ---- | ---- |
| length | uint32_t[2] | 保存当前已处理的数据长度（位） |
| state | uint32_t[16] | 保存计算中间结果 |
| tail_len | uint32_t | 上次计算后剩余未对齐的尾部数据长度 |
| hash_type | uapi_drv_cipher_hash_type_t | hash 计算使用的算法 |
| o_key_pad | uint8_t[128] | 保存 o_key_pad，HMAC 算法使用 |
| i_key_pad | uint8_t[128] | 保存 i_key_pad，HMAC 算法使用 |
| tail | uint8_t[128] | 上次计算后剩余未对齐的尾部数据 |

该结构体的内容无需用户构造，通过 uapi_drv_cipher_hash_get 接口获取，并通过 uapi_drv_cipher_hash_set 接口设置。

### uapi_drv_cipher_kdf_pbkdf2_param_t <a id="struct_uapi_drv_cipher_kdf_pbkdf2_param_t"></a>

```c
typedef struct {
    uapi_drv_cipher_hash_type_t hash_type;
    uint8_t *password;
    uint32_t plen;
    uint8_t *salt;
    uint32_t slen;
    uint16_t count;
} uapi_drv_cipher_kdf_pbkdf2_param_t;
```

| 成员 | 类型 | 描述 |
| ---- | ---- | ---- |
| hash_type | uapi_drv_cipher_hash_type_t | PBKDF2 使用的 hash 算法类型 |
| password | uint8_t * | PBKDF2 的输入口令 |
| plen | uint32_t | PBKDF2 的输入口令长度 |
| salt | uint8_t * | PBKDF2 的盐值 |
| slen | uint32_t | PBKDF2 的盐值长度 |
| count | uint16_t | PBKDF2 的迭代次数 |

### uapi_drv_cipher_hkdf_extract_t <a id="struct_uapi_drv_cipher_hkdf_extract_t"></a>

```c
typedef struct {
    uapi_drv_cipher_hash_type_t hmac_type;
    uint8_t *salt;
    uint32_t salt_length;
    uint8_t *ikm;
    uint32_t ikm_length;
} uapi_drv_cipher_hkdf_extract_t;
```

| 成员 | 类型 | 描述 |
| ---- | ---- | ---- |
| hmac_type | uapi_drv_cipher_hash_type_t | 提取密钥的 HMAC 算法类型 |
| salt | uint8_t * | 提取密钥的盐值 |
| salt_length | uint32_t | 提取密钥的盐值长度 |
| ikm | uint8_t * | 提取密钥的原始密钥材料 |
| ikm_length | uint32_t | 提取密钥的原始密钥材料长度 |

### uapi_drv_cipher_hkdf_expand_t <a id="struct_uapi_drv_cipher_hkdf_expand_t"></a>

```c
typedef struct {
    uapi_drv_cipher_hash_type_t hmac_type;
    uint8_t *prk;
    uint32_t prk_length;
    uint8_t *info;
    uint32_t info_length;
} uapi_drv_cipher_hkdf_expand_t;
```

| 成员 | 类型 | 描述 |
| ---- | ---- | ---- |
| hmac_type | uapi_drv_cipher_hash_type_t | 拓展密钥的 HMAC 算法类型 |
| prk | uint8_t * | 拓展密钥的伪随机密钥 |
| prk_length | uint32_t | 拓展密钥的伪随机密钥长度 |
| info | uint8_t * | 拓展密钥的信息 |
| info_length | uint32_t | 拓展密钥的信息长度 |

### uapi_drv_cipher_hkdf_t <a id="struct_uapi_drv_cipher_hkdf_t"></a>

```c
typedef struct {
    uapi_drv_cipher_hash_type_t hmac_type;
    uint8_t *salt;
    uint32_t salt_length;
    uint8_t *ikm;
    uint32_t ikm_length;
    uint8_t *info;
    uint32_t info_length;
} uapi_drv_cipher_hkdf_t;
```

| 成员 | 类型 | 描述 |
| ---- | ---- | ---- |
| hmac_type | uapi_drv_cipher_hash_type_t | 提取、拓展密钥的 HMAC 算法类型 |
| salt | uint8_t * | 提取密钥的盐值 |
| salt_length | uint32_t | 提取密钥的盐值长度 |
| ikm | uint8_t * | 提取密钥的原始密钥材料 |
| ikm_length | uint32_t | 提取密钥的原始密钥材料长度 |
| info | uint8_t * | 拓展密钥的信息 |
| info_length | uint32_t | 拓展密钥的信息长度 |

## Macros

### UAPI_DRV_CIPHER_IV_LEN_IN_BYTES <a id="UAPI_DRV_CIPHER_IV_LEN_IN_BYTES"></a>

```c
#define UAPI_DRV_CIPHER_IV_LEN_IN_BYTES 16
```

### UAPI_DRV_CIPHER_HASH_RESULT_SIZE_MAX_IN_WORD <a id="UAPI_DRV_CIPHER_HASH_RESULT_SIZE_MAX_IN_WORD"></a>

```c
#define UAPI_DRV_CIPHER_HASH_RESULT_SIZE_MAX_IN_WORD 16      // for SHA-512
```

### UAPI_DRV_CIPHER_HASH_BLOCK_SIZE_MAX <a id="UAPI_DRV_CIPHER_HASH_BLOCK_SIZE_MAX"></a>

```c
#define UAPI_DRV_CIPHER_HASH_BLOCK_SIZE_MAX 128              // for SHA-512
```
