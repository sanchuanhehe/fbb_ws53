# string

string 提供操作系统抽象层的字符串与内存操作接口，包括字符串比较、字符查找、子串定位、字符串长度计算、字符串分割、内存比较、内存字符查找以及字符串到整数的转换功能。

**头文件清单**

```c
#include "string/osal_string.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_memncmp](#osal_memncmp) | 比较两个内存区域的前 size 字节 |
| [osal_strcmp](#osal_strcmp) | 比较两个字符串 |
| [osal_strncmp](#osal_strncmp) | 比较两个字符串的前 size 字节 |
| [osal_strcasecmp](#osal_strcasecmp) | 忽略大小写比较两个字符串 |
| [osal_strncasecmp](#osal_strncasecmp) | 忽略大小写比较两个字符串的前 size 字节 |
| [osal_strchr](#osal_strchr) | 在字符串中查找指定字符的首次出现位置 |
| [osal_strnchr](#osal_strnchr) | 在长度受限的字符串中查找指定字符的首次出现位置 |
| [osal_strrchr](#osal_strrchr) | 在字符串中查找指定字符的最后一次出现位置 |
| [osal_strstr](#osal_strstr) | 在字符串中查找子串的首次出现位置 |
| [osal_strnstr](#osal_strnstr) | 在长度受限的字符串中查找子串的首次出现位置 |
| [osal_strlen](#osal_strlen) | 计算字符串长度 |
| [osal_strnlen](#osal_strnlen) | 计算长度受限的字符串长度 |
| [osal_strpbrk](#osal_strpbrk) | 在字符串中搜索字符集合中任一字符的首次出现位置 |
| [osal_strsep](#osal_strsep) | 从字符串中提取分隔符之间的标记 |
| [osal_strspn](#osal_strspn) | 计算字符串前缀中仅包含指定字符集的长度 |
| [osal_strcspn](#osal_strcspn) | 计算字符串前缀中不包含指定字符集的长度 |
| [osal_memscan](#osal_memscan) | 在内存区域中查找指定字节 |
| [osal_memcmp](#osal_memcmp) | 比较两个内存区域 |
| [osal_memchr](#osal_memchr) | 在内存区域中查找指定字节的首次出现位置 |
| [osal_memchr_inv](#osal_memchr_inv) | 在内存区域中查找与指定字节不匹配的首个字节 |
| [osal_strtoull](#osal_strtoull) | 将字符串转换为 unsigned long long 整数 |
| [osal_strtoul](#osal_strtoul) | 将字符串转换为 unsigned long 整数 |
| [osal_strtol](#osal_strtol) | 将字符串转换为 long 整数 |
| [osal_strtoll](#osal_strtoll) | 将字符串转换为 long long 整数 |

## Functions

### osal_memncmp <a id="osal_memncmp"></a>

```c
int osal_memncmp(const void *buf1, const void *buf2, unsigned long size)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 比较内存区域 buf1 和 buf2 的前 size 字节
- 返回值小于零表示 buf1 小于 buf2，等于零表示两者相同，大于零表示 buf1 大于 buf2

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| buf1 | const void * | 待比较的内存区域指针 | 有效内存地址，非 NULL |
| buf2 | const void * | 待比较的内存区域指针 | 有效内存地址，非 NULL |
| size | unsigned long | 待比较的字节数 | 大于 0 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| < 0 | buf1 小于 buf2 | 前 size 字节中 buf1 的值小于 buf2 |
| 0 | buf1 等于 buf2 | 前 size 字节完全相同 |
| > 0 | buf1 大于 buf2 | 前 size 字节中 buf1 的值大于 buf2 |

### osal_strcmp <a id="osal_strcmp"></a>

