---
hide:
  - toc
---

# SLE

> 星闪低功耗（SparkLink Low Energy）领域应用开发参考。大多数案例位于 `src/application/samples/bt/sle/`，并分为 Server 和 Client 两个角色，需要两块 WS53 分别构建和烧录；CHBA 案例位于 `src/application/samples/bt/sle_chba/`。

首次接触星闪开发时，建议先阅读[SLE 概述](overview/index.md)，了解发现、连接、SSAP 服务交互和回调驱动模型，再从 Hello SLE 开始验证。

## 快速导航

### 概述

- [概述](./overview/index.md)

### 基础入门

- [Hello SLE (SparkLink Low Energy)](./basics/hello-connect.md)
- [通知推送（Notify）](./basics/hello-notify.md)
- [属性读写（Read/Write）](./basics/hello-readwrite.md)

### 数据通信

- [UART (Universal Asynchronous Receiver/Transmitter) 透传](./data-comm/uart-bridge.md)
- [传感器上报](./data-comm/sensor-report.md)
- [参数配置与持久化](./data-comm/device-config.md)
- [高吞吐传输](./data-comm/high-throughput.md)
- [分片传输](./data-comm/fragmentation.md)

### 连接管理

- [连接参数动态更新](./link-mgmt/conn-param-tuning.md)
- [无线链路自适应（PHY/MCS）](./link-mgmt/phy-mcs-switch.md)
- [RSSI (Received Signal Strength Indicator) 测距](./link-mgmt/rssi-ranging.md)

### 行业方案

- [SLE CHBA](./verticals/chba.md)
