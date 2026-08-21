# WS53 BLE Hello Server

本样例从 WS63 最新 `ble_hello_server` 移植到 WS53，用 WS63 官方 `ble_hello_client` 作为 Central 参考端，验证广播、连接、配对、Notify、Characteristic Read/Write 和断线重连。

## 数据模型

| 属性 | UUID | 属性/权限 | 初始值 |
| --- | --- | --- | --- |
| Primary Service | `0x3333` | Primary | - |
| Data Characteristic | `0x3434` | READ、WRITE | `device_status_ok` |
| Hello Characteristic | `0x3435` | NOTIFY | `hello world` |
| Hello CCCD | `0x2902` | READ、WRITE | `00 00` |

广播名称固定为 `ble_hello_server`。Data 缓冲区为 32 字节，只接受 1–31 字节写入。

## WS53 构建和烧录

在 `fbb_ws53` 根目录执行：

```powershell
fbb config --target ws53_liteos_app set CONFIG_SAMPLE_ENABLE=y
fbb config --target ws53_liteos_app set CONFIG_ENABLE_BT_SAMPLE=y
fbb config --target ws53_liteos_app set CONFIG_SAMPLE_SUPPORT_BLE_SAMPLE=y
fbb config --target ws53_liteos_app set CONFIG_SAMPLE_SUPPORT_BLE_HELLO_SERVER_SAMPLE=y
fbb build ws53_liteos_app --clean -j1
fbb flash ws53_liteos_app --port COM9 --json-summary
```

参考端在 `fbb_ws63` 中选择 `CONFIG_SAMPLE_SUPPORT_BLE_HELLO_CLIENT_SAMPLE=y`，构建后烧录 COM5。

## 实板通过判据

WS63 Client：

```text
[ble hello client] pair complete, status=0x0
[ble hello client] MTU changed: 247, status=0x0
[ble hello client] Received: hello world
[ble hello client] read result: device_status_ok
[ble hello client] write cfm: success
```

WS53 Server：

```text
[ble hello server] connected, conn_id=0x0000
[ble hello server] hello CCCD enabled
[ble hello server] notification sent: hello world
[ble hello server] read response sent: value=device_status_ok
[ble hello server] property updated: new_config_value
[ble hello server] write response sent: success
```

2026-08-14 已在 COM9/WS53 Server 与 COM5/WS63 Client 上完成上述闭环。WS53 当前目标关闭 Central role，因此这里仅移植 Server，不包含 WS63 的 Client 源码。
