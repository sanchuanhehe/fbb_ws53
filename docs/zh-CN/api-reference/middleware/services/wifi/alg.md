# Algorithm

ALG (Algorithm) 提供 Wi-Fi 算法配置能力，包括固定速率设置、协商速率查询、TPC（Transmit Power Control）模式配置、RTS（Request To Send）模式配置、CCA（Clear Channel Assessment）门限设置及抗干扰模式配置。

**模块公共头文件**

```c
#include "include/middleware/services/wifi/wifi_alg.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [wifi_set_fixed_tx_rate](#wifi_set_fixed_tx_rate) | 设置TX方向发送报文的速率模式 |
| [wifi_get_negotiated_rate](#wifi_get_negotiated_rate) | 获取用户当前的最优速率 |
| [wifi_set_tpc_mode](#wifi_set_tpc_mode) | 设置TPC模式 |
| [wifi_set_rts_mode](#wifi_set_rts_mode) | 设置RTS模式 |
| [wifi_set_cca_threshold](#wifi_set_cca_threshold) | 设置CCA门限 |
| [wifi_set_intrf_mode](#wifi_set_intrf_mode) | 设置抗干扰模式 |

## Functions

### wifi_set_fixed_tx_rate <a id="wifi_set_fixed_tx_rate"></a>

```c
errcode_t wifi_set_fixed_tx_rate(unsigned char auto_rate, alg_param_stru *alg_param)
```

**声明头文件**

```c
#include "include/middleware/services/wifi/wifi_alg.h"
```

**功能说明**

- 设置TX方向发送报文的速率模式，可选择固定速率或自动速率。

**前置条件**

- Wi-Fi 已初始化并启动。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | -------- | ---- | ------------ |
| auto_rate | unsigned char | 速率模式选择，0表示固定速率，非0表示自动速率 | - |
| alg_param | [alg_param_stru](#alg_param_stru) * | 速率参数结构体指针，包含固定速率值 | 非NULL |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| ------ | ---- | ---- |
| ERRCODE_SUCC | 0 | 成功 |
| ERROR_WIFI_NOT_STARTED | -7 | Wi-Fi未初始化或未启动 |
| ERROR_WIFI_INVALID_ARGS | -1 | 参数无效（alg_param为NULL） |
| ERROR_WIFI_UNKNOWN | -128 | 未知错误（底层设置失败） |

**参考案例**

- `middleware/utils/at/at_wifi_cmd/at/at_wifi.c`

### wifi_get_negotiated_rate <a id="wifi_get_negotiated_rate"></a>

```c
errcode_t wifi_get_negotiated_rate(const uint8_t *mac, int32_t mac_len, uint32_t *tx_best_rate)
```

**声明头文件**

```c
#include "include/middleware/services/wifi/wifi_alg.h"
```

**功能说明**

- 获取指定用户当前协商的最优速率。

**前置条件**

- Wi-Fi 已初始化并启动。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | -------- | ---- | ------------ |
| mac | const uint8_t * | 用户的MAC地址 | 非NULL |
| mac_len | int32_t | MAC地址长度 | - |
| tx_best_rate | uint32_t * | 获取的用户最佳速率输出缓冲区 | 非NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | -------- | -------- |
| tx_best_rate | uint32_t * | 用户当前协商的最优速率值 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| ------ | ---- | ---- |
| ERRCODE_SUCC | 0 | 成功 |
| ERROR_WIFI_NOT_STARTED | -7 | Wi-Fi未初始化或未启动 |
| ERROR_WIFI_INVALID_ARGS | -1 | 参数无效（mac为NULL） |
| ERROR_WIFI_UNKNOWN | -128 | 未知错误（底层查询失败） |

**参考案例**

- `middleware/utils/at/at_wifi_cmd/at/at_wifi.c`

### wifi_set_tpc_mode <a id="wifi_set_tpc_mode"></a>

```c
errcode_t wifi_set_tpc_mode(uint32_t tpc_value)
```

**声明头文件**

```c
#include "include/middleware/services/wifi/wifi_alg.h"
```

**功能说明**

- 设置TPC模式，用于控制发射功率的动态调整策略。

**前置条件**

- Wi-Fi 已初始化并启动。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | -------- | ---- | ------------ |
| tpc_value | uint32_t | TPC模式值：0-关闭动态调整，1-功率提升模式，2-自动调整模式 | 0~2 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| ------ | ---- | ---- |
| ERRCODE_SUCC | 0 | 成功 |
| ERROR_WIFI_NOT_STARTED | -7 | Wi-Fi未初始化或未启动 |
| ERROR_WIFI_UNKNOWN | -128 | 未知错误（底层设置失败） |

**参考案例**

- `middleware/utils/at/at_wifi_cmd/at/at_wifi.c`

### wifi_set_rts_mode <a id="wifi_set_rts_mode"></a>

```c
errcode_t wifi_set_rts_mode(uint8_t mode, uint16_t pkt_length)
```

**声明头文件**

```c
#include "include/middleware/services/wifi/wifi_alg.h"
```

**功能说明**

- 设置RTS模式，控制发送报文时是否使用RTS/CTS握手机制。

**前置条件**

- Wi-Fi 已初始化并启动。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | -------- | ---- | ------------ |
| mode | uint8_t | RTS模式：0-自动模式，1-超过配置报文长度发送RTS未超过不发，2-不发RTS | 0~2 |
| pkt_length | uint16_t | RTS模式为1时配置的RTS报文长度门限（字节） | mode为1时有效 |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| ------ | ---- | ---- |
| ERRCODE_SUCC | 0 | 成功 |
| ERROR_WIFI_NOT_STARTED | -7 | Wi-Fi未初始化或未启动 |
| ERROR_WIFI_UNKNOWN | -128 | 未知错误（底层设置失败） |

**参考案例**

- `middleware/utils/at/at_wifi_cmd/at/at_wifi.c`

### wifi_set_cca_threshold <a id="wifi_set_cca_threshold"></a>

```c
errcode_t wifi_set_cca_threshold(uint8_t mode, int8_t threshold)
```

**声明头文件**

```c
#include "include/middleware/services/wifi/wifi_alg.h"
```

**功能说明**

- 设置CCA门限值，用于信道空闲检测的判定阈值。

**前置条件**

- Wi-Fi 已初始化并启动。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | -------- | ---- | ------------ |
| mode | uint8_t | 带宽模式：0-20M，1-40M | 0~1 |
| threshold | int8_t | CCA门限值 | - |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| ------ | ---- | ---- |
| ERRCODE_SUCC | 0 | 成功 |
| ERROR_WIFI_NOT_STARTED | -7 | Wi-Fi未初始化或未启动 |
| ERROR_WIFI_UNKNOWN | -128 | 未知错误（底层设置失败） |

**参考案例**

- `middleware/utils/at/at_wifi_cmd/at/at_wifi.c`

### wifi_set_intrf_mode <a id="wifi_set_intrf_mode"></a>

```c
errcode_t wifi_set_intrf_mode(const char *ifname, uint8_t enable, uint16_t flag)
```

**声明头文件**

```c
#include "include/middleware/services/wifi/wifi_alg.h"
```

**功能说明**

- 设置抗干扰模式，配置干扰检测与规避策略的使能及措施标志。

**前置条件**

- Wi-Fi 已初始化并启动。
- 宏 `_PRE_WLAN_FEATURE_INTRF_MODE` 已在构建配置中使能。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | -------- | ---- | ------------ |
| ifname | const char * | 设备名 | 非NULL |
| enable | uint8_t | 是否使能抗干扰模式 | 0或1 |
| flag | uint16_t | 抗干扰措施使能bit配置 | - |

**返回值**

| 返回值 | 文字含义 | 触发场景 |
| ------ | ---- | ---- |
| ERRCODE_SUCC | 0 | 成功 |
| ERROR_WIFI_NOT_STARTED | -7 | Wi-Fi未初始化或未启动 |
| ERROR_WIFI_INVALID_ARGS | -1 | 参数无效（ifname为NULL） |
| ERROR_WIFI_UNKNOWN | -128 | 未知错误（底层设置失败） |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| ------ | ------ | ---- | ------ |
| _PRE_WLAN_FEATURE_INTRF_MODE | 特性宏 | 使能抗干扰模式功能 | 由构建目标决定 |

**参考案例**

- `middleware/utils/at/at_wifi_cmd/at/at_wifi.c`

## Structures

### alg_param_stru <a id="alg_param_stru"></a>

```c
typedef struct {
    uint32_t rate_value;    /*!< 固定速率值。 */
} alg_param_stru;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------ | ---- | ---- |
| rate_value | uint32_t | 固定速率值 |
