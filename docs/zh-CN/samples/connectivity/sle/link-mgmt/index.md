---
hide:
  - toc
---

# 连接管理

本节介绍 WS53 SLE 示例中已经由源码实现的三类链路管理能力：连接参数更新、PHY/MCS 自适应和 RSSI 粗粒度测距。示例均使用一块 Server 和一块 Client 开发板；无线环境会影响运行结果，量产参数应结合实际天线、业务流量、功耗和时延目标重新评估。

- [连接参数动态更新](./conn-param-tuning.md)
- [无线链路自适应（PHY/MCS）](./phy-mcs-switch.md)
- [RSSI 测距](./rssi-ranging.md)

三个页面的源码分别位于：

```text
src/application/samples/bt/sle/sle_conn_param_tuning/
src/application/samples/bt/sle/sle_phy_mcs_switch/
src/application/samples/bt/sle/sle_rssi_ranging/
```
