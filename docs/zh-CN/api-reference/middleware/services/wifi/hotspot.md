# hotspot

hotspot 提供 WiFi SoftAP (Software Access Point) 功能，支持开启/关闭热点、配置基本与扩展参数、查询已连接 STA (Station) 信息以及断开指定 STA 连接。

**头文件清单**

```c
#include "middleware/services/wifi/wifi_hotspot.h"
#include "middleware/services/wifi/wifi_hotspot_config.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [wifi_softap_enable](#wifi_softap_enable) | 启动 SoftAP |
| [wifi_softap_disable](#wifi_softap_disable) | 关闭 SoftAP |
| [wifi_is_softap_enabled](#wifi_is_softap_enabled) | 获取 SoftAP 使能状态 |
| [wifi_set_softap_config_advance](#wifi_set_softap_config_advance) | 设置 SoftAP 扩展配置 |
| [wifi_get_softap_config](#wifi_get_softap_config) | 获取 SoftAP 基本配置 |
| [wifi_get_softap_config_advance](#wifi_get_softap_config_advance) | 获取 SoftAP 扩展配置 |
| [wifi_softap_get_sta_list](#wifi_softap_get_sta_list) | 获取已连接的 STA 信息列表 |
| [wifi_softap_deauth_sta](#wifi_softap_deauth_sta) | 断开指定 MAC 地址的 STA 连接 |

## Functions

### wifi_softap_enable <a id="wifi_softap_enable"></a>

```c
errcode_t wifi_softap_enable(const softap_config_stru *config)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_hotspot.h"
```

**功能说明**

- 启动 SoftAP 接口，使设备以热点模式工作
- 根据 config 参数中的 SSID、密码、安全类型和信道号配置热点
- 启动前需先通过 wifi_set_softap_config_advance 设置扩展配置

**前置条件**

- 调用时序约束：当前接口必须在 WiFi 初始化完成（wifi_init 成功返回）后调用
- 依赖关系：当前接口依赖 SoftAP 未处于使能状态，且 P2P 未使能
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| config | const [softap_config_stru](#softap_config_stru)* | SoftAP 基本配置参数 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 配置合法且 SoftAP 启动成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 配置无效或 SoftAP 启动失败 |

**参考案例**

- `src/application/samples/wifi/softap_sample/softap_sample.c`

### wifi_softap_disable <a id="wifi_softap_disable"></a>

```c
errcode_t wifi_softap_disable(void)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_hotspot.h"
```

**功能说明**

- 关闭 SoftAP 接口，停止热点模式
- 关闭时自动停止 DHCP 服务器（如果已启动）
- 关闭后清除热点接口名与配置信息

**前置条件**

- 调用时序约束：当前接口必须在 WiFi 初始化完成且 SoftAP 已使能后调用
- 依赖关系：当前接口依赖 SoftAP 处于使能状态

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | SoftAP 正常关闭 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | WiFi 未初始化或 SoftAP 未使能 |

**参考案例**

- `src/application/samples/wifi/softap_sample/softap_sample.c`

### wifi_is_softap_enabled <a id="wifi_is_softap_enabled"></a>

```c
int32_t wifi_is_softap_enabled(void)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_hotspot.h"
```

**功能说明**

- 查询 SoftAP 是否已使能
- 返回值 1 表示已使能，0 表示未使能
- WiFi 未初始化时返回 0

**返回值**

- 返回类型：int32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 1 | SoftAP 已使能 | SoftAP 已成功启动 |
| 0 | SoftAP 未使能 | SoftAP 未启动或 WiFi 未初始化 |

### wifi_set_softap_config_advance <a id="wifi_set_softap_config_advance"></a>

```c
errcode_t wifi_set_softap_config_advance(const softap_config_advance_stru *config)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_hotspot.h"
```

**功能说明**

- 设置 SoftAP 的扩展配置参数，包括信标间隔、DTIM 周期、组播密钥更新时间、SSID 隐藏标志、GI 和协议模式
- 必须在 SoftAP 使能之前调用
- 配置中 protocol_mode 为 0 表示不配置，按芯片最大协议能力设置

**前置条件**

- 调用时序约束：当前接口必须在 WiFi 初始化完成且 SoftAP 未使能时调用
- 依赖关系：当前接口依赖 SoftAP 处于未使能状态

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| config | const [softap_config_advance_stru](#softap_config_advance_stru)* | SoftAP 扩展配置参数 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 配置合法且设置成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 配置无效或 SoftAP 已使能 |

**参考案例**

- `src/application/samples/wifi/softap_sample/softap_sample.c`

### wifi_get_softap_config <a id="wifi_get_softap_config"></a>

```c
errcode_t wifi_get_softap_config(softap_config_stru *result)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_hotspot.h"
```

**功能说明**

- 获取 SoftAP 的基本配置信息
- 返回当前 SoftAP 的 SSID、预共享密钥、安全类型、信道号和 PSK 类型

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| result | [softap_config_stru](#softap_config_stru)* | SoftAP 基本配置输出缓冲区 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| result | softap_config_stru* | SoftAP 基本配置信息，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 获取配置成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 内存拷贝失败 |

**参考案例**

- `src/middleware/utils/at/at_wifi_cmd/at/at_wifi.c`

### wifi_get_softap_config_advance <a id="wifi_get_softap_config_advance"></a>

```c
errcode_t wifi_get_softap_config_advance(softap_config_advance_stru *result)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_hotspot.h"
```

**功能说明**

- 获取 SoftAP 的扩展配置信息
- 返回当前 SoftAP 的信标间隔、DTIM 周期、组播密钥更新时间、SSID 隐藏标志、GI 和协议模式

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| result | [softap_config_advance_stru](#softap_config_advance_stru)* | SoftAP 扩展配置输出缓冲区 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| result | softap_config_advance_stru* | SoftAP 扩展配置信息，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 获取配置成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 内存拷贝失败 |

**参考案例**

- `src/middleware/utils/at/at_wifi_cmd/at/at_wifi.c`

### wifi_softap_get_sta_list <a id="wifi_softap_get_sta_list"></a>

```c
errcode_t wifi_softap_get_sta_list(wifi_sta_info_stru *result, uint32_t *size)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_hotspot.h"
```

**功能说明**

- 获取当前连接到 SoftAP 的所有 STA 信息
- 返回每个 STA 的 MAC 地址、RSSI 和最佳发送速率
- size 参数输入时表示缓冲区可容纳的 STA 数量，输出时为实际 STA 数量

**前置条件**

- 调用时序约束：当前接口必须在 WiFi 初始化完成且 SoftAP 已使能后调用
- 依赖关系：当前接口依赖 SoftAP 处于使能状态

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| result | [wifi_sta_info_stru](#wifi_sta_info_stru)* | STA 信息输出缓冲区 | 不为NULL |
| size | uint32_t* | 输入时为缓冲区可容纳 STA 数量，输出时为实际 STA 数量 | 不为NULL，*size > 0 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| result | wifi_sta_info_stru* | 已连接 STA 的信息列表 |
| size | uint32_t* | 实际连接的 STA 数量 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 成功获取 STA 列表 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | WiFi 未初始化、SoftAP 未使能或参数无效 |

**参考案例**

- `src/middleware/utils/at/at_wifi_cmd/at/at_wifi.c`

### wifi_softap_deauth_sta <a id="wifi_softap_deauth_sta"></a>

```c
errcode_t wifi_softap_deauth_sta(const uint8_t *mac, int32_t mac_len)
```

**头文件清单**

```c
#include "middleware/services/wifi/wifi_hotspot.h"
```

**功能说明**

- 断开指定 MAC 地址的 STA 与 SoftAP 的连接
- 向目标 STA 发送 deauth 报文

**前置条件**

- 调用时序约束：当前接口必须在 WiFi 初始化完成且 SoftAP 已使能后调用
- 依赖关系：当前接口依赖 SoftAP 处于使能状态

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| mac | const uint8_t* | 目标 STA 的 MAC 地址 | 不为NULL，长度为 [WIFI_MAC_LEN](#WIFI_MAC_LEN)(6) |
| mac_len | int32_t | MAC 地址长度 | 6 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 执行成功 | 成功断开指定 STA |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | WiFi 未初始化、SoftAP 未使能、MAC 地址无效或断开失败 |

**参考案例**

- `src/middleware/utils/at/at_wifi_cmd/at/at_wifi.c`

## Enumerations

### wifi_security_enum <a id="wifi_security_enum"></a>

```c
typedef enum wifi_security_enum {
    WIFI_SEC_TYPE_INVALID = -1,
    WIFI_SEC_TYPE_OPEN,
    WIFI_SEC_TYPE_WEP,
    WIFI_SEC_TYPE_WPA2PSK,
    WIFI_SEC_TYPE_WPA2_WPA_PSK_MIX,
    WIFI_SEC_TYPE_WPAPSK,
    WIFI_SEC_TYPE_WPA,
    WIFI_SEC_TYPE_WPA2,
    WIFI_SEC_TYPE_SAE,
    WIFI_SEC_TYPE_WPA3_WPA2_PSK_MIX,
    WIFI_SEC_TYPE_WPA3,
    WIFI_SEC_TYPE_OWE,
    WIFI_SEC_TYPE_WAPI_PSK,
    WIFI_SEC_TYPE_WAPI_CERT,
    WIFI_SEC_TYPE_WPA3_WPA2_MIX,
    WIFI_SEC_TYPE_WEP_OPEN,
    WIFI_SEC_TYPE_UNKNOWN
} wifi_security_enum;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| WIFI_SEC_TYPE_INVALID | -1 | 无效安全类型 |
| WIFI_SEC_TYPE_OPEN | 0 | Open |
| WIFI_SEC_TYPE_WEP | 1 | WEP (Wired Equivalent Privacy) SHARED |
| WIFI_SEC_TYPE_WPA2PSK | 2 | WPA2-Personal |
| WIFI_SEC_TYPE_WPA2_WPA_PSK_MIX | 3 | WPA-Personal 和 WPA2-Personal 混合 |
| WIFI_SEC_TYPE_WPAPSK | 4 | WPA-Personal |
| WIFI_SEC_TYPE_WPA | 5 | WPA-Enterprise |
| WIFI_SEC_TYPE_WPA2 | 6 | WPA2-Enterprise |
| WIFI_SEC_TYPE_SAE | 7 | SAE (Simultaneous Authentication of Equals，WPA3 个人级) |
| WIFI_SEC_TYPE_WPA3_WPA2_PSK_MIX | 8 | WPA2-Personal 和 WPA3-Personal 混合 |
| WIFI_SEC_TYPE_WPA3 | 9 | WPA3-Enterprise |
| WIFI_SEC_TYPE_OWE | 10 | OWE (Opportunistic Wireless Encryption) |
| WIFI_SEC_TYPE_WAPI_PSK | 11 | WAPI 个人级 |
| WIFI_SEC_TYPE_WAPI_CERT | 12 | WAPI 企业级 |
| WIFI_SEC_TYPE_WPA3_WPA2_MIX | 13 | WPA2-Enterprise 和 WPA3-Enterprise 混合 |
| WIFI_SEC_TYPE_WEP_OPEN | 14 | WEP OPEN |
| WIFI_SEC_TYPE_UNKNOWN | 15 | 其它认证类型 |

