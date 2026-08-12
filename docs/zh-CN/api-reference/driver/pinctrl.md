# Pinctrl

Pinctrl (Pin Multiplexing Control) 提供引脚复用与引脚配置功能，支持引脚复用模式、驱动能力、上下拉、输入使能与施密特触发状态的设置与获取，并支持低功耗场景下的挂起与恢复。

**头文件清单**

```c
#include "include/driver/pinctrl.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_pin_init](#uapi_pin_init) | 初始化 Pinctrl 模块 |
| [uapi_pin_deinit](#uapi_pin_deinit) | 去初始化 Pinctrl 模块 |
| [uapi_pin_set_mode](#uapi_pin_set_mode) | 设置引脚复用模式 |
| [uapi_pin_get_mode](#uapi_pin_get_mode) | 获取引脚复用模式 |
| [uapi_pin_set_ds](#uapi_pin_set_ds) | 设置引脚驱动能力 |
| [uapi_pin_get_ds](#uapi_pin_get_ds) | 获取引脚驱动能力 |
| [uapi_pin_set_pull](#uapi_pin_set_pull) | 设置引脚上下拉 |
| [uapi_pin_get_pull](#uapi_pin_get_pull) | 获取引脚上下拉状态 |
| [uapi_pin_set_ie](#uapi_pin_set_ie) | 设置引脚输入使能状态 |
| [uapi_pin_get_ie](#uapi_pin_get_ie) | 获取引脚输入使能状态 |
| [uapi_pin_set_st](#uapi_pin_set_st) | 设置引脚施密特触发状态 |
| [uapi_pin_get_st](#uapi_pin_get_st) | 获取引脚施密特触发状态 |
| [uapi_pin_suspend](#uapi_pin_suspend) | 挂起 Pinctrl |
| [uapi_pin_resume](#uapi_pin_resume) | 恢复 Pinctrl |

## Functions

### uapi_pin_init <a id="uapi_pin_init"></a>

```c
void uapi_pin_init(void)
```

**头文件清单**

```c
#include "include/driver/pinctrl.h"
```

**功能说明**

- 初始化 Pinctrl 模块
- 注册底层 HAL 引脚操作接口实例
- 本模块其他接口的调用前提

**前置条件**

- 调用时序约束：当前接口必须在其他本模块函数被调用前执行
- 依赖关系：当前接口依赖底层 HAL 引脚操作接口已实现

**参考案例**

- `src/application/samples/peripheral/pinctrl/pinctrl_demo.c`

### uapi_pin_deinit <a id="uapi_pin_deinit"></a>

```c
void uapi_pin_deinit(void)
```

**头文件清单**

```c
#include "include/driver/pinctrl.h"
```

**功能说明**

- 去初始化 Pinctrl 模块
- 注销底层 HAL 引脚操作接口实例
- 释放本模块占用的引脚操作资源

**前置条件**

- 调用时序约束：当前接口必须在 uapi_pin_init 成功返回后调用
- 依赖关系：当前接口依赖底层 HAL 引脚操作接口已注册

**参考案例**

- `src/application/samples/peripheral/pinctrl/pinctrl_demo.c`

### uapi_pin_set_mode <a id="uapi_pin_set_mode"></a>

```c
errcode_t uapi_pin_set_mode(pin_t pin, pin_mode_t mode)
```

**头文件清单**

```c
#include "include/driver/pinctrl.h"
```

**功能说明**

- 设置指定引脚的复用模式
- 支持对单个引脚配置其复用功能选择
- 配置操作受中断保护，保证设置过程原子性

**前置条件**

- 调用时序约束：当前接口必须在 uapi_pin_init 成功返回后调用
- 依赖关系：当前接口依赖底层 HAL 引脚操作接口已注册

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#enum_pin_t) | 引脚编号 | 0 ~ 47 |
| mode | [pin_mode_t](#enum_pin_mode_t) | 复用模式 | [PIN_MODE_0](#enum_pin_mode_t)(0) / [PIN_MODE_1](#enum_pin_mode_t)(1) / [PIN_MODE_2](#enum_pin_mode_t)(2) / [PIN_MODE_3](#enum_pin_mode_t)(3) / [PIN_MODE_4](#enum_pin_mode_t)(4) / [PIN_MODE_5](#enum_pin_mode_t)(5) / [PIN_MODE_6](#enum_pin_mode_t)(6) / [PIN_MODE_7](#enum_pin_mode_t)(7) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 设置引脚复用模式成功 |
| [ERRCODE_PIN_INVALID_PARAMETER](#ERRCODE_PIN_INVALID_PARAMETER):0x80001190 | 参数无效 | pin 大于等于 PIN_MAX_NUMBER 或 mode 大于等于 PIN_MODE_MAX |
| [ERRCODE_PIN_MODE_NO_FUNC](#ERRCODE_PIN_MODE_NO_FUNC):0x80001191 | 模式无效 | 引脚不支持指定的复用模式 |
| [ERRCODE_PIN_NOT_INIT](#ERRCODE_PIN_NOT_INIT):0x80001192 | 未初始化 | HAL 引脚操作接口未注册 |

**参考案例**

- `src/application/samples/peripheral/pinctrl/pinctrl_demo.c`

### uapi_pin_get_mode <a id="uapi_pin_get_mode"></a>

```c
pin_mode_t uapi_pin_get_mode(pin_t pin)
```

**头文件清单**

```c
#include "include/driver/pinctrl.h"
```

**功能说明**

- 获取指定引脚的复用模式
- 返回值类型为 pin_mode_t，取值为引脚复用模式枚举
- 读取操作受中断保护，保证读取过程原子性

**前置条件**

- 调用时序约束：当前接口必须在 uapi_pin_init 成功返回后调用
- 依赖关系：当前接口依赖底层 HAL 引脚操作接口已注册

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#enum_pin_t) | 引脚编号 | 0 ~ 47 |

**返回值**

- 返回类型：pin_mode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [PIN_MODE_0](#enum_pin_mode_t)(0) ~ [PIN_MODE_7](#enum_pin_mode_t)(7) | 有效复用模式 | 读取到引脚的有效复用模式 |
| [PIN_MODE_MAX](#enum_pin_mode_t)(8) | 无效值 | pin 大于等于 PIN_MAX_NUMBER 或 HAL 引脚操作接口未注册 |

**参考案例**

- `src/application/samples/peripheral/pinctrl/pinctrl_demo.c`

### uapi_pin_set_ds <a id="uapi_pin_set_ds"></a>

```c
errcode_t uapi_pin_set_ds(pin_t pin, pin_drive_strength_t ds)
```

**头文件清单**

```c
#include "include/driver/pinctrl.h"
```

**功能说明**

- 设置指定引脚的驱动能力
- 支持对单个引脚配置其驱动强度等级
- 配置操作受中断保护，保证设置过程原子性

**前置条件**

- 调用时序约束：当前接口必须在 uapi_pin_init 成功返回后调用
- 依赖关系：当前接口依赖底层 HAL 引脚操作接口已注册

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#enum_pin_t) | 引脚编号 | 0 ~ 47 |
| ds | [pin_drive_strength_t](#enum_pin_drive_strength_t) | 驱动能力 | [PIN_DS_0](#enum_pin_drive_strength_t)(0) / [PIN_DS_1](#enum_pin_drive_strength_t)(1) / [PIN_DS_2](#enum_pin_drive_strength_t)(2) / [PIN_DS_3](#enum_pin_drive_strength_t)(3) / [PIN_DS_4](#enum_pin_drive_strength_t)(4) / [PIN_DS_5](#enum_pin_drive_strength_t)(5) / [PIN_DS_6](#enum_pin_drive_strength_t)(6) / [PIN_DS_7](#enum_pin_drive_strength_t)(7) / [PIN_DS_8](#enum_pin_drive_strength_t)(8) / [PIN_DS_9](#enum_pin_drive_strength_t)(9) / [PIN_DS_10](#enum_pin_drive_strength_t)(10) / [PIN_DS_11](#enum_pin_drive_strength_t)(11) / [PIN_DS_12](#enum_pin_drive_strength_t)(12) / [PIN_DS_13](#enum_pin_drive_strength_t)(13) / [PIN_DS_14](#enum_pin_drive_strength_t)(14) / [PIN_DS_15](#enum_pin_drive_strength_t)(15) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 设置引脚驱动能力成功 |
| [ERRCODE_PIN_INVALID_PARAMETER](#ERRCODE_PIN_INVALID_PARAMETER):0x80001190 | 参数无效 | pin 大于等于 PIN_MAX_NUMBER 或 ds 大于等于 PIN_DS_MAX |
| [ERRCODE_PIN_NOT_INIT](#ERRCODE_PIN_NOT_INIT):0x80001192 | 未初始化 | HAL 引脚操作接口未注册 |

**参考案例**

- `src/application/samples/peripheral/pinctrl/pinctrl_demo.c`

### uapi_pin_get_ds <a id="uapi_pin_get_ds"></a>

```c
pin_drive_strength_t uapi_pin_get_ds(pin_t pin)
```

**头文件清单**

```c
#include "include/driver/pinctrl.h"
```

**功能说明**

- 获取指定引脚的驱动能力
- 返回值类型为 pin_drive_strength_t，取值为驱动能力等级枚举
- 读取操作受中断保护，保证读取过程原子性

**前置条件**

- 调用时序约束：当前接口必须在 uapi_pin_init 成功返回后调用
- 依赖关系：当前接口依赖底层 HAL 引脚操作接口已注册

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#enum_pin_t) | 引脚编号 | 0 ~ 47 |

**返回值**

- 返回类型：pin_drive_strength_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [PIN_DS_0](#enum_pin_drive_strength_t)(0) ~ [PIN_DS_15](#enum_pin_drive_strength_t)(15) | 有效驱动能力 | 读取到引脚的有效驱动能力 |
| [PIN_DS_MAX](#enum_pin_drive_strength_t)(16) | 无效值 | pin 大于等于 PIN_MAX_NUMBER 或 HAL 引脚操作接口未注册 |

**参考案例**

- `src/application/samples/peripheral/pinctrl/pinctrl_demo.c`

### uapi_pin_set_pull <a id="uapi_pin_set_pull"></a>

```c
errcode_t uapi_pin_set_pull(pin_t pin, pin_pull_t pull_type)
```

**头文件清单**

```c
#include "include/driver/pinctrl.h"
```

**功能说明**

- 设置指定引脚的上下拉状态
- 支持对单个引脚配置无上下拉、上拉或下拉
- 配置操作受中断保护，保证设置过程原子性

**前置条件**

- 调用时序约束：当前接口必须在 uapi_pin_init 成功返回后调用
- 依赖关系：当前接口依赖底层 HAL 引脚操作接口已注册

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#enum_pin_t) | 引脚编号 | 0 ~ 47 |
| pull_type | [pin_pull_t](#enum_pin_pull_t) | 上下拉类型 | [PIN_PULL_NONE](#enum_pin_pull_t)(0) / [PIN_PULL_UP](#enum_pin_pull_t)(1) / [PIN_PULL_DOWN](#enum_pin_pull_t)(2) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 设置引脚上下拉状态成功 |
| [ERRCODE_PIN_INVALID_PARAMETER](#ERRCODE_PIN_INVALID_PARAMETER):0x80001190 | 参数无效 | pin 大于等于 PIN_MAX_NUMBER 或 pull_type 大于等于 PIN_PULL_MAX |
| [ERRCODE_PIN_NOT_INIT](#ERRCODE_PIN_NOT_INIT):0x80001192 | 未初始化 | HAL 引脚操作接口未注册 |

**参考案例**

- `src/application/samples/peripheral/pinctrl/pinctrl_demo.c`

### uapi_pin_get_pull <a id="uapi_pin_get_pull"></a>

```c
pin_pull_t uapi_pin_get_pull(pin_t pin)
```

**头文件清单**

```c
#include "include/driver/pinctrl.h"
```

**功能说明**

- 获取指定引脚的上下拉状态
- 返回值类型为 pin_pull_t，取值为上下拉类型枚举
- 读取操作受中断保护，保证读取过程原子性

**前置条件**

- 调用时序约束：当前接口必须在 uapi_pin_init 成功返回后调用
- 依赖关系：当前接口依赖底层 HAL 引脚操作接口已注册

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#enum_pin_t) | 引脚编号 | 0 ~ 47 |

**返回值**

- 返回类型：pin_pull_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [PIN_PULL_NONE](#enum_pin_pull_t)(0) / [PIN_PULL_UP](#enum_pin_pull_t)(1) / [PIN_PULL_DOWN](#enum_pin_pull_t)(2) | 有效上下拉状态 | 读取到引脚的有效上下拉状态 |
| [PIN_PULL_MAX](#enum_pin_pull_t)(3) | 无效值 | pin 大于等于 PIN_MAX_NUMBER 或 HAL 引脚操作接口未注册 |

**参考案例**

- `src/application/samples/peripheral/pinctrl/pinctrl_demo.c`

### uapi_pin_set_ie <a id="uapi_pin_set_ie"></a>

```c
errcode_t uapi_pin_set_ie(pin_t pin, pin_input_enable_t ie)
```

**头文件清单**

```c
#include "include/driver/pinctrl.h"
```

**功能说明**

- 设置指定引脚的输入使能状态
- 支持对单个引脚配置其输入缓冲使能开关
- 配置操作受中断保护，保证设置过程原子性

**前置条件**

- 调用时序约束：当前接口必须在 uapi_pin_init 成功返回后调用
- 依赖关系：当前接口依赖底层 HAL 引脚操作接口已注册

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#enum_pin_t) | 引脚编号 | 0 ~ 47 |
| ie | pin_input_enable_t | 输入使能状态 | 小于 PIN_IE_MAX |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 设置引脚输入使能状态成功 |
| [ERRCODE_PIN_INVALID_PARAMETER](#ERRCODE_PIN_INVALID_PARAMETER):0x80001190 | 参数无效 | pin 大于等于 PIN_MAX_NUMBER 或 ie 大于等于 PIN_IE_MAX |
| [ERRCODE_PIN_NOT_INIT](#ERRCODE_PIN_NOT_INIT):0x80001192 | 未初始化 | HAL 引脚操作接口未注册 |

**参考案例**

- `src/application/samples/peripheral/spi/spi_master_demo.c`
- `src/application/samples/peripheral/i2c/i2c_master_demo.c`
- `src/application/samples/peripheral/uart/uart_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PINCTRL_SUPPORT_IE | 特性宏 | 支持引脚输入使能配置功能（接口级） | n |

