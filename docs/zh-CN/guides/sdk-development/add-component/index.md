---
title: 向 WS53 SDK 新增组件
doc_type: how-to
product: WS53
applies_to:
  sdk: 1.10.106
  target: ws53_liteos_app
status: draft
verification_level: static
source_refs:
  - src/build/config/target_config/ws53/config.py
  - src/build/config/target_config/ws53/ws53.json
---

# 向 WS53 SDK 新增组件

开始前，请完成[构建环境准备](../build/index.md#cli-setup)。下文源码目录相对于 SDK 的 `src/`，目标配置文件为 `src/build/config/target_config/ws53/config.py`；构建命令在已配置的 SDK 工作目录中执行。

> 本节面向维护 SDK 平台组件的开发者。普通产品业务优先在[独立应用工程](../create-project/index.md)的 `main/` 或 `components/` 中扩展，不要为了增加业务功能直接修改 SDK 的 `config.py`。

向 SDK 中添加一个新的软件模块时，按以下步骤操作。以新增 `my_driver` 组件为例：

**第一步：创建源码和 CMakeLists.txt**

```
drivers/drivers/driver/my_driver/
├── my_driver.c
└── CMakeLists.txt
```

```cmake
set(COMPONENT_NAME "my_driver")

set(SOURCES
    ${CMAKE_CURRENT_SOURCE_DIR}/my_driver.c
)

set(PUBLIC_HEADER
)

set(PRIVATE_HEADER
)

set(PRIVATE_DEFINES
)

set(PUBLIC_DEFINES
)

set(COMPONENT_CCFLAGS
)

set(WHOLE_LINK
    true
)

set(MAIN_COMPONENT
    false
)

build_component()
```

模板中各字段含义：

| 字段 | 必填 | 说明 |
|------|:---:|------|
| COMPONENT_NAME | 是 | 组件名，需与 config.py 中注册的名称一致 |
| SOURCES | 是 | 源文件列表，使用 `${CMAKE_CURRENT_SOURCE_DIR}` 拼接路径 |
| PUBLIC_HEADER | 否 | 公开头文件，暴露给其他组件使用 |
| PRIVATE_HEADER | 否 | 私有头文件，仅本组件内部使用 |
| PRIVATE_DEFINES | 否 | 组件内部宏定义，不对外暴露 |
| PUBLIC_DEFINES | 否 | 公开宏定义，其他组件依赖本组件时自动继承 |
| COMPONENT_PUBLIC_CCFLAGS | 否 | 公开编译选项，其他组件依赖本组件时自动追加 |
| COMPONENT_CCFLAGS | 否 | 组件私有编译选项，仅本组件使用 |
| WHOLE_LINK | 否 | 是否全量链接，true 表示即使未被引用也保留所有符号 |
| MAIN_COMPONENT | 否 | 是否为主组件，每个 target 有且仅有一个 |

**第二步：注册到目标 target**

在 config.py 的 ram_component 列表中添加组件名：

```python
'ws53_liteos_app': {
    'ram_component': [
        # ... 已有组件 ...
        'my_driver',         # 新增
    ],
}
```

**第三步（可选）：添加 Kconfig 开关**

如果组件需要可配置，在对应目录下新建或编辑 Kconfig：

```kconfig
config MY_DRIVER_ENABLE
    bool "Enable My Driver"
    default y
```

源码中使用方式：

```c
#ifdef CONFIG_MY_DRIVER_ENABLE
    /* 初始化 */
    my_driver_init();
    /* 创建任务 */
    osal_kthread_lock();
    osal_task *task = osal_kthread_create((osal_kthread_handler)my_driver_task,
                                           0, "MyDriver", 0x1000);
    if (task != NULL) {
        osal_kthread_set_priority(task, 26);
        osal_kfree(task);
    }
    osal_kthread_unlock();
#endif
```

**第四步：重新构建**

```bash
fbb build ws53_liteos_app
```

## 检查结果

确认构建日志包含新组件且编译正常结束。使用可选 Kconfig 开关时，检查菜单中可以找到该选项；若未出现，检查上级 Kconfig 是否已引用相应文件。运行结果按组件自身的成功判据验证。
