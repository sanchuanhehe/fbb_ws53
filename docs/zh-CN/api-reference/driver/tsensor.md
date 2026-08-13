# Tsensor

Tsensor (Temperature Sensor) 提供芯片内部温度采集功能，支持多种采样模式与温度阈值中断（过温/超限/采集完成），并提供单点与两点温度补偿校准、多级温度阈值中断配置以及当前温度值查询能力。

**模块公共头文件**

```c
#include "include/driver/tsensor.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_tsensor_init](#uapi_tsensor_init) | 初始化 Tsensor，配置采样周期、采样模式并启动采样 |
| [uapi_tsensor_get_current_temp](#uapi_tsensor_get_current_temp) | 获取 Tsensor 当前温度值 |

## Functions

### uapi_tsensor_init <a id="uapi_tsensor_init"></a>

```c
errcode_t uapi_tsensor_init(void)
```

**声明头文件**

```c
#include "include/driver/tsensor.h"
```

**功能说明**

- 初始化Tsensor模块，注册HAL (Hardware Abstraction Layer) 层函数与中断处理
- 调用该接口后，Tsensor模块进入可用状态，可进行后续查询或中断模式配置
- 重复调用该接口将返回失败，模块不支持重复初始化

**前置条件**

- Tsensor模块未初始化，即尚未调用过 `uapi_tsensor_init`
- HAL层函数已注册就绪

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC(0x0) | 执行成功 | 初始化成功 |
| Other | 其他错误码，参考errcode_t | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |

### uapi_tsensor_get_current_temp <a id="uapi_tsensor_get_current_temp"></a>

```c
errcode_t uapi_tsensor_get_current_temp(int8_t *temp)
```

**声明头文件**

```c
#include "include/driver/tsensor.h"
```

**功能说明**

- 获取Tsensor当前温度值
- 温度通过输出参数返回，单位为摄氏度
- 温度值可能无效，需通过返回值判断是否获取成功

**前置条件**

- Tsensor模块已通过 `uapi_tsensor_init` 初始化完成
- 入参temp指针不为NULL

**入参**

| 名称 | 参数类型 | 详细说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| temp | int8_t * | 温度指针，输出参数 | 非NULL，指向有效内存空间 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| temp | int8_t | 当前温度值，单位为摄氏度，获取成功时有效 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC(0x0) | 获取温度成功，温度有效 | 温度采集成功 |
| ERRCODE_TSENSOR_GET_TEMP_INVALID(0x80001363) | 获取温度失败，温度无效 | 温度采集值无效 |
| Other | 其他错误码，参考errcode_t | 执行失败 |

## Type definitions

### uapi_tsensor_callback_t <a id="typedef_uapi_tsensor_callback_t"></a>

```c
typedef errcode_t (*uapi_tsensor_callback_t)(int8_t temp);
```

**使用说明**

- Tsensor中断回调函数类型，在 `uapi_tsensor_enable_outtemp_interrupt`、`uapi_tsensor_enable_overtemp_interrupt`、`uapi_tsensor_enable_done_interrupt` 接口中作为入参使用

## Enumerations

### tsensor_samp_mode_t <a id="enum_tsensor_samp_mode"></a>

```c
typedef enum tsensor_samp_mode {
    TSENSOR_SAMP_MODE_AVERAGE_ONCE,
    TSENSOR_SAMP_MODE_AVERAGE_CYCLE,
    TSENSOR_SAMP_MODE_SINGLE_POINT_CYCLE,
    TSENSOR_SAMP_MODE_MAX_NUM,
    TSENSOR_SAMP_MODE_NONE = TSENSOR_SAMP_MODE_MAX_NUM
} tsensor_samp_mode_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| TSENSOR_SAMP_MODE_AVERAGE_ONCE | 0 | 16点平均单次上报模式 |
| TSENSOR_SAMP_MODE_AVERAGE_CYCLE | 1 | 16点平均循环上报模式 |
| TSENSOR_SAMP_MODE_SINGLE_POINT_CYCLE | 2 | 单点循环上报模式 |
| TSENSOR_SAMP_MODE_MAX_NUM | 3 | 采样模式最大数量 |
| TSENSOR_SAMP_MODE_NONE | 3 | 无效采样模式 |

## Structures

### tsensor_calibration_point_t <a id="struct_tsensor_calibration_point"></a>

```c
typedef struct tsensor_calibration_point {
    int8_t tsensor_temp;
    int8_t environment_temp;
} tsensor_calibration_point_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| tsensor_temp | int8_t | 传感器温度值，范围-40 ~ 125 |
| environment_temp | int8_t | 真实环境温度值，范围-40 ~ 125 |
