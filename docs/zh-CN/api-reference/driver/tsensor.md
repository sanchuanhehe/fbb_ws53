# Tsensor

Tsensor（Temperature Sensor）提供芯片内部温度采集功能，支持温度传感器初始化与当前温度值查询。

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

- 初始化 Tsensor 模块，配置采样周期与采样模式并启动采样。
- 初始化后可调用 [uapi_tsensor_get_current_temp](#uapi_tsensor_get_current_temp) 查询温度。
- 重复调用时再次执行初始化流程。

**前置条件**

- 调用时序约束：作为 Tsensor 模块入口，须在 get_current_temp 之前调用。

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 成功执行 | 成功初始化 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

### uapi_tsensor_get_current_temp <a id="uapi_tsensor_get_current_temp"></a>

```c
errcode_t uapi_tsensor_get_current_temp(int8_t *temp)
```

**声明头文件**

```c
#include "include/driver/tsensor.h"
```

**功能说明**

- 获取Tsensor当前温度值。
- 温度通过输出参数返回，单位为 ℃。
- 温度值可能无效，需通过返回值判断是否成功获取。

**前置条件**

- 调用时序约束：必须在 uapi_tsensor_init 成功返回后调用。

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| temp | int8_t * | 当前温度值，单位为 ℃，成功获取时有效，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [ERRCODE_SUCC](#ERRCODE_SUCC)：0 | 获取温度成功，温度有效 | 温度采集成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 执行失败 |

## Type definitions

### typedef_errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块返回类型为 errcode_t 的对外接口的返回值类型。

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a>

```c
#define ERRCODE_SUCC                                        0UL
```
