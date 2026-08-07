# WS53 SLE Sensor Report 接入真实温湿度传感器设计

状态：已批准（用户于 2026-08-07 确认直接实施）
目标芯片/构建目标：WS53 / `ws53_liteos_app`  
本轮硬件：WS53（COM8）  
日期：2026-08-07

## 1. 目标与边界

在已移植的 `sle_sensor_report` Server 中接入用户已连接的四线 I2C 组合模块。用户已确认模块型号为 **AHT20 + BMP280**（此前的“AHD20”为笔误）；软件仍通过上板探测和状态读取确认器件响应，避免在错误地址或不兼容器件上继续读写。

本轮交付目标：

- COM8 上的 WS53 读取真实温度、相对湿度。
- 保留现有 SLE Server/Client、1 秒周期和 packed 数据帧（实际 11 字节），避免破坏既有 Client。
- Server 通过 SLE Notification 将真实温湿度发送给另一块 WS53 Client。
- 传感器不可用时输出明确错误并重试，不发送模拟数据。

本轮不包含：

- BMP280 的气压上报和补偿算法；BMP280 只参与 I2C 存在性探测。
- 光照采集。原帧的 `light` 字段为兼容保留，固定为 `0`，含义为“未提供”。
- 供电电压、极性和电源接线判定。VCC/GND 已由用户连接并负责依据模块/板卡资料确认。
- 生产级校准、长期漂移补偿和环境认证。

## 2. 已确认接线与板卡映射

| 信号 | 用户实际接线 | WS53 SDK 内部引脚号 | 复用模式 | 用途 |
|---|---:|---:|---:|---|
| SCL | GPIO21 | 47（`S_MGPIO21`） | 3 | I2C0 SCL |
| SDA | GPIO22 | 22（`S_MGPIO22`） | 3 | I2C0 SDA |
| VCC | 用户已连接 | 不在软件设计中判定 | - | 由用户按硬件资料确认 |
| GND | 用户已连接 | 不在软件设计中判定 | - | 共地，由用户确认 |

映射依据：WS53 `platform_core.h` 中 `S_MGPIO21 = 47`、`S_MGPIO22 = 22`；SDK 的 I2C Master 样例默认也使用 SCL=47、SDA=22、mode=3。

I2C 参数：

- 总线：I2C0。
- 初始速率：100 kHz，优先保证模块识别和首轮验证稳定。
- 地址制式：7 位地址。
- 引脚输入使能仅在 SDK 的 `CONFIG_PINCTRL_SUPPORT_IE` 可用时调用，与原 I2C 样例一致。

## 3. 样例锚点与复用关系

| 锚点 | 直接复用 | 本项目新增/改变 |
|---|---|---|
| `application/samples/bt/sle/sle_sensor_report` | SLE 广播、连接/配对、SSAP 服务、1 秒定时、现有 packed 帧、Client 解析 | 将 Server 的模拟温湿度源替换为硬件采集源 |
| `application/samples/peripheral/i2c/i2c_master_demo.c` | `uapi_pin_set_mode()`、`uapi_i2c_master_init()`、`uapi_i2c_master_write/read/writeread()` 的调用方式 | 增加传感器协议、状态校验、测量等待和数据换算 |

WS53 当前 `ws53_liteos_app` 基础配置已启用 `CONFIG_I2C_SUPPORT_MASTER=y`，不需要同时选中互斥的外围 I2C 样例。

外部协议依据：

- 奥松官方产品页确认 AHT20 是标准 I2C 数字温湿度芯片：<https://www.aosong.com/en/Products/info.aspx?itemid=2284>
- AHT20 兼容协议流程参考 Zephyr 的 Aosong DHT20 驱动：<https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/aosong/dht20/dht20.c>
- BMP280 识别依据 Bosch 官方数据手册：<https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf>

说明：用户已确认模块型号为 AHT20 + BMP280；上板身份门槛仍会验证实际响应，失败时不会把任意响应设备当作 AHT20 使用。

## 4. 软件结构

计划在现有 Server 子目录中增加独立硬件适配层：

