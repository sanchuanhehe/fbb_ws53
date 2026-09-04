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

## 集成与适配专题

| 专题 | 功能说明 | 源码与依赖 |
| --- | --- | --- |
| [HiLink 独立升级](hilink-indie-upgrade.md) | HiLink SDK 函数映射和独立升级适配 | `wifi/hilink_indie_upgrade/`；还需外部 `libhilink` 头文件、库和产品适配，不是当前仓内可独立烧录运行的完整案例 |

## Wi-Fi 功能专题

以下页面按 WS53 公开接口和现有源码说明功能用法。除“复用案例”列所列内容外，当前没有同名的独立 `src/application/samples/wifi/` 工程。

| 专题 | 功能说明 | 可复用案例或实现状态 |
| --- | --- | --- |
| [扫描](scan/scan.md) | 扫描周边 AP 并解析结果 | 复用 `wifi/sta_sample/` 的扫描流程 |
| [省电模式](power-save/power-save.md) | 控制 STA 低功耗模式并验证功耗/时延 | 在 `wifi/sta_sample/` 上集成 |
| [P2P](p2p.md) | P2P 发现、GO/GC 协商与直连 | 公开 API 可用性取决于目标构建特性 |
| [监听模式](monitor.md) | 混杂模式收包与过滤 | 公开 API，需自行集成诊断任务 |
| [中继设计](repeater.md) | STA + SoftAP 组合及网络层边界 | 无独立中继案例，需补充转发/NAT |

网络地址、端口、SSID、密码和 Broker 信息应根据测试环境配置。先确认 Wi-Fi 链路和 DHCP 正常，再验证 TCP、MQTT 或升级业务。

TCP 和 MQTT 案例归入[网络协议](../../network/index.md)。
