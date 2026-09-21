# fbb_ws53开发指南

## 代码仓介绍

  WS53V100是海思推出的Wi-Fi、BLE和SLE Combo芯片，适用于大小家电、电工照明等物联网智能场景。该fbb_ws53代码包从统一开发平台FBB（Family Big Box，统一开发框架，统一API）构建而来，在该平台上开发的应用很容易被移植到其他星闪解决方案上，有效降低开发者门槛，缩短开发周期，支持开发者快速开发星闪产品。

## 目录介绍

| 目录   | 介绍                                                         |
| ------ | ------------------------------------------------------------ |
| docs   | 存放软件资料手册、用户指南手册，帮助用户快速了解WS53系列 |
| src    | 开发接入SDK源码包，用户基于源码进行二次开发                  |

## 软件资料介绍

| 名称 | 介绍 |
| :--- | :--- |
| [开发者中心](docs/zh-CN/index.md) | WS53 文档总入口和推荐阅读路径。 |
| [快速入门](docs/zh-CN/get-started/index.md) | 选择 CLI 或 VS Code，完成环境准备、Hello World 构建、烧录和运行验证。 |
| [开发指南](docs/zh-CN/guides/index.md) | SDK、连接、网络、外设、安全、系统服务、测试和认证专题。 |
| [参考案例](docs/zh-CN/samples/index.md) | 示例源码入口和历史 SAMPLE 用例资料。 |
| [API 参考](docs/zh-CN/api-reference/index.md) | 驱动、中间件和 OS 抽象层接口。 |
| [硬件资料](docs/zh-CN/hardware/index.md) | 芯片、单板器件选型和射频测试资料。 |
| [常见问题](docs/zh-CN/FAQ/index.md) | 产测等常见问题。 |

## SDK示例

SDK提供了以下Demo供开发参考：

<table  width="990" border="0" cellpadding="0" cellspacing="0" style='border-collapse:collapse;table-layout:fixed;'>
 <tr height="18" style='height:13.50pt;'>
  <td width="140" x:str><strong>一级分类</strong></td>
  <td width="170" x:str><strong>子分类</strong></td>
  <td width="680" colspan="6" align="center" x:str><strong>应用示例</strong></td>
 </tr>
 <tr height="18" style='height:13.50pt;'>
  <td width="140" align="center" rowspan="5" style='height:27.00pt' x:str>
<strong>基础驱动</strong></td>
  <td x:str><strong>GPIO</strong></td>
  <td width="170" x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/peripheral/blinky">blinky（LED闪烁）</a></td>
  <td width="170" x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/peripheral/pinctrl">pinctrl（管脚控制）</a></td>
  <td width="170" x:str>&nbsp;</td>
  <td width="170" x:str>&nbsp;</td>
  <td width="170" x:str>&nbsp;</td>
  <td width="170" x:str>&nbsp;</td>
 </tr>
 <tr height="18" style='height:13.50pt;'>
  <td x:str><strong>I2C</strong></td>
  <td width="170" x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/peripheral/i2c">I2C组件案例</a></td>
  <td width="170" x:str>&nbsp;</td>
  <td width="170" x:str>&nbsp;</td>
  <td width="170" x:str>&nbsp;</td>
  <td ></td>
  <td ></td>
 </tr>
 <tr height="18" style='height:13.50pt;'>
  <td x:str><strong>SPI</strong></td>
  <td x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/peripheral/spi">SPI组件案例</a></td>
  <td x:str>&nbsp;</td>
  <td width="170" x:str>&nbsp;</td>
  <td width="170" x:str>&nbsp;</td>
  <td ></td>
  <td ></td>
 </tr>
 <tr height="18" style='height:13.50pt;'>
  <td x:str><strong>UART</strong></td>
  <td x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/peripheral/uart">UART组件案例</a></td>
  <td x:str>&nbsp;</td>
  <td width="170" x:str>&nbsp;</td>
  <td width="170" x:str>&nbsp;</td>
  <td ></td>
  <td ></td>
 </tr>
 <tr height="18" style='height:13.50pt;'>
  <td x:str><strong>其他驱动</strong></td>
  <td x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/peripheral/adc">ADC</a></td>
  <td x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/peripheral/pwm">PWM</a></td>
  <td x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/peripheral/dma">DMA</a></td>
  <td x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/peripheral/i2s">I2S</a></td>
  <td x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/peripheral/timer">Timer</a></td>
  <td x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/peripheral/watchdog">Watchdog</a></td>
 </tr>
 <tr height="18" style='height:13.50pt;'>
  <td width="140" align="center" rowspan="1" style='height:27.00pt' x:str>
<strong>星闪</strong></td>
  <td x:str><strong>SLE</strong></td>
  <td width="170" x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/bt/sle/sle_speed_client">SLE速度测试（client）</a></td>
  <td width="170" x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/bt/sle/sle_speed_server">SLE速度测试（server）</a></td>
  <td width="170" x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/bt/sle_chba">SLE CHBA</a></td>
  <td width="170" x:str>&nbsp;</td>
  <td width="170" x:str>&nbsp;</td>
  <td width="170" x:str>&nbsp;</td>
 </tr>
 <tr height="18" style='height:13.50pt;'>
  <td width="140" align="center" rowspan="1" style='height:27.00pt' x:str>
<strong>BLE</strong></td>
  <td x:str><strong>BLE</strong></td>
  <td width="170" x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/bt/ble/ble_speed_server">BLE速度测试</a></td>
  <td width="170" x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/bt/ble/ble_wifi_cfg_server">BLE配网</a></td>
  <td width="170" x:str>&nbsp;</td>
  <td width="170" x:str>&nbsp;</td>
  <td width="170" x:str>&nbsp;</td>
  <td width="170" x:str>&nbsp;</td>
 </tr>
 <tr height="18" style='height:13.50pt;'>
  <td width="140" align="center" rowspan="1" style='height:27.00pt' x:str>
<strong>Wi-Fi</strong></td>
  <td x:str><strong>Wi-Fi</strong></td>
  <td width="170" x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/wifi/sta_sample">Wi-Fi STA</a></td>
  <td width="170" x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/wifi/softap_sample">Wi-Fi AP</a></td>
  <td width="170" x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/wifi/tcp_sample">TCP通信</a></td>
  <td width="170" x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/wifi/mqtt_sample">MQTT通信</a></td>
  <td width="170" x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/wifi/syschannel_dev">Syschannel透传</a></td>
  <td width="170" x:str>&nbsp;</td>
 </tr>
</table>

## 参与贡献

- 参考[社区参与贡献指南](https://gitcode.com/HiSpark/docs/blob/master/contribute/%E7%A4%BE%E5%8C%BA%E5%8F%82%E4%B8%8E%E8%B4%A1%E7%8C%AE%E6%8C%87%E5%8D%97.md)