```c
int osal_strcmp(const char *s1, const char *s2)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 比较字符串 s1 和 s2
- 返回值小于零表示 s1 小于 s2，等于零表示两者相同，大于零表示 s1 大于 s2

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| s1 | const char * | 待比较的字符串指针 | 有效字符串指针，以 '\0' 结尾 |
| s2 | const char * | 待比较的字符串指针 | 有效字符串指针，以 '\0' 结尾 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| < 0 | s1 小于 s2 | s1 的字典序小于 s2 |
| 0 | s1 等于 s2 | 两个字符串完全相同 |
| > 0 | s1 大于 s2 | s1 的字典序大于 s2 |

**参考案例**

- `src/protocol/wifi/source/host/feature/hmac_single_proxysta.c`
- `src/protocol/wifi/source/host/feature/interface/hmac_ccpriv.c`
- `src/protocol/wifi/source/host/hmac/hmac_alg_config.c`

### osal_strncmp <a id="osal_strncmp"></a>

```c
int osal_strncmp(const char *s1, const char *s2, unsigned long size)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 比较字符串 s1 和 s2 的前 size 字节
- 返回值小于零表示 s1 小于 s2，等于零表示两者相同，大于零表示 s1 大于 s2

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| s1 | const char * | 待比较的字符串指针 | 有效字符串指针，以 '\0' 结尾 |
| s2 | const char * | 待比较的字符串指针 | 有效字符串指针，以 '\0' 结尾 |
| size | unsigned long | 待比较的最大字节数 | 大于 0 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| < 0 | s1 小于 s2 | 前 size 字节中 s1 的字典序小于 s2 |
| 0 | s1 等于 s2 | 前 size 字节完全相同 |
| > 0 | s1 大于 s2 | 前 size 字节中 s1 的字典序大于 s2 |

### osal_strcasecmp <a id="osal_strcasecmp"></a>

```c
int osal_strcasecmp(const char *s1, const char *s2)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 忽略大小写逐字节比较字符串 s1 和 s2
- 返回值小于零表示 s1 小于 s2，等于零表示两者相同，大于零表示 s1 大于 s2

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| s1 | const char * | 待比较的字符串指针 | 有效字符串指针，以 '\0' 结尾 |
| s2 | const char * | 待比较的字符串指针 | 有效字符串指针，以 '\0' 结尾 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| < 0 | s1 小于 s2 | 忽略大小写后 s1 的字典序小于 s2 |
| 0 | s1 等于 s2 | 忽略大小写后两个字符串完全相同 |
| > 0 | s1 大于 s2 | 忽略大小写后 s1 的字典序大于 s2 |

### osal_strncasecmp <a id="osal_strncasecmp"></a>

```c
int osal_strncasecmp(const char *s1, const char *s2, unsigned long size)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 忽略大小写逐字节比较字符串 s1 和 s2 的前 size 字节
- 返回值小于零表示 s1 小于 s2，等于零表示两者相同，大于零表示 s1 大于 s2

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| s1 | const char * | 待比较的字符串指针 | 有效字符串指针，以 '\0' 结尾 |
| s2 | const char * | 待比较的字符串指针 | 有效字符串指针，以 '\0' 结尾 |
| size | unsigned long | 待比较的最大字节数 | 大于 0 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| < 0 | s1 小于 s2 | 忽略大小写后前 size 字节中 s1 的字典序小于 s2 |
| 0 | s1 等于 s2 | 忽略大小写后前 size 字节完全相同 |
| > 0 | s1 大于 s2 | 忽略大小写后前 size 字节中 s1 的字典序大于 s2 |

### osal_strchr <a id="osal_strchr"></a>

