# Address

Address 提供动态内存分配与释放、虚拟内存管理、内存池管理、I/O 地址映射与地址转换功能，支持 linux、LiteOS 和 FreeRTOS 多系统适配。

**模块公共头文件**

```c
#include "osal_addr.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_kmalloc](#osal_kmalloc) | 分配指定大小的动态内存 |
| [osal_kzalloc](#osal_kzalloc) | 分配指定大小的动态内存并清零 |
| [osal_kmalloc_align](#osal_kmalloc_align) | 分配指定大小且起始地址按指定边界对齐的动态内存 |
| [osal_kzalloc_align](#osal_kzalloc_align) | 分配指定大小且起始地址按指定边界对齐的动态内存并清零 |
| [osal_kfree](#osal_kfree) | 释放已分配的动态内存 |
| [osal_vmalloc](#osal_vmalloc) | 分配虚拟地址连续的内存空间 |
| [osal_vzalloc](#osal_vzalloc) | 分配虚拟地址连续的内存空间并清零 |
| [osal_vfree](#osal_vfree) | 释放由 osal_vmalloc 分配的内存 |
| [osal_pool_mem_init](#osal_pool_mem_init) | 初始化指定内存池 |
| [osal_pool_mem_alloc](#osal_pool_mem_alloc) | 从指定内存池分配动态内存 |
| [osal_pool_mem_alloc_align](#osal_pool_mem_alloc_align) | 从指定内存池分配对齐的动态内存 |
| [osal_pool_mem_free](#osal_pool_mem_free) | 从指定内存池释放动态内存 |
| [osal_pool_mem_deinit](#osal_pool_mem_deinit) | 去初始化指定内存池 |
| [osal_blockmem_get_status](#osal_blockmem_get_status) | 获取预留内存块的状态 |
| [osal_ioremap](#osal_ioremap) | 将总线地址映射为设备内存类型的 CPU 虚拟地址 |
| [osal_ioremap_nocache](#osal_ioremap_nocache) | 将总线地址映射为不可缓存的 CPU 虚拟地址 |
| [osal_ioremap_cached](#osal_ioremap_cached) | 将总线地址映射为可缓存的 CPU 虚拟地址 |
| [osal_iounmap](#osal_iounmap) | 释放 I/O 映射的虚拟地址 |
| [osal_ioremap_wc](#osal_ioremap_wc) | 将总线地址映射为写合并模式的 CPU 虚拟地址 |
| [osal_phys_to_virt](#osal_phys_to_virt) | 将物理地址转换为虚拟地址 |
| [osal_virt_to_phys](#osal_virt_to_phys) | 将虚拟地址转换为物理地址 |
| [osal_blockmem_vmap](#osal_blockmem_vmap) | 将物理地址映射到连续的内核虚拟地址空间 |
| [osal_blockmem_vunmap](#osal_blockmem_vunmap) | 释放由 osal_blockmem_vmap 映射的虚拟地址空间 |
| [osal_blockmem_free](#osal_blockmem_free) | 释放产品中已定义的预留内存 |
| [osal_copy_from_user](#osal_copy_from_user) | 从用户空间拷贝数据到内核空间 |
| [osal_copy_to_user](#osal_copy_to_user) | 从内核空间拷贝数据到用户空间 |
| [osal_access_ok](#osal_access_ok) | 检查用户空间内存块是否可用 |

## Functions

### osal_kmalloc <a id="osal_kmalloc"></a>

```c
void *osal_kmalloc(unsigned long size, unsigned int osal_gfp_flag)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 分配指定大小的动态内存块。
- 在 linux 系统下通过 osal_gfp_flag 指定内存分配类型。
- 分配失败时返回 NULL。

**前置条件**

