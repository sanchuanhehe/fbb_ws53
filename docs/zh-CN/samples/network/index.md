---
hide:
  - toc
---

# 网络协议

WS53 当前可从 `src/application/samples/wifi/` 构建以下网络协议案例。虽然源码位于 Wi-Fi 目录，文档按照 WS63 的结构独立归类。

| 案例 | 功能说明 | 源码目录 | Kconfig 选项 |
| --- | --- | --- | --- |
| [TCP](tcp/tcp.md) | TCP Client / Server 收发和流量统计 | `wifi/tcp_sample/` | `SUPPORT_TCP_CLIENT_SAMPLE` / `SUPPORT_TCP_SERVER_SAMPLE` |
| [MQTT](mqtt/mqtt.md) | TLS MQTT QoS 1 消息发布 | `wifi/mqtt_sample/` | `SAMPLE_SUPPORT_MQTT` |

建议先使用 [STA 连接](../connectivity/wifi/sta/sta-connect.md)确认关联和 DHCP 正常，再排查服务端、端口、证书和应用协议。
