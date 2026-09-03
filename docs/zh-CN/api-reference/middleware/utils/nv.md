# NV

NV（Non-Volatile storage）提供基于 key-value 的非易失性数据存储能力，支持按 key ID 写入、读取、备份与恢复 NV 数据项，可配置加密、永久、不可升级等属性，并支持 NV 键值变更通知回调。模块源自 `include/middleware/utils/nv.h`。

**模块公共头文件**

```c
#include "include/middleware/utils/nv.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_nv_init](#uapi_nv_init) | 初始化 NV 模块，使用 NV 功能前必须调用 |
| [uapi_nv_write](#uapi_nv_write) | 写入 NV 数据项，默认属性为 Normal 且无回调 |
| [uapi_nv_write_with_attr](#uapi_nv_write_with_attr) | 写入 NV 数据项，并配置属性及写入完成回调函数 |
| [uapi_nv_read](#uapi_nv_read) | 读取指定 key ID 对应的 NV 数据项 |
| [uapi_nv_read_with_attr](#uapi_nv_read_with_attr) | 读取指定 key ID 对应的 NV 数据项，同时获取 key 的属性值 |
| [uapi_nv_get_store_status](#uapi_nv_get_store_status) | 获取当前核 NV 存储的空间使用状态 |
| [uapi_nv_backup](#uapi_nv_backup) | 按 NV 区域备份标志执行 NV 数据备份 |
| [uapi_nv_set_restore_mode_all](#uapi_nv_set_restore_mode_all) | 设置 NV 全量恢复标志 |
| [uapi_nv_set_restore_mode_partitial](#uapi_nv_set_restore_mode_partitial) | 设置 NV 部分区域恢复标志 |
| [uapi_nv_flush](#uapi_nv_flush) | 将 RAM 中的 NV 数据同步刷写到 flash |
| [uapi_nv_register_change_notify_proc](#uapi_nv_register_change_notify_proc) | 注册 NV 键值变更通知回调函数 |

## Functions

### uapi_nv_init <a id="uapi_nv_init"></a>

```c
void uapi_nv_init(void)
```

**声明头文件**

```c
#include "include/middleware/utils/nv.h"
```

**功能说明**

- 初始化 NV 模块，为后续 NV 读写、备份、恢复等接口提供运行环境。

**前置条件**

- 调用时序约束：必须在 NV 模块其它对外接口（如 `uapi_nv_write`、`uapi_nv_read`）之前调用。
- 依赖关系：依赖底层 flash 与 NV 直接控制初始化逻辑已就绪。

**参考案例**

- `src/application/ws53/ws53_application/main.c`

### uapi_nv_write <a id="uapi_nv_write"></a>

```c
errcode_t uapi_nv_write(uint16_t key, const uint8_t *kvalue, uint16_t kvalue_length)
```

**声明头文件**

```c
#include "include/middleware/utils/nv.h"
```

**功能说明**

- 写入 NV 数据项，使用默认属性 Normal，且不注册写入完成回调函数。
- 通过 key ID 索引关联待写入的 kvalue 数据。
- 写入完成后触发错误码上报（当 `CONFIG_ERRCODE_SUPPORT_REPORT` 开启时）。

**前置条件**

- 调用时序约束：必须在 `uapi_nv_init` 成功返回后调用。
- 依赖关系：依赖 flash 存储介质可用，底层 NV 写入逻辑就绪。
- 上下文限制：禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| key | uint16_t | 要写入的 NV 项的 key ID，用于索引 | KEY_ID_REGION0(1, 0x1000) ~ KEY_ID_REGION15(0xF000, 0xFFFF) 区域内合法 key ID |
| kvalue | const uint8_t * | 指向待写入 NV 项值的指针 | 不为NULL |
| kvalue_length | uint16_t | 写入数据的长度，单位字节 | 大于 0，普通 NV 不超过 NV_NORMAL_KVALUE_MAX_LEN(4060)，加密 NV 不超过 NV_ENCRYPTED_KVALUE_MAX_LEN(4032) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | NV 数据项写入成功 |
| ERRCODE_NV_INVALID_PARAMS：0x80003083 | 参数无效 | kvalue 为 NULL 或 kvalue_length 为 0 |
| ERRCODE_NV_ILLEGAL_OPERATION：0x80003088 | 非法操作 | 当前未支持加密但配置了加密属性 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_ERRCODE_SUPPORT_REPORT | 特性宏 | 支持错误码上报分支（分支级，dfx Kconfig 声明） | n |

### uapi_nv_write_with_attr <a id="uapi_nv_write_with_attr"></a>

```c
errcode_t uapi_nv_write_with_attr(uint16_t key, const uint8_t *kvalue, uint16_t kvalue_length, nv_key_attr_t *attr,
                                  nv_storage_completed_callback func)
