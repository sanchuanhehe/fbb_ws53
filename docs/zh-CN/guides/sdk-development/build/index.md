---
title: 使用命令行配置并构建 WS53 固件
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

# 使用命令行配置并构建 WS53 固件

本文介绍通过 fbb CLI 准备构建环境、选择目标、配置 Kconfig 并生成固件的方法。首次使用图形化开发流程，请参见[快速入门](../../../get-started/index.md)。

除安装步骤外，下列命令在已配置的 SDK 工作目录中执行。独立应用工程的创建和构建入口见[创建独立应用工程](../create-project/index.md)。

<a name="cli-setup"></a>

## 环境准备

**安装 uv（Python 包管理器）**：

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

**安装或更新 fbb CLI**：

```powershell
uv tool install --force 'git+https://gitcode.com/HiSpark/hs-fbb-cli.git'
fbb -V
```

WS53 SDK 要求 `fbb` 不低于 `1.1.0`，以下命令对应 `fbb 1.2.0`。团队项目可另行固定经过验证的 CLI 提交。

**初始化构建环境并安装 SDK 与工具链**：

```bash
fbb setup
fbb sdk install ws53          # 安装匹配的 SDK 与 RISC-V 工具链
fbb doctor                    # 环境检查
fbb describe --json           # 查看 CLI、SDK、工具链和可用 target
```

> `fbb sdk install` 会下载 SDK 源码并安装该 SDK 声明的匹配工具链。团队项目应在开发说明中固定 SDK tag 或 commit；不要只执行 `git clone` 后假设本机已有匹配工具链。

## 查看可用 Target

```bash
fbb list-targets --json       # 列出所有可构建的 target
fbb describe --json            # 完整环境探测（SDK、工具链、target 等）
```

常用 target：

| Target | 用途 |
|--------|------|
| `ws53_liteos_app` | 主应用镜像（默认） |
| `ws53-flashboot` | FlashBoot 引导 |
| `ws53_liteos_xts` | LiteOS XTS 测试镜像 |

可设置默认 target 后续省略：

```bash
fbb set-target ws53_liteos_app
fbb get-target                 # 查看当前默认 target
```

## 配置 Kconfig

修改配置推荐使用 `fbb menuconfig <target>`。交互式菜单按模块层级组织，方向键移动、空格切换开关，保存退出后 `.config` 和 `mconfig.h` 自动更新：

```bash
fbb menuconfig ws53_liteos_app
```

自动化脚本和 CI 推荐使用无交互的 `fbb config`。该命令会校验 Kconfig 依赖和 choice 互斥关系：

```bash
fbb config --target ws53_liteos_app get CONFIG_SAMPLE_ENABLE
fbb config --target ws53_liteos_app set CONFIG_SAMPLE_ENABLE=y
fbb config --target ws53_liteos_app unset CONFIG_SAMPLE_ENABLE
```

<a name="cli-build"></a>

## 构建

```bash
fbb build ws53_liteos_app              # 增量构建
fbb build --clean ws53_liteos_app      # 全量重编（修改 .config 后必须 --clean）
fbb build ws53_liteos_app -j8          # 指定并行任务数
```

> 修改过 `.config` 后必须 `--clean`，否则 CMake 缓存会导致改动不生效。

构建成功需同时满足：

1. 进程退出码为 `0`
2. `src/output/ws53/fwpkg/<target>/<target>_all.fwpkg` 存在且时间戳更新
3. 使用 `_all.fwpkg`，不要使用 `_load_only.fwpkg`

## 下一步

构建完成后，按[烧录与运行验证](../flash-and-run/index.md)烧录固件并确认应用运行。构建失败时，先运行 `fbb doctor` 检查环境，并核对所选 Target 与 Kconfig 配置。
