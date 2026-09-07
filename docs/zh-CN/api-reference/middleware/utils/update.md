# Update

Update（UPG，Upgrade）提供固件升级（FOTA）功能，支持升级包存储、校验、解密、解压和差分更新，覆盖升级全流程管理。

**模块公共头文件**

```c
#include "middleware/utils/upg.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_upg_init](#uapi_upg_init) | 初始化升级模块 |
| [uapi_upg_start](#uapi_upg_start) | 开始本地升级 |
| [uapi_upg_register_progress_callback](#uapi_upg_register_progress_callback) | 注册升级进度通知回调函数 |
| [uapi_upg_get_result](#uapi_upg_get_result) | 获取升级结果 |
| [uapi_upg_get_status](#uapi_upg_get_status) | 获取升级状态 |
| [uapi_upg_prepare](#uapi_upg_prepare) | 准备本地存储空间以保存升级包 |
| [uapi_upg_reset_upgrade_flag](#uapi_upg_reset_upgrade_flag) | 重置升级标记 |
| [uapi_upg_write_package_async](#uapi_upg_write_package_async) | 异步写入升级包数据到本地存储 |
| [uapi_upg_write_package_sync](#uapi_upg_write_package_sync) | 同步写入升级包数据到本地存储 |
| [uapi_upg_read_package](#uapi_upg_read_package) | 从本地存储读取升级包数据 |
| [uapi_upg_get_storage_size](#uapi_upg_get_storage_size) | 获取可存放升级包的空间大小 |
| [uapi_upg_request_upgrade](#uapi_upg_request_upgrade) | 申请开始本地升级 |
| [uapi_upg_verify_file_head](#uapi_upg_verify_file_head) | 校验升级包头结构 |
| [uapi_upg_verify_file_image](#uapi_upg_verify_file_image) | 校验升级包中的升级镜像 |
| [uapi_upg_verify_file](#uapi_upg_verify_file) | 校验整个升级包 |
| [uapi_upg_register_user_defined_verify_func](#uapi_upg_register_user_defined_verify_func) | 注册用户自定义字段校验函数 |

## Functions

### uapi_upg_init <a id="uapi_upg_init"></a>

```c
errcode_t uapi_upg_init(const upg_func_t *func_list)
```

**声明头文件**

```c
#include "middleware/utils/upg.h"
```

**功能说明**

- 初始化升级模块，注册内存分配、释放和串口输出函数。
- 标记升级模块为已初始化。
- 获取并保存当前升级状态。

**前置条件**

- 调用时序约束：首次使用升级模块其他接口前必须调用本接口完成初始化。
- 依赖关系：func_list 中 malloc 和 free 函数必须有效。
- 上下文限制：禁止重复调用，重复调用返回 ERRCODE_UPG_ALREADY_INIT。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func_list | [upg_func_t](#struct_upg_func)* | 升级模块使用的注册函数列表 | 允许为 NULL（实现接受 NULL，按默认函数表处理） |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 初始化成功 |
| ERRCODE_UPG_ALREADY_INIT：0x80003041 | 模块已初始化 | 重复调用初始化接口 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**参考案例**

- `src/middleware/chips/ws53/update/common/upg_common_porting.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIDDLEWARE_SUPPORT_UPDATE | 编译参与宏 | update 组件纳入编译的组件集配置（WS53 组件集） | n |
| CONFIG_MIDDLEWARE_SUPPORT_UPG | 编译参与宏 | 支持 FOTA 功能（接口级） | n |

### uapi_upg_start <a id="uapi_upg_start"></a>

```c
errcode_t uapi_upg_start(void)
```

**声明头文件**

```c
#include "middleware/utils/upg.h"
```

**功能说明**

- 开始本地升级流程，读取升级标记并校验升级包。
- 根据升级包中的镜像列表逐个执行升级任务。
- 升级完成后更新升级标记和完成标记。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_upg_init 成功返回后调用。
- 依赖关系：当前接口依赖升级标记区已存在有效的升级包信息。
- 上下文限制：升级流程中禁止并发调用。

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 升级流程执行成功 |
| ERRCODE_UPG_NOT_INIT：0x80003040 | 模块未初始化 | 未调用 uapi_upg_init |
| ERRCODE_UPG_NOT_NEED_TO_UPDATE：0x80003047 | 不需要升级 | 升级区无有效升级包 |
| Other | 其他错误码，参考 errcode_t | 升级流程执行失败 |

**参考案例**