```

**声明头文件**

```c
#include "include/middleware/utils/nv.h"
```

**功能说明**

- 写入 NV 数据项，并按业务需求配置 key 的存储属性。
- 支持注册写入完成回调函数，在 kvalue 写入 flash 后被调用。
- 加密属性与永久属性不可修改，永久属性 key 的 kvalue 不可修改。

**前置条件**

- 调用时序约束：必须在 `uapi_nv_init` 成功返回后调用。
- 依赖关系：依赖 flash 存储介质可用，底层 NV 写入逻辑就绪。
- 上下文限制：禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| key | uint16_t | 要写入的 NV 项的 key ID，用于索引 | KEY_ID_REGION0(1, 0x1000) ~ KEY_ID_REGION15(0xF000, 0xFFFF) 区域内合法 key ID |
| kvalue | const uint8_t * | 指向待写入 NV 项值的指针 | 不为NULL |
| kvalue_length | uint16_t | 写入数据的长度，单位字节 | 大于 0，普通 NV 不超过 NV_NORMAL_KVALUE_MAX_LEN(4060)，加密 NV 不超过 NV_ENCRYPTED_KVALUE_MAX_LEN(4032) |
| attr | [nv_key_attr_t](#struct_nv_key_attr_t) * | 指向 NV 项属性配置的指针，传入 NULL 表示使用默认属性 Normal | NULL 或合法属性结构指针 |
| func | [nv_storage_completed_callback](#typedef_nv_storage_completed_callback) | kvalue 写入 flash 完成后调用的回调函数，传入 NULL 表示不注册回调 | NULL 或合法回调函数指针 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | NV 数据项写入成功 |
| ERRCODE_NV_INVALID_PARAMS：0x80003083 | 参数无效 | kvalue 为 NULL 或 kvalue_length 为 0 |
| ERRCODE_NV_ILLEGAL_OPERATION：0x80003088 | 非法操作 | 当前未支持加密但配置了加密属性 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

**参考案例**

- `middleware/chips/ws53/factory/factory.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_NV_SUPPORT_ENCRYPT | 特性宏 | 支持加密写分支（分支级，nv_config.h 宏，默认 NV_YES） | y |

### uapi_nv_read <a id="uapi_nv_read"></a>

```c
errcode_t uapi_nv_read(uint16_t key, uint16_t kvalue_max_length, uint16_t *kvalue_length, uint8_t *kvalue)
```

**声明头文件**

```c
#include "include/middleware/utils/nv.h"
```

**功能说明**

- 读取指定 key ID 对应的 NV 数据项。
- 默认情况下不获取 NV 属性值。
- 读取完成后触发错误码上报（当 `CONFIG_ERRCODE_SUPPORT_REPORT` 开启时）。

**前置条件**

- 调用时序约束：必须在 `uapi_nv_init` 成功返回后调用。
- 依赖关系：依赖 flash 存储介质可用，目标 key ID 对应数据已写入。
- 上下文限制：禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| key | uint16_t | 要读取的 NV 项的 key ID，用于索引 | KEY_ID_REGION0(1, 0x1000) ~ KEY_ID_REGION15(0xF000, 0xFFFF) 区域内合法 key ID |
| kvalue_max_length | uint16_t | 允许拷贝到 kvalue 缓冲区的最大长度，单位字节 | 大于等于实际读取数据长度 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| kvalue_length | uint16_t * | 实际读取到的 NV 数据长度，单位字节，由调用方分配内存、函数填充 |
| kvalue | uint8_t * | 指向保存读取数据的缓冲区指针，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | NV 数据项读取成功 |
| ERRCODE_NV_INVALID_PARAMS：0x80003083 | 参数无效 | kvalue_length、kvalue 或 attr 指针为 NULL |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

