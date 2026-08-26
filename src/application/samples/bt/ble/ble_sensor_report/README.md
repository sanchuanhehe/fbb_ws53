# WS53 BLE Sensor Report Server

## 1. 一句话说明

本示例演示 WS53 采集 AHT20 和 BMP280，并将温度、湿度、气压格式化为可读 ASCII 文本，通过 BLE Notification 周期上报。

## 2. 适用场景

- 快速查看环境数据，无需解析二进制协议。
- 验证 WS53 I2C0 传感器驱动、BLE Notification 和远程周期配置。
- 作为手机、WS63 Collector 或测试自动化的独立传感器样例。

## 3. 支持能力

- I2C0 100 kHz，SDA=MGPIO22、SCL=MGPIO21、`PIN_MODE_3`。
- 支持 AHT20 `0x38` 和 BMP280 `0x76/0x77`。
- 广播名 `sensor_node`，Service `0x3333`，Data `0x3434`，Notify `0x3435`。
- 默认每 1000 ms 上报，支持写入 `interval=<ms>` 动态调整为 200～60000 ms。
- 传感器未接或读取失败时继续运行 BLE 并周期重试。

## 4. 不支持/限制

- WS53 只实现 Server，Collector/Client 需使用 WS63 或手机工具。
- 同时要求 AHT20 与 BMP280 初始化成功后才上报完整样本。
- 报告为文本格式，吞吐和带宽效率低于 `ble_gateway` 的 14 字节二进制格式。
- 使用 Just Works，未提供 MITM 身份认证。

## 5. 关键词

### 中文关键词

WS53、BLE 传感器、AHT20、BMP280、I2C、温湿度、气压、通知、采样周期

### English Keywords

WS53, BLE sensor, AHT20, BMP280, I2C, temperature, humidity, pressure, notification

## 6. 目录结构

```text
ble_sensor_report/
  README.md
  CMakeLists.txt
  ble_sensor_report.c
  ble_sensor_report_server/
    inc/
      aht20_bmp280.h
      ble_sensor_report_server.h
      ble_sensor_report_server_adv.h
    src/
      aht20_bmp280.c
      ble_sensor_report_server.c
      ble_sensor_report_server_adv.c
```

## 7. 入口文件

- 主入口：`ble_sensor_report.c` 中的 `app_run(ble_sensor_report_entry)`。
- 初始化入口：`ble_sensor_report_server_init()`。
- 主业务循环：`ble_sensor_report_server_report_loop()`。
- 传感器驱动：`ble_sensor_report_server/src/aht20_bmp280.c`。
- 构建配置：上级 `../Kconfig` 和本目录 `CMakeLists.txt`。

## 8. 整体流程

1. 创建传感器报告任务并初始化 BLE GATT Server。
2. 创建 Service、Data、Notify 和 CCCD，开始广播 `sensor_node`。
3. 报告循环初始化 I2C0 和传感器；失败时等待当前周期后重试。
4. 读取传感器并生成 `seq/temp/hum/press` ASCII 报告。
5. Client 订阅 CCCD 后发送 Notification。
6. Client 写入 `interval=<ms>` 可修改周期；断线后重新广播。

## 9. 核心文件说明

| 文件 | 作用 | 关键内容 |
|---|---|---|
| `ble_sensor_report.c` | 应用入口 | 任务创建和报告循环启动 |
| `ble_sensor_report_server/src/ble_sensor_report_server.c` | GATT 与采样业务 | Read/Write、CCCD、文本报告 |
| `ble_sensor_report_server/src/aht20_bmp280.c` | I2C 驱动 | 传感器探测、CRC 和补偿计算 |
| `ble_sensor_report_server/src/ble_sensor_report_server_adv.c` | 广播 | 名称、Service UUID、缓存状态 |

## 10. 核心函数/类说明

- `ble_sensor_report_server_init()`：使能 BLE 并创建 GATT Server。
- `ble_sensor_report_server_report_loop()`：周期采样、格式化和发送通知。
- `ble_sensor_report_parse_interval()`：解析并校验 `interval=<ms>`。
- `aht20_bmp280_init()`：初始化 I2C0、AHT20 和 BMP280。
- `aht20_bmp280_read()`：读取补偿后的定点环境数据。

## 11. 配置项说明

- `CONFIG_SAMPLE_SUPPORT_BLE_SENSOR_REPORT_SERVER_SAMPLE=y`：选择本示例。
- 默认周期：1000 ms。
- 最小周期：200 ms；最大周期：60000 ms。
- Data 缓冲区：32 字节；报告缓冲区：80 字节。

GATT 模型：Service `0x3333`；Data `0x3434` Read/Write；Report `0x3435` Notify；CCCD `0x2902`。

## 12. 使用方法

### 环境准备

- WS53、AHT20、BMP280。
- SDA 接 MGPIO22，SCL 接 MGPIO21，使用 3.3 V 并共地。
- WS63 Sensor Client 或手机 BLE 调试工具。

由于 WS53 工程未提供 BLE Central/GATT Client 相关组件，无法承担 Client 角色，因此本例使用 WS63 作为配套 Client 验证端。Client 工程位于 `fbb_ws63/src/application/samples/bt/ble/ble_sensor_report/ble_sensor_report_client`，在 WS63 工程中选择 `CONFIG_SAMPLE_SUPPORT_BLE_SENSOR_REPORT_CLIENT_SAMPLE=y` 后编译、烧录。WS63 Client 负责发现服务、订阅 Notification、校验传感器数据并写入 `interval=<ms>` 周期配置。

### 编译

```powershell
fbb build ws53-liteos-app --clean -j1
```

### 运行

```powershell
fbb flash -f src/output/ws53/fwpkg/ws53_liteos_app/ws53_liteos_app_all.fwpkg --chip ws53 -p COM<N> --timeout 240
fbb monitor --port COM<N> --baud 115200 --chip ws53 --reset --timeout 60
```

连接 `sensor_node`，订阅 `0x3435`；需要修改周期时向 `0x3434` 写入 ASCII 命令。

### 运行结果

正常时周期输出 `sensor sample` 并发送 Notification。未接传感器时输出 `sensor init pending`，BLE Server 仍保持工作。

## 13. 输入输出示例

### 输入

```text
interval=1000
```

### 输出

```text
[ble sensor report server] sensor initialized: I2C0 SDA=GPIO22 SCL=GPIO21
[ble sensor report server] sensor sample: seq=33,temp=20.5,hum=58.8,press=1009.5
[ble sensor report server] report interval updated: 1000 ms
```
