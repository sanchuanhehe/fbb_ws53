# GPIO

GPIO（General-Purpose Input/Output）提供通用输入输出引脚的配置与控制功能，支持引脚方向设置、电平读写、电平翻转，以及上升沿、下降沿、双边沿、高/低电平等多种触发模式的中断注册与使能控制。支持低功耗挂起/恢复与多核选择特性。

**模块公共头文件**

```c
#include "include/driver/gpio.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_gpio_init](#uapi_gpio_init) | 初始化 GPIO 模块 |
| [uapi_gpio_deinit](#uapi_gpio_deinit) | 去初始化 GPIO 模块 |
| [uapi_gpio_set_dir](#uapi_gpio_set_dir) | 设置指定引脚的输入输出方向 |
| [uapi_gpio_get_dir](#uapi_gpio_get_dir) | 获取指定引脚的输入输出方向 |
| [uapi_gpio_set_val](#uapi_gpio_set_val) | 设置指定引脚的输出电平 |
| [uapi_gpio_get_output_val](#uapi_gpio_get_output_val) | 获取指定引脚的输出电平 |
| [uapi_gpio_get_val](#uapi_gpio_get_val) | 读取指定引脚的输入电平 |
| [uapi_gpio_toggle](#uapi_gpio_toggle) | 翻转指定引脚的输出电平 |
| [uapi_gpio_set_isr_mode](#uapi_gpio_set_isr_mode) | 设置指定引脚的中断触发模式 |
| [uapi_gpio_register_isr_func](#uapi_gpio_register_isr_func) | 注册指定引脚的中断回调函数 |
| [uapi_gpio_unregister_isr_func](#uapi_gpio_unregister_isr_func) | 去注册指定引脚的中断回调 |
| [uapi_gpio_enable_interrupt](#uapi_gpio_enable_interrupt) | 使能指定引脚的中断 |
| [uapi_gpio_disable_interrupt](#uapi_gpio_disable_interrupt) | 去使能指定引脚的中断 |
| [uapi_gpio_clear_interrupt](#uapi_gpio_clear_interrupt) | 清除指定引脚的中断 |
| [uapi_gpio_suspend](#uapi_gpio_suspend) | 挂起所有 GPIO 通道 |
| [uapi_gpio_resume](#uapi_gpio_resume) | 恢复所有 GPIO 通道 |
| [uapi_gpio_select_core](#uapi_gpio_select_core) | 选择指定引脚归属的核心 |

## Functions

### uapi_gpio_init <a id="uapi_gpio_init"></a>

```c
void uapi_gpio_init(void)
```

**声明头文件**

```c
#include "include/driver/gpio.h"
```

**功能说明**

- 初始化 GPIO 模块，为后续引脚方向、电平、中断等操作建立基础运行环境。
- 已初始化时重复调用直接返回成功。

**前置条件**

- 调用时序约束：应在调用模块内任何其他接口之前完成初始化。
- 依赖关系：依赖底层 GPIO HAL 已可被调用。

**参考案例**

- `src/application/ws53/ws53_application/main.c`

### uapi_gpio_deinit <a id="uapi_gpio_deinit"></a>

```c
void uapi_gpio_deinit(void)
```

**声明头文件**

```c
#include "include/driver/gpio.h"
```

**功能说明**

- 去初始化 GPIO 模块，释放初始化状态。
- 未初始化时调用直接返回。
- 与 uapi_gpio_init() 配对使用。

**前置条件**

- 调用时序约束：应在 uapi_gpio_init() 成功执行之后调用。

### uapi_gpio_set_dir <a id="uapi_gpio_set_dir"></a>

```c
errcode_t uapi_gpio_set_dir(pin_t pin, gpio_direction_t dir)
```

**声明头文件**

```c
#include "include/driver/gpio.h"
```

**功能说明**

- 设置指定 GPIO 引脚的输入或输出方向。
- 方向配置操作具备原子性。
- 返回操作执行结果。

**前置条件**

- 调用时序约束：必须在 uapi_gpio_init() 成功返回后调用。
- 上下文限制：可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#pin_t) | 待设置方向的 GPIO 引脚编号 | 有效引脚编号 |
| dir | [gpio_direction_t](#enum_gpio_direction) | 引脚输入输出方向 | [gpio_direction_t](#enum_gpio_direction) 全体成员 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 方向设置成功 |
| [ERRCODE_GPIO_NOT_INIT](#ERRCODE_GPIO_NOT_INIT)：0x80001001 | 模块未初始化 | 未调用 uapi_gpio_init() |
| [ERRCODE_GPIO_DIR_SET_FAIL](#ERRCODE_GPIO_DIR_SET_FAIL)：0x80001000 | 方向设置失败 | dir 超出有效范围（≥ 2） |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层设置失败 |

**参考案例**

- `src/application/samples/peripheral/blinky/blinky_demo.c`
- `src/application/samples/peripheral/lpc/lpc_gpio_wakeup_demo.c`
- `src/application/ws53/ws53_application/main.c`
- `src/middleware/chips/ws53/pm/pm_porting.c`
- `src/middleware/utils/at/at_plt_cmd/at/at_plt.c`
- `src/middleware/utils/connectivity/common/acore/low_power_control.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_GPIO_SUPPORT_DISCONTINUOUS | 特性宏 | 支持非连续引脚编号转换特性（分支级）；源码引用存在但全仓 Kconfig 未声明对应 config，接口实际不可启用 | - |