**参考案例**

- `src/application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`
- `src/application/ws53/ws53_application/bt_customize.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_ERRCODE_SUPPORT_REPORT | 特性宏 | 支持错误码上报分支（分支级，dfx Kconfig 声明） | n |

### uapi_nv_read_with_attr <a id="uapi_nv_read_with_attr"></a>

```c
errcode_t uapi_nv_read_with_attr(uint16_t key, uint16_t kvalue_max_length, uint16_t *kvalue_length, uint8_t *kvalue,
                                 nv_key_attr_t *attr)
```

**声明头文件**

```c
#include "include/middleware/utils/nv.h"
```

**功能说明**

- 读取指定 key ID 对应的 NV 数据项，并同时获取该 key 的属性值。
- 适用于需要读取 NV 数据并感知其加密、永久、不可升级等属性的场景。

**前置条件**

- 调用时序约束：必须在 `uapi_nv_init` 成功返回后调用。
- 依赖关系：依赖 flash 存储介质可用，目标 key ID 对应数据已写入。
- 上下文限制：禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| key | uint16_t | 要读取的 NV 项的 key ID，用于索引 | KEY_ID_REGION0(1, 0x1000) ~ KEY_ID_REGION15(0xF000, 0xFFFF) 区域内合法 key ID |
| kvalue_max_length | uint16_t | 允许拷贝到 kvalue 缓冲区的最大长度，单位字节 | 大于等于实际读取数据长度 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| kvalue_length | uint16_t * | 实际读取到的 NV 数据长度，单位字节，由调用方分配内存、函数填充 |
| kvalue | uint8_t * | 指向保存读取数据的缓冲区指针，由调用方分配内存、函数填充 |
| attr | [nv_key_attr_t](#struct_nv_key_attr_t) * | 获取到的 NV 项属性，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | NV 数据项读取成功 |
| ERRCODE_NV_INVALID_PARAMS：0x80003083 | 参数无效 | kvalue_length、kvalue 或 attr 指针为 NULL |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

**参考案例**

- `middleware/chips/ws53/factory/factory.c`

### uapi_nv_get_store_status <a id="uapi_nv_get_store_status"></a>

```c
errcode_t uapi_nv_get_store_status(nv_store_status_t *status)
```

**声明头文件**

```c
#include "include/middleware/utils/nv.h"
```

**功能说明**

- 查询当前核的 NV 存储空间使用状态。
- 输出总空间、已用空间、可回收空间、已损坏空间、单 NV 项最大可存储空间等指标。
- 适用于上层业务感知 NV 容量占用、决定是否触发回收或备份恢复。

**前置条件**

- 调用时序约束：必须在 `uapi_nv_init` 成功返回后调用。
- 依赖关系：依赖 NV 模块已正确初始化并完成 NV 区域扫描。
- 上下文限制：禁止在中断上下文调用。

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| status | [nv_store_status_t](#struct_nv_store_status_t) * | 指向保存 NV 状态数据的指针，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | NV 存储状态查询成功 |
| ERRCODE_NV_INVALID_PARAMS：0x80003083 | 参数无效 | status 指针为 NULL |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### uapi_nv_backup <a id="uapi_nv_backup"></a>

```c
errcode_t uapi_nv_backup(const nv_backup_mode_t *backup_mode)
```

**声明头文件**

```c
#include "include/middleware/utils/nv.h"
```

**功能说明**

- 按 NV 区域备份标志执行 NV 数据备份。
- 备份区域由 `nv_backup_mode_t` 中各 region 标志位决定，标志位为 true 表示对应区域需要备份。
- 仅在启用 NV 备份恢复特性时有效。

**前置条件**

- 调用时序约束：必须在 `uapi_nv_init` 成功返回后调用。
- 依赖关系：依赖 flash 存储介质可用，且 `CONFIG_NV_SUPPORT_BACKUP_RESTORE` 已开启。
- 上下文限制：禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| backup_mode | [nv_backup_mode_t](#struct_nv_backup_mode_t) * | 指向 NV 备份区域标志配置的指针 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | NV 备份成功 |
| ERRCODE_NV_INVALID_PARAMS：0x80003083 | 参数无效 | backup_mode 指针为 NULL |
| ERRCODE_NOT_SUPPORT：0x80000002 | 不支持 | 未开启 `CONFIG_NV_SUPPORT_BACKUP_RESTORE` 特性 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

**参考案例**

- `middleware/chips/ws53/factory/factory.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_NV_SUPPORT_BACKUP_RESTORE | 特性宏 | 支持备份/恢复功能（接口级，nv_config.h 宏，默认 NV_YES） | y |

