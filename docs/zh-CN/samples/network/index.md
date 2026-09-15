---
hide:
  - toc
---

# 网络协议

| 案例 | 功能说明 | 源码目录 | Kconfig 选项 |
| --- | --- | --- | --- |
| [TCP](tcp/tcp.md) | TCP Client / Server 收发和流量统计 | `wifi/tcp_sample/` | `SUPPORT_TCP_CLIENT_SAMPLE` / `SUPPORT_TCP_SERVER_SAMPLE` |
| [MQTT](mqtt/mqtt.md) | TLS MQTT QoS 1 消息发布 | `wifi/mqtt_sample/` | `SAMPLE_SUPPORT_MQTT` |

建议先使用 [STA 连接](../connectivity/wifi/sta/sta-connect.md)确认关联和 DHCP 正常，再排查服务端、端口、证书和应用协议。
