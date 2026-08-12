# Others

others 模块提供 OSAL (OS Abstract Layer) 通用基础设施，核心为双向链表 (doubly linked list) 与哈希链表 (hash list) 的内联操作接口，涵盖链表节点的初始化、插入、删除、替换、移动、拼接、判空、切割与旋转等操作。所有接口以 static inline 函数形式实现于头文件中，无独立编译单元，不依赖 Kconfig 配置，可在任意包含该头文件的上下文中直接使用。模块还包含 OSAL 通用定义、错误码与 ioctl 辅助宏等头文件，为其他 OSAL 子模块提供基础类型与宏定义支撑。

**头文件清单**

```c
#include "osal_list.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [OSAL_INIT_LIST_HEAD](#OSAL_INIT_LIST_HEAD) | 初始化双向链表头节点，将 next/prev 指向自身 |
| [osal___list_add](#osal___list_add) | 在两个已知节点之间插入新节点（内部辅助函数） |
| [osal_list_add](#osal_list_add) | 在链表头部添加新节点（栈式插入） |
| [osal_list_add_tail](#osal_list_add_tail) | 在链表尾部添加新节点（队列式插入） |
| [osal___list_del](#osal___list_del) | 通过 prev/next 指针删除链表节点（内部辅助函数） |
| [osal___list_del_entry](#osal___list_del_entry) | 删除链表节点（内部辅助函数） |
| [osal_list_del](#osal_list_del) | 删除链表节点并将 next/prev 置为中毒值 |
| [osal_list_replace](#osal_list_replace) | 用新节点替换旧节点 |
| [osal_list_replace_init](#osal_list_replace_init) | 用新节点替换旧节点并重新初始化旧节点 |
| [osal_list_del_init](#osal_list_del_init) | 删除链表节点并重新初始化该节点 |
| [osal_list_move](#osal_list_move) | 将节点移动到另一链表头部 |
| [osal_list_move_tail](#osal_list_move_tail) | 将节点移动到另一链表尾部 |
| [osal_list_is_last](#osal_list_is_last) | 判断节点是否为链表的最后一个节点 |
| [osal_list_empty](#osal_list_empty) | 判断链表是否为空 |
| [osal_list_empty_careful](#osal_list_empty_careful) | 判断链表是否为空且未被修改 |
| [osal_list_rotate_left](#osal_list_rotate_left) | 将链表左旋一位 |
| [osal_list_is_singular](#osal_list_is_singular) | 判断链表是否仅含一个节点 |
| [osal___list_cut_position](#osal___list_cut_position) | 切割链表内部辅助函数 |
| [osal_list_cut_position](#osal_list_cut_position) | 将链表从指定位置切分为两个链表 |
| [osal___list_splice](#osal___list_splice) | 拼接两个链表内部辅助函数 |
| [osal_list_splice](#osal_list_splice) | 将一个链表拼接到另一链表头部 |
| [osal_list_splice_tail](#osal_list_splice_tail) | 将一个链表拼接到另一链表尾部 |
| [osal_list_splice_init](#osal_list_splice_init) | 拼接链表到头部并重新初始化源链表 |
| [osal_list_splice_tail_init](#osal_list_splice_tail_init) | 拼接链表到尾部并重新初始化源链表 |
| [INIT_OSAL_HLIST_NODE](#INIT_OSAL_HLIST_NODE) | 初始化哈希链表节点 |
| [osal_hlist_unhashed](#osal_hlist_unhashed) | 判断哈希链表节点是否未被哈希 |
| [osal_hlist_empty](#osal_hlist_empty) | 判断哈希链表是否为空 |
| [osal___hlist_del](#osal___hlist_del) | 删除哈希链表节点内部辅助函数 |
| [osal_hlist_del](#osal_hlist_del) | 删除哈希链表节点并标记为中毒状态 |
| [osal_hlist_del_init](#osal_hlist_del_init) | 删除哈希链表节点并重新初始化 |
| [osal_hlist_add_head](#osal_hlist_add_head) | 在哈希链表头部添加节点 |
| [osal_hlist_add_before](#osal_hlist_add_before) | 在指定节点之前添加新节点 |
| [osal_hlist_add_after](#osal_hlist_add_after) | 在指定节点之后添加新节点 |
| [osal_hlist_add_fake](#osal_hlist_add_fake) | 将节点伪添加到哈希链表 |
| [osal_hlist_move_list](#osal_hlist_move_list) | 将哈希链表从一个头移动到另一个头 |

## Functions

### OSAL_INIT_LIST_HEAD <a id="OSAL_INIT_LIST_HEAD"></a>

```c
void OSAL_INIT_LIST_HEAD(struct osal_list_head *list)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 初始化双向链表头节点
- 将 list 的 next 和 prev 指针均指向自身，形成自引用的空链表
- 当 list 为 NULL 时直接返回，不执行初始化操作

