# PWM

PWM（Pulse Width Modulation）提供脉冲宽度调制信号的生成与管理功能，支持多通道配置、占空比与周期设置、通道分组以及完成中断回调，并支持低功耗场景下的挂起与恢复。

**模块公共头文件**

```c
#include "include/driver/pwm.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_pwm_init](#uapi_pwm_init) | 初始化 PWM 驱动，注册 HAL（Hardware Abstraction Layer）函数表并使能时钟 |
| [uapi_pwm_deinit](#uapi_pwm_deinit) | 反初始化 PWM 驱动，关闭已打开通道并注销 HAL 函数表 |
| [uapi_pwm_open](#uapi_pwm_open) | 以指定配置打开一个 PWM 通道 |
| [uapi_pwm_close](#uapi_pwm_close) | 关闭指定 PWM 通道并注销其中断回调 |
| [uapi_pwm_start](#uapi_pwm_start) | 启动指定 PWM 通道输出 |
| [uapi_pwm_get_frequency](#uapi_pwm_get_frequency) | 获取指定 PWM 通道的工作频率 |
| [uapi_pwm_stop](#uapi_pwm_stop) | 停止正在运行的 PWM 通道输出 |
| [uapi_pwm_update_duty_ratio](#uapi_pwm_update_duty_ratio) | 在已打开的 PWM 通道上更新占空比 |
| [uapi_pwm_isr](#uapi_pwm_isr) | PWM 中断服务例程，清除指定通道的中断标志 |
| [uapi_pwm_register_interrupt](#uapi_pwm_register_interrupt) | 为指定 PWM 通道注册完成中断回调 |
| [uapi_pwm_unregister_interrupt](#uapi_pwm_unregister_interrupt) | 注销指定 PWM 通道的完成中断回调 |
| [uapi_pwm_set_group](#uapi_pwm_set_group) | 将多个 PWM 通道归入同一分组 |
| [uapi_pwm_clear_group](#uapi_pwm_clear_group) | 清空指定分组中的 PWM 通道成员 |
| [uapi_pwm_start_group](#uapi_pwm_start_group) | 启动指定分组中的全部 PWM 通道 |
| [uapi_pwm_stop_group](#uapi_pwm_stop_group) | 停止指定分组中的全部 PWM 通道 |
| [uapi_pwm_update_cfg](#uapi_pwm_update_cfg) | 更新指定 PWM 通道的配置参数 |
| [uapi_pwm_config_preload](#uapi_pwm_config_preload) | 为指定通道配置预加载参数 |
| [uapi_pwm_suspend](#uapi_pwm_suspend) | 挂起 PWM 驱动，进入低功耗准备状态 |
| [uapi_pwm_resume](#uapi_pwm_resume) | 恢复 PWM 驱动并重建挂起前的通道配置 |

## Functions

### uapi_pwm_init <a id="uapi_pwm_init"></a>

```c
errcode_t uapi_pwm_init(void)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 初始化 PWM 驱动模块。
- 已初始化时重复调用直接返回成功，不重复执行初始化动作。
- 成功初始化后本模块其他接口方可使用。

**前置条件**

- 调用时序约束：作为 PWM 驱动的入口，使用其他 PWM 接口前必须先调用本接口。
- 依赖关系：依赖目标芯片 porting 层已提供 `pwm_port_register_hal_funcs` 与底层 HAL 初始化实现。

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 驱动已初始化或本次初始化成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层 HAL 初始化返回失败 |

**参考案例**

- `src/application/samples/peripheral/pwm/pwm_demo.c`

### uapi_pwm_deinit <a id="uapi_pwm_deinit"></a>

```c
void uapi_pwm_deinit(void)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 反初始化 PWM 驱动模块，关闭所有已打开的通道。
- 注销 HAL 函数表并关闭 PWM 外设时钟。
- 未初始化时调用直接返回，不执行任何动作。

**前置条件**

- 调用时序约束：应在 `uapi_pwm_init` 成功返回之后调用。
- 依赖关系：内部会逐一调用 `uapi_pwm_close` 关闭已打开通道，依赖该接口可用。

**参考案例**

- `src/application/samples/peripheral/pwm/pwm_demo.c`

### uapi_pwm_open <a id="uapi_pwm_open"></a>

```c
errcode_t uapi_pwm_open(uint8_t channel, const pwm_config_t *cfg)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 以指定配置打开并初始化一个 PWM 通道，设置低/高电平时间、相位偏移、重复周期与连续输出标志。
- 通道已打开时先关闭再按新配置重新打开。
- 注册默认中断回调 `uapi_pwm_isr`，用于响应通道完成中断。

