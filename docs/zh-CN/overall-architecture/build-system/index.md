# 构建系统

构建入口为 `src/build.py`。脚本读取目标和 Kconfig 配置，生成 CMake 参数并完成组件编译、链接、签名与固件打包。

```bash
cd src
python build.py ws53_liteos_app
```

ELF 输出到 `src/output/ws53/acore/ws53-liteos-app/ws53-liteos-app.elf`，固件包输出到 `src/output/ws53/fwpkg/ws53-liteos-app/ws53-liteos-app_all.fwpkg`。
