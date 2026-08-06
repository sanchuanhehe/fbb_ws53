# ota

OTA (Over-The-Air) 基于 SLE (Star Flash Low Energy) 通信提供设备固件升级数据的服务端接收与确认能力。本模块对外提供 OTA 服务器初始化、升级数据确认发送以及接收数据回调注册三类接口。

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_ota.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [sle_ota_service_init](#sle_ota_service_init) | 初始化 SLE OTA 服务器 |
| [sle_ota_data_ack](#sle_ota_data_ack) | 服务器发送 OTA 数据确认 |
| [sle_ota_reg_chan_data_report_cbk](#sle_ota_reg_chan_data_report_cbk) | 注册服务端接收 OTA 升级数据的回调 |

## Functions

### sle_ota_service_init <a id="sle_ota_service_init"></a>

```c
errcode_t sle_ota_service_init(uint8_t server_id)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_ota.h"
```

**功能说明**

- 初始化 SLE OTA 服务器端，建立升级数据传输所需的服务端运行环境
- 以入参指定的 server_id 标识本次初始化的 OTA 服务实例
- 返回执行结果，成功返回 ERRCODE_SUCC，失败返回相应错误码

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| server_id | uint8_t | SLE OTA 服务器实例标识 | 0 ~ 255 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 成功 | 服务器初始化成功 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

### sle_ota_data_ack <a id="sle_ota_data_ack"></a>

```c
errcode_t sle_ota_data_ack(uint16_t value_len, uint8_t *value)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_ota.h"
```

**功能说明**

- 服务端向对端发送 OTA 数据确认信息
- 通过入参指定待发送数据的长度与内容
- 返回执行结果，成功返回 ERRCODE_SUCC，失败返回相应错误码

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| value_len | uint16_t | 待发送数据的字节长度 | 0 ~ 65535 |
| value | uint8_t * | 指向待发送数据缓冲区的指针 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x00 | 成功 | 数据确认发送成功 |
| Other | 其他错误码，参考 errcode_t | 执行失败 |

### sle_ota_reg_chan_data_report_cbk <a id="sle_ota_reg_chan_data_report_cbk"></a>

```c
void sle_ota_reg_chan_data_report_cbk(sle_ota_chan_data_report data_report)
```

**头文件清单**

```c
#include "include/middleware/services/bts/sle/sle_ota.h"
```

**功能说明**

- 注册服务端接收 OTA 升级数据的回调函数
- 当服务端接收到 OTA 升级数据时，通过已注册的回调向应用层上报数据
- 回调函数的注册状态由本模块内部维护，应用层通过本接口完成回调设置

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| data_report | [sle_ota_chan_data_report](#sle_ota_chan_data_report) | 服务端接收 OTA 升级数据的回调函数指针 | 不为 NULL |

## Type definitions

### sle_ota_chan_data_report <a id="sle_ota_chan_data_report"></a>

```c
typedef void (*sle_ota_chan_data_report) (const uint8_t *data_ptr,  const uint16_t data_len);
```

**使用说明**

服务端接收 OTA 升级数据时触发的回调函数指针类型，由 `sle_ota_reg_chan_data_report_cbk` 注册；当服务端接收到 OTA 升级数据时，本回调被调用，将接收到的数据及其长度上报给应用层。回调返回值类型为 void，调用方无需处理返回值。

回调说明：

- 调用时机：服务端通过 SLE 通道接收到 OTA 升级数据时由本模块调用
- 参数 `data_ptr`：指向接收到的 OTA 升级数据的指针，数据内容只读
- 参数 `data_len`：接收到的 OTA 升级数据的字节长度
- 返回值处理：回调返回类型为 void，无返回值