### uapi_nv_set_restore_mode_all <a id="uapi_nv_set_restore_mode_all"></a>

```c
errcode_t uapi_nv_set_restore_mode_all(void)
```

**声明头文件**

```c
#include "include/middleware/utils/nv.h"
```

**功能说明**

- 设置 NV 全量恢复标志，标记全部 NV 区域在下次启动时恢复出厂数据。
- 仅在启用 NV 备份恢复特性时有效。

**前置条件**

- 调用时序约束：必须在 `uapi_nv_init` 成功返回后调用。
- 依赖关系：依赖 `CONFIG_NV_SUPPORT_BACKUP_RESTORE` 已开启。
- 上下文限制：禁止在中断上下文调用。

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 全量恢复标志设置成功 |
| ERRCODE_NOT_SUPPORT：0x80000002 | 不支持 | 未开启 `CONFIG_NV_SUPPORT_BACKUP_RESTORE` 特性 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_NV_SUPPORT_BACKUP_RESTORE | 特性宏 | 支持备份/恢复功能（接口级，nv_config.h 宏，默认 NV_YES） | y |

### uapi_nv_set_restore_mode_partitial <a id="uapi_nv_set_restore_mode_partitial"></a>

```c
errcode_t uapi_nv_set_restore_mode_partitial(const nv_restore_mode_t *restore_mode)
```

**声明头文件**

```c
#include "include/middleware/utils/nv.h"
```

**功能说明**

- 设置 NV 部分区域恢复标志，按 `nv_restore_mode_t` 中各 region 标志位决定恢复范围。
- 标志位为 true 表示对应区域在下次启动时恢复出厂数据。
- 仅在启用 NV 备份恢复特性时有效。

**前置条件**

