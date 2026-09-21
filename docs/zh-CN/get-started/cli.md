---
title: 使用 CLI 构建并运行 WS53 第一个示例
doc_type: tutorial
product: WS53
applies_to:
  sdk: 1.10.106
  branch: master
  target: ws53_liteos_app
  board: ws53
  host:
    - Windows 10/11 x86_64
    - Linux x86_64
  cli: fbb 1.2.1（SDK 最低要求 1.1.0）
  toolchain: hcc 7.3.0-20240618
status: draft
owner: WS53 SDK Maintainers
verification_level: build
last_verified: 2026-09-21
source_refs:
  - .gitattributes
  - .github/scripts/get_started_cli.py
  - .github/scripts/get_started_hook.py
  - .github/workflows/docs-pages.yml
  - src/build/config/target_config/ws53/ws53.json
  - src/build/config/target_config/ws53/menuconfig/acore/ws53_liteos_app.config
  - src/application/Kconfig
  - src/application/samples/Kconfig
  - src/application/samples/peripheral/Kconfig
  - src/application/samples/peripheral/helloworld/helloworld.c
  - src/build/config/target_config/ws53/script/entry.py
  - src/tools/pkg/chip_packet/ws53/packet.py
  - src/tools/bin/compiler/riscv/cc_riscv32_musl_b010/cc_riscv32_musl/bin/riscv32-linux-musl-gcc
upstream_refs:
  - project: hs-fbb-cli
    version: "1.2.1 (master d0722a3)"
    url: https://gitcode.com/HiSpark/hs-fbb-cli
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

# 使用 CLI 构建并运行 WS53 第一个示例

本教程只使用命令行和 FBB CLI，适用于 Windows PowerShell 或 Linux Bash。平台差异只出现在命令壳层、文件检查和串口发现；Kconfig、Target、构建命令、产物、烧录参数和成功判据完全相同。

完成后，你会得到一个启用 Hello World 的 `ws53_liteos_app` 固件，将它烧录到 WS53 开发板，并从串口看到可重复验证的输出。非 HIL 命令路径已在 GitHub-hosted Ubuntu 24.04 和 Windows Server 2025 x86_64 runner 上完成干净构建；这不是 Windows 10/11 桌面安装或开发板验证，因此完整教程仍暂不承诺完成时间。

## 选择主机系统

在本页任意一组标签中选择 `Windows` 或 `Linux`，其他同名标签会自动切换到同一系统。

=== "Windows"

    使用 Windows PowerShell 执行本页命令。

=== "Linux"

    使用 Linux Bash 执行本页命令。

## 前置条件

开始前确认以下 5 项：

