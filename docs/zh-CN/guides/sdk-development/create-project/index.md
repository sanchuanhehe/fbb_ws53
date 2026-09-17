---
title: 创建 WS53 独立应用工程
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

# 创建 WS53 独立应用工程

本文介绍创建 SDK 目录之外的产品应用工程。开始前，先按[命令行配置与构建](../build/index.md#cli-setup)准备 fbb CLI、SDK 和工具链。

在用于保存应用工程的父目录中执行以下命令。

产品应用使用 SDK 外的独立工程，不直接修改 `application/ws53/ws53_application/main.c`。升级后的 fbb CLI (Command Line Interface) 提供工程脚手架：

```bash
fbb create-project my_ws53_app --chip ws53
cd my_ws53_app
fbb build
```

生成的工程包含：

```text
my_ws53_app/
├── fbb-project.toml        # 芯片、target 和依赖
├── CMakeLists.txt          # 外置工程构建入口
└── main/
    ├── CMakeLists.txt
    └── app.c               # app_run() 业务入口
```

业务可以继续拆分到 `components/`。外置工程通过 `FBB_SDK_DIR` 接入 SDK 组件树，应用代码与 SDK 源码分开管理。

## 检查结果

确认工程目录包含上述文件，且 `fbb build` 正常结束。随后按[烧录与运行验证](../flash-and-run/index.md)检查生成固件的运行结果。
