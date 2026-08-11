---
hide:
  - toc
---

# WS53 系列开发指南

<div class="hero-banner" markdown>

<div class="hero-left" markdown>

**Wi-Fi + SLE（SparkLink Low Energy）+ BLE（Bluetooth Low Energy）Combo 芯片开发平台**

</div>

</div>

## 芯片介绍

WS53 是海思推出的低功耗 Wi-Fi、BLE 和 SLE Combo 芯片，适用于智能门锁、智能门铃、电池类摄像头等物联网智能终端领域。SDK 基于 FBB（Family Big Box）统一开发框架构建，提供无线连接、系统服务、外设驱动和安全等开发能力。

### 关键参数

| 类别 | 参数 | WS53 |
|---|---|---|
| Wi-Fi | 协议 | 802.11b/g/n/ax，MAC 支持 802.11d/e/i/k/v/r/w |
| | 频段 / MIMO | 2.4 GHz，1×1 |
| | 频宽 / 速率 | HT40 MCS7 150 Mbps，HE20 MCS9 114.7 Mbps |
| | 模式 | STA、SoftAP、STA + SoftAP，SoftAP 最大支持 4 路 STA 接入 |
| | 安全 | WPA/WPA2/WPA3 Personal、WPS 2.0 |
| | 特性 | 支持 A-MPDU、A-MSDU、QoS、STBC 和 LDPC |
| BLE | 协议 | BLE 5.4 |
| | 频宽 / 速率 | 1 MHz、2 MHz；125 Kbit/s、500 Kbit/s、1 Mbit/s、2 Mbit/s，最大发射功率 14 dBm |
| | 特性 | 多路广播，支持 Class 1 和 Class 2 |
| SLE | 协议 | SLE 1.0 |
| | 频宽 / 速率 | 1 MHz、2 MHz、4 MHz，最高 12 Mbps，最大发射功率 14 dBm |
| | 特性 | 低功耗、Polar 信道编码、SM4 |
| 处理器 | 内核 | 双核高性能 32-bit 微处理器，最大工作频率 120 MHz |
| 存储 | 内置 | SRAM 576 KB + ROM 352 KB + 4 MB Flash + 2 KB eFuse |
| 外设 | 接口 | 1×SPI、1×QSPI、2×I2C、1×I2S、3×UART、1×SDIO 2.0<br/>28×GPIO、7×ADC、8×PWM |
| 时钟 | 晶体 / 低频时钟 | 外部晶体时钟频率 32 MHz，支持外接 32 kHz 时钟 |
| 电源 | 芯片供电 | 3.0 V～3.6 V，典型值 3.3 V |
| IO | 输入输出电平 | 支持 1.8 V/3.3 V |
| 封装 | 规格 | QFN-52，6 mm × 6 mm |
| 温度 | 工作范围 | -40 ℃～+85 ℃ |

更多电气特性、管脚和硬件设计信息，请查阅[硬件资料](hardware/index.md)。

---

## 开发流程

从零开始开发 WS53 应用，可按以下顺序进行：

<nav class="grid cards" markdown>

-   [**1. 环境搭建**](get-started/environment-setup.md)

    ---

    准备 Python、构建工具和 WS53 RISC-V 工具链，完成 SDK 构建环境配置。

-   [**2. 快速开始**](get-started/quick-start.md)

    ---

    构建 `ws53_liteos_app`，检查 ELF 和固件包输出。

-   [**3. 创建应用**](get-started/create-application.md)

    ---

    参考现有 Sample 和组件构建方式创建应用，并通过 Kconfig 接入目标。

-   [**4. 烧录与运行**](get-started/flash-and-run.md)

    ---

    烧录固件、复位开发板并通过串口日志验证运行结果。

-   [**5. 开发指南**](guides/index.md)

    ---

    按专题了解功能配置、开发流程和验证方法。

-   [**6. 参考案例**](samples/index.md)

    ---

    结合仓库中的外设、蓝牙、星闪和 Wi-Fi Sample 继续开发。

</nav>

---

## 文档入口

<nav class="grid cards" markdown>

-   [**整体架构**](overall-architecture/index.md)

    SDK 源码分层、目录结构和构建系统。

-   [**API 参考**](api-reference/index.md)

    驱动、中间件和 OS 抽象层接口说明。

-   [**硬件资料**](hardware/index.md)

    芯片硬件、关键器件选型和射频测试资料。

-   [**常见问题**](FAQ/index.md)

    开发和产测过程中的常见问题与处理建议。

</nav>
