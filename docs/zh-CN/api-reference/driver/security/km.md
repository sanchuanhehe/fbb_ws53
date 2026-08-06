# km

security_unified KM (Key Manager) 子模块提供 Keyslot、KLAD (Key Ladder)、KDF (Key Derivation Function) 三类密钥管理能力，包括密钥槽句柄的创建与销毁、Key Ladder 通道的创建、属性配置与密钥派生下发、根密钥更新等接口。该模块通过统一的对外句柄抽象，由应用层发起调用，完成对称密钥与 HMAC (Hash-based Message Authentication Code) 密钥的安全派生与下发。

**头文件清单**

```c
#include "include/driver/security_unified/km.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_drv_km_init](#uapi_drv_km_init) | 初始化 KM 模块 |
| [uapi_drv_km_deinit](#uapi_drv_km_deinit) | 去初始化 KM 模块 |
| [uapi_drv_keyslot_create](#uapi_drv_keyslot_create) | 创建 keyslot 句柄 |
| [uapi_drv_keyslot_destroy](#uapi_drv_keyslot_destroy) | 销毁 keyslot 句柄 |
| [uapi_drv_klad_create](#uapi_drv_klad_create) | 创建 Key Ladder 通道句柄 |
| [uapi_drv_klad_destroy](#uapi_drv_klad_destroy) | 销毁 Key Ladder 通道句柄 |
| [uapi_drv_klad_attach](#uapi_drv_klad_attach) | 将 keyslot 句柄与 klad 通道关联 |
| [uapi_drv_klad_detach](#uapi_drv_klad_detach) | 将 keyslot 句柄与 klad 通道解关联 |
| [uapi_drv_klad_set_attr](#uapi_drv_klad_set_attr) | 设置 Key Ladder 通道属性 |
| [uapi_drv_klad_get_attr](#uapi_drv_klad_get_attr) | 获取 Key Ladder 通道属性 |
| [uapi_drv_klad_set_effective_key](#uapi_drv_klad_set_effective_key) | 设置硬件派生密钥参数 |
| [uapi_drv_klad_set_clear_key](#uapi_drv_klad_set_clear_key) | 设置明文密钥 |
| [uapi_drv_kdf_update](#uapi_drv_kdf_update) | 更新根密钥 |

## Functions

### uapi_drv_km_init <a id="uapi_drv_km_init"></a>

```c
errcode_t uapi_drv_km_init(void)
```

**头文件清单**

```c
#include "include/driver/security_unified/km.h"
```

**功能说明**

- 初始化 KM (Key Manager) 模块运行所需的内部资源与状态
- 完成模块底层初始化，使后续 Keyslot、KLAD (Key Ladder)、KDF (Key Derivation Function) 接口可被调用
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在应用使用任意 Keyslot / KLAD / KDF 接口之前调用
- 依赖关系：当前接口依赖 security_unified 模块底层驱动已就绪

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 初始化成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 初始化失败 |

**参考案例**

- `src/drivers/drivers/driver/security_unified/service_layer/cipher_simple.c`

### uapi_drv_km_deinit <a id="uapi_drv_km_deinit"></a>

```c
errcode_t uapi_drv_km_deinit(void)
```

**头文件清单**

```c
#include "include/driver/security_unified/km.h"
```

**功能说明**

- 去初始化 KM 模块，释放初始化阶段占用的内部资源
- 与 uapi_drv_km_init 配对使用，恢复模块至未初始化状态
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 uapi_drv_km_init 成功返回后调用
- 依赖关系：当前接口依赖 KM 模块已初始化

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 去初始化成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 去初始化失败 |

**参考案例**

- `src/drivers/drivers/driver/security_unified/service_layer/cipher_simple.c`

### uapi_drv_keyslot_create <a id="uapi_drv_keyslot_create"></a>

```c
errcode_t uapi_drv_keyslot_create(uint32_t *keyslot_handle, uapi_drv_keyslot_type_t keyslot_type)
```

**头文件清单**

```c
#include "include/driver/security_unified/km.h"
```

**功能说明**

- 按指定用途类型创建一个 keyslot 句柄，用于保存密钥
- 创建成功后通过出参返回句柄，供后续 KLAD 关联或销毁使用
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 uapi_drv_km_init 成功返回后调用
- 依赖关系：当前接口依赖 KM 模块已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| keyslot_type | [uapi_drv_keyslot_type_t](#enum_uapi_drv_keyslot_type_t) | keyslot 的用途类型 | UAPI_DRV_KEYSLOT_TYPE_MCIPHER(0) / UAPI_DRV_KEYSLOT_TYPE_HMAC(1) / UAPI_DRV_KEYSLOT_TYPE_FLASH(2) |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| keyslot_handle | uint32_t * | 创建成功的 keyslot 句柄，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | keyslot 创建成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 创建失败 |

**参考案例**

- `src/middleware/chips/ws53/nv/nv_porting/nv_crypto.c`
- `src/drivers/drivers/driver/security_unified/service_layer/cipher_simple.c`

### uapi_drv_keyslot_destroy <a id="uapi_drv_keyslot_destroy"></a>

```c
errcode_t uapi_drv_keyslot_destroy(uint32_t keyslot_handle)
```

**头文件清单**

```c
#include "include/driver/security_unified/km.h"
```

**功能说明**

- 销毁指定的 keyslot 句柄，释放其占用的通道资源
- 销毁后该句柄不再可用，需重新创建才能再次使用
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 uapi_drv_keyslot_create 成功返回后调用
- 依赖关系：当前接口依赖待销毁的 keyslot 句柄有效

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| keyslot_handle | uint32_t | 待销毁的 keyslot 通道句柄 | 由 uapi_drv_keyslot_create 返回的有效句柄 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | keyslot 销毁成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 销毁失败 |

**参考案例**

- `src/middleware/chips/ws53/nv/nv_porting/nv_crypto.c`
- `src/drivers/drivers/driver/security_unified/service_layer/cipher_simple.c`

### uapi_drv_klad_create <a id="uapi_drv_klad_create"></a>

```c
errcode_t uapi_drv_klad_create(uint32_t *klad_handle)
```

**头文件清单**

```c
#include "include/driver/security_unified/km.h"
```

**功能说明**

- 创建一个 Key Ladder 通道句柄，用于后续密钥派生与下发
- 创建成功后通过出参返回句柄
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 uapi_drv_km_init 成功返回后调用
- 依赖关系：当前接口依赖 KM 模块已初始化

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| klad_handle | uint32_t * | 创建成功的 Key Ladder 通道句柄，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | Key Ladder 通道创建成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 创建失败 |

**参考案例**

- `src/middleware/chips/ws53/nv/nv_porting/nv_crypto.c`
- `src/drivers/drivers/driver/security_unified/service_layer/cipher_simple.c`

### uapi_drv_klad_destroy <a id="uapi_drv_klad_destroy"></a>

```c
errcode_t uapi_drv_klad_destroy(uint32_t klad_handle)
```

**头文件清单**

```c
#include "include/driver/security_unified/km.h"
```

**功能说明**

- 销毁指定的 Key Ladder 通道句柄，释放其占用的通道资源
- 销毁后该句柄不再可用，需重新创建才能再次使用
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 uapi_drv_klad_create 成功返回后调用
- 依赖关系：当前接口依赖待销毁的 klad 通道句柄有效

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| klad_handle | uint32_t | 待销毁的 Key Ladder 通道句柄 | 由 uapi_drv_klad_create 返回的有效句柄 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | Key Ladder 通道销毁成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 销毁失败 |

**参考案例**

- `src/middleware/chips/ws53/nv/nv_porting/nv_crypto.c`
- `src/drivers/drivers/driver/security_unified/service_layer/cipher_simple.c`

### uapi_drv_klad_attach <a id="uapi_drv_klad_attach"></a>

```c
errcode_t uapi_drv_klad_attach(uint32_t klad_handle, uapi_drv_klad_dest_t klad_type, uint32_t keyslot_handle)
```

**头文件清单**

```c
#include "include/driver/security_unified/km.h"
```

**功能说明**

- 将指定 keyslot 句柄与 Key Ladder 通道建立关联关系
- 通过 klad_type 指定密钥送出的目标模块
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 uapi_drv_klad_create 与 uapi_drv_keyslot_create 成功返回后调用
- 依赖关系：当前接口依赖待关联的 klad 通道与 keyslot 句柄均有效

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| klad_handle | uint32_t | 要关联的 Key Ladder 通道句柄 | 由 uapi_drv_klad_create 返回的有效句柄 |
| klad_type | [uapi_drv_klad_dest_t](#enum_uapi_drv_klad_dest_t) | klad 目标模块类型 | UAPI_DRV_KLAD_DEST_MCIPHER(0) / UAPI_DRV_KLAD_DEST_HMAC(1) / UAPI_DRV_KLAD_DEST_FLASH(2) / UAPI_DRV_KLAD_DEST_NPU(3) / UAPI_DRV_KLAD_DEST_AIDSP(4) |
| keyslot_handle | uint32_t | 要关联的 keyslot 通道句柄 | 由 uapi_drv_keyslot_create 返回的有效句柄 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 关联成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 关联失败 |

**参考案例**

- `src/middleware/chips/ws53/nv/nv_porting/nv_crypto.c`
- `src/drivers/drivers/driver/security_unified/service_layer/cipher_simple.c`

### uapi_drv_klad_detach <a id="uapi_drv_klad_detach"></a>

```c
errcode_t uapi_drv_klad_detach(uint32_t klad_handle, uapi_drv_klad_dest_t klad_type, uint32_t keyslot_handle)
```

**头文件清单**

```c
#include "include/driver/security_unified/km.h"
```

**功能说明**

- 将指定 keyslot 句柄与 Key Ladder 通道解除关联关系
- 通过 klad_type 指定密钥送出的目标模块
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 uapi_drv_klad_attach 成功返回后调用
- 依赖关系：当前接口依赖待解关联的 klad 通道与 keyslot 句柄均有效

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| klad_handle | uint32_t | 要解关联的 Key Ladder 通道句柄 | 由 uapi_drv_klad_create 返回的有效句柄 |
| klad_type | [uapi_drv_klad_dest_t](#enum_uapi_drv_klad_dest_t) | klad 目标模块类型 | UAPI_DRV_KLAD_DEST_MCIPHER(0) / UAPI_DRV_KLAD_DEST_HMAC(1) / UAPI_DRV_KLAD_DEST_FLASH(2) / UAPI_DRV_KLAD_DEST_NPU(3) / UAPI_DRV_KLAD_DEST_AIDSP(4) |
| keyslot_handle | uint32_t | 要解关联的 keyslot 通道句柄 | 由 uapi_drv_keyslot_create 返回的有效句柄 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 解关联成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 解关联失败 |

**参考案例**

- `src/middleware/chips/ws53/nv/nv_porting/nv_crypto.c`

### uapi_drv_klad_set_attr <a id="uapi_drv_klad_set_attr"></a>

```c
errcode_t uapi_drv_klad_set_attr(uint32_t klad_handle, const uapi_drv_klad_attr_t *attr)
```

**头文件清单**

```c
#include "include/driver/security_unified/km.h"
```

**功能说明**

- 设置 Key Ladder 通道的配置属性，包括 Key Ladder 配置、工作密钥配置与工作密钥安全配置
- 设置完成后影响后续派生密钥的属性与安全策略
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 uapi_drv_klad_create 成功返回后调用
- 依赖关系：当前接口依赖待配置的 klad 通道句柄有效，attr 指针非空

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| klad_handle | uint32_t | Key Ladder 通道句柄 | 由 uapi_drv_klad_create 返回的有效句柄 |
| attr | const [uapi_drv_klad_attr_t](#struct_uapi_drv_klad_attr_t) * | Key Ladder 配置属性指针 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 属性设置成功 |
| ERRCODE_INVALID_PARAM:0x80000001 | 参数无效 | attr 为 NULL |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 设置失败 |

**参考案例**

- `src/middleware/chips/ws53/nv/nv_porting/nv_crypto.c`
- `src/drivers/drivers/driver/security_unified/service_layer/cipher_simple.c`

### uapi_drv_klad_get_attr <a id="uapi_drv_klad_get_attr"></a>

```c
errcode_t uapi_drv_klad_get_attr(uint32_t klad_handle, uapi_drv_klad_attr_t *attr)
```

**头文件清单**

```c
#include "include/driver/security_unified/km.h"
```

**功能说明**

- 获取 Key Ladder 通道当前配置属性，包括 Key Ladder 配置、工作密钥配置与工作密钥安全配置
- 获取结果通过出参 attr 返回
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 uapi_drv_klad_create 成功返回后调用
- 依赖关系：当前接口依赖待查询的 klad 通道句柄有效，attr 指针非空

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| klad_handle | uint32_t | Key Ladder 通道句柄 | 由 uapi_drv_klad_create 返回的有效句柄 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| attr | [uapi_drv_klad_attr_t](#struct_uapi_drv_klad_attr_t) * | 当前 Key Ladder 通道配置属性，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 属性获取成功 |
| ERRCODE_INVALID_PARAM:0x80000001 | 参数无效 | attr 为 NULL |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 获取失败 |

### uapi_drv_klad_set_effective_key <a id="uapi_drv_klad_set_effective_key"></a>

```c
errcode_t uapi_drv_klad_set_effective_key(uint32_t klad_handle, const uapi_drv_klad_effective_key_t *key)
```

**头文件清单**

```c
#include "include/driver/security_unified/km.h"
```

**功能说明**

- 设置 Key Ladder 通道硬件派生密钥参数，包括派生 HMAC 算法、主密钥类型、密钥长度、盐值与单向性配置
- 设置完成后触发硬件密钥派生并下发至目标引擎
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 uapi_drv_klad_set_attr 成功返回后调用
- 依赖关系：当前接口依赖待配置的 klad 通道句柄有效，key 指针及其 salt 字段非空

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| klad_handle | uint32_t | Key Ladder 通道句柄 | 由 uapi_drv_klad_create 返回的有效句柄 |
| key | const [uapi_drv_klad_effective_key_t](#struct_uapi_drv_klad_effective_key_t) * | 硬件派生密钥参数指针 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 硬件派生密钥设置成功 |
| ERRCODE_INVALID_PARAM:0x80000001 | 参数无效 | key 为 NULL |
| ERRCODE_FAIL:0xFFFFFFFF | 执行失败 | salt 拷贝失败 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 设置失败 |

**参考案例**

- `src/middleware/chips/ws53/nv/nv_porting/nv_crypto.c`

### uapi_drv_klad_set_clear_key <a id="uapi_drv_klad_set_clear_key"></a>

```c
errcode_t uapi_drv_klad_set_clear_key(uint32_t klad_handle, const uapi_drv_klad_clear_key_t *key)
```

**头文件清单**

```c
#include "include/driver/security_unified/km.h"
```

**功能说明**

- 设置 Key Ladder 通道的明文密钥，包括明文密钥内容、长度、奇偶属性与 HMAC 算法类型
- 设置完成后将明文密钥下发至目标引擎
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 uapi_drv_klad_set_attr 成功返回后调用
- 依赖关系：当前接口依赖待配置的 klad 通道句柄有效，key 指针及其 key 字段非空

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| klad_handle | uint32_t | Key Ladder 通道句柄 | 由 uapi_drv_klad_create 返回的有效句柄 |
| key | const [uapi_drv_klad_clear_key_t](#struct_uapi_drv_klad_clear_key_t) * | 明文密钥参数指针 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 明文密钥设置成功 |
| ERRCODE_INVALID_PARAM:0x80000001 | 参数无效 | key 为 NULL |
| ERRCODE_FAIL:0xFFFFFFFF | 执行失败 | 明文密钥拷贝失败 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 设置失败 |

**参考案例**

- `src/drivers/drivers/driver/security_unified/service_layer/cipher_simple.c`

### uapi_drv_kdf_update <a id="uapi_drv_kdf_update"></a>

```c
errcode_t uapi_drv_kdf_update(uapi_drv_kdf_otp_key_t otp_key, uapi_drv_kdf_update_alg_t alg)
```

**头文件清单**

```c
#include "include/driver/security_unified/km.h"
```

**功能说明**

- 更新指定的 OTP (One-Time Programmable) 根密钥
- 通过 alg 指定更新所使用的对称算法
- 返回执行结果状态码

**前置条件**

- 调用时序约束：当前接口必须在 uapi_drv_km_init 成功返回后调用
- 依赖关系：当前接口依赖 KM 模块已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| otp_key | [uapi_drv_kdf_otp_key_t](#enum_uapi_drv_kdf_otp_key_t) | 要更新的 OTP 根密钥类型 | UAPI_DRV_KDF_OTP_KEY_MRK1(0) / UAPI_DRV_KDF_OTP_KEY_MRK0(1) / UAPI_DRV_KDF_OTP_KEY_RUSK(2) / UAPI_DRV_KDF_OTP_KEY_USK(3) |
| alg | [uapi_drv_kdf_update_alg_t](#enum_uapi_drv_kdf_update_alg_t) | 更新时使用的对称算法类型 | UAPI_DRV_KDF_UPDATE_ALG_AES(0) / UAPI_DRV_KDF_UPDATE_ALG_SM4(1) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 根密钥更新成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 更新失败 |

## Type definitions

### typedef_errcode_t <a id="typedef_errcode_t"></a>

```c
// errcode_t 定义于 include/errcode.h，为错误码枚举类型别名
typedef uint32_t errcode_t;
```

**使用说明**

本模块全部 13 个对外接口的返回值类型均为 errcode_t，表示接口执行结果状态码。 
## Enumerations

### enum_uapi_drv_keyslot_type_t <a id="enum_uapi_drv_keyslot_type_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    UAPI_DRV_KEYSLOT_TYPE_MCIPHER = 0,
    UAPI_DRV_KEYSLOT_TYPE_HMAC,
    UAPI_DRV_KEYSLOT_TYPE_FLASH,
} uapi_drv_keyslot_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_KEYSLOT_TYPE_MCIPHER | 0 | 对称加解密密钥槽 |
| UAPI_DRV_KEYSLOT_TYPE_HMAC | 1 | HMAC 密钥槽 |
| UAPI_DRV_KEYSLOT_TYPE_FLASH | 2 | Flash 在线解密密钥槽 |

### enum_uapi_drv_kdf_otp_key_t <a id="enum_uapi_drv_kdf_otp_key_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    UAPI_DRV_KDF_OTP_KEY_MRK1 = 0,
    UAPI_DRV_KDF_OTP_KEY_MRK0,
    UAPI_DRV_KDF_OTP_KEY_RUSK,
    UAPI_DRV_KDF_OTP_KEY_USK
} uapi_drv_kdf_otp_key_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_KDF_OTP_KEY_MRK1 | 0 | 主根密钥 1 |
| UAPI_DRV_KDF_OTP_KEY_MRK0 | 1 | 主根密钥 0 |
| UAPI_DRV_KDF_OTP_KEY_RUSK | 2 | 根用户会话密钥 |
| UAPI_DRV_KDF_OTP_KEY_USK | 3 | 用户会话密钥 |

### enum_uapi_drv_kdf_update_alg_t <a id="enum_uapi_drv_kdf_update_alg_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    UAPI_DRV_KDF_UPDATE_ALG_AES = 0,
    UAPI_DRV_KDF_UPDATE_ALG_SM4
} uapi_drv_kdf_update_alg_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_KDF_UPDATE_ALG_AES | 0 | KDF 密钥派生使用 AES 对称算法 |
| UAPI_DRV_KDF_UPDATE_ALG_SM4 | 1 | KDF 密钥派生使用 SM4 对称算法 |

### enum_uapi_drv_kdf_hard_key_type_t <a id="enum_uapi_drv_kdf_hard_key_type_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    UAPI_DRV_KDF_HARD_KEY_TYPE_SBRK0  = 0x03000000,
    UAPI_DRV_KDF_HARD_KEY_TYPE_SBRK1,
    UAPI_DRV_KDF_HARD_KEY_TYPE_SBRK2,
    UAPI_DRV_KDF_HARD_KEY_TYPE_ABRK0,
    UAPI_DRV_KDF_HARD_KEY_TYPE_ABRK1,
    UAPI_DRV_KDF_HARD_KEY_TYPE_ABRK2,
    UAPI_DRV_KDF_HARD_KEY_TYPE_DRK0,
    UAPI_DRV_KDF_HARD_KEY_TYPE_DRK1,
    UAPI_DRV_KDF_HARD_KEY_TYPE_RDRK0,
    UAPI_DRV_KDF_HARD_KEY_TYPE_RDRK1,
    UAPI_DRV_KDF_HARD_KEY_TYPE_PSK,
    UAPI_DRV_KDF_HARD_KEY_TYPE_FDRK0,
    UAPI_DRV_KDF_HARD_KEY_TYPE_ODRK0,
    UAPI_DRV_KDF_HARD_KEY_TYPE_ODRK1,
    UAPI_DRV_KDF_HARD_KEY_TYPE_OARK0,
    UAPI_DRV_KDF_HARD_KEY_TYPE_MDRK0,
    UAPI_DRV_KDF_HARD_KEY_TYPE_MDRK1,
    UAPI_DRV_KDF_HARD_KEY_TYPE_MDRK2,
    UAPI_DRV_KDF_HARD_KEY_TYPE_MDRK3,

    UAPI_DRV_KDF_HARD_KEY_TYPE_ABRK_REE,
    UAPI_DRV_KDF_HARD_KEY_TYPE_ABRK_TEE,
    UAPI_DRV_KDF_HARD_KEY_TYPE_RDRK_REE,
    UAPI_DRV_KDF_HARD_KEY_TYPE_RDRK_TEE,
} uapi_drv_kdf_hard_key_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_KDF_HARD_KEY_TYPE_SBRK0 | 0x03000000 | 静态启动根密钥 0 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_SBRK1 | 0x03000001 | 静态启动根密钥 1 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_SBRK2 | 0x03000002 | 静态启动根密钥 2 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_ABRK0 | 0x03000003 | 动态启动根密钥 0 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_ABRK1 | 0x03000004 | 动态启动根密钥 1 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_ABRK2 | 0x03000005 | 动态启动根密钥 2 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_DRK0 | 0x03000006 | 设备根密钥 0 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_DRK1 | 0x03000007 | 设备根密钥 1 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_RDRK0 | 0x03000008 | REE 设备根密钥 0 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_RDRK1 | 0x03000009 | REE 设备根密钥 1 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_PSK | 0x0300000A | 预共享密钥 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_FDRK0 | 0x0300000B | Flash 设备根密钥 0 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_ODRK0 | 0x0300000C | OTP 设备根密钥 0 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_ODRK1 | 0x0300000D | OTP 设备根密钥 1 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_OARK0 | 0x0300000E | OTP 鉴权根密钥 0 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_MDRK0 | 0x0300000F | 多媒体设备根密钥 0 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_MDRK1 | 0x03000010 | 多媒体设备根密钥 1 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_MDRK2 | 0x03000011 | 多媒体设备根密钥 2 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_MDRK3 | 0x03000012 | 多媒体设备根密钥 3 |
| UAPI_DRV_KDF_HARD_KEY_TYPE_ABRK_REE | 0x03000013 | 动态启动根密钥 REE |
| UAPI_DRV_KDF_HARD_KEY_TYPE_ABRK_TEE | 0x03000014 | 动态启动根密钥 TEE |
| UAPI_DRV_KDF_HARD_KEY_TYPE_RDRK_REE | 0x03000015 | REE 设备根密钥 REE |
| UAPI_DRV_KDF_HARD_KEY_TYPE_RDRK_TEE | 0x03000016 | REE 设备根密钥 TEE |

### enum_uapi_drv_kdf_hard_alg_t <a id="enum_uapi_drv_kdf_hard_alg_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    UAPI_DRV_KDF_HARD_ALG_SHA256 = 0,
    UAPI_DRV_KDF_HARD_ALG_SM3,
    UAPI_DRV_KDF_HARD_ALG_MAX
} uapi_drv_kdf_hard_alg_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_KDF_HARD_ALG_SHA256 | 0 | 硬件 PBKDF2 算法使用 SHA256 |
| UAPI_DRV_KDF_HARD_ALG_SM3 | 1 | 硬件 PBKDF2 算法使用 SM3 |
| UAPI_DRV_KDF_HARD_ALG_MAX | 2 | 算法类型上限，无效值 |

### enum_uapi_drv_kdf_master_key_type <a id="enum_uapi_drv_kdf_master_key_type"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    UAPI_DRV_MRK0 = 0,
    UAPI_DRV_MRK1,
} uapi_drv_kdf_master_key_type;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_MRK0 | 0 | 主根密钥 0 |
| UAPI_DRV_MRK1 | 1 | 主根密钥 1 |

### enum_uapi_drv_klad_engine_t <a id="enum_uapi_drv_klad_engine_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    UAPI_DRV_KLAD_ENGINE_AES = 0x20,
    UAPI_DRV_KLAD_ENGINE_LAE = 0x40,
    UAPI_DRV_KLAD_ENGINE_SM4 = 0x50,
    UAPI_DRV_KLAD_ENGINE_TDES = 0x70,
    UAPI_DRV_KLAD_ENGINE_SHA1_HMAC = 0xA0,
    UAPI_DRV_KLAD_ENGINE_SHA2_HMAC = 0xA1,
    UAPI_DRV_KLAD_ENGINE_SM3_HMAC = 0xA2,
    UAPI_DRV_KLAD_ENGINE_MAX
} uapi_drv_klad_engine_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_KLAD_ENGINE_AES | 0x20 | AES 算法引擎 |
| UAPI_DRV_KLAD_ENGINE_LAE | 0x40 | LAE 算法引擎 |
| UAPI_DRV_KLAD_ENGINE_SM4 | 0x50 | SM4 算法引擎 |
| UAPI_DRV_KLAD_ENGINE_TDES | 0x70 | 三重 DES (Triple Data Encryption Standard) 算法引擎 |
| UAPI_DRV_KLAD_ENGINE_SHA1_HMAC | 0xA0 | SHA1 HMAC 算法引擎 |
| UAPI_DRV_KLAD_ENGINE_SHA2_HMAC | 0xA1 | SHA2 HMAC 算法引擎 |
| UAPI_DRV_KLAD_ENGINE_SM3_HMAC | 0xA2 | SM3 HMAC 算法引擎 |
| UAPI_DRV_KLAD_ENGINE_MAX | 0xA3 | 引擎类型上限，无效值 |

### enum_uapi_drv_klad_dest_t <a id="enum_uapi_drv_klad_dest_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    UAPI_DRV_KLAD_DEST_MCIPHER = 0,
    UAPI_DRV_KLAD_DEST_HMAC,
    UAPI_DRV_KLAD_DEST_FLASH,
    UAPI_DRV_KLAD_DEST_NPU,
    UAPI_DRV_KLAD_DEST_AIDSP,
    UAPI_DRV_KLAD_DEST_MAX,
} uapi_drv_klad_dest_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_KLAD_DEST_MCIPHER | 0 | 目标为对称加解密模块 |
| UAPI_DRV_KLAD_DEST_HMAC | 1 | 目标为 HMAC 模块 |
| UAPI_DRV_KLAD_DEST_FLASH | 2 | 目标为 Flash 在线解密模块 |
| UAPI_DRV_KLAD_DEST_NPU | 3 | 目标为 NPU 模块 |
| UAPI_DRV_KLAD_DEST_AIDSP | 4 | 目标为 AIDSP 模块 |
| UAPI_DRV_KLAD_DEST_MAX | 5 | 目标模块类型上限，无效值 |

### enum_uapi_drv_klad_flash_key_type_t <a id="enum_uapi_drv_klad_flash_key_type_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    UAPI_DRV_KLAD_FLASH_KEY_TYPE_REE_DEC = 0x00,  /* REE flash online decryption key */
    UAPI_DRV_KLAD_FLASH_KEY_TYPE_TEE_DEC,         /* TEE flash online decryption key */
    UAPI_DRV_KLAD_FLASH_KEY_TYPE_TEE_AUT,         /* TEE flash online authentication key */
    UAPI_DRV_KLAD_FLASH_KEY_TYPE_INVALID,
} uapi_drv_klad_flash_key_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_KLAD_FLASH_KEY_TYPE_REE_DEC | 0x00 | REE Flash 在线解密密钥 |
| UAPI_DRV_KLAD_FLASH_KEY_TYPE_TEE_DEC | 0x01 | TEE Flash 在线解密密钥 |
| UAPI_DRV_KLAD_FLASH_KEY_TYPE_TEE_AUT | 0x02 | TEE Flash 在线鉴权密钥 |
| UAPI_DRV_KLAD_FLASH_KEY_TYPE_INVALID | 0x03 | 无效 Flash 密钥类型 |

### enum_uapi_drv_klad_key_size_t <a id="enum_uapi_drv_klad_key_size_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    UAPI_DRV_KLAD_KEY_SIZE_128BIT,
    UAPI_DRV_KLAD_KEY_SIZE_192BIT,
    UAPI_DRV_KLAD_KEY_SIZE_256BIT,
    UAPI_DRV_KLAD_KEY_SIZE_INVALID = 0xffffffff
} uapi_drv_klad_key_size_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_KLAD_KEY_SIZE_128BIT | 0 | 128 位对称密钥 |
| UAPI_DRV_KLAD_KEY_SIZE_192BIT | 1 | 192 位对称密钥 |
| UAPI_DRV_KLAD_KEY_SIZE_256BIT | 2 | 256 位对称密钥 |
| UAPI_DRV_KLAD_KEY_SIZE_INVALID | 0xFFFFFFFF | 无效密钥长度 |

### enum_uapi_drv_klad_hmac_type_t <a id="enum_uapi_drv_klad_hmac_type_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    UAPI_DRV_KLAD_HMAC_TYPE_SHA1 = 0x20,
    UAPI_DRV_KLAD_HMAC_TYPE_SHA224,
    UAPI_DRV_KLAD_HMAC_TYPE_SHA256,
    UAPI_DRV_KLAD_HMAC_TYPE_SHA384,
    UAPI_DRV_KLAD_HMAC_TYPE_SHA512,
    UAPI_DRV_KLAD_HMAC_TYPE_SM3 = 0x30,
    UAPI_DRV_KLAD_HMAC_TYPE_MAX,
    UAPI_DRV_KLAD_HMAC_TYPE_INVALID = 0xffffffff,
} uapi_drv_klad_hmac_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UAPI_DRV_KLAD_HMAC_TYPE_SHA1 | 0x20 | HMAC 使用 SHA1 算法 |
| UAPI_DRV_KLAD_HMAC_TYPE_SHA224 | 0x21 | HMAC 使用 SHA224 算法 |
| UAPI_DRV_KLAD_HMAC_TYPE_SHA256 | 0x22 | HMAC 使用 SHA256 算法 |
| UAPI_DRV_KLAD_HMAC_TYPE_SHA384 | 0x23 | HMAC 使用 SHA384 算法 |
| UAPI_DRV_KLAD_HMAC_TYPE_SHA512 | 0x24 | HMAC 使用 SHA512 算法 |
| UAPI_DRV_KLAD_HMAC_TYPE_SM3 | 0x30 | HMAC 使用 SM3 算法 |
| UAPI_DRV_KLAD_HMAC_TYPE_MAX | 0x31 | 算法类型上限，无效值 |
| UAPI_DRV_KLAD_HMAC_TYPE_INVALID | 0xFFFFFFFF | 无效 HMAC 算法类型 |

## Structures

### struct_uapi_drv_klad_clear_key_t <a id="struct_uapi_drv_klad_clear_key_t"></a>

```c
// 源码原始定义，保留注释
typedef struct {
    uint8_t *key;     /*!< 明文key内容。 */
    uint32_t key_length;  /*!< 明文key长度，单位为字节。
                                对于对称算法，只能是16/24/32；
                                对于HMAC-SH1/SHA224/SHA256/SM3，长度不超过64；
                                对于HMAC-SHA384/SHA512，长度不超过128。*/
    bool key_parity; /*!< key的奇偶属性。当目标为对称算法引擎且key_length为16时生效。 */
    uapi_drv_klad_hmac_type_t hmac_type; /*!< hmac 算法。当目标为HMAC算法引擎时生效。 */
} uapi_drv_klad_clear_key_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| key | uint8_t * | 明文密钥内容指针，对称算法仅可取 16 / 24 / 32 字节；HMAC-SHA1/SHA224/SHA256/SM3 不超过 64；HMAC-SHA384/SHA512 不超过 128 |
| key_length | uint32_t | 明文密钥长度，单位为字节 |
| key_parity | bool | 密钥奇偶属性，当目标为对称算法引擎且 key_length 为 16 时生效 |
| hmac_type | uapi_drv_klad_hmac_type_t | HMAC 算法类型，仅当目标为 HMAC 算法引擎时生效 |

