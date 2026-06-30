# fbb_ws53开发指南

## 代码仓介绍

  WS53V100是海思推出的Wi-Fi、BLE和SLE Combo芯片，适用于大小家电、电工照明等物联网智能场景。该fbb_ws53代码包从统一开发平台FBB（Family Big Box，统一开发框架，统一API）构建而来，在该平台上开发的应用很容易被移植到其他星闪解决方案上，有效降低开发者门槛，缩短开发周期，支持开发者快速开发星闪产品。

## 目录介绍

| 目录   | 介绍                                                         |
| ------ | ------------------------------------------------------------ |
| docs   | 存放软件资料手册、用户指南手册，帮助用户快速了解WS53系列 |
| src    | 开发接入SDK源码包，用户基于源码进行二次开发                  |

## 软件资料介绍

| 名称                                                         | 介绍                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [SDK 开发指南](docs/zh-CN/software/SDK%20开发指南/SDK%20开发指南.md) | 本文档主要介绍WS53V100的SDK开发相关内容，包括SDK架构、接口实现机制与使用说明。 |
| [软件 开发指南](docs/zh-CN/software/软件%20开发指南/软件%20开发指南.md) | 本文档详细介绍了WS53V100 Wi-Fi、BLE&SLE接口功能以及开发流程。 |
| [设备驱动 开发指南](docs/zh-CN/software/设备驱动%20开发指南/设备驱动%20开发指南.md) | 介绍WS53V100各外设驱动的使用方法和注意事项。 |
| [AT命令 使用指南](docs/zh-CN/software/AT命令%20使用指南/AT命令%20使用指南.md) | AT命令格式说明及使用示例。 |
| [SAMPLE用例 用户指南](docs/zh-CN/software/SAMPLE用例%20用户指南/SAMPLE用例%20用户指南.md) | 介绍WS53V100中SAMPLE测试用例的使用，指导工程人员快速使用SAMPLE测试用例进行外设驱动验证。 |
| [特性开发说明书](docs/zh-CN/software/特性开发说明书/特性开发说明书.md) | 详细描述WS53V100相关特性的应用场景、实现原理及接口说明。 |
| [SDK开发环境搭建 用户指南](docs/zh-CN/software/SDK开发环境搭建%20用户指南/SDK开发环境搭建%20用户指南.md) | 开发环境搭建指南，包括编译工具链安装及SDK配置。 |
| [Boot移植应用 开发指南](docs/zh-CN/software/Boot移植应用%20开发指南/Boot移植应用%20开发指南.md) | Boot启动流程及移植开发指南。 |
| [HTTP 开发指南](docs/zh-CN/software/HTTP%20开发指南/HTTP%20开发指南.md) | HTTP客户端开发流程及接口说明。 |
| [MQTT 开发指南](docs/zh-CN/software/MQTT%20开发指南/MQTT%20开发指南.md) | MQTT协议开发流程及接口说明。 |
| [CoAP 开发指南](docs/zh-CN/software/CoAP%20开发指南/CoAP%20开发指南.md) | CoAP协议开发流程及接口说明。 |
| [CJSON 开发指南](docs/zh-CN/software/CJSON%20开发指南/CJSON%20开发指南.md) | CJSON使用开发流程及接口说明。 |
| [lwIP 开发指南](docs/zh-CN/software/lwIP%20开发指南/lwIP%20开发指南.md) | lwIP协议栈开发流程及接口说明。 |
| [TLS&DTLS 开发指南](docs/zh-CN/software/TLS&DTLS%20开发指南/TLS&DTLS%20开发指南.md) | TLS/DTLS安全传输开发流程及接口说明。 |
| [FOTA 开发指南](docs/zh-CN/software/FOTA%20开发指南/FOTA%20开发指南.md) | 固件升级（FOTA）开发流程及接口说明。 |
| [低功耗 开发指南](docs/zh-CN/software/低功耗%20开发指南/低功耗%20开发指南.md) | 低功耗模式配置及开发说明。 |
| [NV存储 用户指南](docs/zh-CN/software/NV存储%20用户指南/NV存储%20用户指南.md) | NV存储模块使用说明。 |
| [文件系统 使用指南](docs/zh-CN/software/文件系统%20使用指南/文件系统%20使用指南.md) | LFS文件系统使用说明。 |
| [安全模块 使用指南](docs/zh-CN/software/安全模块%20使用指南/安全模块%20使用指南.md) | 安全模块功能及接口说明。 |
| [Syschannel 使用指南](docs/zh-CN/software/Syschannel%20使用指南/Syschannel%20使用指南.md) | Syschannel（SDIO从接口）使用说明。 |
| [单板冒烟 测试指南](docs/zh-CN/software/单板冒烟%20测试指南/单板冒烟%20测试指南.md) | 单板冒烟测试说明。 |
| [第三方软件 移植指南](docs/zh-CN/software/第三方软件%20移植指南/第三方软件%20移植指南.md) | 第三方软件移植说明。 |

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
  <td width="170" x:str><a href=""></a></td>
  <td width="170" x:str><a href=""></a></td>
  <td width="170" x:str><a href=""></a></td>
  <td width="170" x:str><a href=""></a></td>
 </tr>
 <tr height="18" style='height:13.50pt;'>
  <td x:str><strong>I2C</strong></td>
  <td width="170" x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/peripheral/i2c">I2C组件案例</a></td>
  <td width="170" x:str><a href=""></a></td>
  <td width="170" x:str><a href=""></a></td>
  <td width="170" x:str><a href=""></a></td>
  <td ></td>
  <td ></td>
 </tr>
 <tr height="18" style='height:13.50pt;'>
  <td x:str><strong>SPI</strong></td>
  <td x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/peripheral/spi">SPI组件案例</a></td>
  <td x:str><a href=""></a></td>
  <td width="170" x:str><a href=""></a></td>
  <td width="170" x:str><a href=""></a></td>
  <td ></td>
  <td ></td>
 </tr>
 <tr height="18" style='height:13.50pt;'>
  <td x:str><strong>UART</strong></td>
  <td x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/peripheral/uart">UART组件案例</a></td>
  <td x:str><a href=""></a></td>
  <td width="170" x:str><a href=""></a></td>
  <td width="170" x:str><a href=""></a></td>
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
  <td width="170" x:str><a href=""></a></td>
  <td width="170" x:str><a href=""></a></td>
  <td width="170" x:str><a href=""></a></td>
 </tr>
 <tr height="18" style='height:13.50pt;'>
  <td width="140" align="center" rowspan="1" style='height:27.00pt' x:str>
<strong>BLE</strong></td>
  <td x:str><strong>BLE</strong></td>
  <td width="170" x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/bt/ble/ble_speed_server">BLE速度测试</a></td>
  <td width="170" x:str><a href="https://gitcode.com/HiSpark/fbb_ws53/tree/master/src/application/samples/bt/ble/ble_wifi_cfg_server">BLE配网</a></td>
  <td width="170" x:str><a href=""></a></td>
  <td width="170" x:str><a href=""></a></td>
  <td width="170" x:str><a href=""></a></td>
  <td width="170" x:str><a href=""></a></td>
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
  <td width="170" x:str><a href=""></a></td>
 </tr>
</table>

## 参与贡献

- 参考[社区参与贡献指南](https://gitcode.com/HiSpark/docs/blob/master/contribute/%E7%A4%BE%E5%8C%BA%E5%8F%82%E4%B8%8E%E8%B4%A1%E7%8C%AE%E6%8C%87%E5%8D%97.md)
