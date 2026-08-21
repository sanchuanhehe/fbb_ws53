# WS53 BLE Hello Server

## 1. 一句话说明

本示例演示 WS53 作为 BLE GATT Server，完成广播、连接、Just Works 配对、Characteristic Read/Write、Notification 和断线后重新广播。

## 2. 适用场景

- 验证 WS53 BLE Peripheral/GATT Server 基本能力。
- 学习自定义 16-bit Service、Characteristic 和 CCCD 的创建方法。
- 作为 WS63 Central、手机 BLE 调试工具的最小联调对象。

## 3. 支持能力

- 广播名称 `ble_hello_server`，Service UUID `0x3333`。
- Data `0x3434` 支持 Read/Write，初始值为 `device_status_ok`。
- Hello `0x3435` 支持 Notification，订阅后发送 `hello world`。
- 支持绑定、配对失败清理、断线后重新广播和广播状态同步。

## 4. 不支持/限制

- WS53 当前仅提供 Server/Peripheral，本目录不包含 BLE Client。
- Data 缓冲区为 32 字节，应用写入有效长度为 1～31 字节。
- 使用 NoInputNoOutput Just Works，未提供 MITM 身份认证。
- 各 BLE Sample 由 Kconfig `choice` 互斥选择，不能同时启用多个 BLE 示例。

## 5. 关键词

### 中文关键词

WS53、BLE、低功耗蓝牙、GATT Server、广播、配对、通知、读写、CCCD

### English Keywords

WS53, BLE, Bluetooth Low Energy, GATT Server, advertising, pairing, notification, characteristic

## 6. 目录结构

```text
ble_hello/
  README.md
  SDD.md
  CMakeLists.txt
  ble_hello.c
  ble_hello_server/
    inc/
      ble_hello_server.h
      ble_hello_server_adv.h
    src/
      ble_hello_server.c
      ble_hello_server_adv.c
```

## 7. 入口文件

- 主入口：`ble_hello.c` 中的 `app_run(ble_hello_entry)`。
- 初始化入口：`ble_hello_server_init()`。
- 主业务逻辑：`ble_hello_server/src/ble_hello_server.c`。
- 广播配置：`ble_hello_server/src/ble_hello_server_adv.c`。
- 构建配置：上级 `../Kconfig` 和本目录 `CMakeLists.txt`。

## 8. 整体流程

1. `ble_hello_entry()` 创建 BLE Hello 任务。
2. 任务调用 `ble_hello_server_init()`，使能 BLE 并注册 GAP/GATTS 回调。
3. 创建 `0x3333` 服务、`0x3434/0x3435` 特征和 `0x2902` CCCD。
4. 服务启动后广播 `ble_hello_server`。
5. Client 连接、配对并写 CCCD 后，Server 发送 `hello world` Notification。
6. Client 可读取或修改 Data 特征；断线后 Server 自动恢复广播。

## 9. 核心文件说明

| 文件 | 作用 | 关键内容 |
|---|---|---|
| `ble_hello.c` | 应用入口和任务创建 | `ble_hello_entry()`、`ble_hello_task()` |
| `ble_hello_server/src/ble_hello_server.c` | GATT 服务及连接生命周期 | Read/Write、CCCD、配对、通知 |
| `ble_hello_server/src/ble_hello_server_adv.c` | 广播参数和载荷 | 名称、Service UUID、缓存状态 |
| `ble_hello_server/inc/ble_hello_server.h` | UUID、长度和公开接口 | `ble_hello_server_init()` |

## 10. 核心函数/类说明

- `ble_hello_server_init()`：使能 BLE、注册回调并创建 GATT 服务；成功返回 `ERRCODE_BT_SUCCESS`。
- `ble_hello_write_request_cb()`：校验 Data/CCCD 写请求，更新缓存并按需返回 ATT Response。
- `ble_hello_read_request_cb()`：返回当前 Data 特征值。
- `ble_hello_server_send_notification()`：在已连接且 CCCD 使能时发送 Notification。
- `ble_hello_conn_state_cb()`：维护连接状态，断线后重新广播。

## 11. 配置项说明

- `CONFIG_SAMPLE_ENABLE=y`：启用 Sample 框架。
- `CONFIG_ENABLE_BT_SAMPLE=y`：启用 BT Sample。
- `CONFIG_SAMPLE_SUPPORT_BLE_SAMPLE=y`：选择 BLE 类别。
- `CONFIG_SAMPLE_SUPPORT_BLE_HELLO_SERVER_SAMPLE=y`：选择本示例。

GATT 数据模型：

| 属性 | UUID | 属性/权限 | 初始值 |
|---|---|---|---|
| Primary Service | `0x3333` | Primary | - |
| Data | `0x3434` | Read、Write | `device_status_ok` |
| Hello | `0x3435` | Notify | `hello world` |
| CCCD | `0x2902` | Read、Write | `00 00` |

## 12. 使用方法

### 环境准备

- WS53 开发板及其调试串口。
- WS63 BLE Client、手机或 PC BLE 调试工具。
- 串口监视参数为 115200 8N1。

### 编译

在 `fbb_ws53` 根目录选择上述 Kconfig 项，然后执行：

```powershell
fbb build ws53-liteos-app --clean -j1
```

### 运行

```powershell
fbb flash -f src/output/ws53/fwpkg/ws53_liteos_app/ws53_liteos_app_all.fwpkg --chip ws53 -p COM<N> --timeout 240
fbb monitor --port COM<N> --baud 115200 --chip ws53 --reset --timeout 40
```

### 运行结果

正常情况下可看到 `advertising started`、`connected`、`hello CCCD enabled`、`notification sent` 和 Read/Write 成功日志。初始化、服务启动或广播失败时会输出对应 `failed` 和错误码。

## 13. 输入输出示例

### 输入

- Client 向 CCCD 写入 `01 00` 开启 Notification。
- Client 读取 `0x3434`，或向其写入 `new_config_value`。

### 输出

```text
[ble hello server] advertising started: ble_hello_server
[ble hello server] connected, conn_id=0x0000
[ble hello server] hello CCCD enabled
[ble hello server] notification sent: hello world
[ble hello server] read response sent: value=device_status_ok
[ble hello server] property updated: new_config_value
```
