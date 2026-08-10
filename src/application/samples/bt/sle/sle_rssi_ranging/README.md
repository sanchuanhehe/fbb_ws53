# SLE RSSI 粗粒度测距与一米校准

## 1. 一句话说明

本示例使用两块 WS53 的连接态 RSSI 估算距离，并支持在 Client 板上长按 S1 完成 100 cm 单点校准及 NV 持久化。

## 2. 适用场景

- 接近检测、距离趋势观察和近/中/远粗粒度分区。
- 学习连接态 RSSI 读取、中值滤波、EMA 和路径损耗模型。
- 使用板载按键完成现场一米标定并保存结果。

## 3. 支持能力

- Client 每秒读取一次连接态 RSSI。
- 使用 7 点中值滤波和权重 3:1 的 EMA 平滑结果。
- 输出估算厘米值及 `near`、`middle`、`far` 分区。
- 长按板载 S1 约 2 秒，按 200 ms 间隔采集 31 个校准样本。
- 以中位数作为 `A=RSSI@1m`，保存 MAD、范围和样本数到 NV `0x5101`。
- 已验证按键、校准、NV 重启加载及 100 cm 实测链路。

## 4. 不支持/限制

- RSSI 测距易受遮挡、多径、天线方向和个体差异影响，不能替代 HADM 等高精度测距方案。
- 100 cm 单点只能校准固定偏移 `A`，不能同时拟合路径损耗指数 `n`。
- 实测 100 cm 时曾输出约 89 cm，仅代表当时环境，不构成精度保证。
- GPIO5 的可选 SK6805-EC20 灯效代码已保留，但灯效和波形尚未实物验证；串口日志不依赖该灯，未测灯效不影响主功能验收。
- Server 与 Client 互斥构建；校准按键位于 Client 板。

## 5. 关键词

### 中文关键词

WS53、星闪、SLE、RSSI、测距、中值滤波、EMA、一米校准、S1、NV

### English Keywords

WS53, SLE, RSSI ranging, median filter, EMA, one-metre calibration, button, NV

## 6. 目录结构

```text
sle_rssi_ranging/
├── CMakeLists.txt
├── Kconfig
├── README.md
├── sle_rssi_ranging.c
├── sle_rssi_ranging_server/
│   └── src/
│       ├── sle_rssi_ranging_server.c
│       ├── sle_rssi_ranging_server.h
│       ├── sle_rssi_ranging_server_adv.c
│       └── sle_rssi_ranging_server_adv.h
└── sle_rssi_ranging_client/
    └── src/
        ├── sle_rssi_ranging_client.c
        ├── sle_rssi_ranging_client.h
        ├── sle_rssi_ranging_calibration.c
        └── sle_rssi_ranging_calibration.h
```

## 7. 入口文件

- 主入口：`sle_rssi_ranging.c`
- 初始化入口：`sle_rssi_ranging_entry()`
- 测距业务：`sle_rssi_ranging_client/src/sle_rssi_ranging_client.c`
- 按键与校准：`sle_rssi_ranging_client/src/sle_rssi_ranging_calibration.c`
- Server 广播：`sle_rssi_ranging_server/src/sle_rssi_ranging_server_adv.c`
- 配置入口：`Kconfig`

## 8. 整体流程

1. Server 以 `sle_rssi_server` 广播，Client 匹配名称并连接。
2. Client 每秒调用 `sle_read_remote_device_rssi()`。
3. 正常测距样本进入 7 点中值滤波，再进入 EMA。
4. Client 用 `d = 100 × 10^((A - RSSI) / (10 × n))` 估算厘米距离并分区。
5. 两板固定在 100 cm，长按 Client 板载 S1 约 2 秒进入校准。
6. 校准模式以 200 ms 间隔收集 31 个原始 RSSI，计算中位数和 MAD。
7. 校准记录写入 NV，当前会话立即生效；正常重启后自动加载。

## 9. 核心文件说明

| 文件 | 作用 |
| --- | --- |
| `sle_rssi_ranging.c` | 创建 Server 或 Client 任务。 |
| `sle_rssi_ranging_client.c` | 建链、轮询 RSSI、滤波、距离估算与分区。 |
| `sle_rssi_ranging_calibration.c` | 轮询 S1、收集校准样本、读写 NV，并驱动可选 SK6805。 |
| `sle_rssi_ranging_server.c` | 管理 Server 连接状态。 |
| `sle_rssi_ranging_server_adv.c` | 配置 `sle_rssi_server` 广播。 |