```text
sle_sensor_report/
└─ sle_sensor_report_server/
   ├─ CMakeLists.txt                         # 纳入新增源文件
   └─ src/
      ├─ sle_sensor_report_server.c          # 调用硬件采集，打包并上报
      ├─ sle_sensor_report_server.h          # 保持现有空口帧定义
      ├─ sensor_aht20.c                      # I2C、识别、测量、换算、错误恢复
      └─ sensor_aht20.h                      # init/read 接口和测量结构
```

硬件适配层对 SLE 层只暴露：

```c
errcode_t sensor_aht20_init(void);
errcode_t sensor_aht20_read(int16_t *temperature_x100,
                            uint8_t *humidity_percent);
```

职责边界：

- `sensor_aht20.c`：配置 GPIO21/22、初始化 I2C0、探测预期设备、执行 AHT20 兼容初始化/测量、检查忙状态与 CRC（响应包含 CRC 时）、定点换算、记录硬件状态。
- `sle_sensor_report_server.c`：维持连接和定时器状态；成功读数后填帧并发送；失败则记录并在下一周期重试。
- Client：空口帧不变，无需协议改造；当前 packed 结构为 11 字节（`1+1+4+2+1+2`），继续使用 `sizeof(sensor_data_frame_t)`；只调整输出文字，使 `light=0` 明确显示为未提供，避免误读为 0 lux 的真实测量。

## 5. 启动与运行流程

```text
COM8 上电/复位
  -> GPIO21/22 配置为 I2C0 mode 3
  -> I2C0 以 100 kHz 初始化
  -> 探测 AHT20 兼容器件并读取状态
     -> 兼容：完成初始化，标记 hardware ready
     -> 不兼容/无响应：保留 SLE 广播，但标记 sensor unavailable
  -> 启动原有 SLE Server、广播 sensor_server
  -> Server 工作任务每 1 秒采集并打印一次真实温湿度
     -> 此阶段不依赖 Client，可先完成 COM8 单板验证
  -> Client 连接并配对
  -> 后续每次采集：
       触发测量 -> 等待完成 -> 读取并校验 -> 定点换算
       成功：填入真实 temp/humidity，light=0；已配对时发送 SLE 帧
       失败：不发送该帧，打印错误，下一周期重新探测/初始化后重试
```

重要行为：

- 不保留 `get_simulated_temperature()`、`get_simulated_humidity()`、`get_simulated_light()` 的运行时回退路径。
- `sensor_count` 从 3 改为 2，表示本帧只有温度和湿度两项有效；现有 11 字节 packed 布局不变。
- 温度仍用 `int16_t` 的摄氏度 ×100；湿度仍用 0～100 的整数百分比。
- 原温度高/低阈值与 Notification/Indication 分流逻辑保留。室温条件下通常只会看到普通 Notification。
- I2C 事务不直接长期占用 SLE 回调；传感器读数在 Server 工作上下文中串行执行，并限制单次等待时长。

## 6. 身份门槛和异常策略

首次初始化必须满足以下条件才能进入 `ready`：

1. 目标地址有 ACK。
2. AHT20 兼容状态读取成功，状态位符合兼容协议预期；必要时执行兼容初始化序列后复查。
3. 首次测量在限时内结束，原始温湿度数据可解析，CRC（若模块返回）正确。
4. 换算后数值位于传感器物理范围内。

BMP280 仅用于辅助确认组合板存在：若探测到其标准 I2C 地址并读到正确芯片 ID，打印 `bmp280 detected (pressure disabled)`；探测不到不会阻止 AHT20 温湿度功能。

错误处理：

- 初始化失败：打印阶段、地址和 SDK 错误码；SLE Server 仍可启动，便于串口观察和后续热恢复。
- 采集失败：丢弃本周期，不沿用旧值，不构造模拟值。
- 连续失败：按 1 秒周期重新初始化，但日志做计数/节流，避免刷屏淹没 SLE 日志。
- 恢复成功：打印一次 `sensor recovered`，随后恢复上报。

## 7. 可观察日志

COM8 Server 至少提供以下稳定关键字：

