# ADC

ADC（Analog-to-Digital Converter）提供模拟信号到数字信号的转换能力。输入时钟 32MHz，12bit 分辨率，单通道采样率最大为 1Msps。共 6 个通道，支持软件配置 0～5 任意通道使能，逻辑按通道编号先低后高发起切换，完成单通道采样并完成平均值滤波后自动进行通道切换。支持 128×17bit FIFO 用于数据缓存，数据存储格式：高 3bit 为通道编号，低 14bit 为有效数据。支持对 ADC 采样数据进行平均滤波处理，平均次数支持 1（不进行平均）、2、4、8；多通道时，每个通道接收 N 个数据（平均滤波个数）再切换通道。支持 FIFO 水线中断、满中断上报，ADC 忙状态、控制器 FIFO 空满状态查询。

**模块公共头文件**

```c
#include "include/driver/adc.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_adc_init](#uapi_adc_init) | 初始化 ADC |
| [uapi_adc_deinit](#uapi_adc_deinit) | 去初始化 ADC |
| [uapi_adc_power_en](#uapi_adc_power_en) | ADC 上电/下电并使能/关闭 |
| [uapi_adc_is_using](#uapi_adc_is_using) | 查询 ADC 是否正在使用 |
| [uapi_adc_open_channel](#uapi_adc_open_channel) | 打开一个 ADC 通道 |
| [uapi_adc_close_channel](#uapi_adc_close_channel) | 关闭一个 ADC 通道 |
| [uapi_adc_auto_scan_ch_enable](#uapi_adc_auto_scan_ch_enable) | 启用单通道自动扫描 |
| [uapi_adc_auto_scan_ch_disable](#uapi_adc_auto_scan_ch_disable) | 禁用单通道自动扫描 |
| [uapi_adc_auto_scan_disable](#uapi_adc_auto_scan_disable) | 禁用全部自动扫描并下电 ADC |
| [uapi_adc_auto_scan_is_enabled](#uapi_adc_auto_scan_is_enabled) | 查询自动扫描是否已使能 |
| [uapi_adc_manual_sample](#uapi_adc_manual_sample) | 触发 ADC 手动采样 |

## Functions

### uapi_adc_init <a id="uapi_adc_init"></a>

```c
errcode_t uapi_adc_init(adc_clock_t clock)
```

**声明头文件**

```c
#include "include/driver/adc.h"
```

**功能说明**

- 初始化 ADC 模块。
- ADC 已完成初始化时再次调用直接返回成功。
- 成功初始化后本模块其他接口方可使用。

**前置条件**

- 调用时序约束：当前接口为 ADC 模块入口接口，须在其他 ADC 接口之前调用。
- 依赖关系：当前接口依赖 ADC 时钟与复位资源已就绪。
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| clock | [adc_clock_t](#enum_adc_clock) | 采样时钟参数。当前芯片版本上此参数不影响实际采样时钟配置 | [adc_clock_t](#enum_adc_clock) 全体成员 |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 操作成功，或 ADC 已完成初始化 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | HAL 初始化失败 |

**参考案例**

- `src/application/samples/peripheral/adc/adc_demo.c`
- `src/application/samples/peripheral/adc/adc_demo_inc.c`

### uapi_adc_deinit <a id="uapi_adc_deinit"></a>

```c
errcode_t uapi_adc_deinit(void)
```

**声明头文件**

```c
#include "include/driver/adc.h"
```

**功能说明**

- 去初始化 ADC。
- 关闭 ADC 时钟。
- ADC 尚未初始化时直接返回成功。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_adc_init](#uapi_adc_init) 成功返回后调用。
- 依赖关系：当前接口依赖 ADC 已初始化。
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用。

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 操作成功，或 ADC 尚未初始化 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | HAL 去初始化失败 |

**参考案例**

- `src/application/samples/peripheral/adc/adc_demo_inc.c`

### uapi_adc_power_en <a id="uapi_adc_power_en"></a>

```c
void uapi_adc_power_en(afe_scan_mode_t afe_scan_mode, bool en)
```

**声明头文件**

```c
#include "include/driver/adc.h"
```

**功能说明**

- 对 ADC 执行上电或下电。
- 选择 AFE 模拟前端精度模式（常规精度/高精度/麦克风/生物测量）。
- 在启用高精度模式（CONFIG_ADC_SUPPORT_AFE 且 CONFIG_ADC_SUPPORT_HAFE）时管理各 AFE 模式的电源状态。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_adc_init](#uapi_adc_init) 成功返回后调用。
- 依赖关系：当前接口依赖 ADC 已初始化且 HAL 函数指针表已注册。
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| afe_scan_mode | [afe_scan_mode_t](#enum_afe_scan_mode) | AFE 模拟前端精度模式 | [afe_scan_mode_t](#enum_afe_scan_mode) 全体成员 |
| en | bool | 上电或下电标志，true 表示上电，false 表示下电 | true；<br>false。 |

**参考案例**

- `src/application/samples/peripheral/adc/adc_demo.c`

### uapi_adc_is_using <a id="uapi_adc_is_using"></a>

```c
bool uapi_adc_is_using(void)
```

**声明头文件**

```c
#include "include/driver/adc.h"
```

**功能说明**

- 查询 ADC 是否处于使用（已上电）状态。
- 在启用高精度模式（CONFIG_ADC_SUPPORT_AFE 且 CONFIG_ADC_SUPPORT_HAFE）时综合判断常规精度与高精度两种 AFE 模式的电源状态。
- 返回当前 ADC 电源占用情况。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_adc_init](#uapi_adc_init) 成功返回后调用。
- 依赖关系：当前接口依赖 ADC 已初始化。
- 上下文限制：当前接口可在中断或主线程调用。

**返回值**

返回类型：bool

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| true | 使用中 | ADC 已上电 |
| false | 未使用 | ADC 未上电 |

### uapi_adc_open_channel <a id="uapi_adc_open_channel"></a>

```c
errcode_t uapi_adc_open_channel(uint8_t channel)
```

**声明头文件**

```c
#include "include/driver/adc.h"
```

**功能说明**

- 打开指定的 ADC 通道。
- 在自动扫描已使能时拒绝打开通道。
- 记录当前正在工作的通道号。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_adc_init](#uapi_adc_init) 与 [uapi_adc_power_en](#uapi_adc_power_en) 成功返回后调用。
- 依赖关系：当前接口依赖 ADC 已上电、自动扫描未使能。
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | ADC 通道号 | 0 ~ 7（实现中以 ADC_CHANNEL_MAX_NUM(8) 为上界校验，channel < 8） |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 通道打开成功 |
| [ERRCODE_ADC_INVALID_PARAMETER](#ERRCODE_ADC_INVALID_PARAMETER)：0x80001141 | 参数无效 | channel 大于等于 ADC_CHANNEL_MAX_NUM |
| [ERRCODE_ADC_SCAN_NOT_DISABLE](#ERRCODE_ADC_SCAN_NOT_DISABLE)：0x80001142 | 自动扫描未禁用 | 自动扫描已使能时调用（CONFIG_ADC_SUPPORT_AUTO_SCAN 启用时） |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | HAL 通道设置失败 |

### uapi_adc_close_channel <a id="uapi_adc_close_channel"></a>

```c
errcode_t uapi_adc_close_channel(uint8_t channel)
```

**声明头文件**

```c
#include "include/driver/adc.h"
```

**功能说明**

- 关闭指定的 ADC 通道。
- 校验入参通道与当前工作通道一致性。
- 在自动扫描已使能时拒绝关闭通道。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_adc_open_channel](#uapi_adc_open_channel) 成功打开通道后调用。
- 依赖关系：当前接口依赖 ADC 已上电、自动扫描未使能、入参通道与当前工作通道一致。
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | ADC 通道号，须与当前工作通道一致 | 0 ~ 7（须等于已打开的工作通道） |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 通道关闭成功 |
| [ERRCODE_ADC_INVALID_PARAMETER](#ERRCODE_ADC_INVALID_PARAMETER)：0x80001141 | 参数无效 | channel 与当前工作通道不一致 |
| [ERRCODE_ADC_SCAN_NOT_DISABLE](#ERRCODE_ADC_SCAN_NOT_DISABLE)：0x80001142 | 自动扫描未禁用 | 自动扫描已使能时调用（CONFIG_ADC_SUPPORT_AUTO_SCAN 启用时） |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | HAL 通道设置失败 |

### uapi_adc_auto_scan_ch_enable <a id="uapi_adc_auto_scan_ch_enable"></a>

```c
errcode_t uapi_adc_auto_scan_ch_enable(uint8_t channel, adc_scan_config_t config, adc_callback_t callback)
```

**声明头文件**

```c
#include "include/driver/adc.h"
```

**功能说明**

- 启用指定 ADC 通道的自动扫描（FIFO 全扫描或阈值扫描）。
- 配置扫描类型、扫描频率、阈值上下限等扫描参数。
- 注册自动扫描中断回调函数。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_adc_init](#uapi_adc_init) 与 [uapi_adc_power_en](#uapi_adc_power_en) 成功返回后调用，且 ADC 已上电。
- 依赖关系：当前接口依赖 ADC 已上电、CONFIG_ADC_SUPPORT_AUTO_SCAN 已启用、callback 不为 NULL。
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | ADC 通道号 | 0 ~ 7（实现中以 ADC_CHANNEL_MAX_NUM(8) 为上界校验，channel < 8） |
| config | [adc_scan_config_t](#struct_adc_scan_config) | 自动扫描配置（FIFO 全扫描或阈值扫描），含扫描类型、频率、阈值 | config.type ≤ 1；config.freq < 8（0 ~ 7） |
| callback | [adc_callback_t](#typedef_adc_callback_t) | 自动扫描中断回调函数指针 | 不为 NULL |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 自动扫描通道启用成功 |
| [ERRCODE_ADC_INVALID_PARAMETER](#ERRCODE_ADC_INVALID_PARAMETER)：0x80001141 | 参数无效 | channel、config.type、config.freq 非法或 callback 为 NULL |
| [ERRCODE_PWM_NOT_POWER_ON](#ERRCODE_PWM_NOT_POWER_ON)：0x80001084 | ADC 未上电 | ADC 未上电（adc_is_power_on 为 false）时调用 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | HAL 通道扫描配置失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_ADC_SUPPORT_AUTO_SCAN | 特性宏 | 支持自动扫描接口功能（接口级，头文件中包裹函数声明） | y |
| CONFIG_ADC_SUPPORT_LONG_SAMPLE | 特性宏 | 支持长采样上报周期特性（分支级，控制 config.long_sample_time 成员存在性） | n |

### uapi_adc_auto_scan_ch_disable <a id="uapi_adc_auto_scan_ch_disable"></a>

```c
errcode_t uapi_adc_auto_scan_ch_disable(uint8_t channel)
```

**声明头文件**

```c
#include "include/driver/adc.h"
```

**功能说明**

- 禁用指定 ADC 通道的自动扫描。
- 校验入参通道号有效性。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_adc_auto_scan_ch_enable](#uapi_adc_auto_scan_ch_enable) 成功返回后调用。
- 依赖关系：当前接口依赖 ADC 已初始化、CONFIG_ADC_SUPPORT_AUTO_SCAN 已启用。
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | ADC 通道号 | 0 ~ 7（实现中以 ADC_CHANNEL_MAX_NUM(8) 为上界校验，channel < 8） |

**返回值**

返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 自动扫描通道禁用成功 |
| [ERRCODE_ADC_INVALID_PARAMETER](#ERRCODE_ADC_INVALID_PARAMETER)：0x80001141 | 参数无效 | channel 大于等于 ADC_CHANNEL_MAX_NUM |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | HAL 通道禁用失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_ADC_SUPPORT_AUTO_SCAN | 特性宏 | 支持自动扫描接口功能（接口级，头文件中包裹函数声明） | y |

### uapi_adc_auto_scan_disable <a id="uapi_adc_auto_scan_disable"></a>

```c
void uapi_adc_auto_scan_disable(void)
```

**声明头文件**

```c
#include "include/driver/adc.h"
```

**功能说明**

- 禁用 ADC 自动扫描总控制。
- 关闭所有扫描通道。
- 关闭 ADC 电源。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_adc_auto_scan_ch_enable](#uapi_adc_auto_scan_ch_enable) 成功返回后调用。
- 依赖关系：当前接口依赖 ADC 已初始化、CONFIG_ADC_SUPPORT_AUTO_SCAN 已启用。
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用。

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_ADC_SUPPORT_AUTO_SCAN | 特性宏 | 支持自动扫描接口功能（接口级，头文件中包裹函数声明） | y |

### uapi_adc_auto_scan_is_enabled <a id="uapi_adc_auto_scan_is_enabled"></a>

```c
bool uapi_adc_auto_scan_is_enabled(void)
```

**声明头文件**

```c
#include "include/driver/adc.h"
```

**功能说明**

- 查询 ADC 自动扫描总控制是否已使能。
- 返回当前自动扫描使能状态。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_adc_init](#uapi_adc_init) 成功返回后调用。
- 依赖关系：当前接口依赖 ADC 已初始化、CONFIG_ADC_SUPPORT_AUTO_SCAN 已启用。
- 上下文限制：当前接口可在中断或主线程调用。

**返回值**

返回类型：bool

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| true | 已使能 | 自动扫描总控制已使能 |
| false | 未使能 | 自动扫描总控制未使能 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_ADC_SUPPORT_AUTO_SCAN | 特性宏 | 支持自动扫描接口功能（接口级，头文件中包裹函数声明） | y |

### uapi_adc_manual_sample <a id="uapi_adc_manual_sample"></a>

```c
int32_t uapi_adc_manual_sample(uint8_t channel)
```

**声明头文件**

```c
#include "include/driver/adc.h"
```

**功能说明**

- 触发 ADC 手动采样。
- 校验入参通道号有效性。
- 返回 ADC 采样值。

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_adc_init](#uapi_adc_init) 与 [uapi_adc_open_channel](#uapi_adc_open_channel) 成功返回后调用。
- 依赖关系：当前接口依赖 ADC 已初始化、目标通道已打开。
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| channel | uint8_t | ADC 通道号 | 0 ~ 7（实现中以 ADC_CHANNEL_MAX_NUM(8) 为上界校验，channel < 8） |

**返回值**

返回类型：int32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 采样值 | ADC 采样值 | 通道号有效，采样成功 |
| 0 | 采样失败 | channel 大于等于 ADC_CHANNEL_MAX_NUM |

## Type definitions

### typedef_adc_callback_t <a id="typedef_adc_callback_t"></a>

```c
typedef void (*adc_callback_t)(uint8_t channel, uint32_t *buffer, uint32_t length, bool *next);
```

**使用说明**

- 用于 [uapi_adc_auto_scan_ch_enable](#uapi_adc_auto_scan_ch_enable) 的入参 `callback`，作为 ADC 自动扫描中断回调函数指针类型。
- 参数 channel：自动扫描通道号（入参）。
- 参数 buffer：自动扫描采样结果存放缓冲区（出参）。
- 参数 length：扫描失败时长度为 0；FIFO 全扫描时长度为 128；阈值扫描时长度为 1（入参）。
- 参数 next：继续自动扫描或停止自动扫描（出参）。

### typedef_errcode_t <a id="typedef_errcode_t"></a>

```c
// 源码原始定义
typedef uint32_t errcode_t;
```

**使用说明**

- 本模块返回类型为 errcode_t 的对外接口的返回值类型。
## Enumerations

### enum_adc_clock <a id="enum_adc_clock"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum adc_clock {
    ADC_CLOCK_500KHZ = 0,               /*!< ADC时钟频率： 500KHZ。  */
    ADC_CLOCK_250KHZ = 1,               /*!< ADC时钟频率： 250KHZ。  */
    ADC_CLOCK_125KHZ = 2,               /*!< ADC时钟频率： 125KHZ。  */
    ADC_CLOCK_015KHZ = 3,               /*!< ADC时钟频率： 015KHZ。  */
    ADC_CLOCK_MAX,
    ADC_CLOCK_NONE = ADC_CLOCK_MAX
} adc_clock_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| ADC_CLOCK_500KHZ | 0 | ADC 时钟频率：500KHZ |
| ADC_CLOCK_250KHZ | 1 | ADC 时钟频率：250KHZ |
| ADC_CLOCK_125KHZ | 2 | ADC 时钟频率：125KHZ |
| ADC_CLOCK_015KHZ | 3 | ADC 时钟频率：015KHZ |
| ADC_CLOCK_MAX | 4 | ADC 时钟枚举上限 |
| ADC_CLOCK_NONE | 4 | ADC 时钟未指定（等同 ADC_CLOCK_MAX） |

### enum_afe_scan_mode <a id="enum_afe_scan_mode"></a>

```c
// 源码原始定义，无修改、无补充
typedef enum afe_scan_mode {
    AFE_GADC_MODE = 0,                  /*!< 模拟前端ADC常规精度模式。 */
#if defined (CONFIG_ADC_SUPPORT_HAFE)
    AFE_HADC_MODE,                      /*!< 模拟前端ADC高精度模式。 */
#elif (defined CONFIG_ADC_SUPPORT_AMIC)
    AFE_AMIC_MODE,                      /*!< 模拟前端ADC麦克风模式。 */
    AFE_BIO_MODE,                      /*!< 模拟前端ADC生物测量模式。 */
#endif
    AFE_SCAN_MODE_MAX_NUM
} afe_scan_mode_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| AFE_GADC_MODE | 0 | 模拟前端 ADC 常规精度模式 |
| AFE_HADC_MODE | 1 | 模拟前端 ADC 高精度模式（CONFIG_ADC_SUPPORT_HAFE 启用时存在） |
| AFE_AMIC_MODE | 1 | 模拟前端 ADC 麦克风模式（CONFIG_ADC_SUPPORT_AMIC 启用且 CONFIG_ADC_SUPPORT_HAFE 未启用时存在） |
| AFE_BIO_MODE | 2 | 模拟前端 ADC 生物测量模式（CONFIG_ADC_SUPPORT_AMIC 启用且 CONFIG_ADC_SUPPORT_HAFE 未启用时存在） |
| AFE_SCAN_MODE_MAX_NUM | 1 / 2 / 3 | 模拟前端扫描模式枚举上限（取值随条件编译配置而定：仅 GADC 时为 1；HAFE 启用时为 2；AMIC 启用时为 3） |

