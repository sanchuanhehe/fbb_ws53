# WS53 BLE Speed Server

## 1. 一句话说明

本示例提供 WS53 BLE GATT 吞吐 Server，可选择连续 220 字节 Notification 压测模式，或 Write Without Response 到 Indication 的回环模式。

## 2. 适用场景

- 测量 WS53 BLE 空口吞吐和稳定性。
- 验证 ATT MTU、2M PHY、Data Length Extension 和协议栈发送缓冲。
- 作为 WS63 Speed Client 的吞吐或回环联调端。

## 3. 支持能力

- 广播名 `ble_uuid_server`，Service `0xABCD`，Report `0xCDEF`，CCCD `0x2902`。
- 吞吐模式：220 字节 Notification，目标 MTU 247、2M PHY、251 字节 Data Length。
- 回环模式：接收 Write Without Response 并通过 Indication 原样返回。
- 连接后请求 MTU 247，并支持断线后重新广播。

## 4. 不支持/限制

- 吞吐结果受 Client、射频环境、连接参数和日志打印影响，不代表产品保证值。
- 吞吐模式持续运行，发送任务不会自动结束。
- 本示例使用固定 BLE 地址，和其他固定地址 Sample 并行时需避免冲突。
- `CONFIG_BLE_SPEED_TEST` 改变特征属性，Server 和 Client 必须选择匹配模式。

## 5. 关键词

### 中文关键词

WS53、BLE 吞吐、速度测试、2M PHY、MTU、Notification、Indication、回环

### English Keywords

WS53, BLE throughput, speed test, 2M PHY, MTU, notification, indication, loopback

## 6. 目录结构

```text
ble_speed_server/
  README.md
  Kconfig
  CMakeLists.txt
  inc/
    ble_speed_server.h
    ble_speed_server_adv.h
  src/
    ble_speed_server.c
    ble_speed_server_adv.c
```

## 7. 入口文件

- 主入口：`src/ble_speed_server.c` 中的 `app_run(ble_speed_entry)`。
- 初始化入口：`ble_uuid_server_init()`。
- 吞吐发送任务：`send_data_thread_function()`。
- 回环处理：`ble_uuid_server_send_report_back()`。
- 配置入口：`Kconfig`。

## 8. 整体流程

1. 创建 Speed Server 任务，使能 BLE 并注册 GAP/GATTS 回调。
2. 创建 `0xABCD/0xCDEF` 服务并广播 `ble_uuid_server`。
3. Client 连接后请求 MTU 247。
4. 吞吐模式等待 5 秒，设置 2M PHY 和 Data Length，再按发送缓冲余量持续发送。
5. 每发送 100 包打印一次内存状态并退避 330 ms。
6. 回环模式把 Client 写入载荷通过 Indication 返回。

## 9. 核心文件说明

| 文件 | 作用 | 关键内容 |
|---|---|---|
| `src/ble_speed_server.c` | GATT 和测试业务 | 连接、MTU、发送任务、回环 |
| `src/ble_speed_server_adv.c` | 广播 | 名称、Appearance、广播参数 |
| `inc/ble_speed_server.h` | UUID 和公开接口 | 模式相关 Characteristic 属性 |
| `Kconfig` | 模式选择 | `BLE_SPEED_TEST` |

## 10. 核心函数/类说明

- `ble_uuid_server_init()`：配置安全、地址、回调、服务和广播。
- `send_data_thread_function()`：吞吐模式下持续发送 220 字节 Notification。
- `ble_uuid_server_receive_write_req_cbk()`：接收 Client 写入；回环模式触发原样返回。
- `ble_uuid_server_send_report_by_uuid()`：按 UUID 发送报告。
- `ble_uuid_server_send_report_by_handle()`：按 Handle 发送回环 Indication。

## 11. 配置项说明

| 配置项 | 默认值 | 说明 |
|---|---:|---|
| `CONFIG_SAMPLE_SUPPORT_BLE_SPEED_SERVER_SAMPLE` | `y` | 选择 Speed Server |
| `CONFIG_BLE_SPEED_TEST` | `y` | `y`=连续 Notification；`n`=Write/Indication 回环 |
| `DATA_LEN` | 220 | 吞吐包载荷字节数 |
| `DEFAULT_BLE_SPEED_MTU_SIZE` | 247 | 目标 ATT MTU |

## 12. 使用方法

### 环境准备

- WS53 Server 和匹配模式的 WS63 Speed Client。
- 两块板尽量靠近，并关闭同地址 BLE Sample。

### 编译

选择 Speed Server 和所需模式后执行：

```powershell
fbb build ws53-liteos-app --clean -j1
```

### 运行

```powershell
fbb flash -f src/output/ws53/fwpkg/ws53_liteos_app/ws53_liteos_app_all.fwpkg --chip ws53 -p COM<N> --timeout 240
fbb monitor --port COM<N> --baud 115200 --chip ws53 --reset --timeout 60
```

### 运行结果

吞吐模式应看到 `start send notify info` 和每 100 包的内存日志；回环模式应看到 `write echo len=<n>`，Client 负责统计包数、耗时和吞吐。

## 13. 输入输出示例

### 输入

- 吞吐模式：Client 连接并订阅 `0xCDEF` Notification。
- 回环模式：Client 向 `0xCDEF` Write Without Response 写入测试包。

### 输出

```text
mtu change change server_id: 1, conn_id: 0, mtu_size: 247, status:0
start send notify info.
[SYS INFO] send 100 pkt: mem: used:<n>, free:<n>.
```