### uapi_gpio_get_dir <a id="uapi_gpio_get_dir"></a>

```c
gpio_direction_t uapi_gpio_get_dir(pin_t pin)
```

**声明头文件**

```c
#include "include/driver/gpio.h"
```

**功能说明**

- 获取指定 GPIO 引脚当前的输入输出方向。
- 直接返回方向枚举值。

**前置条件**

- 调用时序约束：必须在 uapi_gpio_init() 成功返回后调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#pin_t) | 待查询方向的 GPIO 引脚编号 | 有效引脚编号 |

**返回值**

- 返回类型：gpio_direction_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| GPIO_DIRECTION_INPUT(0) | 输入方向 | 引脚配置为输入或模块未初始化时返回 |
| GPIO_DIRECTION_OUTPUT(1) | 输出方向 | 引脚配置为输出 |

**参考案例**

- `src/middleware/utils/at/at_plt_cmd/at/at_plt.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_GPIO_SUPPORT_DISCONTINUOUS | 特性宏 | 支持非连续引脚编号转换特性（分支级）；源码引用存在但全仓 Kconfig 未声明对应 config，接口实际不可启用 | - |

### uapi_gpio_set_val <a id="uapi_gpio_set_val"></a>

```c
errcode_t uapi_gpio_set_val(pin_t pin, gpio_level_t level)
```

**声明头文件**

```c
#include "include/driver/gpio.h"
```

**功能说明**

- 设置指定 GPIO 引脚的输出电平（高或低）。
- 输出电平写入操作具备原子性。
- 返回操作执行结果。

**前置条件**

- 调用时序约束：必须在 uapi_gpio_init() 成功返回后调用，且引脚应已配置为输出方向。
- 上下文限制：可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#pin_t) | 待设置输出电平的 GPIO 引脚编号 | 有效引脚编号 |
| level | [gpio_level_t](#enum_gpio_level) | 输出电平值 | [gpio_level_t](#enum_gpio_level) 全体成员 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 电平设置成功 |
| [ERRCODE_GPIO_NOT_INIT](#ERRCODE_GPIO_NOT_INIT)：0x80001001 | 模块未初始化 | 未调用 uapi_gpio_init() |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层输出失败 |

**参考案例**

- `src/application/samples/peripheral/blinky/blinky_demo.c`
- `src/middleware/utils/at/at_plt_cmd/at/at_plt.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_GPIO_SUPPORT_DISCONTINUOUS | 特性宏 | 支持非连续引脚编号转换特性（分支级）；源码引用存在但全仓 Kconfig 未声明对应 config，接口实际不可启用 | - |

### uapi_gpio_get_output_val <a id="uapi_gpio_get_output_val"></a>

```c
gpio_level_t uapi_gpio_get_output_val(pin_t pin)
```

**声明头文件**

```c
#include "include/driver/gpio.h"
```

**功能说明**

- 获取指定 GPIO 引脚当前的输出电平值。
- 直接返回输出电平枚举值。

**前置条件**

- 调用时序约束：必须在 uapi_gpio_init() 成功返回后调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#pin_t) | 待查询输出电平的 GPIO 引脚编号 | 有效引脚编号 |

**返回值**