1. 一台 Windows 10/11 x86_64 或 Linux x86_64 电脑，并拥有安装开发工具和使用串口所需的权限；
2. 稳定的网络连接；
3. 已按 [Git 官方下载与安装说明](https://git-scm.com/downloads/)和 [Git LFS 官方安装说明](https://git-lfs.com/)安装适用于当前系统的 Git 和 Git LFS，且 `git --version`、`git lfs version` 都能显示版本；
4. 准备足以保存 SDK、工具链和构建输出的磁盘空间，以及一个较短、不含中文字符的工作目录；
5. WS53 开发板和一根可传输数据的 Type-C USB 线。

## 1. 获取 SDK

在所用系统的终端中进入工作目录，获取 SDK 和 Git LFS 文件：

<!-- get-started-cli:checkout:begin -->
<!-- get-started-cli:checkout:end -->

检查当前系统使用的编译器文件，并进入 SDK 的 `src` 目录：

<!-- get-started-cli:sdk-platform-checks:begin -->
<!-- get-started-cli:sdk-platform-checks:end -->

**预期结果：** Git LFS 下载完成且编译器文件不再是小于 1 MiB 的指针文件。Windows 的 `Test-Path` 输出 `True`；Linux 输出 `Git LFS objects: OK` 和 `SDK root: OK`。两个系统都能找到 `SDK_VERSION` 为 `1.10.106` 的源码行。

如果克隆或 LFS 下载失败，先检查网络和 Git 凭据；如果检查没有得到预期结果，不要构建，重新取得完整 SDK 后再继续。

## 2. 准备 FBB CLI 和工具链

按 [FBB CLI 项目说明](https://gitcode.com/HiSpark/hs-fbb-cli)中对应操作系统的安装方法，安装项目认可的 FBB CLI。安装后重新打开当前终端，然后执行：

<!-- get-started-cli:version:begin -->
<!-- get-started-cli:version:end -->

本教程固定验证 FBB CLI `1.2.1`；SDK 声明的 `1.1.0` 只是最低兼容版本，不表示 Nightly 覆盖了所有 `>= 1.1.0` 版本。若 `fbb -V` 未输出 `fbb 1.2.1`，请从项目认可的发布渠道取得该版本，不要绕过版本检查继续构建。

仍在 SDK 的 `src` 目录中执行：

<!-- get-started-cli:setup:begin -->
<!-- get-started-cli:setup:end -->

**预期结果：** `fbb doctor` 以 `0` 退出；`fbb describe --json` 能识别芯片 `ws53`、Target `ws53_liteos_app` 和工具链 `hcc 7.3.0-20240618`。任一检查失败时，先按命令输出修复环境，不要进入下一步。

本页已对照 FBB CLI `1.2.1`：其工具清单为 `ws53` 同时提供 `hcc 7.3.0-20240618` 的 Windows x86_64 与 Linux x86_64 包。两个系统仍必须以本步实际的 `doctor` 和 `describe` 结果为准；工具链未解析成功时停止。

## 3. 只启用 Hello World

以下 4 个操作以全新 checkout 中未修改的默认配置为起点。执行前先检查该文件没有本地改动：

<!-- get-started-cli:clean-config:begin -->
<!-- get-started-cli:clean-config:end -->

命令必须以 `0` 退出。若存在本地改动，先另行保存并恢复自己的配置，不要用本教程的命令覆盖或误判已有 Sample 配置。

确认配置文件未修改后，执行以下 4 个配置操作：

<!-- get-started-cli:configure:begin -->
<!-- get-started-cli:configure:end -->

检查配置：

<!-- get-started-cli:verify-config:begin -->
<!-- get-started-cli:verify-config:end -->

**预期结果：** 4 项依次为 `y`、`n`、`y`、`y`。如果结果不同，重新执行对应的 `set` 或 `unset` 命令；不要直接编辑生成的 `.config` 文件。

## 4. 构建固件

配置改变后执行一次干净构建：

<!-- get-started-cli:build:begin -->
<!-- get-started-cli:build:end -->

**预期结果：** 命令以 `0` 退出，并生成以下两个文件：

<!-- get-started-cli:artifacts:begin -->
<!-- get-started-cli:artifacts:end -->

按所用命令壳层检查文件：

<!-- get-started-cli:artifact-checks:begin -->
<!-- get-started-cli:artifact-checks:end -->

Windows 的两行都应输出 `True`；Linux 应输出 `ELF: OK` 和 `FWPKG: OK`。

构建失败时保留完整日志，先重新运行 `fbb doctor`，再核对 Target 和第 3 步的配置。

## 5. 连接开发板并确认串口

使用 Type-C USB 数据线连接开发板，然后按当前系统确认串口：

=== "Windows"

    1. 安装与 USB 转串口芯片匹配的驱动。
    2. 在 PowerShell 中列出串口：

        ```powershell
        [System.IO.Ports.SerialPort]::GetPortNames()
        ```

    记录新出现的端口，例如 `COM3`；下文用 `<PORT>` 表示该端口。

    **预期结果：** Windows 能稳定识别开发板串口。如果没有新端口，先更换确认支持数据传输的 USB 线或 USB 口，再检查设备管理器中的驱动状态。

=== "Linux"

    1. 确认当前用户具有访问串口设备的权限。
    2. 在 Bash 中列出串口：

        ```bash
        find /dev -maxdepth 1 -type c \( -name 'ttyUSB*' -o -name 'ttyACM*' \) -print
        ```

    记录新出现的端口，例如 `/dev/ttyUSB0`；下文用 `<PORT>` 表示该端口。

    **预期结果：** Linux 能稳定识别开发板串口。如果没有新端口，先更换确认支持数据传输的 USB 线或 USB 口，再检查内核日志和当前用户的串口权限。

## 6. 烧录完整固件

> 烧录会覆盖开发板中的现有固件。需要保留原固件时，请先取得可恢复的固件包；烧录失败后使用本次构建的完整固件包重新烧录。

关闭占用 `<PORT>` 的其他串口程序，然后在 `src` 目录执行：

```console
fbb flash ws53_liteos_app --port <PORT> --baud 921600 --manual-reset
```

FBB CLI `1.2.1` 会读取 `ws53.json` 中配置的完整固件路径。工具提示连接设备时，按下开发板的 `RST` 按钮。

**预期结果：** 烧录命令以 `0` 退出，并报告 `All images burnt successfully` 或等价成功结果。失败时按[烧录故障恢复](../guides/sdk-development/flash-and-run/index.md#flash-recovery)依次检查固件、端口、供电和复位操作。

## 7. 监视并验证 Hello World

执行：

```console
fbb monitor --chip ws53 --port <PORT> --baud 115200
```

打开监视器后按一次开发板的 `RST` 按钮。成功日志必须同时包含：

```text
start helloworld sample
hello world
hello world
```

`start helloworld sample` 表示示例任务已经启动，随后应约每秒重复输出 `hello world`。只看到系统启动日志不能判定 Hello World 成功。验证完成后按 `Ctrl+C` 退出监视器。

## 完成判据

只有以下条件全部满足，才完成本教程：

- FBB CLI、工具链和 `ws53_liteos_app` Target 通过环境检查；
- ELF 和 `_all_in_one.fwpkg` 均由本次构建生成；
- 完整固件以 `921600` 波特率烧录成功；
- 串口以 `115200` 波特率看到启动标志和重复的 `hello world`。

## 构建较慢时

构建性能优化不是首次成功的前置条件。完成上述流程后，如确认耗时主要来自文件 I/O 或实时扫描，可按[构建 How-to 的性能说明](../guides/sdk-development/build/index.md#build-performance)评估以下方案：

=== "Windows"

    - 符合微软前置条件的 Windows 11 主机进行原生构建时，可了解 [Microsoft Dev Drive](https://learn.microsoft.com/windows/dev-drive/)；
    - 仅在团队已经支持 WSL 且决定使用 Linux 工具构建时，才按 [Microsoft WSL 文件系统说明](https://learn.microsoft.com/windows/wsl/filesystems)将仓库放在 WSL 的 Linux 文件系统。

=== "Linux"

    Linux 原生构建应把仓库放在 Linux 文件系统，避免从挂载的 Windows 文件系统构建。

Dev Drive 与 WSL 不是需要叠加执行的步骤。WSL 安装、USB 和串口透传属于独立任务，本教程不展开。

## 当前验证边界

截至 2026-09-21，本页的非 HIL 路径已在 GitHub-hosted Ubuntu 24.04 和 Windows Server 2025 x86_64 runner 上通过环境检查、4 项配置切换、干净构建，以及 ELF/FWPKG 非空且为本次新生成的断言。因此页面保持 `draft`，验证等级为 `verification_level: build`。

为防止文档与自动验证漂移，SDK/FBB CLI 版本、仓库地址、Windows/Linux 编译器检查、公共命令和产物路径只在 `.github/scripts/get_started_cli.py` 中维护。MkDocs 构建时由 hook 将同一份契约注入本页，Nightly 则按相同阶段和常量执行语义等价检查；其中 checkout 使用 GitHub Actions 固定到当次提交，并另行确认文档声明的 GitCode `master` 分支可解析。静态门禁会拒绝缺失、重复或写入标记区的受管内容，构建后门禁还会核对最终 HTML 中的命令和产物。

验证没有覆盖 Windows 10/11 桌面安装、固件烧录、串口输出、Smoke 或开发板 HIL，不能据此声称 Hello World 已在目标板运行。Nightly 证据保留 14 天；上述未覆盖项继续作为 `not_run` 记录。
