**概述<a name="section4537382116410"></a>**

本文档介绍WS53芯片SDK开发环境（包括：SDK编译、应用程序的开发等），用于帮助用户在快速了解开发环境后编译出可执行文件进行二次开发。

# 开发环境搭建<a name="ZH-CN_TOPIC_0000001777234338"></a>

-   **[SDK开发环境简介](#ZH-CN_TOPIC_0000001823873929)**  

-   **[搭建Linux开发环境](#ZH-CN_TOPIC_0000001823873925)**  

## SDK开发环境简介<a name="ZH-CN_TOPIC_0000001823873929"></a>

典型的SDK开发环境主要包括：

-   Linux服务器

    Linux服务器主要用于建立交叉编译环境，实现在Linux服务器上编译出可以在目标板上运行的可执行代码。

-   工作台

    工作台主要用于目标板烧录和调试，通过串口与目标板连接，开发人员可以在工作台中烧录目标板的镜像、调试程序。工作台通常需要安装终端工具，用于登录Linux服务器和目标板，查看目标板的打印输出信息。工作台一般为Windows或Linux操作系统，在Windows或Linux工作台运行的终端工具通常有SecureCRT、Putty、miniCom等，这些软件需要从其官网下载。

-   目标板

    本文的目标板以DEMO板为例，DEMO板与工作台通过USB转串口连接。工作台将交叉编译出来的DEMO板镜像通过串口烧录到DEMO板。如[图1](#fig1236915206315)所示。

    **图 1**  SDK 开发环境<a name="fig1236915206315"></a>  
    
    ![](figures/zh-cn_image_0000001777234358.png)

## 搭建Linux开发环境<a name="ZH-CN_TOPIC_0000001823873925"></a>

Linux系统推荐使用Ubuntu 18.04及以上版本，Shell使用bash ，SDK使用Cmake编译（3.14.1以上），编译工具还包括Python（3.8.0以上）等。

-   **[配置Shell](#ZH-CN_TOPIC_0000001777394006)**  

-   **[安装Cmake](#ZH-CN_TOPIC_0000001823993865)**  

-   **[安装Python环境](#ZH-CN_TOPIC_0000001777394014)**  

### 配置Shell<a name="ZH-CN_TOPIC_0000001777394006"></a>

配置默认使用 bash。打开Linux终端，执行命令“sudo dpkg-reconfigure dash”，选择 no。

### 安装Cmake<a name="ZH-CN_TOPIC_0000001823993865"></a>

打开Linux终端，执行命令“sudo apt install cmake”，完成Cmake的安装。

### 安装Python环境<a name="ZH-CN_TOPIC_0000001777394014"></a>

1.  打开Linux终端，输入命令“python3 -V”，查看Python版本号，推荐python3.8.0以上版本。
2.  如果Python版本太低，请使用命令“sudo apt-get update”更新系统到最新，或通过命令“sudo apt-get install python3 -y”安装Python3（需root/sudo权限安装），安装后再次确认Python版本。

    如果仍不能满足版本要求，请从“[https://www.python.org/downloads/source/](https://www.python.org/downloads/source/)  ”下载对应版本源码包，下载与安装方法请阅读  [https://wiki.python.org/moin/BeginnersGuide/Download](https://wiki.python.org/moin/BeginnersGuide/Download)  和源码包内README内容。

3.  安装Python包管理工具，运行命令“sudo apt-get install python3-setuptools python3-pip -y”（需root/sudo权限安装）。
4.  安装Kconfiglib 14.1.0+，使用命令“sudo pip3 install kconfiglib”（需root/sudo权限安装），或从“[https://pypi.org/project/kconfiglib](https://pypi.org/project/kconfiglib)”下载.whl文件（例如：kconfiglib-14.1.0-py2.py3-none-any.whl）后，使用“pip3 install kconfiglib-xxx.whl”进行安装（需root/sudo权限安装），或者下载源码包到本地并解压，使用“python setup.py install”进行安装（需root/sudo权限安装）。安装完成界面如[图1](#fig743717512220)所示。

    **图 1**  安装Kconfiglib组件包完成示例<a name="fig743717512220"></a>  
    ![](figures/安装Kconfiglib组件包完成示例.png "安装Kconfiglib组件包完成示例")

5.  安装升级文件签名依赖的Python组件包。

    安装pycparser：

    从“[https://pypi.org/project/pycparser/](https://pypi.org/project/pycparser/)”下载.whl文件（例如：pycparser-2.21-py2.py3-none-any.whl）后，使用“pip3 install pycparser-xxx.whl”进行安装（需root/sudo权限安装），或者下载源码包到本地并解压，使用“python setup.py install”进行安装（需root/sudo权限安装）。安装完成后界面会提示“Successfully intalled pycparser-2.21”。

>![](public_sys-resources/icon-note.gif) **说明：** 
>如果构建环境中包含多个python，特别是多个同版本的python，而用户无法辨认正在使用的是其中的哪个版本，此情况下，在安装python组件包时，推荐使用组件包源码进行安装。

# 编译<a name="ZH-CN_TOPIC_0000001777394010"></a>

-   **[SDK目录结构介绍](#ZH-CN_TOPIC_0000001777394018)**  

-   **[编译（Cmake）](#ZH-CN_TOPIC_0000001777234346)**  

## SDK目录结构介绍<a name="ZH-CN_TOPIC_0000001777394018"></a>

解压缩SDK后的根目录，如[图1](#fig3274131411460)所示。（编译后生成output目录）

**图 1**  解压缩SDK示例<a name="fig3274131411460"></a>  
![](figures/解压缩SDK示例.png "解压缩SDK示例")

SDK根目录结构如[表1](#table13927142512394)所示。

**表 1**  SDK根目录

<a name="table13927142512394"></a>
<table><thead align="left"><tr id="row15927132514396"><th class="cellrowborder" valign="top" width="27.38%" id="mcps1.2.3.1.1"><p id="p11927325113916"><a name="p11927325113916"></a><a name="p11927325113916"></a>目录</p>
</th>
<th class="cellrowborder" valign="top" width="72.61999999999999%" id="mcps1.2.3.1.2"><p id="p1292722593913"><a name="p1292722593913"></a><a name="p1292722593913"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row292882517399"><td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.3.1.1 "><p id="p159281025163910"><a name="p159281025163910"></a><a name="p159281025163910"></a>application</p>
</td>
<td class="cellrowborder" valign="top" width="72.61999999999999%" headers="mcps1.2.3.1.2 "><p id="p417918234"><a name="p417918234"></a><a name="p417918234"></a>应用层代码（其中包含demo程序为参考示例）。</p>
</td>
</tr>
<tr id="row9528141355717"><td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.3.1.1 "><p id="p185281313195712"><a name="p185281313195712"></a><a name="p185281313195712"></a>bootloader</p>
</td>
<td class="cellrowborder" valign="top" width="72.61999999999999%" headers="mcps1.2.3.1.2 "><p id="p9528101318575"><a name="p9528101318575"></a><a name="p9528101318575"></a>boot引导文件目录。</p>
</td>
</tr>
<tr id="row19928225163913"><td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.3.1.1 "><p id="p2928122511393"><a name="p2928122511393"></a><a name="p2928122511393"></a>build</p>
</td>
<td class="cellrowborder" valign="top" width="72.61999999999999%" headers="mcps1.2.3.1.2 "><p id="p1192882518398"><a name="p1192882518398"></a><a name="p1192882518398"></a>SDK构建所需的脚本、配置文件。</p>
</td>
</tr>
<tr id="row109286253399"><td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.3.1.1 "><p id="p387753614257"><a name="p387753614257"></a><a name="p387753614257"></a>drivers</p>
</td>
<td class="cellrowborder" valign="top" width="72.61999999999999%" headers="mcps1.2.3.1.2 "><p id="p69284253398"><a name="p69284253398"></a><a name="p69284253398"></a>驱动代码。</p>
</td>
</tr>
<tr id="row15928132512396"><td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.3.1.1 "><p id="p3928172518391"><a name="p3928172518391"></a><a name="p3928172518391"></a>include</p>
</td>
<td class="cellrowborder" valign="top" width="72.61999999999999%" headers="mcps1.2.3.1.2 "><p id="p0346235152311"><a name="p0346235152311"></a><a name="p0346235152311"></a>API头文件存放目录。</p>
</td>
</tr>
<tr id="row415218166102"><td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.3.1.1 "><p id="p77991553198"><a name="p77991553198"></a><a name="p77991553198"></a>interim_binary</p>
</td>
<td class="cellrowborder" valign="top" width="72.61999999999999%" headers="mcps1.2.3.1.2 "><p id="p1615231614109"><a name="p1615231614109"></a><a name="p1615231614109"></a>库存放目录。</p>
</td>
</tr>
<tr id="row75842056117"><td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.3.1.1 "><p id="p2058415591118"><a name="p2058415591118"></a><a name="p2058415591118"></a>kernel</p>
</td>
<td class="cellrowborder" valign="top" width="72.61999999999999%" headers="mcps1.2.3.1.2 "><p id="p558420511112"><a name="p558420511112"></a><a name="p558420511112"></a>内核代码和OS接口适配层代码。</p>
</td>
</tr>
<tr id="row66711609211"><td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.3.1.1 "><p id="p17671140720"><a name="p17671140720"></a><a name="p17671140720"></a>libs_url</p>
</td>
<td class="cellrowborder" valign="top" width="72.61999999999999%" headers="mcps1.2.3.1.2 "><p id="p5671150426"><a name="p5671150426"></a><a name="p5671150426"></a>二进制bin校对文件目录。</p>
</td>
</tr>
<tr id="row152262035269"><td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.3.1.1 "><p id="p9770185051720"><a name="p9770185051720"></a><a name="p9770185051720"></a>middleware</p>
</td>
<td class="cellrowborder" valign="top" width="72.61999999999999%" headers="mcps1.2.3.1.2 "><p id="p1422613353614"><a name="p1422613353614"></a><a name="p1422613353614"></a>中间件代码。</p>
</td>
</tr>
<tr id="row07472124410"><td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.3.1.1 "><p id="p1574821211416"><a name="p1574821211416"></a><a name="p1574821211416"></a>open_source</p>
</td>
<td class="cellrowborder" valign="top" width="72.61999999999999%" headers="mcps1.2.3.1.2 "><p id="p126461354552"><a name="p126461354552"></a><a name="p126461354552"></a>开源代码。</p>
</td>
</tr>
<tr id="row26011201747"><td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.3.1.1 "><p id="p1601420844"><a name="p1601420844"></a><a name="p1601420844"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="72.61999999999999%" headers="mcps1.2.3.1.2 "><p id="p14611201340"><a name="p14611201340"></a><a name="p14611201340"></a>WiFi、BT、Radar等组件代码。</p>
</td>
</tr>
<tr id="row17392173512420"><td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.3.1.1 "><p id="p1839303512418"><a name="p1839303512418"></a><a name="p1839303512418"></a>test</p>
</td>
<td class="cellrowborder" valign="top" width="72.61999999999999%" headers="mcps1.2.3.1.2 "><p id="p83938351045"><a name="p83938351045"></a><a name="p83938351045"></a>testsuite代码。</p>
</td>
</tr>
<tr id="row17747172410413"><td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.3.1.1 "><p id="p203484262154"><a name="p203484262154"></a><a name="p203484262154"></a>tools</p>
</td>
<td class="cellrowborder" valign="top" width="72.61999999999999%" headers="mcps1.2.3.1.2 "><p id="p87471724848"><a name="p87471724848"></a><a name="p87471724848"></a>包含编译工具链（包括linux和windows）、镜像打包脚本、NV制作工具和签名脚本等。</p>
</td>
</tr>
<tr id="row768611001510"><td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.3.1.1 "><p id="p374913341514"><a name="p374913341514"></a><a name="p374913341514"></a>output</p>
</td>
<td class="cellrowborder" valign="top" width="72.61999999999999%" headers="mcps1.2.3.1.2 "><p id="p1774983141513"><a name="p1774983141513"></a><a name="p1774983141513"></a>编译时生成的目标文件与中间文件（包括库文件、打印log、生成的二进制文件等）。</p>
</td>
</tr>
<tr id="row74261653608"><td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.3.1.1 "><p id="p026611127118"><a name="p026611127118"></a><a name="p026611127118"></a>build.py</p>
</td>
<td class="cellrowborder" valign="top" width="72.61999999999999%" headers="mcps1.2.3.1.2 "><p id="p16266812117"><a name="p16266812117"></a><a name="p16266812117"></a>编译入口脚本。</p>
</td>
</tr>
<tr id="row1927612418117"><td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.3.1.1 "><p id="p12661212616"><a name="p12661212616"></a><a name="p12661212616"></a>CMakeLists.txt</p>
</td>
<td class="cellrowborder" valign="top" width="72.61999999999999%" headers="mcps1.2.3.1.2 "><p id="p1626716121115"><a name="p1626716121115"></a><a name="p1626716121115"></a>Cmake工程顶层“CMakeLists.txt”文件。</p>
</td>
</tr>
<tr id="row175646591908"><td class="cellrowborder" valign="top" width="27.38%" headers="mcps1.2.3.1.1 "><p id="p8267101212119"><a name="p8267101212119"></a><a name="p8267101212119"></a>config.in</p>
</td>
<td class="cellrowborder" valign="top" width="72.61999999999999%" headers="mcps1.2.3.1.2 "><p id="p1426721212110"><a name="p1426721212110"></a><a name="p1426721212110"></a>Kconfig配置文件。</p>
</td>
</tr>
</tbody>
</table>

## 编译（Cmake）<a name="ZH-CN_TOPIC_0000001777234346"></a>

-   **[内核依赖配置](#ZH-CN_TOPIC_0000001987379681)**  

-   **[编译方法](#ZH-CN_TOPIC_0000001823993877)**  

-   **[Flash分区表配置](#ZH-CN_TOPIC_0000002079231697)**  

-   **[Menuconfig配置](#ZH-CN_TOPIC_0000001777234354)**  

-   **[UART配置方法](#ZH-CN_TOPIC_0000001949361268)**  

-   **[注意事项](#ZH-CN_TOPIC_0000001823993861)**  

### 内核依赖配置<a name="ZH-CN_TOPIC_0000001987379681"></a>

SDK编译默认包含Syschannel Host驱动编译，编译SDK前，需要修改“/middleware/utils/syschannel/syschannel\_host/Makefile”指定正确的内核路径。

详细配置方法参考《WS53V100 Syschannel 使用指南》 的“Syschannel 组件编译”章节。

如果不需要编译Syschannel Host驱动，可以修改"build/config/target\_config/ws53/config.py"文件，删除或注释掉ram\_component中的"syschannel\_host\_ko"组件。

### 编译方法<a name="ZH-CN_TOPIC_0000001823993877"></a>

根目录下执行“python3 build.py ws53\_liteos\_app”指令运行脚本编译ws53\_liteos\_app。编译命令列表如[表1](#table1646491114816)所示。

**表 1**  build.sh参数列表

<a name="table1646491114816"></a>
<table><thead align="left"><tr id="row44654114810"><th class="cellrowborder" valign="top" width="12.76%" id="mcps1.2.4.1.1"><p id="p194651412487"><a name="p194651412487"></a><a name="p194651412487"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="37.480000000000004%" id="mcps1.2.4.1.2"><p id="p6461872507"><a name="p6461872507"></a><a name="p6461872507"></a>示例</p>
</th>
<th class="cellrowborder" valign="top" width="49.76%" id="mcps1.2.4.1.3"><p id="p1246515144820"><a name="p1246515144820"></a><a name="p1246515144820"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row746513144812"><td class="cellrowborder" valign="top" width="12.76%" headers="mcps1.2.4.1.1 "><p id="p2465219482"><a name="p2465219482"></a><a name="p2465219482"></a>无</p>
</td>
<td class="cellrowborder" valign="top" width="37.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p1215022142715"><a name="p1215022142715"></a><a name="p1215022142715"></a>python3 build.py ws53_liteos_app</p>
</td>
<td class="cellrowborder" valign="top" width="49.76%" headers="mcps1.2.4.1.3 "><p id="p144651117489"><a name="p144651117489"></a><a name="p144651117489"></a>启动ws53_liteos_app目标的增量编译。</p>
</td>
</tr>
<tr id="row04651218489"><td class="cellrowborder" valign="top" width="12.76%" headers="mcps1.2.4.1.1 "><p id="p24654119480"><a name="p24654119480"></a><a name="p24654119480"></a>-c</p>
</td>
<td class="cellrowborder" valign="top" width="37.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p16463717500"><a name="p16463717500"></a><a name="p16463717500"></a>python3 build.py -c ws53_liteos_app</p>
</td>
<td class="cellrowborder" valign="top" width="49.76%" headers="mcps1.2.4.1.3 "><p id="p1046516134810"><a name="p1046516134810"></a><a name="p1046516134810"></a>启动ws53_liteos_app目标的全量编译。</p>
</td>
</tr>
<tr id="row11696675533"><td class="cellrowborder" valign="top" width="12.76%" headers="mcps1.2.4.1.1 "><p id="p206971172535"><a name="p206971172535"></a><a name="p206971172535"></a>menuconfig</p>
</td>
<td class="cellrowborder" valign="top" width="37.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p1669710713535"><a name="p1669710713535"></a><a name="p1669710713535"></a>python3 build.py  ws53_liteos_app menuconfig</p>
</td>
<td class="cellrowborder" valign="top" width="49.76%" headers="mcps1.2.4.1.3 "><p id="p18697274534"><a name="p18697274534"></a><a name="p18697274534"></a>启动ws53_liteos_app目标的menuconfig图形配置界面。</p>
</td>
</tr>
</tbody>
</table>

编译得到的烧录全量镜像在“output/ws53/fwpkg/pack\_all\_core/ws53\_liteos\_app”目录下（如[表2](#table5535429403)所示）。

**表 2**  烧录镜像

<a name="table5535429403"></a>
<table><thead align="left"><tr id="row1353722184019"><th class="cellrowborder" valign="top" width="21.45%" id="mcps1.2.3.1.1"><p id="p97691634164219"><a name="p97691634164219"></a><a name="p97691634164219"></a>文件名</p>
</th>
<th class="cellrowborder" valign="top" width="78.55%" id="mcps1.2.3.1.2"><p id="p253772164019"><a name="p253772164019"></a><a name="p253772164019"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row75376234019"><td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.2.3.1.1 "><p id="p1740682318402"><a name="p1740682318402"></a><a name="p1740682318402"></a>ws53_liteos_app_all_in_one.fwpkg</p>
</td>
<td class="cellrowborder" valign="top" width="78.55%" headers="mcps1.2.3.1.2 "><p id="p10903201011919"><a name="p10903201011919"></a><a name="p10903201011919"></a>空片烧录时，需要烧录此文件。包含了所有的需要升级的内容。包含：loaderboot_sign.bin、root_params_sign.bin、flashboot_sign_a.bin、flashboot_sign_b.bin、application_sign.bin、control_ws53_sign.bin、ws53_all_nv.bin。</p>
<p id="p7548577443"><a name="p7548577443"></a><a name="p7548577443"></a>各文件介绍如下：</p>
<p id="p195743193449"><a name="p195743193449"></a><a name="p195743193449"></a>loaderboot_sign.bin：loaderboot的镜像文件。升级开始时，芯片中固化的romboot会接收此镜像文件，加载到内存并运行，loadboot负责接收后续的镜像文件。注：此镜像只在升级阶段放在RAM中运行，并不存放在flash中。</p>
<p id="p10824083475"><a name="p10824083475"></a><a name="p10824083475"></a>root_params_sign.bin：flash分区信息的镜像文件。分区信息供romboot、loaderboot和flashboot使用。</p>
<p id="p7357934174719"><a name="p7357934174719"></a><a name="p7357934174719"></a>flashboot_sign_a.bin：flashboot的镜像文件。</p>
<p id="p883010569475"><a name="p883010569475"></a><a name="p883010569475"></a>flashboot_sing_b.bin： flashboot的备份镜像文件。</p>
<p id="p173914138483"><a name="p173914138483"></a><a name="p173914138483"></a>application_sign.bin：版本镜像文件。</p>
<p id="p224522374812"><a name="p224522374812"></a><a name="p224522374812"></a>control_ws53_sign.bin：c核镜像文件。</p>
<p id="p330002919489"><a name="p330002919489"></a><a name="p330002919489"></a>ws53_all_nv.bin：参数区的镜像文件。</p>
</td>
</tr>
<tr id="row15537132114020"><td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.2.3.1.1 "><p id="p20351123274017"><a name="p20351123274017"></a><a name="p20351123274017"></a>ws53_liteos_app_load_only.fwpkg</p>
</td>
<td class="cellrowborder" valign="top" width="78.55%" headers="mcps1.2.3.1.2 "><p id="p109031510191919"><a name="p109031510191919"></a><a name="p109031510191919"></a>版本升级打包文件，包含：loaderboot_sign.bin和application_sign.bin。不包含flashboot相关内容。</p>
<p id="p7556838163116"><a name="p7556838163116"></a><a name="p7556838163116"></a>当芯片烧录过“ws53_liteos_app_all_in_one.fwpkg”镜像后，如果后续修改不涉及root_params、flash_boot、nv的修改，则可以用此文件升级。</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **说明：** 
>注：编译得到的中间文件在“output/ws53/acore/ws53\_liteos\_app”目录下。

### Flash分区表配置<a name="ZH-CN_TOPIC_0000002079231697"></a>

分区表配置文件路径：sdk\\build\\config\\target\_config\\ws53\\param\_sector\\param\_sector.json

![](figures/zh-cn_image_0000002043245450.png)

>![](public_sys-resources/icon-note.gif) **说明：** 
>上图内容仅作文件内容说明，具体分区信息请参考《WS53V100 FOTA 开发指南》“升级包保存”章节的“注意事项”中分区信息。
>分区表ID限制16个分区数量，默认Flash共4M大小，预留5个分区ID，可通过uapi\_partition\_get\_info接口传入分区ID获取对应地址和长度。

根据当前Flash分区方案，Flash划分情况如下图：

![](figures/zh-cn_image_0000002089402393.png)

调整分区时，需要遵守以下原则：

1.  地址段0x000000\~0x030000为不可调整区，**任何改动都可能会导致无法启动而变砖。**
2.  地址段0x030000\~0x270000为APP镜像区，地址段信息来源于分区表中ID为0x20对应的APP镜像区，**该地址段仅支持调整分区大小，分区首地址不支持调整**，调整分区首地址同样会导致无法启动。
3.  地址段0x270000\~0x3F3000为FOTA镜像区，地址段信息来源于分区表中ID为0x22对应的压缩分区/OTA升级分区/产测镜像分区/B面分区，**该分区首地址必须为APP镜像区的结束地址**；**使用压缩升级方案时，该分区大小至少配置为APP镜像区大小的0.7倍及以上**。
4.  地址段0x3F3000\~0x3FA000为预留分区，该分区首地址为FOTA镜像区的结束地址，支持划分为5个不同分区ID的单独分区。
5.  地址段0x3FA000\~0x400000为其他功能区，包括死机信息\(0x11\)以及NV分区\(0x10\)，**该分区不支持调整**。
6.  调整分区时，除不可调整区以外，其他分区的首地址以及大小均要4K对齐。

调整分区示例：

根据分区表中分区信息，想要调整分区ID为0x30的预留分区的大小。

1.  假设在APP镜像分区有8K的空间余量，则调整APP镜像区的大小，0x20以及0x21分区大小同步减少8K，同步修改文件drivers/boards/ws53/memory\_config/include/memory\_config\_common.h，将文件中宏APP\_PROGRAM\_LENGTH的值\(默认为'\(0x213000 - CODE\_INFO\_OFFSET\)'\)修改为调整后分区大小\(如'\(0x211000 - CODE\_INFO\_OFFSET\)'\)。
2.  FOTA分区受APP镜像区的影响，首地址前移8K，调整为0x26E000，压缩升级方案中FOTA分区大小需同步调整，4K对齐后为减少4K，最终FOTA分区结束地址为0x3F0000。
3.  APP镜像分区以及FOTA分区总计调整出12K的余量，可合并到预留分区中，预留分区首地址前移12K，为0x3F0000，同时大小增加12K，结束地址保持为0x3FA000。

### Menuconfig配置<a name="ZH-CN_TOPIC_0000001777234354"></a>

运行“python3 build.py -c ws53\_liteos\_app menuconfig”脚本会启动Menuconfig程序，用户可通过Menuconfig对编译和系统功能进行配置，如[图1](#fig155343385597)所示。

SDK集成了默认配置，但建议用户首次运行时进行相应配置，从而减少因为配置原因引起的问题。用户随时可以运行“python3 build.py -c ws53\_liteos\_app menuconfig”更改配置。

**图 1**  Menuconfig运行界面<a name="fig155343385597"></a>  

![](figures/zh-cn_image_0000001782676170.png)

注：界面如存在差异，以实际版本为准。

Menuconfig操作说明如[表1](#table364152210248)所示，在Menuconfig界面中可输入快捷键进行配置。

**表 1**  Menuconfig常用操作命令

<a name="table364152210248"></a>
<table><thead align="left"><tr id="row2642122213247"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.3.1.1"><p id="p10343125916259"><a name="p10343125916259"></a><a name="p10343125916259"></a>快捷键</p>
</th>
<th class="cellrowborder" valign="top" width="83%" id="mcps1.2.3.1.2"><p id="p0642102212419"><a name="p0642102212419"></a><a name="p0642102212419"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row146421622162417"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="p66421322192415"><a name="p66421322192415"></a><a name="p66421322192415"></a>空格、回车</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><p id="p464282282416"><a name="p464282282416"></a><a name="p464282282416"></a>选中，反选。</p>
</td>
</tr>
<tr id="row0235155732813"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="p123512571284"><a name="p123512571284"></a><a name="p123512571284"></a>ESC</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><p id="p4235125718282"><a name="p4235125718282"></a><a name="p4235125718282"></a>返回上级菜单，退出界面。</p>
</td>
</tr>
<tr id="row1425985152914"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="p02597515295"><a name="p02597515295"></a><a name="p02597515295"></a>Q</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><p id="p1825945119290"><a name="p1825945119290"></a><a name="p1825945119290"></a>退出界面。</p>
</td>
</tr>
<tr id="row161871942143019"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="p718744220300"><a name="p718744220300"></a><a name="p718744220300"></a>S</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><p id="p1818734211305"><a name="p1818734211305"></a><a name="p1818734211305"></a>保存配置。</p>
</td>
</tr>
<tr id="row1661115053113"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="p1861165015311"><a name="p1861165015311"></a><a name="p1861165015311"></a>F</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><p id="p17611125012312"><a name="p17611125012312"></a><a name="p17611125012312"></a>显示帮助菜单。</p>
</td>
</tr>
</tbody>
</table>

所有命令可在Menuconfig界面的下方查看Menuconfig官方说明解释，如[图2](#fig14504171214012)所示。

**图 2**  Menuconfig命令帮助栏<a name="fig14504171214012"></a>  

![](figures/zh-cn_image_0000001829475697.png)

**表 2**  常用Menuconfig配置

<a name="table178211131356"></a>
<table><thead align="left"><tr id="row16821213352"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p189691731122715"><a name="p189691731122715"></a><a name="p189691731122715"></a>配置项</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p763272032717"><a name="p763272032717"></a><a name="p763272032717"></a>menuconfig路径</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p9965112614271"><a name="p9965112614271"></a><a name="p9965112614271"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row98215132054"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p0310939194115"><a name="p0310939194115"></a><a name="p0310939194115"></a>ccpriv at debug command</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15341330885"><a name="p15341330885"></a><a name="p15341330885"></a>Middleware → Utils → AT→ Config AT→ccpriv at debug command</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p17310173918418"><a name="p17310173918418"></a><a name="p17310173918418"></a>打开WiFi模块的调试命令开关</p>
</td>
</tr>
<tr id="row15703124135819"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p77031495819"><a name="p77031495819"></a><a name="p77031495819"></a>Support bluetooth/sparklink host save smp keys</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p370314410584"><a name="p370314410584"></a><a name="p370314410584"></a>Protocol → bt_host → Support bluetooth → sparklink host save smp keys</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p63292277020"><a name="p63292277020"></a><a name="p63292277020"></a>打开星闪/蓝牙模块的密钥持久化能力（需要同时打开Middleware → Chips → Chip Configurations for ws53 → NV）</p>
</td>
</tr>
</tbody>
</table>

### UART配置方法<a name="ZH-CN_TOPIC_0000001949361268"></a>

WS53总共有3个UART，SDK默认配置如下。

<a name="table179737495303"></a>
<table><thead align="left"><tr id="row12271050193018"><th class="cellrowborder" valign="top" width="19.06%" id="mcps1.1.5.1.1"><p id="p4274501303"><a name="p4274501303"></a><a name="p4274501303"></a>UART序号</p>
</th>
<th class="cellrowborder" valign="top" width="22.52%" id="mcps1.1.5.1.2"><p id="p182755019307"><a name="p182755019307"></a><a name="p182755019307"></a>波特率</p>
</th>
<th class="cellrowborder" valign="top" width="31.269999999999996%" id="mcps1.1.5.1.3"><p id="p6509141917115"><a name="p6509141917115"></a><a name="p6509141917115"></a>默认配置</p>
</th>
<th class="cellrowborder" valign="top" width="27.150000000000002%" id="mcps1.1.5.1.4"><p id="p20272509302"><a name="p20272509302"></a><a name="p20272509302"></a>用途</p>
</th>
</tr>
</thead>
<tbody><tr id="row8279503302"><td class="cellrowborder" valign="top" width="19.06%" headers="mcps1.1.5.1.1 "><p id="p11274502303"><a name="p11274502303"></a><a name="p11274502303"></a>0 H1</p>
</td>
<td class="cellrowborder" valign="top" width="22.52%" headers="mcps1.1.5.1.2 "><p id="p327850183010"><a name="p327850183010"></a><a name="p327850183010"></a>115200</p>
</td>
<td class="cellrowborder" valign="top" width="31.269999999999996%" headers="mcps1.1.5.1.3 "><p id="p1509141917110"><a name="p1509141917110"></a><a name="p1509141917110"></a>空闲不使用</p>
</td>
<td class="cellrowborder" valign="top" width="27.150000000000002%" headers="mcps1.1.5.1.4 "><p id="p1227450143011"><a name="p1227450143011"></a><a name="p1227450143011"></a>支持DEBUG、AT、HSO</p>
</td>
</tr>
<tr id="row182785073016"><td class="cellrowborder" valign="top" width="19.06%" headers="mcps1.1.5.1.1 "><p id="p92715013015"><a name="p92715013015"></a><a name="p92715013015"></a>1 H0</p>
</td>
<td class="cellrowborder" valign="top" width="22.52%" headers="mcps1.1.5.1.2 "><p id="p927195023011"><a name="p927195023011"></a><a name="p927195023011"></a>921600</p>
</td>
<td class="cellrowborder" valign="top" width="31.269999999999996%" headers="mcps1.1.5.1.3 "><p id="p165097192115"><a name="p165097192115"></a><a name="p165097192115"></a>HSO（连接HSO工具用于WiFi日志抓取）</p>
</td>
<td class="cellrowborder" valign="top" width="27.150000000000002%" headers="mcps1.1.5.1.4 "><p id="p7272050103014"><a name="p7272050103014"></a><a name="p7272050103014"></a>支持HSO、DEBUG</p>
</td>
</tr>
<tr id="row1327155093018"><td class="cellrowborder" valign="top" width="19.06%" headers="mcps1.1.5.1.1 "><p id="p152735013013"><a name="p152735013013"></a><a name="p152735013013"></a>2 L0</p>
</td>
<td class="cellrowborder" valign="top" width="22.52%" headers="mcps1.1.5.1.2 "><p id="p15271150183018"><a name="p15271150183018"></a><a name="p15271150183018"></a>115200</p>
</td>
<td class="cellrowborder" valign="top" width="31.269999999999996%" headers="mcps1.1.5.1.3 "><p id="p1750911199116"><a name="p1750911199116"></a><a name="p1750911199116"></a>烧录、DEBUG、AT</p>
</td>
<td class="cellrowborder" valign="top" width="27.150000000000002%" headers="mcps1.1.5.1.4 "><p id="p627750153017"><a name="p627750153017"></a><a name="p627750153017"></a>支持烧录、DEBUG、AT、HSO</p>
</td>
</tr>
</tbody>
</table>

-   烧录功能，固定用UART-L0，不可更改。

-   HSO串口默认是UART-H0, 可以配置为UART-L0或UART-H1，波特率可以通过menuconfig进行定制，默认使用921600，支持关闭。

    menuconfig的配置路径为Drivers-\>Chips-\>Chip Configurations for ws53。

    ![](figures/zh-cn_image_0000002247598320.png)

-   AT串口默认是UART-L0，可通过menuconfig配置串口号（可选UART-L0、UART-H1）和波特率，默认使用UART-L0，波特率默认为115200，支持关闭。 menuconfig的配置路径为Drivers-\>Chips-\>Chip Configurations for ws53。

    ![](figures/zh-cn_image_0000002282797565.png)

-   DEBUG串口可通过menuconfig配置串口号（可选UART-L0、UART-H1、UART-H0）和波特率，默认使用UART-L0，波特率默认为115200，支持关闭。

    ![](figures/zh-cn_image_0000002247760108.png)

-   支持UART-L0 RX管脚复用为普通GPIO，仅保留TX功能。可通过打开CONFIG\_UART\_L0\_NOT\_SUPPORT\_RX实现，默认未打开，menuconfig配置方法如下。

    ![](figures/zh-cn_image_0000002247600772.png)

-   支持AT、DEBUG串口功能合一到HSO口上，可以用HSO工具完成AT命令及回显、DEBUG日志、HSO日志功能。需要先打开**CONFIG\_AT\_SUPPORT\_ZDIAG**宏，再通过menuconfig配置HSO/AT/DEBUG为同一串口，波特率一致，可以选择是否打开HSO心跳功能。以下是将AT、DEBUG功能都合一到HSO上，并使用L0作为串口的配置示例如下。
    ![](figures/zh-cn_image_0000002298050126.png)

    ![](figures/zh-cn_image_0000002247763860.png)

    -   AT、DEBUG串口功能合到HSO口，使用时需要注意以下事项：
        1.  连接HSO工具前要配置关闭低功耗。
        2.  想要退出HSO工具连接，切换普通串口连接，需要在HSO工具主动发起断连，确保已退出HSO连接。
        3.  不支持串口合一到H0，深睡时H0不支持唤醒，会导致AT无法使用。
        4.  合一时HSO、AT、DEBUG波特率建议都配置为921600及以上。
        5.  HSO工具的版本号，需要选择3.0.120版本及以上。

-   串口管脚复用配置：

    1.  debug串口方案上A/C核共用串口，debug串口管脚跟随选择的串口选择对应管脚。如果选择UART L0，串口管脚采用AGPIO1和AGPIO2; 如果选择UART H1，串口管脚TX采用MGPIO12，RX采用AGPIO4。为了串口输入能唤醒系统，RX管脚都会采用AGPIO。
    2.  AT口/HSO口，可以选择与debug口复用串口，此时管脚与debug口一致。如果选择其他串口，可以更改管脚配置。配置代码位于文件uart\_porting.c，参考函数uart\_port\_config\_pinmux, 该函数配置了对应串口管脚的模式和上拉。硬件管脚如果与默认配置不一样，需要修改函数中对应管脚定义的宏。
    3.  对于AT命令 UART RX管脚，建议选择AGPIO管脚，否则AT命令本身无法唤醒系统，需要由其它管脚唤醒或者关闭低功耗模式才能输入串口。
    4.  UART RX管脚配置下拉可能导致误触发串口中断，建议针对该管脚在低功耗初始化函数uapi\_pm\_lpc\_init调用pm\_port\_skip\_pull\_down配置跳过睡眠流程下拉处理。

>![](public_sys-resources/icon-notice.gif) **须知：** 
>1.  UART波特率建议配置典型值，如115200/921600/1M等，考虑到兼容性，不建议配置不常用的特殊值，比如115623此类波特率值。
>2.  修改UART序号请慎重，必须要与板级硬件工程师确认uart硬件连接，确保软件配置与硬件板级的实际电路连接匹配，否则无法正常工作。

### 注意事项<a name="ZH-CN_TOPIC_0000001823993861"></a>

-   如果执行“./build.py”提示无权限，可执行命令“chmod +x build.py”添加执行权限或执行“python3 ./build.py”。
-   编译过程中，报错找不到某个包，请检查环境中的python是否已经安装了相应组件。如果构建环境中包含多个python，特别是多个同版本的python，而用户无法辨认正在使用的是其中的哪个版本，此情况下，在安装python组件包时，推荐使用组件包源码进行安装。
-   系统优先使用用户通过Menuconfig所做的配置，如果用户未配置，系统将使用默认配置进行编译。

# 新建APP<a name="ZH-CN_TOPIC_0000001823993873"></a>

-   **[建立源码目录](#ZH-CN_TOPIC_0000001823993869)**  

-   **[开发代码](#ZH-CN_TOPIC_0000001823873917)**  

-   **[镜像烧录](#ZH-CN_TOPIC_0000001777234342)**  

## 建立源码目录<a name="ZH-CN_TOPIC_0000001823993869"></a>

>![](public_sys-resources/icon-note.gif) **说明：** 
>用户可在“application/ws53”同级目录下参考“ws53\_application”目录建立app，以下均以建立“my\_demo”为例。

步骤如下：

1.  新建“application/ws53/my\_demo”目录，用来存放“my\_demo”的源文件。
2.  复制“application/ws53/ws53\_application/CMakeLists.txt”到“application/ws53/my\_demo/CmakeLists.txt”，并将源文件放在“application/ws53/my\_demo”目录下。
3.  修改“application/ws53/my\_demo/CmakeLists.txt”文件。其中各个变量的含义如[表1](#table89969106362)所示。

    **表 1**  组件的CmakeLists.txt中的变量含义

    <a name="table89969106362"></a>
    <table><thead align="left"><tr id="row69971710143612"><th class="cellrowborder" valign="top" width="27.900000000000002%" id="mcps1.2.3.1.1"><p id="p8997181043611"><a name="p8997181043611"></a><a name="p8997181043611"></a>变量名称</p>
    </th>
    <th class="cellrowborder" valign="top" width="72.1%" id="mcps1.2.3.1.2"><p id="p1799771019361"><a name="p1799771019361"></a><a name="p1799771019361"></a>变量含义</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row77088920486"><td class="cellrowborder" valign="top" width="27.900000000000002%" headers="mcps1.2.3.1.1 "><p id="p167083915484"><a name="p167083915484"></a><a name="p167083915484"></a>COMPONENT_NAME</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.1%" headers="mcps1.2.3.1.2 "><p id="p570849194814"><a name="p570849194814"></a><a name="p570849194814"></a>当前组件名称，如“my_demo”。</p>
    </td>
    </tr>
    <tr id="row99971710133619"><td class="cellrowborder" valign="top" width="27.900000000000002%" headers="mcps1.2.3.1.1 "><p id="p199976101361"><a name="p199976101361"></a><a name="p199976101361"></a>SOURCES</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.1%" headers="mcps1.2.3.1.2 "><p id="p499751023618"><a name="p499751023618"></a><a name="p499751023618"></a>当前组件的C文件列表，其中CMAKE_CURRENT_SOURCE_DIR变量标识当前CMakeLists.txt所在的路径。</p>
    </td>
    </tr>
    <tr id="row5997910163618"><td class="cellrowborder" valign="top" width="27.900000000000002%" headers="mcps1.2.3.1.1 "><p id="p129971210143615"><a name="p129971210143615"></a><a name="p129971210143615"></a>PUBLIC_HEADER</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.1%" headers="mcps1.2.3.1.2 "><p id="p69971109360"><a name="p69971109360"></a><a name="p69971109360"></a>当前组件需要对外提供的头文件的路径。</p>
    </td>
    </tr>
    <tr id="row1199791011363"><td class="cellrowborder" valign="top" width="27.900000000000002%" headers="mcps1.2.3.1.1 "><p id="p1699711105364"><a name="p1699711105364"></a><a name="p1699711105364"></a>PRIVATE_HEADER</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.1%" headers="mcps1.2.3.1.2 "><p id="p1799771033615"><a name="p1799771033615"></a><a name="p1799771033615"></a>当前组件内部的头文件搜索路径。</p>
    </td>
    </tr>
    <tr id="row99971610193616"><td class="cellrowborder" valign="top" width="27.900000000000002%" headers="mcps1.2.3.1.1 "><p id="p169971610133618"><a name="p169971610133618"></a><a name="p169971610133618"></a>PRIVATE_DEFINES</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.1%" headers="mcps1.2.3.1.2 "><p id="p14997610103613"><a name="p14997610103613"></a><a name="p14997610103613"></a>当前组件内部生效的宏定义。</p>
    </td>
    </tr>
    <tr id="row12997210203618"><td class="cellrowborder" valign="top" width="27.900000000000002%" headers="mcps1.2.3.1.1 "><p id="p59971910163611"><a name="p59971910163611"></a><a name="p59971910163611"></a>PUBLIC_DEFINES</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.1%" headers="mcps1.2.3.1.2 "><p id="p02671050184018"><a name="p02671050184018"></a><a name="p02671050184018"></a>当前组件需要对外提供的宏定义。</p>
    </td>
    </tr>
    <tr id="row12716914103914"><td class="cellrowborder" valign="top" width="27.900000000000002%" headers="mcps1.2.3.1.1 "><p id="p5717214153911"><a name="p5717214153911"></a><a name="p5717214153911"></a>COMPONENT_PUBLIC_CCFLAGS</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.1%" headers="mcps1.2.3.1.2 "><p id="p14717111473912"><a name="p14717111473912"></a><a name="p14717111473912"></a>当前组件需要对外提供的编译选项。</p>
    </td>
    </tr>
    <tr id="row22992182396"><td class="cellrowborder" valign="top" width="27.900000000000002%" headers="mcps1.2.3.1.1 "><p id="p152993185398"><a name="p152993185398"></a><a name="p152993185398"></a>COMPONENT_CCFLAGS</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.1%" headers="mcps1.2.3.1.2 "><p id="p132991118123913"><a name="p132991118123913"></a><a name="p132991118123913"></a>当前组件内部生效的编译选项。</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  修改“application/ws53/CMakeLists.txt”，将my\_demo目录加入编译。
5.  修改“build/config/target\_config/ws53/config.py”，在ram\_component字段中加入‘my\_demo’，向编译系统中注册my\_demo组件。

## 开发代码<a name="ZH-CN_TOPIC_0000001823873917"></a>

目录结构建立完成后开始启动开发代码（用户可参考“application/samples”进行移植），代码开发完成后即可使用“python3 build.py -c ws53\_liteos\_app -component=my\_demo”编译my\_demo进行代码编译调试。

## 镜像烧录<a name="ZH-CN_TOPIC_0000001777234342"></a>

镜像烧录方法，请参见《WS53V100 BurnTool工具 使用指南》中“操作指南”章节。