- `src/bootloader/flashboot_ws53/startup/main.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIDDLEWARE_SUPPORT_UPDATE | 编译参与宏 | update 组件纳入编译的组件集配置（WS53 组件集） | n |
| CONFIG_MIDDLEWARE_SUPPORT_UPG | 编译参与宏 | 支持 FOTA 功能（接口级） | n |

### uapi_upg_register_progress_callback <a id="uapi_upg_register_progress_callback"></a>

```c
errcode_t uapi_upg_register_progress_callback(uapi_upg_progress_cb func)
```

**声明头文件**

```c
#include "middleware/utils/upg.h"
```

**功能说明**

- 注册升级进度通知回调函数，升级过程中通过回调上报进度百分比。
- 注册后升级流程执行期间会计算已完成镜像大小占总镜像大小的百分比并通知。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_upg_init 成功返回后调用。
- 依赖关系：当前接口依赖 UPG_CFG_PROCESS_NOTIFY_SUPPORT 配置开启。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func | [uapi_upg_progress_cb](#typedef_uapi_upg_progress_cb) | 进度通知回调函数指针；升级过程中按进度百分比调用 | 允许为 NULL（实现接受 NULL，直接赋值） |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 注册成功 |
| ERRCODE_UPG_NOT_SUPPORTED：0x80003046 | 不支持 | UPG_CFG_PROCESS_NOTIFY_SUPPORT 未开启 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**参考案例**

- `src/middleware/chips/ws53/update/common/upg_common_porting.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| UPG_CFG_PROCESS_NOTIFY_SUPPORT | 特性宏 | 支持升级进度通知功能（接口级，无前缀注入宏，包裹实现体，upg_config.h 默认 YES） | y |

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIDDLEWARE_SUPPORT_UPDATE | 编译参与宏 | update 组件纳入编译的组件集配置（WS53 组件集） | n |
| CONFIG_MIDDLEWARE_SUPPORT_UPG | 编译参与宏 | 支持 FOTA 功能（接口级） | n |

### uapi_upg_get_result <a id="uapi_upg_get_result"></a>

```c
errcode_t uapi_upg_get_result(upg_result_t *result, uint32_t *last_image_index)
```

**声明头文件**

```c
#include "middleware/utils/upg.h"
```

**功能说明**

