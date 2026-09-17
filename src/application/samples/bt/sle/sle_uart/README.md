# SLE UART 双向透明传输

## 1. 一句话说明

本示例把两块 WS53 的 UART1 通过 SLE 无线链路桥接，实现 UART 数据在 Server 与 Client 之间的双向透明转发。

## 2. 适用场景

- 无线延长 MCU 调试口或设备数据串口。
- 学习 UART 中断接收、消息队列和 SLE 数据发送的组合方式。
- 验证 Server Notification 与 Client Write Request 两条反向数据通道。

## 3. 支持能力

- Server UART RX → SLE Notification → Client UART TX。
- Client UART RX → SLE Write Request → Server UART TX。
- UART RX 回调只入消息队列，任务上下文负责调用 SLE API。
- 默认 UART1、115200 bps、8N1、MIO17 TX、MIO18 RX。
- 断链后自动恢复广播或扫描，并清理待发送队列。
- USB-TTL 双向端到端实测 11/11 字节原样通过。

## 4. 不支持/限制

- 透明层不定义包头、长度、CRC 或重传；长数据可能按 UART 回调节奏拆成多段。
- 未连接时收到的 UART 数据会丢弃；消息队列满时也会丢弃并打印计数。
- 单个队列项和 SLE MTU 默认最大 520 字节，上层协议应自行处理组帧。
- 启用 `CONFIG_UART_SUPPORT_LPM` 时会占用 `PM_USER0_VETO_ID` 阻止深睡，以保证持续接收，功耗会增加。
- 完整实体验证需要 USB-TTL；USB-TTL 的 VCC 不得连接开发板。

## 5. 关键词

### 中文关键词

WS53、星闪、SLE、UART、USB-TTL、透明传输、串口桥、Notification、Write Request

### English Keywords

WS53, SLE, UART, USB-TTL, transparent bridge, notification, write request

## 6. 目录结构

```text
sle_uart/
├── CMakeLists.txt
├── Kconfig
├── README.md
├── DESIGN.md
├── sle_uart.c
├── sle_uart_server/
│   └── src/
│       ├── sle_uart_server.c
│       ├── sle_uart_server.h
│       ├── sle_uart_server_adv.c
│       └── sle_uart_server_adv.h
└── sle_uart_client/
    └── src/
        ├── sle_uart_client.c
        └── sle_uart_client.h
```

## 7. 入口文件

- 主入口：`sle_uart.c`
- 初始化入口：`sle_uart_entry()`
- UART 初始化与转发任务：`sle_uart.c`
- Server 业务：`sle_uart_server/src/sle_uart_server.c`
- Client 业务：`sle_uart_client/src/sle_uart_client.c`
- 配置入口：`Kconfig`

## 8. 整体流程

1. 两端初始化 UART1、RX 缓冲区和消息队列。
2. Server 以 `uart_server` 广播，Client 扫描并建立 SLE 连接。
3. 双方配对、交换 520 字节 MTU 并完成服务发现。
4. Server UART RX 回调把数据写入队列，Server 任务用 Notification 发送，Client 回调写入 UART TX。
5. Client UART RX 回调把数据写入队列，Client 任务用 Write Request 发送，Server 写回调写入 UART TX。
6. 断链时停止转发并重启广播/扫描，重连后继续工作。

## 9. 核心文件说明

| 文件 | 作用 |
| --- | --- |
| `sle_uart.c` | 初始化 UART、创建消息队列、实现两种角色的数据转发任务。 |
| `sle_uart_server.c` | 注册 SSAP 服务、管理连接并发送 Notification。 |
| `sle_uart_server_adv.c` | 配置 `uart_server` 广播。 |
| `sle_uart_client.c` | 扫描建链、服务发现，并提供 Write Request 通道。 |
| `Kconfig` | 配置 UART 总线、引脚、波特率、缓冲区、MTU 和连接间隔。 |

## 10. 核心函数/类说明

