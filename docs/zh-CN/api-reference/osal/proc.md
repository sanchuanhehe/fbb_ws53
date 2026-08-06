# proc

proc 提供 /proc 文件系统的目录与文件管理能力，支持创建、删除 proc 目录与文件，并通过顺序写接口向 proc 文件输出内容，供用户空间读取模块的调试与状态信息。

**头文件清单**

```c
#include "proc/osal_proc.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [osal_proc_init](#osal_proc_init) | 在 /proc 目录下创建指定名称的目录 |
| [osal_proc_exit](#osal_proc_exit) | 删除由 osal_proc_init 创建的 proc 目录及其下所有文件 |
| [osal_remove_proc_entry](#osal_remove_proc_entry) | 删除由 osal_create_proc_entry 创建的 proc 文件 |
| [osal_create_proc_entry](#osal_create_proc_entry) | 在 osal_proc_init 创建的 proc 目录下创建 proc 文件 |
| [osal_seq_printf](#osal_seq_printf) | 在 read 回调期间向 proc 文件顺序写入格式化内容 |

## Functions

### osal_proc_init <a id="osal_proc_init"></a>

```c
void osal_proc_init(const char *name)
```

**头文件清单**

```c
#include "proc/osal_proc.h"
```

**功能说明**

- 在 /proc 目录下创建指定名称的目录
- 作为后续 osal_create_proc_entry 创建 proc 文件的前置入口
- 同一时刻仅允许存在一个由本接口创建的 proc 目录

**前置条件**

- 调用时序约束：当前接口应在调用 osal_create_proc_entry、osal_remove_proc_entry 之前调用
- 调用限制：当前接口仅可调用一次，重复调用时不会再创建新目录

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| name | const char * | 待创建的 proc 目录名称 | 字符串长度 < [OSAL_PROC_NAME_LENGTH](#OSAL_PROC_NAME_LENGTH)(32) |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| LOSCFG_FS_PROC | 编译参与宏 | 控制 osal_proc.c 参与编译 | 由构建目标决定 |

### osal_proc_exit <a id="osal_proc_exit"></a>

```c
void osal_proc_exit(const char *name)
```

**头文件清单**

```c
#include "proc/osal_proc.h"
```

**功能说明**

- 删除由 osal_proc_init 创建的 proc 目录及其下的所有文件
- 与 osal_proc_init 配对使用，用于清理 proc 模块资源
- 删除后 proc 目录及其文件不再可访问

**前置条件**

- 调用时序约束：当前接口应在 osal_proc_init 成功执行后调用
- 依赖关系：当前接口依赖 osal_proc_init 已创建 proc 目录

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| name | const char * | 待删除的 proc 目录名称，应为 osal_proc_init 时传入的名称 | 非NULL |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| LOSCFG_FS_PROC | 编译参与宏 | 控制 osal_proc.c 参与编译 | 由构建目标决定 |

### osal_remove_proc_entry <a id="osal_remove_proc_entry"></a>

```c
void osal_remove_proc_entry(const char *name, osal_proc_entry *parent)
```

**头文件清单**

```c
#include "proc/osal_proc.h"
```

**功能说明**

- 删除由 osal_create_proc_entry 创建的 proc 文件
- 通过文件名定位并移除对应的 proc 条目
- 与 osal_create_proc_entry 配对使用

**前置条件**

- 调用时序约束：当前接口应在 osal_create_proc_entry 成功创建 proc 文件后调用
- 依赖关系：当前接口依赖 osal_proc_init 已成功执行

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| name | const char * | 待删除的 proc 文件名称，应与 osal_create_proc_entry 时传入的名称一致 | 非NULL |
| parent | [osal_proc_entry](#osal_proc_entry) * | 由 osal_create_proc_entry 返回的 proc 条目指针 | 非NULL |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| LOSCFG_FS_PROC | 编译参与宏 | 控制 osal_proc.c 参与编译 | 由构建目标决定 |

### osal_create_proc_entry <a id="osal_create_proc_entry"></a>

```c
osal_proc_entry *osal_create_proc_entry(const char *name, osal_proc_entry *parent)
```

**头文件清单**

```c
#include "proc/osal_proc.h"
```

**功能说明**

- 在 osal_proc_init 创建的 proc 目录下创建指定名称的 proc 文件
- 返回 osal_proc_entry 指针，供调用方设置 read/write/open 回调与命令列表
- 创建的 proc 文件可通过 osal_remove_proc_entry 删除

**前置条件**

- 调用时序约束：当前接口应在 osal_proc_init 成功执行后调用
- 依赖关系：当前接口依赖 osal_proc_init 已创建 proc 目录

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| name | const char * | 待创建的 proc 文件名称 | 字符串长度 < [OSAL_PROC_NAME_LENGTH](#OSAL_PROC_NAME_LENGTH)(32) |
| parent | [osal_proc_entry](#osal_proc_entry) * | 保留参数，当前未使用 | 无约束（保留参数，当前未使用） |

**返回值**

- 返回类型：osal_proc_entry *

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| 非NULL | 创建成功，返回 proc 文件条目指针 | proc 文件创建成功 |
| NULL | 创建失败 | proc 目录未初始化或 proc 文件创建失败 |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| LOSCFG_FS_PROC | 编译参与宏 | 控制 osal_proc.c 参与编译 | 由构建目标决定 |

### osal_seq_printf <a id="osal_seq_printf"></a>

```c
void osal_seq_printf(void *seqfile, const char *fmt, ...)
```

**头文件清单**

```c
#include "proc/osal_proc.h"
```

**功能说明**

- 在 proc 文件的 read 回调执行期间，向 seqfile 顺序写入格式化内容
- 写入的内容作为 proc 文件的读取输出返回给用户空间
- 支持可变参数格式化输出

**前置条件**

- 调用时序约束：当前接口应在 proc 文件的 read 回调执行期间调用，seqfile 取自回调入参 entry 的 seqfile 字段
- 依赖关系：当前接口依赖 osal_create_proc_entry 已成功创建 proc 文件并设置了 read 回调

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| seqfile | void * | 顺序文件指针，取自 read 回调入参 entry 的 seqfile 字段 | 非NULL |
| fmt | const char * | 格式化字符串，与可变参数一一对应 | 非NULL |
| ... | 可变参数 | 与 fmt 中的格式说明符一一对应的可变参数 | - |

**Kconfig配置**

| 配置项 | 宏类型 | 说明 | 默认值 |
| -------- | -------- | -------- | -------- |
| LOSCFG_FS_PROC | 编译参与宏 | 控制 osal_proc.c 参与编译 | 由构建目标决定 |

## Structures

### osal_proc_cmd <a id="osal_proc_cmd"></a>

```c
typedef struct osal_proc_cmd_ {
    char name[OSAL_PROC_NAME_LENGTH];
    int (*handler)(unsigned int argc, char (*argv)[PROC_CMD_SINGEL_LENGTH_MAX], void *private_data);
} osal_proc_cmd;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| name | char[OSAL_PROC_NAME_LENGTH] | 命令名称字符串 |
| handler | int (*)(unsigned int, char (*)[PROC_CMD_SINGEL_LENGTH_MAX], void *) | 命令处理函数指针，被调用时传入参数个数 argc、参数字符串数组 argv 与私有数据 private_data |

