# Timer

timer 提供通用硬件定时器功能，支持创建与管理软件定时器、设置单次或周期性定时超时回调、获取硬件定时器最大可设置的延时时间，并可选支持高精度专用定时与低功耗挂起/恢复特性。

**模块公共头文件**

```c
#include "include/driver/timer.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_timer_init](#uapi_timer_init) | 初始化定时器模块 |
| [uapi_timer_adapter](#uapi_timer_adapter) | 适配指定硬件定时器索引并注册中断 |
| [uapi_timer_deinit](#uapi_timer_deinit) | 去初始化定时器模块 |
| [uapi_timer_create](#uapi_timer_create) | 在指定硬件索引下创建软件定时器并返回句柄 |
| [uapi_timer_delete](#uapi_timer_delete) | 删除指定的软件定时器 |
| [uapi_timer_get_max_us](#uapi_timer_get_max_us) | 获取硬件定时器最大可设置延时时间，单位 us |
| [uapi_timer_start](#uapi_timer_start) | 启动指定定时器并注册超时回调 |
| [uapi_timer_stop](#uapi_timer_stop) | 停止指定定时器 |
| [uapi_timer_get_current_time_us](#uapi_timer_get_current_time_us) | 获取底层硬件定时器当前时间，单位 us |
| [uapi_timer_start_high_precision](#uapi_timer_start_high_precision) | 启动高精度专用定时器 |
| [uapi_timer_reset_high_precision](#uapi_timer_reset_high_precision) | 重启高精度专用定时器 |
| [uapi_timer_stop_high_precision](#uapi_timer_stop_high_precision) | 停止高精度专用定时器 |
| [uapi_timer_suspend](#uapi_timer_suspend) | 挂起定时器模块 |
| [uapi_timer_resume](#uapi_timer_resume) | 恢复定时器模块 |

## Functions

### uapi_timer_init <a id="uapi_timer_init"></a>

```c
errcode_t uapi_timer_init(void)
```

**声明头文件**

```c
#include "include/driver/timer.h"
```

**功能说明**

- 初始化定时器模块的全局管理资源
- 为各硬件定时器索引准备软件定时器链表
- 重复调用时若模块已初始化则直接返回成功

**前置条件**

- 调用时序约束：当前接口为模块入口，须在使用其他定时器接口之前调用
- 依赖关系：当前接口依赖底层 HAL 定时器与定时器 porting 层资源可访问
- 上下文限制：可在任务上下文调用

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 初始化成功或模块已初始化 |
| ERRCODE_MEMSET:0x80000003 | 内存设置失败 | 软件定时器链表清零失败 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 软件定时器链表初始化失败 |

**参考案例**

- `src/application/samples/peripheral/timer/timer_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_TIMER_SUPPORT_LPC | 特性宏 | 支持低功耗时钟控制特性（分支级） | n |

### uapi_timer_adapter <a id="uapi_timer_adapter"></a>

```c
errcode_t uapi_timer_adapter(timer_index_t index, uint32_t int_id, uint16_t int_priority)
```

**声明头文件**

```c
#include "include/driver/timer.h"
```

**功能说明**