```text
[sensor hw] i2c ready: bus=0, scl=GPIO21, sda=GPIO22, rate=100000
[sensor hw] aht20 compatible device ready
[sensor hw] bmp280 detected (pressure disabled)        # 仅实际探测到时出现
[sensor server] source=hardware temp=xx.xxC hum=xx% light=N/A
[sensor hw] read failed: stage=..., err=0x...           # 仅失败时出现
[sensor hw] sensor recovered                            # 故障恢复时出现
```

Client 日志显示收到的温湿度，并把光照显示为 `light=N/A`。

## 8. 构建、烧录与上板验证

板卡分工：

- COM8：WS53，真实传感器 Server，GPIO21/22 已接线。
- COM7 或 COM9：WS53，现有 `sle_sensor_report` Client；优先选择空闲端口。

执行门槛：用户批准本设计后，才修改产品源文件、配置、构建和烧录。

验收步骤：

1. 构建硬件版 Server，烧录 COM8，复位后确认 I2C 初始化日志。
2. 确认 AHT20 兼容身份门槛通过；若组合板含可识别 BMP280，同时记录其探测日志。
3. 先单板观察 COM8，连续取得至少 10 组真实温湿度；日志必须含 `source=hardware`，不得出现模拟数据生成路径。
4. 构建 Client，烧录 COM7 或 COM9，确认与 COM8 连接、配对、服务发现成功。
5. 对比两端至少 10 帧：温度和湿度一致，周期约 1 秒，Client 显示 `light=N/A`。
6. 用手靠近或对传感器呼气造成温湿度变化，确认 Server 与 Client 的变化方向同步，以排除固定值/模拟值。
7. 在用户负责安全断电和重新接线的前提下验证一次传感器不可用与恢复：不可用期间无伪造帧，恢复后自动继续上报。

通过标准：

- Server/Client 均完成构建、烧录和串口证据留存。
- COM8 识别到兼容温湿度器件并连续产生合理、可随环境变化的真实读数。
- SLE Client 收到与 Server 一致的数据。
- 断连、读失败不会崩溃；无模拟值回退。

## 9. 风险与回退

- **器件响应风险**：型号已确认为 AHT20 + BMP280，但接线、模块版本或总线状态仍可能导致响应与预期不符。身份门槛将以实测响应决定；若不兼容，停止传感器数据上报并报告原始探测证据，不盲写寄存器。
- **模块电气风险**：模块板是否带 I2C 上拉、实际供电适用范围未知。软件不能替代硬件资料确认；若总线无 ACK 或持续忙，优先保留日志，用户核对模块资料和接线。
- **定时上下文风险**：现实现从 OS 定时器回调打包发送。实现时若 I2C 读取可能阻塞，将把采集/发送移入专用工作任务，定时器只发信号，避免阻塞系统定时器上下文。
- **兼容风险**：空口帧布局保持不变，因此现有 Client 可继续解析；原文档曾误写为 12 字节，按 packed 字段求和实际为 11 字节。本次不添加填充字节，`sensor_count=2` 和 `light=0/N/A` 是唯一语义变化。

回退仅指软件回退：恢复原来的纯模拟 `sle_sensor_report` 版本。不会在硬件驱动失败时自动切换到模拟数据，因为那会掩盖传感器故障。

## 10. 设计批准点

批准此设计即表示同意以下实现范围：

- COM8 为真实传感器 Server；GPIO21=SCL、GPIO22=SDA。
- 本轮只上报 AHT20 兼容温度/湿度；BMP280 气压以后再扩展。
- 保持现有 11 字节 packed SLE 帧；`sensor_count=2`，`light=0/N/A`。
- 模块不兼容或读取失败时不伪造数据，以串口证据作为诊断结果。

## 11. 实施与首次上板记录

执行日期：2026-08-07