- 返回类型：gpio_level_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| GPIO_LEVEL_LOW(0) | 低电平 | 引脚输出为低电平或模块未初始化时返回 |
| GPIO_LEVEL_HIGH(1) | 高电平 | 引脚输出为高电平 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_GPIO_SUPPORT_DISCONTINUOUS | 特性宏 | 支持非连续引脚编号转换特性（分支级）；源码引用存在但全仓 Kconfig 未声明对应 config，接口实际不可启用 | - |

### uapi_gpio_get_val <a id="uapi_gpio_get_val"></a>

```c
gpio_level_t uapi_gpio_get_val(pin_t pin)
```

**声明头文件**

```c
#include "include/driver/gpio.h"
```

**功能说明**

- 读取指定 GPIO 引脚的输入电平值。
- 直接返回输入电平枚举值。

**前置条件**

- 调用时序约束：必须在 uapi_gpio_init() 成功返回后调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#pin_t) | 待读取输入电平的 GPIO 引脚编号 | 有效引脚编号 |

**返回值**

- 返回类型：gpio_level_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| GPIO_LEVEL_LOW(0) | 低电平 | 引脚输入为低电平或模块未初始化时返回 |
| GPIO_LEVEL_HIGH(1) | 高电平 | 引脚输入为高电平 |

**参考案例**

- `src/middleware/utils/at/at_plt_cmd/at/at_plt.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_GPIO_SUPPORT_DISCONTINUOUS | 特性宏 | 支持非连续引脚编号转换特性（分支级）；源码引用存在但全仓 Kconfig 未声明对应 config，接口实际不可启用 | - |

### uapi_gpio_toggle <a id="uapi_gpio_toggle"></a>

```c
errcode_t uapi_gpio_toggle(pin_t pin)
```

**声明头文件**

```c
#include "include/driver/gpio.h"
```

**功能说明**

- 翻转指定 GPIO 引脚的输出电平状态（高变低、低变高）。
- 翻转操作具备原子性。
- 返回操作执行结果。

**前置条件**

- 调用时序约束：必须在 uapi_gpio_init() 成功返回后调用，且引脚应已配置为输出方向。
- 上下文限制：可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#pin_t) | 待翻转输出电平的 GPIO 引脚编号 | 有效引脚编号 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 电平翻转成功 |
| [ERRCODE_GPIO_NOT_INIT](#ERRCODE_GPIO_NOT_INIT)：0x80001001 | 模块未初始化 | 未调用 uapi_gpio_init() |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层翻转失败 |

**参考案例**

- `src/application/samples/peripheral/blinky/blinky_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_GPIO_SUPPORT_DISCONTINUOUS | 特性宏 | 支持非连续引脚编号转换特性（分支级）；源码引用存在但全仓 Kconfig 未声明对应 config，接口实际不可启用 | - |

### uapi_gpio_set_isr_mode <a id="uapi_gpio_set_isr_mode"></a>

```c
errcode_t uapi_gpio_set_isr_mode(pin_t pin, uint32_t trigger)
```

**声明头文件**

```c
#include "include/driver/gpio.h"
```

**功能说明**

- 设置指定 GPIO 引脚的中断触发模式（上升沿、下降沿、双边沿、高/低电平）。
- 中断模式配置操作具备原子性。
- 返回操作执行结果。

**前置条件**

