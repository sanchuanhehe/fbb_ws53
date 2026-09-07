# Mutex

Mutex 提供互斥锁功能，用于保护临界区资源，确保同一时刻仅有一个任务访问共享资源，支持永久等待、限时等待、可中断等待与不等待等多种加锁方式。该模块封装底层操作系统互斥锁服务，向上提供统一的初始化、加锁、解锁、查询与销毁接口。

**模块公共头文件**

```c
#include "lock/osal_mutex.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_mutex_init](#osal_mutex_init) | 初始化指定的互斥锁，使其进入可用状态 |
| [osal_mutex_lock](#osal_mutex_lock) | 获取互斥锁，独占锁定，不可用则阻塞等待 |
| [osal_mutex_lock_timeout](#osal_mutex_lock_timeout) | 在指定超时时间内尝试获取互斥锁 |
| [osal_mutex_lock_interruptible](#osal_mutex_lock_interruptible) | 获取互斥锁，等待期间可被信号中断 |
| [osal_mutex_trylock](#osal_mutex_trylock) | 尝试获取互斥锁，不等待 |
| [osal_mutex_unlock](#osal_mutex_unlock) | 释放当前任务持有的互斥锁 |
| [osal_mutex_is_locked](#osal_mutex_is_locked) | 查询指定互斥锁当前的锁定状态 |
| [osal_mutex_destroy](#osal_mutex_destroy) | 销毁指定的互斥锁，释放其占用资源 |

## Functions

### osal_mutex_init <a id="osal_mutex_init"></a>

```c
int osal_mutex_init(osal_mutex *mutex)
```

**声明头文件**

```c
#include "lock/osal_mutex.h"
```

**功能说明**

- 初始化指定的互斥锁，使其进入可用状态。
- 初始化后的互斥锁可用于保护临界区资源的互斥访问。
- 是使用互斥锁生命周期中的第一个步骤。

**前置条件**

- 调用时序约束：当前接口为互斥锁使用的起始步骤，使用互斥锁前必须先调用本接口完成初始化。
- 依赖关系：当前接口依赖底层操作系统互斥锁服务与内存分配能力可用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| mutex | [osal_mutex](#osal_mutex) * | 待初始化的互斥锁指针 | 不为 NULL，且未被初始化过 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS：0 | 初始化成功 | 互斥锁初始化成功 |
| OSAL_FAILURE：-1 | 初始化失败 | mutex 为 NULL、已初始化或内存分配失败 |

**参考案例**

- `src/middleware/utils/dfx/log_file/log_file.c`
- `src/open_source/lwip/lwip_adapter/liteos_207/src/arch/sys_arch.c`
- `src/protocol/wifi/source/host/hmac/hmac_dfx.c`

### osal_mutex_lock <a id="osal_mutex_lock"></a>

```c
int osal_mutex_lock(osal_mutex *mutex)
```

**声明头文件**

```c
#include "lock/osal_mutex.h"
```

**功能说明**

- 获取指定的互斥锁，对互斥锁进行独占锁定。
- 若互斥锁不可用则阻塞等待，直到获取成功。
- 用于保护临界区，确保同一时刻仅一个任务访问共享资源。

**前置条件**

- 调用时序约束：当前接口必须在 [osal_mutex_init](#osal_mutex_init)() 成功返回后调用。
- 上下文限制：当前接口可能阻塞睡眠，禁止在中断上下文调用；获取的互斥锁必须由同一任务释放，禁止递归加锁。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| mutex | [osal_mutex](#osal_mutex) * | 待获取的互斥锁指针 | 不为 NULL，且已通过 osal_mutex_init() 初始化 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS：0 | 获取互斥锁成功 | 成功锁定互斥锁 |
| OSAL_FAILURE：-1 | 获取互斥锁失败 | mutex 为 NULL 或内部句柄为空 |

**参考案例**

- `src/protocol/wifi/source/host/hmac/hmac_sta_pm.c`
- `src/open_source/lwip/lwip_adapter/liteos_207/src/arch/sys_arch.c`
- `src/protocol/wifi/source/host/hmac/hmac_dfx.c`

### osal_mutex_lock_timeout <a id="osal_mutex_lock_timeout"></a>

```c
int osal_mutex_lock_timeout(osal_mutex *mutex, unsigned int timeout)
```

**声明头文件**

```c
#include "lock/osal_mutex.h"
```

**功能说明**

- 在指定超时时间内尝试获取互斥锁。
- 若互斥锁在超时时间内可用则获取成功，否则超时返回失败。
- 支持永久等待与限时等待两种模式。

**前置条件**

- 调用时序约束：当前接口必须在 [osal_mutex_init](#osal_mutex_init)() 成功返回后调用。
- 上下文限制：当前接口可能阻塞睡眠，禁止在中断上下文调用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| mutex | [osal_mutex](#osal_mutex) * | 待获取的互斥锁指针 | 不为 NULL，且已通过 osal_mutex_init() 初始化 |
| timeout | unsigned int | 超时等待时间（毫秒） | [OSAL_MUTEX_WAIT_FOREVER](#OSAL_MUTEX_WAIT_FOREVER)(-1) 表示永久等待；<br>其他数值为超时毫秒数。 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS：0 | 获取互斥锁成功 | 在超时时间内成功锁定互斥锁 |
| OSAL_FAILURE：-1 | 获取互斥锁失败 | mutex 为 NULL 或超时未获取到互斥锁 |

**参考案例**

- `src/middleware/utils/at/at_wifi_cmd/at/at_register.c`
- `src/middleware/services/wifi_service/wpa/osdep/osdep_osal.c`

### osal_mutex_lock_interruptible <a id="osal_mutex_lock_interruptible"></a>

```c
int osal_mutex_lock_interruptible(osal_mutex *mutex)
```

**声明头文件**

```c
#include "lock/osal_mutex.h"
```

**功能说明**

- 获取互斥锁，等待期间可被信号中断。
- 若等待过程中收到信号则返回，不获取互斥锁。
- 适用于可能被信号打断的加锁场景。

**前置条件**

- 调用时序约束：当前接口必须在 [osal_mutex_init](#osal_mutex_init)() 成功返回后调用。
- 上下文限制：当前接口可能阻塞睡眠，等待期间可被信号中断。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| mutex | [osal_mutex](#osal_mutex) * | 待获取的互斥锁指针 | 不为 NULL，且已通过 osal_mutex_init() 初始化 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS：0 | 获取互斥锁成功 | 成功锁定互斥锁 |
| OSAL_FAILURE：-1 | 获取互斥锁失败 | mutex 为 NULL 或内部句柄为空 |
| OSAL_EINTR：-4 | 被信号中断 | 等待过程中被信号中断，未获取互斥锁 |

### osal_mutex_trylock <a id="osal_mutex_trylock"></a>

```c
int osal_mutex_trylock(osal_mutex *mutex)
```

**声明头文件**

```c
#include "lock/osal_mutex.h"
```

**功能说明**

- 尝试获取互斥锁，不等待。
- 若互斥锁立即可用则获取成功，否则立即返回失败。
- 适用于不希望阻塞的加锁场景。

**前置条件**

- 调用时序约束：当前接口必须在 [osal_mutex_init](#osal_mutex_init)() 成功返回后调用。
- 上下文限制：当前接口不等待，不会阻塞睡眠。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| mutex | [osal_mutex](#osal_mutex) * | 待获取的互斥锁指针 | 不为 NULL，且已通过 osal_mutex_init() 初始化 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| TRUE：1 | 获取互斥锁成功 | 成功获取互斥锁 |
| FALSE：0 | 获取互斥锁失败 | 互斥锁被占用或参数无效 |

### osal_mutex_unlock <a id="osal_mutex_unlock"></a>

```c
void osal_mutex_unlock(osal_mutex *mutex)
```

**声明头文件**

```c
#include "lock/osal_mutex.h"
```

**功能说明**

- 释放当前任务持有的互斥锁。
- 解除对互斥锁的独占锁定。
- 用于离开临界区后释放互斥锁。

**前置条件**

- 调用时序约束：当前接口必须在 osal_mutex_lock() 等加锁接口成功获取互斥锁后调用，且由加锁的同一任务释放。
- 上下文限制：当前接口禁止在中断上下文调用，禁止解锁未被锁定的互斥锁。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| mutex | [osal_mutex](#osal_mutex) * | 待释放的互斥锁指针 | 不为 NULL，且已通过 osal_mutex_init() 初始化 |

**参考案例**

- `src/protocol/wifi/source/host/hmac/hmac_sta_pm.c`
- `src/open_source/lwip/lwip_adapter/liteos_207/src/arch/sys_arch.c`
- `src/protocol/wifi/source/host/hmac/hmac_dfx.c`

### osal_mutex_is_locked <a id="osal_mutex_is_locked"></a>

```c
int osal_mutex_is_locked(osal_mutex *mutex)
```

**声明头文件**

```c
#include "lock/osal_mutex.h"
```

**功能说明**

- 查询指定互斥锁当前的锁定状态。
- 返回互斥锁是否处于锁定状态。
- 用于在不改变互斥锁状态的前提下获取其锁定信息。

**前置条件**

- 调用时序约束：当前接口必须在 [osal_mutex_init](#osal_mutex_init)() 成功返回后调用。
- 依赖关系：当前接口依赖底层操作系统提供互斥锁状态查询能力。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| mutex | [osal_mutex](#osal_mutex) * | 待查询的互斥锁指针 | 不为 NULL，且已通过 osal_mutex_init() 初始化 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 1 | 互斥锁已锁定 | 互斥锁处于锁定状态 |
| 0 | 互斥锁未锁定 | 互斥锁处于未锁定状态 |
| OSAL_FAILURE：-1 | 查询失败 | mutex 为 NULL 或内部句柄为空 |

### osal_mutex_destroy <a id="osal_mutex_destroy"></a>

```c
void osal_mutex_destroy(osal_mutex *mutex)
```

**声明头文件**

```c
#include "lock/osal_mutex.h"
```

**功能说明**

- 销毁指定的互斥锁，释放其占用的资源。
- 互斥锁销毁后不可再用于加锁/解锁操作。
- 是使用互斥锁生命周期中的最后一个步骤。

**前置条件**

- 调用时序约束：当前接口必须在互斥锁不再被使用（已解锁）时调用，模块退出时须调用以避免内存泄漏。
- 依赖关系：当前接口调用后互斥锁指针应由调用方置空。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| mutex | [osal_mutex](#osal_mutex) * | 待销毁的互斥锁指针 | 不为 NULL，且已通过 osal_mutex_init() 初始化 |

**参考案例**

- `src/middleware/utils/dfx/log_file/log_file.c`
- `src/protocol/wifi/source/host/hmac/hmac_dfx.c`

## Structures

### osal_mutex <a id="osal_mutex"></a>

```c
typedef struct {
    void *mutex;
} osal_mutex;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| mutex | void * | 互斥锁内部句柄指针 |

## Macros

### OSAL_MUTEX_WAIT_FOREVER <a id="OSAL_MUTEX_WAIT_FOREVER"></a>

```c
#define OSAL_MUTEX_WAIT_FOREVER (-1)
```
