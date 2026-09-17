# SLE Hello 基础通信

## 1. 一句话说明

本示例在 WS53 上演示 SLE Server 与 Client 从广播、扫描、连接、配对、服务发现到通知及属性读写的完整基础链路。

## 2. 适用场景

- 初次验证两块开发板的 SLE 通信能力。
- 学习 SSAP Service、Property、Notification、Read 和 Write 的基本用法。
- 作为其他双板 SLE Sample 的最小参考工程。

## 3. 支持能力

- Server 以 `hello_server` 名称广播，Client 自动扫描并连接。
- 使用 Just Works 配对并交换 520 字节 MTU。
- Server 推送 `hello world` 通知。
- Client 自动读取属性，再写入 `new_config_value`。
- 断链后 Server 恢复广播，Client 恢复扫描。

## 4. 不支持/限制

- Server 与 Client 属于同一个 Kconfig `choice`，同一份固件只能选择一个角色。
- Just Works 不提供 MITM 防护，生产产品应按安全要求调整配对方式。
- 本示例用于功能演示，不包含吞吐量、功耗或异常链路压力测试。
- 主链路已在 WS53 双板及 WS53/WS63 跨芯片场景验证，无需外接外设。

## 5. 关键词

### 中文关键词

WS53、星闪、SLE、SSAP、广播、扫描、配对、通知、属性读写

### English Keywords

WS53, SLE, SSAP, announce, seek, pairing, notification, read, write

## 6. 目录结构

```text
sle_hello/
├── CMakeLists.txt
├── Kconfig
├── README.md
├── DESIGN.md
├── sle_hello.c
├── sle_hello_server/
│   └── src/
│       ├── sle_hello_server.c
│       ├── sle_hello_server.h
│       ├── sle_hello_server_adv.c
│       └── sle_hello_server_adv.h
└── sle_hello_client/
    └── src/
        ├── sle_hello_client.c
        └── sle_hello_client.h
```

## 7. 入口文件

- 主入口：`sle_hello.c`
- 初始化入口：`sle_hello_entry()`
- Server 业务：`sle_hello_server/src/sle_hello_server.c`
- Client 业务：`sle_hello_client/src/sle_hello_client.c`
- 配置入口：顶层 SLE Sample `choice` 与本目录 `Kconfig`

## 8. 整体流程

1. Server 注册连接、SSAP 和广播回调，创建服务后开始广播。
2. Client 启动扫描，匹配 `hello_server` 后停止扫描并发起连接。
3. Client 发起配对和 MTU 交换，然后发现 Service 与 Property。
4. Server 发送 `hello world` Notification。
5. Client 发起 Read Request，收到确认后发送 `new_config_value` Write Request。
6. 任一端断链后恢复广播或扫描，等待重新连接。

## 9. 核心文件说明

| 文件 | 作用 |
| --- | --- |
| `sle_hello.c` | 创建 Sample 任务，选择 Server 或 Client，并处理 Client 侧通知及读写确认。 |
| `sle_hello_server.c` | 注册 SSAP 服务、处理读写请求并发送通知。 |
| `sle_hello_server_adv.c` | 配置 `hello_server` 广播数据与广播参数。 |
| `sle_hello_client.c` | 完成扫描、连接、配对、服务发现和属性读写。 |

## 10. 核心函数/类说明

| 函数 | 功能与调用关系 |
| --- | --- |
| `sle_hello_entry()` | 系统启动入口，根据 Kconfig 创建对应角色任务。 |
| `sle_hello_server_init()` | Server 任务调用，初始化 SLE 服务并开始广播。 |
| `sle_hello_server_send_data()` | Server 在连接完成后通过 Notification 发送数据。 |
| `sle_hello_client_init()` | Client 任务调用，注册扫描、连接和 SSAP Client 回调。 |
| `sle_hello_client_send_write_req()` | Client 在读取确认后发送属性写请求。 |
| `sle_hello_client_start_scan()` | Client 初始化完成或断链后启动扫描。 |

## 11. 配置项说明

| 配置项 | 说明 |
| --- | --- |
| `CONFIG_SAMPLE_SUPPORT_SLE_HELLO_SERVER_SAMPLE` | 构建 Server 固件。 |
| `CONFIG_SAMPLE_SUPPORT_SLE_HELLO_CLIENT_SAMPLE` | 构建 Client 固件。 |
| 广播名 | `hello_server`。 |
| Service / Property UUID | `0x3333` / `0x3434`。 |
| MTU | 520 字节。 |

## 12. 使用方法

### 环境准备

- 两块 WS53 开发板、两根 USB 数据线及两个可用串口。
- 在 SDK 根目录执行命令，端口以系统实际枚举结果为准。

### 编译

先构建并烧录 Server，再切换到 Client；两种角色共享同一固件输出路径。

```powershell
fbb config set CONFIG_SAMPLE_SUPPORT_SLE_HELLO_SERVER_SAMPLE=y --target ws53_liteos_app
fbb build ws53_liteos_app --clean
fbb flash ws53_liteos_app --port <SERVER_COM> --json-summary

fbb config set CONFIG_SAMPLE_SUPPORT_SLE_HELLO_CLIENT_SAMPLE=y --target ws53_liteos_app
fbb build ws53_liteos_app --clean
fbb flash ws53_liteos_app --port <CLIENT_COM> --json-summary
```

固件输出：`output/ws53/fwpkg/pack_all_core/ws53_liteos_app/ws53_liteos_app_all_in_one.fwpkg`。

### 运行

两块板上电后会自动建立连接，无固定上电顺序。分别监视两个调试串口即可。

```powershell
fbb monitor --port <CLIENT_COM> --until "hello world" --timeout 30 --json-summary
```

### 运行结果

Client 收到 `hello world`，Read Confirmation 成功且 Write Confirmation 返回成功即通过。

## 13. 输入输出示例

### 输入

无需人工输入；Client 自动读取属性并写入字符串 `new_config_value`。

### 输出

```text
[sle hello client] connected, conn_id=0x00
[sle hello client] pair complete conn_id:0, status:0
[SLE Hello Client] Received: hello world
[SLE Hello Client] Write cfm: success, handle=0x11
```

验证结论：SLE 建链、通知、读取与写入均已通过上板验证。
