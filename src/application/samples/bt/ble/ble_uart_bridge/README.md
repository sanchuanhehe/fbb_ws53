# WS53 BLE UART Bridge Server

## 1. 一句话说明

本示例在 WS53 上实现 UART_H1 与 BLE GATT 的双向透传：UART RX 经 Indication 发给 Central，Central Write 经 UART TX 输出。

## 2. 适用场景

- 把传统 3.3 V TTL 串口设备接入 BLE。
- 验证 WS53 UART_H1、BLE GATT、分片、队列和重连恢复。
- 配合 WS63 BLE UART Bridge Client 进行双板端到端联调。

## 3. 支持能力

- UART_H1：TX=MGPIO12、RX=AGPIO4、`PIN_MODE_2`、115200 8N1、无流控。
- 广播名 `uart1_bridge`，Service `0x4444`，Data `0x4545`，Indication `0x4546`。
- 目标 ATT MTU 247，最大 BLE 载荷 244 字节。
- 双向 640 字节环形存储，有效容量各 639 字节，带溢出计数、失败保留和重试。
- 使用加密权限、Just Works 配对、断线重新广播和动态 MTU 分片。

## 4. 不支持/限制

- WS53 只实现 Server；Client 位于 WS63 工程。
- UART 无 CTS/RTS，持续输入超过 BLE 消费能力会触发有界队列整段丢弃。
- 为保持 UART 连续接收，示例选择 UART LPM 并持有 sleep veto；功耗高于允许深睡的应用。
- 当前固定 BLE 地址可能与其他 Sample 冲突；量产应使用唯一地址或 NV 配置。

## 5. 关键词

### 中文关键词

WS53、BLE UART、串口透传、UART_H1、MGPIO12、AGPIO4、GATT、Indication、队列

### English Keywords

WS53, BLE UART bridge, UART_H1, serial passthrough, GATT, indication, ring buffer, MTU

## 6. 目录结构

```text
ble_uart_bridge/
  README.md
  CMakeLists.txt
  ble_uart_bridge.c
  ble_uart_bridge.h
  ble_uart_bridge_server/
    inc/
      ble_uart_bridge_server.h
      ble_uart_bridge_server_adv.h
    src/
      ble_uart_bridge_server.c
      ble_uart_bridge_server_adv.c
```

## 7. 入口文件

- 主入口：`ble_uart_bridge.c` 中的 `app_run(ble_uart_bridge_entry)`。
- UART/Worker 初始化：`ble_uart_bridge_task()`。
- BLE 初始化：`ble_uart_bridge_server_init()`。
- GATT 业务：`ble_uart_bridge_server/src/ble_uart_bridge_server.c`。
- 广播配置：`ble_uart_bridge_server/src/ble_uart_bridge_server_adv.c`。

## 8. 整体流程

1. 创建 Bridge Worker，初始化 UART_H1 回调、双向队列和低功耗保护。
2. 初始化 BLE Server，创建服务并广播 `uart1_bridge`。
3. WS63 Client 连接、配对、协商 MTU、发现服务并写 CCCD `02 00`。
4. UART_H1 RX 回调只负责入队，Worker 按当前 MTU 分片发送确认型 Indication。
5. Central 向 Data 特征写入后，数据进入 UART TX 队列并由 Worker 输出。
6. Indication 仅在确认后消费队列；失败或断线时保留数据等待重试。

## 9. 核心文件说明

| 文件 | 作用 | 关键内容 |
|---|---|---|
| `ble_uart_bridge.c` | UART 和桥接 Worker | 引脚、队列、重试、sleep veto |
| `ble_uart_bridge.h` | 公共桥接接口 | 最大载荷、入队和完成通知 |
| `ble_uart_bridge_server/src/ble_uart_bridge_server.c` | GATT Server | 配对、MTU、Read/Write、Indication |
| `ble_uart_bridge_server/src/ble_uart_bridge_server_adv.c` | 广播 | 名称、Service UUID、缓存状态 |

## 10. 核心函数/类说明

- `ble_uart_bridge_uart_init()`：配置 UART_H1 和 RX 回调，并建立低功耗保护。
- `ble_uart_bridge_uart_rx_cb()`：将完整 UART 回调片段放入 RX 环形队列。
- `ble_uart_bridge_process_ble_tx()`：按协商 MTU 从 UART 队列生成下一包 Indication。
- `ble_uart_bridge_uart_enqueue()`：把 BLE Write/Indication 数据放入 UART TX 队列。
- `ble_uart_bridge_server_send_notification()`：发送确认型 Indication。
- `ble_uart_bridge_ble_send_complete()`：成功时消费数据，失败时保留并退避重试。

## 11. 配置项说明

- `CONFIG_SAMPLE_SUPPORT_BLE_UART_BRIDGE_SERVER_SAMPLE=y`：选择本示例。
- 该选项自动 `select UART_SUPPORT_LPM`。
- UART 参数：115200、8 数据位、1 停止位、无校验、无硬件流控。
- GATT：Service `0x4444`；Data `0x4545` Read/Write/Write No Response；UART Indication `0x4546`；CCCD `0x2902`。

接线：

| USB-TTL | WS53 | 说明 |
|---|---|---|
| TX | 板上 pin 4 / AGPIO4 | UART_H1 RX |
| RX | 板上 pin 12 / MGPIO12 | UART_H1 TX |
| GND | GND | 必须共地 |

不要连接 USB-TTL 的 5 V 或 3.3 V 电源脚。

## 12. 使用方法

### 环境准备

- WS53、3.3 V USB-TTL 和 WS63 BLE Client。
- WS53 调试串口、WS63 调试串口和 USB-TTL 三个串口。

### 编译

```powershell
fbb build ws53-liteos-app --clean -j1
```

### 运行

```powershell
fbb flash -f src/output/ws53/fwpkg/ws53_liteos_app/ws53_liteos_app_all.fwpkg --chip ws53 -p COM<N> --timeout 240
fbb monitor --port COM<N> --baud 115200 --chip ws53 --reset --timeout 60
```

USB-TTL 也设为 115200 8N1。WS63 Client 会自动扫描、配对、发现并订阅。

### 运行结果

正常时输出 UART_H1 ready、广播、连接、MTU 247 和 CCCD enabled。出现 `UART RX/TX queue overflow` 表示输入速率超过当前链路处理能力。

## 13. 输入输出示例

### 输入

USB-TTL 向 WS53 pin 4 发送：

```text
WS53_H1_TO_WS63_BLE_OK\r\n
```

Central 向 Data `0x4545` 写入：

```text
uart_from_central
```

### 输出

```text
[ble uart bridge] UART_H1 ready: IRQ mode, RX queue=639, TX queue=639, no DMA, UART_H1 TX=MGPIO12 RX=AGPIO4 mode2 115200 8N1
[ble uart bridge server] UART RX indication CCCD enabled
[ble uart bridge server] BLE write queued to UART TX: bytes=17
```
