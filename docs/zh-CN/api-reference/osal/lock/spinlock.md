# Spinlock

Spinlock 提供 OSAL（OS Abstract Layer）自旋锁的初始化、加锁、解锁、尝试加锁与销毁功能，支持普通加锁、禁用软中断加锁、保存并禁用 IRQ（Interrupt Request）状态加锁等多种中断处理模式。

**模块公共头文件**

```c
#include "lock/osal_spinlock.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_spin_lock_init](#osal_spin_lock_init) | 初始化自旋锁 |
| [osal_spin_lock](#osal_spin_lock) | 获取自旋锁 |
| [osal_spin_lock_bh](#osal_spin_lock_bh) | 禁用软中断并获取自旋锁 |
| [osal_spin_trylock](#osal_spin_trylock) | 尝试获取自旋锁 |
| [osal_spin_trylock_irq](#osal_spin_trylock_irq) | 尝试获取自旋锁并禁用 CPU 中断 |
| [osal_spin_trylock_irqsave](#osal_spin_trylock_irqsave) | 保存中断状态并尝试获取自旋锁 |
| [osal_spin_unlock](#osal_spin_unlock) | 释放自旋锁 |
| [osal_spin_unlock_bh](#osal_spin_unlock_bh) | 释放自旋锁并恢复软中断 |
| [osal_spin_lock_irqsave](#osal_spin_lock_irqsave) | 保存中断状态并获取自旋锁 |
| [osal_spin_unlock_irqrestore](#osal_spin_unlock_irqrestore) | 释放自旋锁并恢复中断状态 |
| [osal_spin_lock_destroy](#osal_spin_lock_destroy) | 销毁自旋锁 |

## Functions

### osal_spin_lock_init <a id="osal_spin_lock_init"></a>

```c
int osal_spin_lock_init(osal_spinlock *lock)
```

**声明头文件**

```c
#include "lock/osal_spinlock.h"
```

**功能说明**

- 初始化自旋锁，使其可用于后续的加锁解锁操作。
- 若锁已初始化（lock->lock 非 NULL）则返回失败。
- 支持 linux 和 liteos 系统。

**前置条件**

- 调用时序约束：lock 必须未被初始化（lock->lock 为 NULL）。
- 依赖关系：初始化后的自旋锁必须通过 osal_spin_lock_destroy 释放，否则会导致内存泄漏。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| lock | [osal_spinlock](#struct_osal_spinlock) * | 待初始化的自旋锁结构体指针 | 非 NULL; lock->lock 为 NULL |

**返回值**

返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 执行成功 | 初始化成功 |
| -1 | 执行失败 | 参数无效或内存分配失败 |

**参考案例**

- `src/middleware/utils/hcc/comm/hcc.c`
- `src/middleware/utils/hcc/comm/hcc_dfx.c`

### osal_spin_lock <a id="osal_spin_lock"></a>

```c
void osal_spin_lock(osal_spinlock *lock)
```

**声明头文件**

```c
#include "lock/osal_spinlock.h"
```

**功能说明**

- 获取指定的自旋锁。
- 若锁已被其他线程持有，当前线程将循环等待直至成功获取锁。
- 支持 linux 和 liteos 系统。

**前置条件**

- 调用时序约束：lock 必须已通过 osal_spin_lock_init 初始化。
- 上下文限制：同一任务内不可重复加锁，否则会死锁；任务与中断共用时需使用 osal_spin_lock_irqsave。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| lock | [osal_spinlock](#struct_osal_spinlock) * | 待获取的自旋锁结构体指针，须由 osal_spin_lock_init 初始化 | 非 NULL; lock->lock 非 NULL |

**参考案例**

- `src/protocol/wifi/source/host/feature/hmac_11k.c`
- `src/protocol/wifi/source/host/feature/interface/hmac_ccpriv.c`

### osal_spin_lock_bh <a id="osal_spin_lock_bh"></a>

```c
void osal_spin_lock_bh(osal_spinlock *lock)
```

**声明头文件**

```c
#include "lock/osal_spinlock.h"
```

**功能说明**

- 获取指定的自旋锁并禁用软中断。
- 在 liteos 和 freertos 系统上禁用调度。
- 支持 linux、liteos 和 freertos 系统。

**前置条件**

- 调用时序约束：lock 必须已通过 osal_spin_lock_init 初始化。
- 上下文限制：加锁后需使用 osal_spin_unlock_bh 解锁，不可与其他解锁接口混用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| lock | [osal_spinlock](#struct_osal_spinlock) * | 待获取的自旋锁结构体指针，须由 osal_spin_lock_init 初始化 | 非 NULL; lock->lock 非 NULL |

**参考案例**

- `src/protocol/wifi/source/host/feature/hmac_tx_amsdu.c`

### osal_spin_trylock <a id="osal_spin_trylock"></a>

```c
int osal_spin_trylock(osal_spinlock *lock)
```

**声明头文件**

```c
#include "lock/osal_spinlock.h"
```

**功能说明**

- 尝试获取指定的自旋锁。
- 若锁可立即获取则返回成功，否则立即返回失败。
- 支持 linux 和 liteos 系统。

**前置条件**

- 调用时序约束：lock 必须已通过 osal_spin_lock_init 初始化。
- 上下文限制：获取失败时立即返回，不会阻塞等待。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| lock | [osal_spinlock](#struct_osal_spinlock) * | 待获取的自旋锁结构体指针 | 非 NULL; lock->lock 非 NULL |

**返回值**

返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| true（非 0） | 获取锁成功 | 锁可立即获取 |
| false (0) | 获取锁失败 | 锁已被占用或参数无效 |

### osal_spin_trylock_irq <a id="osal_spin_trylock_irq"></a>

```c
int osal_spin_trylock_irq(osal_spinlock *lock)
```

**声明头文件**

```c
#include "lock/osal_spinlock.h"
```

**功能说明**

- 尝试获取指定的自旋锁并禁用 CPU 中断。
- 若锁可立即获取则返回成功，否则立即返回失败。
- 仅支持 linux 系统。

**前置条件**

- 调用时序约束：lock 必须已通过 osal_spin_lock_init 初始化。
- 上下文限制：仅在 linux 系统支持。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| lock | [osal_spinlock](#struct_osal_spinlock) * | 待获取的自旋锁结构体指针 | 非 NULL; lock->lock 非 NULL |

**返回值**

返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| true（非 0） | 获取锁成功 | 锁可立即获取 |
| false (0) | 获取锁失败 | 锁已被占用 |
| -1 | 参数无效 | lock 为空或未初始化 |

### osal_spin_trylock_irqsave <a id="osal_spin_trylock_irqsave"></a>

```c
void osal_spin_trylock_irqsave(osal_spinlock *lock, unsigned long *flags)
```

**声明头文件**

```c
#include "lock/osal_spinlock.h"
```

**功能说明**

- 保存当前 CPU 中断状态，尝试获取指定的自旋锁，并禁用 CPU 中断。
- 中断状态保存到 flags 参数中，用于后续恢复。
- 仅支持 linux 系统。

**前置条件**

- 调用时序约束：lock 必须已通过 osal_spin_lock_init 初始化。
- 上下文限制：仅在 linux 系统支持；获取锁后需使用 osal_spin_unlock_irqrestore 恢复中断状态。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| lock | [osal_spinlock](#struct_osal_spinlock) * | 待获取的自旋锁结构体指针 | 非 NULL; lock->lock 非 NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| flags | unsigned long * | 保存的 CPU 中断状态值，用于 osal_spin_unlock_irqrestore 恢复中断 |

### osal_spin_unlock <a id="osal_spin_unlock"></a>

```c
void osal_spin_unlock(osal_spinlock *lock)
```

**声明头文件**

```c
#include "lock/osal_spinlock.h"
```

**功能说明**

- 释放指定的自旋锁。
- 释放后允许其他等待该锁的线程获取锁。
- 支持 linux 和 liteos 系统。

**前置条件**

- 调用时序约束：lock 必须已通过 osal_spin_lock 加锁。
- 上下文限制：解锁的锁必须由 osal_spin_lock 加锁，不可与其他加锁接口混用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| lock | [osal_spinlock](#struct_osal_spinlock) * | 待释放的自旋锁结构体指针 | 非 NULL; lock->lock 非 NULL |

**参考案例**

- `src/protocol/wifi/source/host/feature/hmac_11k.c`
- `src/protocol/wifi/source/host/feature/interface/hmac_ccpriv.c`

### osal_spin_unlock_bh <a id="osal_spin_unlock_bh"></a>

```c
void osal_spin_unlock_bh(osal_spinlock *lock)
```

**声明头文件**

```c
#include "lock/osal_spinlock.h"
```

**功能说明**

- 释放指定的自旋锁并恢复软中断。
- 在 liteos 和 freertos 系统上恢复调度。
- 支持 linux、liteos 和 freertos 系统。

**前置条件**

- 调用时序约束：lock 必须已通过 osal_spin_lock_bh 加锁。
- 上下文限制：解锁的锁必须由 osal_spin_lock_bh 加锁，不可与其他加锁接口混用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| lock | [osal_spinlock](#struct_osal_spinlock) * | 待释放的自旋锁结构体指针 | 非 NULL; lock->lock 非 NULL |

**参考案例**

- `src/protocol/wifi/source/host/feature/hmac_tx_amsdu.c`

### osal_spin_lock_irqsave <a id="osal_spin_lock_irqsave"></a>

```c
void osal_spin_lock_irqsave(osal_spinlock *lock, unsigned long *flags)
```

**声明头文件**

```c
#include "lock/osal_spinlock.h"
```

**功能说明**

- 保存当前 CPU 中断状态，获取指定的自旋锁，并禁用 CPU 中断。
- 中断状态保存到 flags 参数中，用于后续恢复。
- 支持 linux、liteos 和 freertos 系统。

**前置条件**

- 调用时序约束：lock 必须已通过 osal_spin_lock_init 初始化。
- 上下文限制：获取锁后需使用 osal_spin_unlock_irqrestore 释放锁并恢复中断状态。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| lock | [osal_spinlock](#struct_osal_spinlock) * | 待获取的自旋锁结构体指针 | 非 NULL; lock->lock 非 NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| flags | unsigned long * | 保存的 CPU 中断状态值，用于 osal_spin_unlock_irqrestore 恢复中断 |

**参考案例**

- `src/drivers/chips/ws53/rom/app/middleware/utils/hcc/acore/master/hcc_ipc_host.c`
- `src/drivers/chips/ws53/rom/app/middleware/utils/hcc/romable/comm/hcc_flow_ctrl.c`

### osal_spin_unlock_irqrestore <a id="osal_spin_unlock_irqrestore"></a>

```c
void osal_spin_unlock_irqrestore(osal_spinlock *lock, unsigned long *flags)
```

**声明头文件**

```c
#include "lock/osal_spinlock.h"
```

**功能说明**

- 释放指定的自旋锁并恢复 CPU 中断状态。
- 使用加锁时保存的 flags 值恢复中断。
- 支持 linux、liteos 和 freertos 系统。

**前置条件**

- 调用时序约束：lock 必须已通过 osal_spin_lock_irqsave 或 osal_spin_trylock_irqsave 加锁。
- 上下文限制：flags 必须为加锁时保存的中断状态值。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| lock | [osal_spinlock](#struct_osal_spinlock) * | 待释放的自旋锁结构体指针 | 非 NULL; lock->lock 非 NULL |
| flags | unsigned long * | 加锁时保存的中断状态值 | 非 NULL |

**参考案例**

- `src/drivers/chips/ws53/rom/app/middleware/utils/hcc/acore/master/hcc_ipc_host.c`

### osal_spin_lock_destroy <a id="osal_spin_lock_destroy"></a>

```c
void osal_spin_lock_destroy(osal_spinlock *lock)
```

**声明头文件**

```c
#include "lock/osal_spinlock.h"
```

**功能说明**

- 销毁自旋锁，释放底层锁资源。
- 销毁后锁不可再使用。
- 支持 linux 和 liteos 系统。

**前置条件**

- 调用时序约束：lock 必须由 osal_spin_lock_init 初始化返回。
- 依赖关系：模块退出时必须调用此接口释放锁，否则会导致内存泄漏。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| lock | [osal_spinlock](#struct_osal_spinlock) * | 待销毁的自旋锁结构体指针 | 非 NULL; lock->lock 非 NULL |

**参考案例**

- `src/drivers/chips/ws53/rom/app/middleware/utils/hcc/acore/master/comm/hcc.c`
- `src/drivers/chips/ws53/rom/app/middleware/utils/hcc/acore/master/hcc_ipc_host.c`

## Structures

### osal_spinlock <a id="struct_osal_spinlock"></a>

```c
typedef struct {
    void *lock;
} osal_spinlock;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| lock | void * | 自旋锁内部实现指针，由 osal_spin_lock_init 初始化，指向底层锁资源 |
