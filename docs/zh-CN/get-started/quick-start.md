# 快速开始

在仓库根目录执行：

```bash
cd src
python build.py ws53_liteos_app
```

需要重新生成全部中间产物时添加 `-c`，需要限制并发时添加 `-j<N>`。构建成功后检查 `src/output/ws53/fwpkg/ws53-liteos-app/ws53-liteos-app_all.fwpkg`。