- 适配指定硬件定时器索引，初始化底层 HAL 定时器
- 注册该索引对应的中断号与中断优先级
- 同一索引重复适配时直接返回成功

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_timer_init](#uapi_timer_init) 成功返回后调用
- 依赖关系：当前接口依赖 HAL 定时器初始化接口与中断注册接口可用
- 上下文限制：可在任务上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| index | [timer_index_t](#enum_timer_index_t) | 硬件定时器索引，须小于 TIMER_MAX_NUM | [TIMER_INDEX_0](#enum_timer_index_t):0 / [TIMER_INDEX_1](#enum_timer_index_t):1 / [TIMER_INDEX_2](#enum_timer_index_t):2（CONFIG_TIMER_MAX_NUM > 2 时存在） |
| int_id | uint32_t | 硬件定时器中断 ID | 有效中断号 |
| int_priority | uint16_t | 硬件定时器中断优先级 | 有效中断优先级 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 适配成功或该索引已适配 |
| ERRCODE_TIMER_NOT_INIT:0x80001324 | 定时器模块未初始化 | 模块尚未调用 uapi_timer_init |
| ERRCODE_INVALID_PARAM:0x80000001 | 参数无效 | index >= TIMER_MAX_NUM |
| ERRCODE_TIMER_USING:0x80001325 | 定时器被占用 | 该索引已被高精度定时器占用 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | HAL 定时器初始化失败 |

**参考案例**

- `src/application/samples/peripheral/timer/timer_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_TIMER_SUPPORT_HIGH_PRECISION | 特性宏 | 支持高精度定时占用检查特性（分支级） | n |

### uapi_timer_deinit <a id="uapi_timer_deinit"></a>

```c
errcode_t uapi_timer_deinit(void)
```

**声明头文件**

```c
#include "include/driver/timer.h"
```

**功能说明**

- 去初始化定时器模块，停止所有已适配的硬件定时器
- 注销各硬件定时器索引的中断注册
- 清空定时器管理资源并复位初始化状态

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_timer_init](#uapi_timer_init) 之后调用，模块未初始化时直接返回成功
- 依赖关系：当前接口依赖 HAL 定时器去初始化与中断注销接口可用
- 上下文限制：可在任务上下文调用

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 去初始化成功或模块未初始化 |

**参考案例**

- `src/application/samples/peripheral/timer/timer_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_TIMER_SUPPORT_LPC | 特性宏 | 支持低功耗时钟控制特性（分支级） | n |

### uapi_timer_create <a id="uapi_timer_create"></a>

```c
errcode_t uapi_timer_create(timer_index_t index, timer_handle_t *timer)
```

**声明头文件**

```c
#include "include/driver/timer.h"
```

**功能说明**

- 在指定硬件定时器索引下创建一个软件定时器
- 分配软件定时器链表中的空闲表项并置为使能
- 通过出参返回该软件定时器的句柄

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_timer_init](#uapi_timer_init) 成功返回后调用
- 依赖关系：当前接口依赖对应索引已完成适配（[uapi_timer_adapter](#uapi_timer_adapter)）
- 上下文限制：可在任务上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| index | [timer_index_t](#enum_timer_index_t) | 硬件定时器索引，须小于 TIMER_MAX_NUM | [TIMER_INDEX_0](#enum_timer_index_t):0 / [TIMER_INDEX_1](#enum_timer_index_t):1 / [TIMER_INDEX_2](#enum_timer_index_t):2（CONFIG_TIMER_MAX_NUM > 2 时存在） |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| timer | [timer_handle_t](#typedef_timer_handle_t) * | 创建成功的软件定时器句柄；无空闲表项时输出 NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 成功分配软件定时器表项 |
| ERRCODE_INVALID_PARAM:0x80000001 | 参数无效 | timer 为 NULL 或 index >= TIMER_MAX_NUM |
| ERRCODE_TIMER_NO_ENOUGH:0x80001320 | 软件定时器表项已满 | 该索引下软件定时器链表无空闲表项 |

**参考案例**

- `src/application/samples/peripheral/timer/timer_demo.c`

### uapi_timer_delete <a id="uapi_timer_delete"></a>

```c
errcode_t uapi_timer_delete(timer_handle_t timer)
```

**声明头文件**

```c
#include "include/driver/timer.h"
```

**功能说明**

- 删除指定的软件定时器，释放其占用的链表表项
- 将对应表项的使能标志置为无效

**前置条件**

- 调用时序约束：当前接口操作的句柄须由 [uapi_timer_create](#uapi_timer_create) 创建
- 依赖关系：当前接口依赖传入句柄对应的软件定时器表项有效
- 上下文限制：可在任务上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| timer | [timer_handle_t](#typedef_timer_handle_t) | 待删除的软件定时器句柄 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 成功删除软件定时器 |
| ERRCODE_INVALID_PARAM:0x80000001 | 参数无效 | timer 为 NULL |

**参考案例**

- `src/application/samples/peripheral/timer/timer_demo.c`

### uapi_timer_get_max_us <a id="uapi_timer_get_max_us"></a>

```c
uint32_t uapi_timer_get_max_us(void)
```

**声明头文件**

```c
#include "include/driver/timer.h"
```

**功能说明**

- 获取当前硬件定时器支持的最大可设置延时时间，单位 us
- 返回值作为 [uapi_timer_start](#uapi_timer_start) 与高精度定时接口 time_us 入参的上限参考

**前置条件**

- 依赖关系：底层定时器时钟配置（CONFIG_TIMER_CLOCK_VALUE）已确定，定时器 porting 层周期换算接口可用
- 上下文限制：无特殊上下文限制

**返回值**

- 返回类型：uint32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| uint32_t | 最大可设置的延时时间，单位 us | 调用成功，恒返回换算结果 |

### uapi_timer_start <a id="uapi_timer_start"></a>

```c
errcode_t uapi_timer_start(timer_handle_t timer, uint32_t time_us, timer_callback_t callback, uintptr_t data)
```

**声明头文件**

```c
#include "include/driver/timer.h"
```

**功能说明**

- 启动指定的软件定时器，设置超时时间与超时回调
- 设置用户数据，在超时触发时透传给回调函数
- 根据剩余周期决定是否立即重载硬件定时器

**前置条件**

- 调用时序约束：当前接口操作的句柄须由 [uapi_timer_create](#uapi_timer_create) 创建
- 依赖关系：当前接口依赖对应索引已完成适配（[uapi_timer_adapter](#uapi_timer_adapter)）且硬件定时器可用
- 上下文限制：可在任务上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| timer | [timer_handle_t](#typedef_timer_handle_t) | 待启动的软件定时器句柄 | 不为NULL |
| time_us | uint32_t | 定时器超时时间，单位 us | 大于 0 且不超过 [uapi_timer_get_max_us](#uapi_timer_get_max_us) 返回值 |
| callback | [timer_callback_t](#typedef_timer_callback_t) | 定时器超时回调函数指针；超时触发时在硬件定时器中断上下文中被调用，data 为透传参数 | 不为NULL |
| data | uintptr_t | 定时器回调函数的透传参数 | 任意值 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 成功启动软件定时器 |
| ERRCODE_INVALID_PARAM:0x80000001 | 参数无效 | timer 或 callback 为 NULL、time_us 为 0 或超过最大值 |
| ERRCODE_TIEMR_NOT_CREATED:0x80001321 | 定时器未创建 | 该句柄对应表项未使能 |

**参考案例**

- `src/application/samples/peripheral/timer/timer_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_TIMER_USING_OLD_VERSION | 特性宏 | 支持旧版本 load count 对齐特性（分支级） | n |

### uapi_timer_stop <a id="uapi_timer_stop"></a>

```c
errcode_t uapi_timer_stop(timer_handle_t timer)
```

**声明头文件**

```c
#include "include/driver/timer.h"
```

**功能说明**

- 停止指定的软件定时器，停止后用户注册的回调不会被调用
- 清空该表项的超时周期、回调与数据
- 若该索引下无运行中的定时器，停止底层硬件定时器

**前置条件**

- 调用时序约束：当前接口操作的句柄须由 [uapi_timer_create](#uapi_timer_create) 创建
- 依赖关系：当前接口依赖传入句柄对应的软件定时器表项有效
- 上下文限制：可在任务上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| timer | [timer_handle_t](#typedef_timer_handle_t) | 待停止的软件定时器句柄 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 成功停止软件定时器，或该定时器本未运行 |
| ERRCODE_INVALID_PARAM:0x80000001 | 参数无效 | timer 为 NULL |
| ERRCODE_TIEMR_NOT_CREATED:0x80001321 | 定时器未创建 | 该句柄对应表项未使能 |

**参考案例**

- `src/application/samples/peripheral/timer/timer_demo.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_TIMER_SUPPORT_HIGH_PRECISION | 特性宏 | 支持高精度定时占用标志复位特性（分支级） | n |

### uapi_timer_get_current_time_us <a id="uapi_timer_get_current_time_us"></a>

```c
errcode_t uapi_timer_get_current_time_us(timer_index_t index, uint32_t *current_time_us)
```

**声明头文件**

```c
#include "include/driver/timer.h"
```

**功能说明**

- 获取指定底层硬件定时器索引的当前计数值，换算为 us 输出

**前置条件**

- 调用时序约束：当前接口依赖对应索引的底层硬件定时器已初始化
- 依赖关系：当前接口依赖 HAL 定时器取值接口与 porting 层周期换算接口可用
- 上下文限制：可在任务上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| index | [timer_index_t](#enum_timer_index_t) | 硬件定时器索引，须小于 TIMER_MAX_NUM | [TIMER_INDEX_0](#enum_timer_index_t):0 / [TIMER_INDEX_1](#enum_timer_index_t):1 / [TIMER_INDEX_2](#enum_timer_index_t):2（CONFIG_TIMER_MAX_NUM > 2 时存在） |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| current_time_us | uint32_t * | 底层硬件定时器当前时间，单位 us，由函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 成功获取当前时间 |
| ERRCODE_INVALID_PARAM:0x80000001 | 参数无效 | index >= TIMER_MAX_NUM 或 current_time_us 为 NULL |

### uapi_timer_start_high_precision <a id="uapi_timer_start_high_precision"></a>

```c
errcode_t uapi_timer_start_high_precision(timer_index_t index, timer_trigger_mode_t mode, uint32_t time_us,
                                          timer_irq_info_t* irq_info, high_precision_timer_callback_t callback)
```

**声明头文件**

```c
#include "include/driver/timer.h"
```

**功能说明**

- 启动一个高精度专用定时器，按指定触发模式与超时时间直接驱动硬件定时器
- 注册该索引对应的中断号与中断优先级
- 超时触发时在硬件定时器中断上下文中调用用户回调

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_timer_init](#uapi_timer_init) 成功返回后调用
- 依赖关系：当前接口依赖该索引未被标准定时器占用（g_timer_useing_flag 非 STANDARD_TIMER_MODE）
- 上下文限制：可在任务上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| index | [timer_index_t](#enum_timer_index_t) | 硬件定时器索引，须小于 TIMER_MAX_NUM | [TIMER_INDEX_0](#enum_timer_index_t):0 / [TIMER_INDEX_1](#enum_timer_index_t):1 / [TIMER_INDEX_2](#enum_timer_index_t):2（CONFIG_TIMER_MAX_NUM > 2 时存在） |
| mode | [timer_trigger_mode_t](#enum_timer_trigger_mode_t) | 定时器触发模式 | [TIMER_MODE_ONE_SHOT](#enum_timer_trigger_mode_t):0 / [TIMER_MODE_PERIODIC](#enum_timer_trigger_mode_t):1 |
| time_us | uint32_t | 定时器超时时间，单位 us | 大于 0 且不超过 [uapi_timer_get_max_us](#uapi_timer_get_max_us) 返回值 |
| irq_info | [timer_irq_info_t](#struct_timer_irq_info_t) * | 中断信息结构体指针，包含中断号与优先级 | 不为NULL |
| callback | [high_precision_timer_callback_t](#typedef_high_precision_timer_callback_t) | 高精度定时器超时回调函数指针；超时触发时在硬件定时器中断上下文中调用，index 为触发的硬件定时器索引 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 成功启动高精度定时器 |
| ERRCODE_INVALID_PARAM:0x80000001 | 参数无效 | index 越界、irq_info 或 callback 为 NULL、mode 越界、time_us 为 0 或超过最大值 |
| ERRCODE_TIMER_USING:0x80001325 | 定时器被占用 | 该索引已被标准定时器占用 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | HAL 定时器初始化失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_TIMER_SUPPORT_HIGH_PRECISION | 特性宏 | 支持高精度专用定时器接口功能（接口级） | n |
| CONFIG_TIMER_SUPPORT_LPC | 特性宏 | 支持低功耗时钟控制特性（分支级） | n |

### uapi_timer_reset_high_precision <a id="uapi_timer_reset_high_precision"></a>

```c
errcode_t uapi_timer_reset_high_precision(timer_index_t index, timer_trigger_mode_t mode, uint32_t time_us)
```

**声明头文件**

```c
#include "include/driver/timer.h"
```

**功能说明**

- 重启指定索引的高精度专用定时器
- 按新的触发模式与超时时间重载硬件定时器

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_timer_start_high_precision](#uapi_timer_start_high_precision) 已将目标索引置为高精度模式后调用
- 依赖关系：当前接口依赖该索引当前处于高精度定时模式
- 上下文限制：可在任务上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| index | [timer_index_t](#enum_timer_index_t) | 硬件定时器索引，须小于 TIMER_MAX_NUM | [TIMER_INDEX_0](#enum_timer_index_t):0 / [TIMER_INDEX_1](#enum_timer_index_t):1 / [TIMER_INDEX_2](#enum_timer_index_t):2（CONFIG_TIMER_MAX_NUM > 2 时存在） |
| mode | [timer_trigger_mode_t](#enum_timer_trigger_mode_t) | 定时器触发模式 | [TIMER_MODE_ONE_SHOT](#enum_timer_trigger_mode_t):0 / [TIMER_MODE_PERIODIC](#enum_timer_trigger_mode_t):1 |
| time_us | uint32_t | 定时器超时时间，单位 us | 大于 0 且不超过 [uapi_timer_get_max_us](#uapi_timer_get_max_us) 返回值 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 成功重启高精度定时器 |
| ERRCODE_INVALID_PARAM:0x80000001 | 参数无效 | index 越界、mode 越界、time_us 为 0 或超过最大值 |
| ERRCODE_TIMER_USING:0x80001325 | 定时器被占用 | 该索引不处于高精度定时模式 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_TIMER_SUPPORT_HIGH_PRECISION | 特性宏 | 支持高精度专用定时器接口功能（接口级） | n |

### uapi_timer_stop_high_precision <a id="uapi_timer_stop_high_precision"></a>

```c
errcode_t uapi_timer_stop_high_precision(timer_index_t index)
```

**声明头文件**

```c
#include "include/driver/timer.h"
```

**功能说明**

- 停止指定索引的高精度专用定时器
- 清除该索引的高精度占用标志

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_timer_start_high_precision](#uapi_timer_start_high_precision) 已将目标索引置为高精度模式后调用
- 依赖关系：当前接口依赖该索引当前处于高精度定时模式
- 上下文限制：可在任务上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| index | [timer_index_t](#enum_timer_index_t) | 硬件定时器索引，须小于 TIMER_MAX_NUM | [TIMER_INDEX_0](#enum_timer_index_t):0 / [TIMER_INDEX_1](#enum_timer_index_t):1 / [TIMER_INDEX_2](#enum_timer_index_t):2（CONFIG_TIMER_MAX_NUM > 2 时存在） |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 成功停止高精度定时器 |
| ERRCODE_INVALID_PARAM:0x80000001 | 参数无效 | index >= TIMER_MAX_NUM |
| ERRCODE_TIMER_USING:0x80001325 | 定时器被占用 | 该索引不处于高精度定时模式 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_TIMER_SUPPORT_HIGH_PRECISION | 特性宏 | 支持高精度专用定时器接口功能（接口级） | n |
| CONFIG_TIMER_SUPPORT_LPC | 特性宏 | 支持低功耗时钟控制特性（分支级） | n |

### uapi_timer_suspend <a id="uapi_timer_suspend"></a>

```c
errcode_t uapi_timer_suspend(uintptr_t val)
```

**声明头文件**

```c
#include "include/driver/timer.h"
```

**功能说明**

- 挂起定时器模块，刷新各已适配索引的软件定时器剩余周期
- 为各索引重新设置下一次硬件中断

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_timer_init](#uapi_timer_init) 成功返回后调用
- 依赖关系：当前接口依赖各索引已完成适配（[uapi_timer_adapter](#uapi_timer_adapter)）且底层 HAL 定时器可用
- 上下文限制：可在任务上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| val | uintptr_t | 挂起参数；当前实现未使用该参数 | 任意值 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 成功挂起定时器模块 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_TIMER_SUPPORT_LPM | 特性宏 | 支持低功耗挂起/恢复接口功能（接口级） | n |

### uapi_timer_resume <a id="uapi_timer_resume"></a>

```c
errcode_t uapi_timer_resume(uintptr_t val)
```

**声明头文件**

```c
#include "include/driver/timer.h"
```

**功能说明**

- 恢复定时器模块，依据传入的补偿计数值重载各已适配索引的硬件定时器

**前置条件**

- 调用时序约束：当前接口必须在 [uapi_timer_suspend](#uapi_timer_suspend) 之后调用
- 依赖关系：当前接口依赖各索引已完成适配（[uapi_timer_adapter](#uapi_timer_adapter)）且底层 HAL 定时器可用
- 上下文限制：可在任务上下文调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| val | uintptr_t | 恢复参数，指向 uint64_t 类型的补偿计数值 | 不为NULL |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC):0x00 | 执行成功 | 成功恢复定时器模块 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_TIMER_SUPPORT_LPM | 特性宏 | 支持低功耗挂起/恢复接口功能（接口级） | n |

## Type definitions

### timer_handle_t <a id="typedef_timer_handle_t"></a>

```c
typedef void *timer_handle_t;
```

**使用说明**

作为 [uapi_timer_create](#uapi_timer_create) 的出参、[uapi_timer_delete](#uapi_timer_delete)/[uapi_timer_start](#uapi_timer_start)/[uapi_timer_stop](#uapi_timer_stop) 的入参类型，用于标识一个软件定时器。不透明类型，实现细节不公开，仅通过对外接口操作。

### timer_callback_t <a id="typedef_timer_callback_t"></a>

```c
typedef void (*timer_callback_t)(uintptr_t data);
```

**使用说明**

作为 [uapi_timer_start](#uapi_timer_start) 的入参类型，用于注册软件定时器超时回调。
- 调用时机：软件定时器超时触发硬件定时器中断时，由中断处理流程在硬件定时器中断上下文中调用（实现中 `timer_int_callback` 经 `timer_process_timers` 判空后调用）。
- 参数 data：调用方在 uapi_timer_start 中传入的 uintptr_t 透传参数，原样传入回调。
- 返回值处理：回调返回类型为 void，无返回值。

### high_precision_timer_callback_t <a id="typedef_high_precision_timer_callback_t"></a>

```c
typedef void (*high_precision_timer_callback_t)(timer_index_t index);
```

**使用说明**

作为 [uapi_timer_start_high_precision](#uapi_timer_start_high_precision) 的入参类型，用于注册高精度定时器超时回调。
- 调用时机：高精度定时器超时触发硬件定时器中断时，由该索引注册的中断处理函数调用。
- 参数 index：触发超时的硬件定时器索引。
- 返回值处理：回调返回类型为 void，无返回值。

### errcode_t <a id="typedef_errcode_t"></a> 
```c
typedef uint32_t errcode_t;
```

**使用说明**

作为本模块多个对外接口的返回类型，表示接口执行结果。
## Enumerations

### timer_index_t <a id="enum_timer_index_t"></a>

```c
typedef enum timer_index {
    TIMER_INDEX_0,                      /*!< Timer0 index. */
    TIMER_INDEX_1,                      /*!< Timer1 index. */
#if defined(CONFIG_TIMER_MAX_NUM) && (CONFIG_TIMER_MAX_NUM > 2)
    TIMER_INDEX_2,                      /*!< Timer2 index. */
#endif
    TIMER_MAX_NUM
} timer_index_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| TIMER_INDEX_0 | 0 | Timer0 索引 |
| TIMER_INDEX_1 | 1 | Timer1 索引 |
| TIMER_INDEX_2 | 2 | Timer2 索引（CONFIG_TIMER_MAX_NUM > 2 时存在） |
| TIMER_MAX_NUM | 2 或 3 | 硬件定时器索引总数上限，取值由 CONFIG_TIMER_MAX_NUM 决定（CONFIG_TIMER_MAX_NUM <= 2 时为 2，> 2 时为 3） |

### timer_trigger_mode_t <a id="enum_timer_trigger_mode_t"></a>

```c
typedef enum timer_trigger_mode {
    /** Timer mode: one shot mode. 定时器控制模式：单触发模式。 */
    TIMER_MODE_ONE_SHOT,
    /** Timer mode: periodic mode. 定时器控制模式：周期触发模式。 */
    TIMER_MODE_PERIODIC,
} timer_trigger_mode_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| TIMER_MODE_ONE_SHOT | 0 | 单次触发模式 |
| TIMER_MODE_PERIODIC | 1 | 周期触发模式 |

## Structures

### timer_irq_info_t <a id="struct_timer_irq_info_t"></a>

```c
#if defined(CONFIG_TIMER_SUPPORT_HIGH_PRECISION)
typedef struct timer_irq_info {
    /** @if Eng  irq num.
     *  @else    中断号。
     *  @endif */
    uint32_t irq;
    /** @if Eng  irq priority.
     *  @else    中断优先级。
     *  @endif */
    uint16_t priority;
} timer_irq_info_t;
#endif /* CONFIG_TIMER_SUPPORT_HIGH_PRECISION */
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| irq | uint32_t | 中断号 |
| priority | uint16_t | 中断优先级 |

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```

### ERRCODE_INVALID_PARAM <a id="ERRCODE_INVALID_PARAM"></a>

```c
#define ERRCODE_INVALID_PARAM                               0x80000001
```

### ERRCODE_MEMSET <a id="ERRCODE_MEMSET"></a>

```c
#define ERRCODE_MEMSET                                      0x80000003
```

### ERRCODE_TIMER_NO_ENOUGH <a id="ERRCODE_TIMER_NO_ENOUGH"></a>

```c
#define ERRCODE_TIMER_NO_ENOUGH                             0x80001320
```

### ERRCODE_TIEMR_NOT_CREATED <a id="ERRCODE_TIEMR_NOT_CREATED"></a>

```c
#define ERRCODE_TIEMR_NOT_CREATED                           0x80001321
```

### ERRCODE_TIMER_NOT_INIT <a id="ERRCODE_TIMER_NOT_INIT"></a>

```c
#define ERRCODE_TIMER_NOT_INIT                              0x80001324
```

### ERRCODE_TIMER_USING <a id="ERRCODE_TIMER_USING"></a>

```c
#define ERRCODE_TIMER_USING                                 0x80001325
```
