# P2P

P2P (Wi-Fi Peer-to-Peer) 提供 Wi-Fi 直连功能，支持设备扫描、连接、断连及 GO (Group Owner) / GC (Group Client) 角色协商，实现无需接入点的点对点 Wi-Fi 通信。

**头文件清单**

```c
#include "middleware/services/wifi/wifi_p2p.h"
#include "middleware/services/wifi/wifi_p2p_config.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [wifi_p2p_enable](#wifi_p2p_enable) | 开启 P2P 功能 |
| [wifi_p2p_disable](#wifi_p2p_disable) | 关闭 P2P 功能 |
| [wifi_p2p_is_enabled](#wifi_p2p_is_enabled) | 获取 P2P 使能状态 |
| [wifi_p2p_find](#wifi_p2p_find) | 触发 P2P 设备扫描搜索 |
| [wifi_p2p_stop_find](#wifi_p2p_stop_find) | 停止 P2P 设备扫描 |
| [wifi_p2p_connect_cancel](#wifi_p2p_connect_cancel) | 停止 P2P 设备连接 |
| [wifi_p2p_listen](#wifi_p2p_listen) | 设置 P2P 设备监听时间 |
| [wifi_p2p_get_peers_info](#wifi_p2p_get_peers_info) | 获取搜索到的 P2P 设备信息 |
| [wifi_p2p_connect](#wifi_p2p_connect) | P2P 主动连接对端设备 |
| [wifi_p2p_connect_accept](#wifi_p2p_connect_accept) | 接受或拒绝对端的 P2P 连接请求 |
| [wifi_p2p_disconnect](#wifi_p2p_disconnect) | 断开 P2P 连接 |
| [wifi_p2p_go_get_gc_info](#wifi_p2p_go_get_gc_info) | GO 获取已连接的 GC 信息 |
| [wifi_p2p_set_device_config](#wifi_p2p_set_device_config) | 设置 P2P 设备信息 |
| [wifi_p2p_get_device_config](#wifi_p2p_get_device_config) | 获取 P2P 设备信息 |
| [wifi_p2p_get_connect_info](#wifi_p2p_get_connect_info) | 获取 P2P 连接状态信息 |

## Functions

### wifi_p2p_enable <a id="wifi_p2p_enable"></a>

```c
errcode_t wifi_p2p_enable(void)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_p2p.h"
```

**功能说明**

- 开启 P2P 功能接口
- 初始化 P2P 模块相关资源
- 调用后 P2P 设备进入可用状态

**前置条件**

- 调用时序约束：需在 Wi-Fi 驱动初始化完成后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | P2P 功能开启成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### wifi_p2p_disable <a id="wifi_p2p_disable"></a>

```c
errcode_t wifi_p2p_disable(void)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_p2p.h"
```

**功能说明**

- 关闭 P2P 功能接口
- 释放 P2P 模块相关资源
- 调用后 P2P 设备进入不可用状态

**前置条件**

- 调用时序约束：需在 wifi_p2p_enable 成功返回后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | P2P 功能关闭成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### wifi_p2p_is_enabled <a id="wifi_p2p_is_enabled"></a>

```c
int32_t wifi_p2p_is_enabled(void)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_p2p.h"
```

**功能说明**

- 查询 P2P 功能是否已使能
- 返回 P2P 初始化状态
- 用于判断 P2P 模块是否处于可用状态

**前置条件**

- 调用时序约束：需在 Wi-Fi 驱动初始化完成后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**返回值**

- 返回类型：int32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 1 | P2P 已初始化 | P2P 功能已开启 |
| 0 | P2P 未初始化 | P2P 功能未开启 |

### wifi_p2p_find <a id="wifi_p2p_find"></a>

```c
errcode_t wifi_p2p_find(int32_t sec)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_p2p.h"
```

**功能说明**

- 触发 P2P 设备扫描搜索
- 在指定时间内扫描周围 P2P 设备
- 扫描结果可通过 wifi_p2p_get_peers_info 获取

**前置条件**

- 调用时序约束：需在 wifi_p2p_enable 成功返回后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| sec | int32_t | 扫描时间，单位秒 | 大于0 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | P2P 设备扫描启动成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### wifi_p2p_stop_find <a id="wifi_p2p_stop_find"></a>

```c
errcode_t wifi_p2p_stop_find(void)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_p2p.h"
```

**功能说明**

- 停止 P2P 设备扫描
- 终止当前正在进行的 P2P 设备搜索过程
- 调用后不再继续扫描周围 P2P 设备

**前置条件**

- 调用时序约束：需在 wifi_p2p_find 调用后使用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | P2P 扫描停止成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### wifi_p2p_connect_cancel <a id="wifi_p2p_connect_cancel"></a>

```c
errcode_t wifi_p2p_connect_cancel(void)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_p2p.h"
```

**功能说明**

- 停止 P2P 设备连接过程
- 终止当前正在进行的 P2P 连接协商
- 调用后取消与对端设备的连接流程

**前置条件**

- 调用时序约束：需在 wifi_p2p_enable 成功返回后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | P2P 连接取消成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### wifi_p2p_listen <a id="wifi_p2p_listen"></a>

```c
errcode_t wifi_p2p_listen(uint32_t period, uint32_t interval)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_p2p.h"
```

**功能说明**

- 设置 P2P 设备监听时间参数
- 配置监听周期和总时间间隔
- 使 P2P 设备在指定时间窗口内监听对端请求

**前置条件**

- 调用时序约束：需在 wifi_p2p_enable 成功返回后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| period | uint32_t | 监听时间 | 大于0 |
| interval | uint32_t | 一个周期的总时间 | 大于0 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | P2P 监听设置成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### wifi_p2p_get_peers_info <a id="wifi_p2p_get_peers_info"></a>

```c
errcode_t wifi_p2p_get_peers_info(p2p_device_stru *dev_list, uint32_t *dev_num)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_p2p.h"
```

**功能说明**

- 获取扫描发现的 P2P 设备信息列表
- 返回 P2P 设备名称、MAC 地址、WPS 连接方式等信息
- 入参 dev_num 同时用于传入最大反馈数量与返回实际反馈数量

**前置条件**

- 调用时序约束：需在 wifi_p2p_find 执行并扫描到设备后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| dev_list | [p2p_device_stru](#p2p_device_stru)* | 搜索到的 P2P 设备列表缓冲区 | 不为NULL |
| dev_num | uint32_t* | 最大反馈 P2P 设备数目 | 大于0 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| dev_list | [p2p_device_stru](#p2p_device_stru)* | 搜索到的 P2P 设备信息列表，由调用方分配内存、函数填充 |
| dev_num | uint32_t* | 实际反馈的 P2P 设备数目 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | P2P 设备信息获取成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### wifi_p2p_connect <a id="wifi_p2p_connect"></a>

```c
errcode_t wifi_p2p_connect(const p2p_config_stru *p2p_config)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_p2p.h"
```

**功能说明**

- P2P 主动连接对端设备
- 根据配置信息发起与指定 P2P 设备的连接
- 支持 WPS 连接方式、GO intent 等参数配置

**前置条件**

- 调用时序约束：需在 wifi_p2p_enable 成功返回后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| p2p_config | const [p2p_config_stru](#p2p_config_stru)* | 待连接的 P2P 设备网络信息 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | P2P 连接请求发起成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### wifi_p2p_connect_accept <a id="wifi_p2p_connect_accept"></a>

```c
errcode_t wifi_p2p_connect_accept(const p2p_config_stru *p2p_config, int assoc)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_p2p.h"
```

**功能说明**

- 接受或拒绝对端的 P2P 连接请求
- 根据 assoc 参数决定是否接受连接
- 配合 P2P 连接协商流程使用

**前置条件**

- 调用时序约束：需在收到对端 P2P 连接请求后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| p2p_config | const [p2p_config_stru](#p2p_config_stru)* | 待连接的 P2P 设备网络信息 | 不为NULL |
| assoc | int | 连接接受标志，1 表示接受连接，0 表示拒绝连接 | 0 / 1 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | P2P 连接响应设置成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### wifi_p2p_disconnect <a id="wifi_p2p_disconnect"></a>

```c
errcode_t wifi_p2p_disconnect(void)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_p2p.h"
```

**功能说明**

- 断开当前 P2P 连接
- 终止与对端设备的 P2P 连接关系
- 调用后设备恢复到未连接状态

**前置条件**

- 调用时序约束：需在 P2P 已建立连接后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | P2P 断连成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### wifi_p2p_go_get_gc_info <a id="wifi_p2p_go_get_gc_info"></a>

```c
errcode_t wifi_p2p_go_get_gc_info(p2p_client_info_stru *client_list, uint32_t *client_num)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_p2p.h"
```

**功能说明**

- GO (Group Owner) 获取已连接的 GC (Group Client) 信息
- 返回 GC 的 MAC 地址、设备地址和设备名称
- 入参 client_num 同时用于传入最大反馈数量与返回实际反馈数量

**前置条件**

- 调用时序约束：需在 P2P 以 GO 模式连接成功后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| client_list | [p2p_client_info_stru](#p2p_client_info_stru)* | GC 信息列表缓冲区 | 不为NULL |
| client_num | uint32_t* | 最大反馈 GC 个数 | 大于0 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| client_list | [p2p_client_info_stru](#p2p_client_info_stru)* | 已连接 GC 的信息列表，由调用方分配内存、函数填充 |
| client_num | uint32_t* | 实际反馈的 GC 个数 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | GC 信息获取成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### wifi_p2p_set_device_config <a id="wifi_p2p_set_device_config"></a>

```c
errcode_t wifi_p2p_set_device_config(const p2p_device_config_stru *p2p_dev_set_info)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_p2p.h"
```

**功能说明**

- 设置 P2P 设备信息
- 配置设备名称、WPS 连接方式、监听信道和工作信道
- 在 P2P 连接前配置本端设备参数

**前置条件**

- 调用时序约束：需在 wifi_p2p_enable 成功返回后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| p2p_dev_set_info | const [p2p_device_config_stru](#p2p_device_config_stru)* | P2P 设备设置信息 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | P2P 设备信息设置成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### wifi_p2p_get_device_config <a id="wifi_p2p_get_device_config"></a>

```c
errcode_t wifi_p2p_get_device_config(p2p_device_config_stru *p2p_dev_set_info)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_p2p.h"
```

**功能说明**

- 获取 P2P 设备信息
- 读取当前设备名称、WPS 连接方式、监听信道和工作信道等配置
- 用于查询本端 P2P 设备参数

**前置条件**

- 调用时序约束：需在 wifi_p2p_enable 成功返回后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| p2p_dev_set_info | [p2p_device_config_stru](#p2p_device_config_stru)* | P2P 设备设置信息缓冲区 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| p2p_dev_set_info | [p2p_device_config_stru](#p2p_device_config_stru)* | P2P 设备设置信息，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | P2P 设备信息获取成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

### wifi_p2p_get_connect_info <a id="wifi_p2p_get_connect_info"></a>

```c
errcode_t wifi_p2p_get_connect_info(p2p_status_info_stru *status)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_p2p.h"
```

**功能说明**

- 获取 P2P 连接状态信息
- 返回工作信道中心频点、P2P 模式、关联状态、Group SSID 和 Group BSSID
- 用于查询当前 P2P 连接的详细状态

**前置条件**

- 调用时序约束：需在 wifi_p2p_enable 成功返回后调用
- 上下文限制：需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| status | [p2p_status_info_stru](#p2p_status_info_stru)* | 待反馈的 P2P 连接状态信息缓冲区 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| status | [p2p_status_info_stru](#p2p_status_info_stru)* | P2P 连接状态信息，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | P2P 连接状态信息获取成功 |
| Other | 其他错误码，参考`errcode_t` | 执行失败 |

## Enumerations

### wps_method_enum <a id="wps_method_enum"></a>

```c
typedef enum {
    WPS_PBC,
    WPS_PIN_DISPLAY,
    WPS_PIN_KEYPAD,
    WPS_PIN_LABEL,
    WPS_OTHER,
} wps_method_enum;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| WPS_PBC | 0 | PBC 方式连接 |
| WPS_PIN_DISPLAY | 1 | PIN DISPLAY 方式连接 |
| WPS_PIN_KEYPAD | 2 | PIN KEYPAD 方式连接 |
| WPS_PIN_LABEL | 3 | PIN LABEL 方式连接 |
| WPS_OTHER | 4 | 其他方式连接 |

