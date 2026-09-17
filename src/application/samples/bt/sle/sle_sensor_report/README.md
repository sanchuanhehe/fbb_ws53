# SLE AHT20 温湿度上报

## 1. 一句话说明

本示例在 WS53 Server 上通过 I2C0 读取 AHT20 温湿度，并以 SLE Notification 或温度告警 Indication 周期发送给另一块 WS53 Client。

## 2. 适用场景

- 采集真实温湿度并通过 SLE 无线上报。
- 学习 I2C 传感器驱动与 SLE SSAP 数据服务的组合方式。
- 验证 AHT20+BMP280 组合模块的器件识别和基础通信。

## 3. 支持能力

- I2C0 以 100 kHz 读取地址 `0x38` 的 AHT20。
- 校验 AHT20 校准状态、忙状态、CRC 和温度范围。
- 每秒生成一个 11 字节温湿度数据帧。
- 正常温度通过 Notification 上报，超出阈值时通过 Indication 上报。
- 启动时探测 BMP280 地址 `0x76`、`0x77` 并读取芯片 ID。
- AHT20 采集和 SLE 双板传输已通过；BMP280 已在 `0x77` 识别为 `0x58`。

## 4. 不支持/限制

- Server 必须连接 AHT20；传感器不可用时 SLE 仍启动，但不会产生有效上报帧。
- BMP280 当前只读取 `0xD0` 芯片 ID，气压初始化、补偿计算及上报尚未实现。
- 数据帧保留 `light` 字段但没有光照传感器，固定为 `0`，日志显示 `N/A`。
- Server 与 Client 互斥构建；传感器只接在 Server 板。
- 本示例使用 3.3 V，勿向传感器供入 5 V。

## 5. 关键词

### 中文关键词

WS53、星闪、SLE、I2C、AHT20、BMP280、温度、湿度、传感器上报

### English Keywords

WS53, SLE, I2C, AHT20, BMP280, temperature, humidity, sensor report

## 6. 目录结构

```text
sle_sensor_report/
├── CMakeLists.txt
├── Kconfig
├── README.md
├── DESIGN.md
├── sle_sensor_report.c
├── sle_sensor_report_server/
│   └── src/
│       ├── sensor_aht20.c
│       ├── sensor_aht20.h
│       ├── sle_sensor_report_server.c
│       ├── sle_sensor_report_server.h
│       ├── sle_sensor_report_server_adv.c
│       └── sle_sensor_report_server_adv.h
└── sle_sensor_report_client/
    └── src/
        ├── sle_sensor_report_client.c
        └── sle_sensor_report_client.h
```

## 7. 入口文件

- 主入口：`sle_sensor_report.c`
- 初始化入口：`sle_sensor_report_entry()`
- AHT20/BMP280 适配：`sle_sensor_report_server/src/sensor_aht20.c`
- Server 业务：`sle_sensor_report_server/src/sle_sensor_report_server.c`
- Client 业务：`sle_sensor_report_client/src/sle_sensor_report_client.c`
- 配置入口：顶层 SLE Sample `choice` 与本目录 `Kconfig`

## 8. 整体流程

1. Server 配置 MIO21/MIO22 为 I2C0，初始化 100 kHz 总线。
2. 启动时分别探测 BMP280 的 `0x76` 和 `0x77` 地址，并打印芯片 ID 结果。
3. Server 初始化 AHT20，随后以 `sensor_server` 广播。
4. Client 扫描、连接、配对、发现服务并启用数据接收。
5. Server 每秒触发一次 AHT20 测量，检查 CRC 后换算温度与湿度。
6. 正常帧从 `0x5656` 属性通知；温度高于 80.00 ℃，或低于 -10.00 ℃时从 `0x5757` 属性指示。
7. Client 解析 11 字节帧并打印时间戳、温度、湿度和帧类型。

## 9. 核心文件说明