```c
char *osal_strchr(const char *s, int n)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 在字符串 s 中查找字符 n 的首次出现位置
- 返回指向该字符的指针，若未找到则返回 NULL

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| s | const char * | 待搜索的字符串指针 | 有效字符串指针，以 '\0' 结尾 |
| n | int | 待查找的字符 | 字符的整数值 |

**返回值**

- 返回类型：char *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非 NULL | 指向字符 n 首次出现位置的指针 | 在字符串中找到字符 n |
| NULL | 未找到指定字符 | 字符串中不包含字符 n |

### osal_strnchr <a id="osal_strnchr"></a>

```c
char *osal_strnchr(const char *s, int count, int c)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 在字符串 s 的前 count 个字符范围内查找字符 c 的首次出现位置
- 返回指向该字符的指针，若未找到则返回 NULL

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| s | const char * | 待搜索的字符串指针 | 有效字符串指针 |
| count | int | 待搜索的字符数 | 大于 0 |
| c | int | 待查找的字符 | 字符的整数值 |

**返回值**

- 返回类型：char *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非 NULL | 指向字符 c 首次出现位置的指针 | 在前 count 个字符中找到字符 c |
| NULL | 未找到指定字符 | 前 count 个字符中不包含字符 c |

### osal_strrchr <a id="osal_strrchr"></a>

```c
char *osal_strrchr(const char *s, int c)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 在字符串 s 中查找字符 c 的最后一次出现位置
- 返回指向该字符的指针，若未找到则返回 NULL

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| s | const char * | 待搜索的字符串指针 | 有效字符串指针，以 '\0' 结尾 |
| c | int | 待查找的字符 | 字符的整数值 |

**返回值**

- 返回类型：char *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非 NULL | 指向字符 c 最后一次出现位置的指针 | 在字符串中找到字符 c |
| NULL | 未找到指定字符 | 字符串中不包含字符 c |

### osal_strstr <a id="osal_strstr"></a>

```c
char *osal_strstr(const char *s1, const char *s2)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 在字符串 s1 中查找子串 s2 的首次出现位置
- 返回指向子串起始位置的指针，若未找到则返回 NULL

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| s1 | const char * | 待搜索的字符串指针 | 有效字符串指针，以 '\0' 结尾 |
| s2 | const char * | 待查找的子串指针 | 有效字符串指针，以 '\0' 结尾 |

**返回值**

- 返回类型：char *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非 NULL | 指向子串 s2 首次出现位置的指针 | 在 s1 中找到子串 s2 |
| NULL | 未找到子串 | s1 中不包含子串 s2 |

**参考案例**

- `src/middleware/utils/syschannel/syschannel_host/channel_host/syschannel_host_adapt.c`

### osal_strnstr <a id="osal_strnstr"></a>

```c
char *osal_strnstr(const char *s1, const char *s2, int n)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 在字符串 s1 的前 n 个字符范围内查找子串 s2 的首次出现位置
- 返回指向子串起始位置的指针，若未找到则返回 NULL

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| s1 | const char * | 待搜索的字符串指针 | 有效字符串指针 |
| s2 | const char * | 待查找的子串指针 | 有效字符串指针 |
| n | int | 待搜索的长度 | 大于 0 |

**返回值**

- 返回类型：char *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非 NULL | 指向子串 s2 首次出现位置的指针 | 在前 n 个字符中找到子串 s2 |
| NULL | 未找到子串 | 前 n 个字符中不包含子串 s2 |

### osal_strlen <a id="osal_strlen"></a>

```c
unsigned int osal_strlen(const char *s)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 计算字符串 s 的长度，不包含终止符 '\0'

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| s | const char * | 待计算长度的字符串指针 | 有效字符串指针，以 '\0' 结尾 |

**返回值**

- 返回类型：unsigned int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非负整数 | 字符串长度 | 字符串中 '\0' 之前的字符数 |

**参考案例**

- `src/middleware/utils/syschannel/syschannel_host/channel_host/syschannel_host_adapt.c`
- `src/protocol/wifi/source/host/feature/hmac_11k.c`
- `src/protocol/wifi/source/host/feature/hmac_apf.c`

### osal_strnlen <a id="osal_strnlen"></a>