- 获取升级结果，包括升级成功或失败的具体原因。
- 获取最后一个处理的升级镜像序号。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_upg_init 成功返回后调用。
- 依赖关系：当前接口依赖升级标记区已写入升级结果。

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| result | [upg_result_t](#enum_upg_result)* | 保存获取的升级结果，由调用方分配内存、函数填充 |
| last_image_index | uint32_t* | 保存获取的最后一个处理的升级镜像的序号，由调用方分配内存、函数填充 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 获取升级结果成功 |
| ERRCODE_UPG_NULL_POINTER：0x80003045 | 空指针 | result 或 last_image_index 为 NULL |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIDDLEWARE_SUPPORT_UPDATE | 编译参与宏 | update 组件纳入编译的组件集配置（WS53 组件集） | n |
| CONFIG_MIDDLEWARE_SUPPORT_UPG | 编译参与宏 | 支持 FOTA 功能（接口级） | n |

### uapi_upg_get_status <a id="uapi_upg_get_status"></a>

```c
upg_status_t uapi_upg_get_status(void)
```

**声明头文件**

```c
#include "middleware/utils/upg.h"
```

**功能说明**

- 获取当前升级状态，包括成功、失败、升级中或非升级状态。
- 返回从升级标记区读取并缓存的状态值。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_upg_init 成功返回后调用。

**返回值**

返回类型：[upg_status_t](#enum_upg_status)

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| UPG_STATUS_SUCC：0 | 升级成功 | 升级标记区记录升级成功 |
| UPG_STATUS_FAIL：1 | 升级失败 | 升级标记区记录升级失败 |
| UPG_STATUS_UPDATING：2 | 正在升级 | 升级标记区记录升级进行中 |
| UPG_STATUS_NONE：3 | 非升级状态 | 无升级记录或标记区无效 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIDDLEWARE_SUPPORT_UPDATE | 编译参与宏 | update 组件纳入编译的组件集配置（WS53 组件集） | n |
| CONFIG_MIDDLEWARE_SUPPORT_UPG | 编译参与宏 | 支持 FOTA 功能（接口级） | n |

### uapi_upg_prepare <a id="uapi_upg_prepare"></a>

```c
errcode_t uapi_upg_prepare(upg_prepare_info_t *prepare_info)
```

**声明头文件**

```c
#include "middleware/utils/upg.h"
```

**功能说明**

- 准备本地存储空间以保存升级包，擦除升级区和进度状态区。
- 初始化升级标记区中的头部偏移、升级包长度和头部魔数。
- 该函数阻塞等待执行完成后返回。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_upg_init 成功返回后、写入升级包数据前调用。
- 依赖关系：当前接口依赖 Flash 升级分区已就绪。
- 上下文限制：该函数为阻塞调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| prepare_info | [upg_prepare_info_t](#struct_upg_prepare_info)* | 准备信息的指针，包含升级包总长度 | 非 NULL，package_len > 0 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 存储空间准备成功 |
| ERRCODE_UPG_NOT_INIT：0x80003040 | 模块未初始化 | 未调用 uapi_upg_init |
| ERRCODE_UPG_INVALID_PARAMETER：0x80003042 | 参数无效 | prepare_info 为 NULL 或 package_len 为 0 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIDDLEWARE_SUPPORT_UPDATE | 编译参与宏 | update 组件纳入编译的组件集配置（WS53 组件集） | n |
| CONFIG_MIDDLEWARE_SUPPORT_UPG | 编译参与宏 | 支持 FOTA 功能（接口级） | n |

### uapi_upg_reset_upgrade_flag <a id="uapi_upg_reset_upgrade_flag"></a>

```c
errcode_t uapi_upg_reset_upgrade_flag(void)
```

**声明头文件**

```c
#include "middleware/utils/upg.h"
```

**功能说明**

- 重置升级标记，擦除标记区后重新初始化头部偏移、头部魔数和升级包长度。
- 该函数阻塞等待执行完成后返回。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_upg_init 成功返回后调用。
- 依赖关系：当前接口依赖 Flash 升级标记区已就绪。
- 上下文限制：该函数为阻塞调用，禁止在中断上下文调用。

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 升级标记重置成功 |
| ERRCODE_UPG_NOT_INIT：0x80003040 | 模块未初始化 | 未调用 uapi_upg_init |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**参考案例**

- `src/bootloader/flashboot_ws53/startup/main.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIDDLEWARE_SUPPORT_UPDATE | 编译参与宏 | update 组件纳入编译的组件集配置（WS53 组件集） | n |
| CONFIG_MIDDLEWARE_SUPPORT_UPG | 编译参与宏 | 支持 FOTA 功能（接口级） | n |

### uapi_upg_write_package_async <a id="uapi_upg_write_package_async"></a>

```c
errcode_t uapi_upg_write_package_async(uint32_t offset, const uint8_t *buff, uint16_t len, uapi_upg_write_done_cb callback)
```

**声明头文件**

```c
#include "middleware/utils/upg.h"
```

**功能说明**

- 将升级包数据异步写入本地存储，写入完成后调用回调函数通知结果。
- 写入位置由相对升级包起始的偏移量指定。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_upg_prepare 成功返回后调用。
- 依赖关系：当前接口依赖本地存储区已准备完成。
- 上下文限制：前一次写入的回调返回前禁止再次调用本接口。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| offset | uint32_t | 相对升级包开头的偏移 | 0 ~ 升级包大小-1 |
| buff | const uint8_t* | 存放升级包数据的缓冲区 | 非 NULL |
| len | uint16_t | 升级包数据缓冲区的长度 | > 0 |
| callback | [uapi_upg_write_done_cb](#typedef_uapi_upg_write_done_cb) | 写入完成的回调函数 | 允许为 NULL（实现接受 NULL，无回调时不通知） |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 数据写入成功 |
| ERRCODE_UPG_NOT_INIT：0x80003040 | 模块未初始化 | 未调用 uapi_upg_init |
| ERRCODE_UPG_NOT_PREPARED：0x80003054 | 未准备存储空间 | 未调用 uapi_upg_prepare |
| ERRCODE_UPG_NULL_POINTER：0x80003045 | 空指针 | buff 为 NULL |
| ERRCODE_UPG_INVALID_BUFF_LEN：0x80003055 | 缓冲区长度无效 | len 为 0 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIDDLEWARE_SUPPORT_UPDATE | 编译参与宏 | update 组件纳入编译的组件集配置（WS53 组件集） | n |
| CONFIG_MIDDLEWARE_SUPPORT_UPG | 编译参与宏 | 支持 FOTA 功能（接口级） | n |

### uapi_upg_write_package_sync <a id="uapi_upg_write_package_sync"></a>

```c
errcode_t uapi_upg_write_package_sync(uint32_t offset, const uint8_t *buff, uint16_t len)
```

**声明头文件**

```c
#include "middleware/utils/upg.h"
```

**功能说明**

- 将升级包数据同步写入本地存储，写入完成后直接返回。
- 写入位置由相对升级包起始的偏移量指定。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_upg_prepare 成功返回后调用。
- 依赖关系：当前接口依赖本地存储区已准备完成。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| offset | uint32_t | 相对升级包开头的偏移 | 0 ~ 升级包大小-1 |
| buff | const uint8_t* | 存放升级包数据的缓冲区 | 非 NULL |
| len | uint16_t | 升级包数据缓冲区的长度 | > 0 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 数据写入成功 |
| ERRCODE_UPG_NOT_INIT：0x80003040 | 模块未初始化 | 未调用 uapi_upg_init |
| ERRCODE_UPG_NOT_PREPARED：0x80003054 | 未准备存储空间 | 未调用 uapi_upg_prepare |
| ERRCODE_UPG_NULL_POINTER：0x80003045 | 空指针 | buff 为 NULL |
| ERRCODE_UPG_INVALID_BUFF_LEN：0x80003055 | 缓冲区长度无效 | len 为 0 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIDDLEWARE_SUPPORT_UPDATE | 编译参与宏 | update 组件纳入编译的组件集配置（WS53 组件集） | n |
| CONFIG_MIDDLEWARE_SUPPORT_UPG | 编译参与宏 | 支持 FOTA 功能（接口级） | n |

### uapi_upg_read_package <a id="uapi_upg_read_package"></a>

```c
errcode_t uapi_upg_read_package(uint32_t offset, uint8_t *buff, uint32_t len)
```

**声明头文件**

```c
#include "middleware/utils/upg.h"
```

**功能说明**

- 从本地存储读取升级包数据。
- 读取位置由相对升级包起始的偏移量指定。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_upg_init 成功返回后调用。
- 依赖关系：当前接口依赖本地存储区已写入升级包数据。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| offset | uint32_t | 相对升级包开头的偏移 | 0 ~ 升级包大小-1 |
| buff | uint8_t* | 存放读取数据的缓冲区 | 非 NULL |
| len | uint32_t | 要读取的数据长度 | > 0 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 数据读取成功 |
| ERRCODE_UPG_NOT_INIT：0x80003040 | 模块未初始化 | 未调用 uapi_upg_init |
| ERRCODE_UPG_NULL_POINTER：0x80003045 | 空指针 | buff 为 NULL |
| ERRCODE_UPG_INVALID_BUFF_LEN：0x80003055 | 缓冲区长度无效 | len 为 0 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIDDLEWARE_SUPPORT_UPDATE | 编译参与宏 | update 组件纳入编译的组件集配置（WS53 组件集） | n |
| CONFIG_MIDDLEWARE_SUPPORT_UPG | 编译参与宏 | 支持 FOTA 功能（接口级） | n |

### uapi_upg_get_storage_size <a id="uapi_upg_get_storage_size"></a>

```c
uint32_t uapi_upg_get_storage_size(void)
```

**声明头文件**

```c
#include "middleware/utils/upg.h"
```

**功能说明**

- 获取可存放升级包的空间大小。
- 返回本地存储中可用于保存升级包的最大字节数。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_upg_init 成功返回后调用。

**返回值**

返回类型：uint32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 获取失败 | 模块未初始化或获取存储大小失败 |
| Others | 可用空间大小 | 获取成功 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIDDLEWARE_SUPPORT_UPDATE | 编译参与宏 | update 组件纳入编译的组件集配置（WS53 组件集） | n |
| CONFIG_MIDDLEWARE_SUPPORT_UPG | 编译参与宏 | 支持 FOTA 功能（接口级） | n |

### uapi_upg_request_upgrade <a id="uapi_upg_request_upgrade"></a>

```c
errcode_t uapi_upg_request_upgrade(bool reset)
```

**声明头文件**

```c
#include "middleware/utils/upg.h"
```

**功能说明**

- 申请开始本地升级，校验升级包后写入升级请求数据到标记区。
- 可选择升级流程结束后是否重启系统。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_upg_init 成功返回后调用，且升级包已完整写入本地存储。
- 依赖关系：当前接口依赖本地存储区已写入完整升级包。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| reset | bool | 申请流程结束后是否重启系统 | true；<br>false。 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 升级申请成功 |
| ERRCODE_UPG_NOT_INIT：0x80003040 | 模块未初始化 | 未调用 uapi_upg_init |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**参考案例**

- `src/bootloader/flashboot_ws53/startup/main.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIDDLEWARE_SUPPORT_UPDATE | 编译参与宏 | update 组件纳入编译的组件集配置（WS53 组件集） | n |
| CONFIG_MIDDLEWARE_SUPPORT_UPG | 编译参与宏 | 支持 FOTA 功能（接口级） | n |

### uapi_upg_verify_file_head <a id="uapi_upg_verify_file_head"></a>

```c
errcode_t uapi_upg_verify_file_head(const upg_package_header_t *pkg_header)
```

**声明头文件**

```c
#include "middleware/utils/upg.h"
```

**功能说明**

- 校验升级包头结构，包括使用根公钥校验密钥区签名、使用二级公钥校验信息区签名。
- 若注册了自定义字段校验函数，则校验用户自定义字段。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_upg_init 成功返回后调用。
- 依赖关系：当前接口依赖根公钥已烧录到 Flash。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pkg_header | [upg_package_header_t](#struct_upg_package_header)* | 指向升级包头结构的指针 | 非 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 包头校验通过 |
| ERRCODE_UPG_NOT_INIT：0x80003040 | 模块未初始化 | 未调用 uapi_upg_init |
| ERRCODE_UPG_VERIFICATION_KEY_ERROR：0x80003063 | 校验密钥错误 | 获取根公钥失败 |
| ERRCODE_FAIL：0xFFFFFFFF | 校验失败 | 签名校验不通过或镜像 ID 不正确 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| UPG_CFG_VERIFICATION_SUPPORT | 特性宏 | 支持升级包校验分支（分支级，upg_config.h 默认 YES） | y |
| CONFIG_MIDDLEWARE_SUPPORT_UPG_SAMPLE_VERIFY | 特性宏 | 样例自校验分支（分支级，构建系统注入） | n |

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIDDLEWARE_SUPPORT_UPDATE | 编译参与宏 | update 组件纳入编译的组件集配置（WS53 组件集） | n |
| CONFIG_MIDDLEWARE_SUPPORT_UPG | 编译参与宏 | 支持 FOTA 功能（接口级） | n |

### uapi_upg_verify_file_image <a id="uapi_upg_verify_file_image"></a>

```c
errcode_t uapi_upg_verify_file_image(const upg_image_header_t *img_header, const uint8_t *hash, uint32_t hash_len, bool verify_old)
```

**声明头文件**

```c
#include "middleware/utils/upg.h"
```

**功能说明**

- 校验升级包中的升级镜像，包括镜像头哈希校验和新镜像数据哈希校验。
- 若为差分升级且 verify_old 为 true，则校验旧镜像哈希。
- 校验镜像头魔术字有效性。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_upg_init 成功返回后调用。
- 依赖关系：当前接口依赖升级包数据已写入本地存储。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| img_header | [upg_image_header_t](#struct_upg_image_header)* | 指向升级镜像头结构的指针 | 非 NULL |
| hash | const uint8_t* | 升级镜像的哈希值 | 非 NULL |
| hash_len | uint32_t | 哈希的长度（单位 Bytes） | SHA_256_LENGTH(32) |
| verify_old | bool | 是否校验旧镜像 | true；<br>false。 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 镜像校验通过 |
| ERRCODE_FAIL：0xFFFFFFFF | 校验失败 | 镜像头魔术字不正确或哈希校验不通过 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| UPG_CFG_VERIFICATION_SUPPORT | 特性宏 | 支持升级包校验分支（分支级，upg_config.h 默认 YES） | y |
| CONFIG_MIDDLEWARE_SUPPORT_UPG_SAMPLE_VERIFY | 特性宏 | 样例自校验分支（分支级，构建系统注入） | n |

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIDDLEWARE_SUPPORT_UPDATE | 编译参与宏 | update 组件纳入编译的组件集配置（WS53 组件集） | n |
| CONFIG_MIDDLEWARE_SUPPORT_UPG | 编译参与宏 | 支持 FOTA 功能（接口级） | n |

### uapi_upg_verify_file <a id="uapi_upg_verify_file"></a>

```c
errcode_t uapi_upg_verify_file(const upg_package_header_t *pkg_header)
```

**声明头文件**

```c
#include "middleware/utils/upg.h"
```

**功能说明**

- 校验整个升级包，依次执行包头校验、镜像哈希表校验和逐个镜像校验。
- 包括防回滚版本号校验（若开启防回滚功能）。

**前置条件**

- 调用时序约束：当前接口必须在 uapi_upg_init 成功返回后调用。
- 依赖关系：当前接口依赖升级包数据已完整写入本地存储。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pkg_header | [upg_package_header_t](#struct_upg_package_header)* | 指向升级包头结构的指针 | 非 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 执行成功 | 整包校验通过 |
| ERRCODE_UPG_NOT_INIT：0x80003040 | 模块未初始化 | 未调用 uapi_upg_init |
| ERRCODE_FAIL：0xFFFFFFFF | 校验失败 | 签名或哈希校验不通过 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

**参考案例**

- `src/bootloader/flashboot_ws53/startup/main.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| UPG_CFG_VERIFICATION_SUPPORT | 特性宏 | 支持升级包校验分支（分支级，upg_config.h 默认 YES） | y |
| CONFIG_MIDDLEWARE_SUPPORT_UPG_SAMPLE_VERIFY | 特性宏 | 样例自校验分支（分支级，构建系统注入） | n |

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIDDLEWARE_SUPPORT_UPDATE | 编译参与宏 | update 组件纳入编译的组件集配置（WS53 组件集） | n |
| CONFIG_MIDDLEWARE_SUPPORT_UPG | 编译参与宏 | 支持 FOTA 功能（接口级） | n |

### uapi_upg_register_user_defined_verify_func <a id="uapi_upg_register_user_defined_verify_func"></a>

```c
void uapi_upg_register_user_defined_verify_func(uapi_upg_user_defined_check func, uintptr_t param)
```

**声明头文件**

```c
#include "middleware/utils/upg.h"
```

**功能说明**

- 注册用户自定义字段校验函数。
- 注册后调用 uapi_upg_verify_file_head 和 uapi_upg_verify_file 时，校验函数会被调用。

**前置条件**

- 调用时序约束：当前接口须在调用 uapi_upg_verify_file_head 或 uapi_upg_verify_file 之前注册。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func | [uapi_upg_user_defined_check](#typedef_uapi_upg_user_defined_check) | 用于校验用户自定义字段的校验函数 | 允许为 NULL（实现接受 NULL，直接赋值） |
| param | uintptr_t | 注册参数，透传给校验函数 | 不限 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| UPG_CFG_VERIFICATION_SUPPORT | 特性宏 | 支持升级包校验分支（接口级，upg_config.h 默认 YES） | y |
| CONFIG_MIDDLEWARE_SUPPORT_UPG | 特性宏 | update 组件纳入编译的组件集配置（编译参与宏） | y |

## Type definitions

### uapi_upg_write_done_cb <a id="typedef_uapi_upg_write_done_cb"></a>

```c
typedef void (*uapi_upg_write_done_cb)(errcode_t result);
```

**使用说明**

作为 uapi_upg_write_package_async 接口的回调类型，用于通知升级包数据写入完成。
- 调用时机：异步写入操作完成后，由内部调用已注册的回调。
- 参数 result：写入操作的返回值，ERRCODE_SUCC 表示写入成功，其他值表示写入失败。
- 返回值处理：回调返回类型为 void，无返回值。

### uapi_upg_progress_cb <a id="typedef_uapi_upg_progress_cb"></a>

```c
typedef void (*uapi_upg_progress_cb)(uint32_t percent);
```

**使用说明**

作为 uapi_upg_register_progress_callback 接口的回调类型，用于上报升级进度百分比。
- 调用时机：升级流程执行期间，每完成部分镜像写入后计算进度并调用。
- 参数 percent：进度百分比值，范围 0 ~ 100。
- 返回值处理：回调返回类型为 void，无返回值。

### uapi_upg_user_defined_check <a id="typedef_uapi_upg_user_defined_check"></a>

```c
typedef errcode_t (*uapi_upg_user_defined_check)(uint8_t *user_info, uint32_t info_len, uintptr_t param);
```

**使用说明**

作为 uapi_upg_register_user_defined_verify_func 接口的回调类型，用于校验升级包中用户自定义字段。
- 调用时机：调用 uapi_upg_verify_file_head 和 uapi_upg_verify_file 时，若已注册则被调用。
- 参数 user_info：指向升级包信息区中用户自定义字段的指针。
- 参数 info_len：用户自定义字段的长度。
- 参数 param：注册时传入的透传参数。
- 返回值处理：返回 ERRCODE_SUCC 表示校验通过，其他值表示校验失败。

### upg_func_malloc <a id="typedef_upg_func_malloc"></a>

```c
typedef void *(*upg_func_malloc)(const uint32_t size);
```

**使用说明**

作为 upg_func_t 结构体成员 malloc 的类型，升级模块使用的内存分配函数。

### upg_func_free <a id="typedef_upg_func_free"></a>

```c
typedef void (*upg_func_free)(void *ptr);
```

**使用说明**

作为 upg_func_t 结构体成员 free 的类型，升级模块使用的内存释放函数。

### upg_func_serial_putc <a id="typedef_upg_func_serial_putc"></a>

```c
typedef void (*upg_func_serial_putc)(const char c);
```

**使用说明**

作为 upg_func_t 结构体成员 serial_putc 的类型，升级模块使用的串口输出函数。

## Enumerations

### upg_result <a id="enum_upg_result"></a>

```c
typedef enum upg_result {
    UPG_RESULT_UPDATE_SUCCESS,
    UPG_RESULT_VERIFY_HEAD_FAILED,
    UPG_RESULT_VERIFY_HASH_TABLE_FAILED,
    UPG_RESULT_VERIFY_IMAGE_FAILED,
    UPG_RESULT_VERIFY_OLD_IMAGE_FAILED,
    UPG_RESULT_DECOMPRESS_IMAGE_FAILED,
    UPG_RESULT_DECRYPT_IMAGE_FAILED,
    UPG_RESULT_RECRYPT_IMAGE_FAILED,
    UPG_RESULT_DIFF_IMAGE_FAILED,
    UPG_RESULT_UPDATE_IMAGE_FAILED,
    UPG_RESULT_PROCESS_NV_FAILED,
    UPG_RESULT_VERIFY_VERSION_FAILED,
    UPG_RESULT_IMAGE_ID_FAILED,
    UPG_RESULT_RETRY_ALL_FAILED,
    UPG_RESULT_MAX,
} upg_result_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UPG_RESULT_UPDATE_SUCCESS | 0 | 升级成功 |
| UPG_RESULT_VERIFY_HEAD_FAILED | 1 | 校验升级包头失败 |
| UPG_RESULT_VERIFY_HASH_TABLE_FAILED | 2 | 校验哈希表失败 |
| UPG_RESULT_VERIFY_IMAGE_FAILED | 3 | 校验镜像失败 |
| UPG_RESULT_VERIFY_OLD_IMAGE_FAILED | 4 | 校验旧镜像失败 |
| UPG_RESULT_DECOMPRESS_IMAGE_FAILED | 5 | 解压缩失败 |
| UPG_RESULT_DECRYPT_IMAGE_FAILED | 6 | 解密失败 |
| UPG_RESULT_RECRYPT_IMAGE_FAILED | 7 | 重加密失败 |
| UPG_RESULT_DIFF_IMAGE_FAILED | 8 | 差分恢复失败 |
| UPG_RESULT_UPDATE_IMAGE_FAILED | 9 | 更新镜像到 Flash 失败 |
| UPG_RESULT_PROCESS_NV_FAILED | 10 | 处理 NV 镜像失败 |
| UPG_RESULT_VERIFY_VERSION_FAILED | 11 | 防回滚校验失败 |
| UPG_RESULT_IMAGE_ID_FAILED | 12 | 镜像 ID 校验失败 |
| UPG_RESULT_RETRY_ALL_FAILED | 13 | 所有升级尝试均失败 |
| UPG_RESULT_MAX | 14 | 升级结果最大值 |

### upg_status <a id="enum_upg_status"></a>

```c
typedef enum upg_status {
    UPG_STATUS_SUCC,
    UPG_STATUS_FAIL,
    UPG_STATUS_UPDATING,
    UPG_STATUS_NONE
} upg_status_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| UPG_STATUS_SUCC | 0 | 升级成功 |
| UPG_STATUS_FAIL | 1 | 升级失败 |
| UPG_STATUS_UPDATING | 2 | 正在进行升级 |
| UPG_STATUS_NONE | 3 | 非升级状态 |

## Structures

### upg_key_area_data <a id="struct_upg_key_area_data"></a>

```c
typedef struct upg_key_area_data {
    uint32_t image_id;
    uint32_t struct_version;
    uint32_t struct_length;
    uint32_t signature_length;
    uint32_t key_owner_id;
    uint32_t key_id;
    uint32_t key_alg;
    uint32_t ecc_curve_type;
    uint32_t key_length;
    uint32_t fota_key_version_ext;
    uint32_t mask_fota_key_version_ext;
    uint32_t msid_ext;
    uint32_t mask_msid_ext;
    uint32_t maintenance_mode;
    uint8_t die_id[DIE_ID_LEN];
    uint32_t fota_info_addr;
    uint8_t reserved[KEY_AREA_RESERVED_LEN];
    uint8_t fota_external_public_key[PUBLIC_KEY_LEN];
    uint8_t sig_fota_key_area[SIG_LEN];
} upg_key_area_data_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| image_id | uint32_t | FOTA 密钥区域的标识 |
| struct_version | uint32_t | FOTA 密钥区域结构版本 |
| struct_length | uint32_t | 结构长度 |
| signature_length | uint32_t | 签名长度 |
| key_owner_id | uint32_t | FOTA 二级公钥的所有者 ID |
| key_id | uint32_t | FOTA 二级公共密钥的密钥 ID |
| key_alg | uint32_t | 二级公钥算法 |
| ecc_curve_type | uint32_t | ECC 曲线类型 |
| key_length | uint32_t | FOTA 二级公共密钥的长度 |
| fota_key_version_ext | uint32_t | FOTA 二级公共密钥的版本 |
| mask_fota_key_version_ext | uint32_t | FOTA 密钥版本扩展的掩码 |
| msid_ext | uint32_t | 细分市场 ID |
| mask_msid_ext | uint32_t | MSID 掩码 |
| maintenance_mode | uint32_t | 维护模式 |
| die_id | uint8_t[DIE_ID_LEN] | 芯片组芯片 ID，在启用维护模式时有效 |
| fota_info_addr | uint32_t | FOTA 信息区域的偏移地址 |
| reserved | uint8_t[KEY_AREA_RESERVED_LEN] | 为字节对齐而保留的字段 |
| fota_external_public_key | uint8_t[PUBLIC_KEY_LEN] | FOTA 二级公钥 |
| sig_fota_key_area | uint8_t[SIG_LEN] | FOTA 密钥区域签名 |

### upg_fota_info_data <a id="struct_upg_fota_info_data"></a>

```c
typedef struct upg_fota_info_data {
    uint32_t image_id;
    uint32_t struct_version;
    uint32_t struct_length;
    uint32_t signature_length;
    uint32_t fota_version_ext;
    uint32_t mask_fota_version_ext;
    uint32_t msid_ext;
    uint32_t mask_msid_ext;
    uint32_t image_hash_table_addr;
    uint32_t image_hash_table_length;
    uint8_t image_hash_table_hash[SHA_256_LENGTH];
    uint32_t image_num;
    uint32_t hardware_id;
    uint8_t user_defined[INFO_AREA_USER_LEN];
    uint8_t sign_fota_info[SIG_LEN];
} upg_fota_info_data_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| image_id | uint32_t | FOTA 信息区标识 |
| struct_version | uint32_t | FOTA 密钥区域结构版本 |
| struct_length | uint32_t | 结构长度 |
| signature_length | uint32_t | 签名长度 |
| fota_version_ext | uint32_t | FOTA 信息区的版本 |
| mask_fota_version_ext | uint32_t | FOTA 二级公共密钥的版本 |
| msid_ext | uint32_t | 细分市场 ID |
| mask_msid_ext | uint32_t | MSID 掩码 |
| image_hash_table_addr | uint32_t | FOTA 包中镜像哈希表的地址 |
| image_hash_table_length | uint32_t | 镜像哈希表的长度 |
| image_hash_table_hash | uint8_t[SHA_256_LENGTH] | 镜像哈希表的哈希 |
| image_num | uint32_t | FOTA 镜像的总数 |
| hardware_id | uint32_t | 硬件 ID |
| user_defined | uint8_t[INFO_AREA_USER_LEN] | 预留字节供用户自定义使用 |
| sign_fota_info | uint8_t[SIG_LEN] | FOTA 信息签名 |

### upg_package_header <a id="struct_upg_package_header"></a>

```c
typedef struct upg_package_header {
    upg_key_area_data_t  key_area;
    upg_fota_info_data_t info_area;
} upg_package_header_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| key_area | upg_key_area_data_t | 升级密钥区域数据 |
| info_area | upg_fota_info_data_t | FOTA 信息区数据 |

### upg_image_header <a id="struct_upg_image_header"></a>

```c
typedef struct upg_image_header {
    uint32_t header_magic;
    uint32_t image_id;
    uint32_t image_offset;
    uint32_t image_len;
    uint8_t image_hash[SHA_256_LENGTH];
    uint32_t old_image_len;
    uint8_t old_image_hash[SHA_256_LENGTH];
    uint32_t new_image_len;
    uint32_t version_ext;
    uint32_t version_mask;
    uint32_t decompress_flag;
    uint32_t re_enc_flag;
    uint32_t root_key_type;
    uint8_t enc_pk_l1[PROTECT_KEY_LEN];
    uint8_t enc_pk_l2[PROTECT_KEY_LEN];
    uint8_t iv[IV_LEN];
    uint8_t padding[4];
} upg_image_header_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| header_magic | uint32_t | 镜像头魔术字 |
| image_id | uint32_t | FOTA 密钥区域的标识 |
| image_offset | uint32_t | 要更新的镜像数据的偏移地址 |
| image_len | uint32_t | 更新的镜像数据的长度（实际数据长度，不包括填充字段） |
| image_hash | uint8_t[SHA_256_LENGTH] | 更新镜像数据的哈希 |
| old_image_len | uint32_t | 旧镜像长度 |
| old_image_hash | uint8_t[SHA_256_LENGTH] | 旧镜像的哈希值 |
| new_image_len | uint32_t | 新镜像长度 |
| version_ext | uint32_t | 新镜像版本 |
| version_mask | uint32_t | 版本掩码 |
| decompress_flag | uint32_t | 解压标志 |
| re_enc_flag | uint32_t | 重新加密标志 |
| root_key_type | uint32_t | 用于加密镜像的密钥 |
| enc_pk_l1 | uint8_t[PROTECT_KEY_LEN] | 用于解密更新镜像的一级加密保护密钥 |
| enc_pk_l2 | uint8_t[PROTECT_KEY_LEN] | 用于解密更新镜像的二级加密保护密钥 |
| iv | uint8_t[IV_LEN] | 用于解密升级镜像的 IV |
| padding | uint8_t[4] | 保留字段，以保证整个结构 16 Bytes 对齐 |

### upg_func <a id="struct_upg_func"></a>

```c
typedef struct upg_func {
    upg_func_malloc malloc;
    upg_func_free free;
    upg_func_serial_putc serial_putc;
} upg_func_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| malloc | upg_func_malloc | 升级使用内存分配函数（必选函数） |
| free | upg_func_free | 升级释放内存函数（必选函数） |
| serial_putc | upg_func_serial_putc | 升级串口输出函数（可选函数） |

### upg_prepare_info <a id="struct_upg_prepare_info"></a>

```c
typedef struct upg_prepare_info {
    uint32_t package_len;
} upg_prepare_info_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| package_len | uint32_t | 升级包的大小 |

## Macros

### SHA_256_LENGTH <a id="SHA_256_LENGTH"></a>

```c
#define SHA_256_LENGTH  32
```

### DIE_ID_LEN <a id="DIE_ID_LEN"></a>

```c
#define DIE_ID_LEN      16
```

### PROTECT_KEY_LEN <a id="PROTECT_KEY_LEN"></a>

```c
#define PROTECT_KEY_LEN 16
```

### IV_LEN <a id="IV_LEN"></a>

```c
#define IV_LEN          16
```

### KEY_AREA_RESERVED_LEN <a id="KEY_AREA_RESERVED_LEN"></a>

```c
#define KEY_AREA_RESERVED_LEN 52
```

### INFO_AREA_USER_LEN <a id="INFO_AREA_USER_LEN"></a>

```c
#define INFO_AREA_USER_LEN 112
```

### SIG_LEN <a id="SIG_LEN"></a>

```c
#define SIG_LEN         64
```

### PUBLIC_KEY_LEN <a id="PUBLIC_KEY_LEN"></a>

```c
#define PUBLIC_KEY_LEN 64
```
