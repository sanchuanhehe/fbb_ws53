# 创建应用

WS53 的应用入口和案例都在 `src/application/`。推荐从现有 Sample 复制组件结构，再通过 Kconfig 控制是否编译；这样可以复用 SDK 的 CMake、日志和打包流程。

## 目录约定

- 外设：`src/application/samples/peripheral/<case>/`
- BLE/SLE：`src/application/samples/bt/ble/`、`src/application/samples/bt/sle/`、`src/application/samples/bt/sle_chba/`
- Wi-Fi：`src/application/samples/wifi/<case>/`
- 应用初始化：`src/application/ws53/ws53_application/`

每个组件通常包含 `CMakeLists.txt`、`Kconfig`、头文件和一个或多个 `.c` 文件。先阅读同类别案例的 CMake 写法，再加入新源文件。

## 添加一个最小案例

1. 复制最接近的案例目录并修改组件名、日志标签和源文件。
2. 在本目录 `Kconfig` 声明一个 `SAMPLE_SUPPORT_*` 开关；若有角色、引脚或参数，也在这里声明默认值和范围。
3. 在上级 `CMakeLists.txt` 使用 `if(CONFIG_...)` 引入该子目录，避免未启用时参与编译。
4. 在 `app_run` 或案例注册表中按现有模式注册入口；入口中完成驱动初始化、错误处理和任务创建，不要在系统启动早期执行阻塞操作。
5. 运行 `python build.py ws53_liteos_app menuconfig`，确认新选项可见并保存配置。

## 构建与调试

```powershell
cd <SDK根目录>\src
python build.py ws53_liteos_app -c -j1
```

先在日志串口验证初始化，再使用 J-Link/HiSparkLinkPro 通过 SWD/JTAG 调试。发布前确认 ELF、map 和 `.fwpkg` 均来自同一份配置。

## 相关页面

- [快速开始](quick-start.md)
- [烧录与运行](flash-and-run.md)
- [外设驱动](../samples/peripherals/index.md)
- [整体架构](../overall-architecture/index.md)
- [SDK 开发](../guides/sdk-development/index.md)