## Structures

### struct_adc_scan_config <a id="struct_adc_scan_config"></a>

```c
// 源码原始定义，保留注释
typedef struct adc_scan_config {
    uint8_t type;                       /*!< FIFO全扫描或阈值扫描。 */

    float threshold_l;                  /*!< 阈值扫描电压（v）下限。 */

    float threshold_h;                  /*!< 阈值扫描电压（v）上限。 */

    uint8_t freq;                       /*!< ADC扫描频率，用于所有频道。 */
#if defined(CONFIG_ADC_SUPPORT_LONG_SAMPLE)
    uint32_t long_sample_time;           /*!< ADC长采样上报周期（单位：毫秒）。 */
#endif
} adc_scan_config_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| type | uint8_t | FIFO 全扫描或阈值扫描（0：FIFO 全扫描；1：阈值扫描） |
| threshold_l | float | 阈值扫描电压（v）下限 |
| threshold_h | float | 阈值扫描电压（v）上限 |
| freq | uint8_t | ADC 扫描频率，用于所有通道（取值范围 0 ~ 7） |
| long_sample_time | uint32_t | ADC 长采样上报周期（单位 ms），仅在 CONFIG_ADC_SUPPORT_LONG_SAMPLE 启用时存在 |

## Macros

### ERRCODE_ADC_INVALID_PARAMETER <a id="ERRCODE_ADC_INVALID_PARAMETER"></a>

```c
#define ERRCODE_ADC_INVALID_PARAMETER                       0x80001141
```

### ERRCODE_ADC_SCAN_NOT_DISABLE <a id="ERRCODE_ADC_SCAN_NOT_DISABLE"></a>

```c
#define ERRCODE_ADC_SCAN_NOT_DISABLE                        0x80001142
```

### ERRCODE_PWM_NOT_POWER_ON <a id="ERRCODE_PWM_NOT_POWER_ON"></a>

```c
#define ERRCODE_PWM_NOT_POWER_ON                            0x80001084
```

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```