```c
unsigned int osal_strnlen(const char *s, unsigned int size)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 计算字符串 s 的长度，但不越过 s + size 的范围
- 返回字符串中 '\0' 之前的字符数，最多返回 size

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| s | const char * | 待计算长度的字符串指针 | 有效字符串指针 |
| size | unsigned int | 最大搜索范围 | 大于 0 |

**返回值**

- 返回类型：unsigned int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非负整数 | 字符串长度 | 字符串中 '\0' 之前的字符数，不超过 size |

### osal_strpbrk <a id="osal_strpbrk"></a>

```c
char *osal_strpbrk(const char *s1, const char *s2)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 在字符串 s1 中搜索字符集合 s2 中任一字符的首次出现位置
- 返回指向该字符的指针，若未找到则返回 NULL

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| s1 | const char * | 待搜索的字符串指针 | 有效字符串指针，以 '\0' 结尾 |
| s2 | const char * | 待匹配的字符集合指针 | 有效字符串指针，以 '\0' 结尾 |

**返回值**

- 返回类型：char *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非 NULL | 指向 s1 中匹配 s2 任一字符的首个位置 | 在 s1 中找到 s2 中的字符 |
| NULL | 未找到匹配字符 | s1 中不包含 s2 中的任何字符 |

### osal_strsep <a id="osal_strsep"></a>

```c
char *osal_strsep(char **s, const char *ct)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 从字符串中提取以分隔符 ct 分隔的下一个标记
- 更新 *s 指向分隔符之后的下一个位置

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| s | char ** | 指向待分割字符串指针的指针，调用后更新为下一个待分割位置 | 有效二级指针，*s 为有效字符串或 NULL |
| ct | const char * | 分隔符字符集合 | 有效字符串指针，以 '\0' 结尾 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| s | char ** | 更新为分隔符之后的下一个待分割位置 |

**返回值**

- 返回类型：char *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非 NULL | 指向提取的标记的指针 | 成功提取到标记 |
| NULL | 无更多标记可提取 | *s 为 NULL |

### osal_strspn <a id="osal_strspn"></a>

```c
unsigned int osal_strspn(const char *s, const char *accept)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 计算字符串 s 前缀中仅由 accept 中字符组成的长度

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| s | const char * | 待计算的字符串指针 | 有效字符串指针，以 '\0' 结尾 |
| accept | const char * | 允许的字符集合 | 有效字符串指针，以 '\0' 结尾 |

**返回值**

- 返回类型：unsigned int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非负整数 | s 前缀中仅包含 accept 字符的字节数 | 正常计算 |

### osal_strcspn <a id="osal_strcspn"></a>

```c
unsigned int osal_strcspn(const char *s, const char *reject)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 计算字符串 s 前缀中不包含 reject 中任何字符的长度

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| s | const char * | 待计算的字符串指针 | 有效字符串指针，以 '\0' 结尾 |
| reject | const char * | 排除的字符集合 | 有效字符串指针，以 '\0' 结尾 |

**返回值**

- 返回类型：unsigned int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非负整数 | s 前缀中不包含 reject 字符的字节数 | 正常计算 |

### osal_memscan <a id="osal_memscan"></a>

```c
void *osal_memscan(void *addr, int c, int size)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 在内存区域 addr 的前 size 字节中查找字节 c
- 返回指向该字节首次出现位置的指针，若未找到则返回内存区域末尾之后一个字节的地址

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| addr | void * | 待搜索的内存区域指针 | 有效内存地址 |
| c | int | 待查找的字节值 | 字节的整数值 |
| size | int | 待搜索的字节数 | 大于 0 |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非 NULL | 指向字节 c 首次出现位置的指针，或内存区域末尾之后一个字节的地址 | 查找完成 |

### osal_memcmp <a id="osal_memcmp"></a>

