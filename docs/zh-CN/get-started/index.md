---
title: 快速入门
doc_type: tutorial
product: WS53
applies_to:
  sdk: 1.10.106
  target: ws53_liteos_app
status: draft
verification_level: not-applicable
source_refs:
  - docs/zh-CN/get-started/quick-start.md
  - src/build/config/target_config/ws53/ws53.json
---

# 快速入门

本入口面向第一次使用 WS53 SDK 的开发者。沿本文完成一个固定的 Hello World 路径，即可创建工程、构建固件、烧录开发板并在串口看到运行结果。

## 默认路径

1. [配置开发环境](../guides/sdk-development/environment-setup/index.md)，获取 WS53 SDK 和开发板。
2. 按[快速开始](quick-start.md)创建并配置 Hello World 工程。
3. 编译、烧录并确认串口输出 `hello world`。

该路径预先选择 WS53、`ws53_liteos_app` 构建目标（Target）、HiSpark Studio for VS Code 和 `SAMPLE_SUPPORT_HELLOWORLD` 配置，不要求在首次成功前选择其他开发板、构建目标或示例。

## 前置条件

开始前请确认：

- 已安装 VS Code 和 HiSpark Studio for VS Code 插件。
- 已获取 WS53 SDK，并完成工具链准备。
- 已准备 WS53 开发板、Type-C USB 数据线和对应串口驱动。
- 开发板连接后能在设备管理器中看到串口。

前置条件无法满足时，请按[环境搭建](../guides/sdk-development/environment-setup/index.md)完成检查。该页面包含完整安装步骤，属于默认路径之外的实践指南。

## 完成后继续

- 需要详细烧录参数或失败恢复时，参见[烧录与运行](../guides/sdk-development/flash-and-run/index.md)。
- 需要使用命令行、menuconfig 或自定义应用时，参见[开发环境搭建详解](../guides/sdk-development/environment-setup/manual/index.md)和[创建应用](../guides/sdk-development/create-application/index.md)。
- 需要查询其他案例时，参见[参考案例](../samples/index.md)。
