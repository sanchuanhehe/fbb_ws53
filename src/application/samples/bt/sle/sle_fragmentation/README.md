# SLE 大数据分片与重组

## 1. 一句话说明

本示例在 WS53 上将 1024 字节测试数据拆成 6 个 SLE Notification 分片发送，并在 Client 端按序重组和校验。

## 2. 适用场景

- 传输大于单次应用载荷的数据块。
- 学习应用层分片头、序号、偏移和完整性校验设计。
- 验证 WS53 与 WS63 之间的 SLE 数据兼容性。

## 3. 支持能力

- 固定生成 1024 字节测试数据。
- 每片最大负载 180 字节，发送 `180 × 5 + 124` 字节。
- 16 字节分片头携带 Magic、传输 ID、序号、总片数、偏移和长度。
- Client 检查分片边界、按偏移重组，并计算总和校验值。
- 已验证 WS53 双板和 WS53/WS63 两个方向的传输。

## 4. 不支持/限制

- 当前数据长度、分片负载和传输 ID 为演示固定值，不是通用文件传输协议。
- 应用层未实现丢片重传、乱序缓存、并发多传输或断点续传。
- 完整性检查使用简单求和，不适合作为安全校验。
- Server 与 Client 需分别构建和烧录，无需外接硬件。

## 5. 关键词

### 中文关键词

WS53、星闪、SLE、分片、重组、大数据、Notification、完整性校验

### English Keywords

WS53, SLE, fragmentation, reassembly, large payload, notification, checksum

## 6. 目录结构

```text
sle_fragmentation/
├── CMakeLists.txt
├── Kconfig
├── README.md
├── sle_fragmentation.c
├── sle_fragmentation_protocol.h
├── sle_fragmentation_server/
│   └── src/
│       ├── sle_fragmentation_server.c
│       ├── sle_fragmentation_server.h
│       ├── sle_fragmentation_server_adv.c
│       └── sle_fragmentation_server_adv.h
└── sle_fragmentation_client/
    └── src/
        ├── sle_fragmentation_client.c
        └── sle_fragmentation_client.h
```

## 7. 入口文件

- 主入口：`sle_fragmentation.c`
- 初始化入口：`sle_fragmentation_entry()`
- 协议定义：`sle_fragmentation_protocol.h`
- Server 业务：`sle_fragmentation_server/src/sle_fragmentation_server.c`
- Client 业务：`sle_fragmentation_client/src/sle_fragmentation_client.c`
- 配置入口：顶层 SLE Sample `choice` 与本目录 `Kconfig`

## 8. 整体流程

1. Server 以 `fragment_server` 广播，Client 自动扫描、连接、配对并发现属性。
2. Client 写入一个字节 `0x01` 作为传输触发命令。
3. Server 生成 1024 字节递增测试数据并计算总片数。
4. Server 每隔 20 ms 发送一个带 16 字节头的 Notification 分片。
5. Client 校验头部和边界，将负载复制到接收缓冲区相应偏移。
6. 收齐 6 片后，Client 计算接收长度和 checksum 并输出结果。

## 9. 核心文件说明

| 文件 | 作用 |
| --- | --- |
| `sle_fragmentation.c` | 创建角色任务，并在 Client 回调中执行分片解析与重组。 |
| `sle_fragmentation_protocol.h` | 定义分片头、数据总长、单片负载和总片数。 |
| `sle_fragmentation_server.c` | 处理启动命令，创建发送任务并逐片发送。 |
| `sle_fragmentation_client.c` | 扫描建链、服务发现并发送传输触发命令。 |
| `sle_fragmentation_server_adv.c` | 配置 `fragment_server` 广播。 |

## 10. 核心函数/类说明

| 函数 | 功能与调用关系 |
| --- | --- |
| `sle_fragmentation_entry()` | 根据 Kconfig 启动 Server 或 Client 任务。 |
| `sle_fragmentation_server_init()` | 初始化 SSAP Server 和广播。 |
| `sle_fragmentation_server_send_data()` | 发送单个已封装分片。 |
| `sle_fragmentation_client_init()` | 初始化 Client 扫描、连接与数据回调。 |
| `sle_fragmentation_client_send_write_req()` | 服务发现后发送 `0x01`，触发 Server 传输。 |
| Client Notification 回调 | 校验分片头、复制负载并在收齐后输出 checksum。 |

## 11. 配置项说明

| 配置项 | 值与说明 |
| --- | --- |
| Server / Client Kconfig | `CONFIG_SAMPLE_SUPPORT_SLE_FRAGMENTATION_SERVER_SAMPLE` / `..._CLIENT_SAMPLE`。 |
| `SLE_FRAGMENTATION_MAGIC` | `0x5346`。 |
| `SLE_FRAGMENTATION_TRANSFER_ID` | `1`。 |
| `SLE_FRAGMENTATION_DATA_SIZE` | 1024 字节。 |
| `SLE_FRAGMENTATION_PAYLOAD_SIZE` | 180 字节。 |
| 总片数 | 6。 |
| SSAP MTU | 520 字节。 |

## 12. 使用方法

### 环境准备

- 两块 WS53 开发板和两个调试串口。
- 若验证跨芯片兼容性，可将一端替换为对应 WS63 固件。

### 编译

```powershell
fbb config set CONFIG_SAMPLE_SUPPORT_SLE_FRAGMENTATION_SERVER_SAMPLE=y --target ws53_liteos_app
fbb build ws53_liteos_app --clean
fbb flash ws53_liteos_app --port <SERVER_COM> --json-summary

fbb config set CONFIG_SAMPLE_SUPPORT_SLE_FRAGMENTATION_CLIENT_SAMPLE=y --target ws53_liteos_app
fbb build ws53_liteos_app --clean
fbb flash ws53_liteos_app --port <CLIENT_COM> --json-summary
```

必须先烧录 Server，再切换 Client。固件位于 `output/ws53/fwpkg/pack_all_core/ws53_liteos_app/ws53_liteos_app_all_in_one.fwpkg`。

### 运行

两端上电后自动建链并传输，无需人工输入。

### 运行结果

Client 收到 6 个连续分片，最终长度为 1024、checksum 为 130560 即通过。

## 13. 输入输出示例

### 输入

Client 自动向 Server 写入启动命令：

```text
01
```

### 输出

```text
[sle fragmentation client] fragment received: 1/6, total_bytes=180
[sle fragmentation client] fragment received: 6/6, total_bytes=1024
[sle fragmentation client] reassembly complete: bytes=1024, checksum=130560
[sle fragmentation client] test passed
```

验证结论：6 片重组和 checksum 已在双 WS53 及 WS53/WS63 双向场景通过。
