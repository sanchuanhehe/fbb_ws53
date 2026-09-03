---
hide:
  - toc
---

# 参考案例

## 快速导航

### 无线连接

- [无线连接](connectivity/index.md)
    - [SLE](connectivity/sle/index.md)
    - [BLE](connectivity/ble/index.md)
    - [Wi-Fi](connectivity/wifi/index.md)

### 外设驱动

- [外设驱动](peripherals/index.md)：ADC、DMA、GPIO、I2C、I2S、LPC、PWM、SPI、UART、RTC 等 16 个案例。

### 网络协议

- [网络协议](network/index.md)
    - [TCP](network/tcp/tcp.md)
    - [MQTT](network/mqtt/mqtt.md)

## 使用说明

1. 根据案例页确认源码目录和 Kconfig 选项。
2. 仅启用当前需要验证的案例及对应角色，避免多个案例同时占用相同外设或任务资源。
3. 按[快速开始](../get-started/quick-start.md)完成配置、构建、烧录和串口验证。