### protocol_mode_enum <a id="protocol_mode_enum"></a>

```c
typedef enum {
    WIFI_MODE_UNDEFINE,
    WIFI_MODE_11B,
    WIFI_MODE_11B_G,
    WIFI_MODE_11B_G_N,
    WIFI_MODE_11B_G_N_AX,
} protocol_mode_enum;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| WIFI_MODE_UNDEFINE | 0 | 未配置 |
| WIFI_MODE_11B | 1 | 802.11b |
| WIFI_MODE_11B_G | 2 | 802.11b/g |
| WIFI_MODE_11B_G_N | 3 | 802.11b/g/n |
| WIFI_MODE_11B_G_N_AX | 4 | 802.11b/g/n/ax |

## Structures

### softap_config_stru <a id="softap_config_stru"></a>

```c
typedef struct {
    int8_t ssid[WIFI_MAX_SSID_LEN];
    int8_t pre_shared_key[WIFI_MAX_KEY_LEN];
    int8_t reserved[2];
    wifi_security_enum security_type;
    int32_t channel_num;
    int32_t wifi_psk_type;
} softap_config_stru;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| ssid | int8_t[WIFI_MAX_SSID_LEN] | SSID (Service Set Identifier) |
| pre_shared_key | int8_t[WIFI_MAX_KEY_LEN] | 预共享密钥 (PSK) |
| reserved | int8_t[2] | 保留字段 |
| security_type | wifi_security_enum | 安全类型 |
| channel_num | int32_t | 信道号，取值范围 0 ~ 14 |
| wifi_psk_type | int32_t | PSK 类型，0 表示不提前计算 PSK，1 表示提前计算 PSK |