- 上下文限制：在 linux 系统下，使用 OSAL_GFP_KERNEL 时不得在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| size | unsigned long | 需要分配的内存字节数 | > 0 |
| osal_gfp_flag | unsigned int | 内存分配标志，指定分配类型；在 LiteOS 和 FreeRTOS 下不使用 | [OSAL_GFP_ATOMIC](#OSAL_GFP_ATOMIC)：2；<br>[OSAL_GFP_DMA](#OSAL_GFP_DMA)：4；<br>[OSAL_GFP_KERNEL](#OSAL_GFP_KERNEL)：8，可按位或 [OSAL_GFP_ZERO](#OSAL_GFP_ZERO)：1。 |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL | 分配成功的内存块指针 | 内存分配成功 |
| NULL | 分配失败 | 内存不足 |

**参考案例**

- `src/application/samples/wifi/sta_sample/sta_sample.c`
- `src/application/samples/wifi/ble_wifi_cfg_sample/ble_wifi_cfg_sample.c`

### osal_kzalloc <a id="osal_kzalloc"></a>

```c
void *osal_kzalloc(unsigned long size, unsigned int osal_gfp_flag)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 分配指定大小的动态内存块并将内存内容清零。
- 在 linux 系统下通过 osal_gfp_flag 指定内存分配类型。
- 分配失败时返回 NULL。

**前置条件**

- 上下文限制：在 linux 系统下，使用 OSAL_GFP_KERNEL 时不得在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| size | unsigned long | 需要分配的内存字节数 | > 0 |
| osal_gfp_flag | unsigned int | 内存分配标志，指定分配类型；在 LiteOS 和 FreeRTOS 下不使用 | [OSAL_GFP_ATOMIC](#OSAL_GFP_ATOMIC)：2；<br>[OSAL_GFP_DMA](#OSAL_GFP_DMA)：4；<br>[OSAL_GFP_KERNEL](#OSAL_GFP_KERNEL)：8，可按位或 [OSAL_GFP_ZERO](#OSAL_GFP_ZERO)：1。 |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL | 分配成功且已清零的内存块指针 | 内存分配成功 |
| NULL | 分配失败 | 内存不足 |

### osal_kmalloc_align <a id="osal_kmalloc_align"></a>

```c
void *osal_kmalloc_align(unsigned int size, unsigned int osal_gfp_flag, unsigned int boundary)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 分配指定大小且起始地址按指定边界对齐的动态内存块。
- 在 linux 系统下通过 osal_gfp_flag 指定内存分配类型。
- 分配失败时返回 NULL。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| size | unsigned int | 需要分配的内存字节数 | > 0 |
| osal_gfp_flag | unsigned int | 内存分配标志，指定分配类型；在 LiteOS 和 FreeRTOS 下不使用 | [OSAL_GFP_ATOMIC](#OSAL_GFP_ATOMIC)：2；<br>[OSAL_GFP_DMA](#OSAL_GFP_DMA)：4；<br>[OSAL_GFP_KERNEL](#OSAL_GFP_KERNEL)：8，可按位或 [OSAL_GFP_ZERO](#OSAL_GFP_ZERO)：1。 |
| boundary | unsigned int | 内存对齐边界（单位：字节） | 2 的幂，≥ 4 |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL | 分配成功且对齐的内存块指针 | 内存分配成功 |
| NULL | 分配失败 | 内存不足或对齐参数无效 |

### osal_kzalloc_align <a id="osal_kzalloc_align"></a>

```c
void *osal_kzalloc_align(unsigned int size, unsigned int osal_gfp_flag, unsigned int boundary)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 分配指定大小且起始地址按指定边界对齐的动态内存块并将内存内容清零。
- 在 linux 系统下通过 osal_gfp_flag 指定内存分配类型。
- 分配失败时返回 NULL。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| size | unsigned int | 需要分配的内存字节数 | > 0 |
| osal_gfp_flag | unsigned int | 内存分配标志，指定分配类型；在 LiteOS 和 FreeRTOS 下不使用 | [OSAL_GFP_ATOMIC](#OSAL_GFP_ATOMIC)：2；<br>[OSAL_GFP_DMA](#OSAL_GFP_DMA)：4；<br>[OSAL_GFP_KERNEL](#OSAL_GFP_KERNEL)：8，可按位或 [OSAL_GFP_ZERO](#OSAL_GFP_ZERO)：1。 |
| boundary | unsigned int | 内存对齐边界（单位：字节） | 2 的幂，≥ 4 |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL | 分配成功且对齐并清零的内存块指针 | 内存分配成功 |
| NULL | 分配失败 | 内存不足或对齐参数无效 |

### osal_kfree <a id="osal_kfree"></a>

```c
void osal_kfree(void *addr)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 释放由 osal_kmalloc、osal_kzalloc、osal_kmalloc_align 或 osal_kzalloc_align 分配的动态内存。
- 传入 NULL 指针时函数直接返回，不执行释放操作。
- 释放后更新模块内存使用记录。

**前置条件**

- 调用时序约束：addr 指向的内存必须由 osal_kmalloc、osal_kzalloc、osal_kmalloc_align 或 osal_kzalloc_align 分配。
- 上下文限制：禁止对同一内存块重复释放。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | void * | 需要释放的内存块起始地址 | 由 osal_kmalloc 等分配的合法指针或 NULL |

**参考案例**

- `src/application/samples/wifi/sta_sample/sta_sample.c`

### osal_vmalloc <a id="osal_vmalloc"></a>

```c
void *osal_vmalloc(unsigned long size)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 分配虚拟地址连续的内存空间。
- 适用于需要大块连续虚拟内存的场景。
- 分配失败时返回 NULL。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| size | unsigned long | 需要分配的内存字节数 | > 0 |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL | 分配成功的虚拟内存指针 | 内存分配成功 |
| NULL | 分配失败 | 内存不足 |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`

### osal_vzalloc <a id="osal_vzalloc"></a>

```c
void *osal_vzalloc(unsigned long size)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 分配虚拟地址连续的内存空间并将内存内容清零。
- 适用于需要大块连续虚拟内存且要求初始化为零的场景。
- 分配失败时返回 NULL。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| size | unsigned long | 需要分配的内存字节数 | > 0 |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL | 分配成功且已清零的虚拟内存指针 | 内存分配成功 |
| NULL | 分配失败 | 内存不足 |

### osal_vfree <a id="osal_vfree"></a>

```c
void osal_vfree(void *addr)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 释放由 osal_vmalloc 或 osal_vzalloc 分配的虚拟内存。
- 传入 NULL 指针时函数直接返回，不执行释放操作。

**前置条件**

- 调用时序约束：addr 指向的内存必须由 osal_vmalloc 或 osal_vzalloc 分配。
- 上下文限制：禁止对同一内存块重复释放。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | void * | 需要释放的内存块起始地址 | 由 osal_vmalloc 或 osal_vzalloc 分配的合法指针或 NULL |

**参考案例**

- `src/application/samples/bt/ble/ble_speed_server/src/ble_speed_server.c`

### osal_pool_mem_init <a id="osal_pool_mem_init"></a>

```c
int osal_pool_mem_init(void *pool, unsigned int size)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 初始化指定内存池的双向链表动态内存。
- 在 LiteOS 下仅在 LOSCFG_MEM_MUL_MODULE 宏定义时可用。
- 在 FreeRTOS 下仅在 XLTCFG_SUPPORT_MEMMNG 宏定义时可用。

**前置条件**

- 调用时序约束：在使用内存池分配接口之前必须先调用本接口初始化内存池。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pool | void * | 内存池起始地址 | 4 或 8 字节对齐的非空指针 |
| size | unsigned int | 内存池大小（单位：字节） | 大于系统最小池大小，小于等于内存池总大小 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS：0 | 初始化成功 | 内存池初始化成功 |
| OSAL_FAILURE：-1 | 初始化失败 | 内存池初始化失败 |

### osal_pool_mem_alloc <a id="osal_pool_mem_alloc"></a>

```c
void *osal_pool_mem_alloc(void *pool, unsigned int size)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 从指定内存池分配指定大小的动态内存块。
- 分配后更新模块内存使用记录。
- 在 LiteOS 下仅在 LOSCFG_MEM_MUL_MODULE 宏定义时可用。

**前置条件**

- 调用时序约束：pool 必须已通过 osal_pool_mem_init 成功初始化。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pool | void * | 已初始化的内存池指针 | 由 osal_pool_mem_init 初始化的合法指针 |
| size | unsigned int | 需要分配的内存字节数 | 4 字节对齐，小于等于内存池大小 |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL | 分配成功的内存块指针 | 内存分配成功 |
| NULL | 分配失败 | 内存不足 |

### osal_pool_mem_alloc_align <a id="osal_pool_mem_alloc_align"></a>

```c
void *osal_pool_mem_alloc_align(void *pool, unsigned int size, unsigned int boundary)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 从指定内存池分配指定大小且起始地址按指定边界对齐的动态内存块。
- 分配后更新模块内存使用记录。
- 在 LiteOS 下仅在 LOSCFG_MEM_MUL_MODULE 宏定义时可用。

**前置条件**

- 调用时序约束：pool 必须已通过 osal_pool_mem_init 成功初始化。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pool | void * | 已初始化的内存池指针 | 由 osal_pool_mem_init 初始化的合法指针 |
| size | unsigned int | 需要分配的内存字节数 | 小于等于内存池大小 |
| boundary | unsigned int | 内存对齐边界（单位：字节） | 2 的幂，≥ 4 |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL | 分配成功且对齐的内存块指针 | 内存分配成功 |
| NULL | 分配失败 | 内存不足或对齐参数无效 |

### osal_pool_mem_free <a id="osal_pool_mem_free"></a>

```c
void osal_pool_mem_free(void *pool, const void *addr)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 从指定内存池释放已分配的动态内存。
- 在 LiteOS 下仅在 LOSCFG_MEM_MUL_MODULE 宏定义时可用。

**前置条件**

- 调用时序约束：pool 必须已通过 osal_pool_mem_init 成功初始化。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pool | void * | 内存池指针 | 由 osal_pool_mem_init 初始化的合法指针 |
| addr | const void * | 需要释放的内存块起始地址 | 由 osal_pool_mem_alloc 或 osal_pool_mem_alloc_align 分配的合法指针 |

### osal_pool_mem_deinit <a id="osal_pool_mem_deinit"></a>

```c
int osal_pool_mem_deinit(void *pool)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 去初始化指定内存池的双向链表动态内存。
- 在 LiteOS 下仅在 LOSCFG_MEM_MUL_POOL 宏定义时可用。
- 在 FreeRTOS 下仅在 XLTCFG_SUPPORT_MEMMNG 和 XLTCFG_MEM_MUL_POOL 宏定义时可用。

**前置条件**

- 调用时序约束：pool 必须已通过 osal_pool_mem_init 成功初始化。
- 上下文限制：须确保该内存池中所有已分配内存已释放。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| pool | void * | 内存池起始地址 | 由 osal_pool_mem_init 初始化的合法指针 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS：0 | 去初始化成功 | 内存池去初始化成功 |
| OSAL_FAILURE：-1 | 去初始化失败 | 内存池去初始化失败 |

### osal_blockmem_get_status <a id="osal_blockmem_get_status"></a>

```c
osal_blockmem_status osal_blockmem_get_status(unsigned long phyaddr, unsigned int size)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 获取预留内存块的状态。
- 检查指定物理地址和大小的内存块是否为有效的预留内存。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| phyaddr | unsigned long | 物理地址 | 有效的物理地址 |
| size | unsigned int | 需要检查的内存大小（单位：字节） | > 0 |

**返回值**

- 返回类型：[osal_blockmem_status](#enum_osal_blockmem_status)

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| [OSAL_BLOCKMEM_VALID](#enum_osal_blockmem_status)：0 | 内存块有效 | 所有页面均为预留内存 |
| [OSAL_BLOCKMEM_INVALID_PHYADDR](#enum_osal_blockmem_status)：1 | 物理地址无效 | 无有效预留页面 |
| [OSAL_BLOCKMEM_INVALID_SIZE](#enum_osal_blockmem_status)：2 | 大小无效 | 部分页面为预留内存，大小不匹配 |

### osal_ioremap <a id="osal_ioremap"></a>

```c
void *osal_ioremap(unsigned long phys_addr, unsigned long size)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 将总线地址映射为设备内存类型的 CPU 虚拟地址。
- 映射的内存类型为设备内存，不使用缓存。
- 映射失败时返回 NULL。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| phys_addr | unsigned long | 需要映射的总线物理地址 | 有效的物理地址 |
| size | unsigned long | 需要映射的资源大小（单位：字节） | > 0 |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL | 映射成功的虚拟地址 | 地址映射成功 |
| NULL | 映射失败 | 地址映射失败 |

### osal_ioremap_nocache <a id="osal_ioremap_nocache"></a>

```c
void *osal_ioremap_nocache(unsigned long phys_addr, unsigned long size)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 将总线地址映射为不可缓存的 CPU 虚拟地址。
- 功能与 osal_ioremap 相同，保留此接口以兼容已有驱动。
- 映射失败时返回 NULL。

**前置条件**

- 依赖关系：映射得到的虚拟地址须在不再使用时通过 osal_iounmap 释放。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| phys_addr | unsigned long | 需要映射的总线物理地址 | 有效的物理地址 |
| size | unsigned long | 需要映射的资源大小（单位：字节） | > 0 |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL | 映射成功的虚拟地址 | 地址映射成功 |
| NULL | 映射失败 | 地址映射失败 |

### osal_ioremap_cached <a id="osal_ioremap_cached"></a>

```c
void *osal_ioremap_cached(unsigned long phys_addr, unsigned long size)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 将总线地址映射为可缓存的 CPU 虚拟地址。
- 映射的内存类型为普通内存，使用缓存，可加速内存访问。
- 映射失败时返回 NULL。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| phys_addr | unsigned long | 需要映射的总线物理地址 | 有效的物理地址 |
| size | unsigned long | 需要映射的资源大小（单位：字节） | > 0 |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL | 映射成功的虚拟地址 | 地址映射成功 |
| NULL | 映射失败 | 地址映射失败 |

### osal_iounmap <a id="osal_iounmap"></a>

```c
void osal_iounmap(void *addr, unsigned long size)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 释放由 ioremap 系列接口映射的虚拟地址。
- 解除物理地址到虚拟地址的映射关系。

**前置条件**

- 调用时序约束：addr 必须由 osal_ioremap、osal_ioremap_nocache、osal_ioremap_cached 或 osal_ioremap_wc 映射获得。
- 上下文限制：同一虚拟地址指针只能执行一次 unmapping。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | void * | ioremap 系列接口返回的虚拟地址 | 由 ioremap 系列接口映射的合法虚拟地址 |
| size | unsigned long | 映射的资源大小（单位：字节） | > 0 |

### osal_ioremap_wc <a id="osal_ioremap_wc"></a>

```c
void *osal_ioremap_wc(unsigned long phys_addr, unsigned long size)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 将总线地址映射为写合并模式的 CPU 虚拟地址。
- 写合并模式可提高设备内存的写入性能。
- 映射失败时返回 NULL。

**前置条件**

- 依赖关系：映射得到的虚拟地址须在不再使用时通过 osal_iounmap 释放。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| phys_addr | unsigned long | 需要映射的总线物理地址 | 有效的物理地址 |
| size | unsigned long | 需要映射的资源大小（单位：字节） | > 0 |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL | 映射成功的虚拟地址 | 地址映射成功 |
| NULL | 映射失败 | 地址映射失败 |

### osal_phys_to_virt <a id="osal_phys_to_virt"></a>

```c
void *osal_phys_to_virt(unsigned long addr)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 将物理地址转换为虚拟地址。
- 转换结果为对应的内核虚拟地址。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | unsigned long | 物理地址 | 有效的物理地址 |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL | 转换后的虚拟地址 | 地址转换成功 |

### osal_virt_to_phys <a id="osal_virt_to_phys"></a>

```c
unsigned long osal_virt_to_phys(const void *virt_addr)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 将虚拟地址转换为物理地址。
- 转换结果为对应的物理地址。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| virt_addr | const void * | 虚拟地址 | 有效的内核虚拟地址 |

**返回值**

- 返回类型：unsigned long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非零 | 转换后的物理地址 | 地址转换成功 |

### osal_blockmem_vmap <a id="osal_blockmem_vmap"></a>

```c
void *osal_blockmem_vmap(unsigned long phys_addr, unsigned long size)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 将物理地址映射到连续的内核虚拟地址空间。
- 仅支持 VM_MAP 与 PAGE_KERNEL 标志的组合映射。
- 映射失败时返回 NULL。

**前置条件**

- 上下文限制：不得在中断上下文中调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| phys_addr | unsigned long | 物理地址 | 不为 0（实现仅对 size 判上界） |
| size | unsigned long | 需要映射的内存大小（单位：字节） | > 0，不超过 OSAL_ADDR_RESERVED_SIZE_MAX |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL | 映射成功的虚拟地址 | 地址映射成功 |
| NULL | 映射失败 | 物理地址为 0、大小为 0、大小超限或内存不足 |

### osal_blockmem_vunmap <a id="osal_blockmem_vunmap"></a>

```c
void osal_blockmem_vunmap(const void *virt_addr)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 释放由 osal_blockmem_vmap 映射的虚拟地址空间。
- 传入 NULL 指针时打印错误日志并返回。

**前置条件**

- 调用时序约束：virt_addr 必须由 osal_blockmem_vmap 映射获得。
- 上下文限制：不得在中断上下文中调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| virt_addr | const void * | 需要释放的虚拟地址 | 由 osal_blockmem_vmap 映射的合法虚拟地址 |

### osal_blockmem_free <a id="osal_blockmem_free"></a>

```c
void osal_blockmem_free(unsigned long phys_addr, unsigned long size)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 释放产品中已定义的预留内存。
- 逐页清除预留标记并释放页面。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| phys_addr | unsigned long | 预留内存的物理地址 | 不为 0 |
| size | unsigned long | 需要释放的内存大小（单位：字节） | > 0 |

### osal_copy_from_user <a id="osal_copy_from_user"></a>

```c
unsigned long osal_copy_from_user(void *to, const void *from, unsigned long n)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 从用户空间拷贝数据到内核空间。
- 拷贝成功时返回 0。
- 拷贝失败时返回未拷贝的字节数。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| to | void * | 内核空间目标地址 | 不为NULL |
| from | const void * | 用户空间源地址 | 不为NULL |
| n | unsigned long | 需要拷贝的数据长度（单位：字节） | > 0 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| to | void * | 从用户空间拷贝来的数据写入目标缓冲区 |

**返回值**

- 返回类型：unsigned long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 拷贝成功 | 数据拷贝完成 |
| 非零 | 未拷贝的字节数 | 拷贝过程中出错 |

### osal_copy_to_user <a id="osal_copy_to_user"></a>

```c
unsigned long osal_copy_to_user(void *to, const void *from, unsigned long n)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 从内核空间拷贝数据到用户空间。
- 拷贝成功时返回 0。
- 拷贝失败时返回未拷贝的字节数。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| to | void * | 用户空间目标地址 | 不为NULL |
| from | const void * | 内核空间源地址 | 不为NULL |
| n | unsigned long | 需要拷贝的数据长度（单位：字节） | > 0 |

**返回值**

- 返回类型：unsigned long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 拷贝成功 | 数据拷贝完成 |
| 非零 | 未拷贝的字节数 | 拷贝过程中出错 |

### osal_access_ok <a id="osal_access_ok"></a>

```c
int osal_access_ok(int type, const void *addr, unsigned long size)
```

**声明头文件**

```c
#include "osal_addr.h"
```

**功能说明**

- 检查用户空间内存块是否可用。
- 检查指定地址和大小的用户空间内存是否具有指定的访问权限。
- 返回 1 表示可用，返回 0 表示不可用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| type | int | 访问类型 | [OSAL_VERIFY_READ](#OSAL_VERIFY_READ)：0；<br>[OSAL_VERIFY_WRITE](#OSAL_VERIFY_WRITE)：1。 |
| addr | const void * | 用户空间内存块起始地址 | 不为NULL |
| size | unsigned long | 需要检查的内存块大小 | > 0 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 1 | 用户空间内存块可用 | 地址和大小检查通过 |
| 0 | 用户空间内存块不可用 | 地址或大小检查未通过 |

## Enumerations

### osal_blockmem_status <a id="enum_osal_blockmem_status"></a>

```c
typedef enum {
    OSAL_BLOCKMEM_VALID = 0,
    OSAL_BLOCKMEM_INVALID_PHYADDR = 1,
    OSAL_BLOCKMEM_INVALID_SIZE = 2,
    OSAL_BLOCKMEM_MAX,
} osal_blockmem_status;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| OSAL_BLOCKMEM_VALID | 0 | 预留内存块有效 |
| OSAL_BLOCKMEM_INVALID_PHYADDR | 1 | 物理地址无效 |
| OSAL_BLOCKMEM_INVALID_SIZE | 2 | 大小无效 |
| OSAL_BLOCKMEM_MAX | 3 | 枚举边界值 |

## Macros

### OSAL_GFP_ZERO <a id="OSAL_GFP_ZERO"></a>

```c
#define OSAL_GFP_ZERO (0x1)
```

### OSAL_GFP_ATOMIC <a id="OSAL_GFP_ATOMIC"></a>

```c
#define OSAL_GFP_ATOMIC (0x1 << 1)
```

### OSAL_GFP_DMA <a id="OSAL_GFP_DMA"></a>

```c
#define OSAL_GFP_DMA (0x1 << 2)
```

### OSAL_GFP_KERNEL <a id="OSAL_GFP_KERNEL"></a>

```c
#define OSAL_GFP_KERNEL (0x1 << 3)
```

### OSAL_VERIFY_READ <a id="OSAL_VERIFY_READ"></a>

```c
#define OSAL_VERIFY_READ 0
```

### OSAL_VERIFY_WRITE <a id="OSAL_VERIFY_WRITE"></a>

```c
#define OSAL_VERIFY_WRITE 1
```