### uapi_pin_get_ie <a id="uapi_pin_get_ie"></a>

```c
pin_input_enable_t uapi_pin_get_ie(pin_t pin)
```

**头文件清单**

```c
#include "include/driver/pinctrl.h"
```

**功能说明**

- 获取指定引脚的输入使能状态
- 返回值类型为 pin_input_enable_t，取值为输入使能状态枚举
- 读取操作受中断保护，保证读取过程原子性

**前置条件**

- 调用时序约束：当前接口必须在 uapi_pin_init 成功返回后调用
- 依赖关系：当前接口依赖底层 HAL 引脚操作接口已注册

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#enum_pin_t) | 引脚编号 | 0 ~ 47 |

**返回值**

- 返回类型：pin_input_enable_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| pin_input_enable_t 有效值 | 有效输入使能状态 | 读取到引脚的有效输入使能状态 |
| PIN_IE_MAX | 无效值 | pin 大于等于 PIN_MAX_NUMBER 或 HAL 引脚操作接口未注册 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PINCTRL_SUPPORT_IE | 特性宏 | 支持引脚输入使能配置功能（接口级） | n |

### uapi_pin_set_st <a id="uapi_pin_set_st"></a>

```c
errcode_t uapi_pin_set_st(pin_t pin, pin_schmitt_trigger_t st)
```

