# security_init

security_hw_security_init 子模块提供硬件安全子系统（security_unified）的环境初始化、去初始化、深睡挂起与唤醒恢复能力，以及安全驱动中断等待模式的开关控制；并向第三方 mbedtls (mbed Transport Layer Security / Cryptography) 密码库注册本芯片硬件加速密码接口的对接适配函数，使 mbedtls 通过安全驱动完成加解密运算。

**头文件清单**

```c
#include "include/driver/security_unified/security_init.h"
#include "include/driver/security_unified/mbedtls_harden_adapt.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [mbedtls_adapt_register_func](#mbedtls_adapt_register_func) | 向第三方 mbedtls 注册本模块硬件密码接口的对接适配函数 |
| [uapi_drv_cipher_env_init](#uapi_drv_cipher_env_init) | 初始化安全驱动模块运行环境 |
| [uapi_drv_cipher_env_deinit](#uapi_drv_cipher_env_deinit) | 去初始化安全驱动模块运行环境 |
| [uapi_drv_cipher_env_resume](#uapi_drv_cipher_env_resume) | 系统深睡唤醒后恢复安全驱动模块运行环境 |
| [uapi_drv_cipher_env_suspend](#uapi_drv_cipher_env_suspend) | 系统进入深睡前挂起安全驱动模块运行环境 |
| [uapi_drv_cipher_wait_func_disable_all](#uapi_drv_cipher_wait_func_disable_all) | 关闭安全驱动模块中断等待模式 |
| [uapi_drv_cipher_wait_func_enable_all](#uapi_drv_cipher_wait_func_enable_all) | 打开安全驱动模块中断等待模式 |

## Functions

### mbedtls_adapt_register_func <a id="mbedtls_adapt_register_func"></a>

```c
int32_t mbedtls_adapt_register_func(void)
```

**头文件清单**

```c
#include "include/driver/security_unified/mbedtls_harden_adapt.h"
```

**功能说明**

- 向第三方 mbedtls 密码库注册本芯片安全驱动提供的硬件加速密码对接适配函数
- 注册范围覆盖对称加解密、哈希、ECP (Elliptic Curve Point) 椭圆曲线运算等适配入口
- 供系统侧 mbedtls harden 对接流程在第三方对接能力开启时调用，将 mbedtls 运算导向安全驱动

**前置条件**

- 调用时序约束：当前接口需在安全驱动模块环境初始化成功后调用，确保安全驱动底层资源就绪
- 依赖关系：当前接口依赖 mbedtls 第三方对接宏 MBEDTLS_HARDEN_OPEN 已开启，且 mbedtls 平台已初始化
- 上下文限制：当前接口由系统对接适配层调用，禁止在用户业务代码或中断上下文直接调用

**返回值**

- 返回类型：int32_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 注册成功 | 对接适配函数注册流程执行完成 |

**参考案例**

- `src/application/ws53/ws53_application/main.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 模块（含 mbedtls_harden_adapt 子组件）源文件参与编译 | y |
| MBEDTLS_HARDEN_OPEN | 特性宏 | 控制 mbedtls 硬件对接特性启用（CMake PUBLIC_DEFINES 注入，无 Kconfig 声明），开启后对接适配层调用当前接口 | 由构建目标决定 |

### uapi_drv_cipher_env_init <a id="uapi_drv_cipher_env_init"></a>

```c
void uapi_drv_cipher_env_init(void)
```

**头文件清单**

```c
#include "include/driver/security_unified/security_init.h"
```

**功能说明**

- 初始化安全驱动模块运行环境，为安全相关业务运行提供基础
- 供系统初始化阶段在运行安全相关业务前调用，建立安全驱动可用状态
- 本接口由系统侧调用，非用户业务接口

**前置条件**

- 调用时序约束：当前接口在系统启动初始化阶段调用，需在安全驱动底层模块资源就绪后执行
- 上下文限制：当前接口由系统初始化流程调用，禁止在用户业务代码或中断上下文直接调用

**参考案例**

