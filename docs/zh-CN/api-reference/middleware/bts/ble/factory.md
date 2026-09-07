# Factory

Factory 提供 BLE（Bluetooth Low Energy）产测 RF（Radio Frequency）收发测试、单音模式与产线校准能力。该模块支持射频长发/长收的启停与复位、NV（Non-Volatile） 校准，以及 XO（Crystal Oscillator）频偏校准、芯片温度获取、功率校准及其补偿值的 EFUSE（electronic Fuse）读写等产线校准命令。

**模块公共头文件**

```c
#include "include/middleware/services/bts/ble/bts_factory.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [ble_factory_register_callbacks](#ble_factory_register_callbacks) | 注册 BLE factory 管理回调函数 |
| [ble_factory_rf_tx_start](#ble_factory_rf_tx_start) | 开启射频长发 |
| [ble_factory_rf_rx_start](#ble_factory_rf_rx_start) | 开启射频长收 |
| [ble_factory_rf_trx_end](#ble_factory_rf_trx_end) | 关闭射频收发 |
| [ble_factory_rf_reset](#ble_factory_rf_reset) | 重置射频收发 |
| [ble_factory_rf_cali_nv](#ble_factory_rf_cali_nv) | 校准射频 NV |
| [ble_factory_rf_single_tone](#ble_factory_rf_single_tone) | 设置射频单音模式 |
| [ble_factory_vendor_productline_cmd](#ble_factory_vendor_productline_cmd) | 发送产线校准 vendor 命令 |

## Functions

### ble_factory_register_callbacks <a id="ble_factory_register_callbacks"></a>

```c
errcode_t ble_factory_register_callbacks(ble_factory_callbacks_t *func)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_factory.h"
```

**功能说明**

- 注册 BLE factory 管理回调函数集合，用于接收射频长发/长收、收发结束、收发复位、NV 校准、单音模式及产线校准命令等异步执行结果。
- 回调函数集合通过 [ble_factory_callbacks_t](#struct_ble_factory_callbacks_t) 结构体指针传入。
- 注册后由 BLE service 在对应操作完成时调用相应回调。

**前置条件**

- 依赖关系：当前接口依赖 bts_def.h 定义的基础类型已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| func | [ble_factory_callbacks_t](#struct_ble_factory_callbacks_t) * | 指向回调函数集合结构体的指针，注册后由 BLE service 在对应事件发生时回调 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| errcode_t | - | - |

### ble_factory_rf_tx_start <a id="ble_factory_rf_tx_start"></a>

```c
errcode_t ble_factory_rf_tx_start(ble_rf_tx_start_t* param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_factory.h"
```

**功能说明**

- 启动射频长发测试，按入参配置的频率、数据长度、数据包类型与射频物理层执行发射。
- 发射启动结果通过已注册的 [ble_factory_rf_tx_start_callback](#ble_factory_rf_tx_start_callback) 回调返回。
- 本接口仅返回发起结果，实际长发状态以回调上报为准。

**前置条件**

- 调用时序约束：当前接口须在 [ble_factory_register_callbacks](#ble_factory_register_callbacks) 成功注册回调后调用。
- 依赖关系：当前接口依赖 bts_def.h 定义的基础类型已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| param | [ble_rf_tx_start_t](#struct_ble_rf_tx_start_t) * | 指向射频长发参数结构体的指针，包含发送频率、测试数据长度、数据包类型与射频物理层 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| errcode_t | - | - |

### ble_factory_rf_rx_start <a id="ble_factory_rf_rx_start"></a>

```c
errcode_t ble_factory_rf_rx_start(ble_rf_rx_start_t* param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_factory.h"
```

**功能说明**

- 启动射频长收测试，按入参配置的接收频率、射频物理层与调制指数执行接收。
- 接收启动结果通过已注册的 [ble_factory_rf_rx_start_callback](#ble_factory_rf_rx_start_callback) 回调返回。
- 本接口仅返回发起结果，实际长收状态以回调上报为准。

**前置条件**

- 调用时序约束：当前接口须在 [ble_factory_register_callbacks](#ble_factory_register_callbacks) 成功注册回调后调用。
- 依赖关系：当前接口依赖 bts_def.h 定义的基础类型已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| param | [ble_rf_rx_start_t](#struct_ble_rf_rx_start_t) * | 指向射频长收参数结构体的指针，包含接收频率、射频物理层与调制指数 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| errcode_t | - | - |

### ble_factory_rf_trx_end <a id="ble_factory_rf_trx_end"></a>

```c
errcode_t ble_factory_rf_trx_end(void)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_factory.h"
```

**功能说明**

- 关闭射频收发，停止当前长发与长收测试。
- 关闭结果通过已注册的 [ble_factory_rf_trx_end_callback](#ble_factory_rf_trx_end_callback) 回调返回，回调中携带收发期间累计的数据包数。
- 本接口仅返回发起结果，实际关闭状态以回调上报为准。

**前置条件**

- 调用时序约束：当前接口须在 [ble_factory_register_callbacks](#ble_factory_register_callbacks) 成功注册回调后调用。
- 依赖关系：当前接口依赖 bts_def.h 定义的基础类型已就绪。

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| errcode_t | - | - |

### ble_factory_rf_reset <a id="ble_factory_rf_reset"></a>

```c
errcode_t ble_factory_rf_reset(void)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_factory.h"
```

**功能说明**

- 重置射频收发，复位当前射频长发与长收状态。
- 重置结果通过已注册的 [ble_factory_rf_reset_callback](#ble_factory_rf_reset_callback) 回调返回。
- 本接口仅返回发起结果，实际重置状态以回调上报为准。

**前置条件**

- 调用时序约束：当前接口须在 [ble_factory_register_callbacks](#ble_factory_register_callbacks) 成功注册回调后调用。
- 依赖关系：当前接口依赖 bts_def.h 定义的基础类型已就绪。

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| errcode_t | - | - |

### ble_factory_rf_cali_nv <a id="ble_factory_rf_cali_nv"></a>

```c
errcode_t ble_factory_rf_cali_nv(void)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_factory.h"
```

**功能说明**

- 触发射频 NV 校准，对射频相关 NV 参数执行校准。
- 校准结果通过已注册的 [ble_factory_rf_cali_nv_callback](#ble_factory_rf_cali_nv_callback) 回调返回。
- 本接口仅返回发起结果，实际校准状态以回调上报为准。

**前置条件**

- 调用时序约束：当前接口须在 [ble_factory_register_callbacks](#ble_factory_register_callbacks) 成功注册回调后调用。
- 依赖关系：当前接口依赖 bts_def.h 定义的基础类型已就绪。

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| errcode_t | - | - |

### ble_factory_rf_single_tone <a id="ble_factory_rf_single_tone"></a>

```c
errcode_t ble_factory_rf_single_tone(ble_rf_single_tone_t* param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_factory.h"
```

**功能说明**

- 设置或关闭射频单音模式，按入参配置的射频频率与单音模式开关执行。
- 单音模式设置结果通过已注册的 [ble_factory_rf_single_tone_callback](#ble_factory_rf_single_tone_callback) 回调返回。
- 本接口仅返回发起结果，实际单音状态以回调上报为准。

**前置条件**

- 调用时序约束：当前接口须在 [ble_factory_register_callbacks](#ble_factory_register_callbacks) 成功注册回调后调用。
- 依赖关系：当前接口依赖 bts_def.h 定义的基础类型已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| param | [ble_rf_single_tone_t](#struct_ble_rf_single_tone_t) * | 指向射频单音参数结构体的指针，包含射频频率与单音模式开关 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| errcode_t | - | - |

### ble_factory_vendor_productline_cmd <a id="ble_factory_vendor_productline_cmd"></a>

```c
errcode_t ble_factory_vendor_productline_cmd(ble_vendor_productline_cmd_t* param)
```

**声明头文件**

```c
#include "include/middleware/services/bts/ble/bts_factory.h"
```

**功能说明**

- 发送产线校准 vendor 命令，按入参子操作码携带的参数执行频偏校准、温度获取/读写、功率校准及其补偿值的 EFUSE 读写等产线操作。
- 命令执行完成事件通过已注册的 [ble_factory_vendor_pdl_cmd_callback](#ble_factory_vendor_pdl_cmd_callback) 回调返回。
- 本接口仅返回发起结果，实际执行结果以回调上报为准。

**前置条件**

- 调用时序约束：当前接口须在 [ble_factory_register_callbacks](#ble_factory_register_callbacks) 成功注册回调后调用。
- 依赖关系：当前接口依赖 bts_def.h 定义的基础类型已就绪。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| param | [ble_vendor_productline_cmd_t](#struct_ble_vendor_productline_cmd_t) * | 指向产线校准命令结构体的指针，包含子操作码及按子操作码生效的联合体参数 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| errcode_t | - | - |

## Type definitions

### errcode_t <a id="errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块全部对外接口的返回值类型，表示接口执行结果错误码。

### ble_factory_rf_tx_start_callback <a id="ble_factory_rf_tx_start_callback"></a>

```c
typedef void (*ble_factory_rf_tx_start_callback)(errcode_t status);
```

**使用说明**

射频长发启动结果上报回调函数指针类型。

回调说明：

- 调用时机：射频长发启动完成后，由 BLE service 在其线程上下文调用，不应在回调中阻塞或长时间等待。
- 参数 status：长发启动执行结果错误码。
- 返回值处理：回调返回值为 void，BLE service 不检查。

### ble_factory_rf_rx_start_callback <a id="ble_factory_rf_rx_start_callback"></a>

```c
typedef void (*ble_factory_rf_rx_start_callback)(errcode_t status);
```

**使用说明**

射频长收启动结果上报回调函数指针类型。

回调说明：

- 调用时机：射频长收启动完成后，由 BLE service 在其线程上下文调用，不应在回调中阻塞或长时间等待。
- 参数 status：长收启动执行结果错误码。
- 返回值处理：回调返回值为 void，BLE service 不检查。

### ble_factory_rf_trx_end_callback <a id="ble_factory_rf_trx_end_callback"></a>

```c
typedef void (*ble_factory_rf_trx_end_callback)(errcode_t status, uint16_t num_packets);
```

**使用说明**

射频收发结束结果上报回调函数指针类型。

回调说明：

- 调用时机：射频收发关闭完成后，由 BLE service 在其线程上下文调用，不应在回调中阻塞或长时间等待。
- 参数 status：收发关闭执行结果错误码。
- 参数 num_packets：收发期间累计的数据包数。
- 返回值处理：回调返回值为 void，BLE service 不检查。

### ble_factory_rf_reset_callback <a id="ble_factory_rf_reset_callback"></a>

```c
typedef void (*ble_factory_rf_reset_callback)(errcode_t status);
```

**使用说明**

射频收发重置结果上报回调函数指针类型。

回调说明：

- 调用时机：射频收发重置完成后，由 BLE service 在其线程上下文调用，不应在回调中阻塞或长时间等待。
- 参数 status：收发重置执行结果错误码。
- 返回值处理：回调返回值为 void，BLE service 不检查。

### ble_factory_rf_cali_nv_callback <a id="ble_factory_rf_cali_nv_callback"></a>

```c
typedef void (*ble_factory_rf_cali_nv_callback)(errcode_t status);
```

**使用说明**

射频 NV 校准结果上报回调函数指针类型。

回调说明：

- 调用时机：射频 NV 校准完成后，由 BLE service 在其线程上下文调用，不应在回调中阻塞或长时间等待。
- 参数 status：NV 校准执行结果错误码。
- 返回值处理：回调返回值为 void，BLE service 不检查。

### ble_factory_rf_single_tone_callback <a id="ble_factory_rf_single_tone_callback"></a>

```c
typedef void (*ble_factory_rf_single_tone_callback)(errcode_t status);
```

**使用说明**

射频单音模式设置结果上报回调函数指针类型。

回调说明：

- 调用时机：单音模式开启或关闭完成后，由 BLE service 在其线程上下文调用，不应在回调中阻塞或长时间等待。
- 参数 status：单音模式设置执行结果错误码。
- 返回值处理：回调返回值为 void，BLE service 不检查。

### ble_factory_vendor_pdl_cmd_callback <a id="ble_factory_vendor_pdl_cmd_callback"></a>

```c
typedef void (*ble_factory_vendor_pdl_cmd_callback)(ble_hci_vendor_productline_complete_t *evt);
```

**使用说明**

产线校准 vendor 命令完成事件上报回调函数指针类型。

回调说明：

- 调用时机：产线校准 vendor 命令执行完成后，由 BLE service 在其线程上下文调用，不应在回调中阻塞或长时间等待。
- 参数 evt：指向完成事件结构体的指针，携带子操作码及对应读取结果，指针内存由 BLE service 申请与释放，回调中不应释放。
- 返回值处理：回调返回值为 void，BLE service 不检查。

## Enumerations

### ble_rf_phy_t <a id="enum_ble_rf_phy_t"></a>

```c
typedef enum {
    BLE_RF_PHY_1M = 0x01,      /*!< radio frequency physical: 1M */
    BLE_RF_PHY_2M = 0x02,      /*!< radio frequency physical: 2M */
    BLE_RF_PHY_S8 = 0x03,      /*!< radio frequency physical: coded PHY with S=8 data coding */
    BLE_RF_PHY_S2 = 0x04,      /*!< radio frequency physical: coded PHY with S=2 data coding */
} ble_rf_phy_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| BLE_RF_PHY_1M | 0x01 | 射频物理层 1M |
| BLE_RF_PHY_2M | 0x02 | 射频物理层 2M |
| BLE_RF_PHY_S8 | 0x03 | 射频物理层 S=8 数据编码的编码 PHY |
| BLE_RF_PHY_S2 | 0x04 | 射频物理层 S=2 数据编码的编码 PHY |

### ble_rf_payload_type_t <a id="enum_ble_rf_payload_type_t"></a>

```c
typedef enum {
    BLE_RF_PATLOAD_TYPE_0 = 0x00,    /*!< radio frequency payload type:PRBS9 */
    BLE_RF_PATLOAD_TYPE_1 = 0x01,    /*!< radio frequency payload type:11110000 */
    BLE_RF_PATLOAD_TYPE_2 = 0x02,    /*!< radio frequency payload type:10101010 */
    BLE_RF_PATLOAD_TYPE_3 = 0x03,    /*!< radio frequency payload type:PRBS15 */
    BLE_RF_PATLOAD_TYPE_4 = 0x04,    /*!< radio frequency payload type:11111111 */
    BLE_RF_PATLOAD_TYPE_5 = 0x05,    /*!< radio frequency payload type:00000000 */
    BLE_RF_PATLOAD_TYPE_6 = 0x06,    /*!< radio frequency payload type:00001111 */
    BLE_RF_PATLOAD_TYPE_7 = 0x07,    /*!< radio frequency payload type:01010101 */
} ble_rf_payload_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| BLE_RF_PATLOAD_TYPE_0 | 0x00 | 射频信息体类型 PRBS9 |
| BLE_RF_PATLOAD_TYPE_1 | 0x01 | 射频信息体类型 11110000 |
| BLE_RF_PATLOAD_TYPE_2 | 0x02 | 射频信息体类型 10101010 |
| BLE_RF_PATLOAD_TYPE_3 | 0x03 | 射频信息体类型 PRBS15 |
| BLE_RF_PATLOAD_TYPE_4 | 0x04 | 射频信息体类型 11111111 |
| BLE_RF_PATLOAD_TYPE_5 | 0x05 | 射频信息体类型 00000000 |
| BLE_RF_PATLOAD_TYPE_6 | 0x06 | 射频信息体类型 00001111 |
| BLE_RF_PATLOAD_TYPE_7 | 0x07 | 射频信息体类型 01010101 |

### ble_pdl_sub_opcode_t <a id="enum_ble_pdl_sub_opcode_t"></a>

```c
typedef enum {
    BTH_PRODUCTLINE_XO_TRIM = 0x01,                    // 设置频偏校准值，寄存器控
    BTH_PRODUCTLINE_XO_TRIM_RD_VAL = 0x02,             // 读取频偏校准寄存器值
    BTH_PRODUCTLINE_GET_TSENSOR_TEMPERATURE = 0x03,    // 获取芯片温度
    BTH_PRODUCTLINE_EFUSE_WRITE_XO_TRIM = 0x04,        // 将频偏校准值写入EFUSE
    BTH_PRODUCTLINE_EFUSE_READ_XO_TRIM = 0x05,         // 从EFUSE读取频偏校准值
    BTH_PRODUCTLINE_EFUSE_WRITE_TEMPERATURE = 0x06,    // 将产测时的芯片温度写入EFUSE
    BTH_PRODUCTLINE_EFUSE_READ_TEMPERATURE = 0x07,     // 从EFUSE读取产测温度
    BTH_PRODUCTLINE_PWR_CALI_SET_MEASSURED_PWR = 0x08, // 将实测发送功率发送给驱动
    BTH_PRODUCTLINE_PWR_CALI_GET_COMP_RESULT = 0x09,   // 获取功率校准结果
    BTH_BTH_PRODUCTLINE_PWR_CALI_APPLY_COMP = 0x0A,    // 应用功率校准结果
    BTH_PRODUCTLINE_EFUSE_WRITE_PWR_COMP = 0x0B,       // 将功率校准结果写入EFUSE
    BTH_PRODUCTLINE_EFUSE_READ_PWR_COMP = 0x0C,        // 从EFUSE读取功率校准结果
} ble_pdl_sub_opcode_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| BTH_PRODUCTLINE_XO_TRIM | 0x01 | 设置频偏校准值，寄存器控制 |
| BTH_PRODUCTLINE_XO_TRIM_RD_VAL | 0x02 | 读取频偏校准寄存器值 |
| BTH_PRODUCTLINE_GET_TSENSOR_TEMPERATURE | 0x03 | 获取芯片温度 |
| BTH_PRODUCTLINE_EFUSE_WRITE_XO_TRIM | 0x04 | 将频偏校准值写入 EFUSE |
| BTH_PRODUCTLINE_EFUSE_READ_XO_TRIM | 0x05 | 从 EFUSE 读取频偏校准值 |
| BTH_PRODUCTLINE_EFUSE_WRITE_TEMPERATURE | 0x06 | 将产测时的芯片温度写入 EFUSE |
| BTH_PRODUCTLINE_EFUSE_READ_TEMPERATURE | 0x07 | 从 EFUSE 读取产测温度 |
| BTH_PRODUCTLINE_PWR_CALI_SET_MEASSURED_PWR | 0x08 | 将实测发送功率发送给驱动 |
| BTH_PRODUCTLINE_PWR_CALI_GET_COMP_RESULT | 0x09 | 获取功率校准结果 |
| BTH_BTH_PRODUCTLINE_PWR_CALI_APPLY_COMP | 0x0A | 应用功率校准结果 |
| BTH_PRODUCTLINE_EFUSE_WRITE_PWR_COMP | 0x0B | 将功率校准结果写入 EFUSE |
| BTH_PRODUCTLINE_EFUSE_READ_PWR_COMP | 0x0C | 从 EFUSE 读取功率校准结果 |

## Structures

### ble_rf_tx_start_t <a id="struct_ble_rf_tx_start_t"></a>

```c
typedef struct {
    uint8_t tx_freq;            /*!< tx frequency,Scope:0x00~0x27,2402+x*2 */
    uint16_t test_data_len;     /*!< tx test data len,Scope:0x00~0xFB */
    uint8_t payload_type;       /*!< palyload type { ble_rf_payload_type_t } */
    uint8_t tx_phy;             /*!< radio frequency physical { ble_rf_phy_t } */
} ble_rf_tx_start_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| tx_freq | uint8_t | 发送频率，范围 0~0x27，对应载波频率 2402+x*2 MHz |
| test_data_len | uint16_t | 发射测试数据长度，范围 0~0xFB |
| payload_type | uint8_t | 发射测试数据包类型，取值为 [ble_rf_payload_type_t](#enum_ble_rf_payload_type_t) 枚举成员 |
| tx_phy | uint8_t | 射频物理层，取值为 [ble_rf_phy_t](#enum_ble_rf_phy_t) 枚举成员 |

### ble_rf_rx_start_t <a id="struct_ble_rf_rx_start_t"></a>

```c
typedef struct {
    uint8_t rx_freq;            /*!< tx frequency,Scope:0x00~0x27,2402+x*2 */
    uint8_t rx_phy;             /*!< radio frequency physical { ble_rf_phy_t } */
    uint8_t modulation_index;   /*!< modulation index,0:standard,1:stable */
} ble_rf_rx_start_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| rx_freq | uint8_t | 接收频率，范围 0~0x27，对应载波频率 2402+x*2 MHz |
| rx_phy | uint8_t | 射频物理层，取值为 [ble_rf_phy_t](#enum_ble_rf_phy_t) 枚举成员 |
| modulation_index | uint8_t | 调制指数，0：标准；<br>1：稳定。|

### ble_rf_single_tone_t <a id="struct_ble_rf_single_tone_t"></a>

```c
typedef struct {
    uint8_t rf_freq;            /*!< tx frequency,Scope:0x00~0x4E,2402+x*2 */
    uint8_t rf_mode;            /*!< single tone mode,00:start,FF:stop */
} ble_rf_single_tone_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| rf_freq | uint8_t | 射频频率，范围 0~0x4E，对应载波频率 2402+x*2 MHz |
| rf_mode | uint8_t | 单音模式开关，0：开启；<br>0xFF：关闭。|

### pdl_xo_trim_t <a id="struct_pdl_xo_trim_t"></a>

```c
typedef struct {
    uint8_t coarse_val;
    uint8_t fine_val;
} pdl_xo_trim_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| coarse_val | uint8_t | 频偏校准粗调值 |
| fine_val | uint8_t | 频偏校准细调值 |

### pdl_efuse_temp_wr_t <a id="struct_pdl_efuse_temp_wr_t"></a>

```c
typedef struct {
    int16_t temp;
} pdl_efuse_temp_wr_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| temp | int16_t | 待写入 EFUSE 的产测芯片温度 |

### pdl_pwr_cali_set_pwr_t <a id="struct_pdl_pwr_cali_set_pwr_t"></a>

```c
typedef struct {
    int16_t target_pwr;
    int16_t pwr;
} pdl_pwr_cali_set_pwr_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| target_pwr | int16_t | 目标发送功率 |
| pwr | int16_t | 实测发送功率 |

### ble_vendor_productline_cmd_t <a id="struct_ble_vendor_productline_cmd_t"></a>

```c
typedef struct {
    uint8_t sub_opcode; // subcode
    union {
        pdl_xo_trim_t xo_trim;
        pdl_efuse_temp_wr_t efuse_wr_temp;
        pdl_pwr_cali_set_pwr_t pwr_info;
    };
} ble_vendor_productline_cmd_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| sub_opcode | uint8_t | 产线校准命令子操作码，取值为 [ble_pdl_sub_opcode_t](#enum_ble_pdl_sub_opcode_t) 枚举成员 |
| xo_trim | [pdl_xo_trim_t](#struct_pdl_xo_trim_t) | 频偏校准参数，sub_opcode 为 BTH_PRODUCTLINE_XO_TRIM 时生效 |
| efuse_wr_temp | [pdl_efuse_temp_wr_t](#struct_pdl_efuse_temp_wr_t) | 温度写入参数，sub_opcode 为 BTH_PRODUCTLINE_EFUSE_WRITE_TEMPERATURE 时生效 |
| pwr_info | [pdl_pwr_cali_set_pwr_t](#struct_pdl_pwr_cali_set_pwr_t) | 功率校准参数，sub_opcode 为 BTH_PRODUCTLINE_PWR_CALI_SET_MEASSURED_PWR 时生效 |

### ble_pdl_rd_xo_trim_t <a id="struct_ble_pdl_rd_xo_trim_t"></a>

```c
typedef struct {
    uint8_t sel;
    uint8_t coarse_val;
    uint8_t fine_val;
} ble_pdl_rd_xo_trim_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| sel | uint8_t | 频偏校准寄存器选择 |
| coarse_val | uint8_t | 频偏校准粗调值 |
| fine_val | uint8_t | 频偏校准细调值 |

### ble_pdl_get_temp_t <a id="struct_ble_pdl_get_temp_t"></a>

```c
typedef struct {
    int16_t temp;
} ble_pdl_get_temp_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| temp | int16_t | 获取到的芯片温度 |

### ble_pdl_efuse_rd_xo_trim_t <a id="struct_ble_pdl_efuse_rd_xo_trim_t"></a>

```c
typedef struct {
    uint8_t coarse_val;
    uint8_t fine_val;
} ble_pdl_efuse_rd_xo_trim_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| coarse_val | uint8_t | 从 EFUSE 读取的频偏校准粗调值 |
| fine_val | uint8_t | 从 EFUSE 读取的频偏校准细调值 |

### ble_pdl_efuse_rd_tmp_t <a id="struct_ble_pdl_efuse_rd_tmp_t"></a>

```c
typedef struct {
    uint8_t temp_lvl;
} ble_pdl_efuse_rd_tmp_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| temp_lvl | uint8_t | 从 EFUSE 读取的产测温度等级 |

### ble_pdl_pwr_cali_get_result_t <a id="struct_ble_pdl_pwr_cali_get_result_t"></a>

```c
typedef struct {
    int16_t curve_c_offset;
} ble_pdl_pwr_cali_get_result_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| curve_c_offset | int16_t | 功率校准曲线 C 偏移结果 |

### ble_pdl_efuse_rd_pwr_result_t <a id="struct_ble_pdl_efuse_rd_pwr_result_t"></a>

```c
typedef struct {
    int16_t curve_c_offset;
} ble_pdl_efuse_rd_pwr_result_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| curve_c_offset | int16_t | 从 EFUSE 读取的功率校准曲线 C 偏移结果 |

### ble_hci_vendor_productline_complete_t <a id="struct_ble_hci_vendor_productline_complete_t"></a>

```c
typedef struct {
    uint8_t nb;
    uint16_t opcode;
    uint8_t status;
    uint8_t subcode;
    union {
        ble_pdl_rd_xo_trim_t xo_trim_reg_val;
        ble_pdl_get_temp_t temp;
        ble_pdl_efuse_rd_xo_trim_t xo_trim;
        ble_pdl_efuse_rd_tmp_t temp_lvl;
        ble_pdl_pwr_cali_get_result_t pwr_result;
        ble_pdl_efuse_rd_pwr_result_t efuse_pwr_result;
    };
} ble_hci_vendor_productline_complete_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| nb | uint8_t | 完成事件返回参数个数 |
| opcode | uint16_t | 命令操作码 |
| status | uint8_t | 命令执行状态 |
| subcode | uint8_t | 子操作码，取值为 [ble_pdl_sub_opcode_t](#enum_ble_pdl_sub_opcode_t) 枚举成员 |
| xo_trim_reg_val | [ble_pdl_rd_xo_trim_t](#struct_ble_pdl_rd_xo_trim_t) | 频偏校准寄存器读取值，subcode 为 BTH_PRODUCTLINE_XO_TRIM_RD_VAL 时生效 |
| temp | [ble_pdl_get_temp_t](#struct_ble_pdl_get_temp_t) | 芯片温度，subcode 为 BTH_PRODUCTLINE_GET_TSENSOR_TEMPERATURE 时生效 |
| xo_trim | [ble_pdl_efuse_rd_xo_trim_t](#struct_ble_pdl_efuse_rd_xo_trim_t) | EFUSE 频偏校准值，subcode 为 BTH_PRODUCTLINE_EFUSE_READ_XO_TRIM 时生效 |
| temp_lvl | [ble_pdl_efuse_rd_tmp_t](#struct_ble_pdl_efuse_rd_tmp_t) | EFUSE 温度等级，subcode 为 BTH_PRODUCTLINE_EFUSE_READ_TEMPERATURE 时生效 |
| pwr_result | [ble_pdl_pwr_cali_get_result_t](#struct_ble_pdl_pwr_cali_get_result_t) | 功率校准结果，subcode 为 BTH_PRODUCTLINE_PWR_CALI_GET_COMP_RESULT 时生效 |
| efuse_pwr_result | [ble_pdl_efuse_rd_pwr_result_t](#struct_ble_pdl_efuse_rd_pwr_result_t) | EFUSE 功率校准结果，subcode 为 BTH_PRODUCTLINE_EFUSE_READ_PWR_COMP 时生效 |

### ble_factory_callbacks_t <a id="struct_ble_factory_callbacks_t"></a>

```c
typedef struct {
    ble_factory_rf_tx_start_callback ble_rf_tx_start_cb;
    ble_factory_rf_rx_start_callback ble_rf_rx_start_cb;
    ble_factory_rf_trx_end_callback ble_rf_trx_end_cb;
    ble_factory_rf_reset_callback ble_rf_reset_cb;
    ble_factory_rf_cali_nv_callback ble_rf_cali_nv_cb;
    ble_factory_rf_single_tone_callback ble_rf_single_tone_cb;
    ble_factory_vendor_pdl_cmd_callback ble_vendor_pdl_cmd_cb;
} ble_factory_callbacks_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| ble_rf_tx_start_cb | [ble_factory_rf_tx_start_callback](#ble_factory_rf_tx_start_callback) | 射频长发回调函数 |
| ble_rf_rx_start_cb | [ble_factory_rf_rx_start_callback](#ble_factory_rf_rx_start_callback) | 射频长收回调函数 |
| ble_rf_trx_end_cb | [ble_factory_rf_trx_end_callback](#ble_factory_rf_trx_end_callback) | 射频收发结束回调函数 |
| ble_rf_reset_cb | [ble_factory_rf_reset_callback](#ble_factory_rf_reset_callback) | 射频收发复位回调 |
| ble_rf_cali_nv_cb | [ble_factory_rf_cali_nv_callback](#ble_factory_rf_cali_nv_callback) | 校准射频 NV 回调 |
| ble_rf_single_tone_cb | [ble_factory_rf_single_tone_callback](#ble_factory_rf_single_tone_callback) | 设置射频单音模式回调 |
| ble_vendor_pdl_cmd_cb | [ble_factory_vendor_pdl_cmd_callback](#ble_factory_vendor_pdl_cmd_callback) | 产线校准命令回调 |
