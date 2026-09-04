# Atomic

Atomic 提供 OSAL（OS Abstract Layer）原子操作接口，对 osal_atomic 原子变量执行读取、设置、自增、自减、加法、减法及结果测试等不可分割的整数运算，支持 linux、liteos、freertos 等多种操作系统后端。

**模块公共头文件**

```c
#include "atomic/osal_atomic.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_atomic_read](#osal_atomic_read) | 原子读取原子变量的当前值 |
| [osal_atomic_set](#osal_atomic_set) | 原子设置原子变量为指定值 |
| [osal_atomic_inc_return](#osal_atomic_inc_return) | 原子自增 1 并返回结果 |
| [osal_atomic_add_return](#osal_atomic_add_return) | 原子增加指定值并返回结果 |
| [osal_atomic_dec_return](#osal_atomic_dec_return) | 原子自减 1 并返回结果 |
| [osal_atomic_inc](#osal_atomic_inc) | 原子自增 1 |
| [osal_atomic_sub](#osal_atomic_sub) | 原子减少指定值 |
| [osal_atomic_dec](#osal_atomic_dec) | 原子自减 1 |
| [osal_atomic_add](#osal_atomic_add) | 原子增加指定值 |
| [osal_atomic_dec_and_test](#osal_atomic_dec_and_test) | 原子自减 1 并测试结果是否为 0 |
| [osal_atomic_inc_and_test](#osal_atomic_inc_and_test) | 原子自增 1 并测试结果是否为 0 |
| [osal_atomic_inc_not_zero](#osal_atomic_inc_not_zero) | 原子变量非 0 时自增 1 |

## Functions

### osal_atomic_read <a id="osal_atomic_read"></a>

```c
int osal_atomic_read(osal_atomic *atomic)
```

**声明头文件**

```c
#include "atomic/osal_atomic.h"
```

**功能说明**

- 原子地读取原子变量的当前值。
- 读取操作以原子方式执行，过程中不可被分割。
- 返回从原子变量读取到的整数值。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| atomic | [osal_atomic *](#osal_atomic) | 指向待读取的原子变量 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| -1 | 参数无效 | atomic 为 NULL |
| 其他 | 原子变量的当前值 | atomic 非空，读取成功 |

**参考案例**

- `src/middleware/utils/hcc/comm/hcc.c`

### osal_atomic_set <a id="osal_atomic_set"></a>

```c
void osal_atomic_set(osal_atomic *atomic, int i)
```

**声明头文件**

```c
#include "atomic/osal_atomic.h"
```

**功能说明**

- 将原子变量原子地设置为指定整数值。
- 设置操作以原子方式执行，过程中不可被分割。
- 操作直接作用于入参 atomic 指向的原子变量。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| atomic | [osal_atomic *](#osal_atomic) | 指向待设置的原子变量 | 不为NULL |
| i | int | 待设置的整数值 | int 类型取值范围 |

**参考案例**

- `src/middleware/utils/hcc/comm/hcc.c`

### osal_atomic_inc_return <a id="osal_atomic_inc_return"></a>

```c
int osal_atomic_inc_return(osal_atomic *atomic)
```

**声明头文件**

```c
#include "atomic/osal_atomic.h"
```

**功能说明**

- 对原子变量执行自增 1 操作。
- 自增操作以原子方式执行，过程中不可被分割。
- 返回自增后的结果值。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| atomic | [osal_atomic *](#osal_atomic) | 指向待自增的原子变量 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| -1 | 参数无效 | atomic 为 NULL |
| 其他 | 自增后的结果值 | atomic 非空，自增成功 |

### osal_atomic_add_return <a id="osal_atomic_add_return"></a>

```c
int osal_atomic_add_return(osal_atomic *atomic, int count)
```

**声明头文件**

```c
#include "atomic/osal_atomic.h"
```

**功能说明**

- 对原子变量增加指定的整数值。
- 加法操作以原子方式执行，过程中不可被分割。
- 返回增加后的结果值。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| atomic | [osal_atomic *](#osal_atomic) | 指向待操作的原子变量 | 不为NULL |
| count | int | 增加的数量值 | int 类型取值范围 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 整数值 | 增加后的结果值 | 加法操作完成 |

### osal_atomic_dec_return <a id="osal_atomic_dec_return"></a>

```c
int osal_atomic_dec_return(osal_atomic *atomic)
```

**声明头文件**

```c
#include "atomic/osal_atomic.h"
```

**功能说明**

- 对原子变量执行自减 1 操作。
- 自减操作以原子方式执行，过程中不可被分割。
- 返回自减后的结果值。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| atomic | [osal_atomic *](#osal_atomic) | 指向待自减的原子变量 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| -1 | 参数无效 | atomic 为 NULL |
| 其他 | 自减后的结果值 | atomic 非空，自减成功 |

### osal_atomic_inc <a id="osal_atomic_inc"></a>

```c
void osal_atomic_inc(osal_atomic *atomic)
```

**声明头文件**

```c
#include "atomic/osal_atomic.h"
```

**功能说明**

- 对原子变量执行自增 1 操作。
- 自增操作以原子方式执行，过程中不可被分割。
- 操作直接作用于入参 atomic 指向的原子变量。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| atomic | [osal_atomic *](#osal_atomic) | 指向待自增的原子变量 | 不为NULL |

**参考案例**

- `src/middleware/utils/hcc/comm/hcc_bus.c`

### osal_atomic_sub <a id="osal_atomic_sub"></a>

```c
void osal_atomic_sub(osal_atomic *atomic, unsigned int count)
```

**声明头文件**

```c
#include "atomic/osal_atomic.h"
```

**功能说明**

- 对原子变量减少指定的整数值。
- 减法操作以原子方式执行，过程中不可被分割。
- 操作直接作用于入参 atomic 指向的原子变量。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| atomic | [osal_atomic *](#osal_atomic) | 指向待操作的原子变量 | 不为NULL |
| count | unsigned int | 减少的数量值 | unsigned int 类型取值范围 |

### osal_atomic_dec <a id="osal_atomic_dec"></a>

```c
void osal_atomic_dec(osal_atomic *atomic)
```

**声明头文件**

```c
#include "atomic/osal_atomic.h"
```

**功能说明**

- 对原子变量执行自减 1 操作。
- 自减操作以原子方式执行，过程中不可被分割。
- 操作直接作用于入参 atomic 指向的原子变量。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| atomic | [osal_atomic *](#osal_atomic) | 指向待自减的原子变量 | 不为NULL |

### osal_atomic_add <a id="osal_atomic_add"></a>

```c
void osal_atomic_add(osal_atomic *atomic, int count)
```

**声明头文件**

```c
#include "atomic/osal_atomic.h"
```

**功能说明**

- 对原子变量增加指定的整数值。
- 加法操作以原子方式执行，过程中不可被分割。
- 操作直接作用于入参 atomic 指向的原子变量。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| atomic | [osal_atomic *](#osal_atomic) | 指向待操作的原子变量 | 不为NULL |
| count | int | 增加的数量值 | int 类型取值范围 |

### osal_atomic_dec_and_test <a id="osal_atomic_dec_and_test"></a>

```c
int osal_atomic_dec_and_test(osal_atomic *atomic)
```

**声明头文件**

```c
#include "atomic/osal_atomic.h"
```

**功能说明**

- 对原子变量执行自减 1 操作。
- 自减操作以原子方式执行，过程中不可被分割。
- 自减后判断结果是否为 0，为 0 返回 true，否则返回 false。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| atomic | [osal_atomic *](#osal_atomic) | 指向待自减并测试的原子变量 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 1 | true | 自减后结果为 0 |
| 0 | false | 自减后结果不为 0 |
| -1 | 参数无效 | atomic 为 NULL |

### osal_atomic_inc_and_test <a id="osal_atomic_inc_and_test"></a>

```c
int osal_atomic_inc_and_test(osal_atomic *atomic)
```

**声明头文件**

```c
#include "atomic/osal_atomic.h"
```

**功能说明**

- 对原子变量执行自增 1 操作。
- 自增操作以原子方式执行，过程中不可被分割。
- 自增后判断结果是否为 0，为 0 返回 true，否则返回 false。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| atomic | [osal_atomic *](#osal_atomic) | 指向待自增并测试的原子变量 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 1 | true | 自增后结果为 0 |
| 0 | false | 自增后结果不为 0 |
| -1 | 参数无效 | atomic 为 NULL |

### osal_atomic_inc_not_zero <a id="osal_atomic_inc_not_zero"></a>

```c
int osal_atomic_inc_not_zero(osal_atomic *atomic)
```

**声明头文件**

```c
#include "atomic/osal_atomic.h"
```

**功能说明**

- 当原子变量当前值非 0 时，对其执行自增 1 操作。
- 自增操作以原子方式执行，过程中不可被分割。
- 若执行了自增则返回 true，若原子变量为 0 未自增则返回 false。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| atomic | [osal_atomic *](#osal_atomic) | 指向待条件自增的原子变量 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 1 | true | 原子变量非 0，已执行自增 |
| 0 | false | 原子变量为 0，未执行自增 |
| -1 | 参数无效 | atomic 为 NULL |

## Structures

### osal_atomic <a id="osal_atomic"></a>

```c
typedef struct {
    volatile int counter;
} osal_atomic;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| counter | volatile int | 原子变量存储的整数值 |