## 10. 核心函数/类说明

| 函数 | 功能与调用关系 |
| --- | --- |
| `sle_rssi_ranging_entry()` | 根据 Kconfig 启动对应角色。 |
| `sle_rssi_ranging_client_init()` | 初始化扫描、连接、校准模块和 RSSI 轮询任务。 |
| `sle_rssi_process_sample()` | 对正常 RSSI 执行中值滤波、EMA、测距和分区。 |
| `sle_rssi_estimate_distance_cm()` | 使用对数路径损耗模型计算距离。 |
| `sle_rssi_calibration_init()` | 初始化 MIO06 S1、NV、校准任务和可选 GPIO5 LED。 |
| `sle_rssi_calibration_add_sample()` | 收齐 31 点后计算 A/MAD 并保存 NV。 |
| `sle_rssi_calibration_get_rssi_at_1m()` | 返回有效 NV 值，若无有效记录则返回 Kconfig 默认值。 |

## 11. 配置项说明

| 配置项 | 默认值与说明 |
| --- | --- |
| Server / Client Kconfig | `CONFIG_SAMPLE_SUPPORT_SLE_RSSI_RANGING_SERVER_SAMPLE` / `..._CLIENT_SAMPLE`。 |
| `CONFIG_SLE_RSSI_RANGING_RSSI_AT_1M` | `-45 dBm`，无有效 NV 时的 A。 |
| `CONFIG_SLE_RSSI_RANGING_PATH_LOSS_TENTHS` | `20`，即路径损耗指数 `n=2.0`。 |
| S1 | `S_MGPIO6`，高电平按下，`PIN_PULL_NONE`。 |
| 校准 | 31 点、200 ms/点，采集约 6.2 秒；长按判定约 2 秒。 |
| 分区 | `near ≤ 150 cm`；`150 < middle ≤ 500 cm`；`far > 500 cm`。 |
| NV | ID `0x5101`，带 Magic、版本和校验值。 |

## 12. 使用方法

### 环境准备

- 两块 WS53 开发板和两个调试串口，无需外接按键。
- 校准时将两板天线保持固定方向，天线间距量到 100 cm。
- 可选 SK6805 的 DIN 使用 GPIO5；没有灯也可完全依靠串口完成校准。

### 编译

```powershell
fbb config set CONFIG_SAMPLE_SUPPORT_SLE_RSSI_RANGING_SERVER_SAMPLE=y --target ws53_liteos_app
fbb build ws53_liteos_app --clean
fbb flash ws53_liteos_app --port <SERVER_COM> --json-summary

fbb config set CONFIG_SAMPLE_SUPPORT_SLE_RSSI_RANGING_CLIENT_SAMPLE=y --target ws53_liteos_app
fbb build ws53_liteos_app --clean
fbb flash ws53_liteos_app --port <CLIENT_COM> --json-summary
```

先烧录 Server，再切换 Client。固件位于 `output/ws53/fwpkg/ws53_liteos_app/ws53_liteos_app_all.fwpkg`。

### 运行

建链后先观察正常测距。需要校准时将距离固定为 100 cm，长按 Client 的 S1 约 2 秒后松开，等待 31 点采集完成；随后复位 Client 检查 NV 加载日志。

### 运行结果

校准完成显示 `nv=ok`，重启后显示相同 A 的 `NV calibration loaded`，并持续输出距离和分区即通过。

## 13. 输入输出示例

### 输入

Client 板载 S1（MIO06）长按约 2 秒；无需串口命令。

### 输出

```text
[sle rssi cal] long press detected, calibration start: distance=100 cm, samples=31
[sle rssi cal] calibration complete: A=-46 dBm, MAD=1 dB, range=[-56,-44] dBm, samples=31, nv=ok
[sle rssi cal] NV calibration loaded: A=-46 dBm, MAD=1 dB, range=[-56,-44] dBm, samples=31
[sle rssi client] range: raw=<rssi> dBm, median=<median> dBm, filtered=<filtered> dBm, samples=7, distance=89 cm, zone=near
```

验证结论：S1、31 点校准、NV 持久化和 100 cm 测距已通过；可选 SK6805 灯效未实物验证。