- 调用时序约束：必须在 uapi_gpio_init() 成功返回后调用。
- 上下文限制：可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#pin_t) | 待设置中断模式的 GPIO 引脚编号 | 有效引脚编号 |
| trigger | uint32_t | GPIO 中断触发类型 | [GPIO_INTERRUPT_RISING_EDGE](#GPIO_INTERRUPT_RISING_EDGE)：1；<br>[GPIO_INTERRUPT_FALLING_EDGE](#GPIO_INTERRUPT_FALLING_EDGE)：2；<br>[GPIO_INTERRUPT_LOW](#GPIO_INTERRUPT_LOW)：4；<br>[GPIO_INTERRUPT_HIGH](#GPIO_INTERRUPT_HIGH)：8；<br>[GPIO_INTERRUPT_DEDGE](#GPIO_INTERRUPT_DEDGE)：3。 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 中断模式设置成功 |
| [ERRCODE_GPIO_NOT_INIT](#ERRCODE_GPIO_NOT_INIT)：0x80001001 | 模块未初始化 | 未调用 uapi_gpio_init() |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层设置失败 |

**参考案例**

- `src/application/samples/peripheral/lpc/lpc_gpio_wakeup_demo.c`
- `src/middleware/chips/ws53/pm/pm_porting.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_GPIO_SUPPORT_DISCONTINUOUS | 特性宏 | 支持非连续引脚编号转换特性（分支级）；源码引用存在但全仓 Kconfig 未声明对应 config，接口实际不可启用 | - |

### uapi_gpio_register_isr_func <a id="uapi_gpio_register_isr_func"></a>

```c
errcode_t uapi_gpio_register_isr_func(pin_t pin, uint32_t trigger, gpio_callback_t callback)
```

**声明头文件**

```c
#include "include/driver/gpio.h"
```

**功能说明**

- 为指定 GPIO 引脚注册中断回调函数，并设置中断触发模式。
- 中断触发时调用已注册的回调函数。
- 注册操作具备原子性。

**前置条件**

- 调用时序约束：必须在 uapi_gpio_init() 成功返回后调用。
- 上下文限制：可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#pin_t) | 待注册中断的 GPIO 引脚编号 | 有效引脚编号 |
| trigger | uint32_t | GPIO 中断触发类型 | [GPIO_INTERRUPT_RISING_EDGE](#GPIO_INTERRUPT_RISING_EDGE)：1；<br>[GPIO_INTERRUPT_FALLING_EDGE](#GPIO_INTERRUPT_FALLING_EDGE)：2；<br>[GPIO_INTERRUPT_LOW](#GPIO_INTERRUPT_LOW)：4；<br>[GPIO_INTERRUPT_HIGH](#GPIO_INTERRUPT_HIGH)：8；<br>[GPIO_INTERRUPT_DEDGE](#GPIO_INTERRUPT_DEDGE)：3。 |
| callback | [gpio_callback_t](#gpio_callback_t) | 中断回调函数指针 | 不为 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 中断注册成功 |
| [ERRCODE_GPIO_NOT_INIT](#ERRCODE_GPIO_NOT_INIT)：0x80001001 | 模块未初始化 | 未调用 uapi_gpio_init() |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层注册失败 |

**参考案例**

- `src/application/samples/peripheral/lpc/lpc_gpio_wakeup_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_GPIO_SUPPORT_DISCONTINUOUS | 特性宏 | 支持非连续引脚编号转换特性（分支级）；源码引用存在但全仓 Kconfig 未声明对应 config，接口实际不可启用 | - |

### uapi_gpio_unregister_isr_func <a id="uapi_gpio_unregister_isr_func"></a>

```c
errcode_t uapi_gpio_unregister_isr_func(pin_t pin)
```

**声明头文件**

```c
#include "include/driver/gpio.h"
```

**功能说明**

- 去注册指定 GPIO 引脚已注册的中断回调。
- 去注册操作具备原子性。
- 返回操作执行结果。

**前置条件**

- 调用时序约束：必须在 uapi_gpio_init() 成功返回后调用。
- 上下文限制：可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#pin_t) | 待去注册中断的 GPIO 引脚编号 | 有效引脚编号 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 去成功注册 |
| [ERRCODE_GPIO_NOT_INIT](#ERRCODE_GPIO_NOT_INIT)：0x80001001 | 模块未初始化 | 未调用 uapi_gpio_init() |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层去注册失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_GPIO_SUPPORT_DISCONTINUOUS | 特性宏 | 支持非连续引脚编号转换特性（分支级）；源码引用存在但全仓 Kconfig 未声明对应 config，接口实际不可启用 | - |

### uapi_gpio_enable_interrupt <a id="uapi_gpio_enable_interrupt"></a>

```c
errcode_t uapi_gpio_enable_interrupt(pin_t pin)
```

**声明头文件**

```c
#include "include/driver/gpio.h"
```

**功能说明**

- 使能指定 GPIO 引脚的中断。
- 使能操作具备原子性。
- 返回操作执行结果。

**前置条件**

- 调用时序约束：必须在 uapi_gpio_init() 成功返回后调用，且已通过 uapi_gpio_register_isr_func() 完成回调注册。
- 上下文限制：可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#pin_t) | 待使能中断的 GPIO 引脚编号 | 有效引脚编号 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 中断使能成功 |
| [ERRCODE_GPIO_NOT_INIT](#ERRCODE_GPIO_NOT_INIT)：0x80001001 | 模块未初始化 | 未调用 uapi_gpio_init() |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层使能失败 |

**参考案例**

- `src/application/samples/peripheral/lpc/lpc_gpio_wakeup_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_GPIO_SUPPORT_DISCONTINUOUS | 特性宏 | 支持非连续引脚编号转换特性（分支级）；源码引用存在但全仓 Kconfig 未声明对应 config，接口实际不可启用 | - |

### uapi_gpio_disable_interrupt <a id="uapi_gpio_disable_interrupt"></a>

```c
errcode_t uapi_gpio_disable_interrupt(pin_t pin)
```

**声明头文件**

```c
#include "include/driver/gpio.h"
```

**功能说明**

- 去使能指定 GPIO 引脚的中断。
- 去使能操作具备原子性。
- 返回操作执行结果。

**前置条件**

- 调用时序约束：必须在 uapi_gpio_init() 成功返回后调用。
- 上下文限制：可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#pin_t) | 待去使能中断的 GPIO 引脚编号 | 有效引脚编号 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 中断去使能成功 |
| [ERRCODE_GPIO_NOT_INIT](#ERRCODE_GPIO_NOT_INIT)：0x80001001 | 模块未初始化 | 未调用 uapi_gpio_init() |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层去使能失败 |

**参考案例**

- `src/application/samples/peripheral/lpc/lpc_gpio_wakeup_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_GPIO_SUPPORT_DISCONTINUOUS | 特性宏 | 支持非连续引脚编号转换特性（分支级）；源码引用存在但全仓 Kconfig 未声明对应 config，接口实际不可启用 | - |

### uapi_gpio_clear_interrupt <a id="uapi_gpio_clear_interrupt"></a>

```c
errcode_t uapi_gpio_clear_interrupt(pin_t pin)
```

**声明头文件**

```c
#include "include/driver/gpio.h"
```

**功能说明**

- 清除指定 GPIO 引脚已触发的中断。
- 清除操作具备原子性。
- 返回操作执行结果。

**前置条件**

- 调用时序约束：必须在 uapi_gpio_init() 成功返回后调用。
- 上下文限制：可在任务上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#pin_t) | 待清除中断的 GPIO 引脚编号 | 有效引脚编号 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 中断清除成功 |
| [ERRCODE_GPIO_NOT_INIT](#ERRCODE_GPIO_NOT_INIT)：0x80001001 | 模块未初始化 | 未调用 uapi_gpio_init() |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层清除失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_GPIO_SUPPORT_DISCONTINUOUS | 特性宏 | 支持非连续引脚编号转换特性（分支级）；源码引用存在但全仓 Kconfig 未声明对应 config，接口实际不可启用 | - |

### uapi_gpio_suspend <a id="uapi_gpio_suspend"></a>

```c
errcode_t uapi_gpio_suspend(uintptr_t arg)
```

**声明头文件**

```c
#include "include/driver/gpio.h"
```

**功能说明**

- 挂起所有 GPIO 通道，用于进入低功耗场景。
- 返回操作执行结果。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| arg | uintptr_t | 挂起操作所需的参数 | - |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 挂起成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层挂起失败 |

**参考案例**

- `src/middleware/chips/ws53/pm/pm_sleep/pm_sleep_porting.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_GPIO_SUPPORT_LPM | 特性宏 | 支持 GPIO 低功耗挂起/恢复功能（接口级） | y |

### uapi_gpio_resume <a id="uapi_gpio_resume"></a>

```c
errcode_t uapi_gpio_resume(uintptr_t arg)
```

**声明头文件**

```c
#include "include/driver/gpio.h"
```

**功能说明**

- 恢复所有 GPIO 通道，用于退出低功耗场景。
- 返回操作执行结果。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| arg | uintptr_t | 恢复操作所需的参数 | - |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 恢复成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 底层恢复失败 |

**参考案例**

- `src/middleware/chips/ws53/pm/pm_sleep/pm_sleep_porting.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_GPIO_SUPPORT_LPM | 特性宏 | 支持 GPIO 低功耗挂起/恢复功能（接口级） | y |

### uapi_gpio_select_core <a id="uapi_gpio_select_core"></a>

```c
void uapi_gpio_select_core(pin_t pin, cores_t core)
```

**声明头文件**

```c
#include "include/driver/gpio.h"
```

**功能说明**

- 选择指定 GPIO 引脚归属的核心。
- 当前芯片版本上此接口不产生实际配置效果。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#pin_t) | 待选择归属核心的 GPIO 引脚编号 | 有效引脚编号 |
| core | [cores_t](#cores_t) | 引脚归属的目标核心 | 有效核心枚举值 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_GPIO_SELECT_CORE | 特性宏 | 支持 GPIO 多核选择功能（接口级） | n |

## Type definitions

### gpio_callback_t <a id="gpio_callback_t"></a>

```c
typedef void (*gpio_callback_t)(pin_t pin, uintptr_t param);
```

**使用说明**

用于 uapi_gpio_register_isr_func() 注册中断回调。当指定引脚的中断触发时被调用，回调参数 pin 为产生中断的引脚编号，param 为透传给回调的上下文参数。

### errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

错误码类型，作为本模块多个 GPIO 接口的返回值类型。

## Enumerations

### enum gpio_direction <a id="enum_gpio_direction"></a>

```c
typedef enum gpio_direction {
    GPIO_DIRECTION_INPUT,
    GPIO_DIRECTION_OUTPUT
} gpio_direction_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GPIO_DIRECTION_INPUT | 0 | 输入方向 |
| GPIO_DIRECTION_OUTPUT | 1 | 输出方向 |

### enum gpio_level <a id="enum_gpio_level"></a>

```c
typedef enum gpio_level {
    GPIO_LEVEL_LOW,
    GPIO_LEVEL_HIGH
} gpio_level_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| GPIO_LEVEL_LOW | 0 | 低电平 |
| GPIO_LEVEL_HIGH | 1 | 高电平 |

### enum pin_t <a id="pin_t"></a>

```c
typedef enum {
    S_MGPIO0  = 0,
    S_MGPIO1  = 38, // MGPIO1 <=> AGPIO6 (AON)
    S_MGPIO2  = 2,
    S_MGPIO3  = 3,
    S_MGPIO4  = 4,
    S_MGPIO5  = 5,
    S_MGPIO6  = 32, // MGPIO6 <=> AGPIO0 (AON)
    S_MGPIO7  = 41, // MGPIO7 <=> AGPIO9 (AON)
    S_MGPIO8  = 8,
    S_MGPIO9  = 9,
    S_MGPIO10 = 10,
    S_MGPIO11 = 39, // MGPI11 <=> AGPIO7 (AON)
    S_MGPIO12 = 12,
    S_MGPIO13 = 13,
    S_MGPIO14 = 45, // same as SGPIO0 (SEC GPIO)
    S_MGPIO15 = 46, // same as SGPIO1 (SEC GPIO)
    S_MGPIO16 = 40, // MGPIO16 <=> AGPIO8 (AON)
    S_MGPIO17 = 17,
    S_MGPIO18 = 18,
    S_MGPIO19 = 19,
    S_MGPIO20 = 20,
    S_MGPIO21 = 47, // same as SGPIO2 (SEC GPIO)
    S_MGPIO22 = 22,
    // 23
    // 24 S_MGPIO24 not pin out
    // 25 S_MGPIO25 not pin out
    // 26 S_MGPIO26 not pin out
    // 27 S_MGPIO27 not pin out
    // 28 S_MGPIO28 not pin out
    // 29 S_MGPIO29 not pin out
    S_MGPIO30 = 30,
    S_MGPIO31 = 31,

    S_AGPIO0  = S_MGPIO6, // 32
    S_AGPIO1  = 33,
    S_AGPIO2  = 34,
    S_AGPIO3  = 35,
    S_AGPIO4  = 36,
    S_AGPIO5  = 37,
    S_AGPIO6  = S_MGPIO1,   // 38
    S_AGPIO7  = S_MGPIO11,  // 39
    S_AGPIO8  = S_MGPIO16,  // 40
    S_AGPIO9  = S_MGPIO7,   // 41
    S_AGPIO10 = 42, // RTC_IN
    S_AGPIO11 = 43, // RTC_OUT
    S_AGPIO12 = 44, // RST_N (不能作为GPIO,不能配置pinmux,但可以配置padctrl)

    S_SGPIO0  = S_MGPIO14, // 45 same as MGPIO14
    S_SGPIO1  = S_MGPIO15, // 46 same as MGPIO15
    S_SGPIO2  = S_MGPIO21, // 47 same as MGPIO21

    PIN_NONE  = 48, // used as invalid/unused PIN number
} pin_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| S_MGPIO0 | 0 | 主 GPIO 引脚 0 |
| S_MGPIO1 | 38 | 主 GPIO 引脚 1，与 AGPIO6（AON 域）复用 |
| S_MGPIO2 | 2 | 主 GPIO 引脚 2 |
| S_MGPIO3 | 3 | 主 GPIO 引脚 3 |
| S_MGPIO4 | 4 | 主 GPIO 引脚 4 |
| S_MGPIO5 | 5 | 主 GPIO 引脚 5 |
| S_MGPIO6 | 32 | 主 GPIO 引脚 6，与 AGPIO0（AON 域）复用 |
| S_MGPIO7 | 41 | 主 GPIO 引脚 7，与 AGPIO9（AON 域）复用 |
| S_MGPIO8 | 8 | 主 GPIO 引脚 8 |
| S_MGPIO9 | 9 | 主 GPIO 引脚 9 |
| S_MGPIO10 | 10 | 主 GPIO 引脚 10 |
| S_MGPIO11 | 39 | 主 GPIO 引脚 11，与 AGPIO7（AON 域）复用 |
| S_MGPIO12 | 12 | 主 GPIO 引脚 12 |
| S_MGPIO13 | 13 | 主 GPIO 引脚 13 |
| S_MGPIO14 | 45 | 主 GPIO 引脚 14，与 SGPIO0（安全 GPIO）同编号 |
| S_MGPIO15 | 46 | 主 GPIO 引脚 15，与 SGPIO1（安全 GPIO）同编号 |
| S_MGPIO16 | 40 | 主 GPIO 引脚 16，与 AGPIO8（AON 域）复用 |
| S_MGPIO17 | 17 | 主 GPIO 引脚 17 |
| S_MGPIO18 | 18 | 主 GPIO 引脚 18 |
| S_MGPIO19 | 19 | 主 GPIO 引脚 19 |
| S_MGPIO20 | 20 | 主 GPIO 引脚 20 |
| S_MGPIO21 | 47 | 主 GPIO 引脚 21，与 SGPIO2（安全 GPIO）同编号 |
| S_MGPIO22 | 22 | 主 GPIO 引脚 22（23~29 未引出） |
| S_MGPIO30 | 30 | 主 GPIO 引脚 30 |
| S_MGPIO31 | 31 | 主 GPIO 引脚 31 |
| S_AGPIO0 | 32 | 常开域 GPIO 引脚 0，等同 S_MGPIO6 |
| S_AGPIO1 | 33 | 常开域 GPIO 引脚 1 |
| S_AGPIO2 | 34 | 常开域 GPIO 引脚 2 |
| S_AGPIO3 | 35 | 常开域 GPIO 引脚 3 |
| S_AGPIO4 | 36 | 常开域 GPIO 引脚 4 |
| S_AGPIO5 | 37 | 常开域 GPIO 引脚 5 |
| S_AGPIO6 | 38 | 常开域 GPIO 引脚 6，等同 S_MGPIO1 |
| S_AGPIO7 | 39 | 常开域 GPIO 引脚 7，等同 S_MGPIO11 |
| S_AGPIO8 | 40 | 常开域 GPIO 引脚 8，等同 S_MGPIO16 |
| S_AGPIO9 | 41 | 常开域 GPIO 引脚 9，等同 S_MGPIO7 |
| S_AGPIO10 | 42 | 常开域 GPIO 引脚 10（RTC_IN） |
| S_AGPIO11 | 43 | 常开域 GPIO 引脚 11（RTC_OUT） |
| S_AGPIO12 | 44 | 常开域 GPIO 引脚 12（RST_N，不能作为 GPIO、不能配置 pinmux，可配置 padctrl） |
| S_SGPIO0 | 45 | 安全 GPIO 引脚 0，与 MGPIO14 同编号 |
| S_SGPIO1 | 46 | 安全 GPIO 引脚 1，与 MGPIO15 同编号 |
| S_SGPIO2 | 47 | 安全 GPIO 引脚 2，与 MGPIO21 同编号 |
| PIN_NONE | 48 | 无效/未使用的引脚编号 |

### enum cores_t <a id="cores_t"></a>

```c
typedef enum {
    CORES_BT_CORE = 0,                              /* !< bt Core. */
    CORES_PROTOCOL_CORE = 1,                        /* !< Hifi Core. */
    CORES_APPS_CORE = 2,                            /* !< Applications Core. */
    CORES_EXTERN0_CORE = 3,                         /* !< Gnss or Hifi Core. */
#if (defined(GNSS_EXIST) && GNSS_EXIST == YES)
    CORES_GNSS_CORE = CORES_EXTERN0_CORE,
#else
    CORES_HIFI1_CORE = CORES_EXTERN0_CORE,
#endif
    CORES_EXTERN1_CORE = 4,                         /* !< Sec or Sensor Core */
#if (defined(SENSOR_EXIST) && SENSOR_EXIST == YES)
    CORES_SEN_CORE = CORES_EXTERN1_CORE,
#else
    CORES_SEC_CORE = CORES_EXTERN1_CORE,
#endif
#if (CORE_NUMS < 3)                                 /* !< For BS25, dsp core is null. */
    CORES_MAX_NUMBER_PHYSICAL = 3,                  /* !< Used to size/range arrays for physical cores where needed. */
#else
    CORES_MAX_NUMBER_PHYSICAL,
#endif
    CORES_NONE = CORES_MAX_NUMBER_PHYSICAL,         /* !< Used to return a NONE value where needed. */
    CORES_ASSET_CORE = CORES_MAX_NUMBER_PHYSICAL,   /* used for asset store */
    CORES_UNKNOWN = CORES_MAX_NUMBER_PHYSICAL + 1,  /* !< Used to return a unknown value. */
} cores_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| CORES_BT_CORE | 0 | BT 核心 |
| CORES_PROTOCOL_CORE | 1 | 协议核心（Hifi） |
| CORES_APPS_CORE | 2 | 应用核心 |
| CORES_EXTERN0_CORE | 3 | 外部核心 0（GNSS 或 Hifi） |
| CORES_GNSS_CORE | 3 | GNSS 核心（GNSS_EXIST 启用时，等同 CORES_EXTERN0_CORE） |
| CORES_HIFI1_CORE | 3 | HIFI1 核心（GNSS_EXIST 未启用时，等同 CORES_EXTERN0_CORE） |
| CORES_EXTERN1_CORE | 4 | 外部核心 1（Sec 或 Sensor） |
| CORES_SEN_CORE | 4 | Sensor 核心（SENSOR_EXIST 启用时，等同 CORES_EXTERN1_CORE） |
| CORES_SEC_CORE | 4 | 安全核心（SENSOR_EXIST 未启用时，等同 CORES_EXTERN1_CORE） |
| CORES_MAX_NUMBER_PHYSICAL | 3（CORE_NUMS < 3 时）/ 5（否则） | 物理核心数量上限 |
| CORES_NONE | 同 CORES_MAX_NUMBER_PHYSICAL | 无核心 |
| CORES_ASSET_CORE | 同 CORES_MAX_NUMBER_PHYSICAL | 资产存储核心 |
| CORES_UNKNOWN | 同 CORES_MAX_NUMBER_PHYSICAL + 1 | 未知核心 |

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```

### ERRCODE_FAIL <a id="ERRCODE_FAIL"></a>

```c
#define ERRCODE_FAIL                                        0xFFFFFFFF
```

### ERRCODE_GPIO_NOT_INIT <a id="ERRCODE_GPIO_NOT_INIT"></a>

```c
#define ERRCODE_GPIO_NOT_INIT                               0x80001001
```

### ERRCODE_GPIO_DIR_SET_FAIL <a id="ERRCODE_GPIO_DIR_SET_FAIL"></a>

```c
#define ERRCODE_GPIO_DIR_SET_FAIL                           0x80001000
```

### GPIO_INTERRUPT_RISING_EDGE <a id="GPIO_INTERRUPT_RISING_EDGE"></a>

```c
#define GPIO_INTERRUPT_RISING_EDGE            0x00000001
```

### GPIO_INTERRUPT_FALLING_EDGE <a id="GPIO_INTERRUPT_FALLING_EDGE"></a>

```c
#define GPIO_INTERRUPT_FALLING_EDGE           0x00000002
```

### GPIO_INTERRUPT_LOW <a id="GPIO_INTERRUPT_LOW"></a>

```c
#define GPIO_INTERRUPT_LOW                    0x00000004
```

### GPIO_INTERRUPT_HIGH <a id="GPIO_INTERRUPT_HIGH"></a>

```c
#define GPIO_INTERRUPT_HIGH                   0x00000008
```

### GPIO_INTERRUPT_DEDGE <a id="GPIO_INTERRUPT_DEDGE"></a>

```c
#define GPIO_INTERRUPT_DEDGE                  (GPIO_INTERRUPT_RISING_EDGE | GPIO_INTERRUPT_FALLING_EDGE)
```
