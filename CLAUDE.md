# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

WS53V100 是海思推出的 Wi-Fi、BLE、SLE Combo 芯片，适用于物联网智能场景。本仓库是基于 FBB（Family Big Box）统一开发框架的 SDK 代码包，托管在 gitcode.com/HiSpark/fbb_ws53。

- **芯片架构**: RISC-V 32-bit (rv32imc)
- **操作系统**: Huawei LiteOS v208.5.0
- **工具链**: RISC-V 32-bit musl (`cc_riscv32_musl_b010`)
- **SDK 版本**: 1.10.106

## 构建命令

### 完整构建

```bash
cd src
python build.py ws53_liteos_app
```

常用参数：
- `-c` — clean 后编译
- `-j<N>` — 指定线程数（默认 CPU 核数）
- `-def=XXX,YYY` — 添加编译宏，`-def=-:XXX` 屏蔽宏
- `-component=XXX` — 仅编译指定组件
- `-ninja` — 使用 Ninja 生成器（默认 Unix Makefile）
- `-release` / `-debug` — release/debug 模式（默认 debug）

### 配置（Kconfig）

```bash
# 进入 menuconfig 图形配置界面
cd src
python build.py ws53_liteos_app menuconfig
```

menuconfig 配置文件路径：`src/build/config/target_config/ws53/menuconfig/acore/`

### 产物输出

- ELF: `src/output/ws53/acore/ws53-liteos-app/ws53-liteos-app.elf`
- 最终固件包: `src/output/ws53/fwpkg/ws53-liteos-app/ws53-liteos-app_all.fwpkg`

### 调试与烧录

- **调试器**: JLink 或 HiSparkLinkPro，SWD/JTAG 接口，GDB 客户端（端口 3333）
- **烧录**: 串口（默认 921600 baud）或 SWD
- **串口监控**: 115200 baud

## 架构概览

### 源码分层 (`src/`)

| 层次 | 目录 | 角色 |
|------|------|------|
| 应用层 | `application/` | 业务应用、示例代码（samples）、WS53 标准应用 |
| 协议层 | `protocol/` | BT（controller + host）、WiFi（source + ROM 固化代码） |
| 中间件 | `middleware/` | chips、services、utils |
| 内核层 | `kernel/` | LiteOS、non_os、osal/osal_adapt |
| 驱动层 | `drivers/` | chips/ws53（芯片寄存器定义）、drivers（HAL + 驱动实现） |
| 引导层 | `bootloader/` | flashboot_ws53、commonboot |

### 构建系统 (`src/build/`)

构建入口是 `src/build.py`，它调用 `build/script/cmake_builder.py` 解析 Kconfig → 生成 CMake 参数 → 调用 CMake 构建。

核心 CMake 模块在 `src/build/cmake/`：
- `build_component.cmake` — 组件编译（`build_component()` 宏是每个子目录的核心）
- `build_rom_callback.cmake` — ROM/RAM 分离编译（WS53 使用 ROM 固化代码）
- `build_sdk.cmake` — SDK 导出
- `build_sign.cmake` — 固件签名
- `build_nv_bin.cmake` / `build_partition_bin.cmake` — NV 和分区镜像生成

芯片/目标配置在 `src/build/config/target_config/ws53/`：
- `ws53.json` — 构建目标、调试、烧录配置
- `target_config.py` — target template（编译参数、组件集、defines）
- `menuconfig/acore/` — Kconfig 配置预设

### Kconfig 配置体系

顶层 `src/config.in` → 各层 Kconfig 串联：
1. 开启 `SAMPLE_ENABLE` → 选择 `ENABLE_PERIPHERAL_SAMPLE` / `ENABLE_BT_SAMPLE` / `ENABLE_WIFI_SAMPLE` / `ENABLE_PRODUCTS_SAMPLE` / `ENABLE_RADAR_SAMPLE` / `ENABLE_NFC_SAMPLE`
2. 逐层进入具体 sample 的配置项

### ROM/RAM 分离架构

WS53 使用固定 ROM + 动态 RAM 架构。ROM 中固化不变代码，应用代码编译进 RAM component。关键概念：
- `rom_component` / `ram_component` — ROM 和 RAM 侧各自的组件列表
- ROM callback 机制 — `build_rom_callback.cmake` 处理 RAM 对 ROM 函数的回调
- `fixed_rom_path` — ROM 校验基线（`libs_url/ws53/check_bin/application_rom.bin`）

### 组件编译模式

每个子目录的 `CMakeLists.txt` 通过 `build_component()` 宏定义组件：
- `SOURCES` — 源文件列表
- `PUBLIC_HEADER` — 对外暴露的头文件
- `PUBLIC_DEFINES` — 对外传递的宏
- `COMPONENT_CCFLAGS` — 组件级编译选项
- `WHOLE_LINK` — 是否全量链接（防止被 `--gc-section` 优化掉）

## 软件文档

离线文档位于 `docs/zh-CN/software/`，涵盖：SDK 开发指南、设备驱动、AT 命令、MQTT/HTTP/CoAP/CJSON、FOTA、低功耗、文件系统、安全模块、Syschannel 等。

## 参与贡献

参考社区参与贡献指南：https://gitcode.com/HiSpark/docs/blob/master/contribute/社区参与贡献指南.md