**前置条件**

- 调用时序约束：必须在 `uapi_pwm_init` 成功返回后调用。
- 依赖关系：依赖底层 HAL 已提供 `set_time`、`set_cycles`、`set_action`、`registerfunc` 实现。
- 上下文限制：内部通过关中断保护配置过程，可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | 待打开的 PWM 通道号 | 0 ~ CONFIG_PWM_CHANNEL_NUM-1 |
| cfg | const [pwm_config_t](#struct_pwm_config) * | 指向 PWM 通道配置参数的指针，包含低/高电平时间、相位偏移、重复周期与连续输出标志 | 不为 NULL；cycles 取值 0 ~ 32767；low_time + high_time 与 offset_time 需满足 porting 层 `pwm_port_param_check` 校验 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 通道配置写入并打开成功 |
| ERRCODE_PWM_INVALID_PARAMETER：0x80001082 | 参数无效 | channel 超出有效范围、cfg->cycles 大于最大值或 porting 层参数校验失败 |
| ERRCODE_PWM_NOT_INIT：0x80001080 | 驱动未初始化 | 未先调用 `uapi_pwm_init` |

**参考案例**

- `src/application/samples/peripheral/pwm/pwm_demo.c`

### uapi_pwm_close <a id="uapi_pwm_close"></a>

```c
errcode_t uapi_pwm_close(uint8_t channel)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 关闭指定 PWM 通道，停止其信号输出。
- 注销该通道的完成中断回调并标记通道为未打开状态。
- 按通道所属分组执行停止动作，避免影响同组其他通道（仅 V151）。

**前置条件**

- 调用时序约束：必须在 `uapi_pwm_init` 成功返回且目标通道已通过 `uapi_pwm_open` 打开后调用。
- 依赖关系：依赖底层 HAL 已提供 `set_action`、`set_group`（V151）实现。
- 上下文限制：内部通过关中断保护停止动作，可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | 待关闭的 PWM 通道号 | 0 ~ CONFIG_PWM_CHANNEL_NUM-1 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 通道关闭成功 |
| ERRCODE_PWM_INVALID_PARAMETER：0x80001082 | 参数无效 | channel 超出有效范围或该通道未归属任何分组（V151） |
| ERRCODE_PWM_NOT_INIT：0x80001080 | 驱动未初始化 | 未先调用 `uapi_pwm_init` |
| ERRCODE_PWM_NOT_OPEN：0x80001081 | 通道未打开 | 目标通道尚未通过 `uapi_pwm_open` 打开 |

**参考案例**

- `src/application/samples/peripheral/pwm/pwm_demo.c`

### uapi_pwm_start <a id="uapi_pwm_start"></a>

```c
errcode_t uapi_pwm_start(uint8_t channel)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 启动指定 PWM 通道的信号输出。
- V151 实现下通过通道所属分组下发启动动作，保证分组内通道同步控制。
- 仅触发启动动作，不修改已配置的占空比与周期参数。

**前置条件**

- 调用时序约束：必须在 `uapi_pwm_init` 成功返回且目标通道已通过 `uapi_pwm_open` 配置后调用。
- 依赖关系：V151 实现下要求通道已通过 `uapi_pwm_set_group` 归入某个分组。
- 上下文限制：内部通过关中断保护启动动作，可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | 待启动的 PWM 通道号 | 0 ~ CONFIG_PWM_CHANNEL_NUM-1 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 通道启动成功 |
| ERRCODE_PWM_INVALID_PARAMETER：0x80001082 | 参数无效 | channel 超出有效范围或该通道未归属任何分组（V151） |
| ERRCODE_PWM_NOT_INIT：0x80001080 | 驱动未初始化 | 未先调用 `uapi_pwm_init` |
| ERRCODE_PWM_NOT_OPEN：0x80001081 | 通道未打开 | 目标通道尚未通过 `uapi_pwm_open` 打开 |

**参考案例**

- `src/application/samples/peripheral/pwm/pwm_demo.c`

### uapi_pwm_get_frequency <a id="uapi_pwm_get_frequency"></a>

```c
uint32_t uapi_pwm_get_frequency(uint8_t channel)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 获取指定 PWM 通道的工作频率，返回值单位为 Hz。
- 用于结合 `pwm_config_t` 中的时钟周期计数换算实际高低电平时间。
- 仅读取 porting 层时钟配置，不修改任何硬件状态。

**前置条件**

- 调用时序约束：建议在 `uapi_pwm_init` 之后调用，以确保时钟已使能。
- 依赖关系：依赖目标芯片 porting 层提供的 `pwm_port_get_clock_value` 实现。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | 待查询工作频率的 PWM 通道号 | 0 ~ CONFIG_PWM_CHANNEL_NUM-1 |

**返回值**

- 返回类型：uint32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| uint32_t | PWM 工作频率，单位 Hz | 任意调用均返回 porting 层查询到的时钟值 |

### uapi_pwm_stop <a id="uapi_pwm_stop"></a>

```c
errcode_t uapi_pwm_stop(uint8_t channel)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 停止指定 PWM 通道的信号输出。
- 仅对 V150 HAL 实现可用，V151 通过分组接口停止通道。
- 仅触发停止动作，不关闭通道、不注销中断回调。

**前置条件**

- 调用时序约束：必须在 `uapi_pwm_init` 成功返回且目标通道已打开并启动后调用。
- 依赖关系：依赖底层 HAL（V150）已提供 `set_action` 实现。
- 上下文限制：内部通过关中断保护停止动作，可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | 待停止的 PWM 通道号 | 0 ~ CONFIG_PWM_CHANNEL_NUM-1 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 通道停止成功 |
| ERRCODE_PWM_INVALID_PARAMETER：0x80001082 | 参数无效 | channel 超出有效范围 |
| ERRCODE_PWM_NOT_INIT：0x80001080 | 驱动未初始化 | 未先调用 `uapi_pwm_init` |
| ERRCODE_PWM_NOT_OPEN：0x80001081 | 通道未打开 | 目标通道尚未通过 `uapi_pwm_open` 打开 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PWM_USING_V150 | 特性宏 | 支持 PWM V150 停止通道功能（接口级） | y |

### uapi_pwm_update_duty_ratio <a id="uapi_pwm_update_duty_ratio"></a>

```c
errcode_t uapi_pwm_update_duty_ratio(uint8_t channel, uint32_t low_time, uint32_t high_time)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 在已打开的 PWM 通道上更新低电平与高电平的时钟周期计数，调整占空比。
- 写入后触发刷新动作使新配置立即生效。
- 仅对 V150 HAL 实现可用，V151 通过 `uapi_pwm_update_cfg` 更新配置。

**前置条件**

- 调用时序约束：必须在 `uapi_pwm_init` 成功返回且目标通道已通过 `uapi_pwm_open` 打开后调用。
- 依赖关系：依赖底层 HAL（V150）已提供 `set_time`、`set_action` 实现。
- 上下文限制：内部通过关中断保护更新过程，可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | 待更新占空比的 PWM 通道号 | 0 ~ CONFIG_PWM_CHANNEL_NUM-1 |
| low_time | uint32_t | 低电平部分的时钟周期计数个数，实际低电平时间 = low_time × PWM 工作周期 | 受 porting 层时钟位宽限制 |
| high_time | uint32_t | 高电平部分的时钟周期计数个数，实际高电平时间 = high_time × PWM 工作周期 | 受 porting 层时钟位宽限制 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 占空比更新成功 |
| ERRCODE_PWM_INVALID_PARAMETER：0x80001082 | 参数无效 | channel 超出有效范围 |
| ERRCODE_PWM_NOT_INIT：0x80001080 | 驱动未初始化 | 未先调用 `uapi_pwm_init` |
| ERRCODE_PWM_NOT_OPEN：0x80001081 | 通道未打开 | 目标通道尚未通过 `uapi_pwm_open` 打开 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PWM_USING_V150 | 特性宏 | 支持 PWM V150 占空比更新功能（接口级） | y |

### uapi_pwm_isr <a id="uapi_pwm_isr"></a>

```c
errcode_t uapi_pwm_isr(uint8_t channel)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- PWM 中断服务例程，清除指定通道的中断标志。
- 作为 `uapi_pwm_open` 时注册的默认回调，在通道完成中断触发时被调用。
- 也可由上层在中断处理流程中直接调用以清除中断。

**前置条件**

- 调用时序约束：依赖底层 HAL 已通过 `uapi_pwm_open` 或 `uapi_pwm_register_interrupt` 注册回调。
- 上下文限制：设计用于中断上下文调用，内部通过关中断保护清除动作。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | 待清除中断的 PWM 通道号 | 0 ~ CONFIG_PWM_CHANNEL_NUM-1 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 中断标志成功清除 |
| ERRCODE_PWM_INVALID_PARAMETER：0x80001082 | 参数无效 | channel 超出有效范围 |

### uapi_pwm_register_interrupt <a id="uapi_pwm_register_interrupt"></a>

```c
errcode_t uapi_pwm_register_interrupt(uint8_t channel, pwm_callback_t callback)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 为指定 PWM 通道注册完成中断回调函数。
- 注册时同步在 porting 层注册中断并覆盖 `uapi_pwm_open` 设置的默认回调。
- 回调在通道完成周期输出触发中断时被调用，参数为触发中断的通道号。

**前置条件**

- 调用时序约束：必须在 `uapi_pwm_init` 成功返回且目标通道已通过 `uapi_pwm_open` 打开后调用。
- 依赖关系：依赖 porting 层 `pwm_port_register_irq` 与底层 HAL `registerfunc` 实现。
- 上下文限制：建议在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | 待注册中断回调的 PWM 通道号 | 0 ~ CONFIG_PWM_CHANNEL_NUM-1 |
| callback | [pwm_callback_t](#typedef_pwm_callback_t) | 通道完成中断触发时调用的回调函数指针 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 回调注册成功 |
| ERRCODE_PWM_INVALID_PARAMETER：0x80001082 | 参数无效 | channel 超出有效范围 |
| ERRCODE_PWM_NOT_INIT：0x80001080 | 驱动未初始化 | 未先调用 `uapi_pwm_init` |
| ERRCODE_PWM_NOT_OPEN：0x80001081 | 通道未打开 | 目标通道尚未通过 `uapi_pwm_open` 打开 |

**参考案例**

- `src/application/samples/peripheral/pwm/pwm_demo.c`

### uapi_pwm_unregister_interrupt <a id="uapi_pwm_unregister_interrupt"></a>

```c
errcode_t uapi_pwm_unregister_interrupt(uint8_t channel)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 注销指定 PWM 通道已注册的完成中断回调。
- 同步在 porting 层注销中断并清除底层 HAL 回调注册。
- 在 `uapi_pwm_close` 内部会自动调用本接口完成回调清理。

**前置条件**

- 调用时序约束：必须在 `uapi_pwm_init` 成功返回且目标通道已通过 `uapi_pwm_open` 打开后调用。
- 依赖关系：依赖 porting 层 `pwm_port_unregister_irq` 与底层 HAL `unregisterfunc` 实现。
- 上下文限制：建议在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | 待注销中断回调的 PWM 通道号 | 0 ~ CONFIG_PWM_CHANNEL_NUM-1 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 回调注销成功 |
| ERRCODE_PWM_INVALID_PARAMETER：0x80001082 | 参数无效 | channel 超出有效范围 |
| ERRCODE_PWM_NOT_INIT：0x80001080 | 驱动未初始化 | 未先调用 `uapi_pwm_init` |
| ERRCODE_PWM_NOT_OPEN：0x80001081 | 通道未打开 | 目标通道尚未通过 `uapi_pwm_open` 打开 |

### uapi_pwm_set_group <a id="uapi_pwm_set_group"></a>

```c
errcode_t uapi_pwm_set_group(uint8_t group, const uint8_t *channel_set, uint32_t channel_set_len)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 将一个或多个 PWM 通道归入同一分组，便于按组统一启停控制。
- 同一通道不可同时归属多个分组，归入前会校验是否已存在于其他分组。
- 仅对 V151 HAL 实现可用。

**前置条件**

- 调用时序约束：在 `uapi_pwm_open` 配置通道后、`uapi_pwm_start_group` 启动分组前调用。
- 依赖关系：依赖底层 HAL（V151）已提供 `set_group` 实现。
- 上下文限制：内部通过关中断保护分组写入，可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| group | uint8_t | 目标分组 ID | 0 ~ CONFIG_PWM_GROUP_NUM-1 |
| channel_set | const uint8_t * | 指向待归入分组的通道号集合的指针 | 不为 NULL |
| channel_set_len | uint32_t | 通道号集合的元素个数 | 大于 0 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 通道集合成功归入分组 |
| ERRCODE_PWM_INVALID_PARAMETER：0x80001082 | 参数无效 | group 超出有效范围、channel_set 为 NULL、channel_set_len 为 0 或目标通道已存在于其他分组 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PWM_USING_V151 | 特性宏 | 支持 PWM V151 通道分组功能（接口级） | y |

**参考案例**

- `src/application/samples/peripheral/pwm/pwm_demo.c`

### uapi_pwm_clear_group <a id="uapi_pwm_clear_group"></a>

```c
errcode_t uapi_pwm_clear_group(uint8_t group)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 清空指定分组中的全部 PWM 通道成员。
- 清空后该分组不再持有任何通道，可重新用于 `uapi_pwm_set_group`
- 仅对 V151 HAL 实现可用。

**前置条件**

- 调用时序约束：建议在分组内通道已停止输出后调用。
- 依赖关系：依赖底层 HAL（V151）已提供 `set_group` 实现。
- 上下文限制：内部通过关中断保护清空动作，可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| group | uint8_t | 待清空的分组 ID | 0 ~ CONFIG_PWM_GROUP_NUM-1 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 分组成员成功清空 |
| ERRCODE_PWM_INVALID_PARAMETER：0x80001082 | 参数无效 | group 超出有效范围 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PWM_USING_V151 | 特性宏 | 支持 PWM V151 清空分组功能（接口级） | y |

### uapi_pwm_start_group <a id="uapi_pwm_start_group"></a>

```c
errcode_t uapi_pwm_start_group(uint8_t group)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 启动指定分组中全部 PWM 通道的信号输出。
- 通过通道所属分组下发启动动作，保证分组内通道同步控制。
- 仅对 V151 HAL 实现可用。

**前置条件**

- 调用时序约束：必须在分组已通过 `uapi_pwm_set_group` 设置且组内通道已打开后调用。
- 依赖关系：依赖底层 HAL（V151）已提供 `set_action` 实现。
- 上下文限制：内部通过关中断保护启动动作，可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| group | uint8_t | 待启动的分组 ID | 0 ~ CONFIG_PWM_GROUP_NUM-1 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 分组内通道启动成功 |
| ERRCODE_PWM_INVALID_PARAMETER：0x80001082 | 参数无效 | group 超出有效范围 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PWM_USING_V151 | 特性宏 | 支持 PWM V151 启动分组功能（接口级） | y |

**参考案例**

- `src/application/samples/peripheral/pwm/pwm_demo.c`

### uapi_pwm_stop_group <a id="uapi_pwm_stop_group"></a>

```c
errcode_t uapi_pwm_stop_group(uint8_t group)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 停止指定分组中全部 PWM 通道的信号输出。
- 仅触发停止动作，不关闭通道、不注销回调，可重新通过 `uapi_pwm_start_group` 启动。
- 仅对 V151 HAL 实现可用。

**前置条件**

- 调用时序约束：必须在分组已启动后调用。
- 依赖关系：依赖底层 HAL（V151）已提供 `set_action` 实现。
- 上下文限制：内部通过关中断保护停止动作，可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| group | uint8_t | 待停止的分组 ID | 0 ~ CONFIG_PWM_GROUP_NUM-1 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 分组内通道停止成功 |
| ERRCODE_PWM_INVALID_PARAMETER：0x80001082 | 参数无效 | group 超出有效范围 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PWM_USING_V151 | 特性宏 | 支持 PWM V151 停止分组功能（接口级） | y |

**参考案例**

- `src/application/samples/peripheral/pwm/pwm_demo.c`

### uapi_pwm_update_cfg <a id="uapi_pwm_update_cfg"></a>

```c
errcode_t uapi_pwm_update_cfg(uint8_t channel, const pwm_config_t *cfg)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 更新指定 PWM 通道的全部配置参数，包括低/高电平时间、相位偏移、重复周期与连续输出标志。
- 写入后按通道所属分组下发刷新动作使新配置立即生效。
- 仅对 V151 HAL 实现可用。

**前置条件**

- 调用时序约束：必须在 `uapi_pwm_init` 成功返回且目标通道已通过 `uapi_pwm_open` 打开后调用。
- 依赖关系：V151 实现下要求通道已通过 `uapi_pwm_set_group` 归入某个分组；依赖底层 HAL 已提供 `set_time`、`set_cycles`、`set_action` 实现。
- 上下文限制：内部通过关中断保护更新过程，可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | 待更新配置的 PWM 通道号 | 0 ~ CONFIG_PWM_CHANNEL_NUM-1 |
| cfg | const [pwm_config_t](#struct_pwm_config) * | 指向新 PWM 通道配置参数的指针 | 不为 NULL；cycles 取值 0 ~ 32767；low_time + high_time 与 offset_time 需满足 porting 层 `pwm_port_param_check` 校验 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 通道配置更新成功 |
| ERRCODE_PWM_INVALID_PARAMETER：0x80001082 | 参数无效 | channel 超出有效范围、cfg->cycles 大于最大值或 porting 层参数校验失败 |
| ERRCODE_PWM_NOT_INIT：0x80001080 | 驱动未初始化 | 未先调用 `uapi_pwm_init` |
| ERRCODE_PWM_NOT_OPEN：0x80001081 | 通道未打开 | 目标通道尚未通过 `uapi_pwm_open` 打开 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PWM_USING_V151 | 特性宏 | 支持 PWM V151 配置更新功能（接口级） | y |

**参考案例**

- `src/application/samples/peripheral/pwm/pwm_demo.c`

### uapi_pwm_config_preload <a id="uapi_pwm_config_preload"></a>

```c
errcode_t uapi_pwm_config_preload(uint8_t group, uint8_t channel, const pwm_config_t *cfg)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 为指定分组内的通道配置预加载参数，当上一个 PWM 配置周期完成时自动加载新配置。
- 写入低/高电平时间、相位偏移、重复周期后触发分组预加载动作。
- 仅在同时启用 V151 HAL 与 PWM 预加载特性时可用。

**前置条件**

- 调用时序约束：必须在 `uapi_pwm_init` 成功返回后调用。
- 依赖关系：依赖底层 HAL（V151）已提供 `set_time`、`set_cycles`、`config_preload` 实现。
- 上下文限制：内部通过关中断保护配置过程，可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| group | uint8_t | 通道所属的分组 ID | 0 ~ CONFIG_PWM_GROUP_NUM-1 |
| channel | uint8_t | 待配置预加载参数的 PWM 通道号 | 0 ~ CONFIG_PWM_CHANNEL_NUM-1 |
| cfg | const [pwm_config_t](#struct_pwm_config) * | 指向预加载配置参数的指针 | 不为 NULL；cycles 取值 0 ~ 32767 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 预加载参数写入成功 |
| ERRCODE_PWM_INVALID_PARAMETER：0x80001082 | 参数无效 | channel 或 group 超出有效范围、cfg 为 NULL 或 cfg->cycles 大于最大值 |
| ERRCODE_PWM_NOT_INIT：0x80001080 | 驱动未初始化 | 未先调用 `uapi_pwm_init` |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PWM_USING_V151 | 特性宏 | 支持 PWM V151 接口功能（接口级，外层包裹） | y |
| CONFIG_PWM_PRELOAD | 特性宏 | 支持 PWM 预加载配置功能（接口级） | n |

### uapi_pwm_suspend <a id="uapi_pwm_suspend"></a>

```c
errcode_t uapi_pwm_suspend(uintptr_t arg)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 挂起 PWM 驱动，作为低功耗管理框架的挂起钩子。
- 当前实现忽略传入参数并直接返回成功，不修改硬件状态。
- 仅在启用 PWM 低功耗支持特性时可用。

**前置条件**

- 调用时序约束：由低功耗管理框架在进入低功耗状态前调用。
- 上下文限制：建议在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| arg | uintptr_t | 挂起所需的上下文参数，当前实现未使用 | 任意值 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 任意调用均返回成功 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PWM_SUPPORT_LPM | 特性宏 | 支持 PWM 低功耗挂起与恢复功能（接口级） | n |

**参考案例**

- `src/middleware/chips/ws53/pm/pm_sleep/pm_sleep_porting.c`

### uapi_pwm_resume <a id="uapi_pwm_resume"></a>

```c
errcode_t uapi_pwm_resume(uintptr_t arg)
```

**声明头文件**

```c
#include "include/driver/pwm.h"
```

**功能说明**

- 恢复 PWM 驱动，作为低功耗管理框架的恢复钩子。
- 按挂起前记录的配置恢复已打开的通道。
- 恢复中断注册状态与通道分组配置。
- 仅在启用 PWM 低功耗支持特性时可用。

**前置条件**

- 调用时序约束：由低功耗管理框架在退出低功耗状态后调用，且此前已调用过 `uapi_pwm_suspend`
- 上下文限制：建议在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| arg | uintptr_t | 恢复所需的上下文参数，当前实现未使用 | 任意值 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 驱动状态与通道配置恢复或驱动未成功初始化时直接返回成功 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PWM_SUPPORT_LPM | 特性宏 | 支持 PWM 低功耗挂起与恢复功能（接口级） | n |

**参考案例**

- `src/middleware/chips/ws53/pm/pm_sleep/pm_sleep_porting.c`

## Type definitions

### typedef_pwm_callback_t <a id="typedef_pwm_callback_t"></a>

```c
typedef errcode_t (*pwm_callback_t)(uint8_t channel);
```

**使用说明**

- 在 `uapi_pwm_register_interrupt` 中作为 `callback` 入参类型，用于注册 PWM 通道完成中断回调。
- 回调参数 `channel` 为触发中断的通道号，由底层中断处理流程透传。
- 回调返回 `errcode_t`，由上层注册方约定返回值语义。

### typedef_errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块返回类型为 errcode_t 的对外接口的返回值类型。

## Structures

### struct_pwm_config <a id="struct_pwm_config"></a>

```c
typedef struct pwm_config {
    uint32_t low_time;               /*!< PWM工作时钟周期计数个数低电平部分，
                                                  频率参考 @ref uapi_pwm_get_frequency()。
                                                  如果PWM工作周期为Tus, 实际低电平时间 = low_time * Tus */
    uint32_t high_time;              /*!< PWM工作时钟周期计数个数高电平部分，
                                                  频率参考 @ref uapi_pwm_get_frequency()。
                                                  如果PWM工作周期为Tus, 实际高电平时间 = high_time * Tus */
    uint32_t offset_time;            /*!< PWM相位。  */
    uint16_t cycles;                 /*!< PWM重复周期，范围：0~32767 (15bit)。  */
    bool repeat;                     /*!< 指示PWM应连续输出的标志。  */
} pwm_config_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| low_time | uint32_t | 低电平部分的时钟周期计数个数，实际低电平时间 = low_time × PWM 工作周期 |
| high_time | uint32_t | 高电平部分的时钟周期计数个数，实际高电平时间 = high_time × PWM 工作周期 |
| offset_time | uint32_t | PWM 相位偏移，porting 层校验需满足 offset_time ≤ low_time |
| cycles | uint16_t | PWM 重复周期数，取值范围 0 ~ 32767（15bit） |
| repeat | bool | 指示 PWM 是否连续输出的标志，true 表示连续输出 |

## Macros

### ERRCODE_PWM_NOT_INIT <a id="ERRCODE_PWM_NOT_INIT"></a>

```c
#define ERRCODE_PWM_NOT_INIT                                0x80001080
```

### ERRCODE_PWM_NOT_OPEN <a id="ERRCODE_PWM_NOT_OPEN"></a>

```c
#define ERRCODE_PWM_NOT_OPEN                                0x80001081
```

### ERRCODE_PWM_INVALID_PARAMETER <a id="ERRCODE_PWM_INVALID_PARAMETER"></a>

```c
#define ERRCODE_PWM_INVALID_PARAMETER                       0x80001082
```

### ERRCODE_PWM_REG_ADDR_INVALID <a id="ERRCODE_PWM_REG_ADDR_INVALID"></a>

```c
#define ERRCODE_PWM_REG_ADDR_INVALID                        0x80001083
```

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```

### ERRCODE_FAIL <a id="ERRCODE_FAIL"></a>

```c
#define ERRCODE_FAIL                                        0xFFFFFFFF
```
