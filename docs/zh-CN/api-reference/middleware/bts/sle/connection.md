# Connection

connection 提供 SLE (Star Flash Low Energy) 连接管理、设备发现与传输管理能力，覆盖连接/断开、配对、连接参数更新、PHY/MCS 设置、设备公开（announce）、扫描（seek）以及传输繁忙回调等接口。

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
#include "include/middleware/services/bts/sle/sle_device_discovery.h"
#include "include/middleware/services/bts/sle/sle_transmition_manager.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [sle_connect_remote_device](#sle_connect_remote_device) | 向对端设备发起连接请求 |
| [sle_create_connection_cancel](#sle_create_connection_cancel) | 取消正在进行的连接创建过程 |
| [sle_set_connect_rssi](#sle_set_connect_rssi) | 设置连接使用的 RSSI 门限值 |
| [sle_disconnect_remote_device](#sle_disconnect_remote_device) | 向对端设备发起断开连接请求 |
| [sle_disconnect_all_remote_device](#sle_disconnect_all_remote_device) | 断开所有已建立的连接 |
| [sle_update_connect_param](#sle_update_connect_param) | 发送连接参数更新请求 |
| [sle_pair_remote_device](#sle_pair_remote_device) | 向对端设备发起配对请求 |
| [sle_remove_paired_remote_device](#sle_remove_paired_remote_device) | 删除指定地址设备的配对信息 |
| [sle_remove_all_pairs](#sle_remove_all_pairs) | 删除所有配对信息 |
| [sle_get_paired_devices_num](#sle_get_paired_devices_num) | 获取已配对设备数量 |
| [sle_get_connect_role](#sle_get_connect_role) | 获取指定连接的链路角色 |
| [sle_get_paired_devices](#sle_get_paired_devices) | 获取已配对设备地址列表 |
| [sle_get_bonded_devices](#sle_get_bonded_devices) | 获取已绑定设备地址列表 |
| [sle_set_nv_smp_keys](#sle_set_nv_smp_keys) | 设置 NV 中保存的 SMP 密钥 |
| [sle_get_pair_state](#sle_get_pair_state) | 获取指定设备的配对状态 |
| [sle_read_remote_device_rssi](#sle_read_remote_device_rssi) | 读取对端设备 RSSI 值 |
| [sle_set_acb_evt_param](#sle_set_acb_evt_param) | 设置 ACB 链路重传参数 |
| [sle_read_access_filter_list_size](#sle_read_access_filter_list_size) | 查询访问过滤器列表剩余大小 |
| [sle_clear_access_filter_list](#sle_clear_access_filter_list) | 清空访问过滤器列表 |
| [sle_add_device_to_access_filter_list](#sle_add_device_to_access_filter_list) | 将地址加入访问过滤器列表 |
| [sle_remove_device_from_access_filter_list](#sle_remove_device_from_access_filter_list) | 将地址从访问过滤器列表移除 |
| [sle_set_phy_param](#sle_set_phy_param) | 设置指定连接的 PHY 参数 |
| [sle_set_save_pair_keys_mode](#sle_set_save_pair_keys_mode) | 设置配对密钥保存模式 |
| [sle_set_mcs](#sle_set_mcs) | 设置指定连接的调制与编码策略 |
| [sle_set_data_len](#sle_set_data_len) | 设置连接链路偏好最大传输 payload 字节数 |
| [sle_default_connection_param_set](#sle_default_connection_param_set) | 设置默认连接参数 |
| [sle_connection_register_callbacks](#sle_connection_register_callbacks) | 注册连接管理回调函数 |
| [sle_customize_max_pwr](#sle_customize_max_pwr) | 配置 BLE 与 SLE 最大功率定制化信息 |
| [sle_set_local_addr](#sle_set_local_addr) | 设置本地设备地址 |
| [sle_get_local_addr](#sle_get_local_addr) | 获取本地设备地址 |
| [sle_set_local_name](#sle_set_local_name) | 设置本地设备名称 |
| [sle_get_local_name](#sle_get_local_name) | 获取本地设备名称 |
| [sle_set_announce_data](#sle_set_announce_data) | 设置设备公开数据 |
| [sle_remove_announce](#sle_remove_announce) | 删除指定设备公开实例 |
| [sle_set_announce_param](#sle_set_announce_param) | 设置设备公开参数 |
| [sle_start_announce](#sle_start_announce) | 启动指定设备公开实例 |
| [sle_stop_announce](#sle_stop_announce) | 停止指定设备公开实例 |
| [sle_set_seek_param](#sle_set_seek_param) | 设置设备发现扫描参数 |
| [sle_start_seek](#sle_start_seek) | 启动设备发现扫描 |
| [sle_stop_seek](#sle_stop_seek) | 停止设备发现扫描 |
| [sle_announce_seek_register_callbacks](#sle_announce_seek_register_callbacks) | 注册设备公开与扫描回调函数 |
| [sle_transmission_signal_capability_req](#sle_transmission_signal_capability_req) | 发送连接管理能力查询请求 |
| [sle_transmission_register_callbacks](#sle_transmission_register_callbacks) | 注册传输管理回调函数 |

## Functions

### sle_connect_remote_device <a id="sle_connect_remote_device"></a>

```c
errcode_t sle_connect_remote_device(const sle_addr_t *addr)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 向指定地址的对端设备发送 SLE 连接请求
- 连接状态改变结果通过已注册的 [sle_connect_state_changed_callback](#sle_connect_state_changed_callback) 回调返回
- 调用结果以错误码形式同步返回

**前置条件**

- 调用时序约束：调用前需先调用 [sle_connection_register_callbacks](#sle_connection_register_callbacks) 注册连接状态回调
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | [sle_addr_t](#struct_sle_addr_t) * | 对端设备地址 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 连接请求成功发起 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**参考案例**

- `application/samples/bt/sle/sle_speed_client/src/sle_speed_client.c`

### sle_create_connection_cancel <a id="sle_create_connection_cancel"></a>

```c
errcode_t sle_create_connection_cancel(void)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 取消当前正在进行的连接创建过程
- 终止由 [sle_connect_remote_device](#sle_connect_remote_device) 发起的连接流程
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：需在 [sle_connect_remote_device](#sle_connect_remote_device) 已发起连接但尚未完成时调用
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 取消连接创建成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_set_connect_rssi <a id="sle_set_connect_rssi"></a>

```c
errcode_t sle_set_connect_rssi(int8_t rssi)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 设置连接过程使用的 RSSI 门限值
- 用于在连接建立阶段对信号强度进行过滤
- 调用结果以错误码形式返回

**前置条件**

- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| rssi | int8_t | 连接 RSSI 门限值，单位 dBm | -127 ~ 20 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 设置成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_disconnect_remote_device <a id="sle_disconnect_remote_device"></a>

```c
errcode_t sle_disconnect_remote_device(const sle_addr_t *addr)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 向指定地址的对端设备发送断开连接请求
- 断链结果通过已注册的 [sle_connect_state_changed_callback](#sle_connect_state_changed_callback) 回调返回
- 调用结果以错误码形式同步返回

**前置条件**

- 调用时序约束：目标设备需已建立连接
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | [sle_addr_t](#struct_sle_addr_t) * | 对端设备地址 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 断开连接请求成功发起 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_disconnect_all_remote_device <a id="sle_disconnect_all_remote_device"></a>

```c
errcode_t sle_disconnect_all_remote_device(void)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 断开所有已建立的 SLE 连接
- 各连接的断链结果通过已注册的 [sle_connect_state_changed_callback](#sle_connect_state_changed_callback) 回调返回
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：需在存在已建立连接时调用
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 断开所有连接成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_update_connect_param <a id="sle_update_connect_param"></a>

```c
errcode_t sle_update_connect_param(sle_connection_param_update_t *params)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 向对端设备发送连接参数更新请求
- 更新结果通过已注册的 [sle_connect_param_update_callback](#sle_connect_param_update_callback) 回调返回
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：目标连接需已建立
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| params | [sle_connection_param_update_t](#struct_sle_connection_param_update_t) * | 连接参数更新请求 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 更新请求成功发起 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**参考案例**

- `application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`

### sle_pair_remote_device <a id="sle_pair_remote_device"></a>

```c
errcode_t sle_pair_remote_device(const sle_addr_t *addr)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 向指定地址的对端设备发送配对请求
- 配对完成结果通过已注册的 [sle_pair_complete_callback](#sle_pair_complete_callback) 回调返回
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：目标设备需已建立连接
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | [sle_addr_t](#struct_sle_addr_t) * | 对端设备地址 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 配对请求成功发起 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**参考案例**

- `application/samples/bt/sle/sle_speed_client/src/sle_speed_client.c`

### sle_remove_paired_remote_device <a id="sle_remove_paired_remote_device"></a>

```c
errcode_t sle_remove_paired_remote_device(const sle_addr_t *addr)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 删除指定地址设备的配对信息
- 删除结果通过已注册的 [sle_pair_remove_callback](#sle_pair_remove_callback) 回调返回
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：目标设备需已完成配对
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | [sle_addr_t](#struct_sle_addr_t) * | 对端设备地址 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 删除配对成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_remove_all_pairs <a id="sle_remove_all_pairs"></a>

```c
errcode_t sle_remove_all_pairs(void)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 删除所有已配对设备的配对信息
- 调用结果以错误码形式返回

**前置条件**

- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 删除所有配对成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_get_paired_devices_num <a id="sle_get_paired_devices_num"></a>

```c
errcode_t sle_get_paired_devices_num(uint16_t *number)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 获取当前已配对设备的数量
- 数量通过出参返回
- 调用结果以错误码形式返回

**前置条件**

- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| number | uint16_t * | 已配对设备数量，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 获取成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_get_connect_role <a id="sle_get_connect_role"></a>

```c
errcode_t sle_get_connect_role(uint16_t conn_id, uint8_t *role)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 获取指定连接的链路角色（G 节点或 T 节点）
- 角色结果通过出参返回
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：conn_id 对应的连接需已建立
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| conn_id | uint16_t | 连接 ID | 有效连接 ID |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| role | uint8_t * | 链路角色，取值参考 [sle_link_role_t](#enum_sle_link_role_t)，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 获取成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_get_paired_devices <a id="sle_get_paired_devices"></a>

```c
errcode_t sle_get_paired_devices(sle_addr_t *addr, uint16_t *number)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 获取已配对设备的地址列表
- 地址列表与设备数量通过出参返回
- 调用结果以错误码形式返回

**前置条件**

- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| addr | [sle_addr_t](#struct_sle_addr_t) * | 已配对设备地址链表，由调用方分配内存、函数填充 |
| number | uint16_t * | 入参为调用方分配的地址容量，出参为实际填充的设备数量 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 获取成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_get_bonded_devices <a id="sle_get_bonded_devices"></a>

```c
errcode_t sle_get_bonded_devices(sle_addr_t *addr, uint16_t *number)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 获取已绑定设备的地址列表
- 地址列表与设备数量通过出参返回
- 调用结果以错误码形式返回

**前置条件**

- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| addr | [sle_addr_t](#struct_sle_addr_t) * | 已绑定设备地址链表，由调用方分配内存、函数填充 |
| number | uint16_t * | 入参为调用方分配的地址容量，出参为实际填充的设备数量 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 获取成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_set_nv_smp_keys <a id="sle_set_nv_smp_keys"></a>

```c
errcode_t sle_set_nv_smp_keys(sle_auth_info_evt_t *keys, sle_addr_t *own_addr, sle_addr_t *peer_addr, uint8_t index)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 设置 NV 中保存的 SMP 密钥信息
- 同时记录本端地址、对端地址与索引下标
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：需在配对/认证流程获得密钥后调用
- 依赖关系：依赖 SLE 协议栈与 NV 存储已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| keys | [sle_auth_info_evt_t](#struct_sle_auth_info_evt_t) * | 链路密钥与算法信息 | 不为NULL |
| own_addr | [sle_addr_t](#struct_sle_addr_t) * | 本端设备地址 | 不为NULL |
| peer_addr | [sle_addr_t](#struct_sle_addr_t) * | 对端设备地址 | 不为NULL |
| index | uint8_t | 密钥索引下标 | 0 ~ 255 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 设置成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_get_pair_state <a id="sle_get_pair_state"></a>

```c
errcode_t sle_get_pair_state(const sle_addr_t *addr, uint8_t *state)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 获取指定地址设备的配对状态
- 配对状态通过出参返回
- 调用结果以错误码形式返回

**前置条件**

- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | [sle_addr_t](#struct_sle_addr_t) * | 设备地址 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| state | uint8_t * | 配对状态，取值参考 [sle_pair_state_t](#enum_sle_pair_state_t)，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 获取成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_read_remote_device_rssi <a id="sle_read_remote_device_rssi"></a>

```c
errcode_t sle_read_remote_device_rssi(uint16_t conn_id)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 读取指定连接对端设备的 RSSI 值
- RSSI 读取结果通过已注册的 [sle_read_rssi_callback](#sle_read_rssi_callback) 回调返回
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：conn_id 对应的连接需已建立
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| conn_id | uint16_t | 连接 ID | 有效连接 ID |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 读取请求成功发起 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**参考案例**

- `application/samples/bt/sle/sle_speed_client/src/sle_speed_client.c`

### sle_set_acb_evt_param <a id="sle_set_acb_evt_param"></a>

```c
errcode_t sle_set_acb_evt_param(uint16_t conn_id, uint16_t evt_intv, uint8_t evt_num)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 设置指定连接的 ACB 链路重传间隔与重传次数
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：conn_id 对应的连接需已建立
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| conn_id | uint16_t | 连接 ID | 有效连接 ID |
| evt_intv | uint16_t | 重传间隔 | 0 ~ 65535 |
| evt_num | uint8_t | 重传次数 | 0 ~ 255 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 设置成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_read_access_filter_list_size <a id="sle_read_access_filter_list_size"></a>

```c
errcode_t sle_read_access_filter_list_size(uint8_t *size)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 查询访问过滤器列表的剩余可容纳大小
- 剩余大小通过出参返回
- 调用结果以错误码形式返回

**前置条件**

- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| size | uint8_t * | 访问过滤器列表剩余大小，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 查询成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_clear_access_filter_list <a id="sle_clear_access_filter_list"></a>

```c
errcode_t sle_clear_access_filter_list(void)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 清空访问过滤器列表中的所有地址
- 调用结果以错误码形式返回

**前置条件**

- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 清空成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_add_device_to_access_filter_list <a id="sle_add_device_to_access_filter_list"></a>

```c
errcode_t sle_add_device_to_access_filter_list(sle_addr_t *addr)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 将指定地址加入访问过滤器列表
- 调用结果以错误码形式返回

**前置条件**

- 依赖关系：依赖 SLE 协议栈已初始化完成、访问过滤器列表有剩余空间
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | [sle_addr_t](#struct_sle_addr_t) * | 待加入地址 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 添加成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_remove_device_from_access_filter_list <a id="sle_remove_device_from_access_filter_list"></a>

```c
errcode_t sle_remove_device_from_access_filter_list(sle_addr_t *addr)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 将指定地址从访问过滤器列表中移除
- 调用结果以错误码形式返回

**前置条件**

- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | [sle_addr_t](#struct_sle_addr_t) * | 待移除地址 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 移除成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_set_phy_param <a id="sle_set_phy_param"></a>

```c
errcode_t sle_set_phy_param(uint16_t conn_id, sle_set_phy_t *param)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 设置指定连接的 PHY 参数，包括无线帧类型、PHY、导频密度与反馈类型等
- 设置结果通过已注册的 [sle_set_phy_callback](#sle_set_phy_callback) 回调返回
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：conn_id 对应的连接需已建立
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| conn_id | uint16_t | 连接 ID | 有效连接 ID |
| param | [sle_set_phy_t](#struct_sle_set_phy_t) * | PHY 参数 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 设置请求成功发起 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**参考案例**

- `application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`

### sle_set_save_pair_keys_mode <a id="sle_set_save_pair_keys_mode"></a>

```c
errcode_t sle_set_save_pair_keys_mode(uint8_t is_available)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 设置配对密钥的保存模式（自动保存或手动保存）
- 调用结果以错误码形式返回

**前置条件**

- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| is_available | uint8_t | 配对密钥保存模式 | [SLE_SAVE_SMP_KEYS_AUTO](#enum_sle_save_smp_keys_mode_switch_t)(0x00) / [SLE_SAVE_SMP_KEYS_MANU](#enum_sle_save_smp_keys_mode_switch_t)(0x01) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 设置成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_set_mcs <a id="sle_set_mcs"></a>

```c
errcode_t sle_set_mcs(uint16_t conn_id, uint8_t mcs)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 设置指定连接的调制与编码策略（MCS）索引值
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：conn_id 对应的连接需已建立
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| conn_id | uint16_t | 连接 ID | 有效连接 ID |
| mcs | uint8_t | 调制与编码策略索引值 | 0 ~ 255 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 设置成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**参考案例**

- `application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`

### sle_set_data_len <a id="sle_set_data_len"></a>

```c
errcode_t sle_set_data_len(uint16_t conn_id, uint16_t tx_octets)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 设置指定连接链路上所偏好的最大传输 payload 字节数
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：conn_id 对应的连接需已建立
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| conn_id | uint16_t | 连接 ID | 有效连接 ID |
| tx_octets | uint16_t | 偏好的最大传输 payload 字节数 | 0 ~ 65535 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 设置成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**参考案例**

- `application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`

### sle_default_connection_param_set <a id="sle_default_connection_param_set"></a>

```c
errcode_t sle_default_connection_param_set(sle_default_connect_param_t *set_param)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 设置 SLE 默认连接参数，包括过滤策略、扫描窗口、调度间隔与超时等
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：建议在发起连接之前调用
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| set_param | [sle_default_connect_param_t](#struct_sle_default_connect_param_t) * | 默认连接参数 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 设置成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**参考案例**

- `application/samples/bt/sle/sle_speed_client/src/sle_speed_client.c`
- `application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`

### sle_connection_register_callbacks <a id="sle_connection_register_callbacks"></a>

```c
errcode_t sle_connection_register_callbacks(sle_connection_callbacks_t *func)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 注册 SLE 连接管理回调函数集合
- 涵盖连接状态改变、参数更新、认证、配对、RSSI 读取、低时延、PHY 设置与取消配对等事件
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：应在发起连接/配对等相关操作之前调用
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func | [sle_connection_callbacks_t](#struct_sle_connection_callbacks_t) * | 连接管理回调函数集合 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 注册成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**参考案例**

- `application/samples/bt/sle/sle_speed_client/src/sle_speed_client.c`
- `application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`

### sle_customize_max_pwr <a id="sle_customize_max_pwr"></a>

```c
errcode_t sle_customize_max_pwr(int8_t ble_pwr, int8_t sle_pwr)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_connection_manager.h"
```

**功能说明**

- 配置 BLE 与 SLE 的最大功率定制化信息
- 调用结果以错误码形式返回

**前置条件**

- 依赖关系：依赖 NV 定制化配置模块已就绪
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| ble_pwr | int8_t | BLE 最大功率，单位 dBm | -127 ~ 20 |
| sle_pwr | int8_t | SLE 最大功率，单位 dBm | -127 ~ 20 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 配置成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_set_local_addr <a id="sle_set_local_addr"></a>

```c
errcode_t sle_set_local_addr(sle_addr_t *addr)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_device_discovery.h"
```

**功能说明**

- 设置本地 SLE 设备地址
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：应在发起设备公开或扫描之前调用
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | [sle_addr_t](#struct_sle_addr_t) * | 本地设备地址 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 设置成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**参考案例**

- `application/samples/bt/sle/sle_speed_client/src/sle_speed_client.c`
- `application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`

### sle_get_local_addr <a id="sle_get_local_addr"></a>

```c
errcode_t sle_get_local_addr(sle_addr_t *addr)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_device_discovery.h"
```

**功能说明**

- 获取本地 SLE 设备地址
- 地址通过出参返回
- 调用结果以错误码形式返回

**前置条件**

- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| addr | [sle_addr_t](#struct_sle_addr_t) * | 本地设备地址，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 获取成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_set_local_name <a id="sle_set_local_name"></a>

```c
errcode_t sle_set_local_name(const uint8_t *name, uint8_t len)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_device_discovery.h"
```

**功能说明**

- 设置本地 SLE 设备名称
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：应在发起设备公开之前调用
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| name | const uint8_t * | 本地设备名称 | 不为NULL |
| len | uint8_t | 设备名称长度，包括结束符 \0 | 0 ~ 255 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 设置成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_get_local_name <a id="sle_get_local_name"></a>

```c
errcode_t sle_get_local_name(uint8_t *name, uint8_t *len)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_device_discovery.h"
```

**功能说明**

- 获取本地 SLE 设备名称
- 名称与长度通过出参返回
- 调用结果以错误码形式返回

**前置条件**

- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| name | uint8_t * | 本地设备名称，由调用方分配内存、函数填充 |
| len | uint8_t * | 入参为用户分配的缓冲区大小，出参为本地设备名称长度 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 获取成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_set_announce_data <a id="sle_set_announce_data"></a>

```c
errcode_t sle_set_announce_data(uint8_t announce_id, const sle_announce_data_t *data)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_device_discovery.h"
```

**功能说明**

- 设置指定设备公开实例的公开数据与扫描响应数据
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：应在 [sle_start_announce](#sle_start_announce) 之前调用
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| announce_id | uint8_t | 设备公开 ID | 0 ~ [SLE_ANNOUNCE_ID_MAX](#SLE_ANNOUNCE_ID_MAX)(16) |
| data | [sle_announce_data_t](#struct_sle_announce_data_t) * | 设备公开数据 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 设置成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**参考案例**

- `application/samples/bt/sle/sle_speed_server/src/sle_speed_server_adv.c`

### sle_remove_announce <a id="sle_remove_announce"></a>

```c
errcode_t sle_remove_announce(uint8_t announce_id)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_device_discovery.h"
```

**功能说明**

- 删除指定的设备公开实例
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：目标设备公开实例需已停止
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| announce_id | uint8_t | 设备公开 ID | 0 ~ [SLE_ANNOUNCE_ID_MAX](#SLE_ANNOUNCE_ID_MAX)(16) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 删除成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_set_announce_param <a id="sle_set_announce_param"></a>

```c
errcode_t sle_set_announce_param(uint8_t announce_id, const sle_announce_param_t *param)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_device_discovery.h"
```

**功能说明**

- 设置指定设备公开实例的参数，包括公开类型、G/T 角色、等级、间隔、信道与连接参数等
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：应在 [sle_start_announce](#sle_start_announce) 之前调用
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| announce_id | uint8_t | 设备公开 ID | 0 ~ [SLE_ANNOUNCE_ID_MAX](#SLE_ANNOUNCE_ID_MAX)(16) |
| param | [sle_announce_param_t](#struct_sle_announce_param_t) * | 设备公开参数 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 设置成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**参考案例**

- `application/samples/bt/sle/sle_speed_server/src/sle_speed_server_adv.c`

### sle_start_announce <a id="sle_start_announce"></a>

```c
errcode_t sle_start_announce(uint8_t announce_id)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_device_discovery.h"
```

**功能说明**

- 启动指定的设备公开实例
- 启动结果通过已注册的 [sle_announce_enable_callback](#sle_announce_enable_callback) 回调返回
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：需先调用 [sle_set_announce_param](#sle_set_announce_param) 与 [sle_set_announce_data](#sle_set_announce_data) 完成参数与数据设置
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| announce_id | uint8_t | 设备公开 ID | 0 ~ [SLE_ANNOUNCE_ID_MAX](#SLE_ANNOUNCE_ID_MAX)(16) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 启动请求成功发起 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**参考案例**

- `application/samples/bt/sle/sle_speed_server/src/sle_speed_server.c`
- `application/samples/bt/sle/sle_speed_server/src/sle_speed_server_adv.c`

### sle_stop_announce <a id="sle_stop_announce"></a>

```c
errcode_t sle_stop_announce(uint8_t announce_id)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_device_discovery.h"
```

**功能说明**

- 停止指定的设备公开实例
- 停止结果通过已注册的 [sle_announce_disable_callback](#sle_announce_disable_callback) 回调返回
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：目标设备公开实例需已启动
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| announce_id | uint8_t | 设备公开 ID | 0 ~ [SLE_ANNOUNCE_ID_MAX](#SLE_ANNOUNCE_ID_MAX)(16) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 停止请求成功发起 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_set_seek_param <a id="sle_set_seek_param"></a>

```c
errcode_t sle_set_seek_param(sle_seek_param_t *param)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_device_discovery.h"
```

**功能说明**

- 设置设备发现扫描参数，包括地址类型、过滤策略、PHY、扫描类型、间隔与窗口等
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：应在 [sle_start_seek](#sle_start_seek) 之前调用
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| param | [sle_seek_param_t](#struct_sle_seek_param_t) * | 设备发现扫描参数 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 设置成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**参考案例**

- `application/samples/bt/sle/sle_speed_client/src/sle_speed_client.c`



### sle_start_seek <a id="sle_start_seek"></a>

```c
errcode_t sle_start_seek(void)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_device_discovery.h"
```

**功能说明**

- 启动设备发现扫描
- 启动结果通过已注册的 [sle_start_seek_callback](#sle_start_seek_callback) 回调返回
- 扫描到的设备结果通过已注册的 [sle_seek_result_callback](#sle_seek_result_callback) 回调返回

**前置条件**

- 调用时序约束：需先调用 [sle_set_seek_param](#sle_set_seek_param) 完成扫描参数设置
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 启动扫描成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**参考案例**

- `application/samples/bt/sle/sle_speed_client/src/sle_speed_client.c`

### sle_stop_seek <a id="sle_stop_seek"></a>

```c
errcode_t sle_stop_seek(void)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_device_discovery.h"
```

**功能说明**

- 停止设备发现扫描
- 停止结果通过已注册的 [sle_seek_disable_callback](#sle_seek_disable_callback) 回调返回

**前置条件**

- 调用时序约束：扫描需已启动
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 停止扫描成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**参考案例**

- `application/samples/bt/sle/sle_speed_client/src/sle_speed_client.c`

### sle_announce_seek_register_callbacks <a id="sle_announce_seek_register_callbacks"></a>

```c
errcode_t sle_announce_seek_register_callbacks(sle_announce_seek_callbacks_t *func)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_device_discovery.h"
```

**功能说明**

- 注册 SLE 设备公开与扫描的回调函数集合
- 涵盖设备公开使能/关闭/停止/删除、扫描使能/关闭、扫描结果上报与 dfr 等事件
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：应在发起设备公开或扫描之前调用
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func | [sle_announce_seek_callbacks_t](#struct_sle_announce_seek_callbacks_t) * | 设备公开与扫描回调函数集合 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 注册成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

**参考案例**

- `application/samples/bt/sle/sle_speed_client/src/sle_speed_client.c`
- `application/samples/bt/sle/sle_speed_server/src/sle_speed_server_adv.c`

### sle_transmission_signal_capability_req <a id="sle_transmission_signal_capability_req"></a>

```c
errcode_t sle_transmission_signal_capability_req(uint16_t conn_id, sle_transmission_signal_capability_bit_t* param)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_transmition_manager.h"
```

**功能说明**

- 向对端发送连接管理能力查询请求
- 查询的能力信息通过入参指定
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：conn_id 对应的连接需已建立
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| conn_id | uint16_t | 连接 ID | 有效连接 ID |
| param | [sle_transmission_signal_capability_bit_t](#struct_sle_transmission_signal_capability_bit_t) * | 查询的能力信息 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 查询请求成功发起 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

### sle_transmission_register_callbacks <a id="sle_transmission_register_callbacks"></a>

```c
errcode_t sle_transmission_register_callbacks(sle_transmission_callbacks_t *func)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_transmition_manager.h"
```

**功能说明**

- 注册 SLE 传输管理回调函数集合
- 涵盖传输数据繁忙状态事件
- 调用结果以错误码形式返回

**前置条件**

- 调用时序约束：应在进行传输数据收发之前调用
- 依赖关系：依赖 SLE 协议栈已初始化完成
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func | [sle_transmission_callbacks_t](#struct_sle_transmission_callbacks_t) * | 传输管理回调函数集合 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 注册成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 执行失败 |

## Type definitions

### sle_connect_state_changed_callback <a id="sle_connect_state_changed_callback"></a>

```c
typedef void (*sle_connect_state_changed_callback)(uint16_t conn_id, const sle_addr_t *addr,
    sle_acb_state_t conn_state, sle_pair_state_t pair_state, sle_disc_reason_t disc_reason);
```

**使用说明**

SLE 连接状态改变时由 SLE service 调用的事件回调函数类型。

回调说明：
- 调用时机：连接建立/断开等状态改变时，运行于 SLE service 线程，不能阻塞或长时间等待；
- 参数语义：conn_id 为连接 ID，addr 为对端地址，conn_state 为连接状态，pair_state 为配对状态，disc_reason 为断链原因；
- 返回值处理：返回类型为 void，无返回值；指针由 SLE service 申请内存并由其释放，回调中不应释放。

### sle_connect_param_update_callback <a id="sle_connect_param_update_callback"></a>

```c
typedef void (*sle_connect_param_update_callback)(uint16_t conn_id, errcode_t status,
    const sle_connection_param_update_evt_t *param);
```

**使用说明**

连接参数更新完成时由 SLE service 调用的事件回调函数类型。

回调说明：
- 调用时机：连接参数更新完成时，运行于 SLE service 线程，不能阻塞或长时间等待；
- 参数语义：conn_id 为连接 ID，status 为执行结果错误码，param 为更新后的连接参数；
- 返回值处理：返回类型为 void，无返回值；指针由 SLE service 申请内存并由其释放，回调中不应释放。

### sle_connect_param_update_req_callback <a id="sle_connect_param_update_req_callback"></a>

```c
typedef void (*sle_connect_param_update_req_callback)(uint16_t conn_id, errcode_t status,
    const sle_connection_param_update_req_t *param);
```

**使用说明**

连接参数更新请求完成前由 SLE service 调用的事件回调函数类型。

回调说明：
- 调用时机：连接参数更新请求完成前，运行于 SLE service 线程，不能阻塞或长时间等待；
- 参数语义：conn_id 为连接 ID，status 为执行结果错误码，param 为连接参数更新请求；
- 返回值处理：返回类型为 void，无返回值；指针由 SLE service 申请内存并由其释放，回调中不应释放。

### sle_auth_complete_callback <a id="sle_auth_complete_callback"></a>

```c
typedef void (*sle_auth_complete_callback)(uint16_t conn_id, const sle_addr_t *addr, errcode_t status,
    const sle_auth_info_evt_t* evt);
```

**使用说明**

认证完成时由 SLE service 调用的事件回调函数类型。

回调说明：
- 调用时机：认证流程完成时，运行于 SLE service 线程，不能阻塞或长时间等待；
- 参数语义：conn_id 为连接 ID，addr 为对端地址，status 为执行结果错误码，evt 为认证事件信息；
- 返回值处理：返回类型为 void，无返回值；指针由 SLE service 申请内存并由其释放，回调中不应释放。

### sle_pair_complete_callback <a id="sle_pair_complete_callback"></a>

```c
typedef void (*sle_pair_complete_callback)(uint16_t conn_id, const sle_addr_t *addr, errcode_t status);
```

**使用说明**

配对完成时由 SLE service 调用的事件回调函数类型。

回调说明：
- 调用时机：配对流程完成时，运行于 SLE service 线程，不能阻塞或长时间等待；
- 参数语义：conn_id 为连接 ID，addr 为对端地址，status 为执行结果错误码；
- 返回值处理：返回类型为 void，无返回值；指针由 SLE service 申请内存并由其释放，回调中不应释放。

### sle_read_rssi_callback <a id="sle_read_rssi_callback"></a>

```c
typedef void (*sle_read_rssi_callback)(uint16_t conn_id, int8_t rssi, errcode_t status);
```

**使用说明**

读取 RSSI 完成时由 SLE service 调用的事件回调函数类型。

回调说明：
- 调用时机：调用 [sle_read_remote_device_rssi](#sle_read_remote_device_rssi) 后读取完成时，运行于 SLE service 线程，不能阻塞或长时间等待；
- 参数语义：conn_id 为连接 ID，rssi 为读取到的 RSSI 值，status 为执行结果错误码；
- 返回值处理：返回类型为 void，无返回值。

### sle_low_latency_callback <a id="sle_low_latency_callback"></a>

```c
typedef void (*sle_low_latency_callback)(uint8_t status, sle_addr_t *addr, uint8_t rate);
```

**使用说明**

设置低时延完成时由 SLE service 调用的事件回调函数类型。

回调说明：
- 调用时机：设置 low latency 完成时，运行于 SLE service 线程，不能阻塞或长时间等待；
- 参数语义：status 为设置结果，addr 为对端设备地址，rate 为鼠标回报率；
- 返回值处理：返回类型为 void，无返回值。

### sle_set_phy_callback <a id="sle_set_phy_callback"></a>

```c
typedef void (*sle_set_phy_callback)(uint16_t conn_id, errcode_t status, const sle_set_phy_t *param);
```

**使用说明**

设置 PHY 完成时由 SLE service 调用的事件回调函数类型。

回调说明：
- 调用时机：调用 [sle_set_phy_param](#sle_set_phy_param) 后设置完成时，运行于 SLE service 线程，不能阻塞或长时间等待；
- 参数语义：conn_id 为连接 ID，status 为设置结果，param 为当前 PHY 参数；
- 返回值处理：返回类型为 void，无返回值；指针由 SLE service 申请内存并由其释放，回调中不应释放。

### sle_pair_remove_callback <a id="sle_pair_remove_callback"></a>

```c
typedef void (*sle_pair_remove_callback)(const sle_addr_t *addr, errcode_t status);
```

**使用说明**

取消单个设备配对完成时由 SLE service 调用的事件回调函数类型。

回调说明：
- 调用时机：取消配对完成时，运行于 SLE service 线程，不能阻塞或长时间等待；
- 参数语义：addr 为地址，status 为执行结果错误码；
- 返回值处理：返回类型为 void，无返回值；指针由 SLE service 申请内存并由其释放，回调中不应释放。

### sle_announce_enable_callback <a id="sle_announce_enable_callback"></a>

```c
typedef void (*sle_announce_enable_callback)(uint32_t announce_id, errcode_t status);
```

**使用说明**

设备公开使能完成时由 SLE service 调用的事件回调函数类型。

回调说明：
- 调用时机：设备公开使能完成时，运行于 SLE service 线程，不能阻塞或长时间等待；
- 参数语义：announce_id 为公开 ID，status 为执行结果错误码；
- 返回值处理：返回类型为 void，无返回值。

### sle_announce_disable_callback <a id="sle_announce_disable_callback"></a>

```c
typedef void (*sle_announce_disable_callback)(uint32_t announce_id, errcode_t status);
```

**使用说明**

设备公开关闭完成时由 SLE service 调用的事件回调函数类型。

回调说明：
- 调用时机：设备公开关闭完成时，运行于 SLE service 线程，不能阻塞或长时间等待；
- 参数语义：announce_id 为公开 ID，status 为执行结果错误码；
- 返回值处理：返回类型为 void，无返回值。

### sle_announce_terminal_callback <a id="sle_announce_terminal_callback"></a>

```c
typedef void (*sle_announce_terminal_callback)(uint32_t announce_id);
```

**使用说明**

设备公开停止时由 SLE service 调用的事件回调函数类型。

回调说明：
- 调用时机：设备公开停止时，运行于 SLE service 线程，不能阻塞或长时间等待；
- 参数语义：announce_id 为公开 ID；
- 返回值处理：返回类型为 void，无返回值。

### sle_announce_remove_callback <a id="sle_announce_remove_callback"></a>

```c
typedef void (*sle_announce_remove_callback)(uint32_t announce_id, errcode_t status);
```

**使用说明**

删除广播完成时由 SLE service 调用的事件回调函数类型。

回调说明：
- 调用时机：删除广播完成时，运行于 SLE service 线程，不能阻塞或长时间等待；
- 参数语义：announce_id 为公开 ID，status 为执行结果错误码；
- 返回值处理：返回类型为 void，无返回值。

### sle_start_seek_callback <a id="sle_start_seek_callback"></a>

```c
typedef void (*sle_start_seek_callback)(errcode_t status);
```

**使用说明**

扫描使能完成时由 SLE service 调用的事件回调函数类型。

回调说明：
- 调用时机：扫描使能完成时，运行于 SLE service 线程，不能阻塞或长时间等待；
- 参数语义：status 为执行结果错误码；
- 返回值处理：返回类型为 void，无返回值。

### sle_seek_disable_callback <a id="sle_seek_disable_callback"></a>

```c
typedef void (*sle_seek_disable_callback)(errcode_t status);
```

**使用说明**

扫描关闭完成时由 SLE service 调用的事件回调函数类型。

回调说明：
- 调用时机：扫描关闭完成时，运行于 SLE service 线程，不能阻塞或长时间等待；
- 参数语义：status 为执行结果错误码；
- 返回值处理：返回类型为 void，无返回值。

### sle_seek_result_callback <a id="sle_seek_result_callback"></a>

```c
typedef void (*sle_seek_result_callback)(sle_seek_result_info_t *seek_result_data);
```

**使用说明**

扫描结果上报时由 SLE service 调用的事件回调函数类型。

回调说明：
- 调用时机：扫描到设备结果上报时，运行于 SLE service 线程，不能阻塞或长时间等待；
- 参数语义：seek_result_data 为扫描结果数据；
- 返回值处理：返回类型为 void，无返回值；指针由 SLE service 申请内存并由其释放，回调中不应释放。

### sle_dfr_callback <a id="sle_dfr_callback"></a>

```c
typedef void (*sle_dfr_callback)(void);
```

**使用说明**

SLE 协议栈 dfr 流程的通用回调函数类型。

回调说明：
- 调用时机：SLE 协议栈 dfr 流程触发时；
- 参数语义：无参数；
- 返回值处理：返回类型为 void，无返回值。

### sle_trans_data_busy_callback <a id="sle_trans_data_busy_callback"></a>

```c
typedef void (*sle_trans_data_busy_callback)(uint16_t conn_id, sle_link_qos_state_t link_state);
```

**使用说明**

发送数据繁忙时由 SLE service 调用的事件回调函数类型。

回调说明：
- 调用时机：发送数据繁忙状态变化时；
- 参数语义：conn_id 为连接 ID，link_state 为链路状态；
- 返回值处理：返回类型为 void，无返回值。

### errcode_t <a id="errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块对外接口的返回值类型，表示接口执行结果错误码。[SDK公共基础类型]

## Enumerations

### sle_pair_state_t <a id="enum_sle_pair_state_t"></a>

```c
typedef enum {
    SLE_PAIR_NONE    = 0x01,
    SLE_PAIR_PAIRING = 0x02,
    SLE_PAIR_PAIRED  = 0x03
} sle_pair_state_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_PAIR_NONE | 0x01 | 未配对状态 |
| SLE_PAIR_PAIRING | 0x02 | 正在配对 |
| SLE_PAIR_PAIRED | 0x03 | 已完成配对 |

### sle_disc_reason_t <a id="enum_sle_disc_reason_t"></a>

```c
typedef enum {
    SLE_DISCONNECT_BY_REMOTE = 0x10,
    SLE_DISCONNECT_BY_LOCAL  = 0x11,
} sle_disc_reason_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_DISCONNECT_BY_REMOTE | 0x10 | 远端断链 |
| SLE_DISCONNECT_BY_LOCAL | 0x11 | 本端断链 |

### sle_acb_state_t <a id="enum_sle_acb_state_t"></a>

```c
typedef enum {
    SLE_ACB_STATE_NONE          = 0x00,
    SLE_ACB_STATE_CONNECTED     = 0x01,
    SLE_ACB_STATE_DISCONNECTED  = 0x02,
} sle_acb_state_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_ACB_STATE_NONE | 0x00 | SLE ACB 未连接状态 |
| SLE_ACB_STATE_CONNECTED | 0x01 | SLE ACB 已连接 |
| SLE_ACB_STATE_DISCONNECTED | 0x02 | SLE ACB 已断接 |

### sle_crypto_algo_t <a id="enum_sle_crypto_algo_t"></a>

```c
typedef enum {
    SLE_CRYTO_ALGO_AC1     = 0x01,
    SLE_CRYTO_ALGO_AC2     = 0x02,
    SLE_CRYTO_ALGO_EA1     = 0x03,
    SLE_CRYTO_ALGO_EA2     = 0x04,
} sle_crypto_algo_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_CRYTO_ALGO_AC1 | 0x01 | AC1 加密算法类型 |
| SLE_CRYTO_ALGO_AC2 | 0x02 | AC2 加密算法类型 |
| SLE_CRYTO_ALGO_EA1 | 0x03 | EA1 加密算法类型 |
| SLE_CRYTO_ALGO_EA2 | 0x04 | EA2 加密算法类型 |

### sle_key_deriv_algo_t <a id="enum_sle_key_deriv_algo_t"></a>

```c
typedef enum {
    SLE_KEY_DERIV_ALGO_HA1     = 0x01,
    SLE_KEY_DERIV_ALGO_HA2     = 0x02,
} sle_key_deriv_algo_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_KEY_DERIV_ALGO_HA1 | 0x01 | HA1 秘钥分发算法类型 |
| SLE_KEY_DERIV_ALGO_HA2 | 0x02 | HA2 秘钥分发算法类型 |

### sle_integr_chk_ind_t <a id="enum_sle_integr_chk_ind_t"></a>

```c
typedef enum {
    SLE_ENCRYPTION_ENABLE_INTEGRITY_CHK_ENABLE      = 0x00,
    SLE_ENCRYPTION_DISABLE_INTEGRITY_CHK_ENABLE     = 0x01,
    SLE_ENCRYPTION_ENABLE_INTEGRITY_CHK_DISABLE     = 0x02,
    SLE_ENCRYPTION_DISABLE_INTEGRITY_CHK_DISABLE    = 0x03,
} sle_integr_chk_ind_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_ENCRYPTION_ENABLE_INTEGRITY_CHK_ENABLE | 0x00 | 加密和完整性保护同时启动 |
| SLE_ENCRYPTION_DISABLE_INTEGRITY_CHK_ENABLE | 0x01 | 不启动加密，启动完整性保护 |
| SLE_ENCRYPTION_ENABLE_INTEGRITY_CHK_DISABLE | 0x02 | 启动加密，不启动完整性保护 |
| SLE_ENCRYPTION_DISABLE_INTEGRITY_CHK_DISABLE | 0x03 | 不启动加密，不启动完整性保护 |

### sle_bond_ind_t <a id="enum_sle_bond_ind_t"></a>

```c
typedef enum {
    SLE_PAIR_NO_BOND      = 0x00,
    SLE_PAIR_NEED_BOND    = 0x01,
} sle_bond_ind_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_PAIR_NO_BOND | 0x00 | 星闪配对不需要绑定 |
| SLE_PAIR_NEED_BOND | 0x01 | 星闪配对需要绑定 |

### sle_link_role_t <a id="enum_sle_link_role_t"></a>

```c
typedef enum {
    SLE_LINK_ROLE_G     = 0,
    SLE_LINK_ROLE_T     = 1,
} sle_link_role_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_LINK_ROLE_G | 0 | G 节点 role |
| SLE_LINK_ROLE_T | 1 | T 节点 role |

### sle_radio_frame_t <a id="enum_sle_radio_frame_t"></a>

```c
typedef enum {
    SLE_RADIO_FRAME_1    = 0,
    SLE_RADIO_FRAME_2    = 1,
    SLE_RADIO_FRAME_3_M0 = 2,
    SLE_RADIO_FRAME_3_M1 = 3,
    SLE_RADIO_FRAME_3_M2 = 4,
    SLE_RADIO_FRAME_3_M3 = 5,
    SLE_RADIO_FRAME_3_M4 = 6,
    SLE_RADIO_FRAME_3_M5 = 7,
    SLE_RADIO_FRAME_4_M0 = 8,
    SLE_RADIO_FRAME_4_M1 = 9,
    SLE_RADIO_FRAME_4_M2 = 10,
    SLE_RADIO_FRAME_4_M3 = 11,
    SLE_RADIO_FRAME_4_M4 = 12,
    SLE_RADIO_FRAME_4_M5 = 13,
    SLE_RADIO_FRAME_END
} sle_radio_frame_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_RADIO_FRAME_1 | 0 | 无线帧类型1 |
| SLE_RADIO_FRAME_2 | 1 | 无线帧类型2 |
| SLE_RADIO_FRAME_3_M0 | 2 | 无线帧类型3，m序列0 |
| SLE_RADIO_FRAME_3_M1 | 3 | 无线帧类型3，m序列1 |
| SLE_RADIO_FRAME_3_M2 | 4 | 无线帧类型3，m序列2 |
| SLE_RADIO_FRAME_3_M3 | 5 | 无线帧类型3，m序列3 |
| SLE_RADIO_FRAME_3_M4 | 6 | 无线帧类型3，m序列4 |
| SLE_RADIO_FRAME_3_M5 | 7 | 无线帧类型3，m序列5 |
| SLE_RADIO_FRAME_4_M0 | 8 | 无线帧类型4，m序列0 |
| SLE_RADIO_FRAME_4_M1 | 9 | 无线帧类型4，m序列1 |
| SLE_RADIO_FRAME_4_M2 | 10 | 无线帧类型4，m序列2 |
| SLE_RADIO_FRAME_4_M3 | 11 | 无线帧类型4，m序列3 |
| SLE_RADIO_FRAME_4_M4 | 12 | 无线帧类型4，m序列4 |
| SLE_RADIO_FRAME_4_M5 | 13 | 无线帧类型4，m序列5 |
| SLE_RADIO_FRAME_END | 14 | 无线帧类型结束标志 |

### sle_phy_tx_rx_t <a id="enum_sle_phy_tx_rx_t"></a>

```c
typedef enum {
    SLE_PHY_1M = 0x0,
    SLE_PHY_2M = 0x1,
    SLE_PHY_4M = 0x2,
    SLE_PHY_SUPPORT_NUM,
} sle_phy_tx_rx_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_PHY_1M | 0x0 | 1M PHY |
| SLE_PHY_2M | 0x1 | 2M PHY |
| SLE_PHY_4M | 0x2 | 4M PHY |
| SLE_PHY_SUPPORT_NUM | 0x3 | PHY 支持数量 |

### sle_phy_tx_rx_pilot_density_t <a id="enum_sle_phy_tx_rx_pilot_density_t"></a>

```c
typedef enum {
    SLE_PHY_PILOT_DENSITY_4_TO_1  = 0x0,
    SLE_PHY_PILOT_DENSITY_8_TO_1  = 0x1,
    SLE_PHY_PILOT_DENSITY_16_TO_1 = 0x2,
    SLE_PHY_PILOT_DENSITY_NO = 0x3,
    SLE_PHY_PILOT_DENSITY_NUM,
} sle_phy_tx_rx_pilot_density_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_PHY_PILOT_DENSITY_4_TO_1 | 0x0 | 导频密度为4:1 |
| SLE_PHY_PILOT_DENSITY_8_TO_1 | 0x1 | 导频密度为8:1 |
| SLE_PHY_PILOT_DENSITY_16_TO_1 | 0x2 | 导频密度为16:1 |
| SLE_PHY_PILOT_DENSITY_NO | 0x3 | 无导频 |
| SLE_PHY_PILOT_DENSITY_NUM | 0x4 | 导频密度数量 |

### sle_save_smp_keys_mode_switch_t <a id="enum_sle_save_smp_keys_mode_switch_t"></a>

```c
typedef enum {
    SLE_SAVE_SMP_KEYS_AUTO = 0x00,
    SLE_SAVE_SMP_KEYS_MANU = 0x01,
} sle_save_smp_keys_mode_switch_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_SAVE_SMP_KEYS_AUTO | 0x00 | 秘钥自动保存 |
| SLE_SAVE_SMP_KEYS_MANU | 0x01 | 秘钥用户手动保存 |

### sle_announce_level_t <a id="enum_sle_announce_level_t"></a>

```c
typedef enum {
    SLE_ANNOUNCE_LEVEL_NONE,
    SLE_ANNOUNCE_LEVEL_NORMAL,
    SLE_ANNOUNCE_LEVEL_PRIORITY,
    SLE_ANNOUNCE_LEVEL_PAIRED,
    SLE_ANNOUNCE_LEVEL_SPECIAL,
} sle_announce_level_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_ANNOUNCE_LEVEL_NONE | 0 | 不可见发现，预留 |
| SLE_ANNOUNCE_LEVEL_NORMAL | 1 | 一般可发现 |
| SLE_ANNOUNCE_LEVEL_PRIORITY | 2 | 优先可发现，预留 |
| SLE_ANNOUNCE_LEVEL_PAIRED | 3 | 被曾配对过的设备发现，预留 |
| SLE_ANNOUNCE_LEVEL_SPECIAL | 4 | 被指定设备发现 |

### sle_announce_gt_role_t <a id="enum_sle_announce_gt_role_t"></a>

```c
typedef enum {
    SLE_ANNOUNCE_ROLE_T_CAN_NEGO = 0,
    SLE_ANNOUNCE_ROLE_G_CAN_NEGO,
    SLE_ANNOUNCE_ROLE_T_NO_NEGO,
    SLE_ANNOUNCE_ROLE_G_NO_NEGO
} sle_announce_gt_role_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_ANNOUNCE_ROLE_T_CAN_NEGO | 0 | 期望做T可协商 |
| SLE_ANNOUNCE_ROLE_G_CAN_NEGO | 1 | 期望做G可协商 |
| SLE_ANNOUNCE_ROLE_T_NO_NEGO | 2 | 期望做T不可协商 |
| SLE_ANNOUNCE_ROLE_G_NO_NEGO | 3 | 期望做G不可协商 |

### sle_announce_mode_t <a id="enum_sle_announce_mode_t"></a>

```c
typedef enum {
    SLE_ANNOUNCE_MODE_NONCONN_NONSCAN      = 0x00,
    SLE_ANNOUNCE_MODE_CONNECTABLE_NONSCAN  = 0x01,
    SLE_ANNOUNCE_MODE_NONCONN_SCANABLE     = 0x02,
    SLE_ANNOUNCE_MODE_CONNECTABLE_SCANABLE = 0x03,
    SLE_ANNOUNCE_MODE_CONNECTABLE_DIRECTED = 0x07,
} sle_announce_mode_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_ANNOUNCE_MODE_NONCONN_NONSCAN | 0x00 | 不可连接不可扫描 |
| SLE_ANNOUNCE_MODE_CONNECTABLE_NONSCAN | 0x01 | 可连接不可扫描 |
| SLE_ANNOUNCE_MODE_NONCONN_SCANABLE | 0x02 | 不可连接可扫描 |
| SLE_ANNOUNCE_MODE_CONNECTABLE_SCANABLE | 0x03 | 可连接可扫描 |
| SLE_ANNOUNCE_MODE_CONNECTABLE_DIRECTED | 0x07 | 可连接可扫描定向 |

### sle_seek_phy_t <a id="enum_sle_seek_phy_t"></a>

```c
typedef enum {
    SLE_SEEK_PHY_1M = 0x1,
    SLE_SEEK_PHY_2M = 0x2,
    SLE_SEEK_PHY_4M = 0x4,
} sle_seek_phy_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_SEEK_PHY_1M | 0x1 | 1M PHY |
| SLE_SEEK_PHY_2M | 0x2 | 2M PHY |
| SLE_SEEK_PHY_4M | 0x4 | 4M PHY |

### sle_seek_type_t <a id="enum_sle_seek_type_t"></a>

```c
typedef enum {
    SLE_SEEK_PASSIVE = 0x00,
    SLE_SEEK_ACTIVE  = 0x01,
} sle_seek_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_SEEK_PASSIVE | 0x00 | 被动扫描 |
| SLE_SEEK_ACTIVE | 0x01 | 主动扫描 |

### sle_seek_filter_t <a id="enum_sle_seek_filter_t"></a>

```c
typedef enum {
    SLE_SEEK_FILTER_ALLOW_ALL   = 0x00,
    SLE_SEEK_FILTER_ALLOW_WLST  = 0x01,
} sle_seek_filter_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_SEEK_FILTER_ALLOW_ALL | 0x00 | 允许来自任何人的设备发现数据包 |
| SLE_SEEK_FILTER_ALLOW_WLST | 0x01 | 允许来自白名单设备的设备发现数据包，预留 |

### sle_mcs_t <a id="enum_sle_mcs_t"></a>

```c
typedef enum {
    SLE_MCS_00 = 0,
    SLE_MCS_01,
    SLE_MCS_02,
    SLE_MCS_03,
    SLE_MCS_04,
    SLE_MCS_05,
    SLE_MCS_06,
    SLE_MCS_07,
    SLE_MCS_08,
    SLE_MCS_09,
    SLE_MCS_10,
    SLE_MCS_11,
    SLE_MCS_12,
    SLE_MCS_MAX,
} sle_mcs_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_MCS_00 | 0 | MCS0: BPSK1/4 |
| SLE_MCS_01 | 1 | MCS1: BPSK3/8 |
| SLE_MCS_02 | 2 | MCS2: QPSK1/4 |
| SLE_MCS_03 | 3 | MCS3: QPSK3/8 |
| SLE_MCS_04 | 4 | MCS4: QPSK1/2 |
| SLE_MCS_05 | 5 | MCS5: QPSK5/8 |
| SLE_MCS_06 | 6 | MCS6: QPSK3/4 |
| SLE_MCS_07 | 7 | MCS7: QPSK7/8 |
| SLE_MCS_08 | 8 | MCS8: QPSK 1 |
| SLE_MCS_09 | 9 | MCS9: 8PSK5/8 |
| SLE_MCS_10 | 10 | MCS10: 8PSK3/4 |
| SLE_MCS_11 | 11 | MCS11: 8PSK7/8 |
| SLE_MCS_12 | 12 | MCS12: 8PSK 1 |
| SLE_MCS_MAX | 13 | MCS 最大值 |

### sle_filter_policy_t <a id="enum_sle_filter_policy_t"></a>

```c
typedef enum {
    SLE_ANNOUNCE_FLT_ANY_SEEK_ANY_CONNECT,
    SLE_ANNOUNCE_FLT_WHITE_SEEK_ANY_CONNECT,
    SLE_ANNOUNCE_FLT_ANY_SEEK_WHITE_CONNECT,
    SLE_ANNOUNCE_FLT_WHITE_SEEK_WHITE_CONNECT
} sle_filter_policy_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_ANNOUNCE_FLT_ANY_SEEK_ANY_CONNECT | 0 | 接受所有 seek_req/conn_req |
| SLE_ANNOUNCE_FLT_WHITE_SEEK_ANY_CONNECT | 1 | 只接受符合过滤器的 seek_req |
| SLE_ANNOUNCE_FLT_ANY_SEEK_WHITE_CONNECT | 2 | 只接受符合过滤器的 conn_req |
| SLE_ANNOUNCE_FLT_WHITE_SEEK_WHITE_CONNECT | 3 | 接受符合过滤器的 seek_req/conn_req |

### sle_link_qos_state_t <a id="enum_sle_link_qos_state_t"></a>

```c
typedef enum {
    SLE_QOS_IDLE       = 0x00,
    SLE_QOS_FLOWCTRL   = 0x01,
    SLE_QOS_BUSY       = 0x02,
} sle_link_qos_state_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_QOS_IDLE | 0x00 | 空闲状态 |
| SLE_QOS_FLOWCTRL | 0x01 | 流控状态 |
| SLE_QOS_BUSY | 0x02 | 繁忙状态 |

### sle_addr_type_t <a id="enum_sle_addr_type_t"></a>

```c
typedef enum {
    SLE_ADDRESS_TYPE_PUBLIC = 0,
    SLE_ADDRESS_TYPE_RANDOM = 6,
} sle_addr_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_ADDRESS_TYPE_PUBLIC | 0 | 公有地址 |
| SLE_ADDRESS_TYPE_RANDOM | 6 | 随机地址 |

**使用说明**

SLE 设备地址类型，作为 [sle_addr_t](#struct_sle_addr_t) 成员 type 的取值。[SDK公共基础类型]

## Structures

### sle_connection_param_update_req_t <a id="struct_sle_connection_param_update_req_t"></a>

```c
typedef struct {
    uint16_t interval_min;
    uint16_t interval_max;
    uint16_t max_latency;
    uint16_t supervision_timeout;
} sle_connection_param_update_req_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| interval_min | uint16_t | 链路调度最小间隔，单位 slot |
| interval_max | uint16_t | 链路调度最大间隔，单位 slot |
| max_latency | uint16_t | 延迟周期，单位 slot |
| supervision_timeout | uint16_t | 超时时间，单位 10ms |

### sle_connection_param_update_t <a id="struct_sle_connection_param_update_t"></a>

```c
typedef struct {
    uint16_t conn_id;
    uint16_t interval_min;
    uint16_t interval_max;
    uint16_t max_latency;
    uint16_t supervision_timeout;
} sle_connection_param_update_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| conn_id | uint16_t | 连接 ID |
| interval_min | uint16_t | 链路调度最小间隔，单位 slot |
| interval_max | uint16_t | 链路调度最大间隔，单位 slot |
| max_latency | uint16_t | 延迟周期，单位 slot |
| supervision_timeout | uint16_t | 超时时间，单位 10ms |

### sle_connection_param_update_evt_t <a id="struct_sle_connection_param_update_evt_t"></a>

```c
typedef struct {
    uint16_t interval;
    uint16_t latency;
    uint16_t supervision;
} sle_connection_param_update_evt_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| interval | uint16_t | 链路调度间隔，单位 slot |
| latency | uint16_t | 延迟周期，单位 slot |
| supervision | uint16_t | 超时时间，单位 10ms |

### sle_auth_info_evt_t <a id="struct_sle_auth_info_evt_t"></a>

```c
typedef struct {
    uint8_t link_key[SLE_LINK_KEY_LEN];
    uint8_t crypto_algo;
    uint8_t key_deriv_algo;
    uint8_t integr_chk_ind;
    uint8_t is_bond;
} sle_auth_info_evt_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| link_key | uint8_t[] | 链路密钥，长度为 [SLE_LINK_KEY_LEN](#SLE_LINK_KEY_LEN)(16) |
| crypto_algo | uint8_t | 加密算法类型，参考 [sle_crypto_algo_t](#enum_sle_crypto_algo_t) |
| key_deriv_algo | uint8_t | 秘钥分发算法类型，参考 [sle_key_deriv_algo_t](#enum_sle_key_deriv_algo_t) |
| integr_chk_ind | uint8_t | 完整性校验指示，参考 [sle_integr_chk_ind_t](#enum_sle_integr_chk_ind_t) |
| is_bond | uint8_t | 配对绑定指示，参考 [sle_bond_ind_t](#enum_sle_bond_ind_t) |

### sle_set_phy_t <a id="struct_sle_set_phy_t"></a>

```c
typedef struct {
    uint8_t tx_format;
    uint8_t rx_format;
    uint8_t tx_phy;
    uint8_t rx_phy;
    uint8_t tx_pilot_density;
    uint8_t rx_pilot_density;
    uint8_t g_feedback;
    uint8_t t_feedback;
} sle_set_phy_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| tx_format | uint8_t | 发送无线帧类型，参考 [sle_radio_frame_t](#enum_sle_radio_frame_t) |
| rx_format | uint8_t | 接收无线帧类型，参考 [sle_radio_frame_t](#enum_sle_radio_frame_t) |
| tx_phy | uint8_t | 发送 PHY，参考 [sle_phy_tx_rx_t](#enum_sle_phy_tx_rx_t) |
| rx_phy | uint8_t | 接收 PHY，参考 [sle_phy_tx_rx_t](#enum_sle_phy_tx_rx_t) |
| tx_pilot_density | uint8_t | 发送导频密度指示，参考 [sle_phy_tx_rx_pilot_density_t](#enum_sle_phy_tx_rx_pilot_density_t) |
| rx_pilot_density | uint8_t | 接收导频密度指示，参考 [sle_phy_tx_rx_pilot_density_t](#enum_sle_phy_tx_rx_pilot_density_t) |
| g_feedback | uint8_t | 先发链路反馈类型指示，取值范围 0-63 |
| t_feedback | uint8_t | 后发链路反馈类型指示，取值范围 0-7 |

### sle_default_connect_param_t <a id="struct_sle_default_connect_param_t"></a>

```c
typedef struct {
    uint8_t  enable_filter_policy;
    uint8_t  initiate_phys;
    uint8_t  gt_negotiate;
    uint16_t scan_interval;
    uint16_t scan_window;
    uint16_t min_interval;
    uint16_t max_interval;
    uint16_t timeout;
} sle_default_connect_param_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| enable_filter_policy | uint8_t | 链路是否打开过滤功能 |
| initiate_phys | uint8_t | 链路扫描通信带宽：1 表示 1M，2 表示 2M |
| gt_negotiate | uint8_t | 链路建立时是否进行 G 和 T 交互 |
| scan_interval | uint16_t | 链路建立时扫描对端设备的 interval |
| scan_window | uint16_t | 链路建立时扫描对端设备的 windows |
| min_interval | uint16_t | 链路调度最小 interval |
| max_interval | uint16_t | 链路调度最大 interval |
| timeout | uint16_t | 链路超时时间 |

### sle_connection_callbacks_t <a id="struct_sle_connection_callbacks_t"></a>

```c
typedef struct {
    sle_connect_state_changed_callback connect_state_changed_cb;
    sle_connect_param_update_req_callback connect_param_update_req_cb;
    sle_connect_param_update_callback connect_param_update_cb;
    sle_auth_complete_callback auth_complete_cb;
    sle_pair_complete_callback pair_complete_cb;
    sle_read_rssi_callback read_rssi_cb;
    sle_low_latency_callback low_latency_cb;
    sle_set_phy_callback set_phy_cb;
    sle_pair_remove_callback pair_remove_cb;
} sle_connection_callbacks_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| connect_state_changed_cb | [sle_connect_state_changed_callback](#sle_connect_state_changed_callback) | 连接状态改变回调函数 |
| connect_param_update_req_cb | [sle_connect_param_update_req_callback](#sle_connect_param_update_req_callback) | 连接参数更新请求回调函数 |
| connect_param_update_cb | [sle_connect_param_update_callback](#sle_connect_param_update_callback) | 连接参数更新回调函数 |
| auth_complete_cb | [sle_auth_complete_callback](#sle_auth_complete_callback) | 认证完成回调函数 |
| pair_complete_cb | [sle_pair_complete_callback](#sle_pair_complete_callback) | 配对完成回调函数 |
| read_rssi_cb | [sle_read_rssi_callback](#sle_read_rssi_callback) | 读取 RSSI 回调函数 |
| low_latency_cb | [sle_low_latency_callback](#sle_low_latency_callback) | 设置 low latency 回调函数 |
| set_phy_cb | [sle_set_phy_callback](#sle_set_phy_callback) | 设置 PHY 回调函数 |
| pair_remove_cb | [sle_pair_remove_callback](#sle_pair_remove_callback) | 取消配对完成回调函数 |

### sle_conn_param_t <a id="struct_sle_conn_param_t"></a>

```c
typedef struct sle_conn_param {
    uint16_t interval_min;
    uint16_t interval_max;
    uint16_t max_latency;
    uint16_t supervision_timeout;
    uint16_t min_ce_length;
    uint16_t max_ce_length;
} sle_conn_param_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| interval_min | uint16_t | 连接间隔最小取值，取值范围 [0x001E,0x3E80]，时间 = N * 0.25ms，范围 [7.5ms,4s] |
| interval_max | uint16_t | 连接间隔最大取值，取值范围 [0x001E,0x3E80]，时间 = N * 0.25ms，范围 [7.5ms,4s] |
| max_latency | uint16_t | 最大休眠连接间隔，取值范围 [0x0000,0x01F3]，默认 0x0000 |
| supervision_timeout | uint16_t | 最大超时时间，取值范围 [0x000A,0x0C80]，时间 = N * 10ms，范围 [100ms,32s] |
| min_ce_length | uint16_t | 推荐的连接事件最小取值，取值范围 [0x0000,0xFFFF]，时间 = N * 0.125ms |
| max_ce_length | uint16_t | 推荐的连接事件最大取值，取值范围 [0x0000,0xFFFF]，时间 = N * 0.125ms |

### sle_announce_param_t <a id="struct_sle_announce_param_t"></a>

```c
typedef struct sle_announce_param {
    uint8_t  announce_handle;
    uint8_t  announce_mode;
    uint8_t  announce_gt_role;
    uint8_t  announce_level;
    uint32_t announce_interval_min;
    uint32_t announce_interval_max;
    uint8_t  announce_channel_map;
    int8_t   announce_tx_power;
    sle_addr_t own_addr;
    sle_addr_t peer_addr;
    uint16_t conn_interval_min;
    uint16_t conn_interval_max;
    uint16_t conn_max_latency;
    uint16_t conn_supervision_timeout;
    void *ext_param;
} sle_announce_param_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| announce_handle | uint8_t | 设备公开句柄，取值范围 [0, 0xFF] |
| announce_mode | uint8_t | 设备公开类型，参考 [sle_announce_mode_t](#enum_sle_announce_mode_t) |
| announce_gt_role | uint8_t | G/T 角色协商指示，参考 [sle_announce_gt_role_t](#enum_sle_announce_gt_role_t) |
| announce_level | uint8_t | 发现等级，参考 [sle_announce_level_t](#enum_sle_announce_level_t) |
| announce_interval_min | uint32_t | 最小设备公开周期，取值范围 0x000020~0xffffff，单位 125us |
| announce_interval_max | uint32_t | 最大设备公开周期，取值范围 0x000020~0xffffff，单位 125us |
| announce_channel_map | uint8_t | 设备公开信道，0:76，1:77，2:78 |
| announce_tx_power | int8_t | 广播发射功率，单位 dbm，取值范围 [-127, 20]，0x7F 表示不设置特定发送功率 |
| own_addr | [sle_addr_t](#struct_sle_addr_t) | 本端地址 |
| peer_addr | [sle_addr_t](#struct_sle_addr_t) | 对端地址 |
| conn_interval_min | uint16_t | 连接间隔最小取值，取值范围 [0x001E,0x3E80]，announce_gt_role 为 SLE_ANNOUNCE_ROLE_T_NO_NEGO 时无需配置 |
| conn_interval_max | uint16_t | 连接间隔最大取值，取值范围 [0x001E,0x3E80]，announce_gt_role 为 SLE_ANNOUNCE_ROLE_T_NO_NEGO 时无需配置 |
| conn_max_latency | uint16_t | 最大休眠连接间隔，取值范围 [0x0000,0x01F3]，announce_gt_role 为 SLE_ANNOUNCE_ROLE_T_NO_NEGO 时无需配置 |
| conn_supervision_timeout | uint16_t | 最大超时时间，取值范围 [0x000A,0x0C80]，announce_gt_role 为 SLE_ANNOUNCE_ROLE_T_NO_NEGO 时无需配置 |
| ext_param | void * | 扩展设备公开参数，缺省时置空 |

### sle_announce_data_t <a id="struct_sle_announce_data_t"></a>

```c
typedef struct sle_announce_data {
    uint16_t announce_data_len;
    uint16_t seek_rsp_data_len;
    uint8_t  *announce_data;
    uint8_t  *seek_rsp_data;
} sle_announce_data_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| announce_data_len | uint16_t | 设备公开数据长度 |
| seek_rsp_data_len | uint16_t | 扫描响应数据长度 |
| announce_data | uint8_t * | 设备公开数据 |
| seek_rsp_data | uint8_t * | 扫描响应数据 |

### sle_announce_enable_t <a id="struct_sle_announce_enable_t"></a>

```c
typedef struct sle_announce_enable {
    uint8_t enable;
    uint8_t announce_handle;
    uint16_t duration;
    uint8_t max_announce_events;
} sle_announce_enable_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| enable | uint8_t | 0x0 表示关闭设备公开，0x1 表示使能设备公开 |
| announce_handle | uint8_t | 设备公开句柄 |
| duration | uint16_t | 0x0 表示设备公开时间无限制，0x1~0xFFFF 表示设备公开时间 = N * 10ms |
| max_announce_events | uint8_t | 0x0 表示设备公开事件个数无限制，0x1~0xFF 表示设备公开事件个数限制 |

### sle_seek_param_t <a id="struct_sle_seek_param_t"></a>

```c
typedef struct sle_seek_params {
    uint8_t own_addr_type;
    uint8_t filter_duplicates;
    uint8_t seek_filter_policy;
    uint8_t seek_phys;
    uint8_t seek_type[SLE_SEEK_PHY_NUM_MAX];
    uint16_t seek_interval[SLE_SEEK_PHY_NUM_MAX];
    uint16_t seek_window[SLE_SEEK_PHY_NUM_MAX];
} sle_seek_param_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| own_addr_type | uint8_t | 本端地址类型 |
| filter_duplicates | uint8_t | 重复过滤开关，0 表示关闭，1 表示开启 |
| seek_filter_policy | uint8_t | 扫描设备使用的过滤类型，参考 [sle_seek_filter_t](#enum_sle_seek_filter_t) |
| seek_phys | uint8_t | 扫描设备所使用的 PHY，参考 [sle_seek_phy_t](#enum_sle_seek_phy_t) |
| seek_type | uint8_t[] | 扫描类型，参考 [sle_seek_type_t](#enum_sle_seek_type_t)，数组大小 [SLE_SEEK_PHY_NUM_MAX](#SLE_SEEK_PHY_NUM_MAX)(3) |
| seek_interval | uint16_t[] | 扫描间隔，取值范围 [0x0014, 0xFFFF]，时间 = N * 0.125ms，数组大小 [SLE_SEEK_PHY_NUM_MAX](#SLE_SEEK_PHY_NUM_MAX)(3) |
| seek_window | uint16_t[] | 扫描窗口，取值范围 [0x0014, 0xFFFF]，时间 = N * 0.125ms，数组大小 [SLE_SEEK_PHY_NUM_MAX](#SLE_SEEK_PHY_NUM_MAX)(3) |

### sle_seek_result_info_t <a id="struct_sle_seek_result_info_t"></a>

```c
typedef struct sle_seek_result_info {
    uint8_t event_type;
    sle_addr_t addr;
    sle_addr_t direct_addr;
    int8_t rssi;
    uint8_t data_status;
    uint8_t data_length;
    uint8_t *data;
} sle_seek_result_info_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| event_type | uint8_t | 上报事件类型 |
| addr | [sle_addr_t](#struct_sle_addr_t) | 地址 |
| direct_addr | [sle_addr_t](#struct_sle_addr_t) | 定向发现地址 |
| rssi | int8_t | 信号强度指示，取值范围 [-127dBm, 20dBm]，0x7F 表示不提供信号强度指示 |
| data_status | uint8_t | 数据状态 |
| data_length | uint8_t | 数据长度 |
| data | uint8_t * | 数据 |

### sle_announce_seek_callbacks_t <a id="struct_sle_announce_seek_callbacks_t"></a>

```c
typedef struct {
    sle_announce_enable_callback announce_enable_cb;
    sle_announce_disable_callback announce_disable_cb;
    sle_announce_terminal_callback announce_terminal_cb;
    sle_announce_remove_callback announce_remove_cb;
    sle_start_seek_callback seek_enable_cb;
    sle_seek_disable_callback seek_disable_cb;
    sle_seek_result_callback seek_result_cb;
    sle_dfr_callback sle_dfr_cb;
} sle_announce_seek_callbacks_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| announce_enable_cb | [sle_announce_enable_callback](#sle_announce_enable_callback) | 设备公开使能回调函数 |
| announce_disable_cb | [sle_announce_disable_callback](#sle_announce_disable_callback) | 设备公开关闭回调函数 |
| announce_terminal_cb | [sle_announce_terminal_callback](#sle_announce_terminal_callback) | 设备公开停止回调函数 |
| announce_remove_cb | [sle_announce_remove_callback](#sle_announce_remove_callback) | 设备公开停止回调函数 |
| seek_enable_cb | [sle_start_seek_callback](#sle_start_seek_callback) | 扫描使能回调函数 |
| seek_disable_cb | [sle_seek_disable_callback](#sle_seek_disable_callback) | 扫描关闭回调函数 |
| seek_result_cb | [sle_seek_result_callback](#sle_seek_result_callback) | 扫描结果回调函数 |
| sle_dfr_cb | [sle_dfr_callback](#sle_dfr_callback) | dfr 回调函数 |

### sle_transmission_signal_capability_bit_t <a id="struct_sle_transmission_signal_capability_bit_t"></a>

```c
typedef struct {
    uint32_t relay_capability : 1;
    uint32_t trans_mode : 1;
    uint32_t measurement_capability : 1;
    uint32_t access_slb : 1;
    uint32_t access_sle : 1;
    uint32_t mtu : 1;
    uint32_t mps : 1;
    uint32_t reverse : 25;
} sle_transmission_signal_capability_bit_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| relay_capability | uint32_t:1 | 中继能力 |
| trans_mode | uint32_t:1 | 传输模式 |
| measurement_capability | uint32_t:1 | 测量能力 |
| access_slb | uint32_t:1 | slb 接入 |
| access_sle | uint32_t:1 | sle 接入 |
| mtu | uint32_t:1 | 最大支持 mtu |
| mps | uint32_t:1 | 最大支持 mps |
| reverse | uint32_t:25 | 保留比特位 |

### sle_transmission_callbacks_t <a id="struct_sle_transmission_callbacks_t"></a>

```c
typedef struct {
    sle_trans_data_busy_callback send_data_cb;
} sle_transmission_callbacks_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| send_data_cb | [sle_trans_data_busy_callback](#sle_trans_data_busy_callback) | 传输数据繁忙回调函数 |

### sle_addr_t <a id="struct_sle_addr_t"></a>

```c
typedef struct {
    uint8_t type;
    unsigned char addr[SLE_ADDR_LEN];
} sle_addr_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| type | uint8_t | SLE 设备地址类型，参考 [sle_addr_type_t](#enum_sle_addr_type_t) |
| addr | unsigned char[] | SLE 设备地址，长度为 [SLE_ADDR_LEN](#SLE_ADDR_LEN)(6) |

**使用说明**

SLE 设备地址结构，作为本模块多个对外接口的入参/出参载体。[SDK公共基础类型]

## Macros

### SLE_ANNOUNCE_ID_MAX <a id="SLE_ANNOUNCE_ID_MAX"></a>

```c
#define SLE_ANNOUNCE_ID_MAX 16
```

### SLE_SEEK_PHY_NUM_MAX <a id="SLE_SEEK_PHY_NUM_MAX"></a>

```c
#define SLE_SEEK_PHY_NUM_MAX 3
```

### SLE_ADDR_LEN <a id="SLE_ADDR_LEN"></a>

```c
#define SLE_ADDR_LEN        6
```

### SLE_LINK_KEY_LEN <a id="SLE_LINK_KEY_LEN"></a>

```c
#define SLE_LINK_KEY_LEN    16
```
