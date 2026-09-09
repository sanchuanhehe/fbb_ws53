---
hide:
  - toc
---

# 外设驱动

> WS53 常用外设的应用开发参考。可构建案例位于 `src/application/samples/peripheral/`，通过 Peripheral Sample 的 Kconfig 选项选择并编译。

当前共收录 16 个有 WS53 Sample 源码和构建入口的案例。

首次使用外设时，建议先从 GPIO 或 UART 完成单板验证，再根据外接器件的电平、时钟、引脚复用和通信协议选择对应案例。

## 快速导航

### 引脚与波形输出

- [GPIO（General Purpose Input/Output）输出](./gpio/gpio-output.md)
- [Pinctrl 引脚复用与上下拉](./pinctrl/pinctrl.md)
- [PWM（Pulse Width Modulation）波形输出](./pwm/pwm.md)

### 数据采集与计时

- [ADC（Analog-to-Digital Converter）采样](./adc/adc.md)
- [RTC 软件定时器](./rtc/rtc.md)
- [SysTick 时间戳与延时](./systick/systick.md)
- [TCXO 时间戳与延时](./tcxo/tcxo.md)
- [Timer](./timer-hw/timer-hw.md)

### 数据搬运、总线与存储

- [DMA（Direct Memory Access）内存搬运](./dma/dma.md)
- [I2C（Inter-Integrated Circuit）主从收发](./i2c/i2c.md)
- [I2S（Inter-IC Sound）主从收发](./i2s/i2s.md)
- [SFC（Serial Flash Controller）Flash 读写](./sfc/sfc.md)
- [SPI（Serial Peripheral Interface）主从收发](./spi/spi.md)
- [UART（Universal Asynchronous Receiver/Transmitter）收发](./uart/uart.md)

### 系统监控与低功耗

- [Watchdog 看门狗](./watchdog/watchdog.md)
- [LPC GPIO 唤醒](./lpc/lpc.md)（WS53 当前独有 Sample）
