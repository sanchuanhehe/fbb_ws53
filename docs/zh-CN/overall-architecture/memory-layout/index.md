---
title: Flash 与 RAM
doc_type: explanation
product: WS53
applies_to:
  sdk: 1.10.106
  target: ws53_liteos_app
status: draft
verification_level: static
source_refs:
  - src/build/config/target_config/ws53/param_sector/param_sector.json
  - src/build/config/target_config/ws53/
  - src/drivers/boards/ws53/linker/ws53_app_linker/
---

# Flash 与 RAM

> WS53 芯片的 Flash 分区方案与 RAM (Random Access Memory) 内存分配

---

## Flash 分区布局

分区表定义在 `build/config/target_config/ws53/param_sector/param_sector.json`。Flash 基址为 `0x400000`，分区表覆盖 4 MiB（`0x400000`～`0x7FFFFF`）。以下地址均为片内 Flash 绝对地址。

```text
0x400000 ┌──────────────────────────────┐
         │ Root public key  2 KiB       │ ID 0x03
0x402000 ├──────────────────────────────┤
         │ SSB             24 KiB       │ ID 0x00
0x408000 ├──────────────────────────────┤
         │ Customer factory 16 KiB      │ ID 0x08
0x40C000 ├──────────────────────────────┤
         │ NV Backup       16 KiB       │ ID 0x09
0x410000 ├──────────────────────────────┤
         │ FlashBoot backup 64 KiB      │ ID 0x02
0x420000 ├──────────────────────────────┤
         │ FlashBoot       64 KiB       │ ID 0x01
0x430000 ├──────────────────────────────┤
         │ Ccore_imageA                 │ ID 0x20, 2.25 MiB
0x45D000 │ ┌ Acore_imageA               │ ID 0x21，与 ID 0x20 重叠
         │ │                            │
0x670000 ├─┴────────────────────────────┤
         │ Acore_imageB / FOTA data     │ ID 0x22
0x7F3000 ├──────────────────────────────┤
         │ Customer reserve 28 KiB      │ ID 0x30
0x7FA000 ├──────────────────────────────┤
         │ Crash info       8 KiB       │ ID 0x11
0x7FC000 ├──────────────────────────────┤
         │ NV DATA         16 KiB       │ ID 0x10
0x800000 └──────────────────────────────┘
```

| 分区 ID | 分区名称 | 绝对地址 | 大小 | 说明 |
|---------|----------|----------|------|------|
| 0x03 | Root public key | `0x400000` | 2 KiB | 安全启动根公钥；其后保留 6 KiB 间隙 |
| 0x00 | SSB (Secure Secondary Boot) | `0x402000` | 24 KiB | 二级安全引导 |
| 0x08 | Customer factory | `0x408000` | 16 KiB | 客户出厂配置 |
| 0x09 | NV (Non-Volatile) Backup | `0x40C000` | 16 KiB | NV 数据备份 |
| 0x02 | FlashBoot backup | `0x410000` | 64 KiB | FlashBoot 备份区 |
| 0x01 | FlashBoot | `0x420000` | 64 KiB | 引导程序 |
| 0x20 | Ccore_imageA | `0x430000` | 2.25 MiB | JSON 定义的 Ccore_imageA 分区 |
| 0x21 | Acore_imageA | `0x45D000` | 2124 KiB | 地址范围包含在 ID 0x20 内 |
| 0x22 | Acore_imageB / FOTA data | `0x670000` | 1548 KiB | 升级数据区，具体用途由升级配置决定 |
| 0x30 | rsv0 for customer | `0x7F3000` | 28 KiB | 客户预留区 |
| 0x11 | Crash info | `0x7FA000` | 8 KiB | 死机信息保存区 |
| 0x10 | NV DATA | `0x7FC000` | 16 KiB | 非易失性数据存储 |

> ID `0x20` 的地址范围为 `0x430000`～`0x66FFFF`，ID `0x21` 的地址范围为 `0x45D000`～`0x66FFFF`，两者存在重叠，容量不能直接相加。

---

## RAM 内存分配