### struct_uapi_drv_klad_config_t <a id="struct_uapi_drv_klad_config_t"></a>

```c
// 源码原始定义，保留注释
typedef struct {
    uapi_drv_kdf_hard_key_type_t rootkey_type;     /*!< 要生成的根密钥的类型。 */
} uapi_drv_klad_config_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| rootkey_type | uapi_drv_kdf_hard_key_type_t | 要生成的根密钥类型，对硬件密钥有效 |

### struct_uapi_drv_klad_key_config_t <a id="struct_uapi_drv_klad_key_config_t"></a>

```c
// 源码原始定义，保留注释
typedef struct {
    uapi_drv_klad_engine_t engine;  /*!< 工作密钥可用于加密引擎的哪种算法。 */
    bool decrypt_support;    /*!< 工作密钥可用于解密。 */
    bool encrypt_support;    /*!< 工作密钥可用于加密。 */
} uapi_drv_klad_key_config_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| engine | uapi_drv_klad_engine_t | 工作密钥适用的加密引擎算法 |
| decrypt_support | bool | 工作密钥是否可用于解密 |
| encrypt_support | bool | 工作密钥是否可用于加密 |

### struct_uapi_drv_klad_key_secure_config_t <a id="struct_uapi_drv_klad_key_secure_config_t"></a>