### p2p_mode_enum <a id="p2p_mode_enum"></a>

```c
typedef enum {
    P2P_MODE_GC,
    P2P_MODE_GO,
    P2P_MODE_DEVICE_ONLY,
    P2P_MODE_BUTT,
} p2p_mode_enum;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| P2P_MODE_GC | 0 | P2P GC 模式 |
| P2P_MODE_GO | 1 | P2P GO 模式 |
| P2P_MODE_DEVICE_ONLY | 2 | P2P 未协商 GO |
| P2P_MODE_BUTT | 3 | P2P 模式边界值 |

### p2p_conn_state_enum <a id="p2p_conn_state_enum"></a>

```c
typedef enum {
    P2P_DISCONNECTED,
    P2P_CONNECTED,
    P2P_CONNECTING,
    P2P_CONN_STATUS_BUTT,
} p2p_conn_state_enum;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| P2P_DISCONNECTED | 0 | 断连 |
| P2P_CONNECTED | 1 | 已连接 |
| P2P_CONNECTING | 2 | 连接中 |
| P2P_CONN_STATUS_BUTT | 3 | 连接状态边界值 |

## Structures

### wfd_info_stru <a id="wfd_info_stru"></a>

```c
typedef struct wfd_info_stru {
    int16_t device_info;    /*!< WFD设备类型。 */
    int16_t ctrl_port;      /*!< 控制端口号。 */
    int16_t max_throughput; /*!< 最大吞吐量。 */
    int8_t reserved[2];
} wfd_info_stru;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| device_info | int16_t | WFD 设备类型 |
| ctrl_port | int16_t | 控制端口号 |
| max_throughput | int16_t | 最大吞吐量 |
| reserved | int8_t[2] | 保留字段 |

### p2p_device_stru <a id="p2p_device_stru"></a>

```c
typedef struct p2p_device_stru {
    int8_t name[WPS_DEV_NAME_LEN];  /*!< 设备device名称。 */
    uint8_t bssid[WIFI_MAC_LEN];    /*!< 设备device MAC地址。 */
    uint8_t wps_method;             /*!< 支持的WPS连接方式，
                                                 - bit0表示PBC
                                                 - bit1表示PIN LABEL
                                                 - bit2表示PIN DISPLAY
                                                 - bit3表示PIN KEYPAD
                                                 - bit4表示其他方式。 */
    uint8_t is_go           : 1;    /*!< 扫描出来的设备是否是p2p go。 */
    uint8_t enable_add_group : 1;   /*!< 扫描出的go对应的group，是否允许添加gc。 */
    uint8_t reserved       : 6;
    int8_t reserved1[3];
    wfd_info_stru wfd_info;         /*!< 暂不使用。 */
} p2p_device_stru;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| name | int8_t[WPS_DEV_NAME_LEN] | 设备名称 |
| bssid | uint8_t[WIFI_MAC_LEN] | 设备 MAC 地址 |
| wps_method | uint8_t | 支持的 WPS 连接方式，bit0 表示 PBC，bit1 表示 PIN LABEL，bit2 表示 PIN DISPLAY，bit3 表示 PIN KEYPAD，bit4 表示其他方式 |
| is_go | uint8_t:1 | 扫描到的设备是否为 P2P GO |
| enable_add_group | uint8_t:1 | 扫描出的 GO 对应的 group 是否允许添加 GC |
| reserved | uint8_t:6 | 保留位 |
| reserved1 | int8_t[3] | 保留字段 |
| wfd_info | [wfd_info_stru](#wfd_info_stru) | WFD 相关信息，暂不使用 |

### p2p_config_stru <a id="p2p_config_stru"></a>

```c
typedef struct p2p_config_stru {
    uint8_t bssid[WIFI_MAC_LEN];           /*!< peer的device MAC地址。 */
    int8_t pin[WIFI_WPS_PIN_MAX_LEN_NUM];  /*!< WPS的Pin码。 */
    uint8_t wps_method;                    /*!< WPS的连接方式。 */
    uint8_t go_intent;                     /*!< go intent，有效范围0~15。 */
    uint8_t persistent;                    /*!< 1:按照永久网络存储;0:不按照永久网络存储。 */
    int8_t reserved[2];
} p2p_config_stru;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| bssid | uint8_t[WIFI_MAC_LEN] | 对端设备 MAC 地址 |
| pin | int8_t[WIFI_WPS_PIN_MAX_LEN_NUM] | WPS 的 PIN 码 |
| wps_method | uint8_t | WPS 的连接方式 |
| go_intent | uint8_t | GO intent，有效范围 0~15 |
| persistent | uint8_t | 1 表示按照永久网络存储，0 表示不按照永久网络存储 |
| reserved | int8_t[2] | 保留字段 |

### p2p_status_info_stru <a id="p2p_status_info_stru"></a>

```c
typedef struct p2p_status_info_stru {
    int32_t operation_channel;            /*!< GO/GC连接之后工作信道的中心频点，在wpa_state为CONNECTED时有效。 */
    uint8_t mode;                         /*!< P2P模式, 和P2pMode对应。 */
    uint8_t wpa_state;                    /*!< p2p关联状态，和P2pConnState对应.。 */
    int8_t group_ssid[WPS_DEV_NAME_LEN];  /*!< Group SSID，并且P2P的WPS关联成功（当前阶段组协商成功）时有效。 */
    uint8_t group_bssid[WIFI_MAC_LEN];    /*!< Group BSSID==go bssid，在wpa_state为CONNECTED，
                                                       并且P2P的WPS关联成功（当前阶段组协商成功）时有效。 */
    int8_t reserved[3];
} p2p_status_info_stru;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| operation_channel | int32_t | GO/GC 连接之后工作信道的中心频点，在 wpa_state 为 CONNECTED 时有效 |
| mode | uint8_t | P2P 模式，对应 [p2p_mode_enum](#p2p_mode_enum) |
| wpa_state | uint8_t | P2P 关联状态，对应 [p2p_conn_state_enum](#p2p_conn_state_enum) |
| group_ssid | int8_t[WPS_DEV_NAME_LEN] | Group SSID，在 wpa_state 为 CONNECTED 且 P2P WPS 关联成功时有效 |
| group_bssid | uint8_t[WIFI_MAC_LEN] | Group BSSID（即 GO BSSID），在 wpa_state 为 CONNECTED 且 P2P WPS 关联成功时有效 |
| reserved | int8_t[3] | 保留字段 |

### p2p_client_info_stru <a id="p2p_client_info_stru"></a>

```c
typedef struct p2p_client_info_stru {
    uint8_t gc_bssid[WIFI_MAC_LEN];           /*!< 与go相连的client mac地址。 */
    uint8_t gc_device_bssid[WIFI_MAC_LEN];    /*!< 与go相连的client dev地址。 */
    int8_t gc_device_name[WPS_DEV_NAME_LEN];  /*!< client 设备名称。 */
    int8_t reserved[3];
} p2p_client_info_stru;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| gc_bssid | uint8_t[WIFI_MAC_LEN] | 与 GO 相连的 Client MAC 地址 |
| gc_device_bssid | uint8_t[WIFI_MAC_LEN] | 与 GO 相连的 Client 设备地址 |
| gc_device_name | int8_t[WPS_DEV_NAME_LEN] | Client 设备名称 |
| reserved | int8_t[3] | 保留字段 |

### p2p_device_config_stru <a id="p2p_device_config_stru"></a>

```c
typedef struct {
    int8_t dev_name[WPS_DEV_NAME_LEN];      /*!< 设备名称。 */
    uint8_t wps_method;                     /*!< 支持的WPS连接方式，可选项为WpsMethod,仅支持配置0/1/2/3。 */
    int32_t listen_channel;                 /*!< 回复probe response的信道。 */
    int32_t oper_channel;                   /*!< 建议的工作信道：0表示随机信道；非0有效值表示建议的信道。 */
} p2p_device_config_stru;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| dev_name | int8_t[WPS_DEV_NAME_LEN] | 设备名称 |
| wps_method | uint8_t | 支持的 WPS 连接方式，对应 [wps_method_enum](#wps_method_enum)，仅支持配置 0/1/2/3 |
| listen_channel | int32_t | 回复 probe response 的信道 |
| oper_channel | int32_t | 建议的工作信道，0 表示随机信道，非 0 有效值表示建议的信道 |

## Macros

### WPS_DEV_NAME_LEN <a id="WPS_DEV_NAME_LEN"></a>

```c
#define WPS_DEV_NAME_LEN 33
```
