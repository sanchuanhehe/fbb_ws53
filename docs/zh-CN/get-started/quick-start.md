---
title: 构建并运行 WS53 第一个示例
doc_type: tutorial
product: WS53
applies_to:
  sdk: 1.10.106
  target: ws53_liteos_app
  board: ws53
  toolchain: cc_riscv32_musl_fp_win (hcc 7.3.0-20240618)
status: draft
verification_level: static
source_refs:
  - src/application/samples/peripheral/helloworld/
  - src/application/samples/peripheral/Kconfig
  - src/build/config/target_config/ws53/ws53.json
---

# 构建并运行 WS53 第一个示例

本教程引导没有 WS53 开发经验的用户，在约 30 分钟内完成一个可观察的 Hello World 结果：串口每秒输出一行 `hello world`。

## 适用范围

本教程固定使用以下组合：

| 项目 | 取值 |
| --- | --- |
| 产品/芯片界面选项 | `WS53` |
| 构建目标（Target） | `ws53_liteos_app` |
| 开发板 | 项目配置中标识为 `ws53` 的 WS53 开发板 |
| 工具 | HiSpark Studio for VS Code |
| 示例配置 | `Application` → `Enable Sample` → `Enable the Sample of peripheral` → `Support hello world Sample` |
| 烧录方式 | `serial` |

开发板或工具链不符合上述组合时，请先完成[环境搭建](../guides/sdk-development/environment-setup/index.md)，不要在本教程中自行切换配置。本教程固定使用构建目标 `ws53_liteos_app`。

## 前置条件

每项条件都必须在开始前检查：

1. VS Code 已安装，且左侧活动栏能打开 HiSpark Studio。
2. WS53 SDK 已下载，工程配置可以指向 SDK 的 `src` 目录。
3. 工具链准备已完成，HiSpark Studio 不再提示环境缺失。
4. WS53 开发板已通过 Type-C USB 数据线连接电脑并正常供电。
5. 设备管理器中已出现开发板对应的串口。

## 操作步骤

### 步骤一：创建工程

1. 打开 HiSpark Studio，在“欢迎使用”页面单击“新建工程”。
2. 按以下值填写工程配置：芯片选择 `WS53`，工程类型选择“示例工程”，软件包选择已下载 SDK 的 `src` 目录，工程名和工程路径使用不含中文且层级较浅的路径。
3. 单击“完成”。如果出现文件夹信任提示，确认信任当前工程。

![HiSpark Studio 欢迎页面中的新建工程入口](figures/点击新建工程.png)

**预期结果：** HiSpark Studio 打开新工程，并显示工程文件和命令面板。

**恢复入口：** 如果工程未打开，关闭当前窗口后重新从 HiSpark Studio 的“新建工程”进入；仍无法创建时，返回[环境搭建](../guides/sdk-development/environment-setup/index.md)检查 SDK 路径。

### 步骤二：选择固定示例配置

1. 在命令面板中打开“系统配置”。
2. 依次进入 `Application` → `Enable Sample` → `Enable the Sample of peripheral`，启用 `Support hello world Sample`。
3. 保存配置，并确认配置文件路径以 `build/config/target_config/ws53/menuconfig/acore/ws53_liteos_app.config` 结尾。

![HiSpark Studio 中选择 Hello World 示例配置的页面](figures/配置sample-helloworld.png)

**预期结果：** 配置文件已生成，且只启用了本教程的 Hello World 示例。

**恢复入口：** 如果配置路径或示例名称不一致，关闭配置窗口后重新打开“系统配置”，不要继续编译未知配置。

### 步骤三：编译工程

单击命令面板中的“编译”，等待终端完成构建。

![HiSpark Studio 命令面板中的 Hello World 编译操作](figures/编译helloworld-sample.png)

**预期结果：** 终端显示 `SUCCESS`，并生成与当前配置对应的 ELF 和 `.fwpkg` 构建产物。

**恢复入口：** 如果编译失败，保留终端日志，先返回步骤二确认只启用了 Hello World，再参见[开发环境搭建详解](../guides/sdk-development/environment-setup/manual/index.md#ZH-CN_TOPIC_0000001777394010)中的编译排查内容。

### 步骤四：确认串口

1. 打开 Windows“设备管理器”。
2. 确认开发板上电，并记录新出现的实际 COM 口。

![Windows 设备管理器中显示开发板串口的页面](figures/设备管理器-新设备端口.png)

**预期结果：** 设备管理器显示开发板串口，后续烧录和监视使用同一个 COM 口。

**恢复入口：** 如果没有新串口，重新插拔数据线并检查驱动；仍无法识别时，返回[环境搭建](../guides/sdk-development/environment-setup/index.md#serial-driver)中的串口驱动检查。

### 步骤五：烧录固件

1. 在命令面板中打开“工程配置”，进入“程序加载”。
2. 将传输方式设置为 `serial`，选择步骤三生成的完整 `.fwpkg`，填入步骤四记录的 COM 口，波特率设置为 `921600`。
3. 单击“烧录”。当终端提示按下复位键时，按开发板上的 `RST` 按钮。

![HiSpark Studio 工程配置中的烧录入口](figures/sample-helloworld-工程配置.png)

![HiSpark Studio 提示按下开发板复位键的烧录页面](figures/烧录-复位提示.png)

**预期结果：** 终端显示 `All images burnt successfully`。

**恢复入口：** 如果烧录失败，关闭占用 COM 口的终端，确认使用步骤三生成的 `.fwpkg` 和步骤四记录的 COM 口后重新执行本步骤；仍失败时参见[烧录与运行](../guides/sdk-development/flash-and-run/index.md#flash-recovery)。

### 步骤六：打开串口监视器

1. 在命令面板中打开“命令行”，再选择“监视器”。
2. 监视模式选择 `Serial`，选择烧录时使用的 COM 口，波特率设置为 `115200`，单击“开始监视”。

![HiSpark Studio 中打开串口监视器的页面](figures/监视器-连接串口.png)

**预期结果：** 监视器开始接收开发板复位后的日志。

**恢复入口：** 如果监视器无法打开，关闭其他串口工具并确认 COM 口未被占用，然后重新打开监视器。

### 步骤七：验证 Hello World 输出

观察串口日志，确认每秒出现一行：

```text
hello world
```

![串口监视器中每秒输出 hello world 的日志](figures/监视器-串口输出.png)

**完成判据：** 连续观察到 `hello world` 输出，表示本教程的构建、烧录和运行路径完成。

**恢复入口：** 如果没有出现该标记，保留完整串口日志和烧录输出，参见[烧录与运行](../guides/sdk-development/flash-and-run/index.md#flash-recovery)检查固件、构建目标、串口和供电状态。

## 下一步

- 了解源码入口：`src/application/samples/peripheral/helloworld/`。
- 查询其他可运行案例：参见[参考案例](../samples/index.md)。
- 使用命令行、menuconfig 或创建自定义应用：参见[开发环境搭建详解](../guides/sdk-development/environment-setup/manual/index.md)和[创建应用](../guides/sdk-development/create-application/index.md)。

本教程当前只完成文档和源码静态核对；目标板端到端验证完成后，再将页面状态更新为 `verified`。
