# Partition

partition 提供分区管理功能，支持分区管理模块的初始化与分区信息查询。分区信息支持按内存地址和文件系统路径两种存储方式进行获取。

**模块公共头文件**

```c
#include "include/middleware/utils/partition.h"
```

## 接口清单

| 接口名称 | 功能简述 |
| -------- | -------- |
| [uapi_partition_init](#uapi_partition_init) | 初始化分区管理模块 |
| [uapi_partition_get_info](#uapi_partition_get_info) | 获取指定ID对应的分区信息 |

## Functions

### uapi_partition_init <a id="uapi_partition_init"></a>

```c
errcode_t uapi_partition_init(void)
```

**声明头文件**

```c
#include "include/middleware/utils/partition.h"
```

**功能说明**

- 初始化分区管理模块，为后续分区信息查询做准备
- 校验分区镜像标识的有效性
- 加载并解析分区表配置信息

**前置条件**

- 调用时序约束：当前接口为分区模块初始化接口，须在 uapi_partition_get_info 之前调用
- 依赖关系：当前接口依赖分区存储区域已就绪且可被访问

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x0 | 执行成功 | 分区镜像标识校验通过且分区表加载完成 |
| Other | 其他错误码 | 分区镜像标识不匹配或分区数量不足 |

**参考案例**

- `src/application/ws53/ws53_application/main.c`
- `src/bootloader/flashboot_ws53/startup/main.c`

### uapi_partition_get_info <a id="uapi_partition_get_info"></a>

```c
errcode_t uapi_partition_get_info(partition_ids_t partition_id, partition_information_t *info)
```

**声明头文件**

```c
#include "include/middleware/utils/partition.h"
```

**功能说明**

- 获取指定ID对应的分区信息
- 支持按内存地址方式查询分区信息
- 支持按文件系统路径方式查询分区信息

**前置条件**

- 调用时序约束：当前接口必须在 uapi_partition_init 成功返回后调用
- 依赖关系：当前接口依赖分区模块已完成初始化

**入参**

| 名称 | 参数类型 | 说明 | 约束取值范围 |
| ---- | ---- | ---- | ---- |
| partition_id | [partition_ids_t](#enum_partition_ids_t) | 指定的分区的ID | [PARTITION_SSB](#enum_partition_ids_t)(0x0) / [PARTITION_FLASH_BOOT_IMAGE](#enum_partition_ids_t)(0x1) / [PARTITION_FLASH_BOOT_IMAGE_BACKUP](#enum_partition_ids_t)(0x2) / [PARTITION_FLASH_ROOT_PUBLIC_KEYS_AREA](#enum_partition_ids_t)(0x3) / [PARTITION_CUSTOMER_FACTORY](#enum_partition_ids_t)(0x8) / [PARTITION_NV_DATA_BACKUP](#enum_partition_ids_t)(0x9) / [PARTITION_NV_DATA](#enum_partition_ids_t)(0x10) / [PARTITION_CRASH_INFO](#enum_partition_ids_t)(0x11) / [PARTITION_CCPU_IMAGE](#enum_partition_ids_t)(0x20) / [PARTITION_APP_IMAGE](#enum_partition_ids_t)(0x21) / [PARTITION_FOTA_DATA](#enum_partition_ids_t)(0x22) / [PARTITION_CCPU_IMAGE_BACKUP](#enum_partition_ids_t)(0x23) / [PARTITION_RESERVE2](#enum_partition_ids_t)(0x30) / [PARTITION_RESERVE3](#enum_partition_ids_t)(0x31) / [PARTITION_RESERVE4](#enum_partition_ids_t)(0x32) / [PARTITION_RESERVE5](#enum_partition_ids_t)(0x33) / [PARTITION_MAX_CNT](#enum_partition_ids_t)(16) |

**出参**

| 名称 | 数据类型 | 输出说明 |
| ---- | ---- | ---- |
| info | [partition_information_t](#struct_partition_information_t) * | 用来保存获取到的分区信息，由调用方分配内存、函数填充 |

**返回值**

- 返回类型：errcode_t

| 返回值 | 文字含义 | 触发场景 |
| -------- | -------- | -------- |
| ERRCODE_SUCC:0x0 | 执行成功 | 成功获取分区信息 |
| Other | 其他错误码 | info指针为NULL或指定分区配置未找到 |

**参考案例**

- `src/bootloader/flashboot_ws53/startup/main.c`
- `src/middleware/utils/at/at_plt_cmd/at/at_plt.c`
- `src/middleware/utils/nv/nv_storage_lib/nv_update.c`
- `src/middleware/utils/update/common/upg_common.c`

## Type definitions

### errcode_t <a id="typedef_errcode_t"></a>

```c
typedef uint32_t errcode_t;
```

**使用说明**

本模块对外接口的返回值类型。[SDK公共基础类型]

## Associations

### union_part_info <a id="union_part_info"></a>

```c
union {
    struct {
        uint32_t addr; /*!< @if Eng Address of partition if partition stored on an memory address.
                            @else   如果分区存储在内存地址上，addr存储分区的起始地址 @endif */
        uint32_t size; /*!< @if Eng Byte length of partition if partition stored on flash or ram.
                            @else   如果分区存储在内存地址上，size存储分区的字节长度 @endif */
    } addr_info;       /*!< @if Eng The address info of the partition.
                            @else   分区的地址信息 @endif */
    char *file_path;   /*!< @if Eng File path if image partition on filesystem.
                            @else   如果分区存在文件系统上，file_path标识存储分区所在路径 @endif */
} part_info;
```

| 成员名称 | 类型 | 描述 | 接口使用逻辑 |
| ------- | ---- | ---- | ----------- |
| addr_info | struct | 分区的地址信息，包含起始地址(addr)和字节长度(size) | 接口出参载体 |
| file_path | char * | 如果分区存在文件系统上，file_path标识存储分区所在路径 | 接口出参载体 |

## Enumerations

### partition_type_t <a id="enum_partition_type_t"></a>

```c
typedef enum partition_type {
    PARTITION_BY_ADDRESS,  /*!< @if Eng Partition stored on an memory address.
                                  @else   分区存储在内存地址上 @endif */
    PARTITION_BY_PATH,     /*!< @if Eng Partition stored on filesystem.
                                  @else   分区存储在文件系统上 @endif */
    PARTITION_TYPE_COUNT   /*!< @if Eng type count, not a valid type.
                                  @else   类型数量，不作为类型使用 @endif */
} partition_type_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| PARTITION_BY_ADDRESS | 0 | 分区存储在内存地址上 |
| PARTITION_BY_PATH | 1 | 分区存储在文件系统上 |
| PARTITION_TYPE_COUNT | 2 | 类型数量，不作为类型使用 |

### partition_ids_t <a id="enum_partition_ids_t"></a>

```c
typedef enum {
    PARTITION_SSB = 0x0,
    PARTITION_FLASH_BOOT_IMAGE = 0x1,
    PARTITION_FLASH_BOOT_IMAGE_BACKUP = 0x2,
    PARTITION_FLASH_ROOT_PUBLIC_KEYS_AREA = 0x3,

    PARTITION_CUSTOMER_FACTORY = 0x8,
    PARTITION_NV_DATA_BACKUP = 0x9,
    PARTITION_NV_DATA = 0x10,
    PARTITION_CRASH_INFO = 0x11,

    PARTITION_CCPU_IMAGE = 0x20,
    PARTITION_APP_IMAGE = 0x21,
    PARTITION_FOTA_DATA = 0x22,
    PARTITION_CCPU_IMAGE_BACKUP = 0x23,

    PARTITION_RESERVE2 = 0x30,
    PARTITION_RESERVE3 = 0x31,
    PARTITION_RESERVE4 = 0x32,
    PARTITION_RESERVE5 = 0x33,

    PARTITION_MAX_CNT = 16 /*!< @if Eng Maximum number of partitions.
        The value is recorded only as the number of partitions and is not used to determine the ID validity.
                                @else   分区的数量，这个枚举只用来记录分区的数量，不作为分区ID有效性的判断 @endif */
} partition_ids_t;
```

| 枚举成员 | 取值 | 描述 |
| ------- | ---- | ---- |
| PARTITION_SSB | 0x0 | SSB分区ID |
| PARTITION_FLASH_BOOT_IMAGE | 0x1 | Flash启动镜像分区ID |
| PARTITION_FLASH_BOOT_IMAGE_BACKUP | 0x2 | Flash启动镜像备份分区ID |
| PARTITION_FLASH_ROOT_PUBLIC_KEYS_AREA | 0x3 | Flash根公钥区域分区ID |
| PARTITION_CUSTOMER_FACTORY | 0x8 | 客户出厂分区ID |
| PARTITION_NV_DATA_BACKUP | 0x9 | NV数据备份分区ID |
| PARTITION_NV_DATA | 0x10 | NV数据分区ID |
| PARTITION_CRASH_INFO | 0x11 | 崩溃信息分区ID |
| PARTITION_CCPU_IMAGE | 0x20 | CCPU镜像分区ID |
| PARTITION_APP_IMAGE | 0x21 | 应用镜像分区ID |
| PARTITION_FOTA_DATA | 0x22 | FOTA数据分区ID |
| PARTITION_CCPU_IMAGE_BACKUP | 0x23 | CCPU镜像备份分区ID |
| PARTITION_RESERVE2 | 0x30 | 保留分区2 |
| PARTITION_RESERVE3 | 0x31 | 保留分区3 |
| PARTITION_RESERVE4 | 0x32 | 保留分区4 |
| PARTITION_RESERVE5 | 0x33 | 保留分区5 |
| PARTITION_MAX_CNT | 16 | 分区的数量，只用来记录分区的数量，不作为分区ID有效性的判断 |

## Structures

### partition_information_t <a id="struct_partition_information_t"></a>

```c
typedef struct partition_information {
    partition_type_t type; /*!< @if Eng Partition storage location type.
                                  @else   分区存储位置类型 @endif */
    union {
        struct {
            uint32_t addr; /*!< @if Eng Address of partition if partition stored on an memory address.
                                @else   如果分区存储在内存地址上，addr存储分区的起始地址 @endif */
            uint32_t size; /*!< @if Eng Byte length of partition if partition stored on flash or ram.
                                @else   如果分区存储在内存地址上，size存储分区的字节长度 @endif */
        } addr_info;       /*!< @if Eng The address info of the partition.
                                @else   分区的地址信息 @endif */
        char *file_path;   /*!< @if Eng File path if image partition on filesystem.
                                @else   如果分区存在文件系统上，file_path标识存储分区所在路径 @endif */
    } part_info;           /*!< @if Eng the union of partition information(address or file path).
                                @else   保存分区信息（地址或文件路径）的共同体 @endif */
} partition_information_t;
```

**成员说明**

| 成员名称 | 数据类型 | 描述 |
| ------- | ------- | ---- |
| type | [partition_type_t](#enum_partition_type_t) | 分区存储位置类型 |
| part_info | union | 保存分区信息（地址或文件路径）的共同体 |

## Macros

### ERRCODE_SUCC <a id="ERRCODE_SUCC"></a> [SDK公共共享宏]

```c
#define ERRCODE_SUCC                                        0UL
```