- `src/application/ws53/ws53_application/main.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 模块（含 security_init.c）源文件参与编译 | y |

### uapi_drv_cipher_env_deinit <a id="uapi_drv_cipher_env_deinit"></a>

```c
void uapi_drv_cipher_env_deinit(void)
```

**头文件清单**

```c
#include "include/driver/security_unified/security_init.h"
```

**功能说明**

- 去初始化安全驱动模块运行环境，释放运行期建立的可用状态
- 供系统侧在进入深睡前调用，将安全驱动置于去初始化状态
- 本接口由系统侧调用，非用户业务接口

**前置条件**

- 调用时序约束：当前接口需在安全驱动模块已完成初始化后调用
- 上下文限制：当前接口由系统去初始化流程调用，禁止在用户业务代码或中断上下文直接调用

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 模块（含 security_init.c）源文件参与编译 | y |

### uapi_drv_cipher_env_resume <a id="uapi_drv_cipher_env_resume"></a>

```c
void uapi_drv_cipher_env_resume(void)
```

**头文件清单**

```c
#include "include/driver/security_unified/security_init.h"
```

**功能说明**

- 系统深睡唤醒后恢复安全驱动模块运行环境
- 供系统侧深睡唤醒恢复流程调用，重建安全驱动可用状态
- 本接口由系统侧调用，非用户业务接口

**前置条件**

- 调用时序约束：当前接口在系统深睡唤醒恢复流程中调用，需在深睡前已执行对应的挂起操作
- 上下文限制：当前接口由系统唤醒恢复流程调用，禁止在用户业务代码或中断上下文直接调用

**参考案例**

- `src/middleware/chips/ws53/pm/pm_sleep/pm_sleep_porting.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 模块（含 security_init.c）源文件参与编译 | y |

### uapi_drv_cipher_env_suspend <a id="uapi_drv_cipher_env_suspend"></a>

```c
void uapi_drv_cipher_env_suspend(void)
```

**头文件清单**

```c
#include "include/driver/security_unified/security_init.h"
```

**功能说明**

- 系统进入深睡前挂起安全驱动模块运行环境
- 供系统侧深睡挂起流程调用，将安全驱动转入挂起状态
- 本接口由系统侧调用，非用户业务接口

**前置条件**

- 调用时序约束：当前接口在系统进入深睡的挂起流程中调用
- 上下文限制：当前接口由系统挂起流程调用，禁止在用户业务代码或中断上下文直接调用

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 模块（含 security_init.c）源文件参与编译 | y |

### uapi_drv_cipher_wait_func_disable_all <a id="uapi_drv_cipher_wait_func_disable_all"></a>

```c
void uapi_drv_cipher_wait_func_disable_all(void)
```

**头文件清单**

```c
#include "include/driver/security_unified/security_init.h"
```

**功能说明**

- 关闭安全驱动模块的中断等待模式
- 在 NMI (Non-Maskable Interrupt) 中需调用本接口关闭安全驱动的中断
- 本接口由系统侧调用，非用户业务接口

**前置条件**

- 调用时序约束：当前接口需在安全驱动模块已初始化后调用
- 上下文限制：当前接口在 NMI 等需要关闭安全驱动中断的上下文中调用

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 模块（含 security_init.c）源文件参与编译 | y |

### uapi_drv_cipher_wait_func_enable_all <a id="uapi_drv_cipher_wait_func_enable_all"></a>

```c
void uapi_drv_cipher_wait_func_enable_all(void)
```

**头文件清单**

```c
#include "include/driver/security_unified/security_init.h"
```

**功能说明**

- 打开安全驱动模块的中断等待模式
- 安全驱动中断默认处于打开状态，本接口用于重新使能已被关闭的中断等待模式
- 本接口由系统侧调用，非用户业务接口

**前置条件**

- 调用时序约束：当前接口需在安全驱动模块已初始化后调用
- 上下文限制：当前接口需在主线程调用，禁止在中断上下文调用

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_DRIVER_SUPPORT_SECURITY_UNIFIED | 编译参与宏 | 控制 security_unified 模块（含 security_init.c）源文件参与编译 | y |
