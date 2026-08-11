**概述<a name="section4537382116410"></a>**

本文档主要介绍HTTP Client功能开发实现示例。

# 开发指南<a name="ZH-CN_TOPIC_0000001953701494"></a>

-   **[概述](#ZH-CN_TOPIC_0000001988140881)**  

-   **[代码示例](#ZH-CN_TOPIC_0000001988300717)**  

## 概述<a name="ZH-CN_TOPIC_0000001988140881"></a>

HTTP示例通过lwIP提供的API完成对指定IP的建立链接，获取网页的功能。

>![](public_sys-resources/icon-note.gif) **说明：** 
>HTTP实现不新增额外的API，仅依赖lwIP提供的API接口。

## 代码示例<a name="ZH-CN_TOPIC_0000001988300717"></a>

以下为HTTP Client主动获取用户传入IP地址首页的代码示例：

```
#include <stdio.h>
#include "lwip/sockets.h"
#include "lwip/netdb.h"

#define HTTPC_DEMO_RECV_BUFSIZE 64
#define SOCK_TARGET_PORT  80
static const char *g_request = "GET / HTTP/1.1\r\n\
    Content-Type: application/x-www-form-urlencoded;charset=UTF-8\r\n\
    Host: baidu.com\r\n\
    Connection: close\r\n\
    \r\n";
/* ip_addr为访问的ip地址字符串 */
unsigned int http_clienti_get(char *ip_addr)
{
    if (ip_addr == NULL) {
        return 1;
    }
    struct sockaddr_in addr = {0};
    int s, r;
    char recv_buf[HTTPC_DEMO_RECV_BUFSIZE];
    addr.sin_family = AF_INET;
    addr.sin_port = PP_HTONS(SOCK_TARGET_PORT);
    addr.sin_addr.s_addr = inet_addr(ip_addr);
    s = socket(AF_INET, SOCK_STREAM, 0);
    if (s < 0) {
        return 1;
    }
    printf("... allocated socket\r\n");
    if (connect(s, (struct sockaddr*)&addr, sizeof(addr)) != 0) {
        printf("... socket connect failed errno=%d\r\n", errno);
        lwip_close(s);
        return 1;
    }
    printf("... connected");
    if (lwip_write(s, g_request, strlen(g_request)) < 0) {
        lwip_close(s);
        return 1;
    }
    printf("... socket send success\r\n");
    struct timeval receiving_timeout;
    /* 5S Timeout */
    receiving_timeout.tv_sec = 5;
    receiving_timeout.tv_usec = 0;
    if (setsockopt(s, SOL_SOCKET, SO_RCVTIMEO, &receiving_timeout, sizeof(receiving_timeout)) < 0) {
        printf("... failed to set socket receiving timeout\r\n");
        lwip_close(s);
        return 1;
    }
    printf("... set socket receiving timeout success\r\n");
    /* Read HTTP response */
    do {
        (void)memset_s(recv_buf, sizeof(recv_buf), 0, sizeof(recv_buf));
        r = lwip_read(s, recv_buf, sizeof(recv_buf) - 1);
        for (int i = 0; i < r; i++) {
            putchar(recv_buf[i]);
        }
    } while (r > 0);
    printf("... done reading from socket. Last read return=%d errno=%d\r\n", r, errno);
    lwip_close(s);
    return 0;
}
```


