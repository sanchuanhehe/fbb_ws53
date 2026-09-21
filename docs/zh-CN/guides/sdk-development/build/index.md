---
title: 使用命令行配置并构建 WS53 固件
doc_type: how-to
product: WS53
applies_to:
  sdk: 1.10.106
  target: ws53_liteos_app
  host: Windows 10/11 x86_64 或 Linux x86_64
  cli: fbb >= 1.1.0（本页静态核对 1.2.1）
status: draft
owner: WS53 SDK Maintainers
verification_level: static
source_refs:
  - src/build/config/target_config/ws53/config.py
  - src/build/config/target_config/ws53/ws53.json
  - src/build/config/target_config/ws53/menuconfig/acore/ws53_liteos_app.config
  - src/tools/bin/compiler/riscv/cc_riscv32_musl_b010/cc_riscv32_musl/bin/riscv32-linux-musl-gcc
upstream_refs:
  - project: hs-fbb-cli
    version: "1.2.1 (master d0722a3)"
    url: https://gitcode.com/HiSpark/hs-fbb-cli
  - project: Microsoft Dev Drive
    version: Windows 11
    url: https://learn.microsoft.com/windows/dev-drive/
  - project: Windows Subsystem for Linux
    version: WSL 2
    url: https://learn.microsoft.com/windows/wsl/filesystems
---

# 使用命令行配置并构建 WS53 固件

本文介绍如何使用 FBB CLI 检查环境、配置 Kconfig 并构建 WS53 固件。第一次运行 Hello World 时，请从[CLI 快速入门](../../../get-started/cli.md)进入。

除安装和更新 CLI 外，以下命令均在 WS53 SDK 的 `src` 目录中执行。

<a name="cli-setup"></a>

## 准备命令行环境

1. 按 [FBB CLI 项目说明](https://gitcode.com/HiSpark/hs-fbb-cli)安装或更新 `fbb`。
2. 在 PowerShell 或 Bash 中检查版本：

    ```console
    fbb -V
    ```

    `src/build/config/target_config/ws53/ws53.json` 要求 `fbb >= 1.1.0`。版本低于 `1.1.0` 时停止操作，从项目认可的发布渠道取得兼容版本；不要忽略版本检查继续构建。

3. 进入 SDK 的 `src` 目录。`<sdk-root>` 表示 SDK 根目录：

    ```powershell
    cd <sdk-root>\src
    ```

    Linux Bash 使用：

    ```bash
    cd <sdk-root>/src
    ```

4. 准备工具链并检查环境：

    ```console
    fbb setup --sdk-dir .
    fbb doctor
    fbb describe --json
    ```

环境就绪需同时满足：

- `fbb doctor` 以 `0` 退出；
- `fbb describe --json` 识别到芯片 `ws53`；
- 工具链版本为 SDK 声明的 `hcc 7.3.0-20240618`；
- 当前目录包含 `build.py`。

任一检查失败时先修复环境，不要进入配置或构建步骤。

## 查看 Target

```console
fbb list-targets --json
```

本页固定使用 `ws53_liteos_app`。其他 Target 的用途和验证状态不从本页推断。

<a name="configure-kconfig"></a>

## 配置 Kconfig

交互配置使用：

```console
fbb menuconfig ws53_liteos_app
```

脚本化配置使用 `get`、`set` 和 `unset`。以下示例假设目标配置仍是仓库的未修改默认值；复用已有工作目录时，先保存自己的配置，不要据此推断其他 Sample 已关闭。

```console
fbb config set CONFIG_SAMPLE_ENABLE=y --target ws53_liteos_app
fbb config unset CONFIG_ENABLE_BT_SAMPLE --target ws53_liteos_app
fbb config set CONFIG_ENABLE_PERIPHERAL_SAMPLE=y --target ws53_liteos_app
fbb config set CONFIG_SAMPLE_SUPPORT_HELLOWORLD=y --target ws53_liteos_app
```

检查结果：

```console
fbb config get CONFIG_SAMPLE_ENABLE --target ws53_liteos_app
fbb config get CONFIG_ENABLE_BT_SAMPLE --target ws53_liteos_app
fbb config get CONFIG_ENABLE_PERIPHERAL_SAMPLE --target ws53_liteos_app
fbb config get CONFIG_SAMPLE_SUPPORT_HELLOWORLD --target ws53_liteos_app
```

预期依次输出 `y`、`n`、`y`、`y`。配置写入 `build/config/target_config/ws53/menuconfig/acore/ws53_liteos_app.config`；不要直接编辑该生成文件。

<a name="cli-build"></a>

## 构建

修改 Kconfig 后执行干净构建：

```console
fbb build --clean ws53_liteos_app
```

未修改配置时可执行增量构建：

```console
fbb build ws53_liteos_app
```

构建成功需同时满足：

1. 进程退出码为 `0`；
2. `output/ws53/acore/ws53_liteos_app/application.elf` 存在且时间戳更新；
3. `output/ws53/fwpkg/pack_all_core/ws53_liteos_app/ws53_liteos_app_all_in_one.fwpkg` 存在且时间戳更新。

完整烧录使用 `_all_in_one.fwpkg`，不要把 `_load_only.fwpkg` 当作完整固件包。

FBB CLI `1.2.1` 会读取 `ws53.json` 的 `upload.upload_partitions`，按 Target 找到上述完整固件。烧录命令和显式文件路径的恢复方式见[烧录与运行验证](../flash-and-run/index.md#cli-flash)。

<a name="build-performance"></a>

## 构建较慢时

存储位置优化只处理文件 I/O 或实时扫描带来的耗时，不会修复 CLI 版本、工具链、Kconfig 或源码错误。先完成一次正确构建并记录用时，再选择与实际主机环境匹配的方案。

### Windows 原生构建

在符合微软前置条件的 Windows 11 上使用原生 CLI 或 VS Code 构建时，可评估将源码、构建输出和可再生成的缓存放到 Dev Drive。创建 Dev Drive 会涉及磁盘空间、格式化、权限和安全策略，本仓库不复制这些通用步骤；请按 [Microsoft Dev Drive 官方文档](https://learn.microsoft.com/windows/dev-drive/)检查前置条件和风险。

企业设备还应遵循组织的 Defender 和存储策略。不要为了构建速度在快速入门中关闭安全软件或添加未经评审的全目录排除。

### WSL 中使用 Linux 工具构建

WSL 不是快速入门的前置条件。如果团队已经支持 WSL，并决定在 WSL 中使用 Linux 工具构建，请将仓库放在 WSL 的 Linux 文件系统（例如 `~/projects`），不要放在 `/mnt/c` 后跨文件系统反复访问。原因和路径建议见 [Microsoft WSL 文件系统说明](https://learn.microsoft.com/windows/wsl/filesystems)。

Dev Drive 面向 Windows 原生开发负载；WSL 构建应遵循 WSL 文件系统建议，两者不作为叠加优化步骤。WSL 的安装、VS Code Remote、USB 和串口透传属于独立任务，不在本页展开。

## 下一步

构建完成后，按[烧录与运行验证](../flash-and-run/index.md)烧录完整固件并检查应用专属成功标志。构建失败时保留完整日志，先运行 `fbb doctor`，再核对 CLI 版本、Target 和 Kconfig。
