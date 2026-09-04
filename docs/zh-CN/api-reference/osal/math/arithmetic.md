# Arithmetic

Arithmetic 提供 OSAL（Operating System Abstraction Layer）数学运算功能，包括 64 位整数除法与取余运算、随机数生成，以及最大值、最小值、绝对值等常用数学计算宏。

**模块公共头文件**

```c
#include "src/kernel/osal/include/math/osal_math.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_div_u64](#osal_div_u64) | 无符号 64 位整数除以无符号 32 位整数，返回商 |
| [osal_div_s64](#osal_div_s64) | 有符号 64 位整数除以有符号 32 位整数，返回商 |
| [osal_div64_u64](#osal_div64_u64) | 无符号 64 位整数除以无符号 64 位整数，返回商 |
| [osal_div64_s64](#osal_div64_s64) | 有符号 64 位整数除以有符号 64 位整数，返回商 |
| [osal_div_u64_rem](#osal_div_u64_rem) | 无符号 64 位整数除以无符号 32 位整数，返回余数 |
| [osal_div_s64_rem](#osal_div_s64_rem) | 有符号 64 位整数除以有符号 32 位整数，返回余数 |
| [osal_div64_u64_rem](#osal_div64_u64_rem) | 无符号 64 位整数除以无符号 64 位整数，返回余数 |
| [osal_get_random_int](#osal_get_random_int) | 生成无符号 32 位随机数 |

## Functions

### osal_div_u64 <a id="osal_div_u64"></a>

```c
unsigned long long osal_div_u64(unsigned long long dividend, unsigned int divisor)
```

**声明头文件**

```c
#include "src/kernel/osal/include/math/osal_math.h"
```

**功能说明**

- 实现无符号 64 位整数除以无符号 32 位整数的除法运算。
- 返回除法运算的商。
- 适用于需要高精度无符号整数除法的场景。

**前置条件**

- 上下文限制：当前接口支持 linux 和 liteos 系统下使用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| dividend | unsigned long long | 无符号 64 位被除数 | 0 ~ 2^64-1 |
| divisor | unsigned int | 无符号 32 位除数 | 不为0 |

**返回值**

- 返回类型：unsigned long long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 ~ 2^64-1 | dividend / divisor 的无符号商值 | 除数不为零时返回商 |

### osal_div_s64 <a id="osal_div_s64"></a>

```c
long long osal_div_s64(long long dividend, int divisor)
```

**声明头文件**

```c
#include "src/kernel/osal/include/math/osal_math.h"
```

**功能说明**

- 实现有符号 64 位整数除以有符号 32 位整数的除法运算。
- 返回除法运算的商。
- 适用于需要高精度有符号整数除法的场景。

**前置条件**

- 上下文限制：当前接口支持 linux 和 liteos 系统下使用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| dividend | long long | 有符号 64 位被除数 | -2^63 ~ 2^63-1 |
| divisor | int | 有符号 32 位除数 | 不为0 |

**返回值**

- 返回类型：long long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| -2^63 ~ 2^63-1 | dividend / divisor 的有符号商值 | 除数不为零时返回商 |

### osal_div64_u64 <a id="osal_div64_u64"></a>

```c
unsigned long long osal_div64_u64(unsigned long long dividend, unsigned long long divisor)
```

**声明头文件**

```c
#include "src/kernel/osal/include/math/osal_math.h"
```

**功能说明**

- 实现无符号 64 位整数除以无符号 64 位整数的除法运算。
- 返回除法运算的商。
- 适用于需要高精度无符号 64 位整数除法的场景。

**前置条件**

- 上下文限制：当前接口支持 linux 和 liteos 系统下使用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| dividend | unsigned long long | 无符号 64 位被除数 | 0 ~ 2^64-1 |
| divisor | unsigned long long | 无符号 64 位除数 | 不为0 |

**返回值**

- 返回类型：unsigned long long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 ~ 2^64-1 | dividend / divisor 的无符号商值 | 除数不为零时返回商 |

### osal_div64_s64 <a id="osal_div64_s64"></a>

```c
long long osal_div64_s64(long long dividend, long long divisor)
```

**声明头文件**

```c
#include "src/kernel/osal/include/math/osal_math.h"
```

**功能说明**

- 实现有符号 64 位整数除以有符号 64 位整数的除法运算。
- 返回除法运算的商。
- 适用于需要高精度有符号 64 位整数除法的场景。

**前置条件**

- 上下文限制：当前接口支持 linux 和 liteos 系统下使用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| dividend | long long | 有符号 64 位被除数 | -2^63 ~ 2^63-1 |
| divisor | long long | 有符号 64 位除数 | 不为0 |

**返回值**

- 返回类型：long long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| -2^63 ~ 2^63-1 | dividend / divisor 的有符号商值 | 除数不为零时返回商 |

### osal_div_u64_rem <a id="osal_div_u64_rem"></a>

```c
unsigned long long osal_div_u64_rem(unsigned long long dividend, unsigned int divisor)
```

**声明头文件**

```c
#include "src/kernel/osal/include/math/osal_math.h"
```

**功能说明**

- 实现无符号 64 位整数除以无符号 32 位整数的取余运算。
- 返回除法运算的余数。
- 适用于需要高精度无符号整数取余的场景。

**前置条件**

- 上下文限制：当前接口支持 linux 和 liteos 系统下使用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| dividend | unsigned long long | 无符号 64 位被除数 | 0 ~ 2^64-1 |
| divisor | unsigned int | 无符号 32 位除数 | 不为0 |

**返回值**

- 返回类型：unsigned long long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 ~ 2^32-1 | dividend / divisor 的无符号余数 | 除数不为零时返回余数 |

### osal_div_s64_rem <a id="osal_div_s64_rem"></a>

```c
long long osal_div_s64_rem(long long dividend, int divisor)
```

**声明头文件**

```c
#include "src/kernel/osal/include/math/osal_math.h"
```

**功能说明**

- 实现有符号 64 位整数除以有符号 32 位整数的取余运算。
- 返回除法运算的余数。
- 适用于需要高精度有符号整数取余的场景。

**前置条件**

- 上下文限制：当前接口支持 linux 和 liteos 系统下使用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| dividend | long long | 有符号 64 位被除数 | -2^63 ~ 2^63-1 |
| divisor | int | 有符号 32 位除数 | 不为0 |

**返回值**

- 返回类型：long long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| -2^31 ~ 2^31-1 | dividend / divisor 的有符号余数 | 除数不为零时返回余数 |

### osal_div64_u64_rem <a id="osal_div64_u64_rem"></a>

```c
unsigned long long osal_div64_u64_rem(unsigned long long dividend, unsigned long long divisor)
```

**声明头文件**

```c
#include "src/kernel/osal/include/math/osal_math.h"
```

**功能说明**

- 实现无符号 64 位整数除以无符号 64 位整数的取余运算。
- 返回除法运算的余数。
- 适用于需要高精度无符号 64 位整数取余的场景。

**前置条件**

- 上下文限制：当前接口支持 linux 和 liteos 系统下使用。

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| dividend | unsigned long long | 无符号 64 位被除数 | 0 ~ 2^64-1 |
| divisor | unsigned long long | 无符号 64 位除数 | 不为0 |

**返回值**

- 返回类型：unsigned long long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 ~ 2^64-1 | dividend / divisor 的无符号余数 | 除数不为零时返回余数 |

### osal_get_random_int <a id="osal_get_random_int"></a>

```c
unsigned int osal_get_random_int(void)
```

**声明头文件**

```c
#include "src/kernel/osal/include/math/osal_math.h"
```

**功能说明**

- 生成无符号 32 位随机数。
- 返回生成的随机数值。
- 适用于需要随机数的场景。

**前置条件**

- 依赖关系：依赖系统随机数源已就绪。
- 上下文限制：当前接口支持 linux 和 liteos 系统下使用。

**返回值**

- 返回类型：unsigned int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 ~ 0xFFFFFFFF | 生成的无符号 32 位随机数 | 调用时返回随机数 |

## Macros

### osal_max <a id="osal_max"></a>

```c
#define osal_max(x, y)                 \
    ({                                 \
        __typeof__(x)_max1 = (x);      \
        __typeof__(y)_max2 = (y);      \
        (void)(&_max1 == &_max2);      \
        _max1 > _max2 ? _max1 : _max2; \
    })
```

### osal_min <a id="osal_min"></a>

```c
#define osal_min(x, y)                 \
    ({                                 \
        __typeof__(x)_min1 = (x);      \
        __typeof__(y)_min2 = (y);      \
        (void)(&_min1 == &_min2);      \
        _min1 < _min2 ? _min1 : _min2; \
    })
```

### osal_abs <a id="osal_abs"></a>

```c
#define osal_abs(x)                           \
    ({                                        \
        long ret;                             \
        if (sizeof(x) == sizeof(long)) {      \
            long __x = (x);                   \
            ret = (__x < 0) ? (-__x) : (__x); \
        } else {                              \
            int __x = (x);                    \
            ret = (__x < 0) ? (-__x) : (__x); \
        }                                     \
        ret;                                  \
    })
```