### osal_proc_entry <a id="osal_proc_entry"></a>

```c
typedef struct osal_proc_dir_entry {
    char name[OSAL_PROC_NAME_LENGTH];
    unsigned int cmd_cnt;
    osal_proc_cmd *cmd_list;
    void *proc_dir_entry;
    int (*open)(struct osal_proc_dir_entry *entry);
    int (*read)(struct osal_proc_dir_entry *entry);
    int (*write)(struct osal_proc_dir_entry *entry, const char *buf, int count, long long *);
    void *private_data;
    void *seqfile;
    struct osal_list_head node;
} osal_proc_entry;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| name | char[OSAL_PROC_NAME_LENGTH] | proc 文件名称字符串 |
| cmd_cnt | unsigned int | 命令列表中的命令数量 |
| cmd_list | [osal_proc_cmd](#osal_proc_cmd) * | 命令列表指针，指向 osal_proc_cmd 数组 |
| proc_dir_entry | void * | proc 目录项指针 |
| open | int (*)(struct osal_proc_dir_entry *) | 文件打开回调函数指针 |
| read | int (*)(struct osal_proc_dir_entry *) | 文件读取回调函数指针 |
| write | int (*)(struct osal_proc_dir_entry *, const char *, int, long long *) | 文件写入回调函数指针 |
| private_data | void * | 调用方私有数据指针，在回调中透传 |
| seqfile | void * | 顺序文件指针，在 read 回调中传给 osal_seq_printf |
| node | struct osal_list_head | 链表节点，用于模块内部管理 |

## Macros

### OSAL_PROC_NAME_LENGTH <a id="OSAL_PROC_NAME_LENGTH"></a>

```c
#define OSAL_PROC_NAME_LENGTH 32
```
