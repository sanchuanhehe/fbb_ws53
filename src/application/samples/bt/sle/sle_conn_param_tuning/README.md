# SLE 连接参数调优

## 1. 一句话说明

本示例在两块 WS53 之间请求并确认 SLE 连接参数更新，提供 Low Power、Balanced 和 Low Latency 三组可构建档位。

## 2. 适用场景

- 比较连接间隔、从机延迟和监督超时的配置方法。
- 为低功耗、通用或低时延业务选择初始参数。
- 验证连接参数更新请求及双方回调结果。

## 3. 支持能力

- Server 建链后主动请求所选参数档位。
- 请求前校验协议范围及监督超时约束。
- Server 和 Client 都打印请求值与最终生效值。
- 提供 Low Power、Balanced、Low Latency 三组 Kconfig 档位。
- 三种档位均已完成双板上板验证，双方状态均为 `0x0`。

## 4. 不支持/限制

- 档位在编译期选择，运行时不能动态切换。
- 本示例验证参数协商成功，不直接测量整机电流、吞吐量或端到端业务延迟。
- 实际功耗与时延仍受业务流量、PHY、射频环境和睡眠策略影响。
- Server 与 Client 互斥构建，无需外接硬件。

## 5. 关键词

### 中文关键词

WS53、星闪、SLE、连接间隔、从机延迟、监督超时、低功耗、低时延

### English Keywords

WS53, SLE, connection interval, latency, supervision timeout, low power, low latency

## 6. 目录结构

```text
sle_conn_param_tuning/
├── CMakeLists.txt
├── Kconfig
├── README.md
├── sle_conn_param_tuning.c
├── sle_conn_param_tuning_server/
│   └── src/
│       ├── sle_conn_param_tuning_server.c
│       ├── sle_conn_param_tuning_server.h
│       ├── sle_conn_param_tuning_server_adv.c
│       └── sle_conn_param_tuning_server_adv.h
└── sle_conn_param_tuning_client/
    └── src/
        ├── sle_conn_param_tuning_client.c
        └── sle_conn_param_tuning_client.h
```

## 7. 入口文件

- 主入口：`sle_conn_param_tuning.c`
- 初始化入口：`sle_conn_param_tuning_entry()`
- Server 业务：`sle_conn_param_tuning_server/src/sle_conn_param_tuning_server.c`
- Client 业务：`sle_conn_param_tuning_client/src/sle_conn_param_tuning_client.c`
- 档位配置：`Kconfig`

## 8. 整体流程

1. Server 读取编译期档位并以 `sle_param_server` 广播。
2. Client 匹配广播名，停止扫描并发起连接。
3. 建链后 Server 组装 `sle_connection_param_update_t`。
4. Server 校验数值范围和 `timeout > 2 × (latency + 1) × interval` 约束。
5. Server 发起连接参数更新请求。
6. Client 收到请求，双方在完成回调中打印最终 interval、latency、timeout 和 status。

## 9. 核心文件说明

| 文件 | 作用 |
| --- | --- |
| `sle_conn_param_tuning.c` | 创建所选角色的启动任务。 |
| `sle_conn_param_tuning_server.c` | 定义三种档位、校验参数并请求更新。 |
| `sle_conn_param_tuning_server_adv.c` | 配置 `sle_param_server` 广播。 |
| `sle_conn_param_tuning_client.c` | 扫描建链并记录参数请求和更新完成事件。 |
| `Kconfig` | 为 Server 提供互斥的三种参数档位。 |

## 10. 核心函数/类说明

| 函数 | 功能与调用关系 |
| --- | --- |
| `sle_conn_param_tuning_entry()` | 根据 Kconfig 创建 Server 或 Client 任务。 |
| `sle_conn_param_tuning_server_init()` | 初始化 Server 回调和广播，并打印所选档位。 |
| `sle_conn_param_validate()` | 更新前检查协议范围与超时关系。 |
| `sle_conn_param_request_update()` | Server 建链回调调用，发起参数更新。 |
| `sle_conn_param_tuning_client_init()` | 初始化 Client 扫描、连接和参数更新回调。 |
| 参数更新完成回调 | 双方输出控制器最终采用的参数及状态。 |

## 11. 配置项说明

| 配置项 | interval | latency | timeout | 实际时间 |
| --- | ---: | ---: | ---: | --- |
| `CONFIG_SLE_CONN_PARAM_PROFILE_LOW_POWER` | 400 | 49 | 1200 | 100 ms / 12 s |
| `CONFIG_SLE_CONN_PARAM_PROFILE_BALANCED` | 50 | 0 | 500 | 12.5 ms / 5 s |
| `CONFIG_SLE_CONN_PARAM_PROFILE_LOW_LATENCY` | 30 | 0 | 200 | 7.5 ms / 2 s |

interval 单位为 0.25 ms，timeout 单位为 10 ms。角色配置为 `CONFIG_SAMPLE_SUPPORT_SLE_CONN_PARAM_TUNING_SERVER_SAMPLE` 和 `..._CLIENT_SAMPLE`。

## 12. 使用方法

### 环境准备

- 两块 WS53 开发板和两个调试串口，无需外接硬件。
- 三种档位需分别构建 Server；Client 固件可复用。

### 编译

以下以 Low Power 为例。Balanced 或 Low Latency 只需替换档位配置名。

```powershell
fbb config set CONFIG_SAMPLE_SUPPORT_SLE_CONN_PARAM_TUNING_SERVER_SAMPLE=y --target ws53_liteos_app
fbb config set CONFIG_SLE_CONN_PARAM_PROFILE_LOW_POWER=y --target ws53_liteos_app
fbb build ws53_liteos_app --clean
fbb flash ws53_liteos_app --port <SERVER_COM> --json-summary

fbb config set CONFIG_SAMPLE_SUPPORT_SLE_CONN_PARAM_TUNING_CLIENT_SAMPLE=y --target ws53_liteos_app
fbb build ws53_liteos_app --clean
fbb flash ws53_liteos_app --port <CLIENT_COM> --json-summary
```

先烧录 Server，再切换 Client。固件位于 `output/ws53/fwpkg/ws53_liteos_app/ws53_liteos_app_all.fwpkg`。

### 运行

两端上电后自动连接并更新参数。每换一个 Server 档位，观察两端的 `update complete` 日志。

### 运行结果

两端最终参数与所选档位一致且 `status=0x0` 即通过。

## 13. 输入输出示例

### 输入

编译期选择 Low Latency：

```text
CONFIG_SLE_CONN_PARAM_PROFILE_LOW_LATENCY=y
```

### 输出

```text
[sle conn param server] selected profile=low-latency
[sle conn param server] update request: profile=low-latency, interval=30 (0.25ms), latency=0, timeout=200 (10ms)
[sle conn param server] update complete: conn_id=0x00, status=0x0, interval=30, latency=0, timeout=200
[sle conn param client] update complete: conn_id=0x00, status=0x0, interval=30, latency=0, timeout=200
```

验证结论：Low Power、Balanced、Low Latency 三种档位均已通过双板实测。
