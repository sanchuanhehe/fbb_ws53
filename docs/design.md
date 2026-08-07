# WS53 SLE Sensor Report 接入真实温湿度传感器设计

状态：待用户批准  
目标芯片/构建目标：WS53 / `ws53_liteos_app`  
本轮硬件：WS53（COM8）  
日期：2026-08-07

## 1. 目标与边界

在已移植的 `sle_sensor_report` Server 中接入用户已连接的四线 I2C 组合模块。用户已确认模块型号为 **AHT20 + BMP280**（此前的“AHD20”为笔误）；软件仍通过上板探测和状态读取确认器件响应，避免在错误地址或不兼容器件上继续读写。

本轮交付目标：

- COM8 上的 WS53 读取真实温度、相对湿度。
- 保留现有 SLE Server/Client、1 秒周期和 12 字节数据帧，避免破坏既有 Client。
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
| `application/samples/bt/sle/sle_sensor_report` | SLE 广播、连接/配对、SSAP 服务、1 秒定时、12 字节帧、Client 解析 | 将 Server 的模拟温湿度源替换为硬件采集源 |
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
- Client：空口帧不变，无需协议改造；只调整输出文字，使 `light=0` 明确显示为未提供，避免误读为 0 lux 的真实测量。

## 5. 启动与运行流程

```text
COM8 上电/复位
  -> GPIO21/22 配置为 I2C0 mode 3
  -> I2C0 以 100 kHz 初始化
  -> 探测 AHT20 兼容器件并读取状态
     -> 兼容：完成初始化，标记 hardware ready
     -> 不兼容/无响应：保留 SLE 广播，但标记 sensor unavailable
  -> 启动原有 SLE Server、广播 sensor_server
  -> Client 连接并配对
  -> 每 1 秒：
       触发测量 -> 等待完成 -> 读取并校验 -> 定点换算
       成功：填入真实 temp/humidity，light=0，发送 SLE 帧
       失败：不发送该帧，打印错误，下一周期重新探测/初始化后重试
```

重要行为：

- 不保留 `get_simulated_temperature()`、`get_simulated_humidity()`、`get_simulated_light()` 的运行时回退路径。
- `sensor_count` 从 3 改为 2，表示本帧只有温度和湿度两项有效；12 字节布局不变。
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
- **兼容风险**：空口帧布局保持不变，因此现有 Client 可继续解析；`sensor_count=2` 和 `light=0/N/A` 是本次唯一语义变化。

回退仅指软件回退：恢复原来的纯模拟 `sle_sensor_report` 版本。不会在硬件驱动失败时自动切换到模拟数据，因为那会掩盖传感器故障。

## 10. 设计批准点

批准此设计即表示同意以下实现范围：

- COM8 为真实传感器 Server；GPIO21=SCL、GPIO22=SDA。
- 本轮只上报 AHT20 兼容温度/湿度；BMP280 气压以后再扩展。
- 保持 12 字节 SLE 帧；`sensor_count=2`，`light=0/N/A`。
- 模块不兼容或读取失败时不伪造数据，以串口证据作为诊断结果。
