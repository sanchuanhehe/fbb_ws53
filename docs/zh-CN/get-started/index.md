---
title: 选择 WS53 开发方式
doc_type: tutorial
product: WS53
applies_to:
  sdk: 1.10.106
  branch: master
  target: ws53_liteos_app
  host: Windows 10/11 x86_64 或 Linux x86_64
status: draft
owner: WS53 SDK Maintainers
verification_level: static
source_refs:
  - src/build/config/target_config/ws53/target_config.py
  - src/build/config/target_config/ws53/ws53.json
---

# 选择 WS53 开发方式

这是 Get Started 的入口。环境准备、配置、构建、烧录和运行验证都属于 Get Started；你只需要在这里选择一次操作方式，随后沿对应页面完成一条不再分支的 Hello World 路径。

CLI 和 HiSpark Studio for VS Code 使用相同的 SDK、Target、Kconfig、工具链版本、固件格式和完成判据。两条路径都以串口持续输出 `hello world` 为首次成功标志。

## 适用范围

| 项目 | 固定取值 |
| --- | --- |
| SDK | `1.10.106` 的 `master` 分支 |
| CLI 主机 | Windows 10/11 x86_64 或 Linux x86_64 |
| VS Code 主机 | Windows 10/11 x86_64 |
| Target | `ws53_liteos_app` |
| 开发板 | 项目配置中标识为 `ws53` 的 WS53 开发板 |
| Sample | `SAMPLE_SUPPORT_HELLOWORLD` |

## 只选择一个页面

| 你的工作方式 | 进入页面 |
| --- | --- |
| 希望在 Windows PowerShell 或 Linux Shell 中使用命令，并与 CI 对齐 | [使用 CLI 完成第一次开发](cli.md) |
| 希望使用图形界面配置、构建、烧录和监视 | [使用 VS Code 完成第一次开发](vscode.md) |

两个页面都是完整教程，均从各自的环境搭建开始。完成当前所选页面前，不要切换到另一页面，也不需要同时配置两套环境。

## 当前验证边界

本入口已静态核对 SDK 版本、Target 和两条路径的共同边界。CLI 与 VS Code 页面仍需分别取得干净环境 Smoke、构建日志和目标板 HIL 记录，因此当前保持 `draft` 和 `verification_level: static`。
