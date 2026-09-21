---
title: 使用 VS Code 构建并运行 WS53 第一个示例
doc_type: tutorial
product: WS53
applies_to:
  sdk: 1.10.106
  branch: master
  target: ws53_liteos_app
  board: ws53
  host: Windows 10/11 x86_64
  toolchain: hcc 7.3.0-20240618
  interface: HiSpark Studio for VS Code 26.3.1（界面静态核对）
status: draft
owner: WS53 SDK Maintainers
verification_level: static
source_refs:
  - .gitattributes
  - docs/zh-CN/get-started/figures/扩展市场搜索安装HiSparkStudio.png
  - docs/zh-CN/tools/HiSparkStudioforVSCodeUserGuide/HiSparkStudioforVSCodeUserGuide.md
  - src/application/Kconfig
  - src/application/samples/Kconfig
  - src/application/samples/peripheral/Kconfig
  - src/application/samples/peripheral/helloworld/helloworld.c
  - src/build/config/target_config/ws53/menuconfig/acore/ws53_liteos_app.config
  - src/build/config/target_config/ws53/ws53.json
upstream_refs:
  - project: Visual Studio Code
    version: ">= 1.85.0"
    url: https://code.visualstudio.com/Download
  - project: Git
    version: "2.x（本页未限定最低小版本）"
    url: https://git-scm.com/downloads/
  - project: Git LFS
    version: 3.x
    url: https://git-lfs.com/
  - project: Microsoft Dev Drive
    version: Windows 11
    url: https://learn.microsoft.com/windows/dev-drive/
  - project: Windows Subsystem for Linux
    version: WSL 2
    url: https://learn.microsoft.com/windows/wsl/filesystems
---

# 使用 VS Code 构建并运行 WS53 第一个示例

本教程从安装 HiSpark Studio for VS Code 开始，沿一条图形界面路径完成环境准备、Hello World 配置、构建、烧录和串口验证。完成后，开发板会每秒输出一次 `hello world`。

本页只使用 VS Code 路径，不需要在中途切换到 CLI。本路径尚未在全新 Windows 环境实测，因此暂不承诺完成时间。

## 适用范围

| 项目 | 固定取值 |
| --- | --- |
| SDK | `1.10.106` 的 `master` 分支 |
| 主机 | Windows 10/11 x86_64 |
| 开发界面 | HiSpark Studio for VS Code `26.3.1`（界面静态核对） |
| 构建目标（Target） | 界面显示 `WS53-LITEOS-APP`，内部名称为 `ws53_liteos_app` |
| 开发板 | 项目配置中标识为 `ws53` 的 WS53 开发板 |
| Sample | `SAMPLE_SUPPORT_HELLOWORLD` |
| 完成判据 | 串口在启动标志后连续输出 `hello world` |

其他 SDK 版本、Target、主机系统或开发板不属于本教程的已声明范围。

## 前置条件

开始前确认以下 5 项：

