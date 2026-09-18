---
title: 如何烧录并验证 WS53 固件
doc_type: how-to
product: WS53
applies_to:
  sdk: 1.10.106
  target: ws53_liteos_app
  board: ws53
status: draft
verification_level: static
source_refs:
  - src/build/config/target_config/ws53/ws53.json
---

# 如何烧录并验证 WS53 固件

> 本页面是默认快速入门路径之外的烧录实践指南。首次开发请先从[快速入门](../../../get-started/index.md)进入唯一默认成功路径。

构建完成后使用完整固件包烧录 WS53，再通过日志串口确认启动和案例运行。

## 固件位置

默认目标 `ws53_liteos_app` 的完整固件包为：

```text
src/output/ws53/fwpkg/ws53-liteos-app/ws53-liteos-app_all.fwpkg
```

ELF 位于 `src/output/ws53/acore/ws53-liteos-app/ws53-liteos-app.elf`，用于符号化调试和问题定位；同目录下的 `.map` 文件用于分析内存和符号布局。

## 串口参数

| 用途 | 默认波特率 | 说明 |
| --- | --- | --- |
| 烧录串口 | 921600 | 由烧录工具使用 |
| 日志/控制台 | 115200 | 复位后观察启动和案例日志 |

烧录前确认开发板型号、USB 驱动、端口号和供电状态；若板卡有独立下载键，按板卡说明进入下载模式。

## 操作步骤

1. 关闭占用串口的其他终端，连接 USB 数据线。
2. 在 HiSpark Studio 中选择 WS53，并指向上述 `.fwpkg`。
3. 以 921600 开始烧录；失败时降低速率或重新插拔 USB 后重试。
4. 烧录完成后复位开发板，立即打开 115200 日志串口。
5. 检查 `boot.`、`APP|dbg uart init ok.`、`device_module_init::succ!` 和 `cpu 0 entering scheduler` 等启动标志，再观察案例专属日志。

<a name="cli-flash"></a>

## 使用 fbb CLI 烧录

先按[命令行配置与构建](../build/index.md)完成环境准备和固件构建，关闭占用串口的终端，然后在同一 SDK 工作目录执行：

```bash
fbb flash ws53_liteos_app                                 # 自动检测串口
fbb flash ws53_liteos_app --port COM3 --baud 921600       # 指定串口和波特率
```

烧录完成后复位开发板，以 115200 波特率打开日志串口，并按下文检查运行结果。

## 运行验收

- 启动验证：确认串口出现本页“操作步骤”中列出的启动标志。
- 应用验证：按当前 Sample 文档声明的成功判据观察日志、数据或外部信号。
- 不将“串口有输出”单独作为通过依据；缺少 Sample 专属成功标志时，应标记为未完成验证。

<a name="flash-recovery"></a>

## 无法启动时

保留完整启动日志和烧录工具输出；先恢复默认 Kconfig，仅启用一个案例。若日志停在 boot 阶段，优先检查固件包、下载模式和供电；若能进入调度器但案例失败，检查案例角色、引脚和外部设备。