```c
// 源码原始定义，保留注释
typedef struct {
    bool key_sec;    /*!< 安全密钥只能由TEE CPU和AIDSP锁定的对称通道或哈希通道使用。 */
    bool master_only_enable; /*!< 只有与Keylader相同的CPU锁定的密码或哈希通道才能使用此密钥，当TEE CPU或AIDSP时生效。 */
    bool dest_buf_sec_support;   /*!< 目标引擎的目标缓冲区可以是安全的。 */
    bool dest_buf_non_sec_support; /*!< 目标引擎的目标缓冲区可以是非安全的。 */
    bool src_buf_sec_support;      /*!< 目标引擎的源缓冲区可以是安全的。 */
    bool src_buf_non_sec_support;  /*!< 目标引擎的源缓冲区可以是非安全的。 */
} uapi_drv_klad_key_secure_config_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| key_sec | bool | 是否为安全密钥，安全密钥只能由 TEE CPU 与 AIDSP 锁定的对称通道或哈希通道使用 |
| master_only_enable | bool | 是否仅允许与 Key Ladder 相同 CPU 锁定的密码或哈希通道使用该密钥，仅对 TEE CPU 或 AIDSP 生效 |
| dest_buf_sec_support | bool | 目标引擎的目标缓冲区是否可为安全 |
| dest_buf_non_sec_support | bool | 目标引擎的目标缓冲区是否可为非安全 |
| src_buf_sec_support | bool | 目标引擎的源缓冲区是否可为安全 |
| src_buf_non_sec_support | bool | 目标引擎的源缓冲区是否可为非安全 |

### struct_uapi_drv_klad_attr_t <a id="struct_uapi_drv_klad_attr_t"></a>

```c
// 源码原始定义，保留注释
typedef struct {
    uapi_drv_klad_config_t klad_cfg;    /*!< KeyLader配置，对硬件密钥有效。 */
    uapi_drv_klad_key_config_t key_cfg; /*!< 工作密钥配置。 */
    uapi_drv_klad_key_secure_config_t key_sec_cfg;  /*!< 工作密钥安全配置。 */
    uint32_t rkp_sw_cfg;                /*!< NPU模块使用，其他模块不需要配置。 */
} uapi_drv_klad_attr_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| klad_cfg | uapi_drv_klad_config_t | Key Ladder 配置，对硬件密钥有效 |
| key_cfg | uapi_drv_klad_key_config_t | 工作密钥配置 |
| key_sec_cfg | uapi_drv_klad_key_secure_config_t | 工作密钥安全配置 |
| rkp_sw_cfg | uint32_t | NPU 模块使用的软件配置，其他模块不需要配置 |