```c
int osal_memcmp(const void *cs, const void *ct, int count)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 比较内存区域 cs 和 ct 的前 count 字节
- 返回值小于零表示 cs 小于 ct，等于零表示两者相同，大于零表示 cs 大于 ct

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| cs | const void * | 待比较的内存区域指针 | 有效内存地址，非 NULL |
| ct | const void * | 待比较的内存区域指针 | 有效内存地址，非 NULL |
| count | int | 待比较的字节数 | 大于 0 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| < 0 | cs 小于 ct | 前 count 字节中 cs 的值小于 ct |
| 0 | cs 等于 ct | 前 count 字节完全相同 |
| > 0 | cs 大于 ct | 前 count 字节中 cs 的值大于 ct |

**参考案例**

- `src/protocol/wifi/source/host/feature/hmac_11k.c`
- `src/protocol/wifi/source/host/feature/hmac_11v.c`
- `src/protocol/wifi/source/host/feature/hmac_blacklist.c`

### osal_memchr <a id="osal_memchr"></a>

```c
void *osal_memchr(const void *s, int c, int n)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 在内存区域 s 的前 n 字节中查找字节 c 的首次出现位置
- 返回指向该字节的指针，若未找到则返回 NULL

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| s | const void * | 待搜索的内存区域指针 | 有效内存地址 |
| c | int | 待查找的字节值 | 字节的整数值 |
| n | int | 待搜索的字节数 | 大于 0 |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非 NULL | 指向字节 c 首次出现位置的指针 | 在前 n 字节中找到字节 c |
| NULL | 未找到指定字节 | 前 n 字节中不包含字节 c |

### osal_memchr_inv <a id="osal_memchr_inv"></a>

