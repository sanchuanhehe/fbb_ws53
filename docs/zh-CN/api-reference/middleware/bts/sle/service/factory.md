# Service Factory

SLE (Star Flash Low Energy) factory manager 提供射频长发、长收、收发关闭与复位等工厂测试能力，并支持注册工厂管理回调函数以异步接收射频收发执行结果。

**模块公共头文件**

```c
#include "include/middleware/services/bts/sle/sle_factory_manager.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [sle_rf_tx_start](#sle_rf_tx_start) | 开启射频长发 |
| [sle_rf_rx_start](#sle_rf_rx_start) | 开启射频长收 |
| [sle_rf_trx_end](#sle_rf_trx_end) | 关闭射频收发 |
| [sle_rf_reset](#sle_rf_reset) | 重置射频收发 |
| [sle_factory_register_callbacks](#sle_factory_register_callbacks) | 注册 SLE factory 管理回调函数 |

## Functions

### sle_rf_tx_start <a id="sle_rf_tx_start"></a>

```c
errcode_t sle_rf_tx_start(sle_rf_tx_start_t* rf_tx_start)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_factory_manager.h"
```

**功能说明**

- 开启射频长发
- 按入参结构体配置的频率、功率、数据长度、信息体类型、物理层、格式、速率、导频比、极化编码、发射间隔等参数启动长发
- 长发启动结果通过已注册的射频长发回调函数异步返回

**前置条件**

- 调用时序约束：当前接口必须在 [sle_factory_register_callbacks](#sle_factory_register_callbacks) 成功注册射频长发回调函数之后调用
- 依赖关系：当前接口依赖 SLE service 已就绪
- 上下文限制：当前接口需在 SLE service 线程上下文调用，禁止阻塞或长时间等待

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| rf_tx_start | [sle_rf_tx_start_t](#struct_sle_rf_tx_start_t)* | 射频长发参数结构体指针 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 长发启动请求执行结果，具体读取结果在 [sle_rf_tx_start_callback](#typedef_sle_rf_tx_start_callback) 中返回 |

### sle_rf_rx_start <a id="sle_rf_rx_start"></a>

```c
errcode_t sle_rf_rx_start(sle_rf_rx_start_t* rf_rx_start)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_factory_manager.h"
```

**功能说明**

- 开启射频长收
- 按入参结构体配置的频率、物理层、格式、导频比、接收间隔等参数启动长收
- 长收启动结果通过已注册的射频长收回调函数异步返回

**前置条件**

- 调用时序约束：当前接口必须在 [sle_factory_register_callbacks](#sle_factory_register_callbacks) 成功注册射频长收回调函数之后调用
- 依赖关系：当前接口依赖 SLE service 已就绪
- 上下文限制：当前接口需在 SLE service 线程上下文调用，禁止阻塞或长时间等待

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| rf_rx_start | [sle_rf_rx_start_t](#struct_sle_rf_rx_start_t)* | 射频长收参数结构体指针 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 长收启动请求执行结果，具体读取结果在 [sle_rf_rx_start_callback](#typedef_sle_rf_rx_start_callback) 中返回 |

### sle_rf_trx_end <a id="sle_rf_trx_end"></a>

```c
errcode_t sle_rf_trx_end(void)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_factory_manager.h"
```

**功能说明**

- 关闭射频收发
- 停止当前正在进行的射频长发与长收
- 收发关闭结果通过已注册的射频收发结束回调函数异步返回

**前置条件**

- 调用时序约束：当前接口必须在 [sle_factory_register_callbacks](#sle_factory_register_callbacks) 成功注册射频收发结束回调函数之后调用
- 依赖关系：当前接口依赖 SLE service 已就绪
- 上下文限制：当前接口需在 SLE service 线程上下文调用，禁止阻塞或长时间等待

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 收发关闭请求执行结果，具体读取结果在 [sle_rf_trx_end_callback](#typedef_sle_rf_trx_end_callback) 中返回 |

### sle_rf_reset <a id="sle_rf_reset"></a>

```c
errcode_t sle_rf_reset(void)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_factory_manager.h"
```

**功能说明**

- 重置射频收发
- 复位当前射频长发与长收状态
- 复位结果通过已注册的射频收发复位回调函数异步返回

**前置条件**

- 调用时序约束：当前接口必须在 [sle_factory_register_callbacks](#sle_factory_register_callbacks) 成功注册射频收发复位回调函数之后调用
- 依赖关系：当前接口依赖 SLE service 已就绪
- 上下文限制：当前接口需在 SLE service 线程上下文调用，禁止阻塞或长时间等待

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 复位请求执行结果，具体读取结果在 [sle_rf_reset_callback](#typedef_sle_rf_reset_callback) 中返回 |

### sle_factory_register_callbacks <a id="sle_factory_register_callbacks"></a>

```c
errcode_t sle_factory_register_callbacks(sle_factory_callbacks_t *func)
```

**声明头文件**

```c
#include "include/middleware/services/bts/sle/sle_factory_manager.h"
```

**功能说明**

- 注册 SLE factory 管理回调函数
- 注册射频长发、射频长收、射频收发结束、射频收发复位四类事件的回调函数集合
- 后续射频收发相关接口的异步执行结果通过已注册的回调函数返回

**前置条件**

- 调用时序约束：当前接口必须在射频收发相关接口（[sle_rf_tx_start](#sle_rf_tx_start) / [sle_rf_rx_start](#sle_rf_rx_start) / [sle_rf_trx_end](#sle_rf_trx_end) / [sle_rf_reset](#sle_rf_reset)）调用之前完成注册
- 依赖关系：当前接口依赖 SLE service 已就绪
- 上下文限制：回调函数运行于 SLE service 线程，不能阻塞或长时间等待

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func | [sle_factory_callbacks_t](#struct_sle_factory_callbacks_t)* | 回调函数结构体指针，包含射频长发、长收、收发结束、复位四类回调 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0 | 成功 | 回调函数注册成功 |
| Other | 其他错误码，参考[errcode_t](#errcode_t) | 回调函数注册失败 |

## Type definitions

### errcode_t <a id="errcode_t"></a> [SDK公共基础类型]

```c
// 源码原始定义
typedef uint32_t errcode_t;
```

**使用说明**

本模块对外接口的返回值类型，表示接口执行结果错误码。[SDK公共基础类型]

### sle_rf_tx_start_callback <a id="typedef_sle_rf_tx_start_callback"></a>

```c
typedef void (*sle_rf_tx_start_callback)(errcode_t status);
```

**使用说明**

开启射频长发时的回调函数指针类型。

回调说明：
- 调用时机：开启射频长发请求的处理完成后，由 SLE service 调用
- 参数 status：射频长发执行结果错误码，由 SLE service 透传
- 返回值处理：回调无返回值
- 线程上下文：回调运行于 SLE service 线程，不能阻塞或长时间等待
- 内存归属：回调涉及指针由 SLE service 申请与释放，回调中不应释放

### sle_rf_rx_start_callback <a id="typedef_sle_rf_rx_start_callback"></a>

```c
typedef void (*sle_rf_rx_start_callback)(errcode_t status);
```

**使用说明**

开启射频长收时的回调函数指针类型。

回调说明：
- 调用时机：开启射频长收请求的处理完成后，由 SLE service 调用
- 参数 status：射频长收执行结果错误码，由 SLE service 透传
- 返回值处理：回调无返回值
- 线程上下文：回调运行于 SLE service 线程，不能阻塞或长时间等待
- 内存归属：回调涉及指针由 SLE service 申请与释放，回调中不应释放

### sle_rf_trx_end_callback <a id="typedef_sle_rf_trx_end_callback"></a>

```c
typedef void (*sle_rf_trx_end_callback)(sle_rf_trx_end_cmp_evt_t* cmp_evt);
```

**使用说明**

关闭射频收发时的回调函数指针类型。

回调说明：
- 调用时机：关闭射频收发请求的处理完成后，由 SLE service 调用
- 参数 cmp_evt：执行结果返回结构体指针，承载事件完成状态、数据包数、RSSI 等信息，由 SLE service 申请与释放
- 返回值处理：回调无返回值
- 线程上下文：回调运行于 SLE service 线程，不能阻塞或长时间等待
- 内存归属：cmp_evt 指针由 SLE service 申请与释放，回调中不应释放

### sle_rf_reset_callback <a id="typedef_sle_rf_reset_callback"></a>

```c
typedef void (*sle_rf_reset_callback)(errcode_t status);
```

**使用说明**

重置射频收发时的回调函数指针类型。

回调说明：
- 调用时机：重置射频收发请求的处理完成后，由 SLE service 调用
- 参数 status：射频收发复位执行结果错误码，由 SLE service 透传
- 返回值处理：回调无返回值
- 线程上下文：回调运行于 SLE service 线程，不能阻塞或长时间等待
- 内存归属：回调涉及指针由 SLE service 申请与释放，回调中不应释放

## Enumerations

### sle_rf_power_t <a id="enum_sle_rf_power_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    SLE_RF_POWER_LEVEL_0 = 0x00,
    SLE_RF_POWER_LEVEL_1 = 0x01,
    SLE_RF_POWER_LEVEL_2 = 0x02,
    SLE_RF_POWER_LEVEL_3 = 0x03,
    SLE_RF_POWER_LEVEL_4 = 0x04,
    SLE_RF_POWER_LEVEL_5 = 0x05,
} sle_rf_power_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_RF_POWER_LEVEL_0 | 0x00 | 射频功率0等级:-14dbm |
| SLE_RF_POWER_LEVEL_1 | 0x01 | 射频功率1等级:-10dbm |
| SLE_RF_POWER_LEVEL_2 | 0x02 | 射频功率2等级:-6dbm |
| SLE_RF_POWER_LEVEL_3 | 0x03 | 射频功率3等级:-2dbm |
| SLE_RF_POWER_LEVEL_4 | 0x04 | 射频功率4等级:2dbm |
| SLE_RF_POWER_LEVEL_5 | 0x05 | 射频功率5等级:6dbm |

### sle_rf_payload_type_t <a id="enum_sle_rf_payload_type_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    SLE_RF_PATLOAD_TYPE_0 = 0x00,
    SLE_RF_PATLOAD_TYPE_1 = 0x01,
    SLE_RF_PATLOAD_TYPE_2 = 0x02,
    SLE_RF_PATLOAD_TYPE_3 = 0x03,
    SLE_RF_PATLOAD_TYPE_4 = 0x04,
    SLE_RF_PATLOAD_TYPE_5 = 0x05,
    SLE_RF_PATLOAD_TYPE_6 = 0x06,
    SLE_RF_PATLOAD_TYPE_7 = 0x07,
} sle_rf_payload_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_RF_PATLOAD_TYPE_0 | 0x00 | 射频信息体类型:PRBS9 |
| SLE_RF_PATLOAD_TYPE_1 | 0x01 | 射频信息体类型:11110000 |
| SLE_RF_PATLOAD_TYPE_2 | 0x02 | 射频信息体类型:10101010 |
| SLE_RF_PATLOAD_TYPE_3 | 0x03 | 射频信息体类型:PRBS15 |
| SLE_RF_PATLOAD_TYPE_4 | 0x04 | 射频信息体类型:11111111 |
| SLE_RF_PATLOAD_TYPE_5 | 0x05 | 射频信息体类型:00000000 |
| SLE_RF_PATLOAD_TYPE_6 | 0x06 | 射频信息体类型:00001111 |
| SLE_RF_PATLOAD_TYPE_7 | 0x07 | 射频信息体类型:01010101 |

### sle_rf_phy_t <a id="enum_sle_rf_phy_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    SLE_RF_PHY_1M = 0x00,
    SLE_RF_PHY_2M = 0x01,
    SLE_RF_PHY_4M = 0x04,
} sle_rf_phy_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_RF_PHY_1M | 0x00 | 射频物理层1M |
| SLE_RF_PHY_2M | 0x01 | 射频物理层2M |
| SLE_RF_PHY_4M | 0x04 | 射频物理层4M |

### sle_rf_format_t <a id="enum_sle_rf_format_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    SLE_RF_FORMAT_FRAME_TYPE_1 = 0x00,
    SLE_RF_FORMAT_FRAME_TYPE_2 = 0x01,
} sle_rf_format_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_RF_FORMAT_FRAME_TYPE_1 | 0x00 | 射频格式:无线帧类型1 |
| SLE_RF_FORMAT_FRAME_TYPE_2 | 0x01 | 射频格式:无线帧类型2 |

### sle_rf_tx_rate_t <a id="enum_sle_rf_tx_rate_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    SLE_RF_TX_RATE_GFSK = 0x00,
    SLE_RF_TX_RATE_QPSK = 0x02,
    SLE_RF_TX_RATE_8PSK = 0x03,
} sle_rf_tx_rate_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_RF_TX_RATE_GFSK | 0x00 | 射频长发速率:GFSK |
| SLE_RF_TX_RATE_QPSK | 0x02 | 射频长发速率:QPSK |
| SLE_RF_TX_RATE_8PSK | 0x03 | 射频长发速率:8PSK |

### sle_rf_pilot_ratio_t <a id="enum_sle_rf_pilot_ratio_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    SLE_RF_PILOT_RATIO_NO = 0x00,
    SLE_RF_PILOT_RATIO_1_1 = 0x01,
    SLE_RF_PILOT_RATIO_4_1 = 0x02,
    SLE_RF_PILOT_RATIO_16_1 = 0x03,
} sle_rf_pilot_ratio_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_RF_PILOT_RATIO_NO | 0x00 | 射频导频比:No |
| SLE_RF_PILOT_RATIO_1_1 | 0x01 | 射频导频比:1:1 |
| SLE_RF_PILOT_RATIO_4_1 | 0x02 | 射频导频比:4:1 |
| SLE_RF_PILOT_RATIO_16_1 | 0x03 | 射频导频比:16:1 |

### sle_rf_tx_polar_t <a id="enum_sle_rf_tx_polar_t"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum {
    SLE_RF_TX_POLAR_NO = 0x00,
    SLE_RF_TX_POLAR_2_3 = 0x01,
    SLE_RF_TX_POLAR_3_4 = 0x02,
    SLE_RF_TX_POLAR_5_6 = 0x03,
} sle_rf_tx_polar_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| SLE_RF_TX_POLAR_NO | 0x00 | 射频发射极化编码:No |
| SLE_RF_TX_POLAR_2_3 | 0x01 | 射频发射极化编码:2/3 |
| SLE_RF_TX_POLAR_3_4 | 0x02 | 射频发射极化编码:3/4 |
| SLE_RF_TX_POLAR_5_6 | 0x03 | 射频发射极化编码:5/6 |

## Structures

### sle_rf_tx_start_t <a id="struct_sle_rf_tx_start_t"></a>

```c
// 源码原始定义，保留注释
typedef struct {
    uint8_t tx_freq;            /*!< 发送频率,范围:0x00~0x4E,2402+x */
    uint8_t tx_power;           /*!< 发射功率 { sle_rf_power_t } */
    uint16_t test_data_len;     /*!< 发射测试数据长度,取值范围:0x00~0xFF */
    uint8_t pk_payload_type;    /*!< 信息体类型 { sle_rf_payload_type_t } */
    uint8_t tx_phy;             /*!< 射频物理层 { sle_rf_phy_t } */
    uint8_t tx_format;          /*!< 发射格式 { sle_rf_format_t } */
    uint8_t tx_rate;            /*!< 射频长发速率 { sle_rf_tx_rate_t } */
    uint8_t tx_pilot_ratio;     /*!< 射频导频比 { sle_rf_pilot_ratio_t } */
    uint8_t tx_polar_r;         /*!< 射频发射极化编码 { sle_rf_tx_polar_t } */
    uint16_t tx_interval;       /*!< 射频发射间隔,范围:0x0006~0xFFFF, 1个单位长度为125us */
} sle_rf_tx_start_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| tx_freq | uint8_t | 发送频率，取值范围 0x00~0x4E，实际频率为 2402+x |
| tx_power | uint8_t | 发射功率，取值见 [sle_rf_power_t](#enum_sle_rf_power_t) |
| test_data_len | uint16_t | 发射测试数据长度，取值范围 0x00~0xFF |
| pk_payload_type | uint8_t | 信息体类型，取值见 [sle_rf_payload_type_t](#enum_sle_rf_payload_type_t) |
| tx_phy | uint8_t | 射频物理层，取值见 [sle_rf_phy_t](#enum_sle_rf_phy_t) |
| tx_format | uint8_t | 发射格式，取值见 [sle_rf_format_t](#enum_sle_rf_format_t) |
| tx_rate | uint8_t | 射频长发速率，取值见 [sle_rf_tx_rate_t](#enum_sle_rf_tx_rate_t) |
| tx_pilot_ratio | uint8_t | 射频导频比，取值见 [sle_rf_pilot_ratio_t](#enum_sle_rf_pilot_ratio_t) |
| tx_polar_r | uint8_t | 射频发射极化编码，取值见 [sle_rf_tx_polar_t](#enum_sle_rf_tx_polar_t) |
| tx_interval | uint16_t | 射频发射间隔，取值范围 0x0006~0xFFFF，1 个单位长度为 125us |

### sle_rf_rx_start_t <a id="struct_sle_rf_rx_start_t"></a>

```c
// 源码原始定义，保留注释
typedef struct {
    uint8_t rx_freq;            /*!< 发送频率,范围:0x00~0x4E */
    uint8_t rx_phy;             /*!< 射频物理层 { sle_rf_phy_t } */
    uint8_t rx_format;          /*!< 发射格式 { sle_rf_format_t } */
    uint8_t rx_pilot_ratio;     /*!< 射频导频比 { sle_rf_pilot_ratio_t } */
    uint16_t rx_interval;       /*!< 射频接收间隔,范围:0x0000~0xFFFF, 1个单位长度为125us */
} sle_rf_rx_start_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| rx_freq | uint8_t | 接收频率，取值范围 0x00~0x4E |
| rx_phy | uint8_t | 射频物理层，取值见 [sle_rf_phy_t](#enum_sle_rf_phy_t) |
| rx_format | uint8_t | 接收格式，取值见 [sle_rf_format_t](#enum_sle_rf_format_t) |
| rx_pilot_ratio | uint8_t | 射频导频比，取值见 [sle_rf_pilot_ratio_t](#enum_sle_rf_pilot_ratio_t) |
| rx_interval | uint16_t | 射频接收间隔，取值范围 0x0000~0xFFFF，1 个单位长度为 125us |

### sle_rf_trx_end_cmp_evt_t <a id="struct_sle_rf_trx_end_cmp_evt_t"></a>

```c
// 源码原始定义，保留注释
typedef struct {
    uint8_t status;             /*!< 事件完成状态 */
    uint16_t num_packets;       /*!< 数据包数 */
    uint8_t rssi;               /*!< 接收信号强度指示,默认-127 */
} sle_rf_trx_end_cmp_evt_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| status | uint8_t | 事件完成状态 |
| num_packets | uint16_t | 数据包数 |
| rssi | uint8_t | 接收信号强度指示，默认 -127 |

### sle_factory_callbacks_t <a id="struct_sle_factory_callbacks_t"></a>

```c
// 源码原始定义，保留注释
typedef struct {
    sle_rf_tx_start_callback rf_tx_start_cb;                          /*!< 射频长发回调函数。 */
    sle_rf_rx_start_callback rf_rx_start_cb;                          /*!< 射频长收回调函数。 */
    sle_rf_trx_end_callback rf_trx_end_cb;                            /*!< 射频收发结束回调函数。 */
    sle_rf_reset_callback rf_reset_cb;                                /*!< 射频收发复位回调。 */
} sle_factory_callbacks_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| rf_tx_start_cb | [sle_rf_tx_start_callback](#typedef_sle_rf_tx_start_callback) | 射频长发回调函数 |
| rf_rx_start_cb | [sle_rf_rx_start_callback](#typedef_sle_rf_rx_start_callback) | 射频长收回调函数 |
| rf_trx_end_cb | [sle_rf_trx_end_callback](#typedef_sle_rf_trx_end_callback) | 射频收发结束回调函数 |
| rf_reset_cb | [sle_rf_reset_callback](#typedef_sle_rf_reset_callback) | 射频收发复位回调 |

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a> [SDK公共共享宏]

```c
#define ERRCODE_SUCC                                        0UL
```
