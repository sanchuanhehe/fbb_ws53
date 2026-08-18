# cache

cache 模块提供 DCache (Data Cache) 维护接口，作为 OSAL (OS Abstract Layer) 的组成部分，支持按内存区域执行 DCache 回写、失效与清理操作，覆盖 linux、liteos、seliteos 系统。

**模块公共头文件**

```c
#include "kernel/osal/include/memory/osal_cache.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_dcache_region_wb](#osal_dcache_region_wb) | 对指定内存区域执行 DCache 回写操作 |
| [osal_dcache_region_inv](#osal_dcache_region_inv) | 对指定内存区域执行 DCache 失效操作 |
| [osal_dcache_region_clean](#osal_dcache_region_clean) | 对指定内存区域执行 DCache 清理操作 |

## Functions

### osal_dcache_region_wb <a id="osal_dcache_region_wb"></a>

```c
void osal_dcache_region_wb(void *kvirt, unsigned long phys_addr, unsigned long size)
```

**声明头文件**

```c
#include "kernel/osal/include/memory/osal_cache.h"
```

**功能说明**

- 将指定内存区域的DCache数据写回主存（write-back）
- 起始地址若未按CACHE_LINE_SIZE(32Bytes)对齐，将自动向下对齐到CACHE_LINE_SIZE边界
- 当MMU (Memory Management Unit) 不存在时，需确保phys_addr有效，此时用户通过kvirt参数设置地址

**前置条件**

- 无MMU场景下，phys_addr参数必须为有效的物理地址，或通过kvirt传入有效地址

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| kvirt | void * | 内核虚拟地址指针 | 非NULL指针，指向有效内存区域 |
| phys_addr | unsigned long | 需要回写的起始物理地址 | 有效物理地址；当MMU不存在时需确保有效，若为0则使用kvirt的地址值 |
| size | unsigned long | 需要回写的内存大小（字节） | 大于0 |

**参考案例**

- `src/middleware/utils/update/common/upg_verify.c`

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| OSAL_API_SUPPORT_DCACHE | 特性宏 | linux 实现体由 #ifdef 包裹，无前缀注入宏（接口级） | 由构建目标决定 |
| LOSCFG_ARCH_ARM_CORTEX_A | 特性宏 | liteos 实现内部分支宏（分支级） | 由构建目标决定 |

### osal_dcache_region_inv <a id="osal_dcache_region_inv"></a>

```c
void osal_dcache_region_inv(void *addr, unsigned long size)
```

**声明头文件**

```c
#include "kernel/osal/include/memory/osal_cache.h"
```

**功能说明**

- 使指定内存区域的DCache缓存行失效（invalidate）
- 起始地址若未按CACHE_LINE_SIZE(32Bytes)对齐，将自动向下对齐到CACHE_LINE_SIZE边界
- 用于DMA读取前使CPU缓存失效，确保后续读取来自主存而非缓存

**前置条件**

- addr指向的内存区域必须有效且可访问

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | void * | 需要无效的起始地址 | 非NULL指针，指向有效内存区域 |
| size | unsigned long | 需要无效的内存大小（字节） | 大于0 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| OSAL_API_SUPPORT_DCACHE | 特性宏 | linux 实现体由 #ifdef 包裹，无前缀注入宏（接口级） | 由构建目标决定 |
| LOSCFG_ARCH_ARM_CORTEX_A | 特性宏 | liteos 实现内部分支宏（分支级） | 由构建目标决定 |

### osal_dcache_region_clean <a id="osal_dcache_region_clean"></a>

```c
void osal_dcache_region_clean(void *addr, unsigned int size)
```

**声明头文件**

```c
#include "kernel/osal/include/memory/osal_cache.h"
```

**功能说明**

- 将指定内存区域的DCache数据写回主存（clean）
- 根据起始地址和大小清除DCache，将脏缓存行写回主存
- 用于DMA写入前确保CPU已写入的数据已同步到主存

**前置条件**

- addr指向的内存区域必须有效且可访问

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | void * | 需要清除的起始地址 | 非NULL指针，指向有效内存区域 |
| size | unsigned int | 需要清除的内存大小（字节） | 大于0 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| LOSCFG_ARCH_ARM_CORTEX_A | 特性宏 | liteos 实现内部分支宏（分支级） | 由构建目标决定 |
