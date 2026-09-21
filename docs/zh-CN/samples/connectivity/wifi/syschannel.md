# SysChannel 通信

> 本案例演示 WS53 Device 与 Linux Host 通过 SDIO SysChannel 协同工作，包括报文分流、Device 信息上报和 Host 命令交互。完整验证需要匹配的 Linux 驱动、SDIO 硬件连接和 Host 构建环境，不能只烧录 WS53 单板完成。

## 学习目标

- 理解 SysChannel 的 Device、Linux Host 和网络报文分流关系。
- 掌握 WS53 侧通道初始化、过滤规则、收发回调和 IP/MAC 上报流程。
- 掌握 Host 侧 `sample_link` 与 `sample_cli` 的职责和基本验证方法。

## 案例说明

Device 端源码位于：src/application/samples/wifi/syschannel_dev/

Linux Host 配套源码位于：src/application/samples/wifi/syschannel_host/linux/

Device 端设置网络报文过滤规则、初始化 SDIO SysChannel，并处理 Host 发来的命令。Host 端的 `sample_link` 负责连接内核 Netlink 通道、接收 Device 上报并维护 Linux 网络接口；`sample_cli` 通过本机 UDP 端口向 `sample_link` 发送控制命令。

```mermaid
flowchart LR
    C[sample_cli] -->|UDP 127.0.0.1:8822| L[sample_link]
    L <-->|Netlink mode 28| K[Linux SysChannel 驱动]
    K <-->|SDIO| D[WS53 SysChannel Device]
    D --> W[LwIP/Wi-Fi 网络栈]
```

## 关键配置

| 配置项 | 默认值或位置 | 说明 |
| --- | --- | --- |
| Device sample | `CONFIG_SAMPLE_SUPPORT_SYSCHANNEL_DEV` | 使能后，Wi-Fi sample CMake 才加入 `syschannel_dev` |
| Device 传输类型 | `SDIO_TYPE` | 需与硬件和 Host 驱动一致 |
| Host 交叉工具链 | `arm-himix100-linux` | 定义在 `syschannel_host/linux/base.mak`，应按 Host 平台修改 |
| Host 网络接口 | `wlan0` | `sample_link` 使用该名称配置 MAC 和 IP |
| CLI 本机端口 | UDP 8822 | `sample_cli` 与 `sample_link` 的本地命令通道 |
| Netlink 参数 | PID 1100、mode 28 | 必须与配套内核驱动实现一致 |

Host 示例会配置 Linux `wlan0` 的 MAC 和 IP，需要相应权限。不要在生产设备上未经评估直接运行；接口名、Netlink 参数和权限模型都应按实际平台适配。

## 默认过滤规则

`syschannel_set_default_filter()` 先使用 `WIFI_FILTER_VLWIP` 设置默认去向，再通过 `WIFI_FILTER_LWIP` 添加送往 WS53 LwIP 的例外规则。

| 协议 | 匹配方向 | 端口 | 用途 |
| --- | --- | --- | --- |
| IPv4 UDP | 本地端口 | 68 | DHCP Client |
| IPv4 UDP | 本地端口 | 67 | DHCP Server |
| IPv4 TCP | 本地端口 | 6001 | 示例业务端口 |
| IPv4 TCP | 远端端口 | 6002 | 示例业务端口 |
| IPv4 UDP | 本地端口 | 7001 | 示例业务端口 |
| IPv4 UDP | 远端端口 | 7002 | 示例业务端口 |
| IPv6 UDP | 本地端口 | 68 | 示例 IPv6 过滤规则 |

6001、6002、7001 和 7002 只是示例值。产品应按真实协议修改，并检查端口方向、IPv4/IPv6 覆盖范围和默认去向，避免将管理报文错误转发到另一侧。

## 代码详解

### 1. 设置默认去向和精确过滤规则

```c
static int syschannel_add_udp_local_filter(uint16_t port)
{
    syschannel_ipv4_filter filter = {0};

    filter.local_port = port;
    filter.packet_type = IPPROTO_UDP;
    filter.match_mask = WIFI_FILTER_MASK_LOCAL_PORT |
        WIFI_FILTER_MASK_PROTOCOL;
    filter.config_type = WIFI_FILTER_LWIP; /* 报文送往 WS53 */
    return uapi_syschannel_add_filter((osal_char *)&filter,
        sizeof(filter), WIFI_FILTER_TYPE_IPV4);
}

static int syschannel_config_filter(void)
{
    int ret = uapi_syschannel_set_default_filter(WIFI_FILTER_VLWIP);

    if (ret != OSAL_OK) {
        return ret;
    }
    if (syschannel_add_udp_local_filter(68) != OSAL_OK) {
        return OSAL_NOK;
    }
    return syschannel_add_udp_local_filter(67);
}
```

`match_mask` 决定哪些字段参与匹配，`config_type` 决定命中规则后的报文去向。新增 TCP 或远端端口规则时，应同时修改 `packet_type`、端口字段和对应的掩码位。

### 2. 初始化 Device 通道并注册回调

案例在独立任务中初始化 SysChannel，避免阻塞系统启动流程。核心顺序如下。

```c
static int syschannel_device_start(void)
{
    if (netifapi_netif_add_ext_callback(&callback,
        app_demo_netif_ext_callback) != ERR_OK) {
        return OSAL_NOK;
    }
    if (syschannel_set_default_filter() != OSAL_OK) {
        return OSAL_NOK;
    }

    uapi_syschannel_register_rx_cb(syschannel_rx_callback);
    uapi_syschannel_register_timeout_cb(syschannel_timeout_callback);

    if (uapi_syschannel_dev_init(SDIO_TYPE) != OSAL_OK) {
        return OSAL_NOK;
    }
    uapi_syschannel_register_suspend_cb(syschannel_suspend_callback);
    return OSAL_OK;
}
```