- 实施前 Git 回退基线：`d5d5b16 feat: port WS63 SLE samples to WS53`。
- AHT20 硬件适配、Server 工作任务、SLE 帧兼容和诊断日志已完成独立代码复核，无硬件安全阻断项。
- `ws53_liteos_app` Sensor Report Server 构建成功；`sensor_aht20.c.obj` 已确认进入构建，目标配置包含 `CONFIG_SAMPLE_SUPPORT_SLE_SENSOR_REPORT_SERVER_SAMPLE=1` 和 `CONFIG_I2C_SUPPORT_MASTER=1`。
- 构建期间仍会出现仓库既有的 flashboot `libm.a: file format not recognized`，但应用目标完成编译、链接、签名和打包，最终 `fbb` 退出码为 0。
- Server 固件已通过 `hsflash` 成功烧录 COM8，写入 5 个分区。
- COM8 可正常启动 SLE Server、注册服务并广播 `sensor_server`，证明新固件正在运行。
- 首次传感器验证未通过：BMP280 地址 `0x76`、`0x77` 读取芯片 ID 均返回 `0x80001313`；AHT20 地址 `0x38` 在发送状态命令阶段返回同一超时错误，尚未进入状态读取、CRC 或数据换算。
- 引脚只读诊断确认 MIO21/MIO22 均已配置为 mode 3，但默认无内部上拉（`pull=0`）。根据 WS53 I2C 硬件设计要求，软件随后启用两根线的内部弱上拉；这不会把引脚切换为推挽 GPIO 输出。
- 启用内部弱上拉后，AHT20 首个状态命令由超时 `0x80001313` 变为发送异常 `0x80001311`。对照 WS53 驱动实现，后者来自 `TX_ABRT`，表示总线事务已经能够结束，但地址 `0x38` 没有从设备应答。
- 当前判断：I2C0 控制器与 MIO21/MIO22 mode 3 软件映射有效，剩余故障集中在外部设备响应路径。板卡资料显示 MIO21/SCL 与 MIO22/SDA 可能分别位于接插件位置 36 和 5；需要依据实际板卡丝印确认没有把“排针位置 21/22”误认为“MIO21/MIO22”，并确认模块供电、共地。软件保留每秒重试，外部连接恢复后无需重刷即可继续串口验证。
- 用户确认实际接线为：SCL 接排针位置 36（MIO21），SDA 接排针位置 5（MIO22），3.3V 接模块 VDD，GND 接 GND。
- 加入启动阶段的输入态采样与内部弱上拉后，COM8 AHT20 恢复应答并连续输出真实硬件数据；已捕获 13 组连续样本，温度从 `30.89C` 变化到 `31.27C`，湿度从 `57%` 变化到 `59%`，日志均为 `source=hardware`。AHT20 单板验收通过。
- Sensor Report Client 已完成 clean 构建并成功烧录 COM9。准备执行 SLE 端到端验证时，COM8 打开失败，随后系统枚举仅剩 COM1/COM2/COM3，原 COM5/COM7/COM8/COM9 四个 USB 串口均已掉线；端到端验证等待 USB 设备重新枚举后继续。
- 用户随后确认当时线路连接不稳定，因此上述 13 组数据仅保留为诊断记录，不再作为正式验收证据。代码已回退到最初 AHT20 实现：保留 AHT20 协议、CRC、真实数据上报和分阶段错误日志，撤销临时 GPIO 输入采样、内部弱上拉及总线电平日志。
- 回退版 Sensor Report Server 已重新选择并完成 clean 构建，`CONFIG_SAMPLE_SUPPORT_SLE_SENSOR_REPORT_SERVER_SAMPLE=1`，固件包已生成；等待 COM8 重新枚举后，从重新烧录开始重做单板连续采样和双板 SLE 验证。
- USB 设备恢复后，PnP 与 pyserial 均重新枚举到 COM5/COM7/COM8/COM9；`Win32_SerialPort` 当时仍只有 COM1/COM2/COM3，确认是 WMI 枚举滞后而非板卡再次掉线。
- 回退版 Server 已重新烧录 COM8。未使用 GPIO 输入采样或内部弱上拉辅助时，15 秒内连续取得 13 组 `source=hardware` 数据：温度 `23.56~23.61C`、湿度 `67%`，无 I2C 错误；AHT20 单板复测通过。
- Client 已重新 clean 构建并烧录 COM9。首帧为 `temp=22.34C, hum=66%, light=N/A, type=0x01`；随后 13 秒内连续收到 11 帧，温度 `22.22~22.27C`、湿度 `66%`。同期 COM8 Server 抽查值为 `22.14C / 66%`，Server/Client 数据一致，SLE 端到端复测通过。