- 调用时序约束：必须在 `uapi_nv_init` 成功返回后调用。
- 依赖关系：依赖 `CONFIG_NV_SUPPORT_BACKUP_RESTORE` 已开启。
- 上下文限制：禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| restore_mode | [nv_restore_mode_t](#struct_nv_restore_mode_t) * | 指向 NV 恢复区域标志配置的指针 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 部分区域恢复标志设置成功 |
| ERRCODE_NOT_SUPPORT：0x80000002 | 不支持 | 未开启 `CONFIG_NV_SUPPORT_BACKUP_RESTORE` 特性 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_NV_SUPPORT_BACKUP_RESTORE | 特性宏 | 支持备份/恢复功能（接口级，nv_config.h 宏，默认 NV_YES） | y |

### uapi_nv_flush <a id="uapi_nv_flush"></a>

```c
errcode_t uapi_nv_flush(void)
```

**声明头文件**

```c
#include "include/middleware/utils/nv.h"
```

**功能说明**

- 将当前驻留在 RAM 中的 NV 数据同步刷写到 flash。
- 仅在 NV 启用异步存储特性时调用才有效。
- 适用于同步存储语义的业务场景。

**前置条件**

- 调用时序约束：必须在 `uapi_nv_init` 成功返回后调用，且 NV 异步存储特性已开启。
- 依赖关系：依赖 `CONFIG_NV_SUPPORT_ASYNCHRONOUS_STORE` 已开启。
- 上下文限制：禁止在中断上下文调用。

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | RAM 中 NV 数据成功刷写到 flash |
| ERRCODE_NOT_SUPPORT：0x80000002 | 不支持 | 未开启 `CONFIG_NV_SUPPORT_ASYNCHRONOUS_STORE` 特性 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_NV_SUPPORT_ASYNCHRONOUS_STORE | 特性宏 | 支持异步落盘功能（接口级，nv_config.h 宏，默认 NV_NO） | n |

### uapi_nv_register_change_notify_proc <a id="uapi_nv_register_change_notify_proc"></a>

```c
errcode_t uapi_nv_register_change_notify_proc(uint16_t min_key, uint16_t max_key, nv_changed_notify_func func)
```

**声明头文件**

```c
#include "include/middleware/utils/nv.h"
```

**功能说明**

- 注册 NV 键值变更通知回调函数，绑定回调生效的 key ID 区间。
- 当指定区间内的 NV key 值发生变更时，触发已注册的回调。
- 仅在启用 NV 键值变更通知特性时生效。

**前置条件**

- 调用时序约束：必须在 `uapi_nv_init` 成功返回后调用。
- 依赖关系：依赖 `CONFIG_NV_SUPPORT_CHANGE_NOTIFY` 已开启，且系统已分配通知注册槽位。
- 上下文限制：禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| min_key | uint16_t | 注册回调支持的最小 key ID | min_key 不大于 max_key |
| max_key | uint16_t | 注册回调支持的最大 key ID | max_key 不小于 min_key |
| func | [nv_changed_notify_func](#typedef_nv_changed_notify_func) | NV 键值变更通知回调函数指针 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 回调函数注册成功 |
| ERRCODE_NV_INVALID_PARAMS：0x80003083 | 参数无效 | min_key 大于 max_key、func 为 NULL 或通知注册槽位数为 0 |
| ERRCODE_NOT_SUPPORT：0x80000002 | 不支持 | 未开启 `CONFIG_NV_SUPPORT_CHANGE_NOTIFY` 特性 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_NV_SUPPORT_CHANGE_NOTIFY | 特性宏 | 支持变更通知功能（接口级，nv_config.h 宏，默认 NV_NO） | n |

## Type definitions

### typedef_nv_storage_completed_callback <a id="typedef_nv_storage_completed_callback"></a>

```c
// 源码原始定义
typedef void (*nv_storage_completed_callback)(errcode_t result);
```

**使用说明**

NV 存储完成回调函数指针类型，作为 `uapi_nv_write_with_attr` 入参 `func` 的类型，在 kvalue 写入 flash 完成后被调用，参数 `result` 为写入操作的最终结果。

### typedef_nv_changed_notify_func <a id="typedef_nv_changed_notify_func"></a>

```c
// 源码原始定义
typedef void (*nv_changed_notify_func)(uint16_t key);
```

**使用说明**

NV 键值变更通知回调函数指针类型，作为 `uapi_nv_register_change_notify_proc` 入参 `func` 的类型，在已注册 key ID 区间内的 NV 键值发生变更时被调用，参数 `key` 为发生变更的 NV 项 key ID。

## Enumerations

### enum_nv_key_id_region_t <a id="enum_nv_key_id_region_t"></a>

```c
// 源码原始定义
typedef enum {
    KEY_ID_REGION0,
    KEY_ID_REGION1,
    KEY_ID_REGION2,
    KEY_ID_REGION3,
    KEY_ID_REGION4,
    KEY_ID_REGION5,
    KEY_ID_REGION6,
    KEY_ID_REGION7,
    KEY_ID_REGION8,
    KEY_ID_REGION9,
    KEY_ID_REGION10,
    KEY_ID_REGION11,
    KEY_ID_REGION12,
    KEY_ID_REGION13,
    KEY_ID_REGION14,
    KEY_ID_REGION15,
    KEY_ID_REGION_MAX_NUM,
} nv_key_id_region_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| KEY_ID_REGION0 | 0 | key_id 取值区域 0：[1, 0x1000) |
| KEY_ID_REGION1 | 1 | key_id 取值区域 1：[0x1000, 0x2000) |
| KEY_ID_REGION2 | 2 | key_id 取值区域 2：[0x2000, 0x3000) |
| KEY_ID_REGION3 | 3 | key_id 取值区域 3：[0x3000, 0x4000) |
| KEY_ID_REGION4 | 4 | key_id 取值区域 4：[0x4000, 0x5000) |
| KEY_ID_REGION5 | 5 | key_id 取值区域 5：[0x5000, 0x6000) |
| KEY_ID_REGION6 | 6 | key_id 取值区域 6：[0x6000, 0x7000) |
| KEY_ID_REGION7 | 7 | key_id 取值区域 7：[0x7000, 0x8000) |
| KEY_ID_REGION8 | 8 | key_id 取值区域 8：[0x8000, 0x9000) |
| KEY_ID_REGION9 | 9 | key_id 取值区域 9：[0x9000, 0xA000) |
| KEY_ID_REGION10 | 10 | key_id 取值区域 10：[0xA000, 0xB000) |
| KEY_ID_REGION11 | 11 | key_id 取值区域 11：[0xB000, 0xC000) |
| KEY_ID_REGION12 | 12 | key_id 取值区域 12：[0xC000, 0xD000) |
| KEY_ID_REGION13 | 13 | key_id 取值区域 13：[0xD000, 0xE000) |
| KEY_ID_REGION14 | 14 | key_id 取值区域 14：[0xE000, 0xF000) |
| KEY_ID_REGION15 | 15 | key_id 取值区域 15：[0xF000, 0xFFFF] |
| KEY_ID_REGION_MAX_NUM | 16 | key_id 的取值区域数量 |

## Structures

### struct_nv_key_attr_t <a id="struct_nv_key_attr_t"></a>

```c
// 源码原始定义
typedef struct {
    bool permanent;
    bool encrypted;
    bool non_upgrade;
    uint8_t reserve;
} nv_key_attr_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| permanent | bool | 是否为永久 NV，永久属性 key 的 kvalue 不可修改 |
| encrypted | bool | 是否为密文存储 |
| non_upgrade | bool | 是否不可升级 |
| reserve | uint8_t | 保留字段 |

### struct_nv_store_status_t <a id="struct_nv_store_status_t"></a>

```c
// 源码原始定义
typedef struct {
    uint32_t total_space;
    uint32_t used_space;
    uint32_t reclaimable_space;
    uint32_t corrupted_space;
    uint32_t max_key_space;
} nv_store_status_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| total_space | uint32_t | 当前核的 NV 总空间，单位字节 |
| used_space | uint32_t | 当前核已使用的 NV 空间，单位字节 |
| reclaimable_space | uint32_t | 当前核的 NV 可回收空间，擦除后可复用，单位字节 |
| corrupted_space | uint32_t | 当前核已损坏的 NV 空间，数据有效但异常，擦除后可复用，单位字节 |
| max_key_space | uint32_t | 可存储的最大单 NV 项空间，单位字节 |

### struct_nv_restore_mode_t <a id="struct_nv_restore_mode_t"></a>

```c
// 源码原始定义
typedef struct {
    bool region_mode[KEY_ID_REGION_MAX_NUM];
} nv_restore_mode_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| region_mode | bool[KEY_ID_REGION_MAX_NUM] | 恢复出厂区域标志配置，数组下标对应 `nv_key_id_region_t` 区域序号，值为 true 表示对应区域需恢复 |

### struct_nv_backup_mode_t <a id="struct_nv_backup_mode_t"></a>

```c
// 源码原始定义
typedef struct {
    bool region_mode[KEY_ID_REGION_MAX_NUM];
} nv_backup_mode_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| region_mode | bool[KEY_ID_REGION_MAX_NUM] | 备份区域标志配置，数组下标对应 `nv_key_id_region_t` 区域序号，值为 true 表示对应区域需备份 |

## Macros

### NV_NORMAL_KVALUE_MAX_LEN <a id="NV_NORMAL_KVALUE_MAX_LEN"></a>

```c
#define NV_NORMAL_KVALUE_MAX_LEN     4060           /* 普通NV的最大数据长度 */
```

### NV_ENCRYPTED_KVALUE_MAX_LEN <a id="NV_ENCRYPTED_KVALUE_MAX_LEN"></a>

```c
#define NV_ENCRYPTED_KVALUE_MAX_LEN  4032           /* 加密NV的最大数据长度 */
```
