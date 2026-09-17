# SLE 设备参数配置与 NV 持久化

## 1. 一句话说明

本示例使用两块 WS53 演示 Client 通过 SLE SSAP 读写设备配置，由 Server 校验合法性并保存到 NV，复位后仍可恢复配置。

## 2. 适用场景

- 无线修改设备工作参数。
- 验证 SSAP 读写请求、错误状态返回与数据校验。
- 学习 WS53 用户 NV 的保存和启动加载流程。

## 3. 支持能力

- Client 自动写入合法配置、回读并比对。
- Server 拒绝超出范围的配置并返回失败状态。
- 合法配置写入 NV ID `0x20A1`。
- Server 复位后从 NV 加载已保存配置。
- 已验证合法写入、非法拒绝、回读一致性和复位持久化。

## 4. 不支持/限制

- 配置字段仅用于演示，未直接驱动传感器或其他业务外设。
- 协议直接传输 8 字节结构体；跨编译器或跨架构使用时应改为显式序列化。
- Server 与 Client 为互斥构建角色，需要两块开发板分别烧录。
- 本示例无需外接硬件。

## 5. 关键词

### 中文关键词

WS53、星闪、SLE、SSAP、参数配置、数据校验、NV、持久化

### English Keywords

WS53, SLE, SSAP, device configuration, validation, NV, persistence

## 6. 目录结构

```text
sle_device_config/
├── CMakeLists.txt
├── Kconfig
├── README.md
├── sle_device_config.c
├── sle_device_config_protocol.h
├── sle_device_config_server/
│   └── src/
│       ├── sle_device_config_server.c
│       ├── sle_device_config_server.h
│       ├── sle_device_config_server_adv.c
│       └── sle_device_config_server_adv.h
└── sle_device_config_client/
    └── src/
        ├── sle_device_config_client.c
        └── sle_device_config_client.h
```

## 7. 入口文件

- 主入口：`sle_device_config.c`
- 初始化入口：`sle_device_config_entry()`
- 公共协议：`sle_device_config_protocol.h`
- Server 业务：`sle_device_config_server/src/sle_device_config_server.c`
- Client 业务：`sle_device_config_client/src/sle_device_config_client.c`
- 配置入口：顶层 SLE Sample `choice` 与本目录 `Kconfig`

## 8. 整体流程

1. Server 初始化时读取 NV；记录合法则恢复，否则使用默认配置。
2. Server 以 `config_server` 广播，Client 扫描、连接、配对并发现属性。
3. Client 写入 `500 ms / 75.0 ℃ / mode 1` 的合法配置。
4. Server 校验后更新内存并写入 NV，Client 回读确认一致。
5. Client 再写入 `interval=50 ms` 的非法配置。
6. Server 拒绝该写入并返回错误状态；复位 Server 可再次验证 NV 加载。

## 9. 核心文件说明

| 文件 | 作用 |
| --- | --- |
| `sle_device_config.c` | 驱动 Client 自动测试步骤，创建 Server 或 Client 任务。 |
| `sle_device_config_protocol.h` | 定义 8 字节配置结构、Magic、版本与字段范围。 |
| `sle_device_config_server.c` | 处理读写、校验配置并执行 NV 保存和加载。 |
| `sle_device_config_client.c` | 完成建链并发起合法写、回读和非法写。 |
| `sle_device_config_server_adv.c` | 配置 `config_server` 广播。 |

## 10. 核心函数/类说明

| 函数 | 功能与调用关系 |
| --- | --- |
| `sle_device_config_entry()` | 根据 Kconfig 启动 Server 或 Client 任务。 |
| `sle_device_config_server_init()` | 初始化配置、SSAP 服务和广播。 |
| `sle_device_config_is_valid()` | Server 写回调调用，校验 Magic、版本及字段范围。 |
| `sle_device_config_client_init()` | 初始化扫描、连接和 SSAP Client 回调。 |
| `sle_device_config_client_send_valid_config()` | 发送预设合法配置。 |
| `sle_device_config_client_read_config()` | 读取 Server 当前配置并校验持久化结果。 |
| `sle_device_config_client_send_invalid_config()` | 发送越界间隔，验证拒绝路径。 |

## 11. 配置项说明

| 配置项/字段 | 取值与说明 |
| --- | --- |
| Server / Client Kconfig | `CONFIG_SAMPLE_SUPPORT_SLE_DEVICE_CONFIG_SERVER_SAMPLE` / `..._CLIENT_SAMPLE`。 |
| `magic` | 固定 `0x5343`。 |
| `version` | 固定 `1`。 |
| `report_interval_ms` | `100`～`60000` ms。 |
| `alarm_threshold_decicelsius` | `-200`～`1000`，单位 0.1 ℃。 |
| `mode` | `0` 或 `1`。 |
| NV ID | `0x20A1`。 |

## 12. 使用方法

### 环境准备

- 两块 WS53 开发板和两个调试串口，无需外接传感器。
- 记录 Server 串口，持久化验证时需复位同一块 Server 板。

### 编译

```powershell
fbb config set CONFIG_SAMPLE_SUPPORT_SLE_DEVICE_CONFIG_SERVER_SAMPLE=y --target ws53_liteos_app
fbb build ws53_liteos_app --clean
fbb flash ws53_liteos_app --port <SERVER_COM> --json-summary

fbb config set CONFIG_SAMPLE_SUPPORT_SLE_DEVICE_CONFIG_CLIENT_SAMPLE=y --target ws53_liteos_app
fbb build ws53_liteos_app --clean
fbb flash ws53_liteos_app --port <CLIENT_COM> --json-summary
```

必须先烧录 Server，再切换并构建 Client。固件位于 `output/ws53/fwpkg/pack_all_core/ws53_liteos_app/ws53_liteos_app_all_in_one.fwpkg`。

### 运行

两块板上电后自动执行测试。看到非法配置已拒绝后，复位 Server 并检查 NV 加载日志。

### 运行结果

合法配置保存和回读一致、非法配置返回 `status=0xf`、Server 复位后打印 `config loaded from NV` 即通过。

## 13. 输入输出示例

### 输入

```text
valid:   magic=0x5343, interval=500, threshold=750, mode=1, version=1
invalid: magic=0x5343, interval=50,  threshold=750, mode=1, version=1
```

### 输出

```text
[sle device config server] config saved: interval=500, threshold=750, mode=1
[sle device config client] persisted config verified
[sle device config server] rejected: interval=50, threshold=750, mode=1
[sle device config client] invalid config rejected, status=0xf
[sle device config server] config loaded from NV: interval=500, threshold=750, mode=1
```

验证结论：合法/非法写入、读取及 NV 复位持久化均已通过上板验证。
