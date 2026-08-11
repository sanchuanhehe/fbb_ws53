# 整体架构

WS53 SDK 基于 FBB 统一开发框架，运行于 RISC-V 32 位处理器和 Huawei LiteOS。代码按应用、协议、中间件、内核、驱动和引导层组织，构建系统负责 Kconfig 配置、组件编译、ROM/RAM 分离和固件打包。

- [源码结构](source-tree/index.md)
- [构建系统](build-system/index.md)
