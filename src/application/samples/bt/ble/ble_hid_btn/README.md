# WS53 BLE HID Button

## 1. 一句话说明

本示例将 WS53 板载 S1 按键映射为 BLE HID 键盘按键，通过标准 HID Service 向手机或 PC 发送 8 字节键盘报告。

## 2. 适用场景

- BLE 翻页器、遥控按键、快捷键和媒体控制原型。
- 验证 WS53 GPIO 输入、BLE HID Service 和 Notification。
- 作为标准免驱 BLE 键盘外设的最小参考。

## 3. 支持能力

- 标准 HID Service `0x1812` 和 Boot Keyboard Input `0x2A22`。
- S1/MGPIO6 高电平按下、无上下拉，已与 WS53 SLE S1 映射对齐。
- 20 ms 轮询、2 次采样消抖、可选 500 ms 长按重复。
- 按键码和广播名称可由 Kconfig 配置，断线后重新广播。

## 4. 不支持/限制

- 默认只上报一个普通键码，不处理组合键或多键同时按下。
- 默认 Page Down 键码为 `0x4E`；Consumer Page 音量键不能直接当作普通 Keyboard Page 键码使用。
- 非 GPIO6 引脚走低电平有效、内部上拉的通用分支，需按实际硬件复核。
- 手机 BLE 调试工具需手动订阅 `0x2A22` CCCD 才能实时收到报告。

## 5. 关键词

### 中文关键词

WS53、BLE HID、蓝牙键盘、S1 按键、GPIO、Page Down、通知、翻页器

### English Keywords

WS53, BLE HID, keyboard, button, GPIO, Boot Keyboard Input, notification, presenter

## 6. 目录结构

```text
ble_hid_btn/
  README.md
  SDD.md
  Kconfig
  CMakeLists.txt
  inc/
    ble_hid_btn.h
    ble_hid_adv.h
  src/
    ble_hid_btn_sample.c
    ble_hid_btn.c
    ble_hid_adv.c
```

## 7. 入口文件

- 主入口：`src/ble_hid_btn_sample.c` 中的 `app_run(ble_hid_btn_sample_entry)`。
- 初始化入口：`ble_hid_btn_init()`。
- 按键业务：`hid_btn_task()`、`hid_button_handle_state()`。
- GATT 服务：`src/ble_hid_btn.c`。
- 配置入口：`Kconfig`。

## 8. 整体流程

1. 创建主任务并等待 BLE 基础环境就绪。
2. 初始化 HID GATT 服务并启动 `ble_hid_btn` 广播。
3. 创建按键任务，配置 S1 为 `S_MGPIO6`、GPIO 输入、无上下拉。
4. 周期采样并消抖；检测按下时发送键码报告，松开时发送全零报告。
5. 启用长按时，按住超过 500 ms 后额外发送一次释放/按下序列。
6. Host 断开后重新广播，等待下一次连接。

## 9. 核心文件说明

| 文件 | 作用 | 关键内容 |
|---|---|---|
| `src/ble_hid_btn_sample.c` | 入口、按键采样与任务 | GPIO6 映射、消抖、长按 |
| `src/ble_hid_btn.c` | HID GATT 服务 | Report Map、6 个 HID 特征、报告发送 |
| `src/ble_hid_adv.c` | HID 广播 | 设备名、HID UUID、Keyboard Appearance |
| `Kconfig` | 用户配置 | GPIO、键码、长按、设备名 |

## 10. 核心函数/类说明

- `ble_hid_btn_init()`：注册 GAP/GATTS 回调并创建 HID Service。
- `ble_hid_btn_send_report()`：发送 `hid_kb_report_t` 键盘输入报告。
- `hid_button_update_level()`：完成按键电平采样和两次确认消抖。
- `hid_button_handle_state()`：处理按下、松开和长按重复状态。
- `ble_hid_adv_start()`：配置并启动可连接广播。

## 11. 配置项说明

| 配置项 | 默认值 | 说明 |
|---|---:|---|
| `CONFIG_SAMPLE_SUPPORT_BLE_HID_BTN_SAMPLE` | `y` | 选择本示例 |
| `CONFIG_BLE_HID_BTN_PIN` | `6` | 逻辑 MGPIO 号；6 映射为 `S_MGPIO6`/`pin_t 32` |
| `CONFIG_BLE_HID_BTN_KEYCODE` | `78` | USB HID Usage ID，即 `0x4E` Page Down |
| `CONFIG_BLE_HID_BTN_LONGPRESS` | `y` | 启用一次长按重复 |
| `CONFIG_BLE_HID_DEVICE_NAME` | `ble_hid_btn` | 广播设备名 |

## 12. 使用方法

### 环境准备

- WS53 开发板，使用板载 S1，无需外接按键。
- 支持 BLE HID 的 PC/手机，或支持 GATT Notification 的调试工具。

### 编译

选择 `CONFIG_SAMPLE_SUPPORT_BLE_HID_BTN_SAMPLE=y` 后执行：

```powershell
fbb build ws53-liteos-app --clean -j1
```

### 运行

```powershell
fbb flash -f src/output/ws53/fwpkg/pack_all_core/ws53_liteos_app/ws53_liteos_app_all_in_one.fwpkg --chip ws53 -p COM<N> --timeout 240
fbb monitor --port COM<N> --baud 115200 --chip ws53 --reset --timeout 40
```

连接 `ble_hid_btn`；使用 GATT 工具时订阅 HID Service `0x1812` 下的 `0x2A22`。

### 运行结果

初始化成功后输出 `ready` 和 `task started, gpio=6 pin_t=32 ... active=high`。按下/松开 S1 分别输出 `press key=0x4E` 和 `release`。

## 13. 输入输出示例

### 输入

短按板载 S1。

### 输出

| 状态 | `0x2A22` 报告 |
|---|---|
| 按下 | `00 00 4E 00 00 00 00 00` |
| 松开 | `00 00 00 00 00 00 00 00` |

```text
[ble_hid_btn_sample] task started, gpio=6 pin_t=32 keycode=0x4E active=high
[ble_hid_btn_sample] press key=0x4E
[ble_hid_btn_sample] release
```
