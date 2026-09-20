---
hide:
  - toc
---

# BLE

> GATT (Generic Attribute Profile) Server、基础入门、数据通信、垂直应用

WS53 不支持 BLE Central（中心设备）/GATT Client（客户端）功能，BLE 示例均以 Peripheral（外设）/GATT Server（服务端）角色运行。验证示例时，请使用手机、PC 调试工具、WS63 或其他支持 BLE Client 功能的设备完成扫描、连接、服务发现和特征操作。BLE 案例通过 Kconfig `choice` 互斥选择，同一固件中只能启用一个 BLE 示例。

## 快速导航

### 基础入门

- [Hello BLE (Bluetooth Low Energy)](./basics/hello-connect.md)
- [Hello Notify](./basics/hello-notify.md)
- [Hello ReadWrite](./basics/hello-readwrite.md)

### 数据通信

- [UART (Universal Asynchronous Receiver/Transmitter) 透传](./data-comm/uart-bridge.md)
- [传感器上报](./data-comm/sensor-report.md)

### 高级功能

- [BLE 高吞吐传输](./high-throughput.md)

### 垂直应用场景

- [Wi-Fi 配网](./verticals/wifi-config.md)
- [HID (Human Interface Device) 按键](./verticals/hid.md)
- [网关传感器节点](./verticals/gateway.md)
