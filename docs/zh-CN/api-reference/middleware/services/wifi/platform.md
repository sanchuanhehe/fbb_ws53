# Platform

platform 提供平台设备控制接口，支持平台低功耗模式开关设置与单板复位功能。

**头文件清单**

```c
#include "include/middleware/services/wifi/plat_device.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [plat_set_pm_mode](#plat_set_pm_mode) | 设置平台低功耗模式开关 |
| [plat_reset_board](#plat_reset_board) | 复位单板 |

## Functions

### plat_set_pm_mode <a id="plat_set_pm_mode"></a>

```c
errcode_t plat_set_pm_mode(int32_t pm_switch)
```

**头文件清单**

```c
#include "include/middleware/services/wifi/plat_device.h"
```

**功能说明**

- 设置平台低功耗模式的开启或关闭
- 通过传入开关参数控制低功耗功能使能状态
- 返回操作执行结果

**前置条件**

- 编译依赖：当前接口实现受 CONFIG_RST_SUPPORT 宏条件编译控制，宏未定义时接口无实现
- 调用依赖：当前接口依赖平台低功耗管理子模块已就绪

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pm_switch | int32_t | 低功耗开关参数 | 0(关闭) / 1(开启) |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x0 | 执行成功 | 低功耗开关设置成功 |
| ERRCODE_FAIL:0xFFFFFFFF | 执行失败 | 低功耗开关设置失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_RST_SUPPORT | 特性宏 | 支持平台低功耗开关与单板复位接口功能（接口级）；源码引用存在但 Kconfig 未声明，接口实际不可启用 | - |

### plat_reset_board <a id="plat_reset_board"></a>

```c
errcode_t plat_reset_board(void)
```

**头文件清单**

```c
#include "include/middleware/services/wifi/plat_device.h"
```

**功能说明**

- 复位单板设备
- 触发设备级复位操作
- 返回操作执行结果

**前置条件**

- 编译依赖：当前接口实现受 CONFIG_RST_SUPPORT 宏条件编译控制，宏未定义时接口无实现
- 调用依赖：当前接口依赖设备复位功能已可用

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x0 | 执行成功 | 复位流程全部成功 |
| Other | 其他错误码，参考[errcode_t](#typedef_errcode_t) | 复位过程中任一步骤失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_RST_SUPPORT | 特性宏 | 支持平台低功耗开关与单板复位接口功能（接口级）；源码引用存在但 Kconfig 未声明，接口实际不可启用 | - |

## Type definitions

### typedef_errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块对外接口的返回值类型。[SDK公共基础类型]

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a> [SDK公共共享宏]

```c
#define ERRCODE_SUCC                                        0UL
```

### ERRCODE_FAIL <a id="ERRCODE_FAIL"></a> [SDK公共共享宏]

```c
#define ERRCODE_FAIL                                        0xFFFFFFFF
```