**前置条件**

- list 指向的内存必须已分配且可写

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| list | struct [osal_list_head](#osal_list_head) * | 指向待初始化的链表头节点 | 不为NULL |

**参考案例**

- `src/middleware/utils/hcc/comm/hcc_service.c`
- `src/kernel/osal/src/linux/kernel/osal_proc.c`

### osal___list_add <a id="osal___list_add"></a>

```c
void osal___list_add(struct osal_list_head *_new, struct osal_list_head *prev, struct osal_list_head *next)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 在两个已知连续节点 prev 和 next 之间插入新节点 _new
- 仅供内部链表操作使用，调用者需确保 prev 和 next 为连续节点
- 当 _new、prev 或 next 为 NULL 时直接返回，不执行插入

**前置条件**

- 调用时序约束：调用者必须已知 prev 和 next 为链表中连续的两个节点
- _new、prev、next 指向的内存必须已分配且可写

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| _new | struct [osal_list_head](#osal_list_head) * | 指向待插入的新节点 | 不为NULL |
| prev | struct [osal_list_head](#osal_list_head) * | 指向新节点的前驱节点 | 不为NULL |
| next | struct [osal_list_head](#osal_list_head) * | 指向新节点的后继节点 | 不为NULL |

### osal_list_add <a id="osal_list_add"></a>

```c
void osal_list_add(struct osal_list_head *cur, struct osal_list_head *head)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 在链表头部（head 之后）添加新节点 cur
- 适用于实现栈结构（后进先出）
- 内部调用 osal___list_add 在 head 与 head->next 之间插入

**前置条件**

- head 必须已通过 [OSAL_INIT_LIST_HEAD](#OSAL_INIT_LIST_HEAD) 初始化或通过 OSAL_LIST_HEAD 宏静态初始化
- cur 指向的内存必须已分配且可写

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| cur | struct [osal_list_head](#osal_list_head) * | 指向待添加的新节点 | 不为NULL |
| head | struct [osal_list_head](#osal_list_head) * | 指向链表头节点 | 不为NULL，且已初始化 |

**参考案例**

- `src/kernel/osal/src/linux/kernel/osal_workqueue.c`
- `src/kernel/osal/src/linux/kernel/osal_device.c`

### osal_list_add_tail <a id="osal_list_add_tail"></a>

```c
void osal_list_add_tail(struct osal_list_head *cur, struct osal_list_head *head)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 在链表尾部（head 之前）添加新节点 cur
- 适用于实现队列结构（先进先出）
- 内部调用 osal___list_add 在 head->prev 与 head 之间插入

**前置条件**

- head 必须已通过 [OSAL_INIT_LIST_HEAD](#OSAL_INIT_LIST_HEAD) 初始化或通过 OSAL_LIST_HEAD 宏静态初始化
- cur 指向的内存必须已分配且可写

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| cur | struct [osal_list_head](#osal_list_head) * | 指向待添加的新节点 | 不为NULL |
| head | struct [osal_list_head](#osal_list_head) * | 指向链表头节点 | 不为NULL，且已初始化 |

**参考案例**

- `src/middleware/utils/hcc/comm/hcc_channel.c`
- `src/kernel/osal/src/linux/kernel/osal_interrupt.c`
- `src/kernel/osal/src/linux/kernel/osal_proc.c`

### osal___list_del <a id="osal___list_del"></a>

```c
void osal___list_del(struct osal_list_head *prev, struct osal_list_head *next)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 通过修改 prev 和 next 指针来删除它们之间的节点
- 仅供内部链表操作使用，调用者需确保 prev 和 next 为被删节点的前后节点
- 当 prev 或 next 为 NULL 时直接返回，不执行删除

**前置条件**

- 调用时序约束：调用者必须已知 prev 和 next 分别为待删除节点的前驱和后继节点
- prev、next 指向的内存必须已分配且可写

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| prev | struct [osal_list_head](#osal_list_head) * | 指向待删除节点的前驱节点 | 不为NULL |
| next | struct [osal_list_head](#osal_list_head) * | 指向待删除节点的后继节点 | 不为NULL |

### osal___list_del_entry <a id="osal___list_del_entry"></a>

```c
void osal___list_del_entry(struct osal_list_head *entry)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 删除链表节点 entry，通过调用 osal___list_del 修改其前后节点指针
- 仅供内部链表操作使用
- 当 entry 为 NULL 时直接返回，不执行删除
- 删除后 entry 的 next/prev 指针处于未定义状态，不应再访问

**前置条件**

- entry 必须在链表中且指向有效内存

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| entry | struct [osal_list_head](#osal_list_head) * | 指向待删除的链表节点 | 不为NULL |

### osal_list_del <a id="osal_list_del"></a>

```c
void osal_list_del(struct osal_list_head *entry)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 删除链表节点 entry
- 删除后将 entry 的 next 指针置为 [OSAL_LIST_POISON1](#OSAL_LIST_POISON1)、prev 指针置为 [OSAL_LIST_POISON2](#OSAL_LIST_POISON2)，以捕获删除后误用问题
- 当 entry 为 NULL 时直接返回，不执行删除

**前置条件**

- entry 必须在链表中且指向有效内存
- 删除后禁止再通过该节点进行链表操作

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| entry | struct [osal_list_head](#osal_list_head) * | 指向待删除的链表节点 | 不为NULL |

**参考案例**

- `src/middleware/utils/hcc/comm/hcc_channel.c`
- `src/kernel/osal/src/linux/kernel/osal_interrupt.c`
- `src/kernel/osal/src/linux/kernel/osal_device.c`

### osal_list_replace <a id="osal_list_replace"></a>

```c
void osal_list_replace(struct osal_list_head *old, struct osal_list_head *_new)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 用新节点 _new 替换链表中的旧节点 old
- 替换后 _new 占据 old 原有的位置，old 的 next/prev 处于未定义状态
- 若 old 为空链表头则会被覆盖

**前置条件**

- old 必须在链表中且指向有效内存
- _new 指向的内存必须已分配且可写

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| old | struct [osal_list_head](#osal_list_head) * | 指向被替换的旧节点 | 不为NULL |
| _new | struct [osal_list_head](#osal_list_head) * | 指向替换用的新节点 | 不为NULL |

### osal_list_replace_init <a id="osal_list_replace_init"></a>

```c
void osal_list_replace_init(struct osal_list_head *old, struct osal_list_head *_new)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 用新节点 _new 替换链表中的旧节点 old
- 替换后对 old 调用 [OSAL_INIT_LIST_HEAD](#OSAL_INIT_LIST_HEAD) 重新初始化，使其成为空链表头

**前置条件**

- old 必须在链表中且指向有效内存
- _new 指向的内存必须已分配且可写

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| old | struct [osal_list_head](#osal_list_head) * | 指向被替换的旧节点 | 不为NULL |
| _new | struct [osal_list_head](#osal_list_head) * | 指向替换用的新节点 | 不为NULL |

### osal_list_del_init <a id="osal_list_del_init"></a>

```c
void osal_list_del_init(struct osal_list_head *entry)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 删除链表节点 entry
- 删除后对 entry 调用 [OSAL_INIT_LIST_HEAD](#OSAL_INIT_LIST_HEAD) 重新初始化，使其成为自引用的空节点
- 当 entry 为 NULL 时不执行操作

**前置条件**

- entry 必须在链表中且指向有效内存

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| entry | struct [osal_list_head](#osal_list_head) * | 指向待删除并重新初始化的链表节点 | 不为NULL |

**参考案例**

- `src/kernel/osal/src/linux/kernel/osal_proc.c`
- `src/kernel/osal/src/linux/kernel/osal_workqueue.c`

### osal_list_move <a id="osal_list_move"></a>

```c
void osal_list_move(struct osal_list_head *list, struct osal_list_head *head)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 将节点 list 从原链表中删除，并添加到目标链表 head 的头部
- 等效于先调用 osal___list_del_entry 再调用 osal_list_add

**前置条件**

- list 必须在某个链表中且指向有效内存
- head 必须已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| list | struct [osal_list_head](#osal_list_head) * | 指向待移动的节点 | 不为NULL |
| head | struct [osal_list_head](#osal_list_head) * | 指向目标链表头节点 | 不为NULL，且已初始化 |

**参考案例**

- `src/middleware/utils/hcc/host/hcc_ipc_host.c`

### osal_list_move_tail <a id="osal_list_move_tail"></a>

```c
void osal_list_move_tail(struct osal_list_head *list, struct osal_list_head *head)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 将节点 list 从原链表中删除，并添加到目标链表 head 的尾部
- 等效于先调用 osal___list_del_entry 再调用 osal_list_add_tail

**前置条件**

- list 必须在某个链表中且指向有效内存
- head 必须已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| list | struct [osal_list_head](#osal_list_head) * | 指向待移动的节点 | 不为NULL |
| head | struct [osal_list_head](#osal_list_head) * | 指向目标链表头节点 | 不为NULL，且已初始化 |

### osal_list_is_last <a id="osal_list_is_last"></a>

```c
int osal_list_is_last(const struct osal_list_head *list, const struct osal_list_head *head)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 判断节点 list 是否为链表 head 的最后一个节点
- 当 list 或 head 为 NULL 时返回 -1

**前置条件**

- head 必须已初始化
- list 必须在 head 所标识的链表中

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| list | const struct [osal_list_head](#osal_list_head) * | 指向待判断的节点 | 不为NULL |
| head | const struct [osal_list_head](#osal_list_head) * | 指向链表头节点 | 不为NULL，且已初始化 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 1 | list 是最后一个节点 | list->next 等于 head |
| 0 | list 不是最后一个节点 | list->next 不等于 head |
| -1 | 输入无效 | list 或 head 为 NULL |

### osal_list_empty <a id="osal_list_empty"></a>

```c
int osal_list_empty(const struct osal_list_head *head)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 判断链表是否为空
- 当 head 为 NULL 时返回 -1

**前置条件**

- head 必须已通过 [OSAL_INIT_LIST_HEAD](#OSAL_INIT_LIST_HEAD) 初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| head | const struct [osal_list_head](#osal_list_head) * | 指向链表头节点 | 不为NULL，且已初始化 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 1 | 链表为空 | head->next 等于 head |
| 0 | 链表不为空 | head->next 不等于 head |
| -1 | 输入无效 | head 为 NULL |

**参考案例**

- `src/kernel/osal/src/linux/kernel/osal_interrupt.c`
- `src/kernel/osal/src/linux/kernel/osal_proc.c`

### osal_list_empty_careful <a id="osal_list_empty_careful"></a>

```c
int osal_list_empty_careful(const struct osal_list_head *head)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 判断链表是否为空且未被其他 CPU 修改
- 检查 head->next 是否等于 head 且 head->next 是否等于 head->prev
- 当 head 为 NULL 时返回 -1

**前置条件**

- head 必须已通过 [OSAL_INIT_LIST_HEAD](#OSAL_INIT_LIST_HEAD) 初始化
- 无同步保护下使用时，仅允许 list_del_init 操作

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| head | const struct [osal_list_head](#osal_list_head) * | 指向链表头节点 | 不为NULL，且已初始化 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 1 | 链表为空且未被修改 | head->next 等于 head 且等于 head->prev |
| 0 | 链表不为空或可能被修改 | 上述条件不满足 |
| -1 | 输入无效 | head 为 NULL |

### osal_list_rotate_left <a id="osal_list_rotate_left"></a>

```c
void osal_list_rotate_left(struct osal_list_head *head)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 将链表左旋一位，把第一个节点移动到链表尾部
- 当链表为空时不执行操作

**前置条件**

- head 必须已通过 [OSAL_INIT_LIST_HEAD](#OSAL_INIT_LIST_HEAD) 初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| head | struct [osal_list_head](#osal_list_head) * | 指向链表头节点 | 不为NULL，且已初始化 |

### osal_list_is_singular <a id="osal_list_is_singular"></a>

```c
int osal_list_is_singular(const struct osal_list_head *head)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 判断链表是否仅包含一个节点
- 当链表为空时返回 0，当链表有且仅有一个节点时返回 1

**前置条件**

- head 必须已通过 [OSAL_INIT_LIST_HEAD](#OSAL_INIT_LIST_HEAD) 初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| head | const struct [osal_list_head](#osal_list_head) * | 指向链表头节点 | 不为NULL，且已初始化 |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 1 | 链表仅含一个节点 | 链表不为空且 head->next 等于 head->prev |
| 0 | 链表为空或含多个节点 | 上述条件不满足 |

### osal___list_cut_position <a id="osal___list_cut_position"></a>

```c
void osal___list_cut_position(struct osal_list_head *list, struct osal_list_head *head, struct osal_list_head *entry)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 将 head 链表从头部到 entry（含）之间的节点移动到 list 链表
- 仅供内部链表操作使用，调用者需确保 list 为空链表且 entry 在 head 链表中

**前置条件**

- 调用时序约束：list 必须为空链表或不需要保留数据的链表
- entry 必须在 head 所标识的链表中

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| list | struct [osal_list_head](#osal_list_head) * | 指向接收被切出节点的新链表头 | 不为NULL，且已初始化为空 |
| head | struct [osal_list_head](#osal_list_head) * | 指向被切割的源链表头节点 | 不为NULL，且已初始化 |
| entry | struct [osal_list_head](#osal_list_head) * | 指向切割位置节点，含此节点及之前的节点移入 list | 不为NULL，必须在 head 链表中 |

### osal_list_cut_position <a id="osal_list_cut_position"></a>

```c
void osal_list_cut_position(struct osal_list_head *list, struct osal_list_head *head, struct osal_list_head *entry)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 将 head 链表从头部到 entry（含）之间的节点切出并移入 list 链表
- 当 head 为空链表时不执行操作
- 当 head 仅含一个节点且 entry 既不是首节点也不是 head 时不执行操作
- 当 entry 等于 head 时仅将 list 初始化为空链表

**前置条件**

- list 必须为空链表或不需要保留数据的链表
- entry 必须在 head 所标识的链表中

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| list | struct [osal_list_head](#osal_list_head) * | 指向接收被切出节点的新链表头 | 不为NULL，且已初始化为空 |
| head | struct [osal_list_head](#osal_list_head) * | 指向被切割的源链表头节点 | 不为NULL，且已初始化 |
| entry | struct [osal_list_head](#osal_list_head) * | 指向切割位置节点 | 不为NULL，必须在 head 链表中或等于 head |

### osal___list_splice <a id="osal___list_splice"></a>

```c
void osal___list_splice(const struct osal_list_head *list, struct osal_list_head *prev, struct osal_list_head *next)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 将 list 链表的所有节点插入到 prev 与 next 之间
- 仅供内部链表操作使用，调用者需确保 list 不为空且 prev/next 连续

**前置条件**

- 调用时序约束：list 必须不为空，prev 和 next 必须为连续节点
- list 指向的链表会被直接修改

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| list | const struct [osal_list_head](#osal_list_head) * | 指向待拼接的源链表头节点 | 不为NULL，且链表不为空 |
| prev | struct [osal_list_head](#osal_list_head) * | 指向拼接位置的前驱节点 | 不为NULL |
| next | struct [osal_list_head](#osal_list_head) * | 指向拼接位置的后继节点 | 不为NULL |

### osal_list_splice <a id="osal_list_splice"></a>

```c
void osal_list_splice(const struct osal_list_head *list, struct osal_list_head *head)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 将 list 链表的所有节点拼接到 head 链表的头部（head 之后）
- 当 list 为空链表时不执行操作
- 拼接后 list 链表头处于未定义状态，不应再直接使用

**前置条件**

- head 必须已初始化
- list 必须已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| list | const struct [osal_list_head](#osal_list_head) * | 指向待拼接的源链表头节点 | 不为NULL，且已初始化 |
| head | struct [osal_list_head](#osal_list_head) * | 指向目标链表头节点 | 不为NULL，且已初始化 |

### osal_list_splice_tail <a id="osal_list_splice_tail"></a>

```c
void osal_list_splice_tail(struct osal_list_head *list, struct osal_list_head *head)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 将 list 链表的所有节点拼接到 head 链表的尾部（head 之前）
- 当 list 为空链表时不执行操作
- 拼接后 list 链表头处于未定义状态，不应再直接使用

**前置条件**

- head 必须已初始化
- list 必须已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| list | struct [osal_list_head](#osal_list_head) * | 指向待拼接的源链表头节点 | 不为NULL，且已初始化 |
| head | struct [osal_list_head](#osal_list_head) * | 指向目标链表头节点 | 不为NULL，且已初始化 |

### osal_list_splice_init <a id="osal_list_splice_init"></a>

```c
void osal_list_splice_init(struct osal_list_head *list, struct osal_list_head *head)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 将 list 链表的所有节点拼接到 head 链表的头部（head 之后）
- 拼接后对 list 调用 [OSAL_INIT_LIST_HEAD](#OSAL_INIT_LIST_HEAD) 重新初始化为空链表
- 当 list 为空链表时不执行操作

**前置条件**

- head 必须已初始化
- list 必须已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| list | struct [osal_list_head](#osal_list_head) * | 指向待拼接的源链表头节点 | 不为NULL，且已初始化 |
| head | struct [osal_list_head](#osal_list_head) * | 指向目标链表头节点 | 不为NULL，且已初始化 |

### osal_list_splice_tail_init <a id="osal_list_splice_tail_init"></a>

```c
void osal_list_splice_tail_init(struct osal_list_head *list, struct osal_list_head *head)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 将 list 链表的所有节点拼接到 head 链表的尾部（head 之前）
- 拼接后对 list 调用 [OSAL_INIT_LIST_HEAD](#OSAL_INIT_LIST_HEAD) 重新初始化为空链表
- 当 list 为空链表时不执行操作

**前置条件**

- head 必须已初始化
- list 必须已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| list | struct [osal_list_head](#osal_list_head) * | 指向待拼接的源链表头节点 | 不为NULL，且已初始化 |
| head | struct [osal_list_head](#osal_list_head) * | 指向目标链表头节点 | 不为NULL，且已初始化 |

### INIT_OSAL_HLIST_NODE <a id="INIT_OSAL_HLIST_NODE"></a>

```c
void INIT_OSAL_HLIST_NODE(struct osal_hlist_node *h)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 初始化哈希链表节点 h
- 将 h 的 next 指针和 pprev 指针均置为 NULL

**前置条件**

- h 指向的内存必须已分配且可写

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| h | struct [osal_hlist_node](#osal_hlist_node) * | 指向待初始化的哈希链表节点 | 不为NULL |

### osal_hlist_unhashed <a id="osal_hlist_unhashed"></a>

```c
int osal_hlist_unhashed(const struct osal_hlist_node *h)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 判断哈希链表节点 h 是否未被挂载到任何哈希链表中
- 通过检查 h->pprev 是否为 NULL 来判断

**前置条件**

- h 必须指向有效的内存地址，禁止为 NULL

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| h | const struct [osal_hlist_node](#osal_hlist_node) * | 指向待判断的哈希链表节点 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 1 | 节点未被哈希 | h->pprev 为 NULL |
| 0 | 节点已在哈希链表中 | h->pprev 不为 NULL |

### osal_hlist_empty <a id="osal_hlist_empty"></a>

```c
int osal_hlist_empty(const struct osal_hlist_head *h)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 判断哈希链表是否为空
- 通过检查 h->first 是否为 NULL 来判断

**前置条件**

- h 必须指向有效的内存地址，禁止为 NULL

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| h | const struct [osal_hlist_head](#osal_hlist_head) * | 指向哈希链表头 | 不为NULL |

**返回值**

- 返回类型：int

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 1 | 哈希链表为空 | h->first 为 NULL |
| 0 | 哈希链表不为空 | h->first 不为 NULL |

### osal___hlist_del <a id="osal___hlist_del"></a>

```c
void osal___hlist_del(struct osal_hlist_node *n)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 删除哈希链表节点 n，通过修改 pprev 和 next 指针完成
- 仅供内部链表操作使用
- 当 n->next 不为 NULL 时同步更新后继节点的 pprev 指针

**前置条件**

- n 必须在哈希链表中且 pprev 不为 NULL

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| n | struct [osal_hlist_node](#osal_hlist_node) * | 指向待删除的哈希链表节点 | 不为NULL，且已在哈希链表中 |

### osal_hlist_del <a id="osal_hlist_del"></a>

```c
void osal_hlist_del(struct osal_hlist_node *n)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 删除哈希链表节点 n
- 删除后将 n 的 next 指针置为 [OSAL_LIST_POISON1](#OSAL_LIST_POISON1)、pprev 指针置为 [OSAL_LIST_POISON2](#OSAL_LIST_POISON2)，以捕获删除后误用问题

**前置条件**

- n 必须在哈希链表中且 pprev 不为 NULL
- 删除后禁止再通过该节点进行链表操作

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| n | struct [osal_hlist_node](#osal_hlist_node) * | 指向待删除的哈希链表节点 | 不为NULL，且已在哈希链表中 |

### osal_hlist_del_init <a id="osal_hlist_del_init"></a>

```c
void osal_hlist_del_init(struct osal_hlist_node *n)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 删除哈希链表节点 n
- 当 n 未被哈希时（pprev 为 NULL）不执行操作
- 删除后调用 INIT_OSAL_HLIST_NODE 重新初始化 n，使其 next 和 pprev 均为 NULL

**前置条件**

- n 必须指向有效的内存地址

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| n | struct [osal_hlist_node](#osal_hlist_node) * | 指向待删除并重新初始化的哈希链表节点 | 不为NULL |

### osal_hlist_add_head <a id="osal_hlist_add_head"></a>

```c
void osal_hlist_add_head(struct osal_hlist_node *n, struct osal_hlist_head *h)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 将节点 n 添加到哈希链表 h 的头部
- 更新原首节点的 pprev 指针和 h->first 指针

**前置条件**

- n 指向的内存必须已分配且可写
- h 必须已初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| n | struct [osal_hlist_node](#osal_hlist_node) * | 指向待添加的哈希链表节点 | 不为NULL |
| h | struct [osal_hlist_head](#osal_hlist_head) * | 指向哈希链表头 | 不为NULL |

### osal_hlist_add_before <a id="osal_hlist_add_before"></a>

```c
void osal_hlist_add_before(struct osal_hlist_node *n, struct osal_hlist_node *next)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 将节点 n 插入到哈希链表节点 next 之前
- next 必须不为 NULL

**前置条件**

- next 必须在哈希链表中且 pprev 不为 NULL
- n 指向的内存必须已分配且可写

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| n | struct [osal_hlist_node](#osal_hlist_node) * | 指向待插入的新节点 | 不为NULL |
| next | struct [osal_hlist_node](#osal_hlist_node) * | 指向参照节点，n 插入其前 | 不为NULL |

### osal_hlist_add_after <a id="osal_hlist_add_after"></a>

```c
void osal_hlist_add_after(struct osal_hlist_node *n, struct osal_hlist_node *next)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 将节点 next 插入到哈希链表节点 n 之后
- 更新 n 的 next 指针和 next 的 pprev 指针
- 当 n 原有后继节点存在时同步更新其 pprev 指针

**前置条件**

- n 必须在哈希链表中
- next 指向的内存必须已分配且可写

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| n | struct [osal_hlist_node](#osal_hlist_node) * | 指向参照节点，next 插入其后 | 不为NULL |
| next | struct [osal_hlist_node](#osal_hlist_node) * | 指向待插入的新节点 | 不为NULL |

### osal_hlist_add_fake <a id="osal_hlist_add_fake"></a>

```c
void osal_hlist_add_fake(struct osal_hlist_node *n)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 将节点 n 的 pprev 指向自身的 next 成员地址，使其看起来已在哈希链表中
- 伪添加后 osal_hlist_del 可正常工作

**前置条件**

- n 指向的内存必须已分配且可写

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| n | struct [osal_hlist_node](#osal_hlist_node) * | 指向待伪添加的哈希链表节点 | 不为NULL |

### osal_hlist_move_list <a id="osal_hlist_move_list"></a>

```c
void osal_hlist_move_list(struct osal_hlist_head *old, struct osal_hlist_head *cur)
```

**头文件清单**

```c
#include "osal_list.h"
```

**功能说明**

- 将哈希链表从 old 头移动到 cur 头
- 更新首节点的 pprev 指针指向 cur->first
- 移动后 old->first 置为 NULL

**前置条件**

- old 和 cur 指向的内存必须已分配且可写

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| old | struct [osal_hlist_head](#osal_hlist_head) * | 指向源哈希链表头 | 不为NULL |
| cur | struct [osal_hlist_head](#osal_hlist_head) * | 指向目标哈希链表头 | 不为NULL |

## Structures

### osal_list_head <a id="osal_list_head"></a>

```c
struct osal_list_head {
    struct osal_list_head *next, *prev;
};
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| next | struct osal_list_head * | 指向链表的下一个节点 |
| prev | struct osal_list_head * | 指向链表的上一个节点 |

**使用说明**

双向链表节点结构体，用于本模块全部双向链表操作接口的入参类型。链表头节点初始化后 next 和 prev 均指向自身，形成自引用的空链表。

### osal_hlist_node <a id="osal_hlist_node"></a>

```c
struct osal_hlist_node {
    struct osal_hlist_node *next, **pprev;
};
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| next | struct osal_hlist_node * | 指向哈希链表的下一个节点 |
| pprev | struct osal_hlist_node ** | 指向前驱节点的 next 指针的地址（双指针设计便于 O(1) 删除） |

**使用说明**

哈希链表节点结构体，用于本模块全部哈希链表操作接口的入参类型。pprev 采用双指针设计，使得节点删除时无需判断是否为首节点。

### osal_hlist_head <a id="osal_hlist_head"></a>

```c
struct osal_hlist_head {
    struct osal_hlist_node *first;
};
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| first | struct osal_hlist_node * | 指向哈希链表的首个节点，为 NULL 表示空链表 |

**使用说明**

哈希链表头结构体，单指针设计节省内存空间，适用于哈希表场景。配合 osal_hlist_node 使用，first 为 NULL 表示空链表。

## Macros

### OSAL_LIST_POISON1 <a id="OSAL_LIST_POISON1"></a>

```c
#define OSAL_LIST_POISON1    0x00100100
```

### OSAL_LIST_POISON2 <a id="OSAL_LIST_POISON2"></a>

```c
#define OSAL_LIST_POISON2    0x00200200
```
