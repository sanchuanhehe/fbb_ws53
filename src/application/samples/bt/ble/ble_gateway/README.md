# WS53 BLE Gateway Sensor Node

## 1. 一句话说明

本示例演示 WS53 通过 I2C0 采集 AHT20 温湿度和 BMP280 气压，并以固定 14 字节二进制协议周期发送 BLE Notification。

## 2. 适用场景

- 环境传感器节点与 BLE 网关联调。
- 验证 WS53 I2C0、AHT20/BMP280 驱动和二进制 GATT 协议。
- 作为多节点采集、边缘网关或 MQTT 网关前端的参考节点。

## 3. 支持能力

- I2C0 100 kHz，SDA=MGPIO22、SCL=MGPIO21、`PIN_MODE_3`。
- 自动识别 BMP280 地址 `0x76/0x77`，AHT20 地址为 `0x38`。
- 广播名 `sensor_node`，Service `0x3333`，Data `0x3434`，Notify `0x3435`。
- 上报协议包含版本、节点 ID、序号、0.1℃、0.1%RH 和 Pa。
- Client 可写 6 字节命令，将周期设置为 5～3600 秒。

## 4. 不支持/限制

- WS53 仅实现 Sensor Node Server；网关 Client 由 WS63 工程提供。
- 必须正确接入 AHT20 和 BMP280；传感器不可用时会周期重试但不产生有效报告。
- 默认节点 ID 固定为 1，未提供运行时节点 ID 或持久化配置。
- 使用无流控的自定义二进制协议，应用层需自行处理版本兼容和重复序号。

## 5. 关键词

### 中文关键词

WS53、BLE 网关、传感器节点、AHT20、BMP280、I2C、温湿度、气压、二进制协议

### English Keywords

WS53, BLE gateway, sensor node, AHT20, BMP280, I2C, environmental report, binary protocol

## 6. 目录结构

```text
ble_gateway/
  README.md
  CMakeLists.txt
  ble_gateway.c
  inc/
    ble_gateway_protocol.h
  ble_gateway_server/
    inc/
      ble_gateway_sensor.h
      ble_gateway_server.h
      ble_gateway_server_adv.h
    src/
      ble_gateway_sensor.c
      ble_gateway_server.c
      ble_gateway_server_adv.c
```

## 7. 入口文件

- 主入口：`ble_gateway.c` 中的 `app_run(ble_gateway_entry)`。
- 初始化入口：`ble_gateway_server_init()`。
- 采集循环：`ble_gateway_server_report_loop()`。
- 传感器驱动：`ble_gateway_server/src/ble_gateway_sensor.c`。
- 协议定义：`inc/ble_gateway_protocol.h`。

## 8. 整体流程

1. 创建 Gateway Sensor Node 任务并初始化 BLE GATT Server。
2. 建立 Service、Data、Notify 和 CCCD，随后广播 `sensor_node`。
3. 报告循环初始化 I2C0、AHT20 和 BMP280，失败时按当前周期重试。
4. 读取传感器并组装 14 字节 little-endian 报告。
5. Client 订阅 CCCD 后周期发送 Notification。
6. 收到合法 Set Interval 命令后更新采集周期；断线后重新广播。

## 9. 核心文件说明

| 文件 | 作用 | 关键内容 |
|---|---|---|
| `ble_gateway.c` | 应用入口 | 初始化 Server 并进入报告循环 |
| `inc/ble_gateway_protocol.h` | 空口协议 | 报告/命令编码、范围校验 |
| `ble_gateway_server/src/ble_gateway_server.c` | GATT 与报告业务 | CCCD、周期命令、Notification |
| `ble_gateway_server/src/ble_gateway_sensor.c` | 传感器驱动 | AHT20 CRC、BMP280 补偿算法 |
| `ble_gateway_server/src/ble_gateway_server_adv.c` | 广播 | `sensor_node` 和服务状态 |

## 10. 核心函数/类说明

- `ble_gateway_server_init()`：使能 BLE、注册回调并创建服务。
- `ble_gateway_server_report_loop()`：采样、编码并按周期发送报告。
- `ble_gateway_sensor_init()`：初始化 I2C 和两个传感器。
- `ble_gateway_sensor_read()`：返回温度、湿度和气压定点数据。
- `ble_gateway_encode_report()`：把报告字段编码为 14 字节 little-endian 数据。
- `ble_gateway_write_request_cb()`：处理 CCCD 和 Set Interval 命令。

## 11. 配置项说明

- `CONFIG_SAMPLE_SUPPORT_BLE_GATEWAY_SERVER_SAMPLE=y`：选择本示例。
- `BLE_GATEWAY_DEFAULT_INTERVAL_S=10`：默认上报周期 10 秒。
- `BLE_GATEWAY_MIN_INTERVAL_S=5`、`BLE_GATEWAY_MAX_INTERVAL_S=3600`：允许范围。
- `BLE_GATEWAY_NODE_ID_DEFAULT=1`：默认节点 ID。

报告布局：`version(1) + node_id(1) + sequence(4) + temperature_x10(2) + humidity_x10(2) + pressure_pa(4)`；多字节字段采用 little-endian。

## 12. 使用方法

### 环境准备

- WS53、AHT20、BMP280 和 3.3 V I2C 接线。
- SDA 接 MGPIO22，SCL 接 MGPIO21，并共地。
- WS63 Gateway/Sensor Client 或能解析自定义报告的 BLE 工具。

由于 WS53 工程未提供 BLE Central/GATT Client 相关组件，无法承担 Client 角色，因此本例使用 WS63 作为配套 Client 验证端。Client 工程位于 `fbb_ws63/src/application/samples/bt/ble/ble_gateway/ble_gateway_client`，在 WS63 工程中选择 `CONFIG_SAMPLE_SUPPORT_BLE_GATEWAY_CLIENT_SAMPLE=y` 后编译、烧录。WS53 运行本目录的 Sensor Node Server，WS63 负责扫描、连接、订阅、解析报告及写入采样周期命令。

### 编译

```powershell
fbb build ws53-liteos-app --clean -j1
```

### 运行

```powershell
fbb flash -f src/output/ws53/fwpkg/ws53_liteos_app/ws53_liteos_app_all.fwpkg --chip ws53 -p COM<N> --timeout 240
fbb monitor --port COM<N> --baud 115200 --chip ws53 --reset --timeout 60
```

### 运行结果

传感器正常时会输出 AHT20/BMP280 ready、环境样本和 Notification 日志；接线或器件异常时输出 `sensor init pending` 或 `sensor read failed` 并继续重试。

## 13. 输入输出示例

### 输入

设置 10 秒周期的 6 字节命令：

```text
01 01 0A 00 00 00
```

### 输出

```text
[aht20+bmp280] AHT20 ready, status=0x0c
[aht20+bmp280] BMP280 ready, addr=0x77 id=0x58
[ble environment node] sample ready: node=1 seq=2 temp_x10=301 hum_x10=548 pressure=100984 Pa
```
