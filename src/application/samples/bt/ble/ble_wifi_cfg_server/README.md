# WS53 BLE Wi-Fi Configuration Server

## 1. 一句话说明

本示例通过 WS53 BLE GATT 接收 64 字节 Wi-Fi SSID/密码配置，执行 STA 扫描、关联和 DHCP，并经 BLE 返回配网结果。

## 2. 适用场景

- 无屏设备的 BLE 辅助 Wi-Fi 配网。
- 验证 WS53 BLE 与 Wi-Fi STA 协同运行。
- 作为 Android 配网工具或产品配网协议的参考实现。

## 3. 支持能力

- 广播名 `ble_wifi_config`，Service `0xFD5C`。
- Control `0xFD5D` 用于状态 Notification，Information `0xFD5E` 接收配网数据。
- Request/Report `0xFD5F` 支持 AP 列表请求/响应触发。
- 支持 Wi-Fi 扫描、目标 AP 匹配、STA 关联、DHCP 和结果码上报。
- 已支持较大 MTU Client 单次写入完整 64 字节配置。

## 4. 不支持/限制

- 本目录只包含 BLE GATT Server；业务入口和 Wi-Fi 状态机位于 `application/samples/wifi/ble_wifi_cfg_sample`。
- 必须同时启用 BT 侧 `BLE_CFG_SAMPLE` 和 Wi-Fi 侧 `BLE_WIFI_CFG_SAMPLE`，缺一会导致源码或外部符号不完整。
- 配置载荷固定为 `SSID[32] + password[32]`，不包含长度、版本或校验字段。
- 示例会在日志中打印收到的配置十六进制数据；正式产品应关闭敏感信息日志并增加安全认证。

## 5. 关键词

### 中文关键词

WS53、BLE 配网、Wi-Fi STA、SSID、密码、扫描、关联、DHCP、GATT

### English Keywords

WS53, BLE provisioning, Wi-Fi configuration, STA, SSID, password, scan, DHCP, GATT

## 6. 目录结构

```text
ble_wifi_cfg_server/
  README.md
  CMakeLists.txt
  inc/
    ble_wifi_cfg_adv.h
    ble_wifi_cfg_server.h
  src/
    ble_wifi_cfg_adv.c
    ble_wifi_cfg_server.c

../../wifi/ble_wifi_cfg_sample/
  CMakeLists.txt
  ble_wifi_cfg_sample.c
```

## 7. 入口文件

- 应用主入口：`application/samples/wifi/ble_wifi_cfg_sample/ble_wifi_cfg_sample.c` 中的 `app_run(bgle_wifi_cfg_entry)`。
- BLE 初始化入口：`ble_wifi_cfg_server_init()`。
- Wi-Fi 主任务：`ble_wifi_cfg_example_task()`。
- GATT 服务：`src/ble_wifi_cfg_server.c`。
- 广播配置：`src/ble_wifi_cfg_adv.c`。

## 8. 整体流程

1. Wi-Fi Sample 创建配网任务，初始化 BLE Server 并广播 `ble_wifi_config`。
2. 初始化 Wi-Fi STA 并注册扫描、连接事件回调。
3. 手机订阅 `0xFD5D`，向 `0xFD5E` 写入 64 字节 SSID/密码。
4. 任务启动扫描，从结果中匹配目标 SSID 并发起关联。
5. 关联成功后启动 DHCP，轮询获取 IP 地址。
6. 通过 `0xFD5D` 上报 `{type=1, result_code}`。

## 9. 核心文件说明

| 文件 | 作用 | 关键内容 |
|---|---|---|
| `src/ble_wifi_cfg_server.c` | GATT Server | FD5C～FD5F、写回调、状态上报 |
| `src/ble_wifi_cfg_adv.c` | 广播 | 名称、厂商数据、广播参数 |
| `inc/ble_wifi_cfg_server.h` | 公开接口 | 初始化和按 UUID/Handle 上报 |
| `../../wifi/ble_wifi_cfg_sample/ble_wifi_cfg_sample.c` | Wi-Fi 业务 | 配置缓存、扫描、关联、DHCP、结果码 |

## 10. 核心函数/类说明

- `ble_wifi_cfg_server_init()`：使能 BLE、注册回调并创建 FD5C 服务。
- `ble_wifi_cfg_server_receive_write_req_cbk()`：把 FD5E 配置交给 Wi-Fi 业务，处理 FD5F 请求。
- `set_wifi_cfg_info()`：保存 64 字节配置并置位处理标志。
- `bgwc_wifi_connect()`：匹配扫描结果并执行 STA 连接。
- `ble_wifi_cfg_server_send_report_by_uuid()`：通过 FD5D 返回状态。

## 11. 配置项说明

必须同时配置：

- `CONFIG_SAMPLE_ENABLE=y`
- `CONFIG_ENABLE_BT_SAMPLE=y`
- `CONFIG_SAMPLE_SUPPORT_BLE_SAMPLE=y`
- `CONFIG_SAMPLE_SUPPORT_BLE_CFG_SAMPLE=y`
- `CONFIG_ENABLE_WIFI_SAMPLE=y`
- `CONFIG_SAMPLE_SUPPORT_BLE_WIFI_CFG_SAMPLE=y`

GATT 模型：

| UUID | 属性 | 用途 |
|---|---|---|
| `0xFD5C` | Primary Service | BLE 配网服务 |
| `0xFD5D` | Notify、Write No Response | 控制/结果上报 |
| `0xFD5E` | Indicate、Write No Response | SSID/密码配置 |
| `0xFD5F` | Notify、Write No Response | AP 列表请求/响应 |
| `0x2902` | Read、Write | 各上报特征 CCCD |

## 12. 使用方法

### 环境准备

- WS53、2.4 GHz Wi-Fi AP 和 BLE 配网手机/工具。
- SSID 与密码分别编码为 32 字节缓冲，不足部分补零。

### 编译

选择 BT 和 Wi-Fi 两侧配置后执行：

```powershell
fbb build ws53_liteos_app --clean -j1
```

### 运行

```powershell
fbb flash -f src/output/ws53/fwpkg/pack_all_core/ws53_liteos_app/ws53_liteos_app_all_in_one.fwpkg --chip ws53 -p COM<N> --timeout 240
fbb monitor --port COM<N> --baud 115200 --chip ws53 --reset --timeout 90
```

手机连接 `ble_wifi_config`，订阅 FD5D，并向 FD5E 单次写入 64 字节配置。

### 运行结果

成功路径依次出现 BLE init/adv、Wi-Fi scan、STA connect、`STA DHCP Succ.` 和 `result code:0`。失败时结果码区分 SSID 未找到、密码错误、DHCP 失败、Beacon 丢失和其他错误。

## 13. 输入输出示例

### 输入

```text
offset 0..31  : SSID，NUL 补齐到 32 字节
offset 32..63 : password，NUL 补齐到 32 字节
```

### 输出

FD5D 成功状态：

```text
01 00
```

串口日志：

```text
[BGLE_WIFI_DEBUG] Ble Init State:0.
[BGLE_WIFI_DEBUG] Ble Adv State:0.
STA DHCP start.
STA DHCP Succ.
result code:0.
```
