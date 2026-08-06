# bitmap

bitmap 提供位数组的位操作功能，支持对 unsigned long 类型数组按位进行置位、清零、翻转与测试操作。该模块还支持在位数组中查找首个或下一个置位位与清零位的位置，基于 linux 内核位操作接口实现，仅在 linux 系统下可用。

**头文件清单**

```c
#include "math/osal_bitmap.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_bitmap_set_bit](#osal_bitmap_set_bit) | 置位位数组中指定编号的位 |
| [osal_bitmap_clear_bit](#osal_bitmap_clear_bit) | 清零位数组中指定编号的位 |
| [osal_bitmap_change_bit](#osal_bitmap_change_bit) | 翻转位数组中指定编号的位 |
| [osal_bitmap_test_bit](#osal_bitmap_test_bit) | 测试位数组中指定编号的位是否被置位 |
| [osal_bitmap_test_and_set_bit](#osal_bitmap_test_and_set_bit) | 置位指定位并返回该位的旧值 |
| [osal_bitmap_test_and_clear_bit](#osal_bitmap_test_and_clear_bit) | 清零指定位并返回该位的旧值 |
| [osal_bitmap_test_and_change_bit](#osal_bitmap_test_and_change_bit) | 翻转指定位并返回该位的旧值 |
| [osal_bitmap_find_first_zero_bit](#osal_bitmap_find_first_zero_bit) | 查找位数组中首个清零位的位置 |
| [osal_bitmap_find_first_bit](#osal_bitmap_find_first_bit) | 查找位数组中首个置位位的位置 |
| [osal_bitmap_find_next_zero_bit](#osal_bitmap_find_next_zero_bit) | 从指定位移起查找下一个清零位的位置 |
| [osal_bitmap_find_next_bit](#osal_bitmap_find_next_bit) | 从指定位移起查找下一个置位位的位置 |

## Functions

### osal_bitmap_set_bit <a id="osal_bitmap_set_bit"></a>

```c
void osal_bitmap_set_bit(int nr, unsigned long *addr)
```

**头文件清单**

```c
#include "math/osal_bitmap.h"
```

**功能说明**

- 将指定位数组中指定编号的位设置为1
- 操作对象为 unsigned long 类型数组表示的位数组
- 用于在位图中标记某个位为已占用状态

**前置条件**

- 上下文限制：当前接口仅在 linux 系统下可用
- 依赖关系：addr 指向的位数组内存已有效分配

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| nr | int | 位编号，指定要置位的位在位数组中的位置 | >= 0 |
| addr | unsigned long * | 位数组地址，指向要操作的 unsigned long 数组 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| addr | unsigned long * | 操作完成后的位数组，指定位已被置位（值为1） |

### osal_bitmap_clear_bit <a id="osal_bitmap_clear_bit"></a>

```c
void osal_bitmap_clear_bit(int nr, unsigned long *addr)
```

**头文件清单**

```c
#include "math/osal_bitmap.h"
```

**功能说明**

- 清零指定位数组中指定编号的位
- 操作对象为 unsigned long 类型数组表示的位数组
- 用于在位图中释放某个位的占用状态

**前置条件**

- 上下文限制：当前接口仅在 linux 系统下可用
- 依赖关系：addr 指向的位数组内存已有效分配

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| nr | int | 位编号，指定要清零的位在位数组中的位置 | >= 0 |
| addr | unsigned long * | 位数组地址，指向要操作的 unsigned long 数组 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| addr | unsigned long * | 操作完成后的位数组，指定位已被清零（值为0） |

### osal_bitmap_change_bit <a id="osal_bitmap_change_bit"></a>

```c
void osal_bitmap_change_bit(int nr, unsigned long *addr)
```

**头文件清单**

```c
#include "math/osal_bitmap.h"
```

**功能说明**

- 翻转指定位数组中指定编号的位（0变1，1变0）
- 操作对象为 unsigned long 类型数组表示的位数组
- 用于在位图中切换某个位的状态

**前置条件**

- 上下文限制：当前接口仅在 linux 系统下可用
- 依赖关系：addr 指向的位数组内存已有效分配

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| nr | int | 位编号，指定要翻转的位在位数组中的位置 | >= 0 |
| addr | unsigned long * | 位数组地址，指向要操作的 unsigned long 数组 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| addr | unsigned long * | 操作完成后的位数组，指定位已被翻转 |

### osal_bitmap_test_bit <a id="osal_bitmap_test_bit"></a>

```c
int osal_bitmap_test_bit(int nr, unsigned long *addr)
```

**头文件清单**

```c
#include "math/osal_bitmap.h"
```

**功能说明**

- 测试指定位数组中指定编号的位是否被置位
- 返回值为该位的当前状态（0表示未置位，非0表示已置位）
- 操作对象为 unsigned long 类型数组表示的位数组

**前置条件**

- 上下文限制：当前接口仅在 linux 系统下可用
- 依赖关系：addr 指向的位数组内存已有效分配

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| nr | int | 位编号，指定要测试的位在位数组中的位置 | >= 0 |
| addr | unsigned long * | 位数组地址，指向要读取的 unsigned long 数组 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 该位未置位（false） | 指定位当前值为0 |
| 非0 | 该位已置位（true） | 指定位当前值为1 |
| -1 | 执行失败 | addr 为 NULL |

### osal_bitmap_test_and_set_bit <a id="osal_bitmap_test_and_set_bit"></a>

```c
int osal_bitmap_test_and_set_bit(int nr, unsigned long *addr)
```

**头文件清单**

```c
#include "math/osal_bitmap.h"
```

**功能说明**

- 置位指定位数组中指定编号的位并返回该位的旧值
- 返回值为操作前该位的原始状态（0表示原位未置位，非0表示原位已置位）
- 操作对象为 unsigned long 类型数组表示的位数组

**前置条件**

- 上下文限制：当前接口仅在 linux 系统下可用
- 依赖关系：addr 指向的位数组内存已有效分配

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| nr | int | 位编号，指定要置位的位在位数组中的位置 | >= 0 |
| addr | unsigned long * | 位数组地址，指向要操作的 unsigned long 数组 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| addr | unsigned long * | 操作完成后的位数组，指定位已被置位（值为1） |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 原位未置位 | 操作前该位值为0 |
| 非0 | 原位已置位 | 操作前该位值为1 |
| -1 | 执行失败 | addr 为 NULL |

### osal_bitmap_test_and_clear_bit <a id="osal_bitmap_test_and_clear_bit"></a>

```c
int osal_bitmap_test_and_clear_bit(int nr, unsigned long *addr)
```

**头文件清单**

```c
#include "math/osal_bitmap.h"
```

**功能说明**

- 清零指定位数组中指定编号的位并返回该位的旧值
- 返回值为操作前该位的原始状态（0表示原位未置位，非0表示原位已置位）
- 操作对象为 unsigned long 类型数组表示的位数组

**前置条件**

- 上下文限制：当前接口仅在 linux 系统下可用
- 依赖关系：addr 指向的位数组内存已有效分配

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| nr | int | 位编号，指定要清零的位在位数组中的位置 | >= 0 |
| addr | unsigned long * | 位数组地址，指向要操作的 unsigned long 数组 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| addr | unsigned long * | 操作完成后的位数组，指定位已被清零（值为0） |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 原位未置位 | 操作前该位值为0 |
| 非0 | 原位已置位 | 操作前该位值为1 |
| -1 | 执行失败 | addr 为 NULL |

### osal_bitmap_test_and_change_bit <a id="osal_bitmap_test_and_change_bit"></a>

```c
int osal_bitmap_test_and_change_bit(int nr, unsigned long *addr)
```

**头文件清单**

```c
#include "math/osal_bitmap.h"
```

**功能说明**

- 翻转指定位数组中指定编号的位并返回该位的旧值
- 返回值为操作前该位的原始状态（0表示原位未置位，非0表示原位已置位）
- 操作对象为 unsigned long 类型数组表示的位数组

**前置条件**

- 上下文限制：当前接口仅在 linux 系统下可用
- 依赖关系：addr 指向的位数组内存已有效分配

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| nr | int | 位编号，指定要翻转的位在位数组中的位置 | >= 0 |
| addr | unsigned long * | 位数组地址，指向要操作的 unsigned long 数组 | 不为NULL |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| addr | unsigned long * | 操作完成后的位数组，指定位已被翻转 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 0 | 原位未置位 | 操作前该位值为0 |
| 非0 | 原位已置位 | 操作前该位值为1 |
| -1 | 执行失败 | addr 为 NULL |

### osal_bitmap_find_first_zero_bit <a id="osal_bitmap_find_first_zero_bit"></a>

```c
int osal_bitmap_find_first_zero_bit(const unsigned long *name, unsigned size)
```

**头文件清单**

```c
#include "math/osal_bitmap.h"
```

**功能说明**

- 在指定位数组中查找首个清零位（值为0的位）的位置
- 返回值为首个清零位的位编号
- 查找范围为从位0开始的 size 个位

**前置条件**

- 上下文限制：当前接口仅在 linux 系统下可用
- 依赖关系：name 指向的位数组内存已有效分配

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| name | const unsigned long * | 位数组地址，指向要查找的 unsigned long 数组 | 不为NULL |
| size | unsigned | 位数组的位数大小，指定查找范围 | > 0 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| >=0 | 首个清零位的位置 | 在位图中找到首个清零位 |
| -1 | 执行失败 | name 为 NULL |

### osal_bitmap_find_first_bit <a id="osal_bitmap_find_first_bit"></a>

```c
int osal_bitmap_find_first_bit(const unsigned long *name, unsigned size)
```

**头文件清单**

```c
#include "math/osal_bitmap.h"
```

**功能说明**

- 在指定位数组中查找首个置位位（值为1的位）的位置
- 返回值为首个置位位的位编号
- 查找范围为从位0开始的 size 个位

**前置条件**

- 上下文限制：当前接口仅在 linux 系统下可用
- 依赖关系：name 指向的位数组内存已有效分配

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| name | const unsigned long * | 位数组地址，指向要查找的 unsigned long 数组 | 不为NULL |
| size | unsigned | 位数组的位数大小，指定查找范围 | > 0 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| >=0 | 首个置位位的位置 | 在位图中找到首个置位位 |
| -1 | 执行失败 | name 为 NULL |

### osal_bitmap_find_next_zero_bit <a id="osal_bitmap_find_next_zero_bit"></a>

```c
int osal_bitmap_find_next_zero_bit(const unsigned long *name, int size, int offset)
```

**头文件清单**

```c
#include "math/osal_bitmap.h"
```

**功能说明**

- 在指定位数组中从指定位移开始查找下一个清零位（值为0的位）的位置
- 返回值为下一个清零位的位编号
- 查找范围为从 offset 开始的 size 个位

**前置条件**

- 上下文限制：当前接口仅在 linux 系统下可用
- 依赖关系：name 指向的位数组内存已有效分配

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| name | const unsigned long * | 位数组地址，指向要查找的 unsigned long 数组 | 不为NULL |
| size | int | 位数组的位数大小，指定查找范围上限 | > 0 |
| offset | int | 起始搜索的位编号 | >= 0 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| >=0 | 下一个清零位的位置 | 从 offset 起找到下一个清零位 |
| -1 | 执行失败 | name 为 NULL |

### osal_bitmap_find_next_bit <a id="osal_bitmap_find_next_bit"></a>

```c
int osal_bitmap_find_next_bit(const unsigned long *name, unsigned size, int offset)
```

**头文件清单**

```c
#include "math/osal_bitmap.h"
```

**功能说明**

- 在指定位数组中从指定位移开始查找下一个置位位（值为1的位）的位置
- 返回值为下一个置位位的位编号
- 查找范围为从 offset 开始的 size 个位

**前置条件**

- 上下文限制：当前接口仅在 linux 系统下可用
- 依赖关系：name 指向的位数组内存已有效分配

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| name | const unsigned long * | 位数组地址，指向要查找的 unsigned long 数组 | 不为NULL |
| size | unsigned | 位数组的位数大小，指定查找范围上限 | > 0 |
| offset | int | 起始搜索的位编号 | >= 0 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| >=0 | 下一个置位位的位置 | 从 offset 起找到下一个置位位 |
| -1 | 执行失败 | name 为 NULL |