### softap_config_advance_stru <a id="softap_config_advance_stru"></a>

```c
typedef struct {
    uint32_t beacon_interval;
    uint32_t dtim_period;
    uint32_t group_rekey;
    uint32_t hidden_ssid_flag;
    uint32_t gi;
    protocol_mode_enum protocol_mode;
} softap_config_advance_stru;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| beacon_interval | uint32_t | 信标间隔，范围 25ms ~ 1000ms，默认 100ms，0 表示未配置 |
| dtim_period | uint32_t | DTIM 周期，范围 1 ~ 30，默认 2，0 表示未配置 |
| group_rekey | uint32_t | 组播密钥更新时间，范围 30s ~ 86400s，默认 86400s，0 表示未配置 |
| hidden_ssid_flag | uint32_t | SSID 隐藏标志，1 表示不隐藏，2 表示隐藏，0 表示未配置 |
| gi | uint32_t | GI (Guard Interval) 配置，默认 auto_GI，0 表示未配置；配置非 0 有效值时需同时配置有效的协议模式 |
| protocol_mode | protocol_mode_enum | 协议模式，默认按芯片最大协议能力配置，0 表示未配置 |

### wifi_sta_info_stru <a id="wifi_sta_info_stru"></a>

```c
typedef struct {
    uint8_t mac_addr[WIFI_MAC_LEN];
    int8_t rssi;
    int8_t rsv;
    uint32_t best_rate;
} wifi_sta_info_stru;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| mac_addr | uint8_t[WIFI_MAC_LEN] | MAC 地址 |
| rssi | int8_t | 接收信号强度指示 (RSSI) |
| rsv | int8_t | 保留字段 |
| best_rate | uint32_t | 最佳发送速率，单位 kbps |

## Type definitions

### errcode_t <a id="errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

SDK 公共基础类型，本模块对外接口的返回值类型。

## Macros

### WIFI_MAX_SSID_LEN <a id="WIFI_MAX_SSID_LEN"></a> [SDK公共共享宏]

```c
#define WIFI_MAX_SSID_LEN 33 // 32 + \0
```

### WIFI_MAX_KEY_LEN <a id="WIFI_MAX_KEY_LEN"></a> [SDK公共共享宏]

```c
#define WIFI_MAX_KEY_LEN 65 // 64 + \0
```

### WIFI_MAC_LEN <a id="WIFI_MAC_LEN"></a> [SDK公共共享宏]

```c
#define WIFI_MAC_LEN 6
```

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a> [SDK公共共享宏]

```c
#define ERRCODE_SUCC 0UL
```

### ERRCODE_FAIL <a id="ERRCODE_FAIL"></a> [SDK公共共享宏]

```c
#define ERRCODE_FAIL 0xFFFFFFFF
```
