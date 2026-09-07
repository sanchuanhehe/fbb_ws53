# GAP

GAP（Generic Access Profile）提供 BLE（Bluetooth Low Energy） LE 广播、扫描、连接、配对、白名单、PHY（Physical Layer）与数据长度等通用访问控制能力，支持本端设备信息设置与查询、安全参数配置、回调注册以及 SMP（Security Manager Protocol）密钥存储等操作。

**模块公共头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [gap_ble_set_local_addr](#gap_ble_set_local_addr) | 设置本地设备蓝牙地址 |
| [gap_ble_get_local_addr](#gap_ble_get_local_addr) | 获取本地设备蓝牙地址 |
| [gap_ble_set_local_appearance](#gap_ble_set_local_appearance) | 设置本地设备外观类型 |
| [gap_ble_set_local_name](#gap_ble_set_local_name) | 设置本地设备名称 |
| [gap_ble_get_local_name](#gap_ble_get_local_name) | 获取本地设备名称 |
| [gap_ble_set_adv_data](#gap_ble_set_adv_data) | 设置广播数据与扫描响应数据 |
| [gap_ble_set_adv_param](#gap_ble_set_adv_param) | 设置广播参数 |
| [gap_ble_start_adv](#gap_ble_start_adv) | 启动广播 |
| [gap_ble_stop_adv](#gap_ble_stop_adv) | 停止广播 |
| [gap_ble_set_scan_parameters](#gap_ble_set_scan_parameters) | 设置扫描参数 |
| [gap_ble_set_scan_extern_parameters](#gap_ble_set_scan_extern_parameters) | 设置扫描扩展参数 |
| [gap_ble_start_scan](#gap_ble_start_scan) | 启动扫描 |
| [gap_ble_stop_scan](#gap_ble_stop_scan) | 停止扫描 |
| [gap_ble_set_phy](#gap_ble_set_phy) | 设置 BLE PHY 参数 |
| [gap_ble_set_data_length](#gap_ble_set_data_length) | 设置 BLE 发包数据长度参数 |
| [gap_ble_pair_remote_device](#gap_ble_pair_remote_device) | 与指定远端设备启动配对 |
| [gap_ble_get_paired_devices_num](#gap_ble_get_paired_devices_num) | 获取已配对设备数量 |
| [gap_ble_get_paired_devices](#gap_ble_get_paired_devices) | 获取已配对设备地址列表 |
| [gap_ble_get_pair_state](#gap_ble_get_pair_state) | 获取指定设备的配对状态 |
| [gap_ble_remove_pair](#gap_ble_remove_pair) | 与指定设备取消配对 |
| [gap_ble_add_white_list](#gap_ble_add_white_list) | 添加设备到白名单 |
| [gap_ble_remove_white_list](#gap_ble_remove_white_list) | 从白名单移除设备 |
| [gap_ble_get_white_list](#gap_ble_get_white_list) | 获取白名单中的设备 |
| [gap_ble_remove_all_pairs](#gap_ble_remove_all_pairs) | 删除所有已配对设备 |
| [gap_ble_get_bonded_devices](#gap_ble_get_bonded_devices) | 获取已绑定设备地址列表 |
| [gap_ble_connect_param_update](#gap_ble_connect_param_update) | 更新 BLE 连接参数 |
| [gap_ble_connect_remote_device](#gap_ble_connect_remote_device) | 与指定远端设备建立 ACL 连接 |
| [gap_ble_disconnect_remote_device](#gap_ble_disconnect_remote_device) | 断开与指定远端设备的连接 |
| [gap_ble_set_sec_param](#gap_ble_set_sec_param) | 设置安全参数 |
| [gap_ble_read_remote_device_rssi](#gap_ble_read_remote_device_rssi) | 读取远端设备 RSSI |
| [gap_ble_register_callbacks](#gap_ble_register_callbacks) | 注册 BLE GAP 回调函数 |
| [bth_ota_init](#bth_ota_init) | 初始化 bth OTA 通道 |
| [ble_customize_max_pwr](#ble_customize_max_pwr) | 配置 BLE 与 SLE 最大功率定制化信息 |
| [ble_set_nv_pair_keys](#ble_set_nv_pair_keys) | 将 SMP 配对密钥写入 Flash |
| [gap_ble_set_save_smp_keys_mode](#gap_ble_set_save_smp_keys_mode) | 设置配对密钥保存模式 |
| [gap_ble_set_pair_info_available](#gap_ble_set_pair_info_available) | 设置配对信息可获取开关 |

## Functions

### gap_ble_set_local_addr <a id="gap_ble_set_local_addr"></a>

```c
errcode_t gap_ble_set_local_addr(const bd_addr_t *addr)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 设置本端 BLE 设备的蓝牙地址。
- 地址通过 [bd_addr_t](#struct_bd_addr_t) 结构体指针传入。
- 配合广播、扫描、连接流程使用，影响本端设备对外呈现的地址。

**前置条件**

- 调用时序约束：需在协议栈初始化完成、广播或扫描发起之前调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | [bd_addr_t](#struct_bd_addr_t) * | 本地设备蓝牙地址 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 地址设置成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`

### gap_ble_get_local_addr <a id="gap_ble_get_local_addr"></a>

```c
errcode_t gap_ble_get_local_addr(bd_addr_t *addr)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 获取本端 BLE 设备的蓝牙地址。
- 地址通过出参 [bd_addr_t](#struct_bd_addr_t) 结构体指针回填给调用方。
- 用于查询当前生效的本端地址。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| addr | [bd_addr_t](#struct_bd_addr_t) * | 本地设备蓝牙地址，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 地址获取成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_set_local_appearance <a id="gap_ble_set_local_appearance"></a>

```c
errcode_t gap_ble_set_local_appearance(uint16_t appearance)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 设置本端设备的外观类型（Appearance），用于向对端表明设备类别。
- 外观值参考 [gap_ble_appearance_type_t](#enum_gap_ble_appearance_type_t)。
- 影响广播/连接过程中对外呈现的设备类别信息。

**前置条件**

- 调用时序约束：需在协议栈初始化完成、广播发起之前调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| appearance | uint16_t | 本地设备外观类型 | [GAP_BLE_APPEARANCE_TYPE_UNKNOWN](#enum_gap_ble_appearance_type_t)：0；<br>[GAP_BLE_APPEARANCE_TYPE_GENERIC_PHONE](#enum_gap_ble_appearance_type_t)：64；<br>[GAP_BLE_APPEARANCE_TYPE_GENERIC_COMPUTER](#enum_gap_ble_appearance_type_t)：128；<br>[GAP_BLE_APPEARANCE_TYPE_GENERIC_WATCH](#enum_gap_ble_appearance_type_t)：192；<br>[GAP_BLE_APPEARANCE_TYPE_GENERIC_DISPLAY](#enum_gap_ble_appearance_type_t)：320；<br>[GAP_BLE_APPEARANCE_TYPE_GENERIC_HID](#enum_gap_ble_appearance_type_t)：960；<br>[GAP_BLE_APPEARANCE_TYPE_KEYBOARD](#enum_gap_ble_appearance_type_t)：961；<br>[GAP_BLE_APPEARANCE_TYPE_MOUSE](#enum_gap_ble_appearance_type_t)：962；<br>[GAP_BLE_APPEARANCE_TYPE_DIGITAL_PEN](#enum_gap_ble_appearance_type_t)：967。 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 外观类型设置成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_set_local_name <a id="gap_ble_set_local_name"></a>

```c
errcode_t gap_ble_set_local_name(const uint8_t *name, const uint8_t len)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 设置本端 BLE 设备名称。
- 名称通过字节缓冲区指针及长度传入，长度包含结束符 `\0`
- 影响广播/扫描响应中携带的设备名称。

**前置条件**

- 调用时序约束：需在协议栈初始化完成、广播发起之前调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| name | const uint8_t * | 设备名称缓冲区指针 | 不为 NULL |
| len | uint8_t | 名称长度，包含结束符 `\0` | 无实现级边界校验（实现闭源） |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 设备名称设置成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_get_local_name <a id="gap_ble_get_local_name"></a>

```c
errcode_t gap_ble_get_local_name(uint8_t *name, uint8_t *len)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 获取本端 BLE 设备名称。
- 名称通过出参缓冲区回填，`len` 兼作入参与出参。
- 用于查询当前生效的本地设备名称。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| len | uint8_t * | 入参为用户分配的缓冲区大小，出参为设备名称长度 | 不为 NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| name | uint8_t * | 本地设备名称，由函数填充到调用方缓冲区 |
| len | uint8_t * | 本地设备名称长度 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 设备名称获取成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_set_adv_data <a id="gap_ble_set_adv_data"></a>

```c
errcode_t gap_ble_set_adv_data(uint8_t adv_id, const gap_ble_config_adv_data_t *data)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 设置指定广播 ID 的广播数据与扫描响应数据。
- 数据通过 [gap_ble_config_adv_data_t](#struct_gap_ble_config_adv_data_t) 结构体指针传入。
- 数据设置结果通过 [gap_ble_set_adv_data_callback](#typedef_gap_ble_set_adv_data_callback) 回调上报。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后、启动广播之前调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| adv_id | uint8_t | 广播 ID | 0 ~ 255 |
| data | [gap_ble_config_adv_data_t](#struct_gap_ble_config_adv_data_t) * | 广播数据与扫描响应数据 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 数据设置请求成功发起，最终状态通过回调上报 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server_adv.c`
- `src/application/samples/bt/ble/ble_wifi_cfg_server/src/ble_wifi_cfg_adv.c`

### gap_ble_set_adv_param <a id="gap_ble_set_adv_param"></a>

```c
errcode_t gap_ble_set_adv_param(uint8_t adv_id, const gap_ble_adv_params_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 设置指定广播 ID 的广播参数。
- 参数通过 [gap_ble_adv_params_t](#struct_gap_ble_adv_params_t) 结构体指针传入。
- 参数设置结果通过 [gap_ble_set_adv_param_callback](#typedef_gap_ble_set_adv_param_callback) 回调上报。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后、启动广播之前调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| adv_id | uint8_t | 广播 ID | 0 ~ 255 |
| param | [gap_ble_adv_params_t](#struct_gap_ble_adv_params_t) * | 广播参数 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 参数设置请求成功发起，最终状态通过回调上报 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server_adv.c`
- `src/application/samples/bt/ble/ble_wifi_cfg_server/src/ble_wifi_cfg_adv.c`

### gap_ble_start_adv <a id="gap_ble_start_adv"></a>

```c
errcode_t gap_ble_start_adv(uint8_t adv_id)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 启动指定广播 ID 的广播。
- 广播状态通过 [gap_ble_start_adv_callback](#typedef_gap_ble_start_adv_callback) 回调上报。

**前置条件**

- 调用时序约束：需在 [gap_ble_set_adv_param](#gap_ble_set_adv_param) 与 [gap_ble_set_adv_data](#gap_ble_set_adv_data) 成功设置后调用。
- 依赖关系：依赖 BTS 协议栈已就绪、广播参数已配置。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| adv_id | uint8_t | 广播 ID | 0 ~ 255 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 启动请求成功发起，最终状态通过回调上报 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`
- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server_adv.c`
- `src/application/samples/bt/ble/ble_wifi_cfg_server/src/ble_wifi_cfg_adv.c`

### gap_ble_stop_adv <a id="gap_ble_stop_adv"></a>

```c
errcode_t gap_ble_stop_adv(uint8_t adv_id)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 停止指定广播 ID 的广播。
- 广播状态通过 [gap_ble_stop_adv_callback](#typedef_gap_ble_stop_adv_callback) 回调上报。

**前置条件**

- 调用时序约束：需在 [gap_ble_start_adv](#gap_ble_start_adv) 成功启动广播后调用。
- 依赖关系：依赖 BTS 协议栈已就绪、广播处于运行状态。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| adv_id | uint8_t | 广播 ID | 0 ~ 255 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 停止请求成功发起，最终状态通过回调上报 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_set_scan_parameters <a id="gap_ble_set_scan_parameters"></a>

```c
errcode_t gap_ble_set_scan_parameters(const gap_ble_scan_params_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 设置 BLE 扫描参数。
- 参数通过 [gap_ble_scan_params_t](#struct_gap_ble_scan_params_t) 结构体指针传入。
- 参数设置状态通过 [gap_ble_set_scan_param_callback](#typedef_gap_ble_set_scan_param_callback) 回调上报。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后、启动扫描之前调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| param | [gap_ble_scan_params_t](#struct_gap_ble_scan_params_t) * | 扫描参数 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 参数设置请求成功发起，最终状态通过回调上报 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_set_scan_extern_parameters <a id="gap_ble_set_scan_extern_parameters"></a>

```c
errcode_t gap_ble_set_scan_extern_parameters(const gap_ble_extern_scan_params_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 设置 BLE 扫描扩展参数。
- 参数通过 [gap_ble_extern_scan_params_t](#struct_gap_ble_extern_scan_params_t) 结构体指针传入。
- 用于配置重复包过滤、扫描持续时间与扫描周期等扩展行为。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后、启动扫描之前调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| param | [gap_ble_extern_scan_params_t](#struct_gap_ble_extern_scan_params_t) * | 扫描扩展参数 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 扩展参数设置成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_start_scan <a id="gap_ble_start_scan"></a>

```c
errcode_t gap_ble_start_scan(void)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 启动 BLE 扫描。
- 扫描结果通过 [gap_ble_scan_result_callback](#typedef_gap_ble_scan_result_callback) 回调上报。

**前置条件**

- 调用时序约束：需在 [gap_ble_set_scan_parameters](#gap_ble_set_scan_parameters) 成功设置扫描参数后调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 启动请求成功发起，扫描结果通过回调上报 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_stop_scan <a id="gap_ble_stop_scan"></a>

```c
errcode_t gap_ble_stop_scan(void)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 停止 BLE 扫描。

**前置条件**

- 调用时序约束：需在 [gap_ble_start_scan](#gap_ble_start_scan) 成功启动扫描后调用。
- 依赖关系：依赖 BTS 协议栈已就绪、扫描处于运行状态。

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 停止扫描成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_set_phy <a id="gap_ble_set_phy"></a>

```c
errcode_t gap_ble_set_phy(gap_le_set_phy_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 设置指定连接的 BLE PHY 参数。
- 参数通过 [gap_le_set_phy_t](#struct_gap_le_set_phy_t) 结构体指针传入。
- 用于在连接建立后切换发送/接收 PHY 类型与 PHY 选项。

**前置条件**

- 调用时序约束：需在 ACL（Asynchronous Connection-Oriented Link）链路建立成功后调用。
- 依赖关系：依赖 BTS 协议栈已就绪、连接已建立。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| param | [gap_le_set_phy_t](#struct_gap_le_set_phy_t) * | BLE PHY 参数 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | PHY 参数设置成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`

### gap_ble_set_data_length <a id="gap_ble_set_data_length"></a>

```c
errcode_t gap_ble_set_data_length(gap_le_set_data_length_t *param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 设置指定连接的 BLE 发包数据长度参数。
- 参数通过 [gap_le_set_data_length_t](#struct_gap_le_set_data_length_t) 结构体指针传入。
- 设置结果通过 [gap_ble_set_data_length_callback](#typedef_gap_ble_set_data_length_callback) 回调上报。

**前置条件**

- 调用时序约束：需在 ACL 链路建立成功后调用。
- 依赖关系：依赖 BTS 协议栈已就绪、连接已建立。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| param | [gap_le_set_data_length_t](#struct_gap_le_set_data_length_t) * | BLE 发包参数 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 发包参数设置成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`

### gap_ble_pair_remote_device <a id="gap_ble_pair_remote_device"></a>

```c
errcode_t gap_ble_pair_remote_device(const bd_addr_t *addr)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 与指定远端设备启动 SMP 配对。
- 目标设备地址通过 [bd_addr_t](#struct_bd_addr_t) 结构体指针传入。
- 配对结果通过 [gap_ble_paired_complete_callback](#typedef_gap_ble_paired_complete_callback) 回调上报。

**前置条件**

- 调用时序约束：需在 ACL 链路建立成功之后调用。
- 依赖关系：依赖 BTS 协议栈已就绪、连接已建立。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | [bd_addr_t](#struct_bd_addr_t) * | 待配对的远端设备地址 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 配对请求成功发起，最终状态通过回调上报 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_get_paired_devices_num <a id="gap_ble_get_paired_devices_num"></a>

```c
errcode_t gap_ble_get_paired_devices_num(uint16_t *number)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 获取本端已配对设备的数量。
- 数量通过出参 `number` 回填给调用方。
- 用于查询当前已配对设备总数。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| number | uint16_t * | 已配对设备数量，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 数量获取成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_get_paired_devices <a id="gap_ble_get_paired_devices"></a>

```c
errcode_t gap_ble_get_paired_devices(bd_addr_t *addr, uint16_t *number)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 获取本端已配对设备地址列表。
- 地址列表通过出参 `addr` 缓冲区回填，`number` 兼作入参与出参。
- 用于查询当前所有已配对设备的地址。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| number | uint16_t * | 入参为缓冲区可容纳的设备数，出参为实际配对设备数 | 不为 NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| addr | [bd_addr_t](#struct_bd_addr_t) * | 已配对设备地址列表，由函数填充 |
| number | uint16_t * | 实际已配对设备数量 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 地址列表获取成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_get_pair_state <a id="gap_ble_get_pair_state"></a>

```c
errcode_t gap_ble_get_pair_state(const bd_addr_t *addr, gap_ble_pair_state_t *status)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 获取指定设备的配对状态。
- 目标设备地址通过入参传入，配对状态通过出参 [gap_ble_pair_state_t](#enum_gap_ble_pair_state_t) 回填。
- 用于查询特定设备当前的配对状态。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | [bd_addr_t](#struct_bd_addr_t) * | 待查询的设备地址 | 不为 NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| status | [gap_ble_pair_state_t](#enum_gap_ble_pair_state_t) * | 设备配对状态，由函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 配对状态获取成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_remove_pair <a id="gap_ble_remove_pair"></a>

```c
errcode_t gap_ble_remove_pair(const bd_addr_t *addr)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 与指定远端设备取消配对。
- 目标设备地址通过 [bd_addr_t](#struct_bd_addr_t) 结构体指针传入。
- 用于清除与特定设备的配对关系。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | [bd_addr_t](#struct_bd_addr_t) * | 待取消配对的对端设备地址 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 取消配对成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_add_white_list <a id="gap_ble_add_white_list"></a>

```c
errcode_t gap_ble_add_white_list(const bd_addr_t *addr)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 添加指定设备到 BLE 白名单。
- 目标设备地址通过 [bd_addr_t](#struct_bd_addr_t) 结构体指针传入。
- 白名单生效后影响广播过滤与扫描过滤策略。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | [bd_addr_t](#struct_bd_addr_t) * | 待添加到白名单的对端设备地址 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 添加白名单成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_remove_white_list <a id="gap_ble_remove_white_list"></a>

```c
errcode_t gap_ble_remove_white_list(const bd_addr_t *addr)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 从 BLE 白名单中移除指定设备。
- 目标设备地址通过 [bd_addr_t](#struct_bd_addr_t) 结构体指针传入。
- 用于删除白名单中的特定设备条目。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后调用。
- 依赖关系：依赖 BTS 协议栈已就绪、设备已存在于白名单。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | [bd_addr_t](#struct_bd_addr_t) * | 待移除的对端设备地址 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 移除白名单成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_get_white_list <a id="gap_ble_get_white_list"></a>

```c
errcode_t gap_ble_get_white_list(void)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 触发获取 BLE 白名单中的设备。
- 白名单获取结果通过 [gap_ble_get_white_list_callback](#typedef_gap_ble_get_white_list_callback) 回调上报。
- 用于查询当前白名单内容。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 获取请求成功发起，结果通过回调上报 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_remove_all_pairs <a id="gap_ble_remove_all_pairs"></a>

```c
errcode_t gap_ble_remove_all_pairs(void)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 删除本端所有已配对的 BLE 设备。
- 一次清除全部配对关系。
- 用于重置配对状态。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 删除所有配对成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_get_bonded_devices <a id="gap_ble_get_bonded_devices"></a>

```c
errcode_t gap_ble_get_bonded_devices(bd_addr_t *addr, uint16_t *number)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 获取本端已绑定设备的地址列表。
- 地址列表通过出参 `addr` 缓冲区回填，`number` 兼作入参与出参。
- 用于查询当前所有已绑定设备的地址。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| number | uint16_t * | 入参为缓冲区可容纳的设备数，出参为实际绑定设备数 | 不为 NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| addr | [bd_addr_t](#struct_bd_addr_t) * | 已绑定设备地址列表，由函数填充 |
| number | uint16_t * | 实际已绑定设备数量 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 地址列表获取成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_connect_param_update <a id="gap_ble_connect_param_update"></a>

```c
errcode_t gap_ble_connect_param_update(gap_conn_param_update_t *params)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 更新指定连接的 BLE 连接参数。
- 参数通过 [gap_conn_param_update_t](#struct_gap_conn_param_update_t) 结构体指针传入。
- 用于在连接建立后调整连接间隔、从机延迟与超时倍数。

**前置条件**

- 调用时序约束：需在 ACL 链路建立成功后调用。
- 依赖关系：依赖 BTS 协议栈已就绪、连接已建立。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| params | [gap_conn_param_update_t](#struct_gap_conn_param_update_t) * | 待更新的连接参数 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 连接参数更新成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`

### gap_ble_connect_remote_device <a id="gap_ble_connect_remote_device"></a>

```c
errcode_t gap_ble_connect_remote_device(const bd_addr_t *addr)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 与指定远端设备建立 ACL 连接。
- 目标设备地址通过 [bd_addr_t](#struct_bd_addr_t) 结构体指针传入。
- 连接状态通过 [gap_ble_connect_state_changed_callback](#typedef_gap_ble_connect_state_changed_callback) 回调上报。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | [bd_addr_t](#struct_bd_addr_t) * | 待连接的远端设备地址 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 连接请求成功发起，最终状态通过回调上报 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_disconnect_remote_device <a id="gap_ble_disconnect_remote_device"></a>

```c
errcode_t gap_ble_disconnect_remote_device(const bd_addr_t *addr)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 断开与指定远端设备的连接，包括所有 profile 连接。
- 目标设备地址通过 [bd_addr_t](#struct_bd_addr_t) 结构体指针传入。
- 连接状态通过 [gap_ble_connect_state_changed_callback](#typedef_gap_ble_connect_state_changed_callback) 回调上报。

**前置条件**

- 调用时序约束：需在与远端设备建立 ACL 连接之后调用。
- 依赖关系：依赖 BTS 协议栈已就绪、连接处于已建立状态。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | [bd_addr_t](#struct_bd_addr_t) * | 待断开的远端设备地址 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 断连请求成功发起，最终状态通过回调上报 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_set_sec_param <a id="gap_ble_set_sec_param"></a>

```c
errcode_t gap_ble_set_sec_param(gap_ble_sec_params_t *params)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 设置 BLE 安全参数。
- 参数通过 [gap_ble_sec_params_t](#struct_gap_ble_sec_params_t) 结构体指针传入。
- 用于配置绑定能力、输入输出能力、安全配对能力与安全模式。

**前置条件**

- 调用时序约束：需在协议栈初始化完成、发起配对之前调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| params | [gap_ble_sec_params_t](#struct_gap_ble_sec_params_t) * | 安全参数 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 安全参数设置成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_read_remote_device_rssi <a id="gap_ble_read_remote_device_rssi"></a>

```c
errcode_t gap_ble_read_remote_device_rssi(uint16_t conn_id)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 读取指定连接的远端设备 RSSI（Received Signal Strength Indicator）。
- 通过连接 ID 指定目标连接。
- RSSI 结果通过 [gap_ble_read_rssi_callback](#typedef_gap_ble_read_rssi_callback) 回调上报。

**前置条件**

- 调用时序约束：需在 ACL 链路建立成功后调用。
- 依赖关系：依赖 BTS 协议栈已就绪、连接已建立。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| conn_id | uint16_t | 连接 ID | 0 ~ 65535 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 读取请求成功发起，RSSI 结果通过回调上报 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_register_callbacks <a id="gap_ble_register_callbacks"></a>

```c
errcode_t gap_ble_register_callbacks(gap_ble_callbacks_t *func)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 注册 BLE GAP 回调函数集合。
- 回调集合通过 [gap_ble_callbacks_t](#struct_gap_ble_callbacks_t) 结构体指针传入。
- 注册后 BTS 在广播、扫描、连接、配对、认证等事件发生时回调对应接口上报给上层。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后、发起广播/扫描/连接之前调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func | [gap_ble_callbacks_t](#struct_gap_ble_callbacks_t) * | 指向回调函数集合的指针 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 回调函数注册成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`
- `src/application/samples/bt/ble/ble_wifi_cfg_server/src/ble_wifi_cfg_server.c`

### bth_ota_init <a id="bth_ota_init"></a>

```c
errcode_t bth_ota_init(void)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 初始化 bth OTA（Over-The-Air） 通道。
- 用于建立 OTA 升级所需的底层通道资源。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | OTA 通道初始化成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### ble_customize_max_pwr <a id="ble_customize_max_pwr"></a>

```c
errcode_t ble_customize_max_pwr(int8_t ble_pwr, int8_t sle_pwr)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 配置 BLE 与 SLE（Star Flash Low Energy）最大发射功率定制化信息。
- 通过入参分别指定 BLE 与 SLE 的最大功率。
- 用于将定制化功率参数写入生效。

**前置条件**

- 调用时序约束：需在协议栈初始化完成、发起射频业务之前调用。
- 依赖关系：依赖 NV（Non-Volatile） 定制化配置模块已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| ble_pwr | int8_t | BLE 最大功率，单位 dbm | -127 ~ 20（范围取自同头文件 tx_power 字段注释；实现闭源，无进一步校验依据） |
| sle_pwr | int8_t | SLE 最大功率，单位 dbm | -127 ~ 20（范围取自同头文件 tx_power 字段注释；实现闭源，无进一步校验依据） |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 定制化功率配置成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### ble_set_nv_pair_keys <a id="ble_set_nv_pair_keys"></a>

```c
errcode_t ble_set_nv_pair_keys(ble_auth_info_evt_t *key, bd_addr_t *own_addr, bd_addr_t *peer_addr, uint8_t index)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 将 SMP 配对密钥写入 Flash 持久化存储。
- 密钥通过 [ble_auth_info_evt_t](#struct_ble_auth_info_evt_t) 结构体指针传入，并关联本端地址与对端地址。
- 通过 `index` 指定密钥存储下标。

**前置条件**

- 调用时序约束：需在配对完成、获得认证信息之后调用。
- 依赖关系：依赖 BTS 协议栈与 Flash 存储已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| key | [ble_auth_info_evt_t](#struct_ble_auth_info_evt_t) * | 指向 SMP 配对密钥的指针 | 不为 NULL |
| own_addr | [bd_addr_t](#struct_bd_addr_t) * | 指向本端地址的指针 | 不为 NULL |
| peer_addr | [bd_addr_t](#struct_bd_addr_t) * | 指向对端地址的指针 | 不为 NULL |
| index | uint8_t | 密钥的下标索引 | 0 ~ 255 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 密钥写入 Flash 成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_set_save_smp_keys_mode <a id="gap_ble_set_save_smp_keys_mode"></a>

```c
errcode_t gap_ble_set_save_smp_keys_mode(uint8_t is_available)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 设置 SMP 配对密钥的保存模式。
- 模式取值参考 [gap_ble_save_pair_keys_mode_switch_t](#enum_gap_ble_save_pair_keys_mode_switch_t)。
- 用于选择自动保存或用户手动保存配对密钥。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| is_available | uint8_t | 配对密钥保存模式 | [GAP_BLE_SAVE_SMP_KEYS_AUTO](#enum_gap_ble_save_pair_keys_mode_switch_t)：0；<br>[GAP_BLE_SAVE_SMP_KEYS_MANU](#enum_gap_ble_save_pair_keys_mode_switch_t)：1。 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 保存模式设置成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### gap_ble_set_pair_info_available <a id="gap_ble_set_pair_info_available"></a>

```c
errcode_t gap_ble_set_pair_info_available(uint8_t is_available)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_le_gap.h"
```

**功能说明**

- 设置配对信息是否可获取的开关。
- 开关取值参考 [gap_ble_pair_info_switch_t](#enum_gap_ble_pair_info_switch_t)。
- 用于控制配对信息的可获取性。

**前置条件**

- 调用时序约束：需在协议栈初始化完成之后调用。
- 依赖关系：依赖 BTS 协议栈已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| is_available | uint8_t | 配对信息可获取开关 | [GAP_BLE_PAIR_INFO_UNAVAILABLE](#enum_gap_ble_pair_info_switch_t)：0；<br>[GAP_BLE_PAIR_INFO_AVAILABLE](#enum_gap_ble_pair_info_switch_t)：1。 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC：0 | 成功执行 | 开关设置成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

## Type definitions

### typedef_gap_ble_start_adv_callback <a id="typedef_gap_ble_start_adv_callback"></a>

```c
typedef void (*gap_ble_start_adv_callback)(uint8_t adv_id, adv_status_t status);
```

**使用说明**

启动广播结果回调函数指针类型，BTS 在每次启动广播后调用该回调向应用层上报启动结果。

回调说明：
- 调用时机：广播启动完成后在 BTS 线程被调用，不应阻塞或长时间等待。
- 参数 adv_id：广播 ID。
- 参数 status：当前广播状态，参考 [adv_status_t](#enum_adv_status_t)。
- 返回值处理：无返回值。

### typedef_gap_ble_stop_adv_callback <a id="typedef_gap_ble_stop_adv_callback"></a>

```c
typedef void (*gap_ble_stop_adv_callback)(uint8_t adv_id, adv_status_t status);
```

**使用说明**

停止广播结果回调函数指针类型，BTS 在每次停止广播后调用该回调向应用层上报停止结果。

回调说明：
- 调用时机：广播停止完成后在 BTS 线程被调用，不应阻塞或长时间等待。
- 参数 adv_id：广播 ID。
- 参数 status：当前广播状态，参考 [adv_status_t](#enum_adv_status_t)。
- 返回值处理：无返回值。

### typedef_gap_ble_set_adv_data_callback <a id="typedef_gap_ble_set_adv_data_callback"></a>

```c
typedef void (*gap_ble_set_adv_data_callback)(uint8_t adv_id, errcode_t status);
```

**使用说明**

设置广播数据结果回调函数指针类型，BTS 在每次设置广播数据后调用该回调向应用层上报设置结果。

回调说明：
- 调用时机：广播数据设置完成后在 BTS 线程被调用，不应阻塞或长时间等待。
- 参数 adv_id：广播 ID。
- 参数 status：执行结果错误码。
- 返回值处理：无返回值。

### typedef_gap_ble_set_adv_param_callback <a id="typedef_gap_ble_set_adv_param_callback"></a>

```c
typedef void (*gap_ble_set_adv_param_callback)(uint8_t adv_id, errcode_t status);
```

**使用说明**

设置广播参数结果回调函数指针类型，BTS 在每次设置广播参数后调用该回调向应用层上报更新结果。

回调说明：
- 调用时机：广播参数设置完成后在 BTS 线程被调用，不应阻塞或长时间等待。
- 参数 adv_id：广播 ID。
- 参数 status：执行结果错误码。
- 返回值处理：无返回值。

### typedef_gap_ble_scan_result_callback <a id="typedef_gap_ble_scan_result_callback"></a>

```c
typedef void (*gap_ble_scan_result_callback)(gap_scan_result_data_t *scan_result_data);
```

**使用说明**

扫描结果回调函数指针类型，BTS 在每次收到扫描结果后调用该回调向应用层上报扫描结果数据。

回调说明：
- 调用时机：收到扫描结果后在 BTS 线程被调用，不应阻塞或长时间等待。
- 参数 scan_result_data：扫描结果数据，参考 [gap_scan_result_data_t](#struct_gap_scan_result_data_t)，内存由 BTS 申请与释放，回调中不应释放。
- 返回值处理：无返回值。

### typedef_gap_ble_set_scan_param_callback <a id="typedef_gap_ble_set_scan_param_callback"></a>

```c
typedef void (*gap_ble_set_scan_param_callback)(errcode_t status);
```

**使用说明**

扫描参数设置完成回调函数指针类型，BTS 在扫描参数设置完成后调用该回调向应用层上报设置状态。

回调说明：
- 调用时机：扫描参数设置完成后在 BTS 线程被调用，不应阻塞或长时间等待。
- 参数 status：执行结果错误码。
- 返回值处理：无返回值。

### typedef_gap_ble_connect_state_changed_callback <a id="typedef_gap_ble_connect_state_changed_callback"></a>

```c
typedef void (*gap_ble_connect_state_changed_callback)(uint16_t conn_id, bd_addr_t *addr,
    gap_ble_conn_state_t conn_state, gap_ble_pair_state_t pair_state, gap_ble_disc_reason_t disc_reason);
```

**使用说明**

连接状态改变回调函数指针类型，BTS 在连接完成后调用该回调向应用层上报连接状态信息。

回调说明：
- 调用时机：连接状态改变时在 BTS 线程被调用，不应阻塞或长时间等待。
- 参数 conn_id：连接 ID。
- 参数 addr：对端设备地址，参考 [bd_addr_t](#struct_bd_addr_t)。
- 参数 conn_state：连接状态，参考 [gap_ble_conn_state_t](#enum_gap_ble_conn_state_t)。
- 参数 pair_state：配对状态，参考 [gap_ble_pair_state_t](#enum_gap_ble_pair_state_t)。
- 参数 disc_reason：断链原因，参考 [gap_ble_disc_reason_t](#enum_gap_ble_disc_reason_t)。
- 返回值处理：无返回值。

### typedef_gap_ble_paired_complete_callback <a id="typedef_gap_ble_paired_complete_callback"></a>

```c
typedef void (*gap_ble_paired_complete_callback)(uint16_t conn_id, const bd_addr_t *addr, errcode_t status);
```

**使用说明**

配对完成回调函数指针类型，BTS 在配对后调用该回调向应用层上报配对状态信息。

回调说明：
- 调用时机：配对完成后在 BTS 线程被调用，不应阻塞或长时间等待。
- 参数 conn_id：连接 ID。
- 参数 addr：对端设备地址，参考 [bd_addr_t](#struct_bd_addr_t)。
- 参数 status：执行结果错误码。
- 返回值处理：无返回值。

### typedef_gap_ble_terminate_adv_callback <a id="typedef_gap_ble_terminate_adv_callback"></a>

```c
typedef void (*gap_ble_terminate_adv_callback)(uint8_t adv_id, adv_status_t status);
```

**使用说明**

被动中止广播回调函数指针类型，BTS 在广播被中止时调用该回调向应用层上报广播状态。

回调说明：
- 调用时机：广播被中止时在 BTS 线程被调用，不应阻塞或长时间等待。
- 参数 adv_id：广播 ID。
- 参数 status：广播状态，参考 [adv_status_t](#enum_adv_status_t)。
- 返回值处理：无返回值。

### typedef_gap_ble_read_rssi_callback <a id="typedef_gap_ble_read_rssi_callback"></a>

```c
typedef void (*gap_ble_read_rssi_callback)(uint16_t conn_id, int8_t rssi, errcode_t status);
```

**使用说明**

读取 RSSI 结果回调函数指针类型，BTS 在 RSSI 读取完成后调用该回调向应用层上报结果。

回调说明：
- 调用时机：RSSI 读取完成后在 service 线程被调用，不应阻塞或长时间等待。
- 参数 conn_id：连接 ID。
- 参数 rssi：RSSI 值。
- 参数 status：执行结果错误码。
- 返回值处理：无返回值。

### typedef_gap_ble_set_data_length_callback <a id="typedef_gap_ble_set_data_length_callback"></a>

```c
typedef void (*gap_ble_set_data_length_callback)(uint16_t conn_id, errcode_t status);
```

**使用说明**

设置数据长度结果回调函数指针类型，BTS 在数据长度设置完成后调用该回调向应用层上报结果。

回调说明：
- 调用时机：数据长度设置完成后在 service 线程被调用，不应阻塞或长时间等待。
- 参数 conn_id：连接 ID。
- 参数 status：执行结果错误码。
- 返回值处理：无返回值。

### typedef_gap_ble_auth_complete_callback <a id="typedef_gap_ble_auth_complete_callback"></a>

```c
typedef void (*gap_ble_auth_complete_callback)(uint16_t conn_id, const bd_addr_t *addr, errcode_t status,
    const ble_auth_info_evt_t* evt);
```

**使用说明**

认证完成回调函数指针类型，BTS 在认证完成后调用该回调向应用层上报认证结果。

回调说明：
- 调用时机：认证完成后在 service 线程被调用，不应阻塞或长时间等待。
- 参数 conn_id：连接 ID。
- 参数 addr：对端设备地址，参考 [bd_addr_t](#struct_bd_addr_t)。
- 参数 status：执行结果错误码。
- 参数 evt：认证事件信息，参考 [ble_auth_info_evt_t](#struct_ble_auth_info_evt_t)。
- 返回值处理：无返回值。

### typedef_gap_ble_connect_param_update_callback <a id="typedef_gap_ble_connect_param_update_callback"></a>

```c
typedef void (*gap_ble_connect_param_update_callback)(uint16_t conn_id, errcode_t status,
    const gap_ble_conn_param_update_t *param);
```

**使用说明**

连接参数更新回调函数指针类型，BTS 在连接参数更新完成时调用该回调向应用层上报结果。

回调说明：
- 调用时机：连接参数更新完成后在 service 线程被调用，不应阻塞或长时间等待。
- 参数 conn_id：连接 ID。
- 参数 status：执行结果错误码。
- 参数 param：连接参数，参考 [gap_ble_conn_param_update_t](#struct_gap_ble_conn_param_update_t)。
- 返回值处理：无返回值。

### typedef_gap_ble_get_white_list_callback <a id="typedef_gap_ble_get_white_list_callback"></a>

```c
typedef void (*gap_ble_get_white_list_callback)(uint8_t count, bd_addr_t *addr_list);
```

**使用说明**

获取白名单回调函数指针类型，BTS 在白名单获取完成后调用该回调向应用层上报白名单内容。

回调说明：
- 调用时机：白名单获取完成后在 service 线程被调用，不应阻塞或长时间等待。
- 参数 count：白名单中的地址数目。
- 参数 addr_list：白名单中的地址列表，参考 [bd_addr_t](#struct_bd_addr_t)。
- 返回值处理：无返回值。

## Enumerations

### enum_gap_ble_appearance_type_t <a id="enum_gap_ble_appearance_type_t"></a>

```c
typedef enum {
    GAP_BLE_APPEARANCE_TYPE_UNKNOWN = 00,                  /*!< Unknown */
    GAP_BLE_APPEARANCE_TYPE_GENERIC_PHONE = 64,            /*!< Generic Phone */
    GAP_BLE_APPEARANCE_TYPE_GENERIC_COMPUTER = 128,        /*!< Generic Computer */
    GAP_BLE_APPEARANCE_TYPE_GENERIC_WATCH = 192,           /*!< Generic Watch */
    GAP_BLE_APPEARANCE_TYPE_GENERIC_DISPLAY = 320,         /*!< Generic Display */
    GAP_BLE_APPEARANCE_TYPE_GENERIC_HID = 960,             /*!< Generic Human Interface Device */
    GAP_BLE_APPEARANCE_TYPE_KEYBOARD = 961,                /*!< Keyboard */
    GAP_BLE_APPEARANCE_TYPE_MOUSE = 962,                   /*!< Mouse */
    GAP_BLE_APPEARANCE_TYPE_DIGITAL_PEN = 967,             /*!< Digital Pen */
} gap_ble_appearance_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GAP_BLE_APPEARANCE_TYPE_UNKNOWN | 00 | 未知类型 |
| GAP_BLE_APPEARANCE_TYPE_GENERIC_PHONE | 64 | 通用手机 |
| GAP_BLE_APPEARANCE_TYPE_GENERIC_COMPUTER | 128 | 通用电脑 |
| GAP_BLE_APPEARANCE_TYPE_GENERIC_WATCH | 192 | 通用手表 |
| GAP_BLE_APPEARANCE_TYPE_GENERIC_DISPLAY | 320 | 通用显示器 |
| GAP_BLE_APPEARANCE_TYPE_GENERIC_HID | 960 | 通用人机界面设备 |
| GAP_BLE_APPEARANCE_TYPE_KEYBOARD | 961 | 键盘 |
| GAP_BLE_APPEARANCE_TYPE_MOUSE | 962 | 鼠标 |
| GAP_BLE_APPEARANCE_TYPE_DIGITAL_PEN | 967 | 电子笔 |

### enum_gap_ble_adv_filter_allow_scan_t <a id="enum_gap_ble_adv_filter_allow_scan_t"></a>

```c
typedef enum {
    GAP_BLE_ADV_FILTER_ALLOW_SCAN_ANY_CON_ANY = 0x00,   /*!< Accepts all scan and connect requests */
    GAP_BLE_ADV_FILTER_ALLOW_SCAN_WLST_CON_ANY = 0x01,  /*!< Accepts all connect but white list scan requests */
    GAP_BLE_ADV_FILTER_ALLOW_SCAN_ANY_CON_WLST = 0x02,  /*!< Accepts all scan but white list connect requests */
    GAP_BLE_ADV_FILTER_ALLOW_SCAN_WLST_CON_WLST = 0x03, /*!< Accepts only white list connect and scan requests */
} gap_ble_adv_filter_allow_scan_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GAP_BLE_ADV_FILTER_ALLOW_SCAN_ANY_CON_ANY | 0x00 | 处理所有设备的扫描和连接请求 |
| GAP_BLE_ADV_FILTER_ALLOW_SCAN_WLST_CON_ANY | 0x01 | 处理所有连接请求，仅处理白名单的扫描请求 |
| GAP_BLE_ADV_FILTER_ALLOW_SCAN_ANY_CON_WLST | 0x02 | 处理所有扫描请求，仅处理白名单的连接请求 |
| GAP_BLE_ADV_FILTER_ALLOW_SCAN_WLST_CON_WLST | 0x03 | 仅处理白名单中扫描请求和连接请求 |

### enum_gap_ble_adv_type_t <a id="enum_gap_ble_adv_type_t"></a>

```c
typedef enum {
    GAP_BLE_ADV_CONN_SCAN_UNDIR = 0,        /*!< Connectable, scanable, undirected advertising(default). */
    GAP_BLE_ADV_CONN_NONSCAN_DIR,           /*!< Connectable, nonscanble, high duty directed advertising. */
    GAP_BLE_ADV_NONCONN_SCAN_UNDIR,         /*!< Nonconnectable, scanable, undirected advertising. */
    GAP_BLE_ADV_NONCONN_NONSCAN_UNDIR,      /*!< Nonconnectable, nonscanable, undirected advertising. */
    GAP_BLE_ADV_CONN_NONSCAN_DIR_LOW_DUTY,  /*!< Connectable, nonscanble, low duty directed advertising. */
} gap_ble_adv_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GAP_BLE_ADV_CONN_SCAN_UNDIR | 0 | 可连接可扫描非定向广播（默认） |
| GAP_BLE_ADV_CONN_NONSCAN_DIR | 1 | 可连接不可扫描高频定向广播 |
| GAP_BLE_ADV_NONCONN_SCAN_UNDIR | 2 | 不可连接可扫描非定向广播 |
| GAP_BLE_ADV_NONCONN_NONSCAN_UNDIR | 3 | 不可连接不可扫描非定向广播 |
| GAP_BLE_ADV_CONN_NONSCAN_DIR_LOW_DUTY | 4 | 可连接不可扫描低频定向广播 |

### enum_gap_ble_scan_type_t <a id="enum_gap_ble_scan_type_t"></a>

```c
typedef enum {
    GAP_BLE_SCAN_TYPE_PASSIVE = 0x00, /*!< Passive scan */
    GAP_BLE_SCAN_TYPE_ACTIVE,         /*!< Active scan */
} gap_ble_scan_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GAP_BLE_SCAN_TYPE_PASSIVE | 0x00 | 被动扫描 |
| GAP_BLE_SCAN_TYPE_ACTIVE | 0x1 | 主动扫描 |

### enum_gap_ble_scan_filter_policy_t <a id="enum_gap_ble_scan_filter_policy_t"></a>

```c
typedef enum {
    GAP_BLE_SCAN_FILTER_POLICY_ACCEPT_ALL = 0x00,       /*!< Accept all advertising packets except directed
                                                                     advertising packets not addressed to this device
                                                                     (default) */
    GAP_BLE_SCAN_FILTER_POLICY_ONLY_WHITE_LIST,         /*!< Accept only advertisement packets from white list
                                                                     devices. Directed advertising packets which are
                                                                     not addressed for this device shall be ignored */
    GAP_BLE_SCAN_FILTER_POLICY_ACCEPT_ALL_AND_RPA,      /*!< Accept all undirected advertisement packets, and
                                                                     all directed advertising packets where the
                                                                     initiator address is a resolvable private address,
                                                                     and all directed advertising packets addressed to
                                                                     this device */
    GAP_BLE_SCAN_FILTER_POLICY_ONLY_WHITE_LIST_AND_RPA, /*!< Accept all undirected advertisement packets from
                                                                     devices where the advertiser's address is in the
                                                                     White list, and all directed advertising packets
                                                                     where the initiator address is a resolvable
                                                                     private address, and all directed advertising
                                                                     packets addressed to this device */
} gap_ble_scan_filter_policy_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GAP_BLE_SCAN_FILTER_POLICY_ACCEPT_ALL | 0x00 | 接收所有广播，不接收目标地址不是本设备地址的定向广播（默认） |
| GAP_BLE_SCAN_FILTER_POLICY_ONLY_WHITE_LIST | 0x1 | 只接收白名单里设备的广播，不接收目标地址不是本设备地址的定向广播 |
| GAP_BLE_SCAN_FILTER_POLICY_ACCEPT_ALL_AND_RPA | 0x2 | 接收所有的非定向广播、地址是可解析私有地址的广播方发送的定向广播、发给该设备的定向广播 |
| GAP_BLE_SCAN_FILTER_POLICY_ONLY_WHITE_LIST_AND_RPA | 0x3 | 接收白名单中的所有非定向广播、地址是可解析私有地址的广播方发送的定向广播、发给该设备的定向广播 |

### enum_gap_ble_scan_result_evt_type_t <a id="enum_gap_ble_scan_result_evt_type_t"></a>

```c
typedef enum {
    GAP_BLE_EVT_NON_CONNECTABLE_NON_SCANNABLE = 0x00,          /*!< Non-connectable, non-scannable, undirected */
    GAP_BLE_EVT_NON_CONNECTABLE_NON_SCANNABLE_DIRECTED = 0x04, /*!< Non-connectable, non-scannable, directed */
    GAP_BLE_EVT_CONNECTABLE = 0x01,                            /*!< Connectable and undirected */
    GAP_BLE_EVT_CONNECTABLE_DIRECTED = 0x05,                   /*!< Connectable and directed */
    GAP_BLE_EVT_SCANNABLE = 0x02,                              /*!< Scannable and undirected */
    GAP_BLE_EVT_SCANNABLE_DIRECTED = 0x06,                     /*!< Scannable and directed */
    GAP_BLE_EVT_LEGACY_NON_CONNECTABLE = 0x10,                 /*!< Legacy, non-connectable and undirected */
    GAP_BLE_EVT_LEGACY_SCANNABLE = 0x12,                       /*!< Legacy, scannable and undirected */
    GAP_BLE_EVT_LEGACY_CONNECTABLE = 0x13,                     /*!< Legacy, connectable, scannable and
                                                                            undirected */
    GAP_BLE_EVT_LEGACY_CONNECTABLE_DIRECTED = 0x15,            /*!< Legacy, connectable, and directed */
    GAP_BLE_EVT_LEGACY_SCAN_RSP_TO_ADV_SCAN = 0x1A,            /*!< Legacy scan response corresponding to
                                                                            ADV_SCAN_IND */
    GAP_BLE_EVT_LEGACY_SCAN_RSP_TO_ADV = 0x1B                  /*!< Legacy scan response corresponding to
                                                                            ADV_IND */
} gap_ble_scan_result_evt_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GAP_BLE_EVT_NON_CONNECTABLE_NON_SCANNABLE | 0x00 | 扩展的不可连接不可扫描非定向 |
| GAP_BLE_EVT_NON_CONNECTABLE_NON_SCANNABLE_DIRECTED | 0x04 | 扩展的不可连接不可扫描定向 |
| GAP_BLE_EVT_CONNECTABLE | 0x01 | 扩展的可连接非定向 |
| GAP_BLE_EVT_CONNECTABLE_DIRECTED | 0x05 | 扩展的可连接定向 |
| GAP_BLE_EVT_SCANNABLE | 0x02 | 扩展的可扫描非定向 |
| GAP_BLE_EVT_SCANNABLE_DIRECTED | 0x06 | 扩展的可扫描定向 |
| GAP_BLE_EVT_LEGACY_NON_CONNECTABLE | 0x10 | 传统的不可连接非定向 |
| GAP_BLE_EVT_LEGACY_SCANNABLE | 0x12 | 传统的可扫描非定向 |
| GAP_BLE_EVT_LEGACY_CONNECTABLE | 0x13 | 传统的可连接可扫描非定向 |
| GAP_BLE_EVT_LEGACY_CONNECTABLE_DIRECTED | 0x15 | 传统的可连接定向 |
| GAP_BLE_EVT_LEGACY_SCAN_RSP_TO_ADV_SCAN | 0x1A | 传统的与 ADV_SCAN_IND 对应的扫描响应 |
| GAP_BLE_EVT_LEGACY_SCAN_RSP_TO_ADV | 0x1B | 传统的与 ADV_IND 对应的扫描响应 |

### enum_gap_ble_pair_info_switch_t <a id="enum_gap_ble_pair_info_switch_t"></a>

```c
typedef enum {
    GAP_BLE_PAIR_INFO_UNAVAILABLE = 0x00,          /*!< Pair information unavailable */
    GAP_BLE_PAIR_INFO_AVAILABLE = 0x01,            /*!< Pair information available */
} gap_ble_pair_info_switch_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GAP_BLE_PAIR_INFO_UNAVAILABLE | 0x00 | 配对信息不可获取 |
| GAP_BLE_PAIR_INFO_AVAILABLE | 0x01 | 配对信息可获取 |

### enum_gap_ble_save_pair_keys_mode_switch_t <a id="enum_gap_ble_save_pair_keys_mode_switch_t"></a>

```c
typedef enum {
    GAP_BLE_SAVE_SMP_KEYS_AUTO = 0x00,          /*!< Pair information unavailable */
    GAP_BLE_SAVE_SMP_KEYS_MANU = 0x01,            /*!< Pair information available */
} gap_ble_save_pair_keys_mode_switch_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GAP_BLE_SAVE_SMP_KEYS_AUTO | 0x00 | 秘钥自动保存 |
| GAP_BLE_SAVE_SMP_KEYS_MANU | 0x01 | 秘钥用户手动保存 |

### enum_gap_ble_scan_result_data_status_t <a id="enum_gap_ble_scan_result_data_status_t"></a>

```c
typedef enum {
    GAP_BLE_DATA_COMPLETE = 0x00,                /*!< Complete, or last segment */
    GAP_BLE_DATA_INCOMPLETE_MORE_TO_COME = 0x01, /*!< Incomplete */
    GAP_BLE_DATA_INCOMPLETE_TRUNCATED = 0x02,    /*!< Truncated */
} gap_ble_scan_result_data_status_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GAP_BLE_DATA_COMPLETE | 0x00 | 完整数据或最后一个片段 |
| GAP_BLE_DATA_INCOMPLETE_MORE_TO_COME | 0x01 | 不完整的数据 |
| GAP_BLE_DATA_INCOMPLETE_TRUNCATED | 0x02 | 被截断不完整的数据 |

### enum_gap_ble_phy_type_t <a id="enum_gap_ble_phy_type_t"></a>

```c
typedef enum {
    GAP_BLE_PHY_NO_PACKET = 0x00, /*!< No packet */
    GAP_BLE_PHY_1M = 0x01,        /*!< 1M PHY */
    GAP_BLE_PHY_2M = 0x02,        /*!< 2M PHY */
    GAP_BLE_PHY_CODED = 0x03      /*!< Coded PHY */
} gap_ble_phy_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GAP_BLE_PHY_NO_PACKET | 0x00 | 无广播包 |
| GAP_BLE_PHY_1M | 0x01 | 1M PHY |
| GAP_BLE_PHY_2M | 0x02 | 2M PHY |
| GAP_BLE_PHY_CODED | 0x03 | Coded PHY |

### enum_adv_status_t <a id="enum_adv_status_t"></a>

```c
typedef enum {
    ADV_STATUS_STOPPED = 0x00, /*!< advertising stoped */
    ADV_STATUS_ADVERTISING,    /*!< advertising */
} adv_status_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| ADV_STATUS_STOPPED | 0x00 | 广播停止 |
| ADV_STATUS_ADVERTISING | 0x1 | 正在广播 |

### enum_gap_ble_sec_mode_t <a id="enum_gap_ble_sec_mode_t"></a>

```c
typedef enum {
    GAP_BLE_GAP_SECURITY_MODE1_LEVEL1 = 0,     /*!< No security */
    GAP_BLE_GAP_SECURITY_MODE1_LEVEL2,         /*!< Unauthenticated pairing and encryption */
    GAP_BLE_GAP_SECURITY_MODE1_LEVEL3,         /*!< Authenticated Pairing and encryption */
    GAP_BLE_GAP_SECURITY_MODE1_LEVEL4,         /*!< Authenticated ECDH Pairing and encryption */
    GAP_BLE_GAP_SECURITY_MODE2_LEVEL1,         /*!< Unauthenticated pairing and data signing */
    GAP_BLE_GAP_SECURITY_MODE2_LEVEL2,         /*!< Authenticated pairing and data signing */
} gap_ble_sec_mode_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GAP_BLE_GAP_SECURITY_MODE1_LEVEL1 | 0 | 没有安全能力 |
| GAP_BLE_GAP_SECURITY_MODE1_LEVEL2 | 1 | 不需要认证基于链路进行配对和加密 |
| GAP_BLE_GAP_SECURITY_MODE1_LEVEL3 | 2 | 需要认证基于链路进行配对和加密 |
| GAP_BLE_GAP_SECURITY_MODE1_LEVEL4 | 3 | 需要认证基于链路采用 ECDH 算法进行加密和配对 |
| GAP_BLE_GAP_SECURITY_MODE2_LEVEL1 | 4 | 不需要认证基于数据进行配对和加密 |
| GAP_BLE_GAP_SECURITY_MODE2_LEVEL2 | 5 | 需要认证基于数据进行配对和加密 |

### enum_gap_ble_io_ability_t <a id="enum_gap_ble_io_ability_t"></a>

```c
typedef enum {
    GAP_BLE_IO_CAPABILITY_DISPLAYONLY = 0,     /*!< only display */
    GAP_BLE_IO_CAPABILITY_DISPLAYYESNO,        /*!< display and select yes or no */
    GAP_BLE_IO_CAPABILITY_KEYBOARDONLY,        /*!< only keyboard */
    GAP_BLE_IO_CAPABILITY_NOINPUTNOOUTPUT,     /*!< no input and no output */
    GAP_BLE_IO_CAPABILITY_KEYBOARDDISPLAY,     /*!< display and keyboard */
} gap_ble_io_ability_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GAP_BLE_IO_CAPABILITY_DISPLAYONLY | 0 | 只展示 |
| GAP_BLE_IO_CAPABILITY_DISPLAYYESNO | 1 | 展示，并且可以选择 Yes 或者 No |
| GAP_BLE_IO_CAPABILITY_KEYBOARDONLY | 2 | 只支持键盘 |
| GAP_BLE_IO_CAPABILITY_NOINPUTNOOUTPUT | 3 | 没有输入输出 |
| GAP_BLE_IO_CAPABILITY_KEYBOARDDISPLAY | 4 | 支持键盘和展示 |

### enum_gap_ble_filter_duplicates_t <a id="enum_gap_ble_filter_duplicates_t"></a>

```c
typedef enum {
    GAP_BLE_FILTER_DUPLICATES_DISABLE = 0,       /*!< reports each received broadcast packet */
    GAP_BLE_FILTER_DUPLICATES_ENABLE,            /*!< do not report duplicate broadcast packets */
    GAP_BLE_FILTER_DUPLICATES_ENABLE_FOR_PERIOD, /*!< do not report duplicate broadcast packets
                                                              in a period. */
} gap_ble_filter_duplicates_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GAP_BLE_FILTER_DUPLICATES_DISABLE | 0 | 上报每个收到的广播包 |
| GAP_BLE_FILTER_DUPLICATES_ENABLE | 1 | 不上报重复的广播包 |
| GAP_BLE_FILTER_DUPLICATES_ENABLE_FOR_PERIOD | 2 | 周期内不上报重复的广播包 |

### enum_gap_ble_pair_state_t <a id="enum_gap_ble_pair_state_t"></a>

```c
typedef enum {
    GAP_BLE_PAIR_NONE = 0x01,    /*!< Pair state of none */
    GAP_BLE_PAIR_PAIRING = 0x02, /*!< Pair state of pairing */
    GAP_BLE_PAIR_PAIRED = 0x03   /*!< Pair state of paired */
} gap_ble_pair_state_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GAP_BLE_PAIR_NONE | 0x01 | 未配对状态 |
| GAP_BLE_PAIR_PAIRING | 0x02 | 正在配对 |
| GAP_BLE_PAIR_PAIRED | 0x03 | 已完成配对 |

### enum_gap_ble_disc_reason_t <a id="enum_gap_ble_disc_reason_t"></a>

```c
typedef enum {
    GAP_BLE_DISCONN_UNKNOWN              = 0x00,    /*!< disconnect by local */
    GAP_BLE_ERR_CONN_TIMEOUT             = 0x8,     /*!< disconnect by local */
    GAP_BLE_DICSCONNECT_BY_REMOTE_USER   = 0x13,    /*!< disconnect by remote */
    GAP_BLE_CONN_TERMINATE_BY_LOCAL_HOST = 0x16,    /*!< disconnect by remote */
} gap_ble_disc_reason_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GAP_BLE_DISCONN_UNKNOWN | 0x00 | 未知原因断链 |
| GAP_BLE_ERR_CONN_TIMEOUT | 0x8 | 连接超时断链 |
| GAP_BLE_DICSCONNECT_BY_REMOTE_USER | 0x13 | 远端用户断链 |
| GAP_BLE_CONN_TERMINATE_BY_LOCAL_HOST | 0x16 | 本端 HOST 断链 |

### enum_gap_ble_conn_state_t <a id="enum_gap_ble_conn_state_t"></a>

```c
typedef enum {
    GAP_BLE_STATE_DISCONNECTED,/*!< BLE GAP ACL state of disconnected */
    GAP_BLE_STATE_CONNECTED    /*!< BLE GAP ACL state of connected */
} gap_ble_conn_state_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GAP_BLE_STATE_DISCONNECTED | 0 | BLE GAP ACL 已断连 |
| GAP_BLE_STATE_CONNECTED | 1 | BLE GAP ACL 已连接 |

### enum_gap_le_link_bond_result_type_t <a id="enum_gap_le_link_bond_result_type_t"></a>

```c
typedef enum {
    GAP_BLE_LINK_BONDABLE,     /*!< BLE GAP LE BONDABLE */
    GAP_BLE_LINK_UNBONDABLE    /*!< BLE GAP LE UNBONDABLE */
} gap_le_link_bond_result_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GAP_BLE_LINK_BONDABLE | 0 | BLE GAP LE 支持绑定 |
| GAP_BLE_LINK_UNBONDABLE | 1 | BLE GAP LE 不支持绑定 |

## Structures

### struct_gap_conn_param_update_t <a id="struct_gap_conn_param_update_t"></a>

```c
typedef struct {
    uint16_t conn_handle;        /*!< connection id */
    uint16_t interval_min;       /*!< min interval */
    uint16_t interval_max;       /*!< max interval */
    uint16_t slave_latency;      /*!< slave reply min latency */
    uint16_t timeout_multiplier; /*!< interval for disconnection due to timeout */
} gap_conn_param_update_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| conn_handle | uint16_t | 连接 ID |
| interval_min | uint16_t | 最小间隔 |
| interval_max | uint16_t | 最大间隔 |
| slave_latency | uint16_t | 从设备回复最小间隔 |
| timeout_multiplier | uint16_t | 超时断连间隔 |

### struct_gap_le_set_phy_t <a id="struct_gap_le_set_phy_t"></a>

```c
typedef struct {
    uint16_t conn_handle;       /*!< conn handle */
    uint8_t all_phys;           /*!< all phys */
    uint8_t tx_phys;            /*!< tx phys */
    uint8_t rx_phys;            /*!< rx phys */
    uint16_t phy_options;       /*!< phy options */
} gap_le_set_phy_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| conn_handle | uint16_t | 连接句柄 |
| all_phys | uint8_t | 所有 PHY |
| tx_phys | uint8_t | 发送 PHY |
| rx_phys | uint8_t | 接收 PHY |
| phy_options | uint16_t | PHY 选项 |

### struct_gap_le_set_data_length_t <a id="struct_gap_le_set_data_length_t"></a>

```c
typedef struct {
    uint16_t conn_handle;       /*!< conn handle */
    uint16_t maxtxoctets;           /*!< maxtxoctets */
    uint16_t maxtxtime;            /*!< maxtxtime */
} gap_le_set_data_length_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| conn_handle | uint16_t | 连接句柄 |
| maxtxoctets | uint16_t | 最大字节数 |
| maxtxtime | uint16_t | 最大发送时间 |

### struct_gap_ble_config_adv_data_t <a id="struct_gap_ble_config_adv_data_t"></a>

```c
typedef struct {
    uint16_t adv_length;      /*!< Length of advertising data */
    uint8_t *adv_data;        /*!< Advertising data */
    uint16_t scan_rsp_length; /*!< Length of scan response data */
    uint8_t *scan_rsp_data;   /*!< Scan response data */
} gap_ble_config_adv_data_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| adv_length | uint16_t | 广播数据长度 |
| adv_data | uint8_t * | 广播数据 |
| scan_rsp_length | uint16_t | 扫描响应数据长度 |
| scan_rsp_data | uint8_t * | 扫描响应数据 |

### struct_gap_ble_adv_params_t <a id="struct_gap_ble_adv_params_t"></a>

```c
typedef struct {
    uint32_t min_interval;     /*!< Min interval[N * 0.625ms] */
    uint32_t max_interval;     /*!< Max interval[N * 0.625ms] */
    uint8_t adv_type;          /*!< Advertising type { @ref gap_ble_adv_type_t } */
    bd_addr_t own_addr;       /*!< own address */
    bd_addr_t peer_addr;       /*!< Peer address */
    uint8_t channel_map;       /*!< channel bitmap */
    uint8_t adv_filter_policy; /*!< Advertising filter policy
                                            { @ref gap_ble_adv_filter_allow_scan_t } */
    int8_t  tx_power;          /*!< Transmissive power */
    uint32_t duration;         /*!< Duration */
} gap_ble_adv_params_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| min_interval | uint32_t | 最小广播间隔，单位 N * 0.625 ms |
| max_interval | uint32_t | 最大广播间隔，单位 N * 0.625 ms |
| adv_type | uint8_t | 广播类型，参考 [gap_ble_adv_type_t](#enum_gap_ble_adv_type_t) |
| own_addr | bd_addr_t | 本端地址，参考 [bd_addr_t](#struct_bd_addr_t) |
| peer_addr | bd_addr_t | 对端地址，参考 [bd_addr_t](#struct_bd_addr_t) |
| channel_map | uint8_t | 广播通道选择：1 使用 37 通道；7 使用 37/38/39 三个通道 |
| adv_filter_policy | uint8_t | 白名单过滤策略，参考 [gap_ble_adv_filter_allow_scan_t](#enum_gap_ble_adv_filter_allow_scan_t) |
| tx_power | int8_t | 发送功率，单位 dbm，范围 -127 ~ 20 |
| duration | uint32_t | 广播持续发送时长 |

### struct_gap_ble_scan_params_t <a id="struct_gap_ble_scan_params_t"></a>

```c
typedef struct {
    uint16_t scan_interval;     /*!< Scan interval[N * 0.625ms] */
    uint16_t scan_window;       /*!< Scan window[N * 0.625ms] */
    uint8_t scan_type;          /*!< Scan type { @ref gap_ble_scan_type_t } */
    uint8_t scan_phy;           /*!< PHY type { @ref gap_ble_phy_type_t } */
    uint8_t scan_filter_policy; /*!< Scan fileter policy { @ref gap_ble_scan_filter_policy_t } */
} gap_ble_scan_params_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| scan_interval | uint16_t | 扫描间隔，单位 N * 0.625 ms |
| scan_window | uint16_t | 扫描窗长，单位 N * 0.625 ms |
| scan_type | uint8_t | 扫描类型，参考 [gap_ble_scan_type_t](#enum_gap_ble_scan_type_t) |
| scan_phy | uint8_t | PHY 类型，参考 [gap_ble_phy_type_t](#enum_gap_ble_phy_type_t) |
| scan_filter_policy | uint8_t | 扫描过滤策略，参考 [gap_ble_scan_filter_policy_t](#enum_gap_ble_scan_filter_policy_t) |

### struct_gap_scan_result_data_t <a id="struct_gap_scan_result_data_t"></a>

```c
typedef struct {
    uint8_t event_type;             /*!< Event type { @ref gap_ble_scan_result_evt_type_t } */
    uint8_t data_status;            /*!< Data status { @ref gap_ble_scan_result_data_status_t } */
    bd_addr_t addr;                 /*!< Address */
    uint8_t primary_phy;            /*!< primary PHY { @ref gap_ble_phy_type_t } */
    uint8_t secondary_phy;          /*!< secondary PHY { @ref gap_ble_phy_type_t } */
    uint8_t adv_sid;                /*!< Value of the Advertising SID subfield in the ADI field of the PDU */
    int8_t tx_power;                /*!< Transmissive power */
    int8_t rssi;                    /*!< RSSI */
    uint16_t periodic_adv_interval; /*!< Periodic advertising interval */
    bd_addr_t direct_addr;          /*!< Directed address */
    uint8_t adv_len;                /*!< Advertising data length */
    uint8_t *adv_data;              /*!< Advertising data */
} gap_scan_result_data_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| event_type | uint8_t | 广播类型，参考 [gap_ble_scan_result_evt_type_t](#enum_gap_ble_scan_result_evt_type_t) |
| data_status | uint8_t | 扫描结果数据状态，参考 [gap_ble_scan_result_data_status_t](#enum_gap_ble_scan_result_data_status_t) |
| addr | bd_addr_t | 地址，参考 [bd_addr_t](#struct_bd_addr_t) |
| primary_phy | uint8_t | 主广播 PHY 类型，参考 [gap_ble_phy_type_t](#enum_gap_ble_phy_type_t) |
| secondary_phy | uint8_t | 辅广播 PHY 类型，参考 [gap_ble_phy_type_t](#enum_gap_ble_phy_type_t) |
| adv_sid | uint8_t | 广播 SID |
| tx_power | int8_t | 发送功率，范围 -127 ~ +20 dBm |
| rssi | int8_t | 信号强度，范围 -127 ~ +20 dBm |
| periodic_adv_interval | uint16_t | 周期广播间隔，单位 N * 1.25 ms |
| direct_addr | bd_addr_t | 定向广播地址，参考 [bd_addr_t](#struct_bd_addr_t) |
| adv_len | uint8_t | 广播数据长度 |
| adv_data | uint8_t * | 广播数据 |

### struct_gap_ble_extern_scan_params_t <a id="struct_gap_ble_extern_scan_params_t"></a>

```c
typedef struct {
    uint8_t filter_duplicate; /*!< Scan filter duplicates { @ref gap_ble_filter_duplicates_t } */
    uint8_t limited;           /*!< Reserved field */
    uint16_t duration;        /*!< Indicates the scanning duration. The value 0 indicates
                                           continuous scanning. The default value is 0. Unit: 10 ms. */
    uint16_t period;          /*!< Indicates the scanning period. When the value is 0,
                                           the scanning ends after the specified duration.
                                           The default value is 0. Unit: 1.28s. */
} gap_ble_extern_scan_params_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| filter_duplicate | uint8_t | 扫描的过滤配置，参考 [gap_ble_filter_duplicates_t](#enum_gap_ble_filter_duplicates_t) |
| limited | uint8_t | 保留字段 |
| duration | uint16_t | 扫描持续时间，0 表示持续扫描，默认值为 0，单位 10 ms |
| period | uint16_t | 扫描周期，取 0 时扫描执行 duration 时间后超时结束，默认值为 0，单位 1.28 s |

### struct_gap_ble_conn_param_update_t <a id="struct_gap_ble_conn_param_update_t"></a>

```c
typedef struct {
    uint16_t interval;          /*!< interval */
    uint16_t latency;           /*!< latency */
    uint16_t timeout;           /*!< timeout */
} gap_ble_conn_param_update_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| interval | uint16_t | 链路调度间隔，单位 slot |
| latency | uint16_t | 延迟周期，单位 slot |
| timeout | uint16_t | 超时时间，单位 10 ms |

### struct_gap_ble_sec_params_t <a id="struct_gap_ble_sec_params_t"></a>

```c
typedef struct {
    uint8_t bondable;          /*!< bondable */
    uint8_t io_capability;     /*!< input and output type { @ref gap_ble_io_ability_t } */
    uint8_t sc_enable;         /*!< security enable */
    uint8_t sc_mode;           /*!< security mode type { @ref gap_ble_sec_mode_t } */
} gap_ble_sec_params_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| bondable | uint8_t | 绑定能力选择：1 支持绑定；0 不支持绑定 |
| io_capability | uint8_t | 输入输出能力，参考 [gap_ble_io_ability_t](#enum_gap_ble_io_ability_t) |
| sc_enable | uint8_t | 安全配对能力选择：1 支持安全配对；0 不支持安全配对 |
| sc_mode | uint8_t | 安全模式，参考 [gap_ble_sec_mode_t](#enum_gap_ble_sec_mode_t) |

### struct_ble_auth_info_evt_t <a id="struct_ble_auth_info_evt_t"></a>

```c
typedef struct {
    uint8_t ltk_len;                    /*!< link key len. */
    uint8_t fea;                        /*!< Features */
    uint8_t div[BLE_PAIRED_DIV_LEN];    /*!< div */
    uint8_t ltk[BLE_PAIRED_LTK_LEN];    /*!< link key */
    uint8_t ediv[BLE_PAIRED_DIV_LEN];   /*!< ediv */
    uint8_t rand[BLE_PAIRED_RAND_LEN];  /*!< rand */
    uint8_t irk[BLE_PAIRED_LTK_LEN];    /*!< irk */
    uint8_t csrk[BLE_PAIRED_LTK_LEN];    /*!< csrk */
    uint8_t bond_result;                /*!< bond result { @ref gap_le_link_bond_result_type_t }. */
} ble_auth_info_evt_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| ltk_len | uint8_t | 链路秘钥长度 |
| fea | uint8_t | 加密特性 |
| div | uint8_t[] | 分散器，长度 [BLE_PAIRED_DIV_LEN](#BLE_PAIRED_DIV_LEN) |
| ltk | uint8_t[] | 链路秘钥，长度 [BLE_PAIRED_LTK_LEN](#BLE_PAIRED_LTK_LEN) |
| ediv | uint8_t[] | 加密分散器，长度 [BLE_PAIRED_DIV_LEN](#BLE_PAIRED_DIV_LEN) |
| rand | uint8_t[] | 随机数，长度 [BLE_PAIRED_RAND_LEN](#BLE_PAIRED_RAND_LEN) |
| irk | uint8_t[] | 解析可解析地址秘钥，长度 [BLE_PAIRED_LTK_LEN](#BLE_PAIRED_LTK_LEN) |
| csrk | uint8_t[] | 连接签名解析秘钥，长度 [BLE_PAIRED_LTK_LEN](#BLE_PAIRED_LTK_LEN) |
| bond_result | uint8_t | 链路是否绑定，参考 [gap_le_link_bond_result_type_t](#enum_gap_le_link_bond_result_type_t) |

### struct_gap_ble_callbacks_t <a id="struct_gap_ble_callbacks_t"></a>

```c
typedef struct {
    gap_ble_set_adv_data_callback set_adv_data_cb;               /*!< Set advertising data callback */
    gap_ble_set_adv_param_callback set_adv_param_cb;             /*!< Set advertising parameter callback */
    gap_ble_set_scan_param_callback set_scan_param_cb;           /*!< Set scan parameter callback */
    gap_ble_start_adv_callback start_adv_cb;                     /*!< Start advertising callback */
    gap_ble_stop_adv_callback stop_adv_cb;                       /*!< Stop advertising callback */
    gap_ble_scan_result_callback scan_result_cb;                 /*!< Scan result callback */
    gap_ble_connect_state_changed_callback conn_state_change_cb; /*!< Connect state changed callback */
    gap_ble_paired_complete_callback pair_result_cb;             /*!< pair complete callback */
    gap_ble_read_rssi_callback read_rssi_cb;                     /*!< Read rssi callback. */
    gap_ble_terminate_adv_callback terminate_adv_cb;             /*!< terminate adv callback */
    gap_ble_auth_complete_callback auth_complete_cb;             /*!< authentication complete callback */
    gap_ble_connect_param_update_callback conn_param_update_cb;  /*!< connect param update callback */
    gap_ble_get_white_list_callback get_white_list_cb;           /*!< get white list callback */
    gap_ble_set_data_length_callback set_data_length_cb;         /*!< set data len callback */
} gap_ble_callbacks_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| set_adv_data_cb | [gap_ble_set_adv_data_callback](#typedef_gap_ble_set_adv_data_callback) | 设置广播数据回调函数 |
| set_adv_param_cb | [gap_ble_set_adv_param_callback](#typedef_gap_ble_set_adv_param_callback) | 设置广播参数回调函数 |
| set_scan_param_cb | [gap_ble_set_scan_param_callback](#typedef_gap_ble_set_scan_param_callback) | 设置扫描参数回调函数 |
| start_adv_cb | [gap_ble_start_adv_callback](#typedef_gap_ble_start_adv_callback) | 开启广播回调函数 |
| stop_adv_cb | [gap_ble_stop_adv_callback](#typedef_gap_ble_stop_adv_callback) | 关闭广播回调函数 |
| scan_result_cb | [gap_ble_scan_result_callback](#typedef_gap_ble_scan_result_callback) | 扫描结果回调函数 |
| conn_state_change_cb | [gap_ble_connect_state_changed_callback](#typedef_gap_ble_connect_state_changed_callback) | 连接状态改变回调函数 |
| pair_result_cb | [gap_ble_paired_complete_callback](#typedef_gap_ble_paired_complete_callback) | 配对完成回调函数 |
| read_rssi_cb | [gap_ble_read_rssi_callback](#typedef_gap_ble_read_rssi_callback) | 读取 RSSI 回调函数 |
| terminate_adv_cb | [gap_ble_terminate_adv_callback](#typedef_gap_ble_terminate_adv_callback) | 被动中止广播回调函数 |
| auth_complete_cb | [gap_ble_auth_complete_callback](#typedef_gap_ble_auth_complete_callback) | 认证完成回调函数 |
| conn_param_update_cb | [gap_ble_connect_param_update_callback](#typedef_gap_ble_connect_param_update_callback) | 连接参数更新回调函数 |
| get_white_list_cb | [gap_ble_get_white_list_callback](#typedef_gap_ble_get_white_list_callback) | 获取白名单回调函数 |
| set_data_length_cb | [gap_ble_set_data_length_callback](#typedef_gap_ble_set_data_length_callback) | 设置数据长度回调函数 |

### struct_bd_addr_t <a id="struct_bd_addr_t"></a>

```c
typedef struct {
    uint8_t addr[BD_ADDR_LEN];     /*!< bluetooth device address. */
    uint8_t type;                  /*!< bluetooth device address type, See { @ref bt_addr_type }. */
} bd_addr_t;
```

**使用说明**

SDK 公共基础类型，定义设备的蓝牙地址，由地址字节数组与地址类型组成，本模块对外接口中以指针形式作为入参/出参载体使用。

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| addr | uint8_t[] | 蓝牙地址 |
| type | uint8_t | 蓝牙地址类型 |

## Macros

### BLE_PAIRED_DIV_LEN <a id="BLE_PAIRED_DIV_LEN"></a>

```c
#define BLE_PAIRED_DIV_LEN 2
```

### BLE_PAIRED_RAND_LEN <a id="BLE_PAIRED_RAND_LEN"></a>

```c
#define BLE_PAIRED_RAND_LEN 8
```

### BLE_PAIRED_LTK_LEN <a id="BLE_PAIRED_LTK_LEN"></a>

```c
#define BLE_PAIRED_LTK_LEN 16
```