仓库案例实际将网络回调和过滤器注册封装在 `syschannel_dev_init_demo()` 中，并在 `sdio_init_task_body()` 调用 `uapi_syschannel_dev_init()`。产品移植时应保留错误回滚：初始化失败后不得继续发送数据，也不能向业务报告通道已就绪。

### 3. 处理 Host 命令

Device 示例识别以下三个文本命令。

| 命令 | Device 行为 |
| --- | --- |
| `cmd_get_mac` | 读取网络接口 MAC，并向 Host 返回“命令类型 + 6 字节 MAC” |
| `cmd_get_ip` | 返回命令类型、IPv4 地址、掩码和网关 |
| `cmd_set_filter` | 重新设置默认过滤规则 |

```c
static const char g_host_cmd[][20] = {
    "cmd_get_mac",
    "cmd_get_ip",
    "cmd_set_filter",
};

unsigned int syschannel_rx_callback(unsigned char *buf, int length)
{
    struct netif *netif = get_syschannel_netif();

    if ((buf == NULL) || (length <= 0) || (netif == NULL)) {
        return OSAL_NOK;
    }

    /* 比较前必须同时校验 length 和命令字符串长度。 */
    if (syschannel_cmd_equal(buf, length, g_host_cmd[0])) {
        syschannel_send_mac(netif);
    } else if (syschannel_cmd_equal(buf, length, g_host_cmd[1])) {
        syschannel_send_ip(netif);
    } else if (syschannel_cmd_equal(buf, length, g_host_cmd[2])) {
        (void)syschannel_set_default_filter();
    }
    return OSAL_OK;
}
```

`syschannel_cmd_equal()` 表示产品应补充的带长度比较封装。原案例展示了命令分发思路；正式实现应避免对非 NUL 结尾的 Host 缓冲区直接使用无界字符串比较。

### 4. 上报 MAC、IP 和网络变化

MAC 消息共 7 字节：第 1 字节为 `HOST_CMD_GET_MAC`，后续 6 字节为 MAC。IP 有效载荷为 13 字节：1 字节命令类型、4 字节 IPv4 地址、4 字节掩码和 4 字节网关。

```c
osal_char mac_msg[SYSCHANNEL_MAC_ADDR_LEN + 1] = {0};

mac_msg[0] = HOST_CMD_GET_MAC;
(void)memcpy_s(&mac_msg[1], SYSCHANNEL_MAC_ADDR_LEN,
    netif->hwaddr, SYSCHANNEL_MAC_ADDR_LEN);
uapi_syschannel_send_to_host(mac_msg, sizeof(mac_msg));
```

Device 示例还注册了 LwIP netif 扩展回调，在 IPv4 地址发生变化时主动上报。Host 解析协议时必须以消息类型和实际长度为准，并统一约定字节序。

!!! note
    当前示例构造的 IP 有效内容为 13 字节，但调用 `uapi_syschannel_send_to_host()` 时传入 `MAX_IPV4_LEN + 1`。如果 Host 协议只定义上述 13 字节，产品适配时应统一双方长度定义，不能依赖额外的尾部零字节。

### 5. Host 侧命令链路

Host 端构建生成两个程序：

- `sample_link`：初始化 SysChannel、注册接收回调、与 Netlink 驱动通信，并配置 `wlan0`。
- `sample_cli`：将一条命令发往 `127.0.0.1:8822`，等待 `sample_link` 返回结果。

`sample_link` 启动后会主动发送 `cmd_get_mac`。其 CLI 明确支持 `help` 和 `quit`；其他输入会作为设备控制命令转交，能否执行取决于 Host 驱动和 Device 侧协议实现。

### 6. 超时、挂起和重新初始化

案例注册了心跳超时和挂起回调，但回调中的复位/重新探卡流程只是设计注释。超时回调可能运行在中断上下文，不能直接执行等待 SDIO 卡等阻塞操作。

推荐处理方式：

1. 回调中仅设置“需要复位/重新探卡”标志并唤醒恢复任务。
2. 恢复任务调用 `uapi_syschannel_dev_reset()` 清理旧状态。
3. 根据 Host 上下电策略等待硬件稳定。
4. 在任务上下文调用 `uapi_syschannel_dev_reinit()`，重新注册必要状态并恢复收发。
5. 恢复成功前保持上层业务离线，避免继续使用旧通道。

## 运行与验证

1. 确认 WS53 与 Linux Host 的 SDIO 硬件连接、供电时序和内核 SysChannel 驱动匹配。
2. 在 WS53 目标配置中使能 `CONFIG_SAMPLE_SUPPORT_SYSCHANNEL_DEV`，构建、烧录并检查 `syschannel dev init success` 和 `sdio init finish` 日志。
3. 进入 `src/application/samples/wifi/syschannel_host/linux/`，确认 `base.mak` 中的交叉工具链适用于目标 Host，再执行 `make` 构建 `sample_link` 和 `sample_cli`。
4. 以具备网络接口配置权限的用户启动 `sample_link`，确认 Netlink 初始化成功并能收到 Device 的 MAC/IP 消息。
5. 在另一终端执行 `sample_cli help`，验证本地 CLI 通道；完成测试后执行 `sample_cli quit`。
6. 触发 WS53 DHCP 地址变化，确认 Host 能收到更新且 `wlan0` 配置符合预期。
7. 分别验证未知命令、错误长度、通道断开、心跳超时、Host 重启和 Device 重新初始化。
8. 将示例端口、接口名、Netlink 参数和命令协议替换为产品配置后，再进行压力与异常恢复测试。

构建 WS53 固件的基础流程参见[快速入门](../../../get-started/index.md)。
