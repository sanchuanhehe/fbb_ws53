---
hide:
  - toc
---

# Wi-Fi

Wi-Fi 案例位于 `src/application/samples/wifi/`。网络案例除构建和烧录外，还需要准备路由器、TCP/MQTT 服务端或 Linux 主控等配套环境。

## 可直接构建的案例

| 案例 | 功能说明 | 源码目录 | 主要配置 |
| --- | --- | --- | --- |
| [STA 连接](sta/sta-connect.md) | 扫描并连接无线接入点，通过 DHCP 获取地址 | `wifi/sta_sample/` | `SAMPLE_SUPPORT_STA_SAMPLE` |
| [SoftAP](softap/softap.md) | 创建无线接入点和 DHCP Server | `wifi/softap_sample/` | `SAMPLE_SUPPORT_SOFTAP_SAMPLE` |
| [Wi-Fi 配网](../ble/verticals/wifi-config.md) | 通过 BLE 获取 AP 列表和 Wi-Fi 配置 | `wifi/ble_wifi_cfg_sample/` | `SAMPLE_SUPPORT_BLE_WIFI_CFG_SAMPLE` |
| [SysChannel](syschannel.md) | WS53 Device 与 Linux Host 间的数据通道 | `wifi/syschannel_dev/`、`syschannel_host/` | `SAMPLE_SUPPORT_SYSCHANNEL_DEV` |

网络地址、端口、SSID、密码和 Broker 信息应根据测试环境配置。先确认 Wi-Fi 链路和 DHCP 正常，再验证 TCP、MQTT 或升级业务。

TCP 和 MQTT 案例归入[网络协议](../../network/index.md)。
