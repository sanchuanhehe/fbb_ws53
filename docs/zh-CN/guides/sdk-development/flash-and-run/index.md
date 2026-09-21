---
title: 如何烧录并验证 WS53 固件
doc_type: how-to
product: WS53
applies_to:
  sdk: 1.10.106
  target: ws53_liteos_app
  board: ws53
  host: Windows 10/11 x86_64 或 Linux x86_64
status: draft
owner: WS53 SDK Maintainers
verification_level: static
source_refs:
  - src/build/config/target_config/ws53/ws53.json
  - src/tools/pkg/chip_packet/ws53/packet.py
upstream_refs:
  - project: hs-fbb-cli
    version: "1.2.1 (master d0722a3)"
    url: https://gitcode.com/HiSpark/hs-fbb-cli
---

# 如何烧录并验证 WS53 固件

> 本页是烧录与故障恢复实践指南。第一次运行 Hello World 时，请先在[快速入门](../../../get-started/index.md)选择 CLI 或 VS Code 路径。

构建完成后，使用完整固件包烧录 WS53，再通过日志串口确认启动和当前应用的专属成功标志。

## 固件位置

以下路径相对于 WS53 SDK 的 `src` 目录：

```text
output/ws53/fwpkg/pack_all_core/ws53_liteos_app/ws53_liteos_app_all_in_one.fwpkg
```

对应 ELF 为：

```text
output/ws53/acore/ws53_liteos_app/application.elf
```

烧录前确认文件存在且时间戳对应本次构建。`_load_only.fwpkg` 只包含受限加载内容，不替代本页使用的完整固件包。

## 串口参数

| 用途 | 默认波特率 | 来源 |
| --- | --- | --- |
| 烧录串口 | `921600` | `ws53.json` 的 `flash.signalbaud` |
| 日志串口 | `115200` | `ws53.json` 的 `monitor.default_baud` |

`<PORT>` 表示开发板实际出现的端口，例如 Windows 的 `COM3` 或 Linux 的 `/dev/ttyUSB0`。烧录前关闭占用该端口的其他程序；Linux 还需确认当前用户具有串口设备访问权限。

> 烧录会覆盖开发板中的现有固件。需要保留原固件时，请先取得可恢复的固件包；失败后使用完整固件包重新烧录。

<a name="cli-flash"></a>

## 使用 CLI 烧录

在 SDK 的 `src` 目录中执行：

```console
fbb flash ws53_liteos_app --port <PORT> --baud 921600 --manual-reset
```

FBB CLI `1.2.1` 会读取 `ws53.json` 的 `upload.upload_partitions`，找到本页列出的完整固件。工具提示连接设备时，按下开发板的 `RST` 按钮。

如果 Target 查找失败但完整固件文件确实存在，可显式指定同一文件重试：

```console
fbb flash --file output/ws53/fwpkg/pack_all_core/ws53_liteos_app/ws53_liteos_app_all_in_one.fwpkg --chip ws53 --port <PORT> --baud 921600 --manual-reset
```

**预期结果：** 烧录工具以 `0` 退出，并报告 `All images burnt successfully` 或等价成功结果。

## 使用 VS Code 烧录

在 HiSpark Studio 的“工程配置”中打开“程序加载”，设置：

- 传输方式：`serial`；
- 烧写文件：本页列出的 `_all_in_one.fwpkg`；
- 端口：`<PORT>`；
- 波特率：`921600`。

开始烧录，并在出现复位提示时按下开发板的 `RST` 按钮。

**预期结果：** 插件终端报告 `All images burnt successfully`。

## 监视运行结果

CLI 用户执行：

```console
fbb monitor --chip ws53 --port <PORT> --baud 115200
```

VS Code 用户在 HiSpark Studio 中打开 `Serial` 监视器，选择同一个 `<PORT>`，并将波特率设置为 `115200`。

打开监视器后复位开发板，先检查启动日志，再检查当前 Sample 声明的专属成功标志。串口有任意输出不等于应用通过。

<a name="flash-recovery"></a>

## 无法烧录或启动时

按以下顺序处理：

1. 保留完整构建、烧录和串口日志。
2. 确认使用本次构建生成的 `_all_in_one.fwpkg`，而不是旧文件或 `_load_only.fwpkg`。
3. 确认 `<PORT>` 未被其他程序占用，开发板供电正常。
4. 重新执行完整烧录，并在提示时只按一次 `RST`。
5. 能进入系统但 Sample 没有专属成功标志时，返回 Kconfig 检查所选 Sample，不把结果判定为通过。

本页只完成源码和配置静态核对。没有对应构建日志和目标板记录时，不得把烧录或运行路径标记为已验证。