1. 一台 Windows 10/11 x86_64 电脑，并拥有安装开发工具和串口驱动所需的权限；
2. 稳定的网络连接，以及足以保存 SDK、工具链和构建输出的磁盘空间；
3. WS53 开发板和可传输数据的 Type-C USB 线；
4. 两个互不重叠的空目录，分别保存工具链和 SDK；目录层级较浅，且路径不含中文字符或空格；
5. 已按 [Git 官方下载与安装说明](https://git-scm.com/downloads/)和 [Git LFS 官方安装说明](https://git-lfs.com/)安装 Git 和 Git LFS，且 PowerShell 中执行 `git --version`、`git lfs version` 都能显示版本。

## 操作步骤

### 步骤一：安装 VS Code 和 HiSpark Studio

1. 从 [Visual Studio Code 官方下载页](https://code.visualstudio.com/Download)安装 VS Code `1.85.0` 或更高版本。
2. 打开扩展市场（快捷键 `Ctrl+Shift+X`），搜索 `HiSpark Studio`，通过扩展页的“安装特定版本”安装 `26.3.1`。
3. 确认扩展页显示版本 `26.3.1`，再单击左侧活动栏中的 HiSpark Studio 图标。

![VS Code 扩展市场中的 HiSpark Studio](figures/扩展市场搜索安装HiSparkStudio.png)

**预期结果：** HiSpark Studio 主页能够正常打开。

**恢复入口：** 找不到插件入口或安装失败时，按[开发环境详细说明](../guides/sdk-development/environment-setup/index.md)检查 VS Code 版本、网络和扩展安装状态。

### 步骤二：准备工具链和 SDK

1. 在 PowerShell 中执行 `git lfs install`，确认命令成功。
2. 在 HiSpark Studio 主页中单击“下载工具链”。选择前置条件中为工具链准备的空目录，等待下载和安装完成。
3. 界面提示“环境准备完成”后，单击“从 HiSpark 下载 SDK”，选择 `WS53 SDK`，并将 SDK 保存到一个新的、层级较浅且不含中文字符或空格的目录。
4. 下载完成后，在 PowerShell 中进入包含 `.git` 和 `src` 的 `<sdk-root>` 目录，并执行：

    ```powershell
    git lfs pull
    $compiler = Get-Item .\src\tools\bin\compiler\riscv\cc_riscv32_musl_b010\cc_riscv32_musl_win\libexec\gcc\riscv32-linux-musl\7.3.0\cc1.exe
    if ($compiler.Length -lt 1MB) { throw "Git LFS objects are not hydrated" }
    ```

5. 在 VS Code 中打开 `<sdk-root>\src`，再打开 `build/config/target_config/ws53/target_config.py`，确认其中的 `SDK_VERSION` 为 `1.10.106`。
6. 打开“工程配置”，确认芯片为 `WS53`，Target 为 `WS53-LITEOS-APP`。

![HiSpark Studio 提示环境准备完成](figures/工具链-环境准备完成.png)

**预期结果：** Git LFS 下载完成且编译器文件不再是小于 1 MiB 的指针文件；插件识别这份未改动的 SDK；源码声明版本 `1.10.106`，工程配置中显示芯片 `WS53` 和 Target `WS53-LITEOS-APP`。

**恢复入口：** 工具链、SDK 或 Git LFS 下载失败时，不要继续构建。按[开发环境详细说明](../guides/sdk-development/environment-setup/index.md)检查 Git、Git LFS、代理、保存路径和下载失败项后重试。

### 步骤三：只启用 Hello World

1. 在 HiSpark Studio 中打开“系统配置”。
2. 进入 `Application` → `Enable Sample`。
3. 关闭默认启用的 `Enable the Sample of BT`。
4. 启用 `Enable the Sample of peripheral`。
5. 启用 `Support hello world Sample`，然后保存配置。

![在系统配置中启用 Hello World Sample](figures/配置sample-helloworld.png)

由于本教程从未改动的默认配置开始，保存后的 Sample 选择只包含 Hello World；关键配置等价于：

```text
CONFIG_SAMPLE_ENABLE=y
# CONFIG_ENABLE_BT_SAMPLE is not set
CONFIG_ENABLE_PERIPHERAL_SAMPLE=y
CONFIG_SAMPLE_SUPPORT_HELLOWORLD=y
```

**恢复入口：** 看不到 `Support hello world Sample` 时，先确认已启用 `Enable Sample` 和 `Enable the Sample of peripheral`，并确认 Target 仍为 `WS53-LITEOS-APP`。不要直接编辑生成的 `.config` 文件。

### 步骤四：构建完整固件

在 HiSpark Studio 的“命令”面板中选择“重编译”。第一次构建需要下载或解压依赖，耗时可能较长。

![在 HiSpark Studio 中重编译 Hello World](figures/编译helloworld-sample.png)

**预期结果：** 构建终端报告 `ws53_liteos_app` 构建成功，并在 SDK 的 `src` 目录下生成：

- ELF：`output/ws53/acore/ws53_liteos_app/application.elf`；
- 完整固件包：`output/ws53/fwpkg/pack_all_core/ws53_liteos_app/ws53_liteos_app_all_in_one.fwpkg`。

烧录使用 `_all_in_one.fwpkg`，不要使用 `_load_only.fwpkg` 替代完整固件包。

**恢复入口：** 构建失败时保留完整终端日志，先确认“环境准备完成”、Target 和步骤三的配置，再按[构建问题处理](../guides/sdk-development/build/index.md)排查。

### 步骤五：连接开发板并确认串口

1. 使用 Type-C USB 数据线连接开发板，确认开发板正常供电。
2. 打开 Windows“设备管理器”，展开“端口（COM 和 LPT）”，记录开发板对应的新端口，例如 `COM3`。
3. 关闭可能占用该端口的其他串口程序。

**预期结果：** 能确定一个由开发板提供、且未被其他程序占用的 COM 口。

**恢复入口：** 没有新端口时，重新插拔数据线并按[串口驱动检查](../guides/sdk-development/environment-setup/index.md#serial-driver)安装与开发板 USB 转串口芯片匹配的驱动。

### 步骤六：烧录并打开串口监视器

> 烧录会覆盖开发板中的现有固件。需要保留原固件时，请先取得可恢复的固件包；烧录失败后可使用完整固件包重试。

1. 在 HiSpark Studio 的“工程配置”中打开“程序加载”，设置：
   - 传输方式：`serial`；
   - 烧写文件：`output/ws53/fwpkg/pack_all_core/ws53_liteos_app/ws53_liteos_app_all_in_one.fwpkg`；
   - 端口：步骤五记录的 COM 口；
   - 波特率：`921600`。
2. 开始烧录；插件提示连接设备时，按下开发板的 `RST` 按钮。
3. 确认插件终端报告 `All images burnt successfully` 或等价成功结果。
4. 打开 HiSpark Studio 的“监视器”，选择 `Serial`、同一个 COM 口，并将波特率设置为 `115200`。
5. 连接监视器后，再按一次开发板的 `RST` 按钮。

**预期结果：** 烧录成功，监视器开始接收开发板复位后的启动日志。

**恢复入口：** 烧录或监视器连接失败时，关闭占用串口的程序，重新确认完整固件包、COM 口、两个步骤各自的波特率和开发板供电，再按[烧录失败恢复](../guides/sdk-development/flash-and-run/index.md#flash-recovery)处理。

### 步骤七：确认 Hello World

在串口日志中查找以下输出：

```text
start helloworld sample
hello world
hello world
```

源码每隔 1000 ms 输出一次 `hello world`。

**完成判据：** 启动标志之后至少连续观察到两行 `hello world`。只有看到这个应用专属标志，才表示本次环境准备、配置、构建、烧录和运行路径完成；仅有系统启动日志不能判定 Hello World 成功。

未出现 `hello world` 时，保留完整构建、烧录和串口日志，按[烧录与运行验证](../guides/sdk-development/flash-and-run/index.md#flash-recovery)核对 Target、固件包、配置、串口和供电。

完成观察后断开监视器，避免它继续占用串口。

## 下一步

- 阅读 `src/application/samples/peripheral/helloworld/helloworld.c`，了解本教程运行的源码。
- 按[创建应用组件](../guides/sdk-development/create-application/index.md)开始自己的应用。
- 从[参考案例](../samples/index.md)选择下一个开发任务。

### 构建较慢时

Dev Drive 和 WSL 都不是本教程的前置条件，也不会修复工具链、Kconfig 或源码错误。完成第一次构建后，如果确认耗时主要来自文件 I/O 或实时扫描，再按[构建性能说明](../guides/sdk-development/build/index.md#build-performance)选择后续方案：

- 在符合微软前置条件的 Windows 11 上继续使用原生 VS Code 流程时，可评估 Dev Drive。创建、权限和安全设置以 [Microsoft Dev Drive 官方文档](https://learn.microsoft.com/windows/dev-drive/)为准。
- 只有团队决定切换到受支持的 WSL/Linux 构建流程时，才需要评估 WSL；仓库应放在 WSL 的 Linux 文件系统，而不是 `/mnt/c`。原因和边界见 [Microsoft WSL 文件系统说明](https://learn.microsoft.com/windows/wsl/filesystems)。

Dev Drive 与 WSL 是不同主机环境下的存储选择，不作为叠加优化步骤。WSL 安装、VS Code Remote 和 USB/串口透传属于独立任务，不在本教程展开。

## 当前验证边界

本页已静态核对 Target、工具链声明、Kconfig、Hello World 源码、ELF/固件路径和串口参数。本文档变更尚未完成全新 Windows 主机安装、VS Code Smoke、干净构建或目标板 HIL 验证，因此页面保持 `draft` 和 `verification_level: static`。
