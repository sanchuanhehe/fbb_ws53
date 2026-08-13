# Interrupt

interrupt 提供中断管理功能，支持中断请求的申请与释放、中断的使能与禁能、全局中断的锁定与恢复、中断亲和性设置与优先级配置，以及 tasklet 机制的初始化、调度与销毁。

**模块公共头文件**

```c
#include "osal_interrupt.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_irq_get_private_dev](#osal_irq_get_private_dev) | 获取中断处理函数的私有设备参数 |
| [osal_irq_request](#osal_irq_request) | 申请中断线并注册中断处理函数 |
| [osal_irq_free](#osal_irq_free) | 释放已申请的中断线 |
| [osal_irq_set_priority](#osal_irq_set_priority) | 设置中断优先级 |
| [osal_irq_set_affinity](#osal_irq_set_affinity) | 设置中断的 CPU 亲和性 |
| [osal_irq_enable](#osal_irq_enable) | 使能指定中断线 |
| [osal_irq_disable](#osal_irq_disable) | 禁能指定中断线 |
| [osal_irq_lock](#osal_irq_lock) | 禁用所有中断并返回禁用前的 CPSR 值 |
| [osal_irq_unlock](#osal_irq_unlock) | 使能所有中断并返回使能后的 CPSR 值 |
| [osal_irq_restore](#osal_irq_restore) | 恢复中断到 osal_irq_lock 前的状态 |
| [osal_irq_clear](#osal_irq_clear) | 清除指定中断的 pending 状态 |
| [osal_in_interrupt](#osal_in_interrupt) | 检查当前是否处于中断上下文 |
| [osal_tasklet_init](#osal_tasklet_init) | 初始化 tasklet |
| [osal_tasklet_schedule](#osal_tasklet_schedule) | 调度 tasklet 执行 |
| [osal_tasklet_kill](#osal_tasklet_kill) | 销毁 tasklet |
| [osal_tasklet_update](#osal_tasklet_update) | 更新 tasklet 的处理函数和数据 |

## Functions

### osal_irq_get_private_dev <a id="osal_irq_get_private_dev"></a>

```c
void *osal_irq_get_private_dev(void *param_dev)
```

**声明头文件**

```c
#include "osal_interrupt.h"
```

**功能说明**

- 从中断回调函数的参数中提取私有设备标识
- 将底层中断框架传入的参数转换为可直接使用的设备指针
- 返回设备标识指针，供调用方在中断处理中使用

**前置条件**

- 调用时序约束：当前接口需在中断回调函数的上下文中调用
- 依赖关系：当前接口依赖 param_dev 为有效的回调参数指针

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| param_dev | void * | 传递给中断回调函数的参数指针 | 不为NULL |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL | 私有设备标识指针 | 参数有效，成功提取设备标识 |
| NULL | 参数无效 | param_dev 为 NULL |

### osal_irq_request <a id="osal_irq_request"></a>

```c
int osal_irq_request(unsigned int irq, osal_irq_handler handler, osal_irq_handler thread_fn, const char *name, void *dev)
```

**声明头文件**

```c
#include "osal_interrupt.h"
```

**功能说明**

- 申请指定中断线并注册中断处理函数
- 支持注册主处理函数和线程化处理函数，线程化处理函数在内核线程中执行
- 通过 dev 参数传递私有设备标识，供中断处理函数使用

**前置条件**

- 调用时序约束：当前接口需在对应中断线未被占用时调用
- 依赖关系：当前接口依赖 handler 不为 NULL
- 上下文限制：Linux 用户空间下 dev 参数类型必须为 (drval_irq_arg *)

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| irq | unsigned int | 要申请的中断线编号 | 0 ~ 4294967295 |
| handler | [osal_irq_handler](#osal_irq_handler) | 中断主处理函数，中断发生时调用 | 不为NULL |
| thread_fn | [osal_irq_handler](#osal_irq_handler) | 线程化中断处理函数，为 NULL 时不创建中断线程 | - |
| name | const char * | 申请设备的 ASCII 名称 | 不为NULL |
| dev | void * | 传递给处理函数的设备标识 | - |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS(0) | 执行成功 | 中断申请成功 |
| OSAL_FAILURE(-1) | 执行失败 | handler 为 NULL 或中断申请失败 |

**参考案例**

- `src/drivers/chips/ws53/porting/adc/adc_porting.c`
- `src/drivers/chips/ws53/porting/uart/uart_porting.c`
- `src/drivers/chips/ws53/porting/spi/spi_porting.c`
- `src/drivers/chips/ws53/porting/pwm/pwm_porting.c`
- `src/drivers/drivers/driver/security_unified/init/cfbb/os/crypto_drv_irq.c`

### osal_irq_free <a id="osal_irq_free"></a>

```c
void osal_irq_free(unsigned int irq, void *dev)
```

**声明头文件**

```c
#include "osal_interrupt.h"
```

**功能说明**

- 释放已申请的中断线，撤销中断处理函数的注册
- 释放后该中断线不再由当前设备处理
- Linux 用户空间下 dev 参数必须与 osal_irq_request 中的 dev 参数一致

**前置条件**

- 调用时序约束：当前接口必须在 osal_irq_request 成功返回后调用
- 上下文限制：禁止在中断上下文中调用

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| irq | unsigned int | 要释放的中断线编号 | 0 ~ 4294967295 |
| dev | void * | 与 osal_irq_request 中相同的设备标识 | - |

**参考案例**

- `src/drivers/chips/ws53/porting/adc/adc_porting.c`
- `src/drivers/chips/ws53/porting/uart/uart_porting.c`
- `src/drivers/chips/ws53/porting/i2c/i2c_porting.c`

### osal_irq_set_priority <a id="osal_irq_set_priority"></a>

```c
int osal_irq_set_priority(unsigned int irq, unsigned short priority)
```

**声明头文件**

```c
#include "osal_interrupt.h"
```

**功能说明**

- 设置指定中断线的优先级
- 优先级设置依赖中断控制器和 CPU 架构的硬件实现
- 优先级数值的具体含义由底层硬件平台决定

**前置条件**

- 调用时序约束：当前接口需在中断线已申请后调用
- 依赖关系：当前接口依赖中断控制器的硬件实现支持优先级设置

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| irq | unsigned int | 中断线编号 | 0 ~ 4294967295 |
| priority | unsigned short | 中断优先级 | 由硬件平台决定 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS(0) | 执行成功 | 优先级设置成功 |
| OSAL_FAILURE(-1) | 执行失败 | 优先级设置失败 |

**参考案例**

- `src/drivers/chips/ws53/porting/uart/uart_porting.c`
- `src/drivers/chips/ws53/porting/spi/spi_porting.c`

### osal_irq_set_affinity <a id="osal_irq_set_affinity"></a>

```c
int osal_irq_set_affinity(unsigned int irq, const char *name, int cpu_mask)
```

**声明头文件**

```c
#include "osal_interrupt.h"
```

**功能说明**

- 设置中断在指定 CPU 上的亲和性，控制中断由哪个 CPU 处理
- 通过 cpu_mask 参数指定目标 CPU，支持单 CPU 或多 CPU 组合
- 当 cpu_mask 为 OSAL_CPU_ALL 时将中断亲和性设置为所有 CPU

**前置条件**

- 调用时序约束：当前接口需在中断线已申请后调用
- 依赖关系：当前接口依赖多核 CPU 架构支持

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| irq | unsigned int | 中断线编号 | 0 ~ 4294967295 |
| name | const char * | 中断名称 | - |
| cpu_mask | int | CPU 掩码，指定目标 CPU | [OSAL_CPU_ALL](#OSAL_CPU_ALL)(0) / [OSAL_CPU_0](#OSAL_CPU_0)(2) / [OSAL_CPU_1](#OSAL_CPU_1)(4) / [OSAL_CPU_2](#OSAL_CPU_2)(8) / [OSAL_CPU_3](#OSAL_CPU_3)(16) |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS(0) | 执行成功 | 亲和性设置成功 |
| OSAL_FAILURE(-1) | 执行失败 | 亲和性设置失败 |

### osal_irq_enable <a id="osal_irq_enable"></a>

```c
void osal_irq_enable(unsigned int irq)
```

**声明头文件**

```c
#include "osal_interrupt.h"
```

**功能说明**

- 使能指定中断线，恢复因 osal_irq_disable 禁能的中断处理
- 当使能次数与禁能次数匹配时，恢复该中断线的中断处理
- 使能后中断控制器将向 CPU 投递该中断线的中断请求

**前置条件**

- 调用时序约束：当前接口需在中断线已申请后调用
- 依赖关系：当前接口依赖对应的中断线已通过 osal_irq_request 注册

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| irq | unsigned int | 要使能的中断线编号 | 0 ~ 4294967295 |

**参考案例**

- `src/drivers/chips/ws53/porting/adc/adc_porting.c`
- `src/drivers/chips/ws53/porting/uart/uart_porting.c`
- `src/drivers/chips/ws53/porting/spi/spi_porting.c`
- `src/drivers/drivers/driver/security_unified/init/cfbb/os/crypto_drv_irq.c`

### osal_irq_disable <a id="osal_irq_disable"></a>

```c
void osal_irq_disable(unsigned int irq)
```

**声明头文件**

```c
#include "osal_interrupt.h"
```

**功能说明**

- 禁能指定中断线，阻止该中断线的中断请求被处理
- 禁能操作与使能操作支持嵌套，需配对调用
- 禁能后等待该中断线上正在执行的中断处理完成后才返回

**前置条件**

- 调用时序约束：当前接口需在中断线已申请后调用
- 依赖关系：当前接口依赖对应的中断线已通过 osal_irq_request 注册

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| irq | unsigned int | 要禁能的中断线编号 | 0 ~ 4294967295 |

**参考案例**

- `src/drivers/chips/ws53/porting/adc/adc_porting.c`
- `src/drivers/chips/ws53/porting/uart/uart_porting.c`
- `src/drivers/drivers/driver/security_unified/init/cfbb/os/crypto_drv_irq.c`

### osal_irq_lock <a id="osal_irq_lock"></a>

```c
unsigned int osal_irq_lock(void)
```

**声明头文件**

```c
#include "osal_interrupt.h"
```

**功能说明**

- 禁用所有 IRQ 和 FIQ 中断，修改 CPSR 寄存器
- 返回禁用中断前的 CPSR 值，供 osal_irq_restore 恢复使用
- 用于实现临界区保护，防止中断干扰

**前置条件**

- 上下文限制：当前接口可在任意上下文中调用

**返回值**

- 返回类型：unsigned int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| CPSR值 | 禁用中断前的 CPSR 寄存器值 | 操作成功 |

**参考案例**

- `src/drivers/drivers/driver/gpio/gpio.c`
- `src/drivers/drivers/driver/pwm/pwm.c`
- `src/drivers/drivers/driver/efuse/efuse.c`
- `src/drivers/drivers/driver/sfc/sfc.c`
- `src/drivers/chips/ws53/porting/i2c/i2c_porting.c`

### osal_irq_unlock <a id="osal_irq_unlock"></a>

```c
unsigned int osal_irq_unlock(void)
```

**声明头文件**

```c
#include "osal_interrupt.h"
```

**功能说明**

- 使能所有 IRQ 和 FIQ 中断，修改 CPSR 寄存器
- 返回使能中断后的 CPSR 值
- 与 osal_irq_lock 配合使用，实现全局中断的使能

**前置条件**

- 上下文限制：当前接口可在任意上下文中调用

**返回值**

- 返回类型：unsigned int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| CPSR值 | 使能中断后的 CPSR 寄存器值 | 操作成功 |

### osal_irq_restore <a id="osal_irq_restore"></a>

```c
void osal_irq_restore(unsigned int irq_status)
```

**声明头文件**

```c
#include "osal_interrupt.h"
```

**功能说明**

- 恢复 CPSR 寄存器到 osal_irq_lock 调用前的状态
- 通过传入 osal_irq_lock 的返回值来还原中断状态
- 用于临界区退出时恢复中断，与 osal_irq_lock 配对使用

**前置条件**

- 调用时序约束：当前接口必须在 osal_irq_lock 之后调用
- 依赖关系：当前接口依赖 irq_status 为 osal_irq_lock 的返回值

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| irq_status | unsigned int | osal_irq_lock 返回的 CPSR 值 | osal_irq_lock 的返回值 |

**参考案例**

- `src/drivers/drivers/driver/gpio/gpio.c`
- `src/drivers/drivers/driver/pwm/pwm.c`
- `src/drivers/drivers/driver/efuse/efuse.c`
- `src/drivers/drivers/driver/sfc/sfc.c`
- `src/drivers/chips/ws53/porting/i2c/i2c_porting.c`

### osal_irq_clear <a id="osal_irq_clear"></a>

```c
unsigned int osal_irq_clear(unsigned int vector)
```

**声明头文件**

```c
#include "osal_interrupt.h"
```

**功能说明**

- 清除指定中断向量的 pending 状态
- 清除后该中断不再处于挂起状态
- 用于中断处理前清除残留的 pending 标志

**前置条件**

- 调用时序约束：当前接口需在对应中断向量有效时调用
- 依赖关系：当前接口依赖中断控制器支持 pending 状态清除操作

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| vector | unsigned int | 中断向量编号 | 0 ~ 4294967295 |

**返回值**

- 返回类型：unsigned int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS(0) | 执行成功 | pending 状态清除成功 |
| Other | 其他错误码 | pending 状态清除失败 |

**参考案例**

- `src/drivers/chips/ws53/porting/spi/spi_porting.c`
- `src/drivers/chips/ws53/porting/timer/timer_porting.c`

### osal_in_interrupt <a id="osal_in_interrupt"></a>

```c
int osal_in_interrupt(void)
```

**声明头文件**

```c
#include "osal_interrupt.h"
```

**功能说明**

- 检查当前是否处于硬中断、软中断或不可屏蔽中断上下文中
- 返回布尔值指示当前执行环境
- 用于在代码中区分中断上下文与非中断上下文

**前置条件**

- 上下文限制：当前接口可在任意上下文中调用

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| true | 当前处于中断上下文 | 在硬中断/软中断/不可屏蔽中断上下文中调用 |
| false | 当前不处于中断上下文 | 在非中断上下文中调用 |

### osal_tasklet_init <a id="osal_tasklet_init"></a>

```c
int osal_tasklet_init(osal_tasklet *tasklet)
```

**声明头文件**

```c
#include "osal_interrupt.h"
```

**功能说明**

- 初始化 tasklet 结构体，为 tasklet 分配资源
- 初始化前需设置 osal_tasklet 的 handler 和 data 成员，tasklet 成员置空
- 初始化后 tasklet 可通过 osal_tasklet_schedule 进行调度

**前置条件**

- 调用时序约束：当前接口需在 osal_tasklet_schedule 之前调用
- 依赖关系：当前接口依赖 tasklet 不为 NULL 且 tasklet->tasklet 为空

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| tasklet | [osal_tasklet](#osal_tasklet) * | 待初始化的 tasklet 指针 | 不为NULL，handler 和 data 成员已赋值，tasklet 成员为空 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS(0) | 执行成功 | tasklet 初始化成功 |
| OSAL_FAILURE(-1) | 执行失败 | tasklet 为 NULL 或 tasklet->tasklet 不为空或内存分配失败 |

### osal_tasklet_schedule <a id="osal_tasklet_schedule"></a>

```c
int osal_tasklet_schedule(osal_tasklet *tasklet)
```

**声明头文件**

```c
#include "osal_interrupt.h"
```

**功能说明**

- 将 tasklet 加入调度队列并触发执行
- tasklet 在同一时刻仅在一个 CPU 上运行
- 调度后 tasklet 的处理函数将在合适的时机被调用

**前置条件**

- 调用时序约束：当前接口必须在 osal_tasklet_init 成功返回后调用
- 依赖关系：当前接口依赖 tasklet 已初始化且 tasklet->tasklet 不为空

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| tasklet | [osal_tasklet](#osal_tasklet) * | 待调度的 tasklet 指针 | 不为NULL，已通过 osal_tasklet_init 初始化 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS(0) | 执行成功 | tasklet 调度成功 |
| OSAL_FAILURE(-1) | 执行失败 | tasklet 为 NULL 或 tasklet->tasklet 为空 |

### osal_tasklet_kill <a id="osal_tasklet_kill"></a>

```c
int osal_tasklet_kill(osal_tasklet *tasklet)
```

**声明头文件**

```c
#include "osal_interrupt.h"
```

**功能说明**

- 销毁 tasklet，释放其占用的资源
- 销毁后 tasklet 不再可被调度执行
- 销毁操作会等待 tasklet 当前执行完成后再释放

**前置条件**

- 调用时序约束：当前接口必须在 osal_tasklet_init 成功返回后调用
- 依赖关系：当前接口依赖 tasklet 已初始化且 tasklet->tasklet 不为空

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| tasklet | [osal_tasklet](#osal_tasklet) * | 待销毁的 tasklet 指针 | 不为NULL，已通过 osal_tasklet_init 初始化 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS(0) | 执行成功 | tasklet 销毁成功 |
| OSAL_FAILURE(-1) | 执行失败 | tasklet 为 NULL 或 tasklet->tasklet 为空 |

### osal_tasklet_update <a id="osal_tasklet_update"></a>

```c
int osal_tasklet_update(osal_tasklet *tasklet)
```

**声明头文件**

```c
#include "osal_interrupt.h"
```

**功能说明**

- 更新 tasklet 的处理函数和数据
- 更新后后续调度将使用新的处理函数和数据
- 需在 osal_tasklet_init 成功后调用

**前置条件**

- 调用时序约束：当前接口必须在 osal_tasklet_init 成功返回后调用
- 依赖关系：当前接口依赖 tasklet 已初始化且 tasklet->tasklet 不为空

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| tasklet | [osal_tasklet](#osal_tasklet) * | 待更新的 tasklet 指针 | 不为NULL，handler 和 data 成员已赋新值 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS(0) | 执行成功 | tasklet 更新成功 |
| OSAL_FAILURE(-1) | 执行失败 | tasklet 为 NULL 或 tasklet->tasklet 为空 |

## Type definitions

### osal_irq_handler <a id="osal_irq_handler"></a>

```c
typedef int (*osal_irq_handler)(int, void *);
```

**使用说明**

中断处理回调函数指针类型，中断发生时由中断框架调用。回调说明：在中断触发时调用；第一个 int 参数为中断号，第二个 void * 参数为注册时传入的设备标识；回调返回 [osal_irqreturn](#osal_irqreturn) 枚举成员 OSAL_IRQ_NONE 表示中断未处理，返回 OSAL_IRQ_HANDLED 表示中断已处理，返回 OSAL_IRQ_WAKE_THREAD 表示唤醒线程化处理函数。

## Enumerations

### osal_irqreturn <a id="osal_irqreturn"></a>

```c
enum osal_irqreturn {
    OSAL_IRQ_NONE = (0 << 0),
    OSAL_IRQ_HANDLED = (1 << 0),
    OSAL_IRQ_WAKE_THREAD = (1 << 1),
};
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| OSAL_IRQ_NONE | 0 | 中断未处理 |
| OSAL_IRQ_HANDLED | 1 | 中断已处理 |
| OSAL_IRQ_WAKE_THREAD | 2 | 唤醒线程化中断处理函数 |