**头文件清单**

```c
#include "include/driver/pinctrl.h"
```

**功能说明**

- 设置指定引脚的施密特触发状态
- 支持对单个引脚配置其施密特触发使能开关
- 配置操作受中断保护，保证设置过程原子性

**前置条件**

- 调用时序约束：当前接口必须在 uapi_pin_init 成功返回后调用
- 依赖关系：当前接口依赖底层 HAL 引脚操作接口已注册

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#enum_pin_t) | 引脚编号 | 0 ~ 47 |
| st | [pin_schmitt_trigger_t](#enum_pin_schmitt_trigger_t) | 施密特触发状态 | [PIN_ST_DISABLE](#enum_pin_schmitt_trigger_t)(0) / [PIN_ST_ENABLE](#enum_pin_schmitt_trigger_t)(1) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 设置引脚施密特触发状态成功 |
| [ERRCODE_PIN_INVALID_PARAMETER](#ERRCODE_PIN_INVALID_PARAMETER):0x80001190 | 参数无效 | pin 大于等于 PIN_MAX_NUMBER 或 st 大于等于 PIN_ST_MAX |
| [ERRCODE_PIN_NOT_INIT](#ERRCODE_PIN_NOT_INIT):0x80001192 | 未初始化 | HAL 引脚操作接口未注册 |

**参考案例**

- `src/application/samples/peripheral/lpc/lpc_gpio_wakeup_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PINCTRL_SUPPORT_ST | 特性宏 | 支持引脚施密特触发配置功能（接口级） | n |

### uapi_pin_get_st <a id="uapi_pin_get_st"></a>

```c
pin_schmitt_trigger_t uapi_pin_get_st(pin_t pin)
```

**头文件清单**

```c
#include "include/driver/pinctrl.h"
```

**功能说明**

- 获取指定引脚的施密特触发状态
- 返回值类型为 pin_schmitt_trigger_t，取值为施密特触发状态枚举
- 读取操作受中断保护，保证读取过程原子性

**前置条件**

- 调用时序约束：当前接口必须在 uapi_pin_init 成功返回后调用
- 依赖关系：当前接口依赖底层 HAL 引脚操作接口已注册

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pin | [pin_t](#enum_pin_t) | 引脚编号 | 0 ~ 47 |

**返回值**

- 返回类型：pin_schmitt_trigger_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [PIN_ST_DISABLE](#enum_pin_schmitt_trigger_t)(0) / [PIN_ST_ENABLE](#enum_pin_schmitt_trigger_t)(1) | 有效施密特触发状态 | 读取到引脚的有效施密特触发状态 |
| [PIN_ST_MAX](#enum_pin_schmitt_trigger_t)(2) | 无效值 | pin 大于等于 PIN_MAX_NUMBER 或 HAL 引脚操作接口未注册 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PINCTRL_SUPPORT_ST | 特性宏 | 支持引脚施密特触发配置功能（接口级） | n |

### uapi_pin_suspend <a id="uapi_pin_suspend"></a>

```c
errcode_t uapi_pin_suspend(uintptr_t arg)
```

**头文件清单**

```c
#include "include/driver/pinctrl.h"
```

**功能说明**

- 挂起 Pinctrl，用于低功耗进入前的引脚配置保存
- 调用底层 HAL 挂起接口完成引脚配置保存
- 支持透传挂起所需参数

**前置条件**

- 调用时序约束：当前接口必须在 uapi_pin_init 成功返回后调用
- 依赖关系：当前接口依赖底层 HAL 引脚操作接口已注册

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| arg | uintptr_t | 挂起所需要的参数 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 挂起操作成功，或 HAL 引脚操作接口未注册时直接返回成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | HAL 挂起接口执行失败 |

**参考案例**

- `src/middleware/chips/ws53/pm/pm_sleep/pm_sleep_porting.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PINCTRL_SUPPORT_LPM | 特性宏 | 支持低功耗挂起与恢复功能（接口级） | n |

### uapi_pin_resume <a id="uapi_pin_resume"></a>

```c
errcode_t uapi_pin_resume(uintptr_t arg)
```

**头文件清单**

```c
#include "include/driver/pinctrl.h"
```

**功能说明**

- 恢复 Pinctrl，用于低功耗退出后的引脚配置恢复
- 调用底层 HAL 恢复接口完成引脚配置恢复
- 支持透传恢复所需参数

**前置条件**

- 调用时序约束：当前接口必须在 uapi_pin_init 成功返回后调用
- 依赖关系：当前接口依赖底层 HAL 引脚操作接口已注册

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| arg | uintptr_t | 恢复所需要的参数 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 恢复操作成功，或 HAL 引脚操作接口未注册时直接返回成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | HAL 恢复接口执行失败 |

**参考案例**

- `src/middleware/chips/ws53/pm/pm_sleep/pm_sleep_porting.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_PINCTRL_SUPPORT_LPM | 特性宏 | 支持低功耗挂起与恢复功能（接口级） | n |

## Type definitions

### typedef_errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

被本模块所有返回 errcode_t 的对外接口（uapi_pin_set_mode、uapi_pin_set_ds、uapi_pin_set_pull、uapi_pin_set_ie、uapi_pin_set_st、uapi_pin_suspend、uapi_pin_resume）作为返回值类型。 
## Enumerations

### enum_pin_t <a id="enum_pin_t"></a>

```c
// 源码原始定义，保留注释
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
| S_MGPIO0 | 0 | MGPIO0 |
| S_MGPIO1 | 38 | MGPIO1，等价于 AGPIO6（AON） |
| S_MGPIO2 | 2 | MGPIO2 |
| S_MGPIO3 | 3 | MGPIO3 |
| S_MGPIO4 | 4 | MGPIO4 |
| S_MGPIO5 | 5 | MGPIO5 |
| S_MGPIO6 | 32 | MGPIO6，等价于 AGPIO0（AON） |
| S_MGPIO7 | 41 | MGPIO7，等价于 AGPIO9（AON） |
| S_MGPIO8 | 8 | MGPIO8 |
| S_MGPIO9 | 9 | MGPIO9 |
| S_MGPIO10 | 10 | MGPIO10 |
| S_MGPIO11 | 39 | MGPIO11，等价于 AGPIO7（AON） |
| S_MGPIO12 | 12 | MGPIO12 |
| S_MGPIO13 | 13 | MGPIO13 |
| S_MGPIO14 | 45 | MGPIO14，与 SGPIO0 相同（SEC GPIO） |
| S_MGPIO15 | 46 | MGPIO15，与 SGPIO1 相同（SEC GPIO） |
| S_MGPIO16 | 40 | MGPIO16，等价于 AGPIO8（AON） |
| S_MGPIO17 | 17 | MGPIO17 |
| S_MGPIO18 | 18 | MGPIO18 |
| S_MGPIO19 | 19 | MGPIO19 |
| S_MGPIO20 | 20 | MGPIO20 |
| S_MGPIO21 | 47 | MGPIO21，与 SGPIO2 相同（SEC GPIO） |
| S_MGPIO22 | 22 | MGPIO22 |
| S_MGPIO30 | 30 | MGPIO30 |
| S_MGPIO31 | 31 | MGPIO31 |
| S_AGPIO0 | 32 | AGPIO0，别名 S_MGPIO6 |
| S_AGPIO1 | 33 | AGPIO1 |
| S_AGPIO2 | 34 | AGPIO2 |
| S_AGPIO3 | 35 | AGPIO3 |
| S_AGPIO4 | 36 | AGPIO4 |
| S_AGPIO5 | 37 | AGPIO5 |
| S_AGPIO6 | 38 | AGPIO6，别名 S_MGPIO1 |
| S_AGPIO7 | 39 | AGPIO7，别名 S_MGPIO11 |
| S_AGPIO8 | 40 | AGPIO8，别名 S_MGPIO16 |
| S_AGPIO9 | 41 | AGPIO9，别名 S_MGPIO7 |
| S_AGPIO10 | 42 | AGPIO10，RTC_IN |
| S_AGPIO11 | 43 | AGPIO11，RTC_OUT |
| S_AGPIO12 | 44 | AGPIO12，RST_N（不能作为 GPIO，不能配置 pinmux，但可配置 padctrl） |
| S_SGPIO0 | 45 | SGPIO0（SEC GPIO），别名 S_MGPIO14 |
| S_SGPIO1 | 46 | SGPIO1（SEC GPIO），别名 S_MGPIO15 |
| S_SGPIO2 | 47 | SGPIO2（SEC GPIO），别名 S_MGPIO21 |
| PIN_NONE | 48 | 无效/未使用引脚编号，并作为引脚数量上界 PIN_MAX_NUMBER |

**使用说明**

被本模块所有对外接口的 pin 入参作为引脚编号类型。 
### enum_pin_mode_t <a id="enum_pin_mode_t"></a>

```c
// 源码原始定义
typedef enum {
    PIN_MODE_0        = 0,
    PIN_MODE_1        = 1,
    PIN_MODE_2        = 2,
    PIN_MODE_3        = 3,
    PIN_MODE_4        = 4,
    PIN_MODE_5        = 5,
    PIN_MODE_6        = 6,
    PIN_MODE_7        = 7,
    PIN_MODE_MAX
} pin_mode_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| PIN_MODE_0 | 0 | 复用模式 0 |
| PIN_MODE_1 | 1 | 复用模式 1 |
| PIN_MODE_2 | 2 | 复用模式 2 |
| PIN_MODE_3 | 3 | 复用模式 3 |
| PIN_MODE_4 | 4 | 复用模式 4 |
| PIN_MODE_5 | 5 | 复用模式 5 |
| PIN_MODE_6 | 6 | 复用模式 6 |
| PIN_MODE_7 | 7 | 复用模式 7 |
| PIN_MODE_MAX | 8 | 复用模式上界，无效值 |

**使用说明**

被 uapi_pin_set_mode 入参与 uapi_pin_get_mode 返回值使用。

### enum_pin_drive_strength_t <a id="enum_pin_drive_strength_t"></a>

```c
// 源码原始定义
typedef enum {
    PIN_DS_0    = 0,
    PIN_DS_1    = 1,
    PIN_DS_2    = 2,
    PIN_DS_3    = 3,
    PIN_DS_4    = 4,
    PIN_DS_5    = 5,
    PIN_DS_6    = 6,
    PIN_DS_7    = 7,
    PIN_DS_8    = 8,
    PIN_DS_9    = 9,
    PIN_DS_10   = 10,
    PIN_DS_11   = 11,
    PIN_DS_12   = 12,
    PIN_DS_13   = 13,
    PIN_DS_14   = 14,
    PIN_DS_15   = 15,
    PIN_DS_MAX
} pin_drive_strength_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| PIN_DS_0 | 0 | 驱动能力等级 0 |
| PIN_DS_1 | 1 | 驱动能力等级 1 |
| PIN_DS_2 | 2 | 驱动能力等级 2 |
| PIN_DS_3 | 3 | 驱动能力等级 3 |
| PIN_DS_4 | 4 | 驱动能力等级 4 |
| PIN_DS_5 | 5 | 驱动能力等级 5 |
| PIN_DS_6 | 6 | 驱动能力等级 6 |
| PIN_DS_7 | 7 | 驱动能力等级 7 |
| PIN_DS_8 | 8 | 驱动能力等级 8 |
| PIN_DS_9 | 9 | 驱动能力等级 9 |
| PIN_DS_10 | 10 | 驱动能力等级 10 |
| PIN_DS_11 | 11 | 驱动能力等级 11 |
| PIN_DS_12 | 12 | 驱动能力等级 12 |
| PIN_DS_13 | 13 | 驱动能力等级 13 |
| PIN_DS_14 | 14 | 驱动能力等级 14 |
| PIN_DS_15 | 15 | 驱动能力等级 15 |
| PIN_DS_MAX | 16 | 驱动能力上界，无效值 |

**使用说明**

被 uapi_pin_set_ds 入参与 uapi_pin_get_ds 返回值使用。

### enum_pin_pull_t <a id="enum_pin_pull_t"></a>

```c
// 源码原始定义
typedef enum {
    PIN_PULL_NONE = 0,
    PIN_PULL_UP   = 1,
    PIN_PULL_DOWN = 2,
    PIN_PULL_MAX
} pin_pull_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| PIN_PULL_NONE | 0 | 无上下拉 |
| PIN_PULL_UP | 1 | 上拉 |
| PIN_PULL_DOWN | 2 | 下拉 |
| PIN_PULL_MAX | 3 | 上下拉上界，无效值 |

**使用说明**

被 uapi_pin_set_pull 入参与 uapi_pin_get_pull 返回值使用。

### enum_pin_schmitt_trigger_t <a id="enum_pin_schmitt_trigger_t"></a>

```c
// 源码原始定义
typedef enum {
    PIN_ST_DISABLE = 0,
    PIN_ST_ENABLE = 1,
    PIN_ST_MAX,
} pin_schmitt_trigger_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| PIN_ST_DISABLE | 0 | 施密特触发关闭 |
| PIN_ST_ENABLE | 1 | 施密特触发使能 |
| PIN_ST_MAX | 2 | 施密特触发上界，无效值 |

**使用说明**

被 uapi_pin_set_st 入参与 uapi_pin_get_st 返回值使用。

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a> [SDK公共共享宏]

```c
#define ERRCODE_SUCC                                        0UL
```

### ERRCODE_PIN_INVALID_PARAMETER <a id="ERRCODE_PIN_INVALID_PARAMETER"></a> [SDK公共共享宏]

```c
#define ERRCODE_PIN_INVALID_PARAMETER                       0x80001190
```

### ERRCODE_PIN_MODE_NO_FUNC <a id="ERRCODE_PIN_MODE_NO_FUNC"></a> [SDK公共共享宏]

```c
#define ERRCODE_PIN_MODE_NO_FUNC                            0x80001191
```

### ERRCODE_PIN_NOT_INIT <a id="ERRCODE_PIN_NOT_INIT"></a> [SDK公共共享宏]

```c
#define ERRCODE_PIN_NOT_INIT                                0x80001192
```
