# Barrier

barrier 提供 CPU (Central Processing Unit) 内存屏障操作，包括通用内存屏障、读内存屏障、写内存屏障以及 SMP (Symmetric Multiprocessing) 条件下的内存屏障，同时提供指令同步屏障、数据同步屏障与数据内存屏障操作。

**头文件清单**

```c
#include "kernel/osal/include/memory/osal_barrier.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_mb](#osal_mb) | 提供通用 CPU 内存屏障功能 |
| [osal_rmb](#osal_rmb) | 提供读内存屏障功能 |
| [osal_wmb](#osal_wmb) | 提供写内存屏障功能 |
| [osal_smp_mb](#osal_smp_mb) | 提供 SMP 条件下的通用内存屏障功能 |
| [osal_smp_rmb](#osal_smp_rmb) | 提供 SMP 条件下的读内存屏障功能 |
| [osal_smp_wmb](#osal_smp_wmb) | 提供 SMP 条件下的写内存屏障功能 |
| [osal_isb](#osal_isb) | 提供指令同步屏障功能 |
| [osal_dsb](#osal_dsb) | 提供数据同步屏障功能 |
| [osal_dmb](#osal_dmb) | 提供数据内存屏障功能 |

## Functions

### osal_mb <a id="osal_mb"></a>

```c
void osal_mb(void)
```

**头文件清单**

```c
#include "kernel/osal/include/memory/osal_barrier.h"
```

**功能说明**

- 提供通用 CPU 内存屏障功能
- 确保屏障之前的所有内存访问操作在屏障之后的内存访问操作执行前完成
- 对读访问和写访问均产生屏障效果

**前置条件**

- 运行环境约束：当前接口支持在 Linux 系统下调用
- 依赖关系：当前接口依赖 CPU 内存屏障指令可用

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| USER_BIT_64 | 特性宏 | 支持 64 位用户态特性（分支级，无前缀注入宏） | 由构建目标决定 |

### osal_rmb <a id="osal_rmb"></a>

```c
void osal_rmb(void)
```

**头文件清单**

```c
#include "kernel/osal/include/memory/osal_barrier.h"
```

**功能说明**

- 提供读内存屏障功能
- 确保屏障之前的所有读操作在屏障之后的读操作执行前完成
- 仅约束读访问的执行顺序

**前置条件**

- 运行环境约束：当前接口支持在 Linux 系统下调用
- 依赖关系：当前接口依赖 CPU 内存屏障指令可用

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| USER_BIT_64 | 特性宏 | 支持 64 位用户态特性（分支级，无前缀注入宏） | 由构建目标决定 |

### osal_wmb <a id="osal_wmb"></a>

```c
void osal_wmb(void)
```

**头文件清单**

```c
#include "kernel/osal/include/memory/osal_barrier.h"
```

**功能说明**

- 提供写内存屏障功能
- 确保屏障之前的所有写操作在屏障之后的写操作执行前完成
- 仅约束写访问的执行顺序

**前置条件**

- 运行环境约束：当前接口支持在 Linux 系统下调用
- 依赖关系：当前接口依赖 CPU 内存屏障指令可用

### osal_smp_mb <a id="osal_smp_mb"></a>

```c
void osal_smp_mb(void)
```

**头文件清单**

```c
#include "kernel/osal/include/memory/osal_barrier.h"
```

**功能说明**

- 提供 SMP 条件下的通用 CPU 内存屏障功能
- 在多处理器系统中确保屏障前后内存访问的全局顺序
- 屏障效果在 SMP 系统下生效

**前置条件**

- 运行环境约束：当前接口支持在 Linux 系统下调用
- 依赖关系：当前接口依赖 CPU 内存屏障指令可用

### osal_smp_rmb <a id="osal_smp_rmb"></a>

```c
void osal_smp_rmb(void)
```

**头文件清单**

```c
#include "kernel/osal/include/memory/osal_barrier.h"
```

**功能说明**

- 提供 SMP 条件下的读内存屏障功能
- 在多处理器系统中确保屏障前后读操作的全局顺序
- 屏障效果在 SMP 系统下生效

**前置条件**

- 运行环境约束：当前接口支持在 Linux 系统下调用
- 依赖关系：当前接口依赖 CPU 内存屏障指令可用

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| USER_BIT_64 | 特性宏 | 支持 64 位用户态特性（分支级，无前缀注入宏） | 由构建目标决定 |

### osal_smp_wmb <a id="osal_smp_wmb"></a>

```c
void osal_smp_wmb(void)
```

**头文件清单**

```c
#include "kernel/osal/include/memory/osal_barrier.h"
```

**功能说明**

- 提供 SMP 条件下的写内存屏障功能
- 在多处理器系统中确保屏障前后写操作的全局顺序
- 屏障效果在 SMP 系统下生效

**前置条件**

- 运行环境约束：当前接口支持在 Linux 系统下调用
- 依赖关系：当前接口依赖 CPU 内存屏障指令可用

### osal_isb <a id="osal_isb"></a>

```c
void osal_isb(void)
```

**头文件清单**

```c
#include "kernel/osal/include/memory/osal_barrier.h"
```

**功能说明**

- 提供指令同步屏障功能
- 刷新处理器流水线，确保屏障之后的指令从缓存或内存重新取指
- 确保屏障之前的上下文修改操作对屏障之后的指令可见

**前置条件**

- 运行环境约束：当前接口支持在 Linux 和 LiteOS 系统下调用
- 依赖关系：当前接口依赖 CPU 内存屏障指令可用

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIPS | 特性宏 | 支持 MIPS 架构条件编译特性（分支级） | 由构建目标决定 |
| HW_LITEOS_OPEN_VERSION_NUM | 特性宏 | 支持 LiteOS 开源版本适配特性（分支级，无前缀注入宏） | 由构建目标决定 |

### osal_dsb <a id="osal_dsb"></a>

```c
void osal_dsb(void)
```

**头文件清单**

```c
#include "kernel/osal/include/memory/osal_barrier.h"
```

**功能说明**

- 提供数据同步屏障功能
- 确保屏障之前的所有显式内存访问和 Cache、分支预测器及 TLB (Translation Lookaside Buffer) 维护操作完成后，屏障之后的指令才开始执行
- 阻塞后续指令执行直到屏障前所有操作完成

**前置条件**

- 运行环境约束：当前接口支持在 Linux 和 LiteOS 系统下调用
- 依赖关系：当前接口依赖 CPU 内存屏障指令可用

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIPS | 特性宏 | 支持 MIPS 架构条件编译特性（分支级） | 由构建目标决定 |
| CONFIG_64BIT | 特性宏 | 支持 64 位架构特性（分支级） | 由构建目标决定 |
| USER_BIT_64 | 特性宏 | 支持 64 位用户态特性（分支级，无前缀注入宏） | 由构建目标决定 |
| HW_LITEOS_OPEN_VERSION_NUM | 特性宏 | 支持 LiteOS 开源版本适配特性（分支级，无前缀注入宏） | 由构建目标决定 |

### osal_dmb <a id="osal_dmb"></a>

```c
void osal_dmb(void)
```

**头文件清单**

```c
#include "kernel/osal/include/memory/osal_barrier.h"
```

**功能说明**

- 提供数据内存屏障功能
- 确保屏障之前的所有显式内存访问在屏障之后的显式内存访问之前被观察到
- 不影响处理器上其他指令的执行顺序

**前置条件**

- 运行环境约束：当前接口支持在 Linux 和 LiteOS 系统下调用
- 依赖关系：当前接口依赖 CPU 内存屏障指令可用

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| CONFIG_MIPS | 特性宏 | 支持 MIPS 架构条件编译特性（分支级） | 由构建目标决定 |
| CONFIG_64BIT | 特性宏 | 支持 64 位架构特性（分支级） | 由构建目标决定 |
| USER_BIT_64 | 特性宏 | 支持 64 位用户态特性（分支级，无前缀注入宏） | 由构建目标决定 |
| HW_LITEOS_OPEN_VERSION_NUM | 特性宏 | 支持 LiteOS 开源版本适配特性（分支级，无前缀注入宏） | 由构建目标决定 |