## Structures

### osal_tasklet <a id="osal_tasklet"></a>

```c
typedef struct {
    void *tasklet;
    void (*handler)(unsigned long data);
    unsigned long data;
} osal_tasklet;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| tasklet | void * | 底层 tasklet 实现指针，初始化前需置空 |
| handler | void (*)(unsigned long data) | tasklet 处理函数指针 |
| data | unsigned long | 传递给处理函数的数据 |

## Macros

### OSAL_CPU_ALL <a id="OSAL_CPU_ALL"></a>

```c
#define OSAL_CPU_ALL 0
```

### OSAL_CPU_0 <a id="OSAL_CPU_0"></a>

```c
#define OSAL_CPU_0 (1 << 1)
```

### OSAL_CPU_1 <a id="OSAL_CPU_1"></a>

```c
#define OSAL_CPU_1 (1 << 2)
```

### OSAL_CPU_2 <a id="OSAL_CPU_2"></a>

```c
#define OSAL_CPU_2 (1 << 3)
```

### OSAL_CPU_3 <a id="OSAL_CPU_3"></a>

```c
#define OSAL_CPU_3 (1 << 4)
```

### OSAL_SUCCESS <a id="OSAL_SUCCESS"></a> [SDK公共共享宏]

```c
#define OSAL_SUCCESS 0
```

### OSAL_FAILURE <a id="OSAL_FAILURE"></a> [SDK公共共享宏]

```c
#define OSAL_FAILURE (-1)
```