### struct_uapi_drv_klad_effective_key_t <a id="struct_uapi_drv_klad_effective_key_t"></a>

```c
// 源码原始定义，保留注释
typedef struct {
    uapi_drv_kdf_hard_alg_t kdf_hard_alg;   /*!< key派生时使用的hmac算法。 */
    uapi_drv_kdf_master_key_type master_key_type;
    bool key_parity; /*!< key的奇偶属性。当目标为对称算法引擎且key_length为16时生效。 */
    uapi_drv_klad_key_size_t key_size;  /*!< 需要派生的key的长度。 */
    uint8_t *salt;    /*!< 盐值内容。作为用户输入材料参与密钥派生，盐值不同，最终的工作密钥也不同。 */
    uint32_t salt_length; /*!< 盐值长度，单位是字节。只能为28。 */
    bool oneway; /*!< 密钥派生的单一性，默认为0。如果设置为1，即使使用相同的密钥派生材料也无法派生出相同的密钥。 */
} uapi_drv_klad_effective_key_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| kdf_hard_alg | uapi_drv_kdf_hard_alg_t | 密钥派生使用的 HMAC 算法 |
| master_key_type | uapi_drv_kdf_master_key_type | 主密钥类型 |
| key_parity | bool | 密钥奇偶属性，当目标为对称算法引擎且 key_length 为 16 时生效 |
| key_size | uapi_drv_klad_key_size_t | 需要派生的密钥长度 |
| salt | uint8_t * | 盐值内容指针，作为用户输入材料参与密钥派生，盐值不同最终工作密钥不同 |
| salt_length | uint32_t | 盐值长度，单位为字节，只能为 28 |
| oneway | bool | 密钥派生单向性，默认为 0；设置为 1 时即使使用相同派生材料也无法派生出相同密钥 |

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a> [SDK公共共享宏]

```c
#define ERRCODE_SUCC                                        0UL
```
