---
title: 如何创建 WS53 应用组件
doc_type: how-to
product: WS53
applies_to:
  sdk: 1.10.106
  target: ws53_liteos_app
status: draft
verification_level: static
source_refs:
  - src/application/
  - src/application/samples/CMakeLists.txt
  - src/application/samples/peripheral/CMakeLists.txt
  - src/application/samples/peripheral/helloworld/CMakeLists.txt
  - src/drivers/drivers/driver/gpio/CMakeLists.txt
  - src/build/cmake/build_component.cmake
  - src/build/config/target_config/ws53/ws53.json
---

# 如何创建 WS53 应用组件

> 本页面是应用开发实践指南，不属于默认快速入门路径。首次开发请先从[快速入门](../../../get-started/index.md)完成 Hello World。

WS53 的应用入口和案例都在 `src/application/`。推荐从现有 Sample 复制组件结构，再通过 Kconfig 控制是否编译；这样可以复用 SDK 的 CMake、日志和打包流程。

## 目录约定

- 外设：`src/application/samples/peripheral/<case>/`
- BLE/SLE：`src/application/samples/bt/ble/`、`src/application/samples/bt/sle/`、`src/application/samples/bt/sle_chba/`
- Wi-Fi：`src/application/samples/wifi/<case>/`
- 应用初始化：`src/application/ws53/ws53_application/`

应用案例通常包含源码和 `CMakeLists.txt`，按需要提供头文件；Kconfig 可以位于案例目录或上层目录。先阅读同类别案例的构建写法，再加入新源文件。

<a name="component-examples"></a>

## 目录与 CMake 示例

先按现有源码判断目录是向上层汇总源码，还是独立声明构建组件，再选择对应写法。组件的组成和边界见[组件模型](../../../overall-architecture/build-system/index.md#component-model)。

### 应用案例：向上层汇总源码

当前 Hello World 案例的目录为：

```text
src/application/samples/peripheral/helloworld/
├── helloworld.c
└── CMakeLists.txt
```

它的 `CMakeLists.txt` 将源码追加到父作用域：

```cmake
set(SOURCES "${SOURCES}" "${CMAKE_CURRENT_SOURCE_DIR}/helloworld.c" PARENT_SCOPE)
```

上层 `peripheral/CMakeLists.txt` 按 Kconfig 选择是否纳入该目录：

```cmake
if(DEFINED CONFIG_SAMPLE_SUPPORT_HELLOWORLD)
    add_subdirectory_if_exist(helloworld)
endif()
```

源码最终汇总到 `samples` 组件。复制此类案例时，修改源文件名和对应配置开关，并保留向上层传递 `SOURCES` 的方式；Kconfig 开关可以定义在上层目录，不要求每个案例目录单独包含 Kconfig。

<a name="cmake-template"></a>

### 独立构建组件：完整 CMake 模板

以 SDK 中的 GPIO 驱动组件为例：

```text
src/drivers/drivers/driver/gpio/
├── gpio.c
└── CMakeLists.txt
```

以下保留 GPIO 组件的完整字段声明。空的 `set(...)` 表示该组件没有为此字段配置额外内容，创建自己的组件时按需填写。

```cmake
set(COMPONENT_NAME "gpio")

set(SOURCES
    ${CMAKE_CURRENT_SOURCE_DIR}/gpio.c
)

set(PUBLIC_HEADER
)

set(PRIVATE_HEADER
)

set(PRIVATE_DEFINES
)

set(PUBLIC_DEFINES
    SUPPORT_GPIO
)

set(COMPONENT_PUBLIC_CCFLAGS
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

各字段及构建调用的含义如下：

| 字段或调用 | 作用 | 修改时关注的内容 |
| --- | --- | --- |
| `COMPONENT_NAME` | 标识独立构建组件 | 使用自己的组件名，并与目标配置中的注册名称一致 |
| `SOURCES` | 指定参与编译的源文件 | 添加实际 `.c` 文件路径；`${CMAKE_CURRENT_SOURCE_DIR}` 表示当前 CMake 文件所在目录 |
| `PUBLIC_HEADER` | 对外提供头文件搜索目录 | 填写供其他组件使用的接口头文件目录 |
| `PRIVATE_HEADER` | 指定组件私有头文件搜索目录 | 填写仅供当前组件实现使用的目录 |
| `PRIVATE_DEFINES` | 设置组件内部编译宏 | 放置不需要向其他组件传递的宏 |
| `PUBLIC_DEFINES` | 设置对外传递的编译宏 | 仅保留接口或依赖方确实需要的宏；`SUPPORT_GPIO` 是 GPIO 示例的设置 |
| `COMPONENT_PUBLIC_CCFLAGS` | 设置对外传递的编译选项 | 按组件接口的实际要求配置 |
| `COMPONENT_CCFLAGS` | 设置组件自身的编译选项 | 放置当前组件需要的编译参数 |
| `WHOLE_LINK` | 控制组件是否按全量链接方式参与链接 | 是否设为 `true` 应依据组件的链接需求决定 |
| `MAIN_COMPONENT` | 标记是否为主组件 | 本例 GPIO 为普通组件，因此设为 `false` |
| `build_component()` | 将上述声明交给 SDK 构建框架处理 | 在组件属性声明完成后调用 |

这里展示的是 GPIO 的独立组件模板，不是要求每个应用案例都新增一次 `build_component()` 调用。对于前述 Hello World 类型的案例，继续使用向上层汇总源码的方式。需要新增独立组件并注册到目标时，参见[新增 SDK 组件](../add-component/index.md)。

## 添加一个最小案例

1. 复制最接近的案例目录并修改组件名、日志标签和源文件。
2. 在本目录或上层 `Kconfig` 声明一个 `SAMPLE_SUPPORT_*` 开关；若有角色、引脚或参数，也在这里声明默认值和范围。
3. 在上级 `CMakeLists.txt` 使用 `if(CONFIG_...)` 引入该子目录，避免未启用时参与编译。
4. 在 `app_run` 或案例注册表中按现有模式注册入口；入口中完成驱动初始化、错误处理和任务创建，不要在系统启动早期执行阻塞操作。
5. 运行 `python build.py ws53_liteos_app menuconfig`，确认新选项可见并保存配置。

**预期结果：** 新组件目录、Kconfig 开关和构建入口均已注册，且 menuconfig 中可以看到新选项。

**恢复入口：** 如果新选项未出现，先检查上级 `Kconfig` 和 `CMakeLists.txt` 的条件是否与宏名称一致，再使用[快速入门](../../../get-started/quick-start.md)确认基础构建环境正常。

## 构建与调试

```powershell
cd <SDK根目录>\src
python build.py ws53_liteos_app -c -j1
```

先在日志串口验证初始化，再使用 J-Link/HiSparkLinkPro 通过 SWD/JTAG 调试。发布前确认 ELF、map 和 `.fwpkg` 均来自同一份配置。

## 相关页面

- [快速开始](../../../get-started/quick-start.md)
- [烧录与运行](../flash-and-run/index.md)
- [外设驱动](../../../samples/peripherals/index.md)
- [整体架构](../../../overall-architecture/index.md)
- [SDK 开发](../index.md)
