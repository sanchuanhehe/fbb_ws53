# RWLock

osal_rwlock 提供 OSAL (Operating System Abstraction Layer) 读写锁功能，用于多读单写场景下共享资源的并发访问保护，支持读端并发持有与写端独占访问。

**头文件清单**

```c
#include "include/lock/osal_rwlock.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_rwlock_init](#osal_rwlock_init) | 初始化读写锁对象，分配底层资源 |
| [osal_rwlock_read_lock](#osal_rwlock_read_lock) | 获取读模式锁 |
| [osal_rwlock_read_unlock](#osal_rwlock_read_unlock) | 释放读模式锁 |
| [osal_rwlock_write_lock](#osal_rwlock_write_lock) | 获取写模式锁 |
| [osal_rwlock_write_unlock](#osal_rwlock_write_unlock) | 释放写模式锁 |
| [osal_rwlock_destory](#osal_rwlock_destory) | 销毁读写锁对象，释放底层资源 |

## Functions

### osal_rwlock_init <a id="osal_rwlock_init"></a>

```c
int osal_rwlock_init(osal_rwlock *rw_lock)
```

**头文件清单**

```c
#include "include/lock/osal_rwlock.h"
```

**功能说明**

- 初始化读写锁对象
- 为读写锁分配底层资源
- 返回初始化成功或失败的结果

**前置条件**

- 调用时序约束：当前接口为读写锁生命周期首个调用，后续读/写锁操作须在本接口成功返回后进行
- 依赖关系：当前接口运行于 Linux 系统环境

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| rw_lock | [osal_rwlock](#osal_rwlock) * | 读写锁对象指针 | rw_lock 不为 NULL，且 rw_lock->rwlock 为 NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| OSAL_SUCCESS:0 | 初始化成功 | 参数合法且底层读写锁资源分配与初始化成功 |
| OSAL_FAILURE:-1 | 初始化失败 | rw_lock 为 NULL、rwlock 已初始化或底层资源分配失败 |

### osal_rwlock_read_lock <a id="osal_rwlock_read_lock"></a>

```c
void osal_rwlock_read_lock(osal_rwlock *rw_lock)
```

**头文件清单**

```c
#include "include/lock/osal_rwlock.h"
```

**功能说明**

- 获取读模式锁
- 允许多个读端同时持有读锁
- 持有读锁期间阻塞写端获取写锁

**前置条件**

- 调用时序约束：当前接口必须在 osal_rwlock_init 成功返回后调用
- 依赖关系：当前接口运行于 Linux 系统环境

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| rw_lock | [osal_rwlock](#osal_rwlock) * | 读写锁对象指针 | rw_lock 不为 NULL，且 rw_lock->rwlock 不为 NULL |

### osal_rwlock_read_unlock <a id="osal_rwlock_read_unlock"></a>

```c
void osal_rwlock_read_unlock(osal_rwlock *rw_lock)
```

**头文件清单**

```c
#include "include/lock/osal_rwlock.h"
```

**功能说明**

- 释放读模式锁
- 与 osal_rwlock_read_lock 配对使用
- 释放后允许写端竞争写锁

**前置条件**

- 调用时序约束：当前接口必须在 osal_rwlock_read_lock 成功获取读锁后调用
- 依赖关系：当前接口运行于 Linux 系统环境

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| rw_lock | [osal_rwlock](#osal_rwlock) * | 读写锁对象指针 | rw_lock 不为 NULL，且 rw_lock->rwlock 不为 NULL |

### osal_rwlock_write_lock <a id="osal_rwlock_write_lock"></a>

```c
void osal_rwlock_write_lock(osal_rwlock *rw_lock)
```

**头文件清单**

```c
#include "include/lock/osal_rwlock.h"
```

**功能说明**

- 获取写模式锁
- 独占访问受保护的共享资源
- 持有写锁期间阻塞其他读端与写端

**前置条件**

- 调用时序约束：当前接口必须在 osal_rwlock_init 成功返回后调用
- 依赖关系：当前接口运行于 Linux 系统环境

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| rw_lock | [osal_rwlock](#osal_rwlock) * | 读写锁对象指针 | rw_lock 不为 NULL，且 rw_lock->rwlock 不为 NULL |

### osal_rwlock_write_unlock <a id="osal_rwlock_write_unlock"></a>

```c
void osal_rwlock_write_unlock(osal_rwlock *rw_lock)
```

**头文件清单**

```c
#include "include/lock/osal_rwlock.h"
```

**功能说明**

- 释放写模式锁
- 与 osal_rwlock_write_lock 配对使用
- 释放后允许其他读端与写端竞争

**前置条件**

- 调用时序约束：当前接口必须在 osal_rwlock_write_lock 成功获取写锁后调用
- 依赖关系：当前接口运行于 Linux 系统环境

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| rw_lock | [osal_rwlock](#osal_rwlock) * | 读写锁对象指针 | rw_lock 不为 NULL，且 rw_lock->rwlock 不为 NULL |

### osal_rwlock_destory <a id="osal_rwlock_destory"></a>

```c
void osal_rwlock_destory(osal_rwlock *rw_lock)
```

**头文件清单**

```c
#include "include/lock/osal_rwlock.h"
```

**功能说明**

- 释放读写锁占用的底层资源
- 将读写锁对象恢复到未初始化状态
- 释放后读写锁对象不可再用于读/写锁操作

**前置条件**

- 调用时序约束：当前接口必须在 osal_rwlock_init 成功返回后调用，且为读写锁生命周期末尾调用
- 依赖关系：当前接口运行于 Linux 系统环境

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| rw_lock | [osal_rwlock](#osal_rwlock) * | 读写锁对象指针 | rw_lock 不为 NULL，且 rw_lock->rwlock 不为 NULL |

## Structures

### osal_rwlock <a id="osal_rwlock"></a>

```c
typedef struct {
    void *rwlock;
} osal_rwlock;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| rwlock | void * | 底层读写锁句柄，由 osal_rwlock_init 初始化填充，osal_rwlock_destory 释放后置 NULL |