| 文件 | 作用 |
| --- | --- |
| `sle_sensor_report.c` | 创建 Server 周期采集任务，或注册 Client 数据回调。 |
| `sensor_aht20.c` | 初始化 I2C0，驱动 AHT20，并一次性探测 BMP280 ID。 |
| `sle_sensor_report_server.c` | 建立 SSAP 服务，封装并发送传感器数据帧。 |
| `sle_sensor_report_server_adv.c` | 配置 `sensor_server` 广播。 |
| `sle_sensor_report_client.c` | 扫描建链、服务发现并开启数据/告警接收。 |

## 10. 核心函数/类说明

| 函数 | 功能与调用关系 |
| --- | --- |
| `sle_sensor_report_entry()` | 根据 Kconfig 启动 Server 或 Client 任务。 |
| `sensor_aht20_init()` | 初始化 I2C、探测 BMP280，并确认 AHT20 已校准。 |
| `sensor_aht20_read()` | 触发测量、校验 CRC，输出温度 ×100 和整数湿度百分比。 |
| `sle_sensor_report_server_init()` | 初始化传感器、SLE 服务和广播。 |
| `sle_sensor_report_server_process()` | 周期读取硬件，组帧并选择 Notification/Indication。 |
| `sle_sensor_report_client_init()` | 初始化 Client 建链、服务发现和接收回调。 |

## 11. 配置项说明

| 配置项 | 值与说明 |
| --- | --- |
| Server / Client Kconfig | `CONFIG_SAMPLE_SUPPORT_SLE_SENSOR_REPORT_SERVER_SAMPLE` / `..._CLIENT_SAMPLE`。 |
| I2C | I2C0，100 kHz，SCL=MIO21，SDA=MIO22，Pin Mode 3。 |
| AHT20 | 地址 `0x38`，测量 CRC8 多项式 `0x31`。 |
| BMP280 | 探测地址 `0x76`/`0x77`，ID 寄存器 `0xD0`，期望值 `0x58`。 |
| 报告周期 | 1000 ms。 |
| 帧格式 | type(1) + count(1) + timestamp(4) + temperature(2) + humidity(1) + light(2) = 11 字节。 |
| Service / Property UUID | `0x5555`；数据 `0x5656`；告警 `0x5757`。 |

## 12. 使用方法

### 环境准备

将 AHT20+BMP280 模块接到 Server 板：

| 传感器引脚 | WS53 连接 |
| --- | --- |
| VDD/VCC | 3.3 V |
| GND | GND |
| SCL | 排针位置 36，MIO21 / I2C0_SCL |
| SDA | 排针位置 5，MIO22 / I2C0_SDA |

### 编译

```powershell
fbb config set CONFIG_SAMPLE_SUPPORT_SLE_SENSOR_REPORT_SERVER_SAMPLE=y --target ws53_liteos_app
fbb build ws53_liteos_app --clean
fbb flash ws53_liteos_app --port <SERVER_COM> --json-summary

fbb config set CONFIG_SAMPLE_SUPPORT_SLE_SENSOR_REPORT_CLIENT_SAMPLE=y --target ws53_liteos_app
fbb build ws53_liteos_app --clean
fbb flash ws53_liteos_app --port <CLIENT_COM> --json-summary
```

先烧录并连接好 Server，再切换 Client。固件位于 `output/ws53/fwpkg/pack_all_core/ws53_liteos_app/ws53_liteos_app_all_in_one.fwpkg`。

### 运行

两端上电后观察 Server 的传感器识别日志及 Client 的周期上报日志。`0x76` 探测失败而 `0x77` 成功是本次模块的正常现象。

### 运行结果

出现 `aht20 compatible device ready`、`bmp280 detected`，且 Client 持续收到合理温湿度即通过。

## 13. 输入输出示例

### 输入

输入来自 AHT20 实际测量，无需命令行操作。

### 输出

```text
[sensor hw] i2c ready: bus=0, scl=GPIO21, sda=GPIO22, rate=100000
[sensor hw] bmp280 detected: addr=0x77, id=0x58 (pressure disabled)
[sensor hw] aht20 compatible device ready
[sensor server] source=hardware temp=32.10C hum=54% light=N/A
[sensor client] [T=12345ms] temp=32.10C, hum=54%, light=N/A, type=0x01
```

验证结论：AHT20 温湿度读取、SLE 双板上报和 BMP280 芯片识别均已通过；气压读取未实现。