以下数值取自当前 `src/output/ws53/acore/ws53_liteos_app/application.map`。不同 Kconfig、SDK 版本和业务组件会改变实际占用，调试时应以本次构建生成的 `.map` 为准。

### RAM 总体布局

| 地址范围 | 分配大小 | 当前使用情况 | 区域内容 |
|----------|----------|--------------|----------|
| `0x00019C00`～`0x0001FFFF` | 25 KiB | ROM 固定区域 | Acore ROM 符号和固化代码 |
| `0x00020000`～`0x0002FFFF` | 64 KiB | 当前使用到 `0x0002F8CB`，剩余 1844 B | App ITCM (Instruction Tightly Coupled Memory) 代码 |
| `0x20010000`～`0x2005FFFF` | 320 KiB | 固定段使用 34288 B，系统堆 293392 B | App DTCM (Data Tightly Coupled Memory) 数据、固定栈和 LiteOS 堆 |
| `0x20060000`～`0x20063FFF` | 16 KiB | 平台共享区 | Acore 与 Ccore 共享内存 |
| `0x20067F00`～`0x20067FFF` | 256 B | `.preserve` 使用 252 B | 复位或异常流程保留的诊断数据 |
| `0x52006000`～`0x520067F3` | 2036 B | `.cputrace_mem` 使用 2028 B | CPU Trace 缓冲区 |

### App DTCM 详细分配

| 起始地址 | 大小 | 链接段或区域 | 说明 |
|----------|------|--------------|------|
| `0x20010000` | 2 KiB | `.stacks` | 启动及固定栈区域 |
| `0x20010800` | 184 B | `.plt_sramdata` | 平台 SRAM 初始化数据 |
| `0x200108C0` | 1064 B | `.plt_flashdata` | 平台 Flash 初始化数据 |
| `0x200111A0` | 440 B | `.bth_flashdata` | 蓝牙 Host 初始化数据 |
| `0x20011358` | 572 B | `.data` | 普通初始化数据 |
| `0x20011598` | 924 B | `.plt_srambss` | 平台零初始化数据 |
| `0x20011938` | 24829 B | `.wifi_flashbss` | Wi-Fi 相关零初始化数据 |
| `0x20017A38` | 3000 B | `.bss` | 普通 BSS 数据 |
| `0x200185F0` | 293392 B | LiteOS 系统堆 | 任务栈、OSAL 动态对象和运行时缓冲区从此申请 |

### 任务栈与动态缓冲区

普通 LiteOS 任务栈没有固定链接地址，由系统堆在运行时分配。`g_app_tasks[]` 中平台任务的栈申请大小如下；任务是否存在取决于对应编译条件。

| 任务 | 栈申请大小 | 编译条件 |
|------|------------|----------|
| `app` | 2 KiB（`0x800`） | 始终创建 |
| `app_sample` | 2 KiB（`0x800`） | `CONFIG_SAMPLE_ENABLE` |
| `log` | 2 KiB（`0x800`） | 非设备模式且使用非压缩日志 |
| `cmd_loop` | 4 KiB（`0x1000`） | `TEST_SUITE` |
| `bt_sdk` | 2 KiB（`0x800`） | `BTH_TASK_EXIST` 与 `BTH_SDK_TASK_SUPPORT` |
| `bt_service` | 2.5 KiB（`0xA00`） | `BTH_TASK_EXIST` |
| `at` | 4 KiB（`0x1000`） | `AT_COMMAND` |
| `wifi` | 8 KiB（`0x2000`） | `CONFIG_SUPPORT_WIFI` |
| `ohos_start` | 4 KiB（`0x1000`） | `CONFIG_SUPPORT_OHOS_SUPPORT` |

LiteOS 内核任务、工作队列和中间件自行创建的任务也会占用系统堆。`CONFIG_MCU_MODE_2`、`CONFIG_MCU_MODE_3`、`CONFIG_MCU_MODE_4`、设备模式和诊断模式等配置还会改变内存边界，因此不能把链接时的堆容量视为业务可全部使用的空闲 RAM。

## 参考

- [构建系统](../build-system/index.md) — 构建产物与固件包位置
- [启动流程](../boot-flow/index.md) — 各启动阶段对镜像和内存的使用
