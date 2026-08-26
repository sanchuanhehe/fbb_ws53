# WS53 BLE Hello Server SDD

## 1. 状态

- 来源：WS63 `master`，提交 `3808e172a274af414895e7434fae26c5b82e7240`。
- 目标：WS53 `feature/ws53-sle-samples`，基线提交 `8ac4b4ace699c4a4cdc30237033a4b3bf1cb0118`。
- WS53 clean build：通过。
- 烧录：COM9/WS53 Server 与 COM5/WS63 Client 均通过，后端 `hsflash`。
- BLE Notify、Read、Write、重连：通过。
- 验证日期：2026-08-14。

## 2. 架构

| 模块 | 职责 |
| --- | --- |
| `ble_hello.c` | `app_run()` 入口，创建 Server 任务 |
| `ble_hello_server.c` | GAP/GATTS 回调、服务和属性、配对、Notify、读写响应 |
| `ble_hello_server_adv.c` | 广播数据、启动广播和断线重广播 |
| 外层 `Kconfig`/`CMakeLists.txt` | 通过 `CONFIG_SAMPLE_SUPPORT_BLE_HELLO_SERVER_SAMPLE` 选择并接入样例 |

WS63 的 `ble_hello_client` 不复制进 WS53 工程，只作为独立参考端运行。

## 3. GAP/GATT 设计

Server 使用名称 `ble_hello_server`、30 ms 可连接非定向广播，并携带 16-bit Service UUID `0x3333`。

| 属性 | UUID | 行为 |
| --- | --- | --- |
| Primary Service | `0x3333` | 自定义教学服务 |
| Data | `0x3434` | 读写，初值 `device_status_ok` |
| Hello | `0x3435` | CCCD 开启后 Notify `hello world` |
| CCCD | `0x2902` | 接受 `00 00` 或 `01 00` |

Data 固定缓冲区为 32 字节；合法写长度为 1–31。断连时清除连接和 CCCD 状态并重新广播。

## 4. WS53 适配点

- WS53 的 `gap_ble_callbacks_t` 没有 WS63 使用的 `ble_enable_cb`/`ble_disable_cb` 字段，因此不注册这两个回调。
- 初始化任务延时 1 秒后调用 `enable_ble()`，再注册 GAP/GATTS 回调、配置安全参数并创建服务。
- 不执行 WS63 Client 中用于清理 retained GATT 状态的 BLE stack cycle。
- 当前 `ws53_liteos_app` 构建显示 `BTC_CENTRAL_ROLE_SUPPORT OFF`；GATTC 注册 API 在实板返回 `ERRCODE_BT_UNSUPPORTED`，所以本移植只支持 Server/Peripheral 角色。

## 5. 验证序列

```text
WS53 advertise ble_hello_server
  -> WS63 scan/connect/pair
  -> MTU 247
  -> discover service/characteristics/CCCD
  -> write CCCD 01 00
  -> WS53 notify hello world
  -> WS63 read Data = device_status_ok
  -> WS63 write Data = new_config_value
  -> 双端确认写成功
```

实板还覆盖了旧配对信息失效场景：第一次重连因配对状态不一致断开，WS63 删除 stale pair 后重新扫描、配对并完成全部业务。

## 6. 验收证据

| 项目 | 结果 |
| --- | --- |
| WS53 clean build | 通过；map 含 hello server/adv 对象，不含已撤销的 speed client 对象 |
| WS63 clean build | 通过；hello client 对象 1 个，speed client/server 对象 0 个 |
| 烧录 | COM9 WS53、COM5 WS63 均成功 |
| Notify | Client 收到 `hello world` |
| Read | Client 读到 `device_status_ok` |
| Write | Server 更新为 `new_config_value`，Client 收到 success CFM |
| 重连恢复 | 通过 |

日志位于工作区 `codex_test/logs/ws53_com9_ble_hello_server_final.log` 和 `codex_test/logs/ws63_com5_ble_hello_client_final.log`。
