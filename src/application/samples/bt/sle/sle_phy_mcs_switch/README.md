# SLE PHY/MCS 动态切换

## 1. 一句话说明

本示例在 WS53 SLE 链路上周期读取 RSSI，并通过平均、迟滞门限和连续窗口确认，在 Robust、Balanced、Fast 三种 PHY/MCS 档位间自适应切换。

## 2. 适用场景

- 学习 `sle_read_remote_device_rssi()`、`sle_set_phy_param()` 和 `sle_set_mcs()`。
- 根据无线链路质量在可靠性与速率之间切换。
- 验证 1M、2M、4M PHY 及不同 MCS 的协同更新。

## 3. 支持能力

- 每秒读取一次对端 RSSI，每 4 个样本形成一个平均窗口。
- 候选档位连续 2 个窗口一致后才执行切换。
- 使用不同的升档和降档门限形成迟滞，减少来回抖动。
- 先更新 PHY，成功后再设置 MCS。
- Robust、Balanced、Fast 三种档位均已完成双板实测。

## 4. 不支持/限制

- RSSI 受遮挡、天线方向、多径和环境干扰影响，门限需按产品现场重新评估。
- 本示例只演示链路自适应，不包含吞吐量、丢包率和功耗的定量测量。
- Fast 降档等门限触发需要改变实际射频环境，切换时间至少包含两个统计窗口。
- Server 与 Client 互斥构建，无需外接硬件。

## 5. 关键词

### 中文关键词

WS53、星闪、SLE、RSSI、PHY、MCS、自适应、迟滞、链路质量

### English Keywords

WS53, SLE, RSSI, PHY, MCS, adaptive switching, hysteresis, link quality

## 6. 目录结构

```text
sle_phy_mcs_switch/
├── CMakeLists.txt
├── Kconfig
├── README.md
├── sle_phy_mcs_switch.c
├── sle_phy_mcs_switch_server/
│   └── src/
│       ├── sle_phy_mcs_switch_server.c
│       ├── sle_phy_mcs_switch_server.h
│       ├── sle_phy_mcs_switch_server_adv.c
│       └── sle_phy_mcs_switch_server_adv.h
└── sle_phy_mcs_switch_client/
    └── src/
        ├── sle_phy_mcs_switch_client.c
        └── sle_phy_mcs_switch_client.h
```

## 7. 入口文件

- 主入口：`sle_phy_mcs_switch.c`
- 初始化入口：`sle_phy_mcs_switch_entry()`
- 自适应策略：`sle_phy_mcs_switch_server/src/sle_phy_mcs_switch_server.c`
- 广播配置：`sle_phy_mcs_switch_server/src/sle_phy_mcs_switch_server_adv.c`
- Client 业务：`sle_phy_mcs_switch_client/src/sle_phy_mcs_switch_client.c`
- 配置入口：顶层 SLE Sample `choice` 与本目录 `Kconfig`

## 8. 整体流程

1. Server 以 `sle_phy_mcs_server` 广播，Client 自动扫描并连接。
2. Server 建链后首先请求 Robust：1M / MCS0。
3. 自适应任务每秒调用一次远端 RSSI 读取接口。
4. 每 4 个有效样本计算平均 RSSI，并按当前档位和迟滞门限选择候选档。
5. 同一候选连续出现 2 个窗口后，Server 请求更新 PHY。
6. PHY 回调成功后设置对应 MCS；Client 回调显示实际 PHY 更新结果。

## 9. 核心文件说明

| 文件 | 作用 |
| --- | --- |
| `sle_phy_mcs_switch.c` | 创建 Server 或 Client 启动任务。 |
| `sle_phy_mcs_switch_server.c` | RSSI 采样、档位决策、PHY/MCS 两阶段切换。 |
| `sle_phy_mcs_switch_server_adv.c` | 配置 `sle_phy_mcs_server` 广播。 |
| `sle_phy_mcs_switch_client.c` | 扫描建链并输出对端请求后的 PHY 更新结果。 |

## 10. 核心函数/类说明

| 函数 | 功能与调用关系 |
| --- | --- |
| `sle_phy_mcs_switch_entry()` | 根据 Kconfig 启动对应角色。 |
| `sle_phy_mcs_switch_server_init()` | 初始化广播、连接回调和自适应任务。 |
| `sle_phy_mcs_select_profile()` | 根据平均 RSSI、当前档位及迟滞门限选择目标档。 |
| `sle_phy_mcs_request_profile()` | 先调用 `sle_set_phy_param()`，回调成功后调用 `sle_set_mcs()`。 |
| `sle_phy_mcs_read_rssi_cb()` | 汇总 RSSI 样本并执行连续窗口确认。 |
| `sle_phy_mcs_switch_client_init()` | 初始化 Client 扫描、连接和 PHY 回调。 |

## 11. 配置项说明

| 档位 | PHY / MCS | 进入或退出门限 |
| --- | --- | --- |
| Robust | 1M / MCS0 | RSSI ≥ -70 dBm 时转 Balanced。 |
| Balanced | 2M / MCS4 | RSSI ≤ -78 dBm 转 Robust；RSSI ≥ -50 dBm 转 Fast。 |
| Fast | 4M / MCS10 | RSSI ≤ -62 dBm 时转 Balanced。 |

采样周期为 1000 ms，平均窗口为 4 点，确认窗口为 2 个。角色配置为 `CONFIG_SAMPLE_SUPPORT_SLE_PHY_MCS_SWITCH_SERVER_SAMPLE` 和 `..._CLIENT_SAMPLE`。

## 12. 使用方法

### 环境准备

- 两块 WS53 开发板和两个调试串口。
- 改变两板距离、方向或遮挡可促使档位变化，但应避免接触天线区域。

### 编译

```powershell
fbb config set CONFIG_SAMPLE_SUPPORT_SLE_PHY_MCS_SWITCH_SERVER_SAMPLE=y --target ws53_liteos_app
fbb build ws53_liteos_app --clean
fbb flash ws53_liteos_app --port <SERVER_COM> --json-summary

fbb config set CONFIG_SAMPLE_SUPPORT_SLE_PHY_MCS_SWITCH_CLIENT_SAMPLE=y --target ws53_liteos_app
fbb build ws53_liteos_app --clean
fbb flash ws53_liteos_app --port <CLIENT_COM> --json-summary
```

先烧录 Server，再切换 Client。固件位于 `output/ws53/fwpkg/pack_all_core/ws53_liteos_app/ws53_liteos_app_all_in_one.fwpkg`。

### 运行

两板上电后等待建链，观察 Server 的 `RSSI window`、`switch request`、`switch complete` 以及 Client 的 PHY 回调。

### 运行结果

切换状态为 `0x0`，Client 能依次确认 1M、2M、4M，即对应档位生效。

## 13. 输入输出示例

### 输入

无需命令输入；通过改变两板射频环境改变 RSSI。

### 输出

```text
[sle phy mcs server] switch complete: profile=robust, phy=1M, mcs=0, status=0x0
[sle phy mcs server] switch complete: profile=balanced, phy=2M, mcs=4, status=0x0
[sle phy mcs server] switch complete: profile=fast, phy=4M, mcs=10, status=0x0
```

验证结论：Robust 1M/MCS0、Balanced 2M/MCS4、Fast 4M/MCS10 均已通过上板验证。
