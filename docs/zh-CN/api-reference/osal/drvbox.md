# Drvbox

drvbox 提供驱动盒子（Driver Box）与用户盒子（User Box）之间的运行区域切换功能，支持在安全核心（Secure Core）场景下切换 PMP（Physical Memory Protection） / MPU（Memory Protection Unit）配置。

**模块公共头文件**

```c
#include "drvbox/osal_drvbox.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_drvmgr_switch_to_drvbox](#osal_drvmgr_switch_to_drvbox) | 从用户盒子切换到驱动盒子运行区域 |
| [osal_drvmgr_switch_to_usrbox](#osal_drvmgr_switch_to_usrbox) | 从驱动盒子切换到用户盒子运行区域 |

## Functions

### osal_drvmgr_switch_to_drvbox <a id="osal_drvmgr_switch_to_drvbox"></a>

```c
unsigned int osal_drvmgr_switch_to_drvbox(unsigned int drv_id)
```

**声明头文件**

```c
#include "drvbox/osal_drvbox.h"
```

**功能说明**

- 将当前执行区域从用户盒子切换到驱动盒子。
- 切换过程中同步修改 PMP / MPU 配置。
- 通过驱动标识校验调用者对目标驱动的访问权限。

**前置条件**

- 调用时序约束：当前接口只能在 common usr lib 中调用。
- 依赖关系：当前接口依赖 CONFIG_SEC_CORE 宏已启用，drvbox 头文件通过 soc_osal.h 在该宏条件下引入。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| drv_id | unsigned int | 用于校验调用者对驱动的访问权限的驱动标识 | - |

**返回值**

- 返回类型：unsigned int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| LOS_OK：0 | 区域切换成功 | 切换操作成功完成 |
| Other | 其他错误码，参考源码头文件注释中的 DRV_BOX_INVALID_SWITCH / DRV_BOX_SWITCH_FAIL | 执行失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SEC_CORE | 特性宏 | 安全核构建门控（接口级，soc_osal.h 以 #if defined 包裹本模块头文件引入；Kconfig 未声明） | - |

### osal_drvmgr_switch_to_usrbox <a id="osal_drvmgr_switch_to_usrbox"></a>

```c
void osal_drvmgr_switch_to_usrbox(void)
```

**声明头文件**

```c
#include "drvbox/osal_drvbox.h"
```

**功能说明**

- 将当前执行区域从驱动盒子切换到用户盒子。
- 切换过程中同步修改 PMP / MPU 配置。
- 恢复用户空间的内存保护配置。

**前置条件**

- 调用时序约束：当前接口只能在 common usr lib space 中调用。
- 依赖关系：当前接口依赖 CONFIG_SEC_CORE 宏已启用，drvbox 头文件通过 soc_osal.h 在该宏条件下引入。

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_SEC_CORE | 特性宏 | 安全核构建门控（接口级，soc_osal.h 以 #if defined 包裹本模块头文件引入；Kconfig 未声明） | - |
