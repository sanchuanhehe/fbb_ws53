# pke

PKE (Public Key Engine) 提供公钥密码运算能力，覆盖 ECC (Elliptic Curve Cryptography) 密钥生成、ECDSA (Elliptic Curve Digital Signature Algorithm) / EdDSA (Edwards-curve Digital Signature Algorithm) 签名与验签、ECDH (Elliptic Curve Diffie-Hellman) 密钥协商、SM2 签名/加密与解密、RSA (Rivest-Shamir-Adleman) 签名/验签/加解密、DH (Diffie-Hellman) 密钥生成与协商，以及大数模加、模减、模乘、模逆、取模、大数乘和模幂运算。

**模块公共头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_drv_cipher_pke_ecc_gen_key](#uapi_drv_cipher_pke_ecc_gen_key) | 生成 ECC 公私钥对 |
| [uapi_drv_cipher_pke_ecdsa_sign](#uapi_drv_cipher_pke_ecdsa_sign) | 使用 ECC 私钥对摘要进行 ECDSA 签名 |
| [uapi_drv_cipher_pke_ecdsa_verify](#uapi_drv_cipher_pke_ecdsa_verify) | 使用 ECC 公钥对签名进行 ECDSA 验签 |
| [uapi_drv_cipher_pke_eddsa_sign](#uapi_drv_cipher_pke_eddsa_sign) | 使用 Edwards 曲线私钥进行 EdDSA 签名 |
| [uapi_drv_cipher_pke_eddsa_verify](#uapi_drv_cipher_pke_eddsa_verify) | 使用 Edwards 曲线公钥进行 EdDSA 验签 |
| [uapi_drv_cipher_pke_ecc_gen_ecdh_key](#uapi_drv_cipher_pke_ecc_gen_ecdh_key) | 基于 ECC 公私钥进行 ECDH 密钥协商 |
| [uapi_drv_cipher_pke_check_dot_on_curve](#uapi_drv_cipher_pke_check_dot_on_curve) | 检查点是否在指定 ECC 曲线上 |
| [uapi_drv_cipher_pke_sm2_dsa_hash](#uapi_drv_cipher_pke_sm2_dsa_hash) | 计算 SM2 DSA (Digital Signature Algorithm) 的 SM3 摘要 |
| [uapi_drv_cipher_pke_sm2_public_encrypt](#uapi_drv_cipher_pke_sm2_public_encrypt) | 使用 SM2 公钥对明文加密 |
| [uapi_drv_cipher_pke_sm2_private_decrypt](#uapi_drv_cipher_pke_sm2_private_decrypt) | 使用 SM2 私钥对密文解密 |
| [uapi_drv_cipher_pke_rsa_sign](#uapi_drv_cipher_pke_rsa_sign) | 使用 RSA 私钥对摘要进行签名 |
| [uapi_drv_cipher_pke_rsa_verify](#uapi_drv_cipher_pke_rsa_verify) | 使用 RSA 公钥对签名进行验签 |
| [uapi_drv_cipher_pke_rsa_public_encrypt](#uapi_drv_cipher_pke_rsa_public_encrypt) | 使用 RSA 公钥对明文加密 |
| [uapi_drv_cipher_pke_rsa_private_decrypt](#uapi_drv_cipher_pke_rsa_private_decrypt) | 使用 RSA 私钥对密文解密 |
| [uapi_drv_cipher_pke_dh_gen_key](#uapi_drv_cipher_pke_dh_gen_key) | 生成 DH 公私钥对或由私钥推导公钥 |
| [uapi_drv_cipher_pke_dh_compute_key](#uapi_drv_cipher_pke_dh_compute_key) | 基于 DH 算法计算共享密钥 |
| [uapi_drv_cipher_pke_add_mod](#uapi_drv_cipher_pke_add_mod) | 大数模加运算 c = (a + b) mod p |
| [uapi_drv_cipher_pke_sub_mod](#uapi_drv_cipher_pke_sub_mod) | 大数模减运算 c = (a - b) mod p |
| [uapi_drv_cipher_pke_mul_mod](#uapi_drv_cipher_pke_mul_mod) | 大数模乘运算 c = (a * b) mod p |
| [uapi_drv_cipher_pke_inv_mod](#uapi_drv_cipher_pke_inv_mod) | 大数模逆运算 c = (a^-1) mod p |
| [uapi_drv_cipher_pke_mod](#uapi_drv_cipher_pke_mod) | 大数取模运算 c = a mod p |
| [uapi_drv_cipher_pke_mul](#uapi_drv_cipher_pke_mul) | 大数乘运算 c = a * b |
| [uapi_drv_cipher_pke_exp_mod](#uapi_drv_cipher_pke_exp_mod) | 大数模幂运算 out = (in ^ k) mod n |

## Functions

### uapi_drv_cipher_pke_ecc_gen_key <a id="uapi_drv_cipher_pke_ecc_gen_key"></a>

```c
errcode_t uapi_drv_cipher_pke_ecc_gen_key(uapi_drv_cipher_pke_ecc_curve_type_t curve_type,
    const uapi_drv_cipher_pke_data_t *input_priv_key,
    const uapi_drv_cipher_pke_data_t *output_priv_key,
    const uapi_drv_cipher_pke_ecc_point_t *output_pub_key)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 依据指定的 ECC 曲线类型生成 ECC 公私钥对
- 输入私钥可为空指针，为空时由内部生成随机私钥
- 输出私钥与输出公钥由调用方提供缓冲区，接口填充结果

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| curve_type | [uapi_drv_cipher_pke_ecc_curve_type_t](#uapi_drv_cipher_pke_ecc_curve_type_t) | ECC 曲线类型 | [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256](#uapi_drv_cipher_pke_ecc_curve_type_t):0 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384](#uapi_drv_cipher_pke_ecc_curve_type_t):1 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512](#uapi_drv_cipher_pke_ecc_curve_type_t):2 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K](#uapi_drv_cipher_pke_ecc_curve_type_t):3 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P192R](#uapi_drv_cipher_pke_ecc_curve_type_t):4 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P224R](#uapi_drv_cipher_pke_ecc_curve_type_t):5 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256R](#uapi_drv_cipher_pke_ecc_curve_type_t):6 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P384R](#uapi_drv_cipher_pke_ecc_curve_type_t):7 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P521R](#uapi_drv_cipher_pke_ecc_curve_type_t):8 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748](#uapi_drv_cipher_pke_ecc_curve_type_t):9 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748_448](#uapi_drv_cipher_pke_ecc_curve_type_t):10 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC8032](#uapi_drv_cipher_pke_ecc_curve_type_t):11 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_SM2](#uapi_drv_cipher_pke_ecc_curve_type_t):12 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_MAX](#uapi_drv_cipher_pke_ecc_curve_type_t):13 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_INVALID](#uapi_drv_cipher_pke_ecc_curve_type_t):0xffffffff |
| input_priv_key | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入私钥，可为空指针；非空时作为生成私钥的输入 | 可为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| output_priv_key | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出私钥，由调用方分配缓冲区，接口填充私钥数据 |
| output_pub_key | [uapi_drv_cipher_pke_ecc_point_t](#uapi_drv_cipher_pke_ecc_point_t) | 输出公钥，由调用方分配 X/Y 坐标缓冲区，接口填充公钥坐标 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 密钥对生成成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_ECC_GEN_KEY | 特性宏 | 支持 ECC 密钥生成功能 | y |

### uapi_drv_cipher_pke_ecdsa_sign <a id="uapi_drv_cipher_pke_ecdsa_sign"></a>

```c
errcode_t uapi_drv_cipher_pke_ecdsa_sign(uapi_drv_cipher_pke_ecc_curve_type_t curve_type,
    const uapi_drv_cipher_pke_data_t *priv_key,
    const uapi_drv_cipher_pke_data_t *hash,
    const uapi_drv_cipher_pke_ecc_sig_t *sig)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 使用 ECC 私钥对输入摘要进行 ECDSA 数字签名
- 签名结果输出到调用方提供的签名结构体缓冲区
- 支持多种 ECC 曲线类型

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| curve_type | [uapi_drv_cipher_pke_ecc_curve_type_t](#uapi_drv_cipher_pke_ecc_curve_type_t) | ECC 曲线类型 | [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256](#uapi_drv_cipher_pke_ecc_curve_type_t):0 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384](#uapi_drv_cipher_pke_ecc_curve_type_t):1 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512](#uapi_drv_cipher_pke_ecc_curve_type_t):2 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K](#uapi_drv_cipher_pke_ecc_curve_type_t):3 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P192R](#uapi_drv_cipher_pke_ecc_curve_type_t):4 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P224R](#uapi_drv_cipher_pke_ecc_curve_type_t):5 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256R](#uapi_drv_cipher_pke_ecc_curve_type_t):6 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P384R](#uapi_drv_cipher_pke_ecc_curve_type_t):7 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P521R](#uapi_drv_cipher_pke_ecc_curve_type_t):8 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748](#uapi_drv_cipher_pke_ecc_curve_type_t):9 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748_448](#uapi_drv_cipher_pke_ecc_curve_type_t):10 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC8032](#uapi_drv_cipher_pke_ecc_curve_type_t):11 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_SM2](#uapi_drv_cipher_pke_ecc_curve_type_t):12 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_MAX](#uapi_drv_cipher_pke_ecc_curve_type_t):13 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_INVALID](#uapi_drv_cipher_pke_ecc_curve_type_t):0xffffffff |
| priv_key | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入 ECC 私钥 | 不为NULL |
| hash | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入待签名的摘要数据 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| sig | [uapi_drv_cipher_pke_ecc_sig_t](#uapi_drv_cipher_pke_ecc_sig_t) | 输出签名结果，由调用方分配 r/s 缓冲区，接口填充签名值 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 签名生成成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### uapi_drv_cipher_pke_ecdsa_verify <a id="uapi_drv_cipher_pke_ecdsa_verify"></a>

```c
errcode_t uapi_drv_cipher_pke_ecdsa_verify(uapi_drv_cipher_pke_ecc_curve_type_t curve_type,
    const uapi_drv_cipher_pke_ecc_point_t *pub_key,
    const uapi_drv_cipher_pke_data_t *hash,
    const uapi_drv_cipher_pke_ecc_sig_t *sig)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 使用 ECC 公钥对输入签名进行 ECDSA 验签
- 验签输入包括公钥、摘要与签名值
- 支持多种 ECC 曲线类型

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| curve_type | [uapi_drv_cipher_pke_ecc_curve_type_t](#uapi_drv_cipher_pke_ecc_curve_type_t) | ECC 曲线类型 | [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256](#uapi_drv_cipher_pke_ecc_curve_type_t):0 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384](#uapi_drv_cipher_pke_ecc_curve_type_t):1 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512](#uapi_drv_cipher_pke_ecc_curve_type_t):2 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K](#uapi_drv_cipher_pke_ecc_curve_type_t):3 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P192R](#uapi_drv_cipher_pke_ecc_curve_type_t):4 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P224R](#uapi_drv_cipher_pke_ecc_curve_type_t):5 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256R](#uapi_drv_cipher_pke_ecc_curve_type_t):6 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P384R](#uapi_drv_cipher_pke_ecc_curve_type_t):7 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P521R](#uapi_drv_cipher_pke_ecc_curve_type_t):8 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748](#uapi_drv_cipher_pke_ecc_curve_type_t):9 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748_448](#uapi_drv_cipher_pke_ecc_curve_type_t):10 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC8032](#uapi_drv_cipher_pke_ecc_curve_type_t):11 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_SM2](#uapi_drv_cipher_pke_ecc_curve_type_t):12 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_MAX](#uapi_drv_cipher_pke_ecc_curve_type_t):13 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_INVALID](#uapi_drv_cipher_pke_ecc_curve_type_t):0xffffffff |
| pub_key | [uapi_drv_cipher_pke_ecc_point_t](#uapi_drv_cipher_pke_ecc_point_t) | 输入 ECC 公钥 | 不为NULL |
| hash | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入待验签的摘要数据 | 不为NULL |
| sig | [uapi_drv_cipher_pke_ecc_sig_t](#uapi_drv_cipher_pke_ecc_sig_t) | 输入待验证的签名值 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 验签通过 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 验签失败或执行失败 |

**参考案例**

- `src/middleware/utils/update/common/upg_verify.c`

### uapi_drv_cipher_pke_eddsa_sign <a id="uapi_drv_cipher_pke_eddsa_sign"></a>

```c
errcode_t uapi_drv_cipher_pke_eddsa_sign(uapi_drv_cipher_pke_ecc_curve_type_t curve_type,
    const uapi_drv_cipher_pke_data_t *priv_key,
    const uapi_drv_cipher_pke_msg_t *msg,
    const uapi_drv_cipher_pke_ecc_sig_t *sig)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 使用 Edwards 曲线私钥对输入消息进行 EdDSA 数字签名
- 签名输入为完整消息而非摘要
- 签名结果输出到调用方提供的签名结构体缓冲区

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| curve_type | [uapi_drv_cipher_pke_ecc_curve_type_t](#uapi_drv_cipher_pke_ecc_curve_type_t) | ECC 曲线类型 | [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256](#uapi_drv_cipher_pke_ecc_curve_type_t):0 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384](#uapi_drv_cipher_pke_ecc_curve_type_t):1 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512](#uapi_drv_cipher_pke_ecc_curve_type_t):2 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K](#uapi_drv_cipher_pke_ecc_curve_type_t):3 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P192R](#uapi_drv_cipher_pke_ecc_curve_type_t):4 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P224R](#uapi_drv_cipher_pke_ecc_curve_type_t):5 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256R](#uapi_drv_cipher_pke_ecc_curve_type_t):6 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P384R](#uapi_drv_cipher_pke_ecc_curve_type_t):7 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P521R](#uapi_drv_cipher_pke_ecc_curve_type_t):8 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748](#uapi_drv_cipher_pke_ecc_curve_type_t):9 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748_448](#uapi_drv_cipher_pke_ecc_curve_type_t):10 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC8032](#uapi_drv_cipher_pke_ecc_curve_type_t):11 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_SM2](#uapi_drv_cipher_pke_ecc_curve_type_t):12 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_MAX](#uapi_drv_cipher_pke_ecc_curve_type_t):13 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_INVALID](#uapi_drv_cipher_pke_ecc_curve_type_t):0xffffffff |
| priv_key | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入 Edwards 曲线私钥 | 不为NULL |
| msg | [uapi_drv_cipher_pke_msg_t](#uapi_drv_cipher_pke_msg_t) | 输入待签名消息 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| sig | [uapi_drv_cipher_pke_ecc_sig_t](#uapi_drv_cipher_pke_ecc_sig_t) | 输出签名结果，由调用方分配 r/s 缓冲区，接口填充签名值 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 签名生成成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_EDWARD | 特性宏 | 支持 Edwards 曲线签名功能 | y |

### uapi_drv_cipher_pke_eddsa_verify <a id="uapi_drv_cipher_pke_eddsa_verify"></a>

```c
errcode_t uapi_drv_cipher_pke_eddsa_verify(uapi_drv_cipher_pke_ecc_curve_type_t curve_type,
    const uapi_drv_cipher_pke_ecc_point_t *pub_key,
    const uapi_drv_cipher_pke_msg_t *msg,
    const uapi_drv_cipher_pke_ecc_sig_t *sig)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 使用 Edwards 曲线公钥对输入签名进行 EdDSA 验签
- 验签输入包括公钥、消息与签名值
- 支持多种 ECC 曲线类型

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| curve_type | [uapi_drv_cipher_pke_ecc_curve_type_t](#uapi_drv_cipher_pke_ecc_curve_type_t) | ECC 曲线类型 | [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256](#uapi_drv_cipher_pke_ecc_curve_type_t):0 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384](#uapi_drv_cipher_pke_ecc_curve_type_t):1 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512](#uapi_drv_cipher_pke_ecc_curve_type_t):2 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K](#uapi_drv_cipher_pke_ecc_curve_type_t):3 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P192R](#uapi_drv_cipher_pke_ecc_curve_type_t):4 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P224R](#uapi_drv_cipher_pke_ecc_curve_type_t):5 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256R](#uapi_drv_cipher_pke_ecc_curve_type_t):6 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P384R](#uapi_drv_cipher_pke_ecc_curve_type_t):7 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P521R](#uapi_drv_cipher_pke_ecc_curve_type_t):8 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748](#uapi_drv_cipher_pke_ecc_curve_type_t):9 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748_448](#uapi_drv_cipher_pke_ecc_curve_type_t):10 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC8032](#uapi_drv_cipher_pke_ecc_curve_type_t):11 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_SM2](#uapi_drv_cipher_pke_ecc_curve_type_t):12 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_MAX](#uapi_drv_cipher_pke_ecc_curve_type_t):13 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_INVALID](#uapi_drv_cipher_pke_ecc_curve_type_t):0xffffffff |
| pub_key | [uapi_drv_cipher_pke_ecc_point_t](#uapi_drv_cipher_pke_ecc_point_t) | 输入 Edwards 曲线公钥 | 不为NULL |
| msg | [uapi_drv_cipher_pke_msg_t](#uapi_drv_cipher_pke_msg_t) | 输入待验签消息 | 不为NULL |
| sig | [uapi_drv_cipher_pke_ecc_sig_t](#uapi_drv_cipher_pke_ecc_sig_t) | 输入待验证的签名值 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 验签通过 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 验签失败或执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_EDWARD | 特性宏 | 支持 Edwards 曲线验签功能 | y |

### uapi_drv_cipher_pke_ecc_gen_ecdh_key <a id="uapi_drv_cipher_pke_ecc_gen_ecdh_key"></a>

```c
errcode_t uapi_drv_cipher_pke_ecc_gen_ecdh_key(uapi_drv_cipher_pke_ecc_curve_type_t curve_type,
    const uapi_drv_cipher_pke_ecc_point_t *input_pub_key,
    const uapi_drv_cipher_pke_data_t *input_priv_key,
    const uapi_drv_cipher_pke_data_t *output_shared_key)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 基于输入的 ECC 公钥与私钥执行 ECDH 密钥协商
- 输出协商得到的共享密钥
- 支持多种 ECC 曲线类型

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| curve_type | [uapi_drv_cipher_pke_ecc_curve_type_t](#uapi_drv_cipher_pke_ecc_curve_type_t) | ECC 曲线类型 | [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256](#uapi_drv_cipher_pke_ecc_curve_type_t):0 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384](#uapi_drv_cipher_pke_ecc_curve_type_t):1 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512](#uapi_drv_cipher_pke_ecc_curve_type_t):2 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K](#uapi_drv_cipher_pke_ecc_curve_type_t):3 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P192R](#uapi_drv_cipher_pke_ecc_curve_type_t):4 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P224R](#uapi_drv_cipher_pke_ecc_curve_type_t):5 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256R](#uapi_drv_cipher_pke_ecc_curve_type_t):6 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P384R](#uapi_drv_cipher_pke_ecc_curve_type_t):7 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P521R](#uapi_drv_cipher_pke_ecc_curve_type_t):8 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748](#uapi_drv_cipher_pke_ecc_curve_type_t):9 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748_448](#uapi_drv_cipher_pke_ecc_curve_type_t):10 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC8032](#uapi_drv_cipher_pke_ecc_curve_type_t):11 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_SM2](#uapi_drv_cipher_pke_ecc_curve_type_t):12 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_MAX](#uapi_drv_cipher_pke_ecc_curve_type_t):13 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_INVALID](#uapi_drv_cipher_pke_ecc_curve_type_t):0xffffffff |
| input_pub_key | [uapi_drv_cipher_pke_ecc_point_t](#uapi_drv_cipher_pke_ecc_point_t) | 输入对端 ECC 公钥 | 不为NULL |
| input_priv_key | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入本地 ECC 私钥 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| output_shared_key | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出协商得到的共享密钥，由调用方分配缓冲区，接口填充数据 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 共享密钥协商成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_ECC_ECDH | 特性宏 | 支持 ECC ECDH 密钥协商功能 | y |

### uapi_drv_cipher_pke_check_dot_on_curve <a id="uapi_drv_cipher_pke_check_dot_on_curve"></a>

```c
errcode_t uapi_drv_cipher_pke_check_dot_on_curve(uapi_drv_cipher_pke_ecc_curve_type_t curve_type,
    const uapi_drv_cipher_pke_ecc_point_t *pub_key, bool *is_on_curve)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 检查输入点是否在指定 ECC 曲线上
- 输出布尔结果指示点是否在曲线上
- 支持多种 ECC 曲线类型

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| curve_type | [uapi_drv_cipher_pke_ecc_curve_type_t](#uapi_drv_cipher_pke_ecc_curve_type_t) | ECC 曲线类型 | [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256](#uapi_drv_cipher_pke_ecc_curve_type_t):0 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384](#uapi_drv_cipher_pke_ecc_curve_type_t):1 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512](#uapi_drv_cipher_pke_ecc_curve_type_t):2 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K](#uapi_drv_cipher_pke_ecc_curve_type_t):3 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P192R](#uapi_drv_cipher_pke_ecc_curve_type_t):4 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P224R](#uapi_drv_cipher_pke_ecc_curve_type_t):5 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256R](#uapi_drv_cipher_pke_ecc_curve_type_t):6 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P384R](#uapi_drv_cipher_pke_ecc_curve_type_t):7 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P521R](#uapi_drv_cipher_pke_ecc_curve_type_t):8 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748](#uapi_drv_cipher_pke_ecc_curve_type_t):9 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748_448](#uapi_drv_cipher_pke_ecc_curve_type_t):10 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC8032](#uapi_drv_cipher_pke_ecc_curve_type_t):11 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_SM2](#uapi_drv_cipher_pke_ecc_curve_type_t):12 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_MAX](#uapi_drv_cipher_pke_ecc_curve_type_t):13 / [UAPI_DRV_CIPHER_PKE_ECC_TYPE_INVALID](#uapi_drv_cipher_pke_ecc_curve_type_t):0xffffffff |
| pub_key | [uapi_drv_cipher_pke_ecc_point_t](#uapi_drv_cipher_pke_ecc_point_t) | 输入待检查的 ECC 点 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| is_on_curve | bool * | 输出检查结果，true 表示点在曲线上，false 表示不在曲线上 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 检查操作执行成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_ECC_CAL | 特性宏 | 支持 ECC 点校验功能 | y |

### uapi_drv_cipher_pke_sm2_dsa_hash <a id="uapi_drv_cipher_pke_sm2_dsa_hash"></a>

```c
errcode_t uapi_drv_cipher_pke_sm2_dsa_hash(const uapi_drv_cipher_pke_data_t *sm2_id,
    const uapi_drv_cipher_pke_ecc_point_t *pub_key,
    const uapi_drv_cipher_pke_msg_t *msg,
    uapi_drv_cipher_pke_data_t *hash)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 计算 SM2 数字签名所需的 SM3 摘要
- 输入包括 SM2 ID、公钥与待签名消息
- 输出摘要供后续 SM2 签名或验签使用

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| sm2_id | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入 SM2 用户 ID | 不为NULL |
| pub_key | [uapi_drv_cipher_pke_ecc_point_t](#uapi_drv_cipher_pke_ecc_point_t) | 输入 SM2 公钥 | 不为NULL |
| msg | [uapi_drv_cipher_pke_msg_t](#uapi_drv_cipher_pke_msg_t) | 输入待计算摘要的消息 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| hash | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出 SM3 摘要，由调用方分配缓冲区，接口填充摘要数据 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 摘要计算成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**参考案例**

- `src/middleware/utils/update/common/upg_verify.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_SM2_SIGN | 特性宏 | 支持 SM2 签名摘要计算功能 | y |
| CONFIG_PKE_SUPPORT_SM2_VERIFY | 特性宏 | 支持 SM2 验签摘要计算功能 | y |

### uapi_drv_cipher_pke_sm2_public_encrypt <a id="uapi_drv_cipher_pke_sm2_public_encrypt"></a>

```c
errcode_t uapi_drv_cipher_pke_sm2_public_encrypt(const uapi_drv_cipher_pke_ecc_point_t *pub_key,
    const uapi_drv_cipher_pke_data_t *plain_text,
    const uapi_drv_cipher_pke_data_t *cipher_text)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 使用 SM2 公钥对明文进行加密
- 输出密文到调用方提供的缓冲区
- 配合 SM2 私钥解密接口成对使用

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pub_key | [uapi_drv_cipher_pke_ecc_point_t](#uapi_drv_cipher_pke_ecc_point_t) | 输入 SM2 公钥 | 不为NULL |
| plain_text | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入待加密的明文 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| cipher_text | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出密文，由调用方分配缓冲区，接口填充密文数据 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 加密成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_SM2_CRYPTO | 特性宏 | 支持 SM2 加解密功能 | y |

### uapi_drv_cipher_pke_sm2_private_decrypt <a id="uapi_drv_cipher_pke_sm2_private_decrypt"></a>

```c
errcode_t uapi_drv_cipher_pke_sm2_private_decrypt(const uapi_drv_cipher_pke_data_t *priv_key,
    const uapi_drv_cipher_pke_data_t *cipher_text,
    const uapi_drv_cipher_pke_data_t *plain_text)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 使用 SM2 私钥对密文进行解密
- 输出明文到调用方提供的缓冲区
- 配合 SM2 公钥加密接口成对使用

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| priv_key | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入 SM2 私钥 | 不为NULL |
| cipher_text | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入待解密的密文 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| plain_text | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出明文，由调用方分配缓冲区，接口填充明文数据 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 解密成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_SM2_CRYPTO | 特性宏 | 支持 SM2 加解密功能 | y |

### uapi_drv_cipher_pke_rsa_sign <a id="uapi_drv_cipher_pke_rsa_sign"></a>

```c
errcode_t uapi_drv_cipher_pke_rsa_sign(const uapi_drv_cipher_pke_rsa_priv_key_t *priv_key,
    uapi_drv_cipher_pke_rsa_scheme_t scheme,
    uapi_drv_cipher_pke_hash_type_t hash_type,
    const uapi_drv_cipher_pke_data_t *input_hash,
    uapi_drv_cipher_pke_data_t *sign)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 使用 RSA 私钥对输入摘要进行数字签名
- 签名填充方式与摘要算法由入参指定
- 签名结果输出到调用方提供的缓冲区

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| priv_key | [uapi_drv_cipher_pke_rsa_priv_key_t](#uapi_drv_cipher_pke_rsa_priv_key_t) | 输入 RSA 私钥 | 不为NULL |
| scheme | [uapi_drv_cipher_pke_rsa_scheme_t](#uapi_drv_cipher_pke_rsa_scheme_t) | RSA 填充方式 | [UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V15](#uapi_drv_cipher_pke_rsa_scheme_t):0x00 / [UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V21](#uapi_drv_cipher_pke_rsa_scheme_t):0x01 |
| hash_type | [uapi_drv_cipher_pke_hash_type_t](#uapi_drv_cipher_pke_hash_type_t) | RSA 填充使用的摘要算法 | [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA1](#uapi_drv_cipher_pke_hash_type_t):0x00 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA224](#uapi_drv_cipher_pke_hash_type_t):0x01 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA256](#uapi_drv_cipher_pke_hash_type_t):0x02 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA384](#uapi_drv_cipher_pke_hash_type_t):0x03 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA512](#uapi_drv_cipher_pke_hash_type_t):0x04 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SM3](#uapi_drv_cipher_pke_hash_type_t):0x05 |
| input_hash | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入待签名的摘要 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| sign | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出签名结果，由调用方分配缓冲区，接口填充签名数据 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 签名生成成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_RSA | 特性宏 | 支持 RSA 签名功能 | y |

### uapi_drv_cipher_pke_rsa_verify <a id="uapi_drv_cipher_pke_rsa_verify"></a>

```c
errcode_t uapi_drv_cipher_pke_rsa_verify(const uapi_drv_cipher_pke_rsa_pub_key_t *pub_key,
    uapi_drv_cipher_pke_rsa_scheme_t scheme,
    uapi_drv_cipher_pke_hash_type_t hash_type,
    uapi_drv_cipher_pke_data_t *input_hash,
    const uapi_drv_cipher_pke_data_t *sig)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 使用 RSA 公钥对输入签名进行验签
- 验签填充方式与摘要算法由入参指定
- 验签输入包括公钥、摘要与签名值

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pub_key | [uapi_drv_cipher_pke_rsa_pub_key_t](#uapi_drv_cipher_pke_rsa_pub_key_t) | 输入 RSA 公钥 | 不为NULL |
| scheme | [uapi_drv_cipher_pke_rsa_scheme_t](#uapi_drv_cipher_pke_rsa_scheme_t) | RSA 填充方式 | [UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V15](#uapi_drv_cipher_pke_rsa_scheme_t):0x00 / [UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V21](#uapi_drv_cipher_pke_rsa_scheme_t):0x01 |
| hash_type | [uapi_drv_cipher_pke_hash_type_t](#uapi_drv_cipher_pke_hash_type_t) | RSA 填充使用的摘要算法 | [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA1](#uapi_drv_cipher_pke_hash_type_t):0x00 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA224](#uapi_drv_cipher_pke_hash_type_t):0x01 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA256](#uapi_drv_cipher_pke_hash_type_t):0x02 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA384](#uapi_drv_cipher_pke_hash_type_t):0x03 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA512](#uapi_drv_cipher_pke_hash_type_t):0x04 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SM3](#uapi_drv_cipher_pke_hash_type_t):0x05 |
| input_hash | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入待验签的摘要 | 不为NULL |
| sig | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入待验证的签名值 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 验签通过 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 验签失败或执行失败 |

**参考案例**

- `src/middleware/utils/update/common/upg_verify.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_RSA | 特性宏 | 支持 RSA 验签功能 | y |

### uapi_drv_cipher_pke_rsa_public_encrypt <a id="uapi_drv_cipher_pke_rsa_public_encrypt"></a>

```c
errcode_t uapi_drv_cipher_pke_rsa_public_encrypt(uapi_drv_cipher_pke_rsa_scheme_t scheme,
    uapi_drv_cipher_pke_hash_type_t hash_type,
    const uapi_drv_cipher_pke_rsa_pub_key_t *pub_key,
    const uapi_drv_cipher_pke_data_t *input,
    const uapi_drv_cipher_pke_data_t *label,
    uapi_drv_cipher_pke_data_t *output)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 使用 RSA 公钥对明文进行加密
- 填充方式由入参指定，hash_type 与 label 仅 OAEP (Optimal Asymmetric Encryption Padding) 填充模式时使用
- 输出密文到调用方提供的缓冲区

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| scheme | [uapi_drv_cipher_pke_rsa_scheme_t](#uapi_drv_cipher_pke_rsa_scheme_t) | RSA 填充方式 | [UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V15](#uapi_drv_cipher_pke_rsa_scheme_t):0x00 / [UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V21](#uapi_drv_cipher_pke_rsa_scheme_t):0x01 |
| hash_type | [uapi_drv_cipher_pke_hash_type_t](#uapi_drv_cipher_pke_hash_type_t) | RSA 填充使用的摘要算法，仅 OAEP 填充模式时使用此参数 | [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA1](#uapi_drv_cipher_pke_hash_type_t):0x00 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA224](#uapi_drv_cipher_pke_hash_type_t):0x01 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA256](#uapi_drv_cipher_pke_hash_type_t):0x02 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA384](#uapi_drv_cipher_pke_hash_type_t):0x03 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA512](#uapi_drv_cipher_pke_hash_type_t):0x04 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SM3](#uapi_drv_cipher_pke_hash_type_t):0x05 |
| pub_key | [uapi_drv_cipher_pke_rsa_pub_key_t](#uapi_drv_cipher_pke_rsa_pub_key_t) | 输入 RSA 公钥 | 不为NULL |
| input | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入待加密的明文 | 不为NULL |
| label | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | RSA 标签，仅 OAEP 填充模式时使用此参数 | 可为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| output | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出密文，由调用方分配缓冲区，接口填充密文数据 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 加密成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_RSA | 特性宏 | 支持 RSA 公钥加密功能 | y |

### uapi_drv_cipher_pke_rsa_private_decrypt <a id="uapi_drv_cipher_pke_rsa_private_decrypt"></a>

```c
errcode_t uapi_drv_cipher_pke_rsa_private_decrypt(uapi_drv_cipher_pke_rsa_scheme_t scheme,
    uapi_drv_cipher_pke_hash_type_t hash_type,
    const uapi_drv_cipher_pke_rsa_priv_key_t *priv_key,
    const uapi_drv_cipher_pke_data_t *input,
    const uapi_drv_cipher_pke_data_t *label,
    const uapi_drv_cipher_pke_data_t *output)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 使用 RSA 私钥对密文进行解密
- 填充方式由入参指定，hash_type 与 label 仅 OAEP 填充模式时使用
- 输出明文到调用方提供的缓冲区

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| scheme | [uapi_drv_cipher_pke_rsa_scheme_t](#uapi_drv_cipher_pke_rsa_scheme_t) | RSA 填充方式 | [UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V15](#uapi_drv_cipher_pke_rsa_scheme_t):0x00 / [UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V21](#uapi_drv_cipher_pke_rsa_scheme_t):0x01 |
| hash_type | [uapi_drv_cipher_pke_hash_type_t](#uapi_drv_cipher_pke_hash_type_t) | RSA 填充使用的摘要算法，仅 OAEP 填充模式时使用此参数 | [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA1](#uapi_drv_cipher_pke_hash_type_t):0x00 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA224](#uapi_drv_cipher_pke_hash_type_t):0x01 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA256](#uapi_drv_cipher_pke_hash_type_t):0x02 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA384](#uapi_drv_cipher_pke_hash_type_t):0x03 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA512](#uapi_drv_cipher_pke_hash_type_t):0x04 / [UAPI_DRV_CIPHER_PKE_HASH_TYPE_SM3](#uapi_drv_cipher_pke_hash_type_t):0x05 |
| priv_key | [uapi_drv_cipher_pke_rsa_priv_key_t](#uapi_drv_cipher_pke_rsa_priv_key_t) | 输入 RSA 私钥 | 不为NULL |
| input | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入待解密的密文 | 不为NULL |
| label | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | RSA 标签，仅 OAEP 填充模式时使用此参数 | 可为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| output | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出明文，由调用方分配缓冲区，接口填充明文数据 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 解密成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_RSA | 特性宏 | 支持 RSA 私钥解密功能 | y |

### uapi_drv_cipher_pke_dh_gen_key <a id="uapi_drv_cipher_pke_dh_gen_key"></a>

```c
errcode_t uapi_drv_cipher_pke_dh_gen_key(const uapi_drv_cipher_pke_data_t *g_data,
    const uapi_drv_cipher_pke_data_t *mod_n, const uapi_drv_cipher_pke_data_t *input_priv_key,
    const uapi_drv_cipher_pke_data_t *output_priv_key, const uapi_drv_cipher_pke_data_t *output_pub_key)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 生成 DH 公私钥对，或基于输入私钥推导生成公钥
- 输入私钥可为空，为空时由内部生成随机私钥
- 输出私钥与公钥长度应与模数长度相同

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| g_data | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入公开底数，该数为质数；g_data->length 不能大于 mod_n->length | 不为NULL |
| mod_n | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入公开模数，该数为质数；mod_n->length 支持 192/224/256/384/512/521/1024/2048/3072/4096 bits | 不为NULL |
| input_priv_key | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入私钥，可为空；非空时 input_priv_key->length 应与 mod_n->length 相同 | 可为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| output_priv_key | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出私钥，output_priv_key->length 应与 mod_n->length 相同 |
| output_pub_key | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出公钥，output_pub_key->length 应与 mod_n->length 相同 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 密钥生成成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_RSA | 特性宏 | 支持 DH 密钥生成功能 | y |

### uapi_drv_cipher_pke_dh_compute_key <a id="uapi_drv_cipher_pke_dh_compute_key"></a>

```c
errcode_t uapi_drv_cipher_pke_dh_compute_key(const uapi_drv_cipher_pke_data_t *mod_n,
    const uapi_drv_cipher_pke_data_t  *input_priv_key, const uapi_drv_cipher_pke_data_t  *input_pub_key,
    const uapi_drv_cipher_pke_data_t  *output_shared_key)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 基于 DH (Diffie-Hellman) 算法计算共享密钥
- 输入本地私钥与对端公钥，输出协商得到的共享密钥
- 模数为公开质数

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| mod_n | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入公开模数，该数为质数 | 不为NULL |
| input_priv_key | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入本地私钥 | 不为NULL |
| input_pub_key | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入对端公钥 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| output_shared_key | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出协商得到的共享密钥，由调用方分配缓冲区，接口填充数据 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 共享密钥计算成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_RSA | 特性宏 | 支持 DH 密钥协商功能 | y |

### uapi_drv_cipher_pke_add_mod <a id="uapi_drv_cipher_pke_add_mod"></a>

```c
errcode_t uapi_drv_cipher_pke_add_mod(const uapi_drv_cipher_pke_data_t *a, const uapi_drv_cipher_pke_data_t *b,
    const uapi_drv_cipher_pke_data_t *p, const uapi_drv_cipher_pke_data_t *c)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 执行大数模加运算，计算 c = (a + b) mod p
- 模数 p 支持多种比特长度规格
- 输出结果长度应与模数长度相同

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| a | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入第一个大数，a->length 不能大于 p->length | 不为NULL |
| b | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入第二个大数，b->length 不能大于 p->length | 不为NULL |
| p | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入模数，p->length 支持 192/224/256/384/512/521/1024/1536/2048/3072/4096 bits | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| c | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出模加结果，c->length 应与 p->length 相同 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 运算成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_BIG_NUMBER | 特性宏 | 支持大数模加运算功能 | y |

### uapi_drv_cipher_pke_sub_mod <a id="uapi_drv_cipher_pke_sub_mod"></a>

```c
errcode_t uapi_drv_cipher_pke_sub_mod(const uapi_drv_cipher_pke_data_t *a, const uapi_drv_cipher_pke_data_t *b,
    const uapi_drv_cipher_pke_data_t *p, const uapi_drv_cipher_pke_data_t *c)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 执行大数模减运算，计算 c = (a - b) mod p
- 模数 p 支持多种比特长度规格
- 输出结果长度应与模数长度相同

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| a | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入第一个大数，a->length 不能大于 p->length | 不为NULL |
| b | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入第二个大数，b->length 不能大于 p->length | 不为NULL |
| p | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入模数，p->length 支持 192/224/256/384/512/521/1024/1536/2048/3072/4096 bits | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| c | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出模减结果，c->length 应与 p->length 相同 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 运算成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_BIG_NUMBER | 特性宏 | 支持大数模减运算功能 | y |

### uapi_drv_cipher_pke_mul_mod <a id="uapi_drv_cipher_pke_mul_mod"></a>

```c
errcode_t uapi_drv_cipher_pke_mul_mod(const uapi_drv_cipher_pke_data_t *a, const uapi_drv_cipher_pke_data_t *b,
    const uapi_drv_cipher_pke_data_t *p, const uapi_drv_cipher_pke_data_t *c)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 执行大数模乘运算，计算 c = (a * b) mod p
- 模数 p 支持多种比特长度规格且模数不能为偶数
- 输出结果长度应与模数长度相同

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| a | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入第一个大数，a->length 不能大于 p->length | 不为NULL |
| b | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入第二个大数，b->length 不能大于 p->length | 不为NULL |
| p | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入模数，p->length 支持 192/256/384/512/1024/1536/2048/3072/4096 bits，且模数不能为偶数 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| c | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出模乘结果，c->length 应与 p->length 相同 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 运算成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_BIG_NUMBER | 特性宏 | 支持大数模乘运算功能 | y |

### uapi_drv_cipher_pke_inv_mod <a id="uapi_drv_cipher_pke_inv_mod"></a>

```c
errcode_t uapi_drv_cipher_pke_inv_mod(const uapi_drv_cipher_pke_data_t *a, const uapi_drv_cipher_pke_data_t *p,
    const uapi_drv_cipher_pke_data_t *c)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 执行大数模逆运算，计算 c = (a^-1) mod p
- 模数 p 支持多种比特长度规格且模数不能为偶数
- 输入 a 长度应与模数长度相同

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| a | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入大数，a->length 应与 p->length 相同 | 不为NULL |
| p | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入模数，p->length 支持 192/256/384/512/1024/1536/2048/3072/4096 bits，且模数不能为偶数 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| c | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出模逆结果，c->length 应与 p->length 相同 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 运算成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_BIG_NUMBER | 特性宏 | 支持大数模逆运算功能 | y |

### uapi_drv_cipher_pke_mod <a id="uapi_drv_cipher_pke_mod"></a>

```c
errcode_t uapi_drv_cipher_pke_mod(const uapi_drv_cipher_pke_data_t *a, const uapi_drv_cipher_pke_data_t *p,
    const uapi_drv_cipher_pke_data_t *c)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 执行大数取模运算，计算 c = a mod p
- 模数 p 支持多种比特长度规格且模数不能为偶数
- 输入 a 有效数据长度不能大于模数有效数据长度的 2 倍

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| a | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入大数，其有效数据长度不能大于 2 倍的 p->length 有效数据长度 | 不为NULL |
| p | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入模数，p->length 支持 192/256/384/512/1024/1536/2048/3072/4096 bits，且模数不能为偶数 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| c | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出取模结果，c->length 应与 p->length 相同 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 运算成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_BIG_NUMBER | 特性宏 | 支持大数取模运算功能 | y |

### uapi_drv_cipher_pke_mul <a id="uapi_drv_cipher_pke_mul"></a>

```c
errcode_t uapi_drv_cipher_pke_mul(const uapi_drv_cipher_pke_data_t *a, const uapi_drv_cipher_pke_data_t *b,
    const uapi_drv_cipher_pke_data_t *c)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 执行大数乘运算，计算 c = a * b
- 输入 a、b 数据长度均不能大于 2048 bits
- 输出结果长度不能小于 a->length + b->length

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| a | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入第一个大数，a->length 不能大于 2048 bits | 不为NULL |
| b | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入第二个大数，b->length 不能大于 2048 bits | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| c | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出大数乘结果，c->length 不能小于 a->length + b->length |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 运算成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_BIG_NUMBER | 特性宏 | 支持大数乘运算功能 | y |

### uapi_drv_cipher_pke_exp_mod <a id="uapi_drv_cipher_pke_exp_mod"></a>

```c
errcode_t uapi_drv_cipher_pke_exp_mod(const uapi_drv_cipher_pke_data_t *n, const uapi_drv_cipher_pke_data_t *k,
    const uapi_drv_cipher_pke_data_t *in, const uapi_drv_cipher_pke_data_t *out)
```

**声明头文件**

```c
#include "include/driver/security_unified/unified_cipher_pke.h"
```

**功能说明**

- 执行大数模幂运算，计算 out = (in ^ k) mod n
- 模数 n 支持多种比特长度规格且模数不能为偶数
- 指数 k 与输入数据 in 的数据长度均不能大于 4096 bits

**前置条件**

- 依赖关系：依赖 PKE 硬件引擎已就绪
- 上下文限制：需在任务上下文调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| n | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入模数，n->length 支持 192/256/384/512/1024/1536/2048/3072/4096 bits，且模数不能为偶数 | 不为NULL |
| k | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入指数，数据长度不能大于 4096 bits | 不为NULL |
| in | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输入底数数据，数据长度不能大于 4096 bits | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| out | [uapi_drv_cipher_pke_data_t](#uapi_drv_cipher_pke_data_t) | 输出模幂结果，out->length 应与 n->length 相同 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 运算成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PKE_SUPPORT_BIG_NUMBER | 特性宏 | 支持大数模幂运算功能 | y |

## Type definitions

### errcode_t <a id="typedef_errcode_t"></a> 
```c
typedef uint32_t errcode_t;
```

**使用说明**

作为本模块全部对外接口的返回值类型，表示接口执行结果。 
## Enumerations

### uapi_drv_cipher_pke_ecc_curve_type_t <a id="uapi_drv_cipher_pke_ecc_curve_type_t"></a>

```c
typedef enum {
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256 = 0,      /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P192R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P224R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P384R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P521R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748,               /* RFC 7748 - Curve25519 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748_448,           /* RFC 7748 - Curve448 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC8032,               /* RFC 8032 - ED25519 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_SM2,                   /* GMT 0003.2-2012 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_ecc_curve_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256 | 0 | RFC 5639 Brainpool P256 曲线 |
| UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384 | 1 | RFC 5639 Brainpool P384 曲线 |
| UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512 | 2 | RFC 5639 Brainpool P512 曲线 |
| UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K | 3 | NIST FIPS 186-4 P256K 曲线 |
| UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P192R | 4 | NIST FIPS 186-4 P192R 曲线 |
| UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P224R | 5 | NIST FIPS 186-4 P224R 曲线 |
| UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256R | 6 | NIST FIPS 186-4 P256R 曲线 |
| UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P384R | 7 | NIST FIPS 186-4 P384R 曲线 |
| UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P521R | 8 | NIST FIPS 186-4 P521R 曲线 |
| UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748 | 9 | RFC 7748 Curve25519 |
| UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748_448 | 10 | RFC 7748 Curve448 |
| UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC8032 | 11 | RFC 8032 ED25519 |
| UAPI_DRV_CIPHER_PKE_ECC_TYPE_SM2 | 12 | GMT 0003.2-2012 SM2 曲线 |
| UAPI_DRV_CIPHER_PKE_ECC_TYPE_MAX | 13 | 曲线类型上限 |
| UAPI_DRV_CIPHER_PKE_ECC_TYPE_INVALID | 0xffffffff | 无效曲线类型 |

### uapi_drv_cipher_pke_rsa_scheme_t <a id="uapi_drv_cipher_pke_rsa_scheme_t"></a>

```c
typedef enum {
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256 = 0,      /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P192R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P224R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECCtypedef enum {
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256 = 0,      /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P192R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P224R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P384R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P521R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748,       typedef enum {
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256 = 0,      /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P192R,            /* NIST FIPS 186-4typedef enum {
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256 = 0,      /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K,            /* NIST FIPS 186-4 P192/224/256/3typedef enum {
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256 = 0,      /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P192R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P224R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P384R,            /* Ntypedef enum {
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256 = 0,      /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_typedef enum {
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256 = 0,      /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P192R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHEtypedef enum {
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256 = 0,      /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P192R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P224R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P384R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P521R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748,               /* RFC 7748 - Curve25519 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748_448,           /* RFC 7748 - Curve448 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC8032,               /* RFC 8032 - ED25519 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_SM2,                   /* GMT 0003.2-2012 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_ecc_curve_type_t;

/**
 * @if Eng
 * @brief Padding mode of the RSA algorithm
 * @note  PKCS1_V15 is not secure, and we advise not to use it.
 * @else
 * @brief RSA算法填充方式
 * @note  PKCS1_V15不安全，不建议使用。
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V15 = 0x00,    /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V21,
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_MAX,
    UAPI_DRVtypedef enum {
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P256 = 0,      /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P384,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC5639_P512,          /* RFC 5639 - Brainpool P256/384/512 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256K,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P192R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P224R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P384R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P521R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748,               /* RFC 7748 - Curve25519 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748_448,           /* RFC 7748 - Curve448 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC8032,               /* RFC 8032 - ED25519 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_SM2,                   /* GMT 0003.2-2012 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_ecc_curve_type_t;

/**
 * @if Eng
 * @brief Padding mode of the RSA algorithm
 * @note  PKCS1_V15 is not secure, and we advise not to use it.
 * @else
 * @brief RSA算法填充方式
 * @note  PKCS1_V15不安全，不建议使用。
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V15 = 0x00,    /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V21,
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_MAX,
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_rsa_scheme_t;

/**
 * @if Eng
 * @brief Hash algorithm type used for RSA padding
 * @note  SHA1 and SHA224 is not secure, and we advise not to use it.
 * @else
 * @brief RSA填充使用的hash算法类型
 * @note  SHA1和SHA224不安全，不建议使用。
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA1 = 0x00,  /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA224,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA256,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA384,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA512,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SM3,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_hash_type_t;

/**
 * @if Eng
 * @brief Buffer security attribute for RSA input messages
 * @else
 * @brief RSA输入消息的缓冲区安全属性
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_BUF_NONSECURE = 0x00,
    UAPI_DRV_CIPHER_PKE_BUF_SECURE,
    UAPI_DRV_CIPHER_PKE_BUF_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_buffer_secure_t;

/**
 * @if Eng
 * @brief  Common PKE data structure
 * @else
 * @brief PKE通用数据结构体
 * @endif
 */
typedef struct {
    uint32_t  length;   /*!< @if Eng PKE common data buffer length.
                             @else   PKE通用数据缓冲区长度。 @endif */
    uint8_t  *data;     /*!< @if Eng PKE common data buffer.
                             @else   PKE通用数据缓冲区。 @endif */
} uapi_drv_cipher_pke_data_t;

/**
 * @if Eng
 * @brief  ECC public key structure
 * @else
 * @brief ECC公钥结构体
 * @endif
 */
typedef struct {
    uint8_t *x;    /*!< @if Eng X coordinates of the generated public key, the caller ensures it is padded with leading
                                zeros if the effective size of this key is smaller than ecc key size.
                        @else   公钥的X坐标，调用方确保如果此密钥的有效大小小于ecc密钥大小，则用前导零填充。 @endif */
    uint8_t *y;    /*!< @if Eng Y coordinates of the generated public key, the caller ensures it is padded with leading
                                zeros if the effective size of this key is smaller than ecc key size.
                        @else   公钥的Y坐标，调用方确保如果此密钥的有效大小小于ecc密钥大小，则用前导零填充。 @endif */
    uint32_t length;    /*!< @if Eng ECC public key length.
                             @else   RCC公钥长度。 @endif */
} uapi_drv_cipher_pke_ecc_point_t;

/**
 * @if Eng
 * @brief  ECC signature structure
 * @else
 * @brief ECC签名结构体
 * @endif
 */
typedef struct {
    uint8_t *r;    /*!< @if Eng ECC signature R.
                        @else   ECC签名值R。 @endif */
    uint8_t *s;    /*!< @if Eng ECC signature S.
                        @else   ECC签名值S。 @endif */
    uint32_t length;    /*!< @if Eng Length of the ECC signature.
                             @else   ECC签名数据长度。 @endif */
} uapi_drv_cipher_pke_ecc_sig_t;

/**
 * @if Eng
 * @brief  ECC input message structure
 * @else
 * @brief ECC输入消息结构体
 * @endif
 */
typedef struct {
    uint32_t  length;    /*!< @if Eng Length of the ECC input message buffer.
                              @else   ECC输入消息缓冲区长度。 @endif */
    uint8_t  *data;      /*!< @if Eng ECC input message buffer.
                             @else   ECC输入消息缓冲区。 @endif */
    uapi_drv_cipher_pke_buffer_secure_t buf_sec;
} uapi_drv_cipher_pke_msg_t;

/**
 * @if Eng
 * @brief  RSA private key structure
 * @else
 * @brief RSA私钥结构体
 * @endif
 */
typedef struct {
    uint8_t *n;          /*!< @if Eng RSA public modulus.
                              @else   RSA秘钥参数n。 @endif */
    uint8_t *e;          /*!< @if Eng public exponent.
                              @else   RSA公钥参数e。 @endif */
    uint8_t *d;          /*!< @if Eng private exponent.
                              @else   RSA私钥参数d。 @endif */
    uint8_t *p;          /*!< @if Eng 1st prime factor.
                              @else   RSA第一素数因子。 @endif */
    uint8_t *q;          /*!< @if Eng 2nd prime factor.
                              @else   RSA第二素数因子。 @endif */
    uint8_t *dp;         /*!< @if Eng D % (P - 1).
                              @else   D % (P - 1)的结果。 @endif */
    uint8_t *dq;         /*!< @if Eng D % (Q - 1).
                              @else   D % (Q - 1)的结果。 @endif */
    uint8_t *qp;         /*!< @if Eng 1 / (Q % P).
                              @else   1 / (Q % P)的结果。 @endif */
    uint16_t n_len;      /*!< @if Eng length of public modulus.
                              @else   RSA秘钥参数n的长度。 @endif */
    uint16_t e_len;      /*!< @if Eng length of public exponent.
                              @else   RSA公钥参数e的长度。 @endif */
    uint16_t d_len;      /*!< @if Eng length of private exponent.
                              @else   RSA私钥参数d的长度。 @endif */
    uint16_t p_len;      /*!< @if Eng length of 1st prime factor,should be half of u16NLen.
                              @else   RSA第一素因子的长度，应该是u16NLen的一半。 @endif */
    uint16_t q_len;      /*!< @if Eng length of 2nd prime factor,should be half of u16NLen.
                              @else   RSA第二素因子的长度，应该是u16NLen的一半。 @endif */
    uint16_t dp_len;     /*!< @if Eng length of D % (P - 1),should be half of u16NLen.
                              @else   D % (P - 1)结果的长度，应该是u16NLen的一半。 @endif */
    uint16_t dq_len;     /*!< @if Eng length of D % (Q - 1),should be half of u16NLen.
                              @else   D % (Q - 1)结果的长度，应该是u16NLen的一半。 @endif */
    uint16_t qp_len;     /*!< @if Eng length of 1 / (Q % P),should be half of u16NLen.
                              @else   1 / (Q % P)结果的长度，应该是u16NLen的一半。 @endif */
} uapi_drv_cipher_pke_rsa_priv_key_t;

/**
 * @if Eng
 * @brief  RSA public key structure.
 * @else
 * @brief RSA公钥结构体。
 * @endif
 */
typedef struct {
    uint8_t  *n;            /*!< @if Eng private exponent.
                                 @else   RSA私钥参数d。 @endif */
    uint8_t  *e;            /*!< @if Eng public exponent.
                                 @else   RSA公钥参数e。 @endif */
    uint16_t len;           /*!< @if Eng RSA public key length.
                                 @else   RSA公钥长度。 @endif */
} uapi_drv_cipher_pke_rsa_pub_key_t;se
 * @brief RSA填充使用的hash算法类型
 * @note  SHA1和SHA224不安全，不建议使用。
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA1 = 0x00,  /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA224,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA256,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA384,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA512,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SM3,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_hash_type_t;

/**
 * @if Eng
 * @brief Buffer security attribute for RSA input messages
 * @else
 * @brief RSA输入消息的缓冲区安全属性
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_BUF_NONSECURE = 0x00,
    UAPI_DRV_CIPHER_PKE_BUF_SECURE,
    UAPI_DRV_CIPHER_PKE_BUF_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_buffer_secure_t;

/**
 * @if Eng
 * @brief  Common PKE data structure
 * @else
 * @brief PKE通用数据结构体
 * @endif
 */
typedef struct {
    uint32_t  length;   /*!< @if Eng PKE common data buffer length.
                             @else   PKE通用数据缓冲区长度。 @endif */
    uint8_t  *data;     /*!< @if Eng PKE common data buffer.
                             @else   PKE通用数据缓冲区。 @endif */
} uapi_drv_cipher_pke_data_t;

/**
 * @if Eng
 * @brief  ECC public key structure
 * @else
 * @brief ECC公钥结构体
 * @endif
 */
typedef struct {
    uint8_t *x;    /*!< @if Eng X coordinates of the generated public key, the caller ensures it is padded with leading
                                zeros if the effective size of this key is smaller than ecc key size.
                        @else   公钥的X坐标，调用方确保如果此密钥的有效大小小于ecc密钥大小，则用前导零填充。 @endif */
    uint8_t *y;    /*!< @if Eng Y coordinates of the generated public key, the caller ensures it is padded with leading
                                zeros if the effective size of this key is smaller than ecc key size.
                        @else   公钥的Y坐标，调用方确保如果此密钥的有效大小小于ecc密钥大小，则用前导零填充。 @endif */
    uint32_t length;    /*!< @if Eng ECC public key length.
                             @else   RCC公钥长度。 @endif */
} uapi_drv_cipher_pke_ecc_point_t;

/**
 * @if Eng
 * @brief  ECC signature structure
 * @else
 * @brief ECC签名结构体
 * @endif
 */
typedef struct {
    uint8_t *r;    /*!< @if Eng ECC signature R.
                        @else   ECC签名值R。 @endif */
    uint8_t *s;    /*!< @if Eng ECC signature S.
                        @else   ECC签名值S。 @endif */
    uint32_t length;    /*!< @if Eng Length of the ECC signature.
                             @else   ECC签名数据长度。 @endif */
} uapi_drv_cipher_pke_ecc_sig_t;

/**
 * @if Eng
 * @brief  ECC input message structure
 * @else
 * @brief ECC输入消息结构体
 * @endif
 */
typedef struct {
    uint32_t  length;    /*!< @if Eng Length of the ECC input message buffer.
                              @else   ECC输入消息缓冲区长度。 @endif */
    uint8_t  *data;      /*!< @if Eng ECC input message buffer.
                             @else   ECC输入消息缓冲区。 @endif */
    uapi_drv_cipher_pke_buffer_secure_t buf_sec;
} uapi_drv_cipher_pke_msg_t;

/**
 * @if Eng
 * @brief  RSA private key structure
 * @else
 * @brief RSA私钥结构体
 * @endif
 */
typedef struct {
    uint8_t *n;          /*!< @if Eng RSA public modulus.
                              @else   RSA秘钥参数n。 @endif */
    uint8_t *e;          /*!< @if Eng public exponent.
                              @else   RSA公钥参数e。 @endif */
    uint8_t *d;          /*!< @if Eng private exponent.
                              @else   RSA私钥参数d。 @endif */
    uint8_t *p;          /*!< @if Eng 1st prime factor.
                              @else   RSA第一素数因子。 @endif */
    uint8_t *q;          /*!< @if Eng 2nd prime factor.
                              @else   RSA第二素数因子。 @endif */
    uint8_t *dp;         /*!< @if Eng D % (P - 1).
                              @else   D % (P - 1)的结果。 @endif */
    uint8_t *dq;         /*!< @if Eng D % (Q - 1).
                              @else   D % (Q - 1)的结果。 @endif */
    uint8_t *qp;         /*!< @if Eng 1 / (Q % P).
                              @else   1 / (Q % P)的结果。 @endif */
    uint16_t n_len;      /*!< @if Eng length of public modulus.
                              @else   RSA秘钥参数n的长度。 @endif */
    uint16_t e_len;      /*!< @if Eng length of public exponent.
                              @else   RSA公钥参数e的长度。 @endif */
    uint16_t d_len;      /*!< @if Eng length of private exponent.
                              @else   RSA私钥参数d的长度。 @endif */
    uint16_t p_len;      /*!< @if Eng length of 1st prime factor,should be half of u16NLen.
                              @else   RSA第一素因子的长度，应该是u16NLen的一半。 @endif */
    uint16_t q_len;      /*!< @if Eng length of 2nd prime factor,should be half of u16NLen.
                              @else   RSA第二素因子的长度，应该是u16NLen的一半。 @endif */
    uint16_t dp_len;     /*!< @if Eng length of D % (P - 1),should be half of u16NLen.
                              @else   D % (P - 1)结果的长度，应该是u16NLen的一半。 @endif */
    uint16_t dq_len;     /*!< @if Eng length of D % (Q - 1),should be half of u16NLen.
                              @else   D % (Q - 1)结果的长度，应该是u16NLen的一半。 @endif */
    uint16_t qp_len;     /*!< @if Eng length of 1 / (Q % P),should be half of u16NLen.
                              @else   1 / (Q % P)结果的长度，应该是u16NLen的一半。 @endif */
} uapi_drv_cipher_pke_rsa_priv_key_t;brief RSA算法填充方式
 * @note  PKCS1_V15不安全，不建议使用。
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V15 = 0x00,    /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V21,
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_MAX,
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_rsa_scheme_t;

/**
 * @if Eng
 * @brief Hash algorithm type used for RSA padding
 * @note  SHA1 and SHA224 is not secure, and we advise not to use it.
 * @else
 * @brief RSA填充使用的hash算法类型
 * @note  SHA1和SHA224不安全，不建议使用。
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA1 = 0x00,  /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA224,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA256,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA384,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA512,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SM3,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_hash_type_t;

/**
 * @if Eng
 * @brief Buffer security attribute for RSA input messages
 * @else
 * @brief RSA输入消息的缓冲区安全属性
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_BUF_NONSECURE = 0x00,
    UAPI_DRV_CIPHER_PKE_BUF_SECURE,
    UAPI_DRV_CIPHER_PKE_BUF_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_buffer_secure_t;

/**
 * @if Eng
 * @brief  Common PKE data structure
 * @else
 * @brief PKE通用数据结构体
 * @endif
 */
typedef struct {
    uint32_t  length;   /*!< @if Eng PKE common data buffer length.
                             @else   PKE通用数据缓冲区长度。 @endif */
    uint8_t  *data;     /*!< @if Eng PKE common data buffer.
                             @else   PKE通用数据缓冲区。 @endif */
} uapi_drv_cipher_pke_data_t;

/**
 * @if Eng
 * @brief  ECC public key structure
 * @else
 * @brief ECC公钥结构体
 * @endif
 */
typedef struct {
    uint8_t *x;    /*!< @if Eng X coordinates of the generated public key, the caller ensures it is padded with leading
                                zeros if the effective size of this key is smaller than ecc key size.
                        @else   公钥的X坐标，调用方确保如果此密钥的有效大小小于ecc密钥大小，则用前导零填充。 @endif */
    uint8_t *y;    /*!< @if Eng Y coordinates of the generated public key, the caller ensures it is padded with leading
                                zeros if the effective size of this key is smaller than ecc key size.
                        @else   公钥的Y坐标，调用方确保如果此密钥的有效大小小于ecc密钥大小，则用前导零填充。 @endif */
    uint32_t length;    /*!< @if Eng ECC public key length.
                             @else   RCC公钥长度。 @endif */
} uapi_drv_cipher_pke_ecc_point_t;

/**
 * @if Eng
 * @brief  ECC signature structure
 * @else
 * @brief ECC签名结构体
 * @endif
 */
typedef struct {
    uint8_t *r;    /*!< @if Eng ECC signature R.
                        @else   ECC签名值R。 @endif */
    uint8_t *s;    /*!< @if Eng ECC signature S.
                        @else   ECC签名值S。 @endif */
    uint32_t length;    /*!< @if Eng Length of the ECC signature.
                             @else   ECC签名数据长度。 @endif */
} uapi_drv_cipher_pke_ecc_sig_t;

/**
 * @if Eng
 * @brief  ECC input message structure
 * @else
 * @brief ECC输入消息结构体
 * @endif
 */
typedef struct {
    uint32_t  length;    /*!< @if Eng Length of the ECC input message buffer.
                              @else   ECC输入消息缓冲区长度。 @endif */
    uint8_t  *data;      /*!< @if Eng ECC input message buffer.
                             @else   ECC输入消息缓冲区。 @endif */
    uapi_drv_cipher_pke_buffer_secure_t buf_sec;
} uapi_drv_cipher_pke_msg_t;   UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P384R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P521R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748,               /* RFC 7748 - Curve25519 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748_448,           /* RFC 7748 - Curve448 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC8032,               /* RFC 8032 - ED25519 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_SM2,                   /* GMT 0003.2-2012 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_ecc_curve_type_t;

/**
 * @if Eng
 * @brief Padding mode of the RSA algorithm
 * @note  PKCS1_V15 is not secure, and we advise not to use it.
 * @else
 * @brief RSA算法填充方式
 * @note  PKCS1_V15不安全，不建议使用。
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V15 = 0x00,    /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V21,
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_MAX,
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_rsa_scheme_t;

/**
 * @if Eng
 * @brief Hash algorithm type used for RSA padding
 * @note  SHA1 and SHA224 is not secure, and we advise not to use it.
 * @else
 * @brief RSA填充使用的hash算法类型
 * @note  SHA1和SHA224不安全，不建议使用。
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA1 = 0x00,  /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA224,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA256,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA384,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA512,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SM3,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_hash_type_t;

/**
 * @if Eng
 * @brief Buffer security attribute for RSA input messages
 * @else
 * @brief RSA输入消息的缓冲区安全属性
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_BUF_NONSECURE = 0x00,
    UAPI_DRV_CIPHER_PKE_BUF_SECURE,
    UAPI_DRV_CIPHER_PKE_BUF_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_buffer_secure_t;

/**
 * @if Eng
 * @brief  Common PKE data structure
 * @else
 * @brief PKE通用数据结构体
 * @endif
 */
typedef struct {
    uint32_t  length;   /*!< @if Eng PKE common data buffer length.
                             @else   PKE通用数据缓冲区长度。 @endif */
    uint8_t  *data;     /*!< @if Eng PKE common data buffer.
                             @else   PKE通用数据缓冲区。 @endif */
} uapi_drv_cipher_pke_data_t;

/**
 * @if Eng
 * @brief  ECC public key structure
 * @else
 * @brief ECC公钥结构体
 * @endif
 */
typedef struct {
    uint8_t *x;    /*!< @if Eng X coordinates of the generated public key, the caller ensures it is padded with leading
                                zeros if the effective size of this key is smaller than ecc key size.
                        @else   公钥的X坐标，调用方确保如果此密钥的有效大小小于ecc密钥大小，则用前导零填充。 @endif */
    uint8_t *y;    /*!< @if Eng Y coordinates of the generated public key, the caller ensures it is padded with leading
                                zeros if the effective size of this key is smaller than ecc key size.
                        @else   公钥的Y坐标，调用方确保如果此密钥的有效大小小于ecc密钥大小，则用前导零填充。 @endif */
    uint32_t length;    /*!< @if Eng ECC public key length.
                             @else   RCC公钥长度。 @endif */
} uapi_drv_cipher_pke_ecc_point_t;

/**
 * @if Eng
 * @brief  ECC signature structure
 * @else
 * @brief ECC签名结构体
 * @endif
 */
typedef struct {
    uint8_t *r;    /*!< @if Eng ECC signature R.
                        @else   ECC签名值R。 @endif */
    uint8_t *s;    /*!< @if Eng ECC signature S.
                        @else   ECC签名值S。 @endif */
    uint32_t length;    /*!< @if Eng Length of the ECC signature.
                             @else   ECC签名数据长度。 @endif */
} uapi_drv_cipher_pke_ecc_sig_t;PKE_ECC_TYPE_RFC7748,               /* RFC 7748 - Curve25519 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748_448,           /* RFC 7748 - Curve448 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC8032,               /* RFC 8032 - ED25519 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_SM2,                   /* GMT 0003.2-2012 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_ecc_curve_type_t;

/**
 * @if Eng
 * @brief Padding mode of the RSA algorithm
 * @note  PKCS1_V15 is not secure, and we advise not to use it.
 * @else
 * @brief RSA算法填充方式
 * @note  PKCS1_V15不安全，不建议使用。
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V15 = 0x00,    /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V21,
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_MAX,
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_rsa_scheme_t;

/**
 * @if Eng
 * @brief Hash algorithm type used for RSA padding
 * @note  SHA1 and SHA224 is not secure, and we advise not to use it.
 * @else
 * @brief RSA填充使用的hash算法类型
 * @note  SHA1和SHA224不安全，不建议使用。
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA1 = 0x00,  /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA224,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA256,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA384,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA512,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SM3,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_hash_type_t;

/**
 * @if Eng
 * @brief Buffer security attribute for RSA input messages
 * @else
 * @brief RSA输入消息的缓冲区安全属性
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_BUF_NONSECURE = 0x00,
    UAPI_DRV_CIPHER_PKE_BUF_SECURE,
    UAPI_DRV_CIPHER_PKE_BUF_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_buffer_secure_t;

/**
 * @if Eng
 * @brief  Common PKE data structure
 * @else
 * @brief PKE通用数据结构体
 * @endif
 */
typedef struct {
    uint32_t  length;   /*!< @if Eng PKE common data buffer length.
                             @else   PKE通用数据缓冲区长度。 @endif */
    uint8_t  *data;     /*!< @if Eng PKE common data buffer.
                             @else   PKE通用数据缓冲区。 @endif */
} uapi_drv_cipher_pke_data_t;

/**
 * @if Eng
 * @brief  ECC public key structure
 * @else
 * @brief ECC公钥结构体
 * @endif
 */
typedef struct {
    uint8_t *x;    /*!< @if Eng X coordinates of the generated public key, the caller ensures it is padded with leading
                                zeros if the effective size of this key is smaller than ecc key size.
                        @else   公钥的X坐标，调用方确保如果此密钥的有效大小小于ecc密钥大小，则用前导零填充。 @endif */
    uint8_t *y;    /*!< @if Eng Y coordinates of the generated public key, the caller ensures it is padded with leading
                                zeros if the effective size of this key is smaller than ecc key size.
                        @else   公钥的Y坐标，调用方确保如果此密钥的有效大小小于ecc密钥大小，则用前导零填充。 @endif */
    uint32_t length;    /*!< @if Eng ECC public key length.
                             @else   RCC公钥长度。 @endif */
} uapi_drv_cipher_pke_ecc_point_t;IPS_P521R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748,               /* RFC 7748 - Curve25519 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748_448,           /* RFC 7748 - Curve448 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC8032,               /* RFC 8032 - ED25519 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_SM2,                   /* GMT 0003.2-2012 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_ecc_curve_type_t;

/**
 * @if Eng
 * @brief Padding mode of the RSA algorithm
 * @note  PKCS1_V15 is not secure, and we advise not to use it.
 * @else
 * @brief RSA算法填充方式
 * @note  PKCS1_V15不安全，不建议使用。
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V15 = 0x00,    /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V21,
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_MAX,
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_rsa_scheme_t;

/**
 * @if Eng
 * @brief Hash algorithm type used for RSA padding
 * @note  SHA1 and SHA224 is not secure, and we advise not to use it.
 * @else
 * @brief RSA填充使用的hash算法类型
 * @note  SHA1和SHA224不安全，不建议使用。
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA1 = 0x00,  /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA224,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA256,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA384,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA512,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SM3,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_hash_type_t;

/**
 * @if Eng
 * @brief Buffer security attribute for RSA input messages
 * @else
 * @brief RSA输入消息的缓冲区安全属性
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_BUF_NONSECURE = 0x00,
    UAPI_DRV_CIPHER_PKE_BUF_SECURE,
    UAPI_DRV_CIPHER_PKE_BUF_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_buffer_secure_t;

/**
 * @if Eng
 * @brief  Common PKE data structure
 * @else
 * @brief PKE通用数据结构体
 * @endif
 */
typedef struct {
    uint32_t  length;   /*!< @if Eng PKE common data buffer length.
                             @else   PKE通用数据缓冲区长度。 @endif */
    uint8_t  *data;     /*!< @if Eng PKE common data buffer.
                             @else   PKE通用数据缓冲区。 @endif */
} uapi_drv_cipher_pke_data_t;   UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P256R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P384R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_FIPS_P521R,            /* NIST FIPS 186-4 P192/224/256/384/521, suggest not to use */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748,               /* RFC 7748 - Curve25519 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC7748_448,           /* RFC 7748 - Curve448 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC8032,               /* RFC 8032 - ED25519 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_SM2,                   /* GMT 0003.2-2012 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_ecc_curve_type_t;

/**
 * @if Eng
 * @brief Padding mode of the RSA algorithm
 * @note  PKCS1_V15 is not secure, and we advise not to use it.
 * @else
 * @brief RSA算法填充方式
 * @note  PKCS1_V15不安全，不建议使用。
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V15 = 0x00,    /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V21,
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_MAX,
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_rsa_scheme_t;

/**
 * @if Eng
 * @brief Hash algorithm type used for RSA padding
 * @note  SHA1 and SHA224 is not secure, and we advise not to use it.
 * @else
 * @brief RSA填充使用的hash算法类型
 * @note  SHA1和SHA224不安全，不建议使用。
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA1 = 0x00,  /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA224,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA256,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA384,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA512,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SM3,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_hash_type_t;

/**
 * @if Eng
 * @brief Buffer security attribute for RSA input messages
 * @else
 * @brief RSA输入消息的缓冲区安全属性
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_BUF_NONSECURE = 0x00,
    UAPI_DRV_CIPHER_PKE_BUF_SECURE,
    UAPI_DRV_CIPHER_PKE_BUF_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_buffer_secure_t; - ED25519 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_SM2,                   /* GMT 0003.2-2012 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_ecc_curve_type_t;

/**
 * @if Eng
 * @brief Padding mode of the RSA algorithm
 * @note  PKCS1_V15 is not secure, and we advise not to use it.
 * @else
 * @brief RSA算法填充方式
 * @note  PKCS1_V15不安全，不建议使用。
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V15 = 0x00,    /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V21,
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_MAX,
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_rsa_scheme_t;

/**
 * @if Eng
 * @brief Hash algorithm type used for RSA padding
 * @note  SHA1 and SHA224 is not secure, and we advise not to use it.
 * @else
 * @brief RSA填充使用的hash算法类型
 * @note  SHA1和SHA224不安全，不建议使用。
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA1 = 0x00,  /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA224,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA256,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA384,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA512,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SM3,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_hash_type_t;ECC_TYPE_RFC7748_448,           /* RFC 7748 - Curve448 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_RFC8032,               /* RFC 8032 - ED25519 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_SM2,                   /* GMT 0003.2-2012 */
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_ECC_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_ecc_curve_type_t;

/**
 * @if Eng
 * @brief Padding mode of the RSA algorithm
 * @note  PKCS1_V15 is not secure, and we advise not to use it.
 * @else
 * @brief RSA算法填充方式
 * @note  PKCS1_V15不安全，不建议使用。
 * @endif
 */
typedef enum {
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V15 = 0x00,    /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V21,
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_MAX,
    UAPI_DRV_CIPHER_PKE_RSA_SCHEME_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_rsa_scheme_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V15 | 0x00 | PKCS1 V1.5 填充方式 |
| UAPI_DRV_CIPHER_PKE_RSA_SCHEME_PKCS1_V21 | 0x01 | PKCS1 V2.1 填充方式 |
| UAPI_DRV_CIPHER_PKE_RSA_SCHEME_MAX | 0x02 | 填充方式上限 |
| UAPI_DRV_CIPHER_PKE_RSA_SCHEME_INVALID | 0xffffffff | 无效填充方式 |

### uapi_drv_cipher_pke_hash_type_t <a id="uapi_drv_cipher_pke_hash_type_t"></a>

```c
typedef enum {
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA1 = 0x00,  /* not security, suggest not to use */
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA224,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA256,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA384,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA512,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_SM3,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_MAX,
    UAPI_DRV_CIPHER_PKE_HASH_TYPE_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_hash_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA1 | 0x00 | SHA1 摘要算法 |
| UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA224 | 0x01 | SHA224 摘要算法 |
| UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA256 | 0x02 | SHA256 摘要算法 |
| UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA384 | 0x03 | SHA384 摘要算法 |
| UAPI_DRV_CIPHER_PKE_HASH_TYPE_SHA512 | 0x04 | SHA512 摘要算法 |
| UAPI_DRV_CIPHER_PKE_HASH_TYPE_SM3 | 0x05 | SM3 摘要算法 |
| UAPI_DRV_CIPHER_PKE_HASH_TYPE_MAX | 0x06 | 摘要算法上限 |
| UAPI_DRV_CIPHER_PKE_HASH_TYPE_INVALID | 0xffffffff | 无效摘要算法 |

### uapi_drv_cipher_pke_buffer_secure_t <a id="uapi_drv_cipher_pke_buffer_secure_t"></a>

```c
typedef enum {
    UAPI_DRV_CIPHER_PKE_BUF_NONSECURE = 0x00,
    UAPI_DRV_CIPHER_PKE_BUF_SECURE,
    UAPI_DRV_CIPHER_PKE_BUF_INVALID = 0xffffffff,
} uapi_drv_cipher_pke_buffer_secure_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_CIPHER_PKE_BUF_NONSECURE | 0x00 | 非安全缓冲区属性 |
| UAPI_DRV_CIPHER_PKE_BUF_SECURE | 0x01 | 安全缓冲区属性 |
| UAPI_DRV_CIPHER_PKE_BUF_INVALID | 0xffffffff | 无效缓冲区属性 |

## Structures

### uapi_drv_cipher_pke_data_t <a id="uapi_drv_cipher_pke_data_t"></a>

```c
typedef struct {
    uint32_t  length;   /*!< PKE common data buffer length. */
    uint8_t  *data;     /*!< PKE common data buffer. */
} uapi_drv_cipher_pke_data_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| length | uint32_t | PKE 通用数据缓冲区长度 |
| data | uint8_t * | PKE 通用数据缓冲区 |

### uapi_drv_cipher_pke_ecc_point_t <a id="uapi_drv_cipher_pke_ecc_point_t"></a>

```c
typedef struct {
    uint8_t *x;    /*!< X coordinates of the generated public key, the caller ensures it is padded with leading
                                zeros if the effective size of this key is smaller than ecc key size. */
    uint8_t *y;    /*!< Y coordinates of the generated public key, the caller ensures it is padded with leading
                                zeros if the effective size of this key is smaller than ecc key size. */
    uint32_t length;    /*!< ECC public key length. */
} uapi_drv_cipher_pke_ecc_point_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| x | uint8_t * | 公钥的 X 坐标；当有效尺寸小于 ECC 密钥尺寸时，调用方需用前导零填充 |
| y | uint8_t * | 公钥的 Y 坐标；当有效尺寸小于 ECC 密钥尺寸时，调用方需用前导零填充 |
| length | uint32_t | ECC 公钥长度 |

### uapi_drv_cipher_pke_ecc_sig_t <a id="uapi_drv_cipher_pke_ecc_sig_t"></a>

```c
typedef struct {
    uint8_t *r;    /*!< ECC signature R. */
    uint8_t *s;    /*!< ECC signature S. */
    uint32_t length;    /*!< Length of the ECC signature. */
} uapi_drv_cipher_pke_ecc_sig_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| r | uint8_t * | ECC 签名值 R |
| s | uint8_t * | ECC 签名值 S |
| length | uint32_t | ECC 签名数据长度 |

### uapi_drv_cipher_pke_msg_t <a id="uapi_drv_cipher_pke_msg_t"></a>

```c
typedef struct {
    uint32_t  length;    /*!< Length of the ECC input message buffer. */
    uint8_t  *data;      /*!< ECC input message buffer. */
    uapi_drv_cipher_pke_buffer_secure_t buf_sec;
} uapi_drv_cipher_pke_msg_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| length | uint32_t | ECC 输入消息缓冲区长度 |
| data | uint8_t * | ECC 输入消息缓冲区 |
| buf_sec | [uapi_drv_cipher_pke_buffer_secure_t](#uapi_drv_cipher_pke_buffer_secure_t) | 缓冲区安全属性 |

### uapi_drv_cipher_pke_rsa_priv_key_t <a id="uapi_drv_cipher_pke_rsa_priv_key_t"></a>

```c
typedef struct {
    uint8_t *n;          /*!< RSA public modulus. */
    uint8_t *e;          /*!< public exponent. */
    uint8_t *d;          /*!< private exponent. */
    uint8_t *p;          /*!< 1st prime factor. */
    uint8_t *q;          /*!< 2nd prime factor. */
    uint8_t *dp;         /*!< D % (P - 1). */
    uint8_t *dq;         /*!< D % (Q - 1). */
    uint8_t *qp;         /*!< 1 / (Q % P). */
    uint16_t n_len;      /*!< length of public modulus. */
    uint16_t e_len;      /*!< length of public exponent. */
    uint16_t d_len;      /*!< length of private exponent. */
    uint16_t p_len;      /*!< length of 1st prime factor, should be half of u16NLen. */
    uint16_t q_len;      /*!< length of 2nd prime factor, should be half of u16NLen. */
    uint16_t dp_len;     /*!< length of D % (P - 1), should be half of u16NLen. */
    uint16_t dq_len;     /*!< length of D % (Q - 1), should be half of u16NLen. */
    uint16_t qp_len;     /*!< length of 1 / (Q % P), should be half of u16NLen. */
} uapi_drv_cipher_pke_rsa_priv_key_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| n | uint8_t * | RSA 公钥参数 n（模数） |
| e | uint8_t * | RSA 公钥参数 e（公钥指数） |
| d | uint8_t * | RSA 私钥参数 d（私钥指数） |
| p | uint8_t * | RSA 第一素数因子 p |
| q | uint8_t * | RSA 第二素数因子 q |
| dp | uint8_t * | D % (P - 1) 的结果 |
| dq | uint8_t * | D % (Q - 1) 的结果 |
| qp | uint8_t * | 1 / (Q % P) 的结果 |
| n_len | uint16_t | RSA 公钥参数 n 的长度 |
| e_len | uint16_t | RSA 公钥参数 e 的长度 |
| d_len | uint16_t | RSA 私钥参数 d 的长度 |
| p_len | uint16_t | RSA 第一素因子 p 的长度，应为 n_len 的一半 |
| q_len | uint16_t | RSA 第二素因子 q 的长度，应为 n_len 的一半 |
| dp_len | uint16_t | D % (P - 1) 结果的长度，应为 n_len 的一半 |
| dq_len | uint16_t | D % (Q - 1) 结果的长度，应为 n_len 的一半 |
| qp_len | uint16_t | 1 / (Q % P) 结果的长度，应为 n_len 的一半 |

### uapi_drv_cipher_pke_rsa_pub_key_t <a id="uapi_drv_cipher_pke_rsa_pub_key_t"></a>

```c
typedef struct {
    uint8_t  *n;            /*!< RSA public key length. */
    uint8_t  *e;            /*!< public exponent. */
    uint16_t len;           /*!< RSA public key length. */
} uapi_drv_cipher_pke_rsa_pub_key_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| n | uint8_t * | RSA 公钥参数 n（模数） |
| e | uint8_t * | RSA 公钥参数 e（公钥指数） |
| len | uint16_t | RSA 公钥长度 |

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```