```c
void *osal_memchr_inv(const void *s, int c, int n)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 在内存区域 s 的前 n 字节中查找与字节 c 不匹配的首个字节
- 返回指向该不匹配字节的指针，若全部匹配则返回 NULL

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| s | const void * | 待搜索的内存区域指针 | 有效内存地址 |
| c | int | 参考字节值 | 字节的整数值 |
| n | int | 待搜索的字节数 | 大于 0 |

**返回值**

- 返回类型：void *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非 NULL | 指向首个与 c 不匹配的字节的指针 | 找到不匹配字节 |
| NULL | 全部字节均与 c 匹配 | 前 n 字节全部等于 c |

### osal_strtoull <a id="osal_strtoull"></a>

```c
unsigned long long osal_strtoull(const char *cp, char **endp, unsigned int base)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 将字符串 cp 按 base 指定的进制转换为 unsigned long long 整数
- 支持 2 到 36 进制，base 为 0 时根据字符串前缀自动判断进制（0x 为十六进制，0 为八进制，否则为十进制）
- 若 endp 不为 NULL，将第一个无效字符的地址存入 *endp

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| cp | const char * | 待转换的字符串指针 | 有效字符串指针 |
| endp | char ** | 用于存储第一个无效字符地址的指针，可为 NULL | NULL 或有效的二级指针 |
| base | unsigned int | 转换的进制基数 | [OSAL_BASE_DEC](#OSAL_BASE_DEC)(10) / [OSAL_BASE_HEX](#OSAL_BASE_HEX)(16) / 0 / 2~36 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| endp | char ** | 若 endp 不为 NULL，存储第一个无效字符的地址 |

**返回值**

- 返回类型：unsigned long long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 转换结果 | 字符串转换后的无符号长长整数值 | 正常转换 |
| ULLONG_MAX | 溢出 | 转换结果超出 unsigned long long 范围，errno 设置为 ERANGE |

### osal_strtoul <a id="osal_strtoul"></a>

```c
unsigned long osal_strtoul(const char *cp, char **endp, unsigned int base)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 将字符串 cp 按 base 指定的进制转换为 unsigned long 整数
- 支持 2 到 36 进制，base 为 0 时根据字符串前缀自动判断进制（0x 为十六进制，0 为八进制，否则为十进制）
- 若 endp 不为 NULL，将第一个无效字符的地址存入 *endp

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| cp | const char * | 待转换的字符串指针 | 有效字符串指针 |
| endp | char ** | 用于存储第一个无效字符地址的指针，可为 NULL | NULL 或有效的二级指针 |
| base | unsigned int | 转换的进制基数 | [OSAL_BASE_DEC](#OSAL_BASE_DEC)(10) / [OSAL_BASE_HEX](#OSAL_BASE_HEX)(16) / 0 / 2~36 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| endp | char ** | 若 endp 不为 NULL，存储第一个无效字符的地址 |

**返回值**

- 返回类型：unsigned long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 转换结果 | 字符串转换后的无符号长整数值 | 正常转换 |
| ULONG_MAX | 溢出 | 转换结果超出 unsigned long 范围，errno 设置为 ERANGE |

**参考案例**

- `src/protocol/wifi/source/host/wal/common/wal_ccpriv_common.c`

### osal_strtol <a id="osal_strtol"></a>

```c
long osal_strtol(const char *cp, char **endp, unsigned int base)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 将字符串 cp 按 base 指定的进制转换为 long 整数
- 支持 2 到 36 进制，base 为 0 时根据字符串前缀自动判断进制（0x 为十六进制，0 为八进制，否则为十进制）
- 若 endp 不为 NULL，将第一个无效字符的地址存入 *endp

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| cp | const char * | 待转换的字符串指针 | 有效字符串指针 |
| endp | char ** | 用于存储第一个无效字符地址的指针，可为 NULL | NULL 或有效的二级指针 |
| base | unsigned int | 转换的进制基数 | [OSAL_BASE_DEC](#OSAL_BASE_DEC)(10) / [OSAL_BASE_HEX](#OSAL_BASE_HEX)(16) / 0 / 2~36 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| endp | char ** | 若 endp 不为 NULL，存储第一个无效字符的地址 |

**返回值**

- 返回类型：long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 转换结果 | 字符串转换后的长整数值 | 正常转换 |
| LONG_MAX | 溢出 | 转换结果超出 long 范围，errno 设置为 ERANGE |

**参考案例**

- `src/protocol/wifi/source/host/feature/hmac_apf.c`
- `src/protocol/wifi/source/host/feature/hmac_btcoex.c`
- `src/protocol/wifi/source/host/wal/common/wal_ccpriv_common.c`
- `src/protocol/wifi/source/host/wal/release/liteOS/soc_wifi_driver_api.c`
- `src/protocol/wifi/source/host/wal/release/liteOS/wal_ccpriv.c`

### osal_strtoll <a id="osal_strtoll"></a>

```c
long long osal_strtoll(const char *cp, char **endp, unsigned int base)
```

**头文件清单**

```c
#include "string/osal_string.h"
```

**功能说明**

- 将字符串 cp 按 base 指定的进制转换为 long long 整数
- 支持 2 到 36 进制，base 为 0 时根据字符串前缀自动判断进制（0x 为十六进制，0 为八进制，否则为十进制）
- 若 endp 不为 NULL，将第一个无效字符的地址存入 *endp

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| cp | const char * | 待转换的字符串指针 | 有效字符串指针 |
| endp | char ** | 用于存储第一个无效字符地址的指针，可为 NULL | NULL 或有效的二级指针 |
| base | unsigned int | 转换的进制基数 | [OSAL_BASE_DEC](#OSAL_BASE_DEC)(10) / [OSAL_BASE_HEX](#OSAL_BASE_HEX)(16) / 0 / 2~36 |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| endp | char ** | 若 endp 不为 NULL，存储第一个无效字符的地址 |

**返回值**

- 返回类型：long long

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 转换结果 | 字符串转换后的长长整数值 | 正常转换 |
| LLONG_MAX | 溢出 | 转换结果超出 long long 范围，errno 设置为 ERANGE |

## Macros

### OSAL_BASE_DEC <a id="OSAL_BASE_DEC"></a>

```c
#define OSAL_BASE_DEC 10
```

### OSAL_BASE_HEX <a id="OSAL_BASE_HEX"></a>

```c
#define OSAL_BASE_HEX 16
```