| 函数 | 功能与调用关系 |
| --- | --- |
| `sle_uart_entry()` | 根据 Kconfig 创建 Server 或 Client 任务。 |
| `sle_uart_initialize_uart()` | Server 侧初始化 UART1、引脚和低功耗 veto。 |
| `sle_uart_server_rx_handler()` | ISR 上下文接收 UART 数据并写入 Server 消息队列。 |
| `sle_uart_server_send_notification()` | Server 转发任务调用，将队列数据发给 Client。 |
| `sle_uart_client_rx_handler()` | ISR 上下文接收 UART 数据并写入 Client 消息队列。 |
| `sle_uart_client_forward()` | 读取队列并调用 `ssapc_write_req()` 发给 Server。 |
| `sle_uart_client_notification_cb()` | 接收 Server Notification 并写入本地 UART TX。 |

## 11. 配置项说明

| 配置项 | 默认值与说明 |
| --- | --- |
| Server / Client Kconfig | `CONFIG_SAMPLE_SUPPORT_SLE_UART_SERVER_SAMPLE` / `..._CLIENT_SAMPLE`。 |
| `CONFIG_UART_BUS_ID` | `1`。 |
| `CONFIG_UART_TXD_PIN` / `RXD_PIN` | `17` / `18`。 |
| `CONFIG_UART_TXD_PIN_MODE` / `RXD_PIN_MODE` | `2` / `2`。 |
| `CONFIG_SLE_UART_BAUDRATE` | `115200` bps。 |
| `CONFIG_SLE_UART_RX_BUF_SIZE` | 512 字节。 |
| `CONFIG_SLE_UART_MSGQ_LEN` / `ITEM_SIZE` | 16 项 / 520 字节。 |
| `CONFIG_SLE_UART_MTU_SIZE` | 520 字节。 |
| `CONFIG_SLE_UART_CONN_INTERVAL` | `12`，单位 1.25 ms，即 15 ms；范围 6～32。 |

## 12. 使用方法

### 环境准备

每个 UART 端点按交叉方式接 USB-TTL：

| USB-TTL | WS53 |
| --- | --- |
| TXD | MIO18 / UART1 RX |
| RXD | MIO17 / UART1 TX |
| GND | GND |
| VCC | 不连接 |

推荐两块板各接一个 USB-TTL。只有一个 USB-TTL 时，也可把 TXD 接发送源板 MIO18、RXD 接接收目标板 MIO17，分方向验证；两板和 USB-TTL 必须可靠共地。

### 编译

```powershell
fbb config set CONFIG_SAMPLE_SUPPORT_SLE_UART_SERVER_SAMPLE=y --target ws53_liteos_app
fbb build ws53_liteos_app --clean
fbb flash ws53_liteos_app --port <SERVER_COM> --json-summary

fbb config set CONFIG_SAMPLE_SUPPORT_SLE_UART_CLIENT_SAMPLE=y --target ws53_liteos_app
fbb build ws53_liteos_app --clean
fbb flash ws53_liteos_app --port <CLIENT_COM> --json-summary
```

先烧录 Server，再切换 Client。固件位于 `output/ws53/fwpkg/pack_all_core/ws53_liteos_app/ws53_liteos_app_all_in_one.fwpkg`。

### 运行

等待两端均打印 `=== bridge ready ===`。在一端 USB-TTL 串口工具以 115200/8N1 发送短测试串，并在另一端检查原样接收；随后交换方向复测。

### 运行结果

两个方向均收到相同字节数和内容即通过。本次 11 字节短串实测约 58～88 ms，该数值仅作当时环境参考。

## 13. 输入输出示例

### 输入

```text
Server -> Client: S2C_OK_B4Y5
Client -> Server: C2S_OK_F3U4
```

### 输出

```text
[sle uart server] === bridge ready ===
[sle uart client] === bridge ready ===
[sle uart server] send notify 11 bytes: S2C_OK_B4Y5
[sle uart client] recv 11 bytes from server: S2C_OK_B4Y5
[sle uart client] send 11 bytes: C2S_OK_F3U4
[sle uart server] recv 11 bytes from client: C2S_OK_F3U4
```

验证结论：USB-TTL 经 SLE 的两个方向均已完成 11/11 字节端到端验证。
