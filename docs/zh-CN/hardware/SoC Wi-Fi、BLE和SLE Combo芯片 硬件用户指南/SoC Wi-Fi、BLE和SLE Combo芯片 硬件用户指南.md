# 前言<a name="ZH-CN_TOPIC_0000001456242676"></a>

**概述<a name="section4537382116410"></a>**

文档主要介绍WS53V100芯片的封装管脚信息、电气特性参数、原理图设计建议、PCB设计建议、热设计建议、焊接工艺、潮敏参数、接口时序、注意事项等内容。

本文主要为技术服务工程师提供硬件设计的参考。

**产品版本<a name="section12266191774710"></a>**

与本文档相对应的产品版本如下。

<a name="table2270181717471"></a>
<table><thead align="left"><tr id="row15364171712479"><th class="cellrowborder" valign="top" width="42.77%" id="mcps1.1.3.1.1"><p id="p123646174478"><a name="p123646174478"></a><a name="p123646174478"></a><strong id="b5942730175717"><a name="b5942730175717"></a><a name="b5942730175717"></a>产品名称</strong></p>
</th>
<th class="cellrowborder" valign="top" width="57.230000000000004%" id="mcps1.1.3.1.2"><p id="p1936401717470"><a name="p1936401717470"></a><a name="p1936401717470"></a><strong id="b1594613304577"><a name="b1594613304577"></a><a name="b1594613304577"></a>产品版本</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row997133615471"><td class="cellrowborder" valign="top" width="42.77%" headers="mcps1.1.3.1.1 "><p id="p1883204951616"><a name="p1883204951616"></a><a name="p1883204951616"></a>WS53</p>
</td>
<td class="cellrowborder" valign="top" width="57.230000000000004%" headers="mcps1.1.3.1.2 "><p id="p897253619477"><a name="p897253619477"></a><a name="p897253619477"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**读者对象<a name="section4378592816410"></a>**

本文档主要适用于以下工程师：

-   单板硬件开发工程师
-   软件工程师
-   技术支持工程师

**符号约定<a name="section133020216410"></a>**

在本文中可能出现下列标志，它们所代表的含义如下。

<a name="table2778843115213"></a>
<table><thead align="left"><tr id="row677894355211"><th class="cellrowborder" valign="top" width="20.580000000000002%" id="mcps1.1.3.1.1"><p id="p1778104315217"><a name="p1778104315217"></a><a name="p1778104315217"></a><strong id="b15778194315217"><a name="b15778194315217"></a><a name="b15778194315217"></a>符号</strong></p>
</th>
<th class="cellrowborder" valign="top" width="79.42%" id="mcps1.1.3.1.2"><p id="p97795439524"><a name="p97795439524"></a><a name="p97795439524"></a><strong id="b197791443195213"><a name="b197791443195213"></a><a name="b197791443195213"></a>说明</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row12779743155210"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p17779184315215"><a name="p17779184315215"></a><a name="p17779184315215"></a><a name="image1577994319522"></a><a name="image1577994319522"></a><span><img class="" id="image1577994319522" height="25.270000000000003" width="55.9265" src="figures/zh-cn_image_0000001505603565.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p87791343185215"><a name="p87791343185215"></a><a name="p87791343185215"></a>表示如不避免则将会导致死亡或严重伤害的具有高等级风险的危害。</p>
</td>
</tr>
<tr id="row97791743205210"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p10779194345220"><a name="p10779194345220"></a><a name="p10779194345220"></a><a name="image67796439522"></a><a name="image67796439522"></a><span><img class="" id="image67796439522" height="25.270000000000003" width="55.9265" src="figures/zh-cn_image_0000001505882589.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p14779443205218"><a name="p14779443205218"></a><a name="p14779443205218"></a>表示如不避免则可能导致死亡或严重伤害的具有中等级风险的危害。</p>
</td>
</tr>
<tr id="row4779184315526"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p7779114315210"><a name="p7779114315210"></a><a name="p7779114315210"></a><a name="image17795435522"></a><a name="image17795435522"></a><span><img class="" id="image17795435522" height="25.270000000000003" width="55.9265" src="figures/zh-cn_image_0000001505722841.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p17779164315214"><a name="p17779164315214"></a><a name="p17779164315214"></a>表示如不避免则可能导致轻微或中度伤害的具有低等级风险的危害。</p>
</td>
</tr>
<tr id="row677924319525"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p8779124315523"><a name="p8779124315523"></a><a name="p8779124315523"></a><a name="image177798438523"></a><a name="image177798438523"></a><span><img class="" id="image177798438523" height="25.270000000000003" width="55.9265" src="figures/zh-cn_image_0000001456082760.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p5779184355211"><a name="p5779184355211"></a><a name="p5779184355211"></a>用于传递设备或环境安全警示信息。如不避免则可能会导致设备损坏、数据丢失、设备性能降低或其它不可预知的结果。</p>
<p id="p18779204305212"><a name="p18779204305212"></a><a name="p18779204305212"></a>“须知”不涉及人身伤害。</p>
</td>
</tr>
<tr id="row137792043195210"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p1277964313522"><a name="p1277964313522"></a><a name="p1277964313522"></a><a name="image577974325215"></a><a name="image577974325215"></a><span><img class="" id="image577974325215" height="15.96" width="47.88" src="figures/zh-cn_image_0000001455922852.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p1877912438522"><a name="p1877912438522"></a><a name="p1877912438522"></a>对正文中重点信息的补充说明。</p>
<p id="p37791843185213"><a name="p37791843185213"></a><a name="p37791843185213"></a>“说明”不是安全警示信息，不涉及人身、设备及环境伤害信息。</p>
</td>
</tr>
</tbody>
</table>

**修改记录<a name="section2467512116410"></a>**

<a name="table1557726816410"></a>
<table><thead align="left"><tr id="row2942532716410"><th class="cellrowborder" valign="top" width="17.86%" id="mcps1.1.4.1.1"><p id="p3778275416410"><a name="p3778275416410"></a><a name="p3778275416410"></a><strong id="b5687322716410"><a name="b5687322716410"></a><a name="b5687322716410"></a>文档版本</strong></p>
</th>
<th class="cellrowborder" valign="top" width="22.720000000000002%" id="mcps1.1.4.1.2"><p id="p5627845516410"><a name="p5627845516410"></a><a name="p5627845516410"></a><strong id="b5800814916410"><a name="b5800814916410"></a><a name="b5800814916410"></a>发布日期</strong></p>
</th>
<th class="cellrowborder" valign="top" width="59.419999999999995%" id="mcps1.1.4.1.3"><p id="p2382284816410"><a name="p2382284816410"></a><a name="p2382284816410"></a><strong id="b3316380216410"><a name="b3316380216410"></a><a name="b3316380216410"></a>修改说明</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row11718493355"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.4.1.1 "><p id="p141704914352"><a name="p141704914352"></a><a name="p141704914352"></a>05</p>
</td>
<td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.1.4.1.2 "><p id="p131711497352"><a name="p131711497352"></a><a name="p131711497352"></a>2026-07-01</p>
</td>
<td class="cellrowborder" valign="top" width="59.419999999999995%" headers="mcps1.1.4.1.3 "><a name="ul3737112369"></a><a name="ul3737112369"></a><ul id="ul3737112369"><li>更新“<a href="#ZH-CN_TOPIC_0000001505842465">GPIO接口</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001505722809">极限工作电压</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001456242628">推荐工作条件</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001505842481">小系统设计建议</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001505842493">控制信号及低功耗应用参考设计</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001505882549">UART接口时序</a>”小节内容。</li></ul>
</td>
</tr>
<tr id="row11725379488"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.4.1.1 "><p id="p197273734818"><a name="p197273734818"></a><a name="p197273734818"></a>04</p>
</td>
<td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.1.4.1.2 "><p id="p147212374484"><a name="p147212374484"></a><a name="p147212374484"></a>2025-05-28</p>
</td>
<td class="cellrowborder" valign="top" width="59.419999999999995%" headers="mcps1.1.4.1.3 "><p id="p1316414810512"><a name="p1316414810512"></a><a name="p1316414810512"></a>更新“<a href="#ZH-CN_TOPIC_0000001455922820">ADC接口参考设计</a>”小节内容。</p>
</td>
</tr>
<tr id="row12911114210403"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.4.1.1 "><p id="p691144254010"><a name="p691144254010"></a><a name="p691144254010"></a>03</p>
</td>
<td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.1.4.1.2 "><p id="p14911124244016"><a name="p14911124244016"></a><a name="p14911124244016"></a>2025-01-24</p>
</td>
<td class="cellrowborder" valign="top" width="59.419999999999995%" headers="mcps1.1.4.1.3 "><a name="ul193812040152910"></a><a name="ul193812040152910"></a><ul id="ul193812040152910"><li>更新“<a href="#ZH-CN_TOPIC_0000001456242648">管脚分布</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001456082732">管脚排列表</a>”、“<a href="#ZH-CN_TOPIC_0000001505842465">GPIO接口</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001505722809">极限工作电压</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000002018433230">RTC时钟</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001455763072">SDIO接口参考设计</a>”、“<a href="#ZH-CN_TOPIC_0000001455922820">ADC接口参考设计</a>”小节内容。</li></ul>
</td>
</tr>
<tr id="row182171239114317"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.4.1.1 "><p id="p1821713392438"><a name="p1821713392438"></a><a name="p1821713392438"></a>02</p>
</td>
<td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.1.4.1.2 "><p id="p9217539114314"><a name="p9217539114314"></a><a name="p9217539114314"></a>2024-09-13</p>
</td>
<td class="cellrowborder" valign="top" width="59.419999999999995%" headers="mcps1.1.4.1.3 "><a name="ul941322310449"></a><a name="ul941322310449"></a><ul id="ul941322310449"><li>更新“<a href="#ZH-CN_TOPIC_0000001456242644">GPIO复用管脚</a>”小节内容。</li><li>新增“<a href="#ZH-CN_TOPIC_0000002018433230">RTC时钟</a>”小节内容。</li></ul>
</td>
</tr>
<tr id="row1327439191611"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.4.1.1 "><p id="p62742931614"><a name="p62742931614"></a><a name="p62742931614"></a>01</p>
</td>
<td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.1.4.1.2 "><p id="p4274109151615"><a name="p4274109151615"></a><a name="p4274109151615"></a>2024-08-08</p>
</td>
<td class="cellrowborder" valign="top" width="59.419999999999995%" headers="mcps1.1.4.1.3 "><p id="p5274096163"><a name="p5274096163"></a><a name="p5274096163"></a>第一次正式版本发布。</p>
<a name="ul144687409162"></a><a name="ul144687409162"></a><ul id="ul144687409162"><li>更新“<a href="#ZH-CN_TOPIC_0000001505603517">外围接口设计建议</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001505882545">SDIO时序</a>”小节内容。</li></ul>
</td>
</tr>
<tr id="row1015111120324"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.4.1.1 "><p id="p1151101118328"><a name="p1151101118328"></a><a name="p1151101118328"></a>00B05</p>
</td>
<td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.1.4.1.2 "><p id="p1115131112327"><a name="p1115131112327"></a><a name="p1115131112327"></a>2024-07-15</p>
</td>
<td class="cellrowborder" valign="top" width="59.419999999999995%" headers="mcps1.1.4.1.3 "><a name="ul15404208321"></a><a name="ul15404208321"></a><ul id="ul15404208321"><li>更新“<a href="#ZH-CN_TOPIC_0000001505842465">GPIO接口</a>”、“<a href="#ZH-CN_TOPIC_0000001456242644">GPIO复用管脚</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001505603557">上电关键硬件字</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001505842481">小系统设计建议</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001505603517">外围接口设计建议</a>”、小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001505842493">控制信号及低功耗应用参考设计</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001505882573">DBB布线指导</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001505882549">UART接口时序</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001505882545">SDIO时序</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001456242632">硬件设计</a>”小节内容。</li></ul>
</td>
</tr>
<tr id="row19662103365814"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.4.1.1 "><p id="p26632333584"><a name="p26632333584"></a><a name="p26632333584"></a>00B04</p>
</td>
<td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.1.4.1.2 "><p id="p4663133318581"><a name="p4663133318581"></a><a name="p4663133318581"></a>2024-06-11</p>
</td>
<td class="cellrowborder" valign="top" width="59.419999999999995%" headers="mcps1.1.4.1.3 "><a name="ul37618476587"></a><a name="ul37618476587"></a><ul id="ul37618476587"><li>更新“<a href="#ZH-CN_TOPIC_0000001456242644">GPIO复用管脚</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001505603557">上电关键硬件字</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001456082748">复位电路</a>”小节内容。</li></ul>
</td>
</tr>
<tr id="row129014382147"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.4.1.1 "><p id="p17902838141420"><a name="p17902838141420"></a><a name="p17902838141420"></a>00B03</p>
</td>
<td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.1.4.1.2 "><p id="p189021138131410"><a name="p189021138131410"></a><a name="p189021138131410"></a>2024-05-11</p>
</td>
<td class="cellrowborder" valign="top" width="59.419999999999995%" headers="mcps1.1.4.1.3 "><a name="ul1218505291416"></a><a name="ul1218505291416"></a><ul id="ul1218505291416"><li>更新“<a href="#ZH-CN_TOPIC_0000001505842485">参考时钟设计</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001456082736">注意事项</a>”小节内容。</li></ul>
</td>
</tr>
<tr id="row166559578114"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.4.1.1 "><p id="p165685716113"><a name="p165685716113"></a><a name="p165685716113"></a>00B02</p>
</td>
<td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.1.4.1.2 "><p id="p1465616572015"><a name="p1465616572015"></a><a name="p1465616572015"></a>2024-04-07</p>
</td>
<td class="cellrowborder" valign="top" width="59.419999999999995%" headers="mcps1.1.4.1.3 "><a name="ul68671103211"></a><a name="ul68671103211"></a><ul id="ul68671103211"><li>更新“<a href="#ZH-CN_TOPIC_0000001505722821">封装与管脚分布</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001456242644">GPIO复用管脚</a>”小节内容。</li><li>更新“<a href="#ZH-CN_TOPIC_0000001505842485">参考时钟设计</a>”小节内容。</li></ul>
</td>
</tr>
<tr id="row5947359616410"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.4.1.1 "><p id="p2149706016410"><a name="p2149706016410"></a><a name="p2149706016410"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.1.4.1.2 "><p id="p648803616410"><a name="p648803616410"></a><a name="p648803616410"></a>2024-01-04</p>
</td>
<td class="cellrowborder" valign="top" width="59.419999999999995%" headers="mcps1.1.4.1.3 "><p id="p1946537916410"><a name="p1946537916410"></a><a name="p1946537916410"></a>第一次临时版本发布。</p>
</td>
</tr>
</tbody>
</table>

# 封装与管脚<a name="ZH-CN_TOPIC_0000001455922800"></a>

-   **[封装与管脚分布](#ZH-CN_TOPIC_0000001505722821)**  

-   **[管脚描述](#ZH-CN_TOPIC_0000001455922816)**  

-   **[上电关键硬件字](#ZH-CN_TOPIC_0000001505603557)**  

## 封装与管脚分布<a name="ZH-CN_TOPIC_0000001505722821"></a>

-   **[封装](#ZH-CN_TOPIC_0000001455922796)**  

-   **[管脚分布](#ZH-CN_TOPIC_0000001456242648)**  

### 封装<a name="ZH-CN_TOPIC_0000001455922796"></a>

WS53V100芯片采用QFN52封装，封装尺寸为6mm×6mm，管脚间距为0.4mm，详细封装如[图1](#fig381817005920)、[图2](#toc6995721)和[图3](#toc6995723)所示。

**图 1**  芯片封装顶视图<a name="fig381817005920"></a>  
![](figures/芯片封装顶视图.png "芯片封装顶视图")

**图 2**  芯片封装底视图<a name="toc6995721"></a>  
![](figures/芯片封装底视图.png "芯片封装底视图")

**图 3**  芯片侧面放大图<a name="toc6995723"></a>  
![](figures/芯片侧面放大图.png "芯片侧面放大图")

芯片封装尺寸参数如[表1](#table592793102013)所示。

**表 1**  芯片封装参数说明表

<a name="table592793102013"></a>
<table><thead align="left"><tr id="row13060411200"><th class="cellrowborder" valign="top" id="mcps1.2.8.1.1"><p id="p103061746207"><a name="p103061746207"></a><a name="p103061746207"></a>参数</p>
</th>
<th class="cellrowborder" colspan="3" valign="top" id="mcps1.2.8.1.2"><p id="p5306154172019"><a name="p5306154172019"></a><a name="p5306154172019"></a>尺寸（mm）</p>
</th>
<th class="cellrowborder" colspan="3" valign="top" id="mcps1.2.8.1.3"><p id="p63068410202"><a name="p63068410202"></a><a name="p63068410202"></a>尺寸（inch）</p>
</th>
</tr>
</thead>
<tbody><tr id="row773312305515"><td class="cellrowborder" valign="top" width="14.612922584516905%" headers="mcps1.2.8.1.1 "><p id="p16735433551"><a name="p16735433551"></a><a name="p16735433551"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="14.052810562112422%" headers="mcps1.2.8.1.2 "><p id="p23058103555"><a name="p23058103555"></a><a name="p23058103555"></a>最小值</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.2 "><p id="p3305141018554"><a name="p3305141018554"></a><a name="p3305141018554"></a>典型值</p>
</td>
<td class="cellrowborder" valign="top" width="14.32286457291458%" headers="mcps1.2.8.1.2 "><p id="p23051710125513"><a name="p23051710125513"></a><a name="p23051710125513"></a>最大值</p>
</td>
<td class="cellrowborder" valign="top" width="14.012802560512103%" headers="mcps1.2.8.1.3 "><p id="p1030514103554"><a name="p1030514103554"></a><a name="p1030514103554"></a>最小值</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p123051104555"><a name="p123051104555"></a><a name="p123051104555"></a>典型值</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p1730581013558"><a name="p1730581013558"></a><a name="p1730581013558"></a>最大值</p>
</td>
</tr>
<tr id="row83061482016"><td class="cellrowborder" valign="top" width="14.612922584516905%" headers="mcps1.2.8.1.1 "><p id="p13306946204"><a name="p13306946204"></a><a name="p13306946204"></a>A</p>
</td>
<td class="cellrowborder" valign="top" width="14.052810562112422%" headers="mcps1.2.8.1.2 "><p id="p1398165414514"><a name="p1398165414514"></a><a name="p1398165414514"></a>0.80</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.2 "><p id="p19811254658"><a name="p19811254658"></a><a name="p19811254658"></a>0.85</p>
</td>
<td class="cellrowborder" valign="top" width="14.32286457291458%" headers="mcps1.2.8.1.2 "><p id="p19811354953"><a name="p19811354953"></a><a name="p19811354953"></a>0.90</p>
</td>
<td class="cellrowborder" valign="top" width="14.012802560512103%" headers="mcps1.2.8.1.3 "><p id="p1972511326392"><a name="p1972511326392"></a><a name="p1972511326392"></a>0.031</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p8725163233918"><a name="p8725163233918"></a><a name="p8725163233918"></a>0.033</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p4725133212392"><a name="p4725133212392"></a><a name="p4725133212392"></a>0.035</p>
</td>
</tr>
<tr id="row73077414205"><td class="cellrowborder" valign="top" width="14.612922584516905%" headers="mcps1.2.8.1.1 "><p id="p530714410206"><a name="p530714410206"></a><a name="p530714410206"></a>A1</p>
</td>
<td class="cellrowborder" valign="top" width="14.052810562112422%" headers="mcps1.2.8.1.2 "><p id="p14980754255"><a name="p14980754255"></a><a name="p14980754255"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.2 "><p id="p998018541857"><a name="p998018541857"></a><a name="p998018541857"></a>0.02</p>
</td>
<td class="cellrowborder" valign="top" width="14.32286457291458%" headers="mcps1.2.8.1.2 "><p id="p5979105413513"><a name="p5979105413513"></a><a name="p5979105413513"></a>0.05</p>
</td>
<td class="cellrowborder" valign="top" width="14.012802560512103%" headers="mcps1.2.8.1.3 "><p id="p372573233910"><a name="p372573233910"></a><a name="p372573233910"></a>0.000</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p472583253918"><a name="p472583253918"></a><a name="p472583253918"></a>0.001</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p672515329390"><a name="p672515329390"></a><a name="p672515329390"></a>0.002</p>
</td>
</tr>
<tr id="row103073411202"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p103074462013"><a name="p103074462013"></a><a name="p103074462013"></a>A3</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.2 "><p id="p297717541650"><a name="p297717541650"></a><a name="p297717541650"></a>0.203REF</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.3 "><p id="p672533218398"><a name="p672533218398"></a><a name="p672533218398"></a>0.008REF</p>
</td>
</tr>
<tr id="row103074420202"><td class="cellrowborder" valign="top" width="14.612922584516905%" headers="mcps1.2.8.1.1 "><p id="p133076411205"><a name="p133076411205"></a><a name="p133076411205"></a>b</p>
</td>
<td class="cellrowborder" valign="top" width="14.052810562112422%" headers="mcps1.2.8.1.2 "><p id="p109760545518"><a name="p109760545518"></a><a name="p109760545518"></a>0.15</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.2 "><p id="p2097665416518"><a name="p2097665416518"></a><a name="p2097665416518"></a>0.20</p>
</td>
<td class="cellrowborder" valign="top" width="14.32286457291458%" headers="mcps1.2.8.1.2 "><p id="p89761954059"><a name="p89761954059"></a><a name="p89761954059"></a>0.25</p>
</td>
<td class="cellrowborder" valign="top" width="14.012802560512103%" headers="mcps1.2.8.1.3 "><p id="p9725173219399"><a name="p9725173219399"></a><a name="p9725173219399"></a>0.006</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p177251432183911"><a name="p177251432183911"></a><a name="p177251432183911"></a>0.008</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p4725432103911"><a name="p4725432103911"></a><a name="p4725432103911"></a>0.010</p>
</td>
</tr>
<tr id="row136413716306"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1364115716305"><a name="p1364115716305"></a><a name="p1364115716305"></a>b1</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.2 "><p id="p11561181716300"><a name="p11561181716300"></a><a name="p11561181716300"></a>0.14REF</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.3 "><p id="p3725133223918"><a name="p3725133223918"></a><a name="p3725133223918"></a>0.006REF</p>
</td>
</tr>
<tr id="row13084482013"><td class="cellrowborder" valign="top" width="14.612922584516905%" headers="mcps1.2.8.1.1 "><p id="p9308194132017"><a name="p9308194132017"></a><a name="p9308194132017"></a>D</p>
</td>
<td class="cellrowborder" valign="top" width="14.052810562112422%" headers="mcps1.2.8.1.2 "><p id="p1997515417517"><a name="p1997515417517"></a><a name="p1997515417517"></a>5.93</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.2 "><p id="p1997417541510"><a name="p1997417541510"></a><a name="p1997417541510"></a>6.00</p>
</td>
<td class="cellrowborder" valign="top" width="14.32286457291458%" headers="mcps1.2.8.1.2 "><p id="p797410541511"><a name="p797410541511"></a><a name="p797410541511"></a>6.07</p>
</td>
<td class="cellrowborder" valign="top" width="14.012802560512103%" headers="mcps1.2.8.1.3 "><p id="p47259327395"><a name="p47259327395"></a><a name="p47259327395"></a>0.233</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p6725432193919"><a name="p6725432193919"></a><a name="p6725432193919"></a>0.236</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p67251232123910"><a name="p67251232123910"></a><a name="p67251232123910"></a>0.239</p>
</td>
</tr>
<tr id="row630818492014"><td class="cellrowborder" valign="top" width="14.612922584516905%" headers="mcps1.2.8.1.1 "><p id="p7308114122012"><a name="p7308114122012"></a><a name="p7308114122012"></a>E</p>
</td>
<td class="cellrowborder" valign="top" width="14.052810562112422%" headers="mcps1.2.8.1.2 "><p id="p2244726131417"><a name="p2244726131417"></a><a name="p2244726131417"></a>5.93</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.2 "><p id="p1724417266140"><a name="p1724417266140"></a><a name="p1724417266140"></a>6.00</p>
</td>
<td class="cellrowborder" valign="top" width="14.32286457291458%" headers="mcps1.2.8.1.2 "><p id="p3245192671410"><a name="p3245192671410"></a><a name="p3245192671410"></a>6.07</p>
</td>
<td class="cellrowborder" valign="top" width="14.012802560512103%" headers="mcps1.2.8.1.3 "><p id="p1572517326393"><a name="p1572517326393"></a><a name="p1572517326393"></a>0.233</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p1772573219395"><a name="p1772573219395"></a><a name="p1772573219395"></a>0.236</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p1872553215395"><a name="p1872553215395"></a><a name="p1872553215395"></a>0.239</p>
</td>
</tr>
<tr id="row17308245205"><td class="cellrowborder" valign="top" width="14.612922584516905%" headers="mcps1.2.8.1.1 "><p id="p2308447205"><a name="p2308447205"></a><a name="p2308447205"></a>D2</p>
</td>
<td class="cellrowborder" valign="top" width="14.052810562112422%" headers="mcps1.2.8.1.2 "><p id="p2097265416512"><a name="p2097265416512"></a><a name="p2097265416512"></a>3.70</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.2 "><p id="p15972105418513"><a name="p15972105418513"></a><a name="p15972105418513"></a>3.80</p>
</td>
<td class="cellrowborder" valign="top" width="14.32286457291458%" headers="mcps1.2.8.1.2 "><p id="p39715541957"><a name="p39715541957"></a><a name="p39715541957"></a>3.90</p>
</td>
<td class="cellrowborder" valign="top" width="14.012802560512103%" headers="mcps1.2.8.1.3 "><p id="p15725123293912"><a name="p15725123293912"></a><a name="p15725123293912"></a>0.146</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p7725173223917"><a name="p7725173223917"></a><a name="p7725173223917"></a>0.150</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p11725332103920"><a name="p11725332103920"></a><a name="p11725332103920"></a>0.154</p>
</td>
</tr>
<tr id="row11309194202019"><td class="cellrowborder" valign="top" width="14.612922584516905%" headers="mcps1.2.8.1.1 "><p id="p14309741205"><a name="p14309741205"></a><a name="p14309741205"></a>E2</p>
</td>
<td class="cellrowborder" valign="top" width="14.052810562112422%" headers="mcps1.2.8.1.2 "><p id="p1983716492149"><a name="p1983716492149"></a><a name="p1983716492149"></a>3.70</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.2 "><p id="p138371549111418"><a name="p138371549111418"></a><a name="p138371549111418"></a>3.80</p>
</td>
<td class="cellrowborder" valign="top" width="14.32286457291458%" headers="mcps1.2.8.1.2 "><p id="p1183734914148"><a name="p1183734914148"></a><a name="p1183734914148"></a>3.90</p>
</td>
<td class="cellrowborder" valign="top" width="14.012802560512103%" headers="mcps1.2.8.1.3 "><p id="p1172503214395"><a name="p1172503214395"></a><a name="p1172503214395"></a>0.146</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p15725032123910"><a name="p15725032123910"></a><a name="p15725032123910"></a>0.150</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p972563263917"><a name="p972563263917"></a><a name="p972563263917"></a>0.154</p>
</td>
</tr>
<tr id="row153107412017"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p73101040205"><a name="p73101040205"></a><a name="p73101040205"></a>e</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.2 "><p id="p11969854353"><a name="p11969854353"></a><a name="p11969854353"></a>0.40BSC</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.3 "><p id="p272573263912"><a name="p272573263912"></a><a name="p272573263912"></a>0.016BSC</p>
</td>
</tr>
<tr id="row13552022133120"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p165592243114"><a name="p165592243114"></a><a name="p165592243114"></a>Nd</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.2 "><p id="p16540143116317"><a name="p16540143116317"></a><a name="p16540143116317"></a>4.80BSC</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.3 "><p id="p1872623211394"><a name="p1872623211394"></a><a name="p1872623211394"></a>0.189BSC</p>
</td>
</tr>
<tr id="row929014176324"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p02906171325"><a name="p02906171325"></a><a name="p02906171325"></a>Ne</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.2 "><p id="p72031621183211"><a name="p72031621183211"></a><a name="p72031621183211"></a>4.80BSC</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.3 "><p id="p12726632183919"><a name="p12726632183919"></a><a name="p12726632183919"></a>0.189BSC</p>
</td>
</tr>
<tr id="row2310194172018"><td class="cellrowborder" valign="top" width="14.612922584516905%" headers="mcps1.2.8.1.1 "><p id="p173104422016"><a name="p173104422016"></a><a name="p173104422016"></a>L</p>
</td>
<td class="cellrowborder" valign="top" width="14.052810562112422%" headers="mcps1.2.8.1.2 "><p id="p1096815542510"><a name="p1096815542510"></a><a name="p1096815542510"></a>0.35</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.2 "><p id="p596811541251"><a name="p596811541251"></a><a name="p596811541251"></a>0.40</p>
</td>
<td class="cellrowborder" valign="top" width="14.32286457291458%" headers="mcps1.2.8.1.2 "><p id="p1696811541650"><a name="p1696811541650"></a><a name="p1696811541650"></a>0.45</p>
</td>
<td class="cellrowborder" valign="top" width="14.012802560512103%" headers="mcps1.2.8.1.3 "><p id="p1272693214393"><a name="p1272693214393"></a><a name="p1272693214393"></a>0.014</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p1172653263910"><a name="p1172653263910"></a><a name="p1172653263910"></a>0.016</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p17726183214393"><a name="p17726183214393"></a><a name="p17726183214393"></a>0.018</p>
</td>
</tr>
<tr id="row415954413323"><td class="cellrowborder" valign="top" width="14.612922584516905%" headers="mcps1.2.8.1.1 "><p id="p1315934413211"><a name="p1315934413211"></a><a name="p1315934413211"></a>L1</p>
</td>
<td class="cellrowborder" valign="top" width="14.052810562112422%" headers="mcps1.2.8.1.2 "><p id="p11159644203219"><a name="p11159644203219"></a><a name="p11159644203219"></a>0.285</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.2 "><p id="p1415917447329"><a name="p1415917447329"></a><a name="p1415917447329"></a>0.36</p>
</td>
<td class="cellrowborder" valign="top" width="14.32286457291458%" headers="mcps1.2.8.1.2 "><p id="p201595443322"><a name="p201595443322"></a><a name="p201595443322"></a>0.435</p>
</td>
<td class="cellrowborder" valign="top" width="14.012802560512103%" headers="mcps1.2.8.1.3 "><p id="p1372663263917"><a name="p1372663263917"></a><a name="p1372663263917"></a>0.011</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p157268322397"><a name="p157268322397"></a><a name="p157268322397"></a>0.014</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p147261432113910"><a name="p147261432113910"></a><a name="p147261432113910"></a>0.017</p>
</td>
</tr>
<tr id="row359928123313"><td class="cellrowborder" valign="top" width="14.612922584516905%" headers="mcps1.2.8.1.1 "><p id="p1959915863318"><a name="p1959915863318"></a><a name="p1959915863318"></a>L2</p>
</td>
<td class="cellrowborder" valign="top" width="14.052810562112422%" headers="mcps1.2.8.1.2 "><p id="p65991384337"><a name="p65991384337"></a><a name="p65991384337"></a>0.105</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.2 "><p id="p195991788330"><a name="p195991788330"></a><a name="p195991788330"></a>0.18</p>
</td>
<td class="cellrowborder" valign="top" width="14.32286457291458%" headers="mcps1.2.8.1.2 "><p id="p359916812336"><a name="p359916812336"></a><a name="p359916812336"></a>0.255</p>
</td>
<td class="cellrowborder" valign="top" width="14.012802560512103%" headers="mcps1.2.8.1.3 "><p id="p9726123213391"><a name="p9726123213391"></a><a name="p9726123213391"></a>0.004</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p1572643223917"><a name="p1572643223917"></a><a name="p1572643223917"></a>0.007</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p157261632153913"><a name="p157261632153913"></a><a name="p157261632153913"></a>0.010</p>
</td>
</tr>
<tr id="row1495393973319"><td class="cellrowborder" valign="top" width="14.612922584516905%" headers="mcps1.2.8.1.1 "><p id="p795312393331"><a name="p795312393331"></a><a name="p795312393331"></a>h</p>
</td>
<td class="cellrowborder" valign="top" width="14.052810562112422%" headers="mcps1.2.8.1.2 "><p id="p2095311395333"><a name="p2095311395333"></a><a name="p2095311395333"></a>0.30</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.2 "><p id="p1995313914330"><a name="p1995313914330"></a><a name="p1995313914330"></a>0.35</p>
</td>
<td class="cellrowborder" valign="top" width="14.32286457291458%" headers="mcps1.2.8.1.2 "><p id="p4953183911332"><a name="p4953183911332"></a><a name="p4953183911332"></a>0.40</p>
</td>
<td class="cellrowborder" valign="top" width="14.012802560512103%" headers="mcps1.2.8.1.3 "><p id="p20726103243910"><a name="p20726103243910"></a><a name="p20726103243910"></a>0.012</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p472603213390"><a name="p472603213390"></a><a name="p472603213390"></a>0.014</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p167263326393"><a name="p167263326393"></a><a name="p167263326393"></a>0.016</p>
</td>
</tr>
<tr id="row516343151518"><td class="cellrowborder" valign="top" width="14.612922584516905%" headers="mcps1.2.8.1.1 "><p id="p517124311158"><a name="p517124311158"></a><a name="p517124311158"></a>K</p>
</td>
<td class="cellrowborder" valign="top" width="14.052810562112422%" headers="mcps1.2.8.1.2 "><p id="p19171543121518"><a name="p19171543121518"></a><a name="p19171543121518"></a>0.60</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.2 "><p id="p10171843151515"><a name="p10171843151515"></a><a name="p10171843151515"></a>0.70</p>
</td>
<td class="cellrowborder" valign="top" width="14.32286457291458%" headers="mcps1.2.8.1.2 "><p id="p917184316151"><a name="p917184316151"></a><a name="p917184316151"></a>0.80</p>
</td>
<td class="cellrowborder" valign="top" width="14.012802560512103%" headers="mcps1.2.8.1.3 "><p id="p12726163218396"><a name="p12726163218396"></a><a name="p12726163218396"></a>0.024</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p3726193213918"><a name="p3726193213918"></a><a name="p3726193213918"></a>0.028</p>
</td>
<td class="cellrowborder" valign="top" width="14.332866573314664%" headers="mcps1.2.8.1.3 "><p id="p1672673273912"><a name="p1672673273912"></a><a name="p1672673273912"></a>0.031</p>
</td>
</tr>
<tr id="row2312842203"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p4312248201"><a name="p4312248201"></a><a name="p4312248201"></a>aaa</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.2 "><p id="p159655544517"><a name="p159655544517"></a><a name="p159655544517"></a>0.10</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.3 "><p id="p127261432173919"><a name="p127261432173919"></a><a name="p127261432173919"></a>0.004</p>
</td>
</tr>
<tr id="row123126411207"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1931210411205"><a name="p1931210411205"></a><a name="p1931210411205"></a>bbb</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.2 "><p id="p1496413541459"><a name="p1496413541459"></a><a name="p1496413541459"></a>0.07</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.3 "><p id="p14726432153918"><a name="p14726432153918"></a><a name="p14726432153918"></a>0.003</p>
</td>
</tr>
<tr id="row9312144207"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p133127412011"><a name="p133127412011"></a><a name="p133127412011"></a>ccc</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.2 "><p id="p11963654853"><a name="p11963654853"></a><a name="p11963654853"></a>0.10</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.3 "><p id="p13726153233913"><a name="p13726153233913"></a><a name="p13726153233913"></a>0.004</p>
</td>
</tr>
<tr id="row53131348206"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1131320411208"><a name="p1131320411208"></a><a name="p1131320411208"></a>ddd</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.2 "><p id="p79638544513"><a name="p79638544513"></a><a name="p79638544513"></a>0.05</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.3 "><p id="p5726163263918"><a name="p5726163263918"></a><a name="p5726163263918"></a>0.002</p>
</td>
</tr>
<tr id="row1831364142018"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1631314415208"><a name="p1631314415208"></a><a name="p1631314415208"></a>eee</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.2 "><p id="p129625541251"><a name="p129625541251"></a><a name="p129625541251"></a>0.08</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.3 "><p id="p167262323395"><a name="p167262323395"></a><a name="p167262323395"></a>0.003</p>
</td>
</tr>
<tr id="row103139411202"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p163136414207"><a name="p163136414207"></a><a name="p163136414207"></a>fff</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.2 "><p id="p2961135412516"><a name="p2961135412516"></a><a name="p2961135412516"></a>0.10</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.8.1.3 "><p id="p7726163216398"><a name="p7726163216398"></a><a name="p7726163216398"></a>0.004</p>
</td>
</tr>
</tbody>
</table>

### 管脚分布<a name="ZH-CN_TOPIC_0000001456242648"></a>

WS53V100芯片管脚分布如[图1](#fig1269775433017)所示。

**图 1**  WS53V100芯片TOP View管脚分布图<a name="fig1269775433017"></a>  
![](figures/WS53V100芯片TOP-View管脚分布图.png "WS53V100芯片TOP-View管脚分布图")

**表 1**  WS53V100关键特性

<a name="table17413191619910"></a>
<table><thead align="left"><tr id="row19413116596"><th class="cellrowborder" valign="top" width="50.57000000000001%" id="mcps1.2.3.1.1"><p id="p194137167915"><a name="p194137167915"></a><a name="p194137167915"></a>芯片</p>
</th>
<th class="cellrowborder" valign="top" width="49.43%" id="mcps1.2.3.1.2"><p id="p2041321611910"><a name="p2041321611910"></a><a name="p2041321611910"></a>是否支持FLASH</p>
</th>
</tr>
</thead>
<tbody><tr id="row1136643410916"><td class="cellrowborder" valign="top" width="50.57000000000001%" headers="mcps1.2.3.1.1 "><p id="p1036713342915"><a name="p1036713342915"></a><a name="p1036713342915"></a>WS53V100</p>
</td>
<td class="cellrowborder" valign="top" width="49.43%" headers="mcps1.2.3.1.2 "><p id="p32280571112"><a name="p32280571112"></a><a name="p32280571112"></a>内置4MB FLASH</p>
</td>
</tr>
</tbody>
</table>

## 管脚描述<a name="ZH-CN_TOPIC_0000001455922816"></a>

-   **[管脚类型说明](#ZH-CN_TOPIC_0000001505882557)**  

-   **[管脚排列表](#ZH-CN_TOPIC_0000001456082732)**  

-   **[全芯片复位接口](#ZH-CN_TOPIC_0000001505603513)**  

-   **[GPIO接口](#ZH-CN_TOPIC_0000001505842465)**  

-   **[电源管脚](#ZH-CN_TOPIC_0000001505842477)**  

-   **[RF接口](#ZH-CN_TOPIC_0000001456082744)**  

-   **[GND管脚](#ZH-CN_TOPIC_0000001505842473)**  

-   **[GPIO复用管脚](#ZH-CN_TOPIC_0000001456242644)**  

-   **[CLK管脚](#ZH-CN_TOPIC_0000001505722833)**  

### 管脚类型说明<a name="ZH-CN_TOPIC_0000001505882557"></a>

管脚I/O类型说明如[表1](#table24429894)所示。

**表 1**  管脚I/O类型说明

<a name="table24429894"></a>
<table><thead align="left"><tr id="row27904713"><th class="cellrowborder" valign="top" width="27.27%" id="mcps1.2.3.1.1"><p id="p45689312"><a name="p45689312"></a><a name="p45689312"></a>I/O</p>
</th>
<th class="cellrowborder" valign="top" width="72.72999999999999%" id="mcps1.2.3.1.2"><p id="p9846754"><a name="p9846754"></a><a name="p9846754"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row59389625"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p45830349"><a name="p45830349"></a><a name="p45830349"></a>I</p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p21270789"><a name="p21270789"></a><a name="p21270789"></a>输入信号。</p>
</td>
</tr>
<tr id="row57219378"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p4258076"><a name="p4258076"></a><a name="p4258076"></a>I<sub id="sub109481494917"><a name="sub109481494917"></a><a name="sub109481494917"></a>PD</sub></p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p17130265"><a name="p17130265"></a><a name="p17130265"></a>输入信号，内部下拉。</p>
</td>
</tr>
<tr id="row19954658"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p5714573"><a name="p5714573"></a><a name="p5714573"></a>I<sub id="sub794811491913"><a name="sub794811491913"></a><a name="sub794811491913"></a>PU</sub></p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p5174549"><a name="p5174549"></a><a name="p5174549"></a>输入信号，内部上拉。</p>
</td>
</tr>
<tr id="row46570941"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p14149906"><a name="p14149906"></a><a name="p14149906"></a>I<sub id="sub119488497917"><a name="sub119488497917"></a><a name="sub119488497917"></a>S</sub></p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p47625841"><a name="p47625841"></a><a name="p47625841"></a>输入信号，带施密特触发器。</p>
</td>
</tr>
<tr id="row25979390"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p23955812"><a name="p23955812"></a><a name="p23955812"></a>I<sub id="sub194814918912"><a name="sub194814918912"></a><a name="sub194814918912"></a>SPD</sub></p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p15482662"><a name="p15482662"></a><a name="p15482662"></a>输入信号，带施密特触发器，内部下拉。</p>
</td>
</tr>
<tr id="row5126234"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p12571834"><a name="p12571834"></a><a name="p12571834"></a>I<sub id="sub2948449098"><a name="sub2948449098"></a><a name="sub2948449098"></a>SPU</sub></p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p38061996"><a name="p38061996"></a><a name="p38061996"></a>输入信号，带施密特触发器，内部上垃。</p>
</td>
</tr>
<tr id="row7013644"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p31234253"><a name="p31234253"></a><a name="p31234253"></a>O</p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p46946559"><a name="p46946559"></a><a name="p46946559"></a>输出信号。</p>
</td>
</tr>
<tr id="row19865849"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p65629975"><a name="p65629975"></a><a name="p65629975"></a>O<sub id="sub1394815499914"><a name="sub1394815499914"></a><a name="sub1394815499914"></a>OD</sub></p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p62741064"><a name="p62741064"></a><a name="p62741064"></a>输出，漏极开路。</p>
</td>
</tr>
<tr id="row27798664"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p37099307"><a name="p37099307"></a><a name="p37099307"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p52253899"><a name="p52253899"></a><a name="p52253899"></a>双向输入/输出信号。</p>
</td>
</tr>
<tr id="row523045"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p42366666"><a name="p42366666"></a><a name="p42366666"></a>I<sub id="sub1694818495915"><a name="sub1694818495915"></a><a name="sub1694818495915"></a>PD</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p15222565"><a name="p15222565"></a><a name="p15222565"></a>双向，输入下拉。</p>
</td>
</tr>
<tr id="row2785358"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p24287485"><a name="p24287485"></a><a name="p24287485"></a>I<sub id="sub119497498913"><a name="sub119497498913"></a><a name="sub119497498913"></a>PU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p55945983"><a name="p55945983"></a><a name="p55945983"></a>双向，输入上拉。</p>
</td>
</tr>
<tr id="row33751805"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p49541661"><a name="p49541661"></a><a name="p49541661"></a>I<sub id="sub189498491917"><a name="sub189498491917"></a><a name="sub189498491917"></a>SPD</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p11302482"><a name="p11302482"></a><a name="p11302482"></a>双向，输入下拉，带施密特触发器。</p>
</td>
</tr>
<tr id="row34613479"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p52228449"><a name="p52228449"></a><a name="p52228449"></a>I<sub id="sub69491249197"><a name="sub69491249197"></a><a name="sub69491249197"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p23814038"><a name="p23814038"></a><a name="p23814038"></a>双向，输入上拉，带施密特触发器。</p>
</td>
</tr>
<tr id="row12999751"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p46346882"><a name="p46346882"></a><a name="p46346882"></a>I<sub id="sub1594920497918"><a name="sub1594920497918"></a><a name="sub1594920497918"></a>PD</sub>/O<sub id="sub1594919491297"><a name="sub1594919491297"></a><a name="sub1594919491297"></a>OD</sub></p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p11633618"><a name="p11633618"></a><a name="p11633618"></a>双向，输入下拉，输出漏极开路。</p>
</td>
</tr>
<tr id="row37593705"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p25191285"><a name="p25191285"></a><a name="p25191285"></a>I<sub id="sub1794911497914"><a name="sub1794911497914"></a><a name="sub1794911497914"></a>PU</sub>/O<sub id="sub109490499912"><a name="sub109490499912"></a><a name="sub109490499912"></a>OD</sub></p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p58003675"><a name="p58003675"></a><a name="p58003675"></a>双向，输入上拉，输出漏极开路。</p>
</td>
</tr>
<tr id="row52271033"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p6095280"><a name="p6095280"></a><a name="p6095280"></a>I<sub id="sub49497494913"><a name="sub49497494913"></a><a name="sub49497494913"></a>S</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p14274382"><a name="p14274382"></a><a name="p14274382"></a>双向，输入带施密特触发器。</p>
</td>
</tr>
<tr id="row61360575"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p4150696"><a name="p4150696"></a><a name="p4150696"></a>I<sub id="sub189491449396"><a name="sub189491449396"></a><a name="sub189491449396"></a>S</sub>/O<sub id="sub16949124917910"><a name="sub16949124917910"></a><a name="sub16949124917910"></a>OD</sub></p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p53627266"><a name="p53627266"></a><a name="p53627266"></a>双向，输入带施密特触发器，输出漏极开路。</p>
</td>
</tr>
<tr id="row12883349"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p36918374"><a name="p36918374"></a><a name="p36918374"></a>XIN</p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p37598356"><a name="p37598356"></a><a name="p37598356"></a>Crystal Oscillator：晶振输入。</p>
</td>
</tr>
<tr id="row2840889"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p28785469"><a name="p28785469"></a><a name="p28785469"></a>XOUT</p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p49921616"><a name="p49921616"></a><a name="p49921616"></a>Crystal Oscillator：晶振输出。</p>
</td>
</tr>
<tr id="row46641368"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p19854472"><a name="p19854472"></a><a name="p19854472"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p64708380"><a name="p64708380"></a><a name="p64708380"></a>电源。</p>
</td>
</tr>
<tr id="row45504511"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.3.1.1 "><p id="p61986789"><a name="p61986789"></a><a name="p61986789"></a>G</p>
</td>
<td class="cellrowborder" valign="top" width="72.72999999999999%" headers="mcps1.2.3.1.2 "><p id="p54874019"><a name="p54874019"></a><a name="p54874019"></a>地。</p>
</td>
</tr>
</tbody>
</table>

### 管脚排列表<a name="ZH-CN_TOPIC_0000001456082732"></a>

WS53V100采用的封装形式为QFN 52Pin，管脚按位置排列分别如[表1 WS53V100芯片管脚排列](#table3939144)所示。

**表 1**  WS53V100芯片管脚排列

<a name="table3939144"></a>
<table><thead align="left"><tr id="row62775401"><th class="cellrowborder" valign="top" width="16.68166816681668%" id="mcps1.2.5.1.1"><p id="p51642735"><a name="p51642735"></a><a name="p51642735"></a>位置</p>
</th>
<th class="cellrowborder" valign="top" width="34.87348734873487%" id="mcps1.2.5.1.2"><p id="p22312013"><a name="p22312013"></a><a name="p22312013"></a>管脚名称</p>
</th>
<th class="cellrowborder" valign="top" width="16.371637163716375%" id="mcps1.2.5.1.3"><p id="p62442668"><a name="p62442668"></a><a name="p62442668"></a>位置</p>
</th>
<th class="cellrowborder" valign="top" width="32.073207320732074%" id="mcps1.2.5.1.4"><p id="p24691380"><a name="p24691380"></a><a name="p24691380"></a>管脚名称</p>
</th>
</tr>
</thead>
<tbody><tr id="row53844748"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p66457308"><a name="p66457308"></a><a name="p66457308"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p623213452274"><a name="p623213452274"></a><a name="p623213452274"></a>AGPIO1/UART_L0_TXD</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p36303315"><a name="p36303315"></a><a name="p36303315"></a>27</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p205431530193012"><a name="p205431530193012"></a><a name="p205431530193012"></a>MGPIO9/UART_H0_RXD</p>
</td>
</tr>
<tr id="row32200631"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p58114317"><a name="p58114317"></a><a name="p58114317"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p122327459278"><a name="p122327459278"></a><a name="p122327459278"></a>AGPIO2/UART_L0_RXD</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p53188122"><a name="p53188122"></a><a name="p53188122"></a>28</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p9543930183016"><a name="p9543930183016"></a><a name="p9543930183016"></a>MGPIO6/UART_H0_RTS</p>
</td>
</tr>
<tr id="row35275281"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p38725542"><a name="p38725542"></a><a name="p38725542"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p1523211455270"><a name="p1523211455270"></a><a name="p1523211455270"></a>AGPIO3</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p3336177"><a name="p3336177"></a><a name="p3336177"></a>29</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p11543203019301"><a name="p11543203019301"></a><a name="p11543203019301"></a>RST_N</p>
</td>
</tr>
<tr id="row55788668"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p22588250"><a name="p22588250"></a><a name="p22588250"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p112327451279"><a name="p112327451279"></a><a name="p112327451279"></a>AGPIO4</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p31631543"><a name="p31631543"></a><a name="p31631543"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p4543193013018"><a name="p4543193013018"></a><a name="p4543193013018"></a>MGPIO15</p>
</td>
</tr>
<tr id="row6366624"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p45934497"><a name="p45934497"></a><a name="p45934497"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p17232154532712"><a name="p17232154532712"></a><a name="p17232154532712"></a>MGPIO5</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p14872087"><a name="p14872087"></a><a name="p14872087"></a>31</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p254383014304"><a name="p254383014304"></a><a name="p254383014304"></a>MGPIO0/SDIO_D2</p>
</td>
</tr>
<tr id="row63653037"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p55622396"><a name="p55622396"></a><a name="p55622396"></a>6</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p132324459276"><a name="p132324459276"></a><a name="p132324459276"></a>XLDO_OUT</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p43359809"><a name="p43359809"></a><a name="p43359809"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p20543130103014"><a name="p20543130103014"></a><a name="p20543130103014"></a>MGPIO1/SDIO_D3</p>
</td>
</tr>
<tr id="row58558366"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p45607220"><a name="p45607220"></a><a name="p45607220"></a>7</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p223216456272"><a name="p223216456272"></a><a name="p223216456272"></a>XOUT</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p184991050522"><a name="p184991050522"></a><a name="p184991050522"></a>33</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p19543113043012"><a name="p19543113043012"></a><a name="p19543113043012"></a>MGPIO2/SDIO_CMD</p>
</td>
</tr>
<tr id="row22907763"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p43589530"><a name="p43589530"></a><a name="p43589530"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p223294515274"><a name="p223294515274"></a><a name="p223294515274"></a>XIN</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p151631126181615"><a name="p151631126181615"></a><a name="p151631126181615"></a>34</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p1854393014304"><a name="p1854393014304"></a><a name="p1854393014304"></a>MGPIO3/SDIO_CLK</p>
</td>
</tr>
<tr id="row65644149"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p15575880"><a name="p15575880"></a><a name="p15575880"></a>9</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p1423224513271"><a name="p1423224513271"></a><a name="p1423224513271"></a>VDD_VBAT2</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p101628268166"><a name="p101628268166"></a><a name="p101628268166"></a>35</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p1543630133014"><a name="p1543630133014"></a><a name="p1543630133014"></a>MGPIO4/SDIO_D0</p>
</td>
</tr>
<tr id="row60214390"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p45527389"><a name="p45527389"></a><a name="p45527389"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p1623264515275"><a name="p1623264515275"></a><a name="p1623264515275"></a>VDD_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p1446010327164"><a name="p1446010327164"></a><a name="p1446010327164"></a>36</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p125435306309"><a name="p125435306309"></a><a name="p125435306309"></a>AGPIO5/SDIO_D1</p>
</td>
</tr>
<tr id="row43967757"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p4618564"><a name="p4618564"></a><a name="p4618564"></a>11</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p1323224552712"><a name="p1323224552712"></a><a name="p1323224552712"></a>VDD_RFLDO1</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p746023215161"><a name="p746023215161"></a><a name="p746023215161"></a>37</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p2543173023018"><a name="p2543173023018"></a><a name="p2543173023018"></a>VDDIO</p>
</td>
</tr>
<tr id="row24224733"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p16046317"><a name="p16046317"></a><a name="p16046317"></a>12</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p42321545152715"><a name="p42321545152715"></a><a name="p42321545152715"></a>VDD_RFLDO2</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p54601932161620"><a name="p54601932161620"></a><a name="p54601932161620"></a>38</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p95431306306"><a name="p95431306306"></a><a name="p95431306306"></a>AVDD33</p>
</td>
</tr>
<tr id="row52327117"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p10638097"><a name="p10638097"></a><a name="p10638097"></a>13</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p14232204532719"><a name="p14232204532719"></a><a name="p14232204532719"></a>VDD_WL_RF_TRX_1P1</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p1045963214164"><a name="p1045963214164"></a><a name="p1045963214164"></a>39</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p15543153073016"><a name="p15543153073016"></a><a name="p15543153073016"></a>VDD_VBAT1</p>
</td>
</tr>
<tr id="row16154192"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p33421169"><a name="p33421169"></a><a name="p33421169"></a>14</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p14777132513289"><a name="p14777132513289"></a><a name="p14777132513289"></a>VDD_WL_RF_PA_3P3</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p415318218217"><a name="p415318218217"></a><a name="p415318218217"></a>40</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p9823534113020"><a name="p9823534113020"></a><a name="p9823534113020"></a>BUCK_LX</p>
</td>
</tr>
<tr id="row41055134"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p37131542"><a name="p37131542"></a><a name="p37131542"></a>15</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p9777172515283"><a name="p9777172515283"></a><a name="p9777172515283"></a>WB_RFIO</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p121537252115"><a name="p121537252115"></a><a name="p121537252115"></a>41</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p3823153413307"><a name="p3823153413307"></a><a name="p3823153413307"></a>VDD1P3_PMU1</p>
</td>
</tr>
<tr id="row37224696"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p62410385"><a name="p62410385"></a><a name="p62410385"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p20777225172811"><a name="p20777225172811"></a><a name="p20777225172811"></a>VDD_RF_RX_1P1</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p131531826217"><a name="p131531826217"></a><a name="p131531826217"></a>42</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p1182313417303"><a name="p1182313417303"></a><a name="p1182313417303"></a>VDD_CLDO</p>
</td>
</tr>
<tr id="row422023991413"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p124962398211"><a name="p124962398211"></a><a name="p124962398211"></a>17</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p87776255283"><a name="p87776255283"></a><a name="p87776255283"></a>VDD_BSLE_RF_PA_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p20153152162119"><a name="p20153152162119"></a><a name="p20153152162119"></a>43</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p128231434153014"><a name="p128231434153014"></a><a name="p128231434153014"></a>MGPIO22</p>
</td>
</tr>
<tr id="row988613201152"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p42578285"><a name="p42578285"></a><a name="p42578285"></a>18</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p117778255288"><a name="p117778255288"></a><a name="p117778255288"></a>VDD_BSLE_DPALDO</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p11154132192120"><a name="p11154132192120"></a><a name="p11154132192120"></a>44</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p7823134183012"><a name="p7823134183012"></a><a name="p7823134183012"></a>NC/RTC_OUT</p>
</td>
</tr>
<tr id="row23511955131512"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p4126994"><a name="p4126994"></a><a name="p4126994"></a>19</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p13777325122820"><a name="p13777325122820"></a><a name="p13777325122820"></a>VDD_BSLE_RF_DRV_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p1915417212216"><a name="p1915417212216"></a><a name="p1915417212216"></a>45</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p168231534143014"><a name="p168231534143014"></a><a name="p168231534143014"></a>NC/RTC_IN</p>
</td>
</tr>
<tr id="row75142594159"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p25140036"><a name="p25140036"></a><a name="p25140036"></a>20</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p17777172532816"><a name="p17777172532816"></a><a name="p17777172532816"></a>VDD_BSLE_PLL_DCO_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p115418212118"><a name="p115418212118"></a><a name="p115418212118"></a>46</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p282318343305"><a name="p282318343305"></a><a name="p282318343305"></a>MGPIO21</p>
</td>
</tr>
<tr id="row155481513164"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p57438237"><a name="p57438237"></a><a name="p57438237"></a>21</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p577715255289"><a name="p577715255289"></a><a name="p577715255289"></a>MGPIO10/SPI0_CS0</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p131542272111"><a name="p131542272111"></a><a name="p131542272111"></a>47</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p158232341309"><a name="p158232341309"></a><a name="p158232341309"></a>MGPIO16/QSPI1_D3</p>
</td>
</tr>
<tr id="row17331175371515"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p540607"><a name="p540607"></a><a name="p540607"></a>22</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p6778142572810"><a name="p6778142572810"></a><a name="p6778142572810"></a>MGPIO11/SPI0_CLK</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p31541526217"><a name="p31541526217"></a><a name="p31541526217"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p14823153493018"><a name="p14823153493018"></a><a name="p14823153493018"></a>MGPIO17/QSPI1_CLK</p>
</td>
</tr>
<tr id="row171339512156"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p57658513"><a name="p57658513"></a><a name="p57658513"></a>23</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p2778182512818"><a name="p2778182512818"></a><a name="p2778182512818"></a>MGPIO12/SPI0_DI</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p1015417252118"><a name="p1015417252118"></a><a name="p1015417252118"></a>49</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p1182393453019"><a name="p1182393453019"></a><a name="p1182393453019"></a>MGPIO18/QSPI1_D0</p>
</td>
</tr>
<tr id="row632052371512"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p40042374"><a name="p40042374"></a><a name="p40042374"></a>24</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p10778325142810"><a name="p10778325142810"></a><a name="p10778325142810"></a>MGPIO13/SPI0_DO</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p1815411252113"><a name="p1815411252113"></a><a name="p1815411252113"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p4823153420307"><a name="p4823153420307"></a><a name="p4823153420307"></a>MGPIO19/QSPI1_D1</p>
</td>
</tr>
<tr id="row7424134918148"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p53659222"><a name="p53659222"></a><a name="p53659222"></a>25</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p3778202572814"><a name="p3778202572814"></a><a name="p3778202572814"></a>MGPIO14</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p1015412213212"><a name="p1015412213212"></a><a name="p1015412213212"></a>51</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p4823143423011"><a name="p4823143423011"></a><a name="p4823143423011"></a>MGPIO20/QSPI1_CS</p>
</td>
</tr>
<tr id="row1026023"><td class="cellrowborder" valign="top" width="16.68166816681668%" headers="mcps1.2.5.1.1 "><p id="p3650498"><a name="p3650498"></a><a name="p3650498"></a>26</p>
</td>
<td class="cellrowborder" valign="top" width="34.87348734873487%" headers="mcps1.2.5.1.2 "><p id="p1477882572819"><a name="p1477882572819"></a><a name="p1477882572819"></a>MGPIO8/UART_H0_TXD</p>
</td>
<td class="cellrowborder" valign="top" width="16.371637163716375%" headers="mcps1.2.5.1.3 "><p id="p10154182142118"><a name="p10154182142118"></a><a name="p10154182142118"></a>52</p>
</td>
<td class="cellrowborder" valign="top" width="32.073207320732074%" headers="mcps1.2.5.1.4 "><p id="p1823334113016"><a name="p1823334113016"></a><a name="p1823334113016"></a>MGPIO7/QSPI1_D2</p>
</td>
</tr>
</tbody>
</table>

### 全芯片复位接口<a name="ZH-CN_TOPIC_0000001505603513"></a>

全芯片复位信号如[表1](#table31291646)所示。

**表 1**  全局复位信号管脚列表

<a name="table31291646"></a>
<table><thead align="left"><tr id="row21421675"><th class="cellrowborder" valign="top" width="9.21%" id="mcps1.2.7.1.1"><p id="p198711632109"><a name="p198711632109"></a><a name="p198711632109"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="14.829999999999998%" id="mcps1.2.7.1.2"><p id="p57434139"><a name="p57434139"></a><a name="p57434139"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="12.01%" id="mcps1.2.7.1.3"><p id="p9119245"><a name="p9119245"></a><a name="p9119245"></a>类型</p>
</th>
<th class="cellrowborder" valign="top" width="17.75%" id="mcps1.2.7.1.4"><p id="p461342"><a name="p461342"></a><a name="p461342"></a>频率（MHz）</p>
</th>
<th class="cellrowborder" valign="top" width="15.5%" id="mcps1.2.7.1.5"><p id="p37368736"><a name="p37368736"></a><a name="p37368736"></a>电平（V）</p>
</th>
<th class="cellrowborder" valign="top" width="30.7%" id="mcps1.2.7.1.6"><p id="p6968762"><a name="p6968762"></a><a name="p6968762"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row27598869"><td class="cellrowborder" valign="top" width="9.21%" headers="mcps1.2.7.1.1 "><p id="p1311331316109"><a name="p1311331316109"></a><a name="p1311331316109"></a>29</p>
</td>
<td class="cellrowborder" valign="top" width="14.829999999999998%" headers="mcps1.2.7.1.2 "><p id="p20915929"><a name="p20915929"></a><a name="p20915929"></a>RST_N</p>
</td>
<td class="cellrowborder" valign="top" width="12.01%" headers="mcps1.2.7.1.3 "><p id="p58892473"><a name="p58892473"></a><a name="p58892473"></a>I</p>
</td>
<td class="cellrowborder" valign="top" width="17.75%" headers="mcps1.2.7.1.4 "><p id="p5560998"><a name="p5560998"></a><a name="p5560998"></a>&lt;1</p>
</td>
<td class="cellrowborder" valign="top" width="15.5%" headers="mcps1.2.7.1.5 "><p id="p47787675"><a name="p47787675"></a><a name="p47787675"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="30.7%" headers="mcps1.2.7.1.6 "><p id="p45596481"><a name="p45596481"></a><a name="p45596481"></a>全局芯片复位信号，拉低将复位全芯片。</p>
</td>
</tr>
</tbody>
</table>

### GPIO接口<a name="ZH-CN_TOPIC_0000001505842465"></a>

>![](public_sys-resources/icon-notice.gif) **须知：** 
>支持外置RTC功能的芯片，当硬件方案不使用外置RTC时，RTC\_IN管脚板级预留接地电阻位置，若芯片应用场景存在环境或板级干扰，建议RTC\_IN管脚板级接地，RTC\_OUT管脚保持悬空，增强抗干扰能力。板级禁止RTC\_IN和OUT管脚同时接地。

GPIO接口如[表1](#table63646052)所示。

**表 1**  GPIO接口管脚列表

<a name="table63646052"></a>
<table><thead align="left"><tr id="row28141317"><th class="cellrowborder" valign="top" width="10.47%" id="mcps1.2.6.1.1"><p id="p196221351131111"><a name="p196221351131111"></a><a name="p196221351131111"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="21.48%" id="mcps1.2.6.1.2"><p id="p64854219"><a name="p64854219"></a><a name="p64854219"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="11.129999999999999%" id="mcps1.2.6.1.3"><p id="p38336904"><a name="p38336904"></a><a name="p38336904"></a>类型</p>
</th>
<th class="cellrowborder" valign="top" width="19.040000000000003%" id="mcps1.2.6.1.4"><p id="p18281552"><a name="p18281552"></a><a name="p18281552"></a>电平(V)</p>
</th>
<th class="cellrowborder" valign="top" width="37.88%" id="mcps1.2.6.1.5"><p id="p4410728"><a name="p4410728"></a><a name="p4410728"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row21724664"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p7146444174616"><a name="p7146444174616"></a><a name="p7146444174616"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p39511438183118"><a name="p39511438183118"></a><a name="p39511438183118"></a>AGPIO1</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p35632012"><a name="p35632012"></a><a name="p35632012"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p511887"><a name="p511887"></a><a name="p511887"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p41462866"><a name="p41462866"></a><a name="p41462866"></a>普通GPIO，在深睡模式下，此IO支持输入唤醒或输出。</p>
</td>
</tr>
<tr id="row37621475"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p3146184411465"><a name="p3146184411465"></a><a name="p3146184411465"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p15951123893113"><a name="p15951123893113"></a><a name="p15951123893113"></a>AGPIO2</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p51921052"><a name="p51921052"></a><a name="p51921052"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p44855704"><a name="p44855704"></a><a name="p44855704"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p47356620431"><a name="p47356620431"></a><a name="p47356620431"></a>普通GPIO，在深睡模式下，此IO支持输入唤醒或输出。</p>
</td>
</tr>
<tr id="row17792110"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p17146174474615"><a name="p17146174474615"></a><a name="p17146174474615"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p195123814313"><a name="p195123814313"></a><a name="p195123814313"></a>AGPIO3</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p19162058"><a name="p19162058"></a><a name="p19162058"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p8622890"><a name="p8622890"></a><a name="p8622890"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p47311716433"><a name="p47311716433"></a><a name="p47311716433"></a>普通GPIO，在深睡模式下，此IO支持输入唤醒或输出。</p>
</td>
</tr>
<tr id="row44962972"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p2147144144615"><a name="p2147144144615"></a><a name="p2147144144615"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p2095173814312"><a name="p2095173814312"></a><a name="p2095173814312"></a>AGPIO4</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p49143529"><a name="p49143529"></a><a name="p49143529"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p21202951"><a name="p21202951"></a><a name="p21202951"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p667482010436"><a name="p667482010436"></a><a name="p667482010436"></a>普通GPIO，在深睡模式下，此IO支持输入唤醒或输出。</p>
</td>
</tr>
<tr id="row21913016"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p2147184444613"><a name="p2147184444613"></a><a name="p2147184444613"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p16147244104611"><a name="p16147244104611"></a><a name="p16147244104611"></a>MGPIO5</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p6883221"><a name="p6883221"></a><a name="p6883221"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p20670010"><a name="p20670010"></a><a name="p20670010"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p63658128"><a name="p63658128"></a><a name="p63658128"></a>普通GPIO</p>
</td>
</tr>
<tr id="row36052245"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p14458922173213"><a name="p14458922173213"></a><a name="p14458922173213"></a>21</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p1445872283210"><a name="p1445872283210"></a><a name="p1445872283210"></a>MGPIO10</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p60580335"><a name="p60580335"></a><a name="p60580335"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p8060118"><a name="p8060118"></a><a name="p8060118"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p48889850"><a name="p48889850"></a><a name="p48889850"></a>普通GPIO</p>
</td>
</tr>
<tr id="row37355470"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p114583227327"><a name="p114583227327"></a><a name="p114583227327"></a>22</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p145962283215"><a name="p145962283215"></a><a name="p145962283215"></a>MGPIO11</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p17349988"><a name="p17349988"></a><a name="p17349988"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p63171767"><a name="p63171767"></a><a name="p63171767"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p0406163934420"><a name="p0406163934420"></a><a name="p0406163934420"></a>普通GPIO，在深睡模式下，此IO仅支持输入唤醒，不支持输出。</p>
</td>
</tr>
<tr id="row15537542"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p245942243215"><a name="p245942243215"></a><a name="p245942243215"></a>23</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p345912273211"><a name="p345912273211"></a><a name="p345912273211"></a>MGPIO12</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p11404133"><a name="p11404133"></a><a name="p11404133"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p51319614"><a name="p51319614"></a><a name="p51319614"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p63248075"><a name="p63248075"></a><a name="p63248075"></a>普通GPIO</p>
</td>
</tr>
<tr id="row32361769"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p1645952233218"><a name="p1645952233218"></a><a name="p1645952233218"></a>24</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p94595229324"><a name="p94595229324"></a><a name="p94595229324"></a>MGPIO13</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p47015983"><a name="p47015983"></a><a name="p47015983"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p50198296"><a name="p50198296"></a><a name="p50198296"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p39530145"><a name="p39530145"></a><a name="p39530145"></a>普通GPIO</p>
</td>
</tr>
<tr id="row20226985"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p845942220323"><a name="p845942220323"></a><a name="p845942220323"></a>25</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p3459202211328"><a name="p3459202211328"></a><a name="p3459202211328"></a>MGPIO14</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p18492804"><a name="p18492804"></a><a name="p18492804"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p21522166"><a name="p21522166"></a><a name="p21522166"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p65573909"><a name="p65573909"></a><a name="p65573909"></a>普通GPIO</p>
</td>
</tr>
<tr id="row53294272"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p104596223323"><a name="p104596223323"></a><a name="p104596223323"></a>26</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p18459182223219"><a name="p18459182223219"></a><a name="p18459182223219"></a>MGPIO8</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p2533231"><a name="p2533231"></a><a name="p2533231"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p3865173"><a name="p3865173"></a><a name="p3865173"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p44643603"><a name="p44643603"></a><a name="p44643603"></a>普通GPIO</p>
</td>
</tr>
<tr id="row66248115"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p152143306326"><a name="p152143306326"></a><a name="p152143306326"></a>27</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p2021412302322"><a name="p2021412302322"></a><a name="p2021412302322"></a>MGPIO9</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p44282627"><a name="p44282627"></a><a name="p44282627"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p30123063"><a name="p30123063"></a><a name="p30123063"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p24049039"><a name="p24049039"></a><a name="p24049039"></a>普通GPIO</p>
</td>
</tr>
<tr id="row15114764"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p1421433016327"><a name="p1421433016327"></a><a name="p1421433016327"></a>28</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p12214103033210"><a name="p12214103033210"></a><a name="p12214103033210"></a>MGPIO6</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p10309404"><a name="p10309404"></a><a name="p10309404"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p29755367"><a name="p29755367"></a><a name="p29755367"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p125971538483"><a name="p125971538483"></a><a name="p125971538483"></a>普通GPIO，在深睡模式下，此IO仅支持输入唤醒，不支持输出。</p>
</td>
</tr>
<tr id="row24311045"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p28234306345"><a name="p28234306345"></a><a name="p28234306345"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p11214930163219"><a name="p11214930163219"></a><a name="p11214930163219"></a>MGPIO15</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p20668333"><a name="p20668333"></a><a name="p20668333"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p63522246"><a name="p63522246"></a><a name="p63522246"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p45028263"><a name="p45028263"></a><a name="p45028263"></a>普通GPIO</p>
</td>
</tr>
<tr id="row125454764519"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p1121414306328"><a name="p1121414306328"></a><a name="p1121414306328"></a>31</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p1421483017327"><a name="p1421483017327"></a><a name="p1421483017327"></a>MGPIO0</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p53498917496"><a name="p53498917496"></a><a name="p53498917496"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p123494913498"><a name="p123494913498"></a><a name="p123494913498"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p9173202515495"><a name="p9173202515495"></a><a name="p9173202515495"></a>普通GPIO</p>
</td>
</tr>
<tr id="row93005544451"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p421483011327"><a name="p421483011327"></a><a name="p421483011327"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p1821463033220"><a name="p1821463033220"></a><a name="p1821463033220"></a>MGPIO1</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p103491910499"><a name="p103491910499"></a><a name="p103491910499"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p83491399496"><a name="p83491399496"></a><a name="p83491399496"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p493363316283"><a name="p493363316283"></a><a name="p493363316283"></a>普通GPIO</p>
</td>
</tr>
<tr id="row1846415584454"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p20214530163210"><a name="p20214530163210"></a><a name="p20214530163210"></a>33</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p14214130103220"><a name="p14214130103220"></a><a name="p14214130103220"></a>MGPIO2</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p12349119154919"><a name="p12349119154919"></a><a name="p12349119154919"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p123496984917"><a name="p123496984917"></a><a name="p123496984917"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p174651758194520"><a name="p174651758194520"></a><a name="p174651758194520"></a>普通GPIO</p>
</td>
</tr>
<tr id="row161295424617"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p16214930113212"><a name="p16214930113212"></a><a name="p16214930113212"></a>34</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p7214163063212"><a name="p7214163063212"></a><a name="p7214163063212"></a>MGPIO3</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p13349493498"><a name="p13349493498"></a><a name="p13349493498"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p19349109174920"><a name="p19349109174920"></a><a name="p19349109174920"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p56572045114912"><a name="p56572045114912"></a><a name="p56572045114912"></a>普通GPIO</p>
</td>
</tr>
<tr id="row212916412468"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p15214193063211"><a name="p15214193063211"></a><a name="p15214193063211"></a>35</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p6214173013327"><a name="p6214173013327"></a><a name="p6214173013327"></a>MGPIO4</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p12349139154910"><a name="p12349139154910"></a><a name="p12349139154910"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p14349099499"><a name="p14349099499"></a><a name="p14349099499"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p19657154510492"><a name="p19657154510492"></a><a name="p19657154510492"></a>普通GPIO</p>
</td>
</tr>
<tr id="row1620619174612"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p1421418309326"><a name="p1421418309326"></a><a name="p1421418309326"></a>36</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p1321413053216"><a name="p1321413053216"></a><a name="p1321413053216"></a>AGPIO5</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p113495994916"><a name="p113495994916"></a><a name="p113495994916"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p434909174917"><a name="p434909174917"></a><a name="p434909174917"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p1012593211435"><a name="p1012593211435"></a><a name="p1012593211435"></a>普通GPIO，在深睡模式下，此IO支持输入唤醒或输出。</p>
</td>
</tr>
<tr id="row320613914469"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p63171141103212"><a name="p63171141103212"></a><a name="p63171141103212"></a>43</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p163170411325"><a name="p163170411325"></a><a name="p163170411325"></a>MGPIO22</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p2034915916493"><a name="p2034915916493"></a><a name="p2034915916493"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p4350119104913"><a name="p4350119104913"></a><a name="p4350119104913"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p1122264614913"><a name="p1122264614913"></a><a name="p1122264614913"></a>普通GPIO</p>
</td>
</tr>
<tr id="row220610911464"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p63173419322"><a name="p63173419322"></a><a name="p63173419322"></a>44</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p231714412324"><a name="p231714412324"></a><a name="p231714412324"></a>NC/RTC_OUT</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p117431958457"><a name="p117431958457"></a><a name="p117431958457"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p691571054918"><a name="p691571054918"></a><a name="p691571054918"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p27719256331"><a name="p27719256331"></a><a name="p27719256331"></a>-可用作 RTC 晶体专用 PAD。当无外挂 RC32K 晶体需求时，建议板级保持悬空。</p>
</td>
</tr>
<tr id="row82062944613"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p131714113326"><a name="p131714113326"></a><a name="p131714113326"></a>45</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p1331716416324"><a name="p1331716416324"></a><a name="p1331716416324"></a>NC/RTC_IN</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p152961803616"><a name="p152961803616"></a><a name="p152961803616"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p19915161012499"><a name="p19915161012499"></a><a name="p19915161012499"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p2574182385918"><a name="p2574182385918"></a><a name="p2574182385918"></a>-可用作 RTC 晶体专用 PAD。当无外挂 RC32K 晶体需求时，板级预留接地电阻位置，若芯片应用场景存在环境或板级干扰，建议RTC_IN管脚板级接地。</p>
</td>
</tr>
<tr id="row17206149144611"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p133171641113213"><a name="p133171641113213"></a><a name="p133171641113213"></a>46</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p1931710416323"><a name="p1931710416323"></a><a name="p1931710416323"></a>MGPIO21</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p167853126498"><a name="p167853126498"></a><a name="p167853126498"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p2785171284918"><a name="p2785171284918"></a><a name="p2785171284918"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p20345747174912"><a name="p20345747174912"></a><a name="p20345747174912"></a>普通GPIO</p>
</td>
</tr>
<tr id="row87182510468"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p19317341123218"><a name="p19317341123218"></a><a name="p19317341123218"></a>47</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p1331794153212"><a name="p1331794153212"></a><a name="p1331794153212"></a>MGPIO16</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p1785101254919"><a name="p1785101254919"></a><a name="p1785101254919"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p16785121218491"><a name="p16785121218491"></a><a name="p16785121218491"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p1290840132816"><a name="p1290840132816"></a><a name="p1290840132816"></a>普通GPIO，在深睡模式下，此IO仅支持输入唤醒，不支持输出。</p>
</td>
</tr>
<tr id="row197152510465"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p3317341153215"><a name="p3317341153215"></a><a name="p3317341153215"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p231714111323"><a name="p231714111323"></a><a name="p231714111323"></a>MGPIO17</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p1978581224912"><a name="p1978581224912"></a><a name="p1978581224912"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p9785151211498"><a name="p9785151211498"></a><a name="p9785151211498"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p1987244714492"><a name="p1987244714492"></a><a name="p1987244714492"></a>普通GPIO</p>
</td>
</tr>
<tr id="row13722564618"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p1131764112322"><a name="p1131764112322"></a><a name="p1131764112322"></a>49</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p14317104103214"><a name="p14317104103214"></a><a name="p14317104103214"></a>MGPIO18</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p1878620129498"><a name="p1878620129498"></a><a name="p1878620129498"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p3786512124911"><a name="p3786512124911"></a><a name="p3786512124911"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p5810251460"><a name="p5810251460"></a><a name="p5810251460"></a>普通GPIO</p>
</td>
</tr>
<tr id="row108132584611"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p1731784163220"><a name="p1731784163220"></a><a name="p1731784163220"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p5317941123213"><a name="p5317941123213"></a><a name="p5317941123213"></a>MGPIO19</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p17861012194915"><a name="p17861012194915"></a><a name="p17861012194915"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p7786131264918"><a name="p7786131264918"></a><a name="p7786131264918"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p111551749194915"><a name="p111551749194915"></a><a name="p111551749194915"></a>普通GPIO</p>
</td>
</tr>
<tr id="row14812250469"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p1231714415329"><a name="p1231714415329"></a><a name="p1231714415329"></a>51</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p1431784115327"><a name="p1431784115327"></a><a name="p1431784115327"></a>MGPIO20</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p17786212124910"><a name="p17786212124910"></a><a name="p17786212124910"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p97861912104918"><a name="p97861912104918"></a><a name="p97861912104918"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p11551249204910"><a name="p11551249204910"></a><a name="p11551249204910"></a>普通GPIO</p>
</td>
</tr>
<tr id="row18142515461"><td class="cellrowborder" valign="top" width="10.47%" headers="mcps1.2.6.1.1 "><p id="p525120115296"><a name="p525120115296"></a><a name="p525120115296"></a>52</p>
</td>
<td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.6.1.2 "><p id="p163181641133219"><a name="p163181641133219"></a><a name="p163181641133219"></a>MGPIO7</p>
</td>
<td class="cellrowborder" valign="top" width="11.129999999999999%" headers="mcps1.2.6.1.3 "><p id="p878621214912"><a name="p878621214912"></a><a name="p878621214912"></a>I/O</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.6.1.4 "><p id="p1578621212497"><a name="p1578621212497"></a><a name="p1578621212497"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.6.1.5 "><p id="p6391346132817"><a name="p6391346132817"></a><a name="p6391346132817"></a>普通GPIO，在深睡模式下，此IO仅支持输入唤醒，不支持输出。</p>
</td>
</tr>
</tbody>
</table>

### 电源管脚<a name="ZH-CN_TOPIC_0000001505842477"></a>

电源管脚如[表1](#table10750772)所示。

**表 1**  电源管脚列表

<a name="table10750772"></a>
<table><thead align="left"><tr id="row22882960"><th class="cellrowborder" valign="top" width="8.079192080791922%" id="mcps1.2.6.1.1"><p id="p767841121519"><a name="p767841121519"></a><a name="p767841121519"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="23.44765523447655%" id="mcps1.2.6.1.2"><p id="p41580444"><a name="p41580444"></a><a name="p41580444"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="9.68903109689031%" id="mcps1.2.6.1.3"><p id="p11766267"><a name="p11766267"></a><a name="p11766267"></a>类型</p>
</th>
<th class="cellrowborder" valign="top" width="12.468753124687531%" id="mcps1.2.6.1.4"><p id="p13543581"><a name="p13543581"></a><a name="p13543581"></a>电压(V)</p>
</th>
<th class="cellrowborder" valign="top" width="46.31536846315368%" id="mcps1.2.6.1.5"><p id="p23288300"><a name="p23288300"></a><a name="p23288300"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row7304143"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p11130537175316"><a name="p11130537175316"></a><a name="p11130537175316"></a>6</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p813073765319"><a name="p813073765319"></a><a name="p813073765319"></a>XLDO_OUT</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p10465156"><a name="p10465156"></a><a name="p10465156"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p42371273"><a name="p42371273"></a><a name="p42371273"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p9521066"><a name="p9521066"></a><a name="p9521066"></a>芯片XLDO decap管脚，接板级滤波电容1uF。</p>
</td>
</tr>
<tr id="row18580737"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p71306375534"><a name="p71306375534"></a><a name="p71306375534"></a>9</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p9130143755312"><a name="p9130143755312"></a><a name="p9130143755312"></a>VDD_VBAT2</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p33459681"><a name="p33459681"></a><a name="p33459681"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p25879650"><a name="p25879650"></a><a name="p25879650"></a>3.3</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p15876907"><a name="p15876907"></a><a name="p15876907"></a>INTLDO和XLDO输入电源，由板级提供3.3V电源。</p>
</td>
</tr>
<tr id="row8674443"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p151301237125313"><a name="p151301237125313"></a><a name="p151301237125313"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p51304376538"><a name="p51304376538"></a><a name="p51304376538"></a>VDD_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p45634724"><a name="p45634724"></a><a name="p45634724"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p5425146"><a name="p5425146"></a><a name="p5425146"></a>1.3</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p9445112165511"><a name="p9445112165511"></a><a name="p9445112165511"></a>1.3V电压输入，RFLDO1，RFLDO2输入电源。</p>
</td>
</tr>
<tr id="row62618006"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p2013023711530"><a name="p2013023711530"></a><a name="p2013023711530"></a>11</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p1413033725315"><a name="p1413033725315"></a><a name="p1413033725315"></a>VDD_RFLDO1</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p34030663"><a name="p34030663"></a><a name="p34030663"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p5020285"><a name="p5020285"></a><a name="p5020285"></a>1.15</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p183751944183113"><a name="p183751944183113"></a><a name="p183751944183113"></a>内部LDO电源，输出提供给VDD_WL_RF_TRX_1P1、</p>
<p id="p8375194419312"><a name="p8375194419312"></a><a name="p8375194419312"></a>VDD_RF_RX_1P1，外接1μF。</p>
</td>
</tr>
<tr id="row35909463"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p1513033716533"><a name="p1513033716533"></a><a name="p1513033716533"></a>12</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p1013063765320"><a name="p1013063765320"></a><a name="p1013063765320"></a>VDD_RFLDO2</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p13553869"><a name="p13553869"></a><a name="p13553869"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p24121565"><a name="p24121565"></a><a name="p24121565"></a>1.15</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p7689721"><a name="p7689721"></a><a name="p7689721"></a>RFLDO2电源decap管脚，给内部VCO、LO供电，接板级滤波电容1μF。</p>
</td>
</tr>
<tr id="row2098632"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p9130123725318"><a name="p9130123725318"></a><a name="p9130123725318"></a>13</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p7130437155317"><a name="p7130437155317"></a><a name="p7130437155317"></a>VDD_WL_RF_TRX_1P1</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p17053313"><a name="p17053313"></a><a name="p17053313"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p39141076"><a name="p39141076"></a><a name="p39141076"></a>1.15</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p16310625"><a name="p16310625"></a><a name="p16310625"></a>芯片内部TRX相关模块输入电源。</p>
</td>
</tr>
<tr id="row12577900"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p21305375536"><a name="p21305375536"></a><a name="p21305375536"></a>14</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p1513093716539"><a name="p1513093716539"></a><a name="p1513093716539"></a>VDD_WL_RF_PA_3P3</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p33489078"><a name="p33489078"></a><a name="p33489078"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p28260775"><a name="p28260775"></a><a name="p28260775"></a>3.3</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p103169526569"><a name="p103169526569"></a><a name="p103169526569"></a>PA 3V3电源输入，由外部电源提供，由VDD_RFLDO1供电。</p>
</td>
</tr>
<tr id="row66793230"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p639534463316"><a name="p639534463316"></a><a name="p639534463316"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p1639514420338"><a name="p1639514420338"></a><a name="p1639514420338"></a>VDD_RF_RX_1P1</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p31470215"><a name="p31470215"></a><a name="p31470215"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p66059488"><a name="p66059488"></a><a name="p66059488"></a>1.15</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p49218346"><a name="p49218346"></a><a name="p49218346"></a>RF LNA供电输入。</p>
</td>
</tr>
<tr id="row40311937"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p2395844173319"><a name="p2395844173319"></a><a name="p2395844173319"></a>17</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p1539564483310"><a name="p1539564483310"></a><a name="p1539564483310"></a>VDD_BSLE_RF_PA_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p52380055"><a name="p52380055"></a><a name="p52380055"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p14926099"><a name="p14926099"></a><a name="p14926099"></a>1.3</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p1054474"><a name="p1054474"></a><a name="p1054474"></a>BSLE_RF 1V3电源输入管脚。</p>
</td>
</tr>
<tr id="row9490272"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p113952044103311"><a name="p113952044103311"></a><a name="p113952044103311"></a>18</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p7395244123316"><a name="p7395244123316"></a><a name="p7395244123316"></a>VDD_BSLE_DPALDO</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p20484818"><a name="p20484818"></a><a name="p20484818"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p48657561"><a name="p48657561"></a><a name="p48657561"></a>1.1</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p48948360"><a name="p48948360"></a><a name="p48948360"></a>DPA LDO输出，外接1μF。</p>
</td>
</tr>
<tr id="row37882063"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p17395104411336"><a name="p17395104411336"></a><a name="p17395104411336"></a>19</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p03952443334"><a name="p03952443334"></a><a name="p03952443334"></a>VDD_BSLE_RF_DRV_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p26323242"><a name="p26323242"></a><a name="p26323242"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p51807830"><a name="p51807830"></a><a name="p51807830"></a>1.3</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p35684727"><a name="p35684727"></a><a name="p35684727"></a>BSLE供电输入，给内部BSLE模块供电，外接1μF。</p>
</td>
</tr>
<tr id="row52727095"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p7395144419338"><a name="p7395144419338"></a><a name="p7395144419338"></a>20</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p1639544414336"><a name="p1639544414336"></a><a name="p1639544414336"></a>VDD_BSLE_PLL_DCO_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p34322009"><a name="p34322009"></a><a name="p34322009"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p28619382"><a name="p28619382"></a><a name="p28619382"></a>1.3</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p1869817216272"><a name="p1869817216272"></a><a name="p1869817216272"></a>BSLE_PLL 1V3电源输入管脚。</p>
</td>
</tr>
<tr id="row59781901"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p191161854123316"><a name="p191161854123316"></a><a name="p191161854123316"></a>37</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p61161454103311"><a name="p61161454103311"></a><a name="p61161454103311"></a>VDDIO</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p149244349916"><a name="p149244349916"></a><a name="p149244349916"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p14221611"><a name="p14221611"></a><a name="p14221611"></a>1.8/3.3</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p36468595"><a name="p36468595"></a><a name="p36468595"></a>IO电源输入，支持板级1.8V/3.3V。</p>
</td>
</tr>
<tr id="row1262933115317"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p411695493319"><a name="p411695493319"></a><a name="p411695493319"></a>38</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p11165543336"><a name="p11165543336"></a><a name="p11165543336"></a>AVDD33</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p10924434493"><a name="p10924434493"></a><a name="p10924434493"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p1162943111532"><a name="p1162943111532"></a><a name="p1162943111532"></a>3.3</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p15700184716278"><a name="p15700184716278"></a><a name="p15700184716278"></a>AVDD33电源输入，由板级提供3.3V。</p>
</td>
</tr>
<tr id="row06291631125312"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p6116195453312"><a name="p6116195453312"></a><a name="p6116195453312"></a>39</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p161163541335"><a name="p161163541335"></a><a name="p161163541335"></a>VDD_VBAT1</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p1792419341397"><a name="p1792419341397"></a><a name="p1792419341397"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p176296314536"><a name="p176296314536"></a><a name="p176296314536"></a>3.3</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p96291931125310"><a name="p96291931125310"></a><a name="p96291931125310"></a>VBAT电源输入。</p>
</td>
</tr>
<tr id="row176291431155310"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p163301410163416"><a name="p163301410163416"></a><a name="p163301410163416"></a>40</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p10330171011345"><a name="p10330171011345"></a><a name="p10330171011345"></a>BUCK_LX</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p19241334192"><a name="p19241334192"></a><a name="p19241334192"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p16629103114534"><a name="p16629103114534"></a><a name="p16629103114534"></a>1.3</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p36783718"><a name="p36783718"></a><a name="p36783718"></a>BUCK电源输出，给Pin10/17/19/20/41管脚供电。</p>
</td>
</tr>
<tr id="row1062973165311"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p1330131033419"><a name="p1330131033419"></a><a name="p1330131033419"></a>41</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p15330121043412"><a name="p15330121043412"></a><a name="p15330121043412"></a>VDD1P3_PMU1</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p20924234094"><a name="p20924234094"></a><a name="p20924234094"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p166291631115320"><a name="p166291631115320"></a><a name="p166291631115320"></a>1.3</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p1962918319536"><a name="p1962918319536"></a><a name="p1962918319536"></a>BUCK 1.3V输入，给内部CLDO供电。</p>
</td>
</tr>
<tr id="row12405174143410"><td class="cellrowborder" valign="top" width="8.079192080791922%" headers="mcps1.2.6.1.1 "><p id="p133303105342"><a name="p133303105342"></a><a name="p133303105342"></a>42</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.6.1.2 "><p id="p6330181033415"><a name="p6330181033415"></a><a name="p6330181033415"></a>VDD_CLDO</p>
</td>
<td class="cellrowborder" valign="top" width="9.68903109689031%" headers="mcps1.2.6.1.3 "><p id="p5640155619309"><a name="p5640155619309"></a><a name="p5640155619309"></a>P</p>
</td>
<td class="cellrowborder" valign="top" width="12.468753124687531%" headers="mcps1.2.6.1.4 "><p id="p864065683010"><a name="p864065683010"></a><a name="p864065683010"></a>1.1</p>
</td>
<td class="cellrowborder" valign="top" width="46.31536846315368%" headers="mcps1.2.6.1.5 "><p id="p18630173112534"><a name="p18630173112534"></a><a name="p18630173112534"></a>CLDO输出，外接滤波电容1μF。</p>
</td>
</tr>
</tbody>
</table>

### RF接口<a name="ZH-CN_TOPIC_0000001456082744"></a>

RF接口如[表1](#table31902563)所示。

**表 1**  RF接口管脚列表

<a name="table31902563"></a>
<table><thead align="left"><tr id="row46341445"><th class="cellrowborder" valign="top" width="8.66%" id="mcps1.2.6.1.1"><p id="p9943125717166"><a name="p9943125717166"></a><a name="p9943125717166"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="26.1%" id="mcps1.2.6.1.2"><p id="p62669527"><a name="p62669527"></a><a name="p62669527"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="10.870000000000001%" id="mcps1.2.6.1.3"><p id="p65870306"><a name="p65870306"></a><a name="p65870306"></a>类型</p>
</th>
<th class="cellrowborder" valign="top" width="18.490000000000002%" id="mcps1.2.6.1.4"><p id="p33894570"><a name="p33894570"></a><a name="p33894570"></a>电平(V)</p>
</th>
<th class="cellrowborder" valign="top" width="35.88%" id="mcps1.2.6.1.5"><p id="p61105663"><a name="p61105663"></a><a name="p61105663"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row50611656"><td class="cellrowborder" valign="top" width="8.66%" headers="mcps1.2.6.1.1 "><p id="p11561117121714"><a name="p11561117121714"></a><a name="p11561117121714"></a>15</p>
</td>
<td class="cellrowborder" valign="top" width="26.1%" headers="mcps1.2.6.1.2 "><p id="p5903470"><a name="p5903470"></a><a name="p5903470"></a>WB_RFIO</p>
</td>
<td class="cellrowborder" valign="top" width="10.870000000000001%" headers="mcps1.2.6.1.3 "><p id="p10852974"><a name="p10852974"></a><a name="p10852974"></a>ANA</p>
</td>
<td class="cellrowborder" valign="top" width="18.490000000000002%" headers="mcps1.2.6.1.4 "><p id="p6675738"><a name="p6675738"></a><a name="p6675738"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="35.88%" headers="mcps1.2.6.1.5 "><p id="p3863873"><a name="p3863873"></a><a name="p3863873"></a>WLAN/BT/SLE 2.4G RF输入/输出。</p>
</td>
</tr>
</tbody>
</table>

### GND管脚<a name="ZH-CN_TOPIC_0000001505842473"></a>

GND管脚如[表1](#table1348700)所示。

**表 1**  GND管脚列表

<a name="table1348700"></a>
<table><thead align="left"><tr id="row12054440"><th class="cellrowborder" valign="top" width="9.84%" id="mcps1.2.5.1.1"><p id="p158028215213"><a name="p158028215213"></a><a name="p158028215213"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="29.64%" id="mcps1.2.5.1.2"><p id="p36885620"><a name="p36885620"></a><a name="p36885620"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="21.01%" id="mcps1.2.5.1.3"><p id="p11989863"><a name="p11989863"></a><a name="p11989863"></a>电压(V)</p>
</th>
<th class="cellrowborder" valign="top" width="39.51%" id="mcps1.2.5.1.4"><p id="p31654880"><a name="p31654880"></a><a name="p31654880"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row13908493"><td class="cellrowborder" valign="top" width="9.84%" headers="mcps1.2.5.1.1 "><p id="p195131731192118"><a name="p195131731192118"></a><a name="p195131731192118"></a>Epad</p>
</td>
<td class="cellrowborder" valign="top" width="29.64%" headers="mcps1.2.5.1.2 "><p id="p52846167"><a name="p52846167"></a><a name="p52846167"></a>GND</p>
</td>
<td class="cellrowborder" valign="top" width="21.01%" headers="mcps1.2.5.1.3 "><p id="p39312736"><a name="p39312736"></a><a name="p39312736"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="39.51%" headers="mcps1.2.5.1.4 "><p id="p30215023"><a name="p30215023"></a><a name="p30215023"></a>EPAD GND管脚。</p>
</td>
</tr>
</tbody>
</table>

### GPIO复用管脚<a name="ZH-CN_TOPIC_0000001456242644"></a>

GPIO（General Purpose Input/Output）管脚如[表1](#table14315403)所示。

>![](public_sys-resources/icon-note.gif) **说明：** 
>复用信号0为上电复位完成后的缺省功能。

**表 1**  GPIO复用管脚描述

<a name="table14315403"></a>
<table><thead align="left"><tr id="row14008765"><th class="cellrowborder" valign="top" width="7.130713071307132%" id="mcps1.2.7.1.1"><p id="p152550343110"><a name="p152550343110"></a><a name="p152550343110"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="13.281328132813282%" id="mcps1.2.7.1.2"><p id="p39473694"><a name="p39473694"></a><a name="p39473694"></a>管脚名称</p>
</th>
<th class="cellrowborder" valign="top" width="8.140814081408141%" id="mcps1.2.7.1.3"><p id="p43252647"><a name="p43252647"></a><a name="p43252647"></a>类型</p>
</th>
<th class="cellrowborder" valign="top" width="9.200920092009202%" id="mcps1.2.7.1.4"><p id="p13803553"><a name="p13803553"></a><a name="p13803553"></a>驱动(mA)</p>
</th>
<th class="cellrowborder" valign="top" width="17.261726172617266%" id="mcps1.2.7.1.5"><p id="p44346036"><a name="p44346036"></a><a name="p44346036"></a>电压(V)</p>
</th>
<th class="cellrowborder" valign="top" width="44.984498449844985%" id="mcps1.2.7.1.6"><p id="p35259143"><a name="p35259143"></a><a name="p35259143"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row37418306"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p1764965612111"><a name="p1764965612111"></a><a name="p1764965612111"></a>31</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p364955615118"><a name="p364955615118"></a><a name="p364955615118"></a>MGPIO0</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p9649165617118"><a name="p9649165617118"></a><a name="p9649165617118"></a>I<sub id="sub16283356104417"><a name="sub16283356104417"></a><a name="sub16283356104417"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p1564945611114"><a name="p1564945611114"></a><a name="p1564945611114"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p1064911561117"><a name="p1064911561117"></a><a name="p1064911561117"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p2064912568110"><a name="p2064912568110"></a><a name="p2064912568110"></a>复用信号1：SDIO_D2</p>
<p id="p155431325128"><a name="p155431325128"></a><a name="p155431325128"></a>复用信号0、2~7：保留</p>
</td>
</tr>
<tr id="row44077297"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p156496562114"><a name="p156496562114"></a><a name="p156496562114"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p146499568112"><a name="p146499568112"></a><a name="p146499568112"></a>MGPIO1</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p106491456113"><a name="p106491456113"></a><a name="p106491456113"></a>I<sub id="sub102841756204414"><a name="sub102841756204414"></a><a name="sub102841756204414"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p146491956817"><a name="p146491956817"></a><a name="p146491956817"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p1064914561715"><a name="p1064914561715"></a><a name="p1064914561715"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p71186344173"><a name="p71186344173"></a><a name="p71186344173"></a>复用信号1：SDIO_D3</p>
<p id="p10118234111715"><a name="p10118234111715"></a><a name="p10118234111715"></a>复用信号0、2~7：保留</p>
</td>
</tr>
<tr id="row43072099"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p174094374214"><a name="p174094374214"></a><a name="p174094374214"></a>33</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p1058056122516"><a name="p1058056122516"></a><a name="p1058056122516"></a>MGPIO2</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p240910371624"><a name="p240910371624"></a><a name="p240910371624"></a>I<sub id="sub1928465611443"><a name="sub1928465611443"></a><a name="sub1928465611443"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p16409143711216"><a name="p16409143711216"></a><a name="p16409143711216"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p15410123711214"><a name="p15410123711214"></a><a name="p15410123711214"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p184107371125"><a name="p184107371125"></a><a name="p184107371125"></a>复用信号0：MGPIO2</p>
<p id="p517712144269"><a name="p517712144269"></a><a name="p517712144269"></a>复用信号1：SDIO_CMD</p>
<p id="p1041043710214"><a name="p1041043710214"></a><a name="p1041043710214"></a>复用信号2：SPI0_DI</p>
<p id="p17410937228"><a name="p17410937228"></a><a name="p17410937228"></a>复用信号3~7：保留</p>
</td>
</tr>
<tr id="row41172271"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p11410153710218"><a name="p11410153710218"></a><a name="p11410153710218"></a>34</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p111206714342"><a name="p111206714342"></a><a name="p111206714342"></a>MGPIO3</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p1412010793416"><a name="p1412010793416"></a><a name="p1412010793416"></a>I<sub id="sub1428575618445"><a name="sub1428575618445"></a><a name="sub1428575618445"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p6120473347"><a name="p6120473347"></a><a name="p6120473347"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p71207719345"><a name="p71207719345"></a><a name="p71207719345"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p1312012713410"><a name="p1312012713410"></a><a name="p1312012713410"></a>复用信号0：MGPIO3</p>
<p id="p131201774343"><a name="p131201774343"></a><a name="p131201774343"></a>复用信号1：SDIO_CLK</p>
<p id="p1612013793415"><a name="p1612013793415"></a><a name="p1612013793415"></a>复用信号2：SPI0_CLK</p>
<p id="p12120127183412"><a name="p12120127183412"></a><a name="p12120127183412"></a>复用信号3~7：保留</p>
</td>
</tr>
<tr id="row38788755"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p941012372216"><a name="p941012372216"></a><a name="p941012372216"></a>35</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p8701190123515"><a name="p8701190123515"></a><a name="p8701190123515"></a>MGPIO4</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p1670170183514"><a name="p1670170183514"></a><a name="p1670170183514"></a>I<sub id="sub828585615446"><a name="sub828585615446"></a><a name="sub828585615446"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p177017013354"><a name="p177017013354"></a><a name="p177017013354"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p17010010352"><a name="p17010010352"></a><a name="p17010010352"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p270118033516"><a name="p270118033516"></a><a name="p270118033516"></a>复用信号0：MGPIO4</p>
<p id="p19701200103512"><a name="p19701200103512"></a><a name="p19701200103512"></a>复用信号1：SDIO_D0</p>
<p id="p1870118093510"><a name="p1870118093510"></a><a name="p1870118093510"></a>复用信号2：SPI0_DO</p>
<p id="p2701190183520"><a name="p2701190183520"></a><a name="p2701190183520"></a>复用信号3~7：保留</p>
</td>
</tr>
<tr id="row15167431"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p16520154817211"><a name="p16520154817211"></a><a name="p16520154817211"></a>36</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p1331205420357"><a name="p1331205420357"></a><a name="p1331205420357"></a>AGPIO5</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p193185453520"><a name="p193185453520"></a><a name="p193185453520"></a>I<sub id="sub2286456114420"><a name="sub2286456114420"></a><a name="sub2286456114420"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p103185453519"><a name="p103185453519"></a><a name="p103185453519"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p1431254193513"><a name="p1431254193513"></a><a name="p1431254193513"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p63195453511"><a name="p63195453511"></a><a name="p63195453511"></a>复用信号0：AGPIO5</p>
<p id="p16311954113511"><a name="p16311954113511"></a><a name="p16311954113511"></a>复用信号1：SDIO_D1</p>
<p id="p73118542352"><a name="p73118542352"></a><a name="p73118542352"></a>复用信号2：SPI0_CS0</p>
<p id="p143111541353"><a name="p143111541353"></a><a name="p143111541353"></a>复用信号3~7：保留</p>
</td>
</tr>
<tr id="row61804813"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p115207487218"><a name="p115207487218"></a><a name="p115207487218"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p1450710424363"><a name="p1450710424363"></a><a name="p1450710424363"></a>MGPIO5</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p1650814233612"><a name="p1650814233612"></a><a name="p1650814233612"></a>I<sub id="sub18286956174416"><a name="sub18286956174416"></a><a name="sub18286956174416"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p4508542143612"><a name="p4508542143612"></a><a name="p4508542143612"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p12508154217367"><a name="p12508154217367"></a><a name="p12508154217367"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p150804293620"><a name="p150804293620"></a><a name="p150804293620"></a>复用信号0：MGPIO5</p>
<p id="p10508114220363"><a name="p10508114220363"></a><a name="p10508114220363"></a>复用信号1：UART_H1_TXD</p>
<p id="p145081142193611"><a name="p145081142193611"></a><a name="p145081142193611"></a>复用信号2~7：保留</p>
<p id="p179513419421"><a name="p179513419421"></a><a name="p179513419421"></a>可复用做模拟管脚CLK_XOUT_32M</p>
</td>
</tr>
<tr id="row10722842"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p105218481623"><a name="p105218481623"></a><a name="p105218481623"></a>28</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p867631014389"><a name="p867631014389"></a><a name="p867631014389"></a>MGPIO6</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p10676131033812"><a name="p10676131033812"></a><a name="p10676131033812"></a>I<sub id="sub7287115624419"><a name="sub7287115624419"></a><a name="sub7287115624419"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p15676110193818"><a name="p15676110193818"></a><a name="p15676110193818"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p367610101389"><a name="p367610101389"></a><a name="p367610101389"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p96764102389"><a name="p96764102389"></a><a name="p96764102389"></a>复用信号0：MGPIO6</p>
<p id="p8676110143810"><a name="p8676110143810"></a><a name="p8676110143810"></a>复用信号1：UART_H0_RTS</p>
<p id="p567671017381"><a name="p567671017381"></a><a name="p567671017381"></a>复用信号2：SPI0_DI</p>
<p id="p6676161093818"><a name="p6676161093818"></a><a name="p6676161093818"></a>复用信号3：WB_GLP_SYNC_PULSE</p>
<p id="p106761010143812"><a name="p106761010143812"></a><a name="p106761010143812"></a>复用信号4~7：保留</p>
<p id="p178881347114210"><a name="p178881347114210"></a><a name="p178881347114210"></a>可复用做模拟管脚ADC_CH7</p>
</td>
</tr>
<tr id="row19289328"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p718219541822"><a name="p718219541822"></a><a name="p718219541822"></a>52</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p1091375593915"><a name="p1091375593915"></a><a name="p1091375593915"></a>MGPIO7</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p991365516392"><a name="p991365516392"></a><a name="p991365516392"></a>I<sub id="sub1028755618441"><a name="sub1028755618441"></a><a name="sub1028755618441"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p169131855153911"><a name="p169131855153911"></a><a name="p169131855153911"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p159131955103916"><a name="p159131955103916"></a><a name="p159131955103916"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p1491315513393"><a name="p1491315513393"></a><a name="p1491315513393"></a>复用信号0：MGPIO7</p>
<p id="p16914105518394"><a name="p16914105518394"></a><a name="p16914105518394"></a>复用信号1：UART_H0_CTS</p>
<p id="p1091414551394"><a name="p1091414551394"></a><a name="p1091414551394"></a>复用信号2：SPI0_CS0</p>
<p id="p1591412553394"><a name="p1591412553394"></a><a name="p1591412553394"></a>复用信号3：QSPI1_D2</p>
<p id="p491465553910"><a name="p491465553910"></a><a name="p491465553910"></a>复用信号6：ANT_SEL2</p>
<p id="p149141855123911"><a name="p149141855123911"></a><a name="p149141855123911"></a>复用信号7：保留</p>
</td>
</tr>
<tr id="row22868878"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p918220543213"><a name="p918220543213"></a><a name="p918220543213"></a>26</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p9182175418216"><a name="p9182175418216"></a><a name="p9182175418216"></a>MGPIO8</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p1618265418213"><a name="p1618265418213"></a><a name="p1618265418213"></a>I<sub id="sub1288185664412"><a name="sub1288185664412"></a><a name="sub1288185664412"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p12183165410216"><a name="p12183165410216"></a><a name="p12183165410216"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p1618335412215"><a name="p1618335412215"></a><a name="p1618335412215"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p118316547211"><a name="p118316547211"></a><a name="p118316547211"></a>复用信号0：MGPIO8</p>
<p id="p1518310541825"><a name="p1518310541825"></a><a name="p1518310541825"></a>复用信号1：UART_H0_TXD</p>
<p id="p818316541228"><a name="p818316541228"></a><a name="p818316541228"></a>复用信号2：SPI0_CLK</p>
<p id="p1418310541521"><a name="p1418310541521"></a><a name="p1418310541521"></a>复用信号3：I2C1_SCL</p>
<p id="p61835542216"><a name="p61835542216"></a><a name="p61835542216"></a>复用信号4~7：保留</p>
<p id="p145014286475"><a name="p145014286475"></a><a name="p145014286475"></a>可复用做模拟管脚ADC_CH5</p>
</td>
</tr>
<tr id="row34715636"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p61833541321"><a name="p61833541321"></a><a name="p61833541321"></a>27</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p1318385413212"><a name="p1318385413212"></a><a name="p1318385413212"></a>MGPIO9</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p11834541423"><a name="p11834541423"></a><a name="p11834541423"></a>I<sub id="sub1528814564449"><a name="sub1528814564449"></a><a name="sub1528814564449"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p19183195415210"><a name="p19183195415210"></a><a name="p19183195415210"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p21831054125"><a name="p21831054125"></a><a name="p21831054125"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p818316547212"><a name="p818316547212"></a><a name="p818316547212"></a>复用信号0：MGPIO9</p>
<p id="p718318543210"><a name="p718318543210"></a><a name="p718318543210"></a>复用信号1：UART_H0_RXD</p>
<p id="p1396313017470"><a name="p1396313017470"></a><a name="p1396313017470"></a>复用信号2：SPI0_DO</p>
<p id="p940653619476"><a name="p940653619476"></a><a name="p940653619476"></a>复用信号3：I2C1_SDA</p>
<p id="p141831654229"><a name="p141831654229"></a><a name="p141831654229"></a>复用信号4~7：保留</p>
<p id="p1788619347102"><a name="p1788619347102"></a><a name="p1788619347102"></a>可复用做模拟管脚ADC_CH6</p>
</td>
</tr>
<tr id="row43212834"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p7622195917211"><a name="p7622195917211"></a><a name="p7622195917211"></a>21</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p163971139171215"><a name="p163971139171215"></a><a name="p163971139171215"></a>MGPIO10</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p14397739191217"><a name="p14397739191217"></a><a name="p14397739191217"></a>I<sub id="sub1528935614441"><a name="sub1528935614441"></a><a name="sub1528935614441"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p19397339151214"><a name="p19397339151214"></a><a name="p19397339151214"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p14397739151217"><a name="p14397739151217"></a><a name="p14397739151217"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p163975395127"><a name="p163975395127"></a><a name="p163975395127"></a>复用信号0：MGPIO10</p>
<p id="p341320871318"><a name="p341320871318"></a><a name="p341320871318"></a>复用信号1：SPI0_CS0</p>
<p id="p1932717112134"><a name="p1932717112134"></a><a name="p1932717112134"></a>复用信号2：UART_H1_CTS</p>
<p id="p13397133901217"><a name="p13397133901217"></a><a name="p13397133901217"></a>复用信号4：PWM0P</p>
<p id="p039703971217"><a name="p039703971217"></a><a name="p039703971217"></a>复用信号5：I2S_WS</p>
<p id="p0397739181210"><a name="p0397739181210"></a><a name="p0397739181210"></a>复用信号6：ANT_SEL3</p>
<p id="p339793911124"><a name="p339793911124"></a><a name="p339793911124"></a>复用信号7：保留</p>
</td>
</tr>
<tr id="row27184073"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p12623559125"><a name="p12623559125"></a><a name="p12623559125"></a>22</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p162312591324"><a name="p162312591324"></a><a name="p162312591324"></a>MGPIO11</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p126231059529"><a name="p126231059529"></a><a name="p126231059529"></a>I<sub id="sub192901456184414"><a name="sub192901456184414"></a><a name="sub192901456184414"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p1362315920219"><a name="p1362315920219"></a><a name="p1362315920219"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p562312591727"><a name="p562312591727"></a><a name="p562312591727"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p662395917211"><a name="p662395917211"></a><a name="p662395917211"></a>复用信号0：MGPIO11</p>
<p id="p136231559826"><a name="p136231559826"></a><a name="p136231559826"></a>复用信号1：SPI0_CLK</p>
<p id="p662313599219"><a name="p662313599219"></a><a name="p662313599219"></a>复用信号2：UART_H1_RTS</p>
<p id="p7623175914210"><a name="p7623175914210"></a><a name="p7623175914210"></a>复用信号4：PWM0N</p>
<p id="p106235591520"><a name="p106235591520"></a><a name="p106235591520"></a>复用信号5：I2S_BCLK</p>
<p id="p06235591216"><a name="p06235591216"></a><a name="p06235591216"></a>复用信号6~7：保留</p>
</td>
</tr>
<tr id="row56350302"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p662316599217"><a name="p662316599217"></a><a name="p662316599217"></a>23</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p2062317591226"><a name="p2062317591226"></a><a name="p2062317591226"></a>MGPIO12</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p8623185920217"><a name="p8623185920217"></a><a name="p8623185920217"></a>I<sub id="sub1729013569447"><a name="sub1729013569447"></a><a name="sub1729013569447"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p1623175916215"><a name="p1623175916215"></a><a name="p1623175916215"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p862320591218"><a name="p862320591218"></a><a name="p862320591218"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p562311591214"><a name="p562311591214"></a><a name="p562311591214"></a>复用信号0：MGPIO12</p>
<p id="p762335917220"><a name="p762335917220"></a><a name="p762335917220"></a>复用信号1：SPI0_DI</p>
<p id="p8623115912218"><a name="p8623115912218"></a><a name="p8623115912218"></a>复用信号2：UART_H1_TXD</p>
<p id="p062313591224"><a name="p062313591224"></a><a name="p062313591224"></a>复用信号5：I2S_DI</p>
<p id="p162395917216"><a name="p162395917216"></a><a name="p162395917216"></a>复用信号6：ANT_SEL4</p>
<p id="p156239599212"><a name="p156239599212"></a><a name="p156239599212"></a>复用信号7：保留</p>
</td>
</tr>
<tr id="row1985618037"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p177384513319"><a name="p177384513319"></a><a name="p177384513319"></a>24</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p97387511331"><a name="p97387511331"></a><a name="p97387511331"></a>MGPIO13</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p197384511313"><a name="p197384511313"></a><a name="p197384511313"></a>I<sub id="sub8291165611445"><a name="sub8291165611445"></a><a name="sub8291165611445"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p57386515311"><a name="p57386515311"></a><a name="p57386515311"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p273815511132"><a name="p273815511132"></a><a name="p273815511132"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p20906587228"><a name="p20906587228"></a><a name="p20906587228"></a>复用信号0：MGPIO13</p>
<p id="p5906089222"><a name="p5906089222"></a><a name="p5906089222"></a>复用信号1：SPI0_DO</p>
<p id="p1390617812225"><a name="p1390617812225"></a><a name="p1390617812225"></a>复用信号2：UART_H1_RXD</p>
<p id="p1490612812213"><a name="p1490612812213"></a><a name="p1490612812213"></a>复用信号3：I2C0_SCL</p>
<p id="p1090613882215"><a name="p1090613882215"></a><a name="p1090613882215"></a>复用信号5：I2S_DO</p>
<p id="p189060832211"><a name="p189060832211"></a><a name="p189060832211"></a>复用信号6~7：保留</p>
</td>
</tr>
<tr id="row102803215314"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p20738851831"><a name="p20738851831"></a><a name="p20738851831"></a>25</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p1573815511231"><a name="p1573815511231"></a><a name="p1573815511231"></a>MGPIO14</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p97381151538"><a name="p97381151538"></a><a name="p97381151538"></a>I<sub id="sub1729195624417"><a name="sub1729195624417"></a><a name="sub1729195624417"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p1273815113312"><a name="p1273815113312"></a><a name="p1273815113312"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p67381651036"><a name="p67381651036"></a><a name="p67381651036"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p1274012231346"><a name="p1274012231346"></a><a name="p1274012231346"></a>复用信号0：MGPIO14</p>
<p id="p107151224944"><a name="p107151224944"></a><a name="p107151224944"></a>复用信号1：SPWM1N</p>
<p id="p208966261413"><a name="p208966261413"></a><a name="p208966261413"></a>复用信号2：I2C0_SDA</p>
<p id="p164741428346"><a name="p164741428346"></a><a name="p164741428346"></a>复用信号3：WB_GLP_SYNC_PULSE</p>
<p id="p3345172916410"><a name="p3345172916410"></a><a name="p3345172916410"></a>复用信号4：BT_ACTIVE</p>
<p id="p1718818301446"><a name="p1718818301446"></a><a name="p1718818301446"></a>复用信号5：UART_H0_CTS</p>
<p id="p6738851639"><a name="p6738851639"></a><a name="p6738851639"></a>复用信号6：保留</p>
</td>
</tr>
<tr id="row195519269310"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p137383511332"><a name="p137383511332"></a><a name="p137383511332"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p1273815511731"><a name="p1273815511731"></a><a name="p1273815511731"></a>MGPIO15</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p37388515314"><a name="p37388515314"></a><a name="p37388515314"></a>I<sub id="sub182920568445"><a name="sub182920568445"></a><a name="sub182920568445"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p1473910511335"><a name="p1473910511335"></a><a name="p1473910511335"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p5739951737"><a name="p5739951737"></a><a name="p5739951737"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p143461625192517"><a name="p143461625192517"></a><a name="p143461625192517"></a>复用信号0：MGPIO15</p>
<p id="p113461425142512"><a name="p113461425142512"></a><a name="p113461425142512"></a>复用信号1：SPWM1P</p>
<p id="p19346132514257"><a name="p19346132514257"></a><a name="p19346132514257"></a>复用信号2：BT_STATUS</p>
<p id="p133466255251"><a name="p133466255251"></a><a name="p133466255251"></a>复用信号3：UART_H1_RTS</p>
<p id="p153461425192518"><a name="p153461425192518"></a><a name="p153461425192518"></a>复用信号4：保留</p>
</td>
</tr>
<tr id="row1855119261531"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p17391751838"><a name="p17391751838"></a><a name="p17391751838"></a>47</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p12931419277"><a name="p12931419277"></a><a name="p12931419277"></a>MGPIO16</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p12910141275"><a name="p12910141275"></a><a name="p12910141275"></a>I<sub id="sub162927565444"><a name="sub162927565444"></a><a name="sub162927565444"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p4291914132719"><a name="p4291914132719"></a><a name="p4291914132719"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p192921411272"><a name="p192921411272"></a><a name="p192921411272"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p33471832152712"><a name="p33471832152712"></a><a name="p33471832152712"></a>复用信号0：MGPIO16</p>
<p id="p729214182712"><a name="p729214182712"></a><a name="p729214182712"></a>复用信号1：QSPI1_D3</p>
<p id="p172914145277"><a name="p172914145277"></a><a name="p172914145277"></a>复用信号2：PWM3N</p>
<p id="p1229214192710"><a name="p1229214192710"></a><a name="p1229214192710"></a>复用信号3~7：保留</p>
</td>
</tr>
<tr id="row1527783717310"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p3739951130"><a name="p3739951130"></a><a name="p3739951130"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p3963115193319"><a name="p3963115193319"></a><a name="p3963115193319"></a>MGPIO17</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p1496355119336"><a name="p1496355119336"></a><a name="p1496355119336"></a>I<sub id="sub929355620444"><a name="sub929355620444"></a><a name="sub929355620444"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p169631651103311"><a name="p169631651103311"></a><a name="p169631651103311"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p13963145133315"><a name="p13963145133315"></a><a name="p13963145133315"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p1096315113312"><a name="p1096315113312"></a><a name="p1096315113312"></a>复用信号0：MGPIO17</p>
<p id="p11963651193315"><a name="p11963651193315"></a><a name="p11963651193315"></a>复用信号1：QSPI1_CLK</p>
<p id="p1096345117333"><a name="p1096345117333"></a><a name="p1096345117333"></a>复用信号2：UART_H0_TXD</p>
<p id="p596345123312"><a name="p596345123312"></a><a name="p596345123312"></a>复用信号3：I2S_BCLK</p>
<p id="p19963195113319"><a name="p19963195113319"></a><a name="p19963195113319"></a>复用信号5：BT_ACTIVE</p>
<p id="p199631851173313"><a name="p199631851173313"></a><a name="p199631851173313"></a>复用信号6~7：保留</p>
</td>
</tr>
<tr id="row1127819372312"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p187391511433"><a name="p187391511433"></a><a name="p187391511433"></a>49</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p36621251356"><a name="p36621251356"></a><a name="p36621251356"></a>MGPIO18</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p1366242511353"><a name="p1366242511353"></a><a name="p1366242511353"></a>I<sub id="sub17293155612449"><a name="sub17293155612449"></a><a name="sub17293155612449"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p1666216251358"><a name="p1666216251358"></a><a name="p1666216251358"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p14663172515352"><a name="p14663172515352"></a><a name="p14663172515352"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p176631225123515"><a name="p176631225123515"></a><a name="p176631225123515"></a>复用信号0：MGPIO18</p>
<p id="p566352510355"><a name="p566352510355"></a><a name="p566352510355"></a>复用信号1：QSPI1_D0</p>
<p id="p566342553517"><a name="p566342553517"></a><a name="p566342553517"></a>复用信号2：UART_H0_RXD</p>
<p id="p56631025163513"><a name="p56631025163513"></a><a name="p56631025163513"></a>复用信号3：I2S_DO</p>
<p id="p9663112517353"><a name="p9663112517353"></a><a name="p9663112517353"></a>复用信号4：WB_GLP_SYC_PULSE</p>
<p id="p1566342583513"><a name="p1566342583513"></a><a name="p1566342583513"></a>复用信号5：BT_STATUS</p>
<p id="p146631225123515"><a name="p146631225123515"></a><a name="p146631225123515"></a>复用信号6~7：保留</p>
</td>
</tr>
<tr id="row1727818373318"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p19739351238"><a name="p19739351238"></a><a name="p19739351238"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p19333239163612"><a name="p19333239163612"></a><a name="p19333239163612"></a>MGPIO19</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p633323914367"><a name="p633323914367"></a><a name="p633323914367"></a>I<sub id="sub152941856104417"><a name="sub152941856104417"></a><a name="sub152941856104417"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p19333103923615"><a name="p19333103923615"></a><a name="p19333103923615"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p73332394368"><a name="p73332394368"></a><a name="p73332394368"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p2333153913363"><a name="p2333153913363"></a><a name="p2333153913363"></a>复用信号0：MGPIO19</p>
<p id="p18333123915368"><a name="p18333123915368"></a><a name="p18333123915368"></a>复用信号1：QSPI1_D1</p>
<p id="p23331392364"><a name="p23331392364"></a><a name="p23331392364"></a>复用信号2：PWM2P</p>
<p id="p123332039123617"><a name="p123332039123617"></a><a name="p123332039123617"></a>复用信号3：I2S_DI</p>
<p id="p1433303913620"><a name="p1433303913620"></a><a name="p1433303913620"></a>复用信号5：BT_FREQ</p>
<p id="p933314391364"><a name="p933314391364"></a><a name="p933314391364"></a>复用信号6~7：保留</p>
</td>
</tr>
<tr id="row12785377319"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p1673920514315"><a name="p1673920514315"></a><a name="p1673920514315"></a>51</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p1473925118318"><a name="p1473925118318"></a><a name="p1473925118318"></a>MGPIO20</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p673935115311"><a name="p673935115311"></a><a name="p673935115311"></a>I<sub id="sub112945565445"><a name="sub112945565445"></a><a name="sub112945565445"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p4739105111316"><a name="p4739105111316"></a><a name="p4739105111316"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p137396512310"><a name="p137396512310"></a><a name="p137396512310"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p107853353406"><a name="p107853353406"></a><a name="p107853353406"></a>复用信号0：MGPIO20</p>
<p id="p19785113512409"><a name="p19785113512409"></a><a name="p19785113512409"></a>复用信号1：QSPI1_CS</p>
<p id="p167857352406"><a name="p167857352406"></a><a name="p167857352406"></a>复用信号2：PWM2N</p>
<p id="p19785103514011"><a name="p19785103514011"></a><a name="p19785103514011"></a>复用信号3：I2S_WS</p>
<p id="p17851635104012"><a name="p17851635104012"></a><a name="p17851635104012"></a>复用信号5：WLAN_ACTIVE</p>
<p id="p329618801314"><a name="p329618801314"></a><a name="p329618801314"></a>复用信号6~7：保留</p>
</td>
</tr>
<tr id="row289312304312"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p1973910515311"><a name="p1973910515311"></a><a name="p1973910515311"></a>46</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p4105534114116"><a name="p4105534114116"></a><a name="p4105534114116"></a>MGPIO21</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p1810563414415"><a name="p1810563414415"></a><a name="p1810563414415"></a>I<sub id="sub52951556154416"><a name="sub52951556154416"></a><a name="sub52951556154416"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p410653415413"><a name="p410653415413"></a><a name="p410653415413"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p1106734194118"><a name="p1106734194118"></a><a name="p1106734194118"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p1910663404111"><a name="p1910663404111"></a><a name="p1910663404111"></a>复用信号0：MGPIO21</p>
<p id="p8106203413417"><a name="p8106203413417"></a><a name="p8106203413417"></a>复用信号1：PWM0P</p>
<p id="p810663411413"><a name="p810663411413"></a><a name="p810663411413"></a>复用信号2：UART_H0_RTS</p>
<p id="p1810673474117"><a name="p1810673474117"></a><a name="p1810673474117"></a>复用信号3：I2C0_SCL</p>
<p id="p13106193474117"><a name="p13106193474117"></a><a name="p13106193474117"></a>复用信号4：WB_GLP_SYNC_PULSE</p>
<p id="p1310611343417"><a name="p1310611343417"></a><a name="p1310611343417"></a>复用信号5：BT_STATUS</p>
<p id="p2256429121319"><a name="p2256429121319"></a><a name="p2256429121319"></a>复用信号6~7：保留</p>
</td>
</tr>
<tr id="row8893113010317"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p173911511335"><a name="p173911511335"></a><a name="p173911511335"></a>43</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p1385884716425"><a name="p1385884716425"></a><a name="p1385884716425"></a>MGPIO22</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p885864716429"><a name="p885864716429"></a><a name="p885864716429"></a>I<sub id="sub929525634413"><a name="sub929525634413"></a><a name="sub929525634413"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p118581247174215"><a name="p118581247174215"></a><a name="p118581247174215"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p385812476427"><a name="p385812476427"></a><a name="p385812476427"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p11858647124212"><a name="p11858647124212"></a><a name="p11858647124212"></a>复用信号0：MGPIO22</p>
<p id="p1285824754218"><a name="p1285824754218"></a><a name="p1285824754218"></a>复用信号1：PWM3P</p>
<p id="p28581947194211"><a name="p28581947194211"></a><a name="p28581947194211"></a>复用信号2：UART_H1_CTS</p>
<p id="p138582471421"><a name="p138582471421"></a><a name="p138582471421"></a>复用信号3：I2C0_SDA</p>
<p id="p785854784214"><a name="p785854784214"></a><a name="p785854784214"></a>复用信号5：WLAN_ACTIVE</p>
<p id="p58581047164219"><a name="p58581047164219"></a><a name="p58581047164219"></a>复用信号6：ANT_SEL5</p>
<p id="p3858124724210"><a name="p3858124724210"></a><a name="p3858124724210"></a>复用信号7：保留</p>
<p id="p1056420249525"><a name="p1056420249525"></a><a name="p1056420249525"></a>可复用做模拟管脚ADC_CH4</p>
</td>
</tr>
<tr id="row3683502310"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p973965115311"><a name="p973965115311"></a><a name="p973965115311"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p774045111311"><a name="p774045111311"></a><a name="p774045111311"></a>AGPIO1</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p2074065120318"><a name="p2074065120318"></a><a name="p2074065120318"></a>I<sub id="sub18296125618442"><a name="sub18296125618442"></a><a name="sub18296125618442"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p97401511538"><a name="p97401511538"></a><a name="p97401511538"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p1574015113319"><a name="p1574015113319"></a><a name="p1574015113319"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p1822413154614"><a name="p1822413154614"></a><a name="p1822413154614"></a>复用信号0：AGPIO1</p>
<p id="p433617161369"><a name="p433617161369"></a><a name="p433617161369"></a>复用信号1：UART_L0_TXD</p>
<p id="p96269174619"><a name="p96269174619"></a><a name="p96269174619"></a>复用信号2~7：保留</p>
<p id="p17138455155211"><a name="p17138455155211"></a><a name="p17138455155211"></a>可复用做模拟管脚ADC_CH0</p>
</td>
</tr>
<tr id="row176813501537"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p374017518311"><a name="p374017518311"></a><a name="p374017518311"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p149151295443"><a name="p149151295443"></a><a name="p149151295443"></a>AGPIO2</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p14915182917443"><a name="p14915182917443"></a><a name="p14915182917443"></a>I<sub id="sub10296656154411"><a name="sub10296656154411"></a><a name="sub10296656154411"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p6915152914411"><a name="p6915152914411"></a><a name="p6915152914411"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p1991572924415"><a name="p1991572924415"></a><a name="p1991572924415"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p4915102964415"><a name="p4915102964415"></a><a name="p4915102964415"></a>复用信号0：AGPIO2</p>
<p id="p4915192917449"><a name="p4915192917449"></a><a name="p4915192917449"></a>复用信号1：UART_L0_RXD</p>
<p id="p189151029194418"><a name="p189151029194418"></a><a name="p189151029194418"></a>复用信号2：PWM0P</p>
<p id="p12915429134416"><a name="p12915429134416"></a><a name="p12915429134416"></a>复用信号3~7：保留</p>
</td>
</tr>
<tr id="row26814501835"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p187403511037"><a name="p187403511037"></a><a name="p187403511037"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p03411452154414"><a name="p03411452154414"></a><a name="p03411452154414"></a>AGPIO3</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p1634117524443"><a name="p1634117524443"></a><a name="p1634117524443"></a>I<sub id="sub629819561444"><a name="sub629819561444"></a><a name="sub629819561444"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p9341352124416"><a name="p9341352124416"></a><a name="p9341352124416"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p934113521447"><a name="p934113521447"></a><a name="p934113521447"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p19342145211445"><a name="p19342145211445"></a><a name="p19342145211445"></a>复用信号0：AGPIO3</p>
<p id="p13421952204414"><a name="p13421952204414"></a><a name="p13421952204414"></a>复用信号1：I2C1_SCL</p>
<p id="p134213522444"><a name="p134213522444"></a><a name="p134213522444"></a>复用信号2：PWM0N</p>
<p id="p834219522444"><a name="p834219522444"></a><a name="p834219522444"></a>复用信号3~7：保留</p>
<p id="p483682195318"><a name="p483682195318"></a><a name="p483682195318"></a>可复用做模拟管脚ADC_CH1</p>
</td>
</tr>
<tr id="row36815502319"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p4740195119316"><a name="p4740195119316"></a><a name="p4740195119316"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p15881172444518"><a name="p15881172444518"></a><a name="p15881172444518"></a>AGPIO4</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p11881824144510"><a name="p11881824144510"></a><a name="p11881824144510"></a>I<sub id="sub1729865694415"><a name="sub1729865694415"></a><a name="sub1729865694415"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p168811624164514"><a name="p168811624164514"></a><a name="p168811624164514"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p138811424174516"><a name="p138811424174516"></a><a name="p138811424174516"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p98818245457"><a name="p98818245457"></a><a name="p98818245457"></a>复用信号0：AGPIO4</p>
<p id="p11881112412455"><a name="p11881112412455"></a><a name="p11881112412455"></a>复用信号1：I2C1_SDA</p>
<p id="p1288142474510"><a name="p1288142474510"></a><a name="p1288142474510"></a>复用信号2：UART_H1_RXD</p>
<p id="p6881162424516"><a name="p6881162424516"></a><a name="p6881162424516"></a>复用信号3~7：保留</p>
<p id="p8503131215532"><a name="p8503131215532"></a><a name="p8503131215532"></a>可复用做模拟管脚ADC_CH2</p>
</td>
</tr>
<tr id="row12691501136"><td class="cellrowborder" valign="top" width="7.130713071307132%" headers="mcps1.2.7.1.1 "><p id="p13740125116311"><a name="p13740125116311"></a><a name="p13740125116311"></a>29</p>
</td>
<td class="cellrowborder" valign="top" width="13.281328132813282%" headers="mcps1.2.7.1.2 "><p id="p693844554715"><a name="p693844554715"></a><a name="p693844554715"></a>RST_N</p>
</td>
<td class="cellrowborder" valign="top" width="8.140814081408141%" headers="mcps1.2.7.1.3 "><p id="p09382454473"><a name="p09382454473"></a><a name="p09382454473"></a>I<sub id="sub142991856144412"><a name="sub142991856144412"></a><a name="sub142991856144412"></a>SPU</sub>/O</p>
</td>
<td class="cellrowborder" valign="top" width="9.200920092009202%" headers="mcps1.2.7.1.4 "><p id="p2093813451479"><a name="p2093813451479"></a><a name="p2093813451479"></a>可配置</p>
</td>
<td class="cellrowborder" valign="top" width="17.261726172617266%" headers="mcps1.2.7.1.5 "><p id="p493814456474"><a name="p493814456474"></a><a name="p493814456474"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.984498449844985%" headers="mcps1.2.7.1.6 "><p id="p17938245104712"><a name="p17938245104712"></a><a name="p17938245104712"></a>全局复位信号</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-notice.gif) **须知：** 
>在使用SDIO一线模式时，SDIO\_D2和SDIO\_D3需要保持悬空状态，不能复用为其他功能.

### CLK管脚<a name="ZH-CN_TOPIC_0000001505722833"></a>

CLK管脚如[表1](#table54948942)所示。

**表 1**  CLK管脚描述

<a name="table54948942"></a>
<table><thead align="left"><tr id="row16544703"><th class="cellrowborder" valign="top" width="10%" id="mcps1.2.6.1.1"><p id="p65052577"><a name="p65052577"></a><a name="p65052577"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="22.5%" id="mcps1.2.6.1.2"><p id="p34767408"><a name="p34767408"></a><a name="p34767408"></a>管脚名称</p>
</th>
<th class="cellrowborder" valign="top" width="16.25%" id="mcps1.2.6.1.3"><p id="p64696659"><a name="p64696659"></a><a name="p64696659"></a>类型</p>
</th>
<th class="cellrowborder" valign="top" width="16.34%" id="mcps1.2.6.1.4"><p id="p11218807"><a name="p11218807"></a><a name="p11218807"></a>电压(V)</p>
</th>
<th class="cellrowborder" valign="top" width="34.910000000000004%" id="mcps1.2.6.1.5"><p id="p36308168"><a name="p36308168"></a><a name="p36308168"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row25236858"><td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.1 "><p id="p30919631"><a name="p30919631"></a><a name="p30919631"></a>7</p>
</td>
<td class="cellrowborder" valign="top" width="22.5%" headers="mcps1.2.6.1.2 "><p id="p21462168"><a name="p21462168"></a><a name="p21462168"></a>XOUT</p>
</td>
<td class="cellrowborder" valign="top" width="16.25%" headers="mcps1.2.6.1.3 "><p id="p60714046"><a name="p60714046"></a><a name="p60714046"></a>O</p>
</td>
<td class="cellrowborder" valign="top" width="16.34%" headers="mcps1.2.6.1.4 "><p id="p53748798"><a name="p53748798"></a><a name="p53748798"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="34.910000000000004%" headers="mcps1.2.6.1.5 "><p id="p58685418"><a name="p58685418"></a><a name="p58685418"></a>晶体时钟引脚</p>
</td>
</tr>
<tr id="row146681559189"><td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.6.1.1 "><p id="p27762102"><a name="p27762102"></a><a name="p27762102"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="22.5%" headers="mcps1.2.6.1.2 "><p id="p34137829"><a name="p34137829"></a><a name="p34137829"></a>XIN</p>
</td>
<td class="cellrowborder" valign="top" width="16.25%" headers="mcps1.2.6.1.3 "><p id="p13700797"><a name="p13700797"></a><a name="p13700797"></a>I</p>
</td>
<td class="cellrowborder" valign="top" width="16.34%" headers="mcps1.2.6.1.4 "><p id="p32162181"><a name="p32162181"></a><a name="p32162181"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="34.910000000000004%" headers="mcps1.2.6.1.5 "><p id="p256246121011"><a name="p256246121011"></a><a name="p256246121011"></a>晶体时钟引脚</p>
</td>
</tr>
</tbody>
</table>

## 上电关键硬件字<a name="ZH-CN_TOPIC_0000001505603557"></a>

芯片系统正常启动后必须有正确的硬件配置字，与芯片硬件启动强相关，其电平状态需如[表1](#table41337601)所示。

**表 1**  管脚硬件配置字描述

<a name="table41337601"></a>
<table><thead align="left"><tr id="row7972012"><th class="cellrowborder" valign="top" width="8.74%" id="mcps1.2.5.1.1"><p id="p7592133014177"><a name="p7592133014177"></a><a name="p7592133014177"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="15.329999999999998%" id="mcps1.2.5.1.2"><p id="p14180144061811"><a name="p14180144061811"></a><a name="p14180144061811"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="43.1%" id="mcps1.2.5.1.3"><p id="p146987270477"><a name="p146987270477"></a><a name="p146987270477"></a>低电平</p>
</th>
<th class="cellrowborder" valign="top" width="32.83%" id="mcps1.2.5.1.4"><p id="p169872711472"><a name="p169872711472"></a><a name="p169872711472"></a>高电平</p>
</th>
</tr>
</thead>
<tbody><tr id="row52757779"><td class="cellrowborder" valign="top" width="8.74%" headers="mcps1.2.5.1.1 "><p id="p1159312305175"><a name="p1159312305175"></a><a name="p1159312305175"></a>25</p>
</td>
<td class="cellrowborder" valign="top" width="15.329999999999998%" headers="mcps1.2.5.1.2 "><p id="p5180104012183"><a name="p5180104012183"></a><a name="p5180104012183"></a>MGPIO14</p>
</td>
<td class="cellrowborder" valign="top" width="43.1%" headers="mcps1.2.5.1.3 "><p id="p6699327184711"><a name="p6699327184711"></a><a name="p6699327184711"></a>正常启动</p>
</td>
<td class="cellrowborder" valign="top" width="32.83%" headers="mcps1.2.5.1.4 "><p id="p1069910271474"><a name="p1069910271474"></a><a name="p1069910271474"></a>禁用</p>
</td>
</tr>
<tr id="row32802119"><td class="cellrowborder" valign="top" width="8.74%" headers="mcps1.2.5.1.1 "><p id="p10593113016178"><a name="p10593113016178"></a><a name="p10593113016178"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="15.329999999999998%" headers="mcps1.2.5.1.2 "><p id="p101801440111817"><a name="p101801440111817"></a><a name="p101801440111817"></a>MGPIO15</p>
</td>
<td class="cellrowborder" valign="top" width="43.1%" headers="mcps1.2.5.1.3 "><p id="p356555471"><a name="p356555471"></a><a name="p356555471"></a>正常启动</p>
</td>
<td class="cellrowborder" valign="top" width="32.83%" headers="mcps1.2.5.1.4 "><p id="p1818211054915"><a name="p1818211054915"></a><a name="p1818211054915"></a>禁用</p>
</td>
</tr>
</tbody>
</table>

# 电性能参数<a name="ZH-CN_TOPIC_0000001505603521"></a>

-   **[电流分布](#ZH-CN_TOPIC_0000001505842489)**  

-   **[极限工作电压](#ZH-CN_TOPIC_0000001505722809)**  

-   **[推荐工作条件](#ZH-CN_TOPIC_0000001456242628)**  

-   **[DC/AC电气参数](#ZH-CN_TOPIC_0000001455763064)**  

-   **[上下电要求](#ZH-CN_TOPIC_0000001762979362)**  

## 电流分布<a name="ZH-CN_TOPIC_0000001505842489"></a>

WS53V100的功耗分布如[表1](#toc257211771)所示。

**表 1**  电流参数

<a name="toc257211771"></a>
<table><thead align="left"><tr id="row39012433"><th class="cellrowborder" valign="top" width="9.33%" id="mcps1.2.8.1.1"><p id="p3681530154018"><a name="p3681530154018"></a><a name="p3681530154018"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="20.96%" id="mcps1.2.8.1.2"><p id="p5890479"><a name="p5890479"></a><a name="p5890479"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="37.25%" id="mcps1.2.8.1.3"><p id="p7366757"><a name="p7366757"></a><a name="p7366757"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="8.37%" id="mcps1.2.8.1.4"><p id="p59836444"><a name="p59836444"></a><a name="p59836444"></a>最小值</p>
</th>
<th class="cellrowborder" valign="top" width="8.88%" id="mcps1.2.8.1.5"><p id="p14913787"><a name="p14913787"></a><a name="p14913787"></a>典型值</p>
</th>
<th class="cellrowborder" valign="top" width="8.35%" id="mcps1.2.8.1.6"><p id="p57259"><a name="p57259"></a><a name="p57259"></a>最大值</p>
</th>
<th class="cellrowborder" valign="top" width="6.859999999999999%" id="mcps1.2.8.1.7"><p id="p4638036"><a name="p4638036"></a><a name="p4638036"></a>单位</p>
</th>
</tr>
</thead>
<tbody><tr id="row8691190"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p1837111282416"><a name="p1837111282416"></a><a name="p1837111282416"></a>9</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p837132814416"><a name="p837132814416"></a><a name="p837132814416"></a>VDD_VBAT2</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p725915975112"><a name="p725915975112"></a><a name="p725915975112"></a>INTLDO和XLDO输入电源，由板级提供3.3V电源</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p7526153915411"><a name="p7526153915411"></a><a name="p7526153915411"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p4371028134115"><a name="p4371028134115"></a><a name="p4371028134115"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p1237182864117"><a name="p1237182864117"></a><a name="p1237182864117"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p58800757"><a name="p58800757"></a><a name="p58800757"></a>mA</p>
</td>
</tr>
<tr id="row15503917153513"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p1837192854116"><a name="p1837192854116"></a><a name="p1837192854116"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p143719287417"><a name="p143719287417"></a><a name="p143719287417"></a>VDD_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p14259559125113"><a name="p14259559125113"></a><a name="p14259559125113"></a>1.3V电压输入，RFLDO1，RFLDO2输入电源</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p12526113964118"><a name="p12526113964118"></a><a name="p12526113964118"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p2371182824118"><a name="p2371182824118"></a><a name="p2371182824118"></a>60</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p137122815414"><a name="p137122815414"></a><a name="p137122815414"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p12031522153519"><a name="p12031522153519"></a><a name="p12031522153519"></a>mA</p>
</td>
</tr>
<tr id="row1381541216357"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p17371172854118"><a name="p17371172854118"></a><a name="p17371172854118"></a>13</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p437122817418"><a name="p437122817418"></a><a name="p437122817418"></a>VDD_WL_RF_TRX_1P1</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p20259135955116"><a name="p20259135955116"></a><a name="p20259135955116"></a>芯片内部TRX相关模块输入电源</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p1852510391412"><a name="p1852510391412"></a><a name="p1852510391412"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p437152884111"><a name="p437152884111"></a><a name="p437152884111"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p1437117286411"><a name="p1437117286411"></a><a name="p1437117286411"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p0646523143517"><a name="p0646523143517"></a><a name="p0646523143517"></a>mA</p>
</td>
</tr>
<tr id="row59444767"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p1137142815416"><a name="p1137142815416"></a><a name="p1137142815416"></a>14</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p133715286413"><a name="p133715286413"></a><a name="p133715286413"></a>VDD_WL_RF_PA_3P3</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p1725945917513"><a name="p1725945917513"></a><a name="p1725945917513"></a>WiFi PA供电电源，由外部电源提供</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p1385546164316"><a name="p1385546164316"></a><a name="p1385546164316"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p14372192884116"><a name="p14372192884116"></a><a name="p14372192884116"></a>320</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p537212824113"><a name="p537212824113"></a><a name="p537212824113"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p31872695"><a name="p31872695"></a><a name="p31872695"></a>mA</p>
</td>
</tr>
<tr id="row727693412173"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p17372152818416"><a name="p17372152818416"></a><a name="p17372152818416"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p1337215289416"><a name="p1337215289416"></a><a name="p1337215289416"></a>VDD_RF_RX_1P1</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p1425910593514"><a name="p1425910593514"></a><a name="p1425910593514"></a>芯片LNA输入电源</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p1585515610435"><a name="p1585515610435"></a><a name="p1585515610435"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p437232824115"><a name="p437232824115"></a><a name="p437232824115"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p437211280418"><a name="p437211280418"></a><a name="p437211280418"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p15276123417175"><a name="p15276123417175"></a><a name="p15276123417175"></a>mA</p>
</td>
</tr>
<tr id="row1146250174017"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p1537282816413"><a name="p1537282816413"></a><a name="p1537282816413"></a>17</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p83722028124119"><a name="p83722028124119"></a><a name="p83722028124119"></a>VDD_BSLE_RF_PA_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p52595598511"><a name="p52595598511"></a><a name="p52595598511"></a>BSLE LDO输入电源</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p1685514620435"><a name="p1685514620435"></a><a name="p1685514620435"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p1537242813418"><a name="p1537242813418"></a><a name="p1537242813418"></a>120</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p18372142811419"><a name="p18372142811419"></a><a name="p18372142811419"></a>300</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p54511455411"><a name="p54511455411"></a><a name="p54511455411"></a>mA</p>
</td>
</tr>
<tr id="row79566562403"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p93723282413"><a name="p93723282413"></a><a name="p93723282413"></a>19</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p15372202819416"><a name="p15372202819416"></a><a name="p15372202819416"></a>VDD_BSLE_RF_DRV_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p2026035955117"><a name="p2026035955117"></a><a name="p2026035955117"></a>BSLE LDO输入电源</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p1559447154310"><a name="p1559447154310"></a><a name="p1559447154310"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p83721928174117"><a name="p83721928174117"></a><a name="p83721928174117"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p1637292864114"><a name="p1637292864114"></a><a name="p1637292864114"></a>70</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p245134515414"><a name="p245134515414"></a><a name="p245134515414"></a>mA</p>
</td>
</tr>
<tr id="row1423214530409"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p637292814113"><a name="p637292814113"></a><a name="p637292814113"></a>20</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p0372112824119"><a name="p0372112824119"></a><a name="p0372112824119"></a>VDD_BSLE_PLL_DCO_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p726045975118"><a name="p726045975118"></a><a name="p726045975118"></a>BSLE LDO输入电源</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p45941779432"><a name="p45941779432"></a><a name="p45941779432"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p9372132811418"><a name="p9372132811418"></a><a name="p9372132811418"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p237282818416"><a name="p237282818416"></a><a name="p237282818416"></a>40</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p5451345114112"><a name="p5451345114112"></a><a name="p5451345114112"></a>mA</p>
</td>
</tr>
<tr id="row791810511416"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p73727282418"><a name="p73727282418"></a><a name="p73727282418"></a>37</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p9372112811417"><a name="p9372112811417"></a><a name="p9372112811417"></a>VDDIO</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p142601659165115"><a name="p142601659165115"></a><a name="p142601659165115"></a>IO电源，由外部电源提供</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p19594147144310"><a name="p19594147144310"></a><a name="p19594147144310"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p11372428134119"><a name="p11372428134119"></a><a name="p11372428134119"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p1037222812419"><a name="p1037222812419"></a><a name="p1037222812419"></a>150</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p1451145174112"><a name="p1451145174112"></a><a name="p1451145174112"></a>mA</p>
</td>
</tr>
<tr id="row1869317123413"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p1837213283417"><a name="p1837213283417"></a><a name="p1837213283417"></a>38</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p14372102874110"><a name="p14372102874110"></a><a name="p14372102874110"></a>AVDD33</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p626020594517"><a name="p626020594517"></a><a name="p626020594517"></a>AVDD33电源输入，由板级提供3.3V</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p167181281438"><a name="p167181281438"></a><a name="p167181281438"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p113721628124115"><a name="p113721628124115"></a><a name="p113721628124115"></a>40</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p4372102819415"><a name="p4372102819415"></a><a name="p4372102819415"></a>80</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p345174524115"><a name="p345174524115"></a><a name="p345174524115"></a>mA</p>
</td>
</tr>
<tr id="row2069381264116"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p43721828154114"><a name="p43721828154114"></a><a name="p43721828154114"></a>39</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p14372152804118"><a name="p14372152804118"></a><a name="p14372152804118"></a>VDD_VBAT1</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p142601459205111"><a name="p142601459205111"></a><a name="p142601459205111"></a>芯片BUCK输入电源，由外部电源提供</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p87186894314"><a name="p87186894314"></a><a name="p87186894314"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p437232824118"><a name="p437232824118"></a><a name="p437232824118"></a>300</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p1937214280418"><a name="p1937214280418"></a><a name="p1937214280418"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p15927346104119"><a name="p15927346104119"></a><a name="p15927346104119"></a>mA</p>
</td>
</tr>
<tr id="row14693512144117"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p183721328144115"><a name="p183721328144115"></a><a name="p183721328144115"></a>41</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p1437214287413"><a name="p1437214287413"></a><a name="p1437214287413"></a>VDD1P3_PMU1</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p1926095965111"><a name="p1926095965111"></a><a name="p1926095965111"></a>芯片BUCK反馈及CLDO输入</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p47186874312"><a name="p47186874312"></a><a name="p47186874312"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p183721728184118"><a name="p183721728184118"></a><a name="p183721728184118"></a>150</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p6372102854114"><a name="p6372102854114"></a><a name="p6372102854114"></a>300</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p69275467416"><a name="p69275467416"></a><a name="p69275467416"></a>mA</p>
</td>
</tr>
<tr id="row189184511414"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p63721828114120"><a name="p63721828114120"></a><a name="p63721828114120"></a>6</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p193721328194118"><a name="p193721328194118"></a><a name="p193721328194118"></a>XLDO_OUT</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p122601159155115"><a name="p122601159155115"></a><a name="p122601159155115"></a>芯片XLDO decap管脚，接板级滤波电容</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p465114917432"><a name="p465114917432"></a><a name="p465114917432"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p637292814412"><a name="p637292814412"></a><a name="p637292814412"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p1937219282410"><a name="p1937219282410"></a><a name="p1937219282410"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p18927134613411"><a name="p18927134613411"></a><a name="p18927134613411"></a>mA</p>
</td>
</tr>
<tr id="row109181514116"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p1837214288417"><a name="p1837214288417"></a><a name="p1837214288417"></a>11</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p173721128184114"><a name="p173721128184114"></a><a name="p173721128184114"></a>VDD_RFLDO1</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p92601359165118"><a name="p92601359165118"></a><a name="p92601359165118"></a>内部LDO电源，输出提供给VDD_WL_RF_TRX_1P1、</p>
<p id="p7260175915119"><a name="p7260175915119"></a><a name="p7260175915119"></a>VDD_RF_RX_1P1</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p665115916437"><a name="p665115916437"></a><a name="p665115916437"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p6373142884118"><a name="p6373142884118"></a><a name="p6373142884118"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p16373428174115"><a name="p16373428174115"></a><a name="p16373428174115"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p1873284819411"><a name="p1873284819411"></a><a name="p1873284819411"></a>mA</p>
</td>
</tr>
<tr id="row184811153153619"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p537332813412"><a name="p537332813412"></a><a name="p537332813412"></a>12</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p937314286417"><a name="p937314286417"></a><a name="p937314286417"></a>VDD_RFLDO2</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p1626019599511"><a name="p1626019599511"></a><a name="p1626019599511"></a>RFLDO2电源decap管脚，接板级滤波电容</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p206515934319"><a name="p206515934319"></a><a name="p206515934319"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p13373728104114"><a name="p13373728104114"></a><a name="p13373728104114"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p12373122874117"><a name="p12373122874117"></a><a name="p12373122874117"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p157321048134116"><a name="p157321048134116"></a><a name="p157321048134116"></a>mA</p>
</td>
</tr>
<tr id="row19618162510345"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p13731228104120"><a name="p13731228104120"></a><a name="p13731228104120"></a>18</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p163738286417"><a name="p163738286417"></a><a name="p163738286417"></a>VDD_BSLE_DPALDO</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p152601059155112"><a name="p152601059155112"></a><a name="p152601059155112"></a>芯片内部BSLE电源decap管脚，接板级滤波电容</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p11681112438"><a name="p11681112438"></a><a name="p11681112438"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p337302884120"><a name="p337302884120"></a><a name="p337302884120"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p537315281416"><a name="p537315281416"></a><a name="p537315281416"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p147321483418"><a name="p147321483418"></a><a name="p147321483418"></a>mA</p>
</td>
</tr>
<tr id="row14418143523815"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p1337392814111"><a name="p1337392814111"></a><a name="p1337392814111"></a>40</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p1537310288411"><a name="p1537310288411"></a><a name="p1537310288411"></a>BUCK_LX</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p14260459145111"><a name="p14260459145111"></a><a name="p14260459145111"></a>芯片BUCK LX输出1.3V，接板级电感、电容滤波</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p51671115434"><a name="p51671115434"></a><a name="p51671115434"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p16373028144110"><a name="p16373028144110"></a><a name="p16373028144110"></a>300</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p16373132854111"><a name="p16373132854111"></a><a name="p16373132854111"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p1973210486415"><a name="p1973210486415"></a><a name="p1973210486415"></a>mA</p>
</td>
</tr>
<tr id="row17181183293917"><td class="cellrowborder" valign="top" width="9.33%" headers="mcps1.2.8.1.1 "><p id="p13734282410"><a name="p13734282410"></a><a name="p13734282410"></a>42</p>
</td>
<td class="cellrowborder" valign="top" width="20.96%" headers="mcps1.2.8.1.2 "><p id="p12373112810418"><a name="p12373112810418"></a><a name="p12373112810418"></a>VDD_CLDO</p>
</td>
<td class="cellrowborder" valign="top" width="37.25%" headers="mcps1.2.8.1.3 "><p id="p426045935110"><a name="p426045935110"></a><a name="p426045935110"></a>芯片内部数字电源，外接1μF滤波电容</p>
</td>
<td class="cellrowborder" valign="top" width="8.37%" headers="mcps1.2.8.1.4 "><p id="p11611194318"><a name="p11611194318"></a><a name="p11611194318"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.88%" headers="mcps1.2.8.1.5 "><p id="p18373628114115"><a name="p18373628114115"></a><a name="p18373628114115"></a>150</p>
</td>
<td class="cellrowborder" valign="top" width="8.35%" headers="mcps1.2.8.1.6 "><p id="p143732282412"><a name="p143732282412"></a><a name="p143732282412"></a>300</p>
</td>
<td class="cellrowborder" valign="top" width="6.859999999999999%" headers="mcps1.2.8.1.7 "><p id="p273244894116"><a name="p273244894116"></a><a name="p273244894116"></a>mA</p>
</td>
</tr>
</tbody>
</table>

## 极限工作电压<a name="ZH-CN_TOPIC_0000001505722809"></a>

>![](public_sys-resources/icon-notice.gif) **须知：** 
>极限工作电压参数如[表1](#toc528421896)所示，超过这些数值，可能导致芯片损坏与可靠性问题。芯片ESD防护能力如[表2](#table101071935163912)所示。

**表 1**  极限工作电压参数

<a name="toc528421896"></a>
<table><thead align="left"><tr id="row52976132"><th class="cellrowborder" valign="top" width="19.2%" id="mcps1.2.6.1.1"><p id="p63208310"><a name="p63208310"></a><a name="p63208310"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="30.28%" id="mcps1.2.6.1.2"><p id="p19599509"><a name="p19599509"></a><a name="p19599509"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="19.59%" id="mcps1.2.6.1.3"><p id="p44056392"><a name="p44056392"></a><a name="p44056392"></a>最小值</p>
</th>
<th class="cellrowborder" valign="top" width="17.53%" id="mcps1.2.6.1.4"><p id="p11798008"><a name="p11798008"></a><a name="p11798008"></a>最大值</p>
</th>
<th class="cellrowborder" valign="top" width="13.4%" id="mcps1.2.6.1.5"><p id="p16114572"><a name="p16114572"></a><a name="p16114572"></a>单位</p>
</th>
</tr>
</thead>
<tbody><tr id="row16942194819361"><td class="cellrowborder" valign="top" width="19.2%" headers="mcps1.2.6.1.1 "><p id="p1794284863616"><a name="p1794284863616"></a><a name="p1794284863616"></a>VDD_VBAT1</p>
<p id="p1620313228353"><a name="p1620313228353"></a><a name="p1620313228353"></a>VDD_VBAT2</p>
</td>
<td class="cellrowborder" valign="top" width="30.28%" headers="mcps1.2.6.1.2 "><p id="p1194344823616"><a name="p1194344823616"></a><a name="p1194344823616"></a>芯片电源，由外部电源提供</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.6.1.3 "><p id="p12943134893615"><a name="p12943134893615"></a><a name="p12943134893615"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.6.1.4 "><p id="p19431648103616"><a name="p19431648103616"></a><a name="p19431648103616"></a>3.6</p>
</td>
<td class="cellrowborder" valign="top" width="13.4%" headers="mcps1.2.6.1.5 "><p id="p994384833614"><a name="p994384833614"></a><a name="p994384833614"></a>V</p>
</td>
</tr>
<tr id="row142179359411"><td class="cellrowborder" valign="top" width="19.2%" headers="mcps1.2.6.1.1 "><p id="p1121783524118"><a name="p1121783524118"></a><a name="p1121783524118"></a>VDD_WL_RF_PA_3P3</p>
</td>
<td class="cellrowborder" valign="top" width="30.28%" headers="mcps1.2.6.1.2 "><p id="p3206595528"><a name="p3206595528"></a><a name="p3206595528"></a>WiFi PA供电电源，由外部电源提供</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.6.1.3 "><p id="p6972145717423"><a name="p6972145717423"></a><a name="p6972145717423"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.6.1.4 "><p id="p179721657124220"><a name="p179721657124220"></a><a name="p179721657124220"></a>3.6</p>
</td>
<td class="cellrowborder" valign="top" width="13.4%" headers="mcps1.2.6.1.5 "><p id="p139722571422"><a name="p139722571422"></a><a name="p139722571422"></a>V</p>
</td>
</tr>
<tr id="row163854152812"><td class="cellrowborder" valign="top" width="19.2%" headers="mcps1.2.6.1.1 "><p id="p43115452813"><a name="p43115452813"></a><a name="p43115452813"></a>AVDD33</p>
</td>
<td class="cellrowborder" valign="top" width="30.28%" headers="mcps1.2.6.1.2 "><p id="p1130417470298"><a name="p1130417470298"></a><a name="p1130417470298"></a>LSADC和REF供电电源，由外部电源提供</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.6.1.3 "><p id="p872715507299"><a name="p872715507299"></a><a name="p872715507299"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.6.1.4 "><p id="p197271502291"><a name="p197271502291"></a><a name="p197271502291"></a>3.6</p>
</td>
<td class="cellrowborder" valign="top" width="13.4%" headers="mcps1.2.6.1.5 "><p id="p1272720505290"><a name="p1272720505290"></a><a name="p1272720505290"></a>V</p>
</td>
</tr>
<tr id="row561618565361"><td class="cellrowborder" valign="top" width="19.2%" headers="mcps1.2.6.1.1 "><p id="p16616956143614"><a name="p16616956143614"></a><a name="p16616956143614"></a>VDDIO</p>
</td>
<td class="cellrowborder" valign="top" width="30.28%" headers="mcps1.2.6.1.2 "><p id="p1288421414535"><a name="p1288421414535"></a><a name="p1288421414535"></a>IO电源，由外部电源提供</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.6.1.3 "><p id="p10616105693619"><a name="p10616105693619"></a><a name="p10616105693619"></a>1.62</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.6.1.4 "><p id="p561675673619"><a name="p561675673619"></a><a name="p561675673619"></a>3.6</p>
</td>
<td class="cellrowborder" valign="top" width="13.4%" headers="mcps1.2.6.1.5 "><p id="p6616956123620"><a name="p6616956123620"></a><a name="p6616956123620"></a>V</p>
</td>
</tr>
</tbody>
</table>

**表 2**  芯片引脚ESD参数

<a name="table101071935163912"></a>
<table><thead align="left"><tr id="row1210793510390"><th class="cellrowborder" valign="top" width="26.82%" id="mcps1.2.4.1.1"><p id="p6107163514390"><a name="p6107163514390"></a><a name="p6107163514390"></a>ESD模型与管脚</p>
</th>
<th class="cellrowborder" valign="top" width="25.619999999999997%" id="mcps1.2.4.1.2"><p id="p17532150112911"><a name="p17532150112911"></a><a name="p17532150112911"></a>PIN</p>
</th>
<th class="cellrowborder" valign="top" width="47.56%" id="mcps1.2.4.1.3"><p id="p1910710358397"><a name="p1910710358397"></a><a name="p1910710358397"></a>防护能力</p>
</th>
</tr>
</thead>
<tbody><tr id="row1810773523918"><td class="cellrowborder" valign="top" width="26.82%" headers="mcps1.2.4.1.1 "><p id="p16107235193911"><a name="p16107235193911"></a><a name="p16107235193911"></a>ESD-CDM</p>
</td>
<td class="cellrowborder" valign="top" width="25.619999999999997%" headers="mcps1.2.4.1.2 "><p id="p153317014299"><a name="p153317014299"></a><a name="p153317014299"></a>ALL</p>
</td>
<td class="cellrowborder" valign="top" width="47.56%" headers="mcps1.2.4.1.3 "><p id="p3107435133919"><a name="p3107435133919"></a><a name="p3107435133919"></a>CDM 250V</p>
</td>
</tr>
<tr id="row1110716356392"><td class="cellrowborder" rowspan="2" valign="top" width="26.82%" headers="mcps1.2.4.1.1 "><p id="p5102139162916"><a name="p5102139162916"></a><a name="p5102139162916"></a>ESD-HBM</p>
</td>
<td class="cellrowborder" valign="top" width="25.619999999999997%" headers="mcps1.2.4.1.2 "><p id="p13533405297"><a name="p13533405297"></a><a name="p13533405297"></a>14：VDD_WL_RF_PA_3P3</p>
</td>
<td class="cellrowborder" valign="top" width="47.56%" headers="mcps1.2.4.1.3 "><p id="p15107193518399"><a name="p15107193518399"></a><a name="p15107193518399"></a>HBM 2000V</p>
</td>
</tr>
<tr id="row556211434418"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p165339010295"><a name="p165339010295"></a><a name="p165339010295"></a>OTHER PIN</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p19562184194412"><a name="p19562184194412"></a><a name="p19562184194412"></a>HBM 2500V</p>
</td>
</tr>
</tbody>
</table>

## 推荐工作条件<a name="ZH-CN_TOPIC_0000001456242628"></a>

WS53V100的推荐工作条件如[表1](#toc528421897)所示。

**表 1**  推荐工作条件

<a name="toc528421897"></a>
<table><thead align="left"><tr id="row33563999"><th class="cellrowborder" valign="top" width="22.47775222477752%" id="mcps1.2.7.1.1"><p id="p34329384"><a name="p34329384"></a><a name="p34329384"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="25.3974602539746%" id="mcps1.2.7.1.2"><p id="p29216718"><a name="p29216718"></a><a name="p29216718"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="15.238476152384761%" id="mcps1.2.7.1.3"><p id="p17743928"><a name="p17743928"></a><a name="p17743928"></a>最小值</p>
</th>
<th class="cellrowborder" valign="top" width="14.008599140085993%" id="mcps1.2.7.1.4"><p id="p27972046"><a name="p27972046"></a><a name="p27972046"></a>典型值</p>
</th>
<th class="cellrowborder" valign="top" width="13.598640135986404%" id="mcps1.2.7.1.5"><p id="p51143290"><a name="p51143290"></a><a name="p51143290"></a>最大值</p>
</th>
<th class="cellrowborder" valign="top" width="9.27907209279072%" id="mcps1.2.7.1.6"><p id="p48965793"><a name="p48965793"></a><a name="p48965793"></a>单位</p>
</th>
</tr>
</thead>
<tbody><tr id="row533825823911"><td class="cellrowborder" valign="top" width="22.47775222477752%" headers="mcps1.2.7.1.1 "><p id="p14522174932818"><a name="p14522174932818"></a><a name="p14522174932818"></a>VDD_VBAT1</p>
<p id="p8831174612475"><a name="p8831174612475"></a><a name="p8831174612475"></a>VDD_VBAT2</p>
</td>
<td class="cellrowborder" valign="top" width="25.3974602539746%" headers="mcps1.2.7.1.2 "><p id="p4338165833915"><a name="p4338165833915"></a><a name="p4338165833915"></a>电池电源</p>
</td>
<td class="cellrowborder" valign="top" width="15.238476152384761%" headers="mcps1.2.7.1.3 "><p id="p19339155813399"><a name="p19339155813399"></a><a name="p19339155813399"></a>3.16</p>
</td>
<td class="cellrowborder" valign="top" width="14.008599140085993%" headers="mcps1.2.7.1.4 "><p id="p23390586399"><a name="p23390586399"></a><a name="p23390586399"></a>3.3</p>
</td>
<td class="cellrowborder" valign="top" width="13.598640135986404%" headers="mcps1.2.7.1.5 "><p id="p17339125843916"><a name="p17339125843916"></a><a name="p17339125843916"></a>3.465</p>
</td>
<td class="cellrowborder" valign="top" width="9.27907209279072%" headers="mcps1.2.7.1.6 "><p id="p1633915589397"><a name="p1633915589397"></a><a name="p1633915589397"></a>V</p>
</td>
</tr>
<tr id="row9665175818439"><td class="cellrowborder" valign="top" width="22.47775222477752%" headers="mcps1.2.7.1.1 "><p id="p1121783524118"><a name="p1121783524118"></a><a name="p1121783524118"></a>VDD_WL_RF_PA_3P3</p>
</td>
<td class="cellrowborder" valign="top" width="25.3974602539746%" headers="mcps1.2.7.1.2 "><p id="p2217183544113"><a name="p2217183544113"></a><a name="p2217183544113"></a>PA电源</p>
</td>
<td class="cellrowborder" valign="top" width="15.238476152384761%" headers="mcps1.2.7.1.3 "><p id="p18533165594011"><a name="p18533165594011"></a><a name="p18533165594011"></a>3.16</p>
</td>
<td class="cellrowborder" valign="top" width="14.008599140085993%" headers="mcps1.2.7.1.4 "><p id="p179721657124220"><a name="p179721657124220"></a><a name="p179721657124220"></a>3.3</p>
</td>
<td class="cellrowborder" valign="top" width="13.598640135986404%" headers="mcps1.2.7.1.5 "><p id="p112051021104013"><a name="p112051021104013"></a><a name="p112051021104013"></a>3.465</p>
</td>
<td class="cellrowborder" valign="top" width="9.27907209279072%" headers="mcps1.2.7.1.6 "><p id="p766535874320"><a name="p766535874320"></a><a name="p766535874320"></a>V</p>
</td>
</tr>
<tr id="row5101564015"><td class="cellrowborder" valign="top" width="22.47775222477752%" headers="mcps1.2.7.1.1 "><p id="p1133315345474"><a name="p1133315345474"></a><a name="p1133315345474"></a>VDDIO</p>
</td>
<td class="cellrowborder" valign="top" width="25.3974602539746%" headers="mcps1.2.7.1.2 "><p id="p510175164013"><a name="p510175164013"></a><a name="p510175164013"></a>IO输入电源</p>
</td>
<td class="cellrowborder" valign="top" width="15.238476152384761%" headers="mcps1.2.7.1.3 "><p id="p161019515409"><a name="p161019515409"></a><a name="p161019515409"></a>1.71</p>
</td>
<td class="cellrowborder" valign="top" width="14.008599140085993%" headers="mcps1.2.7.1.4 "><p id="p2103564015"><a name="p2103564015"></a><a name="p2103564015"></a>1.8/3.3</p>
</td>
<td class="cellrowborder" valign="top" width="13.598640135986404%" headers="mcps1.2.7.1.5 "><p id="p17196182264018"><a name="p17196182264018"></a><a name="p17196182264018"></a>3.465</p>
</td>
<td class="cellrowborder" valign="top" width="9.27907209279072%" headers="mcps1.2.7.1.6 "><p id="p19104514403"><a name="p19104514403"></a><a name="p19104514403"></a>V</p>
</td>
</tr>
<tr id="row1751565184415"><td class="cellrowborder" valign="top" width="22.47775222477752%" headers="mcps1.2.7.1.1 "><p id="p5876224103617"><a name="p5876224103617"></a><a name="p5876224103617"></a>VDD1P3_PMU1</p>
<p id="p7481115353613"><a name="p7481115353613"></a><a name="p7481115353613"></a>VDD_1P3</p>
<p id="p18419183513818"><a name="p18419183513818"></a><a name="p18419183513818"></a>VDD_BSLE_RF_PA_1P3</p>
<p id="p0181113218393"><a name="p0181113218393"></a><a name="p0181113218393"></a>VDD_BGLE_PLL_DCO_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="25.3974602539746%" headers="mcps1.2.7.1.2 "><p id="p185161751154417"><a name="p185161751154417"></a><a name="p185161751154417"></a>CLDO、RFLDO1/2输入电源</p>
</td>
<td class="cellrowborder" valign="top" width="15.238476152384761%" headers="mcps1.2.7.1.3 "><p id="p910185134013"><a name="p910185134013"></a><a name="p910185134013"></a>1.1</p>
</td>
<td class="cellrowborder" valign="top" width="14.008599140085993%" headers="mcps1.2.7.1.4 "><p id="p1107544011"><a name="p1107544011"></a><a name="p1107544011"></a>1.3</p>
</td>
<td class="cellrowborder" valign="top" width="13.598640135986404%" headers="mcps1.2.7.1.5 "><p id="p6101458401"><a name="p6101458401"></a><a name="p6101458401"></a>1.45</p>
</td>
<td class="cellrowborder" valign="top" width="9.27907209279072%" headers="mcps1.2.7.1.6 "><p id="p710957405"><a name="p710957405"></a><a name="p710957405"></a>V</p>
</td>
</tr>
</tbody>
</table>

## DC/AC电气参数<a name="ZH-CN_TOPIC_0000001455763064"></a>

**表 1**  DC电气参数表 （VDDIO=1.8V GPIO 功能\)

<a name="table12659151412575"></a>
<table><thead align="left"><tr id="row2822181412575"><th class="cellrowborder" valign="top" width="18.840000000000003%" id="mcps1.2.8.1.1"><p id="p18822131435719"><a name="p18822131435719"></a><a name="p18822131435719"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="23.430000000000003%" id="mcps1.2.8.1.2"><p id="p182218143574"><a name="p182218143574"></a><a name="p182218143574"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="11.340000000000002%" id="mcps1.2.8.1.3"><p id="p78224144578"><a name="p78224144578"></a><a name="p78224144578"></a>最小值</p>
</th>
<th class="cellrowborder" valign="top" width="11.340000000000002%" id="mcps1.2.8.1.4"><p id="p15822101485715"><a name="p15822101485715"></a><a name="p15822101485715"></a>典型值</p>
</th>
<th class="cellrowborder" valign="top" width="10.31%" id="mcps1.2.8.1.5"><p id="p8822111495715"><a name="p8822111495715"></a><a name="p8822111495715"></a>最大值</p>
</th>
<th class="cellrowborder" valign="top" width="9.280000000000001%" id="mcps1.2.8.1.6"><p id="p2822151416573"><a name="p2822151416573"></a><a name="p2822151416573"></a>单位</p>
</th>
<th class="cellrowborder" valign="top" width="15.46%" id="mcps1.2.8.1.7"><p id="p58226148570"><a name="p58226148570"></a><a name="p58226148570"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row089016561348"><td class="cellrowborder" valign="top" width="18.840000000000003%" headers="mcps1.2.8.1.1 "><p id="p81424587417"><a name="p81424587417"></a><a name="p81424587417"></a>VDDPST</p>
</td>
<td class="cellrowborder" valign="top" width="23.430000000000003%" headers="mcps1.2.8.1.2 "><p id="p31423580420"><a name="p31423580420"></a><a name="p31423580420"></a>接口电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p414235813412"><a name="p414235813412"></a><a name="p414235813412"></a>1.62</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p19142358740"><a name="p19142358740"></a><a name="p19142358740"></a>1.8</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p151426581145"><a name="p151426581145"></a><a name="p151426581145"></a>1.98</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p1514215815413"><a name="p1514215815413"></a><a name="p1514215815413"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p4142115819419"><a name="p4142115819419"></a><a name="p4142115819419"></a>-</p>
</td>
</tr>
<tr id="row128221114125710"><td class="cellrowborder" valign="top" width="18.840000000000003%" headers="mcps1.2.8.1.1 "><p id="p982261485710"><a name="p982261485710"></a><a name="p982261485710"></a>V<sub id="sub1772453073717"><a name="sub1772453073717"></a><a name="sub1772453073717"></a>IH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="23.430000000000003%" headers="mcps1.2.8.1.2 "><p id="p782211435710"><a name="p782211435710"></a><a name="p782211435710"></a>高电平输入电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p1648981742"><a name="p1648981742"></a><a name="p1648981742"></a>0.65*VDDPST</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p10822191475710"><a name="p10822191475710"></a><a name="p10822191475710"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p78221914185715"><a name="p78221914185715"></a><a name="p78221914185715"></a>VDDPST+0.3</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p1382361411576"><a name="p1382361411576"></a><a name="p1382361411576"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p78231914175717"><a name="p78231914175717"></a><a name="p78231914175717"></a>不兼容5V输入</p>
</td>
</tr>
<tr id="row1082301425713"><td class="cellrowborder" valign="top" width="18.840000000000003%" headers="mcps1.2.8.1.1 "><p id="p188231114135718"><a name="p188231114135718"></a><a name="p188231114135718"></a>V<sub id="sub1272463053717"><a name="sub1272463053717"></a><a name="sub1272463053717"></a>IL</sub></p>
</td>
<td class="cellrowborder" valign="top" width="23.430000000000003%" headers="mcps1.2.8.1.2 "><p id="p88231814105717"><a name="p88231814105717"></a><a name="p88231814105717"></a>低电平输入电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p3823111412579"><a name="p3823111412579"></a><a name="p3823111412579"></a>–0.3</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p882351416576"><a name="p882351416576"></a><a name="p882351416576"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p1582391415711"><a name="p1582391415711"></a><a name="p1582391415711"></a>0.35*VDDPST</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p12823914115715"><a name="p12823914115715"></a><a name="p12823914115715"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p12823161411575"><a name="p12823161411575"></a><a name="p12823161411575"></a>-</p>
</td>
</tr>
<tr id="row88232148573"><td class="cellrowborder" valign="top" width="18.840000000000003%" headers="mcps1.2.8.1.1 "><p id="p1282318141571"><a name="p1282318141571"></a><a name="p1282318141571"></a>I<sub id="sub12725193023717"><a name="sub12725193023717"></a><a name="sub12725193023717"></a>L</sub></p>
</td>
<td class="cellrowborder" valign="top" width="23.430000000000003%" headers="mcps1.2.8.1.2 "><p id="p1782351416571"><a name="p1782351416571"></a><a name="p1782351416571"></a>输入漏电流</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p158234149577"><a name="p158234149577"></a><a name="p158234149577"></a>0.06</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p12987133911193"><a name="p12987133911193"></a><a name="p12987133911193"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p152444201810"><a name="p152444201810"></a><a name="p152444201810"></a>61.18</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p0823614155716"><a name="p0823614155716"></a><a name="p0823614155716"></a>nA</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p1582371415719"><a name="p1582371415719"></a><a name="p1582371415719"></a>-</p>
</td>
</tr>
<tr id="row582316145576"><td class="cellrowborder" valign="top" width="18.840000000000003%" headers="mcps1.2.8.1.1 "><p id="p1982361412579"><a name="p1982361412579"></a><a name="p1982361412579"></a>I<sub id="sub7726330183719"><a name="sub7726330183719"></a><a name="sub7726330183719"></a>OZ</sub></p>
</td>
<td class="cellrowborder" valign="top" width="23.430000000000003%" headers="mcps1.2.8.1.2 "><p id="p16823141455717"><a name="p16823141455717"></a><a name="p16823141455717"></a>三态输出漏电流</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p582310144573"><a name="p582310144573"></a><a name="p582310144573"></a>0.2</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p1611216537187"><a name="p1611216537187"></a><a name="p1611216537187"></a>0.74</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p2082312144578"><a name="p2082312144578"></a><a name="p2082312144578"></a>12.69</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p1982321414571"><a name="p1982321414571"></a><a name="p1982321414571"></a>nA</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p18823614135718"><a name="p18823614135718"></a><a name="p18823614135718"></a>-</p>
</td>
</tr>
<tr id="row9823141425714"><td class="cellrowborder" valign="top" width="18.840000000000003%" headers="mcps1.2.8.1.1 "><p id="p118238140575"><a name="p118238140575"></a><a name="p118238140575"></a>V<sub id="sub3726163018375"><a name="sub3726163018375"></a><a name="sub3726163018375"></a>OH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="23.430000000000003%" headers="mcps1.2.8.1.2 "><p id="p48238145574"><a name="p48238145574"></a><a name="p48238145574"></a>高电平输出电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p1482313141573"><a name="p1482313141573"></a><a name="p1482313141573"></a>VDDPST-0.45</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p128231214145717"><a name="p128231214145717"></a><a name="p128231214145717"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p15823151418575"><a name="p15823151418575"></a><a name="p15823151418575"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p4823314155717"><a name="p4823314155717"></a><a name="p4823314155717"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p48231614175719"><a name="p48231614175719"></a><a name="p48231614175719"></a>-</p>
</td>
</tr>
<tr id="row10823214165713"><td class="cellrowborder" valign="top" width="18.840000000000003%" headers="mcps1.2.8.1.1 "><p id="p682321419577"><a name="p682321419577"></a><a name="p682321419577"></a>V<sub id="sub13727113063712"><a name="sub13727113063712"></a><a name="sub13727113063712"></a>OL</sub></p>
</td>
<td class="cellrowborder" valign="top" width="23.430000000000003%" headers="mcps1.2.8.1.2 "><p id="p98231314175718"><a name="p98231314175718"></a><a name="p98231314175718"></a>低电平输出电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p482381455716"><a name="p482381455716"></a><a name="p482381455716"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p208234149572"><a name="p208234149572"></a><a name="p208234149572"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p198231814125719"><a name="p198231814125719"></a><a name="p198231814125719"></a>0.45</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p68231614175715"><a name="p68231614175715"></a><a name="p68231614175715"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p7823121412572"><a name="p7823121412572"></a><a name="p7823121412572"></a>-</p>
</td>
</tr>
<tr id="row1582341475718"><td class="cellrowborder" valign="top" width="18.840000000000003%" headers="mcps1.2.8.1.1 "><p id="p7823131419574"><a name="p7823131419574"></a><a name="p7823131419574"></a>R<sub id="sub1272843043710"><a name="sub1272843043710"></a><a name="sub1272843043710"></a>PU</sub></p>
</td>
<td class="cellrowborder" valign="top" width="23.430000000000003%" headers="mcps1.2.8.1.2 "><p id="p1182391417577"><a name="p1182391417577"></a><a name="p1182391417577"></a>内部上拉电阻</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p198239143575"><a name="p198239143575"></a><a name="p198239143575"></a>49.3</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p118236147571"><a name="p118236147571"></a><a name="p118236147571"></a>61.56</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p482371425711"><a name="p482371425711"></a><a name="p482371425711"></a>85.07</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p8823121414574"><a name="p8823121414574"></a><a name="p8823121414574"></a>kΩ</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p582315144578"><a name="p582315144578"></a><a name="p582315144578"></a>-</p>
</td>
</tr>
<tr id="row1382371418578"><td class="cellrowborder" valign="top" width="18.840000000000003%" headers="mcps1.2.8.1.1 "><p id="p17823141412579"><a name="p17823141412579"></a><a name="p17823141412579"></a>R<sub id="sub97281230123716"><a name="sub97281230123716"></a><a name="sub97281230123716"></a>PD</sub></p>
</td>
<td class="cellrowborder" valign="top" width="23.430000000000003%" headers="mcps1.2.8.1.2 "><p id="p782371414570"><a name="p782371414570"></a><a name="p782371414570"></a>内部下拉电阻</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p282414146573"><a name="p282414146573"></a><a name="p282414146573"></a>54.54</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p1882441495714"><a name="p1882441495714"></a><a name="p1882441495714"></a>70.3</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p782481425716"><a name="p782481425716"></a><a name="p782481425716"></a>102.3</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p16824201455713"><a name="p16824201455713"></a><a name="p16824201455713"></a>kΩ</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p1282441416570"><a name="p1282441416570"></a><a name="p1282441416570"></a>-</p>
</td>
</tr>
<tr id="row8824111410573"><td class="cellrowborder" rowspan="4" valign="top" width="18.840000000000003%" headers="mcps1.2.8.1.1 "><p id="p1082471475717"><a name="p1082471475717"></a><a name="p1082471475717"></a>I<sub id="sub2729123019373"><a name="sub2729123019373"></a><a name="sub2729123019373"></a>OH</sub></p>
</td>
<td class="cellrowborder" rowspan="4" valign="top" width="23.430000000000003%" headers="mcps1.2.8.1.2 "><p id="p148241214155712"><a name="p148241214155712"></a><a name="p148241214155712"></a>高电平输出电流</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p8149144955910"><a name="p8149144955910"></a><a name="p8149144955910"></a>1.33</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p2148134925910"><a name="p2148134925910"></a><a name="p2148134925910"></a>2.39</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p6147194925913"><a name="p6147194925913"></a><a name="p6147194925913"></a>3.79</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p168241914105714"><a name="p168241914105714"></a><a name="p168241914105714"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p682416142570"><a name="p682416142570"></a><a name="p682416142570"></a>4驱IO档位1</p>
</td>
</tr>
<tr id="row1682471411579"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p197032104612"><a name="p197032104612"></a><a name="p197032104612"></a>2.66</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p146921291619"><a name="p146921291619"></a><a name="p146921291619"></a>4.76</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p1314594945911"><a name="p1314594945911"></a><a name="p1314594945911"></a>7.55</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p98248149574"><a name="p98248149574"></a><a name="p98248149574"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1282416146577"><a name="p1282416146577"></a><a name="p1282416146577"></a>4驱IO档位2</p>
</td>
</tr>
<tr id="row1582471416574"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p77031101165"><a name="p77031101165"></a><a name="p77031101165"></a>3.98</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p8691091669"><a name="p8691091669"></a><a name="p8691091669"></a>7.15</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p1514320496593"><a name="p1514320496593"></a><a name="p1514320496593"></a>11.33</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1882411145575"><a name="p1882411145575"></a><a name="p1882411145575"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1282441416575"><a name="p1282441416575"></a><a name="p1282441416575"></a>4驱IO档位3</p>
</td>
</tr>
<tr id="row10824314115714"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p470317101661"><a name="p470317101661"></a><a name="p470317101661"></a>5.31</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p7690109565"><a name="p7690109565"></a><a name="p7690109565"></a>9.5</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p614014496599"><a name="p614014496599"></a><a name="p614014496599"></a>15.04</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1382418144576"><a name="p1382418144576"></a><a name="p1382418144576"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p178245141577"><a name="p178245141577"></a><a name="p178245141577"></a>4驱IO档位4</p>
</td>
</tr>
<tr id="row1982471414572"><td class="cellrowborder" rowspan="4" valign="top" width="18.840000000000003%" headers="mcps1.2.8.1.1 "><p id="p11824141413574"><a name="p11824141413574"></a><a name="p11824141413574"></a>I<sub id="sub167309308373"><a name="sub167309308373"></a><a name="sub167309308373"></a>OL</sub></p>
</td>
<td class="cellrowborder" rowspan="4" valign="top" width="23.430000000000003%" headers="mcps1.2.8.1.2 "><p id="p1082481435713"><a name="p1082481435713"></a><a name="p1082481435713"></a>低电平输出电流</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p1966518301619"><a name="p1966518301619"></a><a name="p1966518301619"></a>1.54</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p46651301617"><a name="p46651301617"></a><a name="p46651301617"></a>3.03</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p666453010617"><a name="p666453010617"></a><a name="p666453010617"></a>5.01</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p2824151417573"><a name="p2824151417573"></a><a name="p2824151417573"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p10824214175712"><a name="p10824214175712"></a><a name="p10824214175712"></a>4驱IO档位1</p>
</td>
</tr>
<tr id="row1882441414574"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p56641130362"><a name="p56641130362"></a><a name="p56641130362"></a>3.1</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p966419301465"><a name="p966419301465"></a><a name="p966419301465"></a>6.06</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p126641130764"><a name="p126641130764"></a><a name="p126641130764"></a>9.99</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p182571419575"><a name="p182571419575"></a><a name="p182571419575"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1825201413578"><a name="p1825201413578"></a><a name="p1825201413578"></a>4驱IO档位2</p>
</td>
</tr>
<tr id="row1082517145571"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1366410301261"><a name="p1366410301261"></a><a name="p1366410301261"></a>4.65</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p366315301768"><a name="p366315301768"></a><a name="p366315301768"></a>9.09</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p666318305618"><a name="p666318305618"></a><a name="p666318305618"></a>15</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p108251714205715"><a name="p108251714205715"></a><a name="p108251714205715"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1482511411571"><a name="p1482511411571"></a><a name="p1482511411571"></a>4驱IO档位3</p>
</td>
</tr>
<tr id="row7825614115713"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p10663173017613"><a name="p10663173017613"></a><a name="p10663173017613"></a>6.21</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p196638301466"><a name="p196638301466"></a><a name="p196638301466"></a>12.13</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p364614306612"><a name="p364614306612"></a><a name="p364614306612"></a>19.98</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p188261014125716"><a name="p188261014125716"></a><a name="p188261014125716"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p10826161418570"><a name="p10826161418570"></a><a name="p10826161418570"></a>4驱IO档位4</p>
</td>
</tr>
</tbody>
</table>

**表 2**  DC电气参数表 （VDDIO=3.3V GPIO 功能\)

<a name="table168442231501"></a>
<table><thead align="left"><tr id="row17019248015"><th class="cellrowborder" valign="top" width="22.680000000000003%" id="mcps1.2.8.1.1"><p id="p1305245018"><a name="p1305245018"></a><a name="p1305245018"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="19.590000000000003%" id="mcps1.2.8.1.2"><p id="p6010241201"><a name="p6010241201"></a><a name="p6010241201"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="11.340000000000002%" id="mcps1.2.8.1.3"><p id="p1706241605"><a name="p1706241605"></a><a name="p1706241605"></a>最小值</p>
</th>
<th class="cellrowborder" valign="top" width="11.330000000000002%" id="mcps1.2.8.1.4"><p id="p1504241501"><a name="p1504241501"></a><a name="p1504241501"></a>典型值</p>
</th>
<th class="cellrowborder" valign="top" width="10.320000000000002%" id="mcps1.2.8.1.5"><p id="p18013241605"><a name="p18013241605"></a><a name="p18013241605"></a>最大值</p>
</th>
<th class="cellrowborder" valign="top" width="9.280000000000001%" id="mcps1.2.8.1.6"><p id="p7013246020"><a name="p7013246020"></a><a name="p7013246020"></a>单位</p>
</th>
<th class="cellrowborder" valign="top" width="15.46%" id="mcps1.2.8.1.7"><p id="p18014241807"><a name="p18014241807"></a><a name="p18014241807"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row54421610464"><td class="cellrowborder" valign="top" width="22.680000000000003%" headers="mcps1.2.8.1.1 "><p id="p385717119614"><a name="p385717119614"></a><a name="p385717119614"></a>VDDPST</p>
</td>
<td class="cellrowborder" valign="top" width="19.590000000000003%" headers="mcps1.2.8.1.2 "><p id="p285712111769"><a name="p285712111769"></a><a name="p285712111769"></a>接口电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p38574111061"><a name="p38574111061"></a><a name="p38574111061"></a>2.97</p>
</td>
<td class="cellrowborder" valign="top" width="11.330000000000002%" headers="mcps1.2.8.1.4 "><p id="p485731116614"><a name="p485731116614"></a><a name="p485731116614"></a>3.3</p>
</td>
<td class="cellrowborder" valign="top" width="10.320000000000002%" headers="mcps1.2.8.1.5 "><p id="p785741110620"><a name="p785741110620"></a><a name="p785741110620"></a>3.63</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p08572110611"><a name="p08572110611"></a><a name="p08572110611"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p785720114613"><a name="p785720114613"></a><a name="p785720114613"></a>-</p>
</td>
</tr>
<tr id="row12020248015"><td class="cellrowborder" valign="top" width="22.680000000000003%" headers="mcps1.2.8.1.1 "><p id="p180102412019"><a name="p180102412019"></a><a name="p180102412019"></a>V<sub id="sub37348302374"><a name="sub37348302374"></a><a name="sub37348302374"></a>IH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.590000000000003%" headers="mcps1.2.8.1.2 "><p id="p2020241808"><a name="p2020241808"></a><a name="p2020241808"></a>高电平输入电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p50724303"><a name="p50724303"></a><a name="p50724303"></a>2.0</p>
</td>
<td class="cellrowborder" valign="top" width="11.330000000000002%" headers="mcps1.2.8.1.4 "><p id="p20124105"><a name="p20124105"></a><a name="p20124105"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.320000000000002%" headers="mcps1.2.8.1.5 "><p id="p402242015"><a name="p402242015"></a><a name="p402242015"></a>VDDPST+0.3</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p908241503"><a name="p908241503"></a><a name="p908241503"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p13013241600"><a name="p13013241600"></a><a name="p13013241600"></a>不兼容5V输入</p>
</td>
</tr>
<tr id="row180132410018"><td class="cellrowborder" valign="top" width="22.680000000000003%" headers="mcps1.2.8.1.1 "><p id="p901824804"><a name="p901824804"></a><a name="p901824804"></a>V<sub id="sub1273483011373"><a name="sub1273483011373"></a><a name="sub1273483011373"></a>IL</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.590000000000003%" headers="mcps1.2.8.1.2 "><p id="p20192414019"><a name="p20192414019"></a><a name="p20192414019"></a>低电平输入电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p19015241016"><a name="p19015241016"></a><a name="p19015241016"></a>–0.3</p>
</td>
<td class="cellrowborder" valign="top" width="11.330000000000002%" headers="mcps1.2.8.1.4 "><p id="p101241706"><a name="p101241706"></a><a name="p101241706"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.320000000000002%" headers="mcps1.2.8.1.5 "><p id="p1601241202"><a name="p1601241202"></a><a name="p1601241202"></a>0.8</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p1301024603"><a name="p1301024603"></a><a name="p1301024603"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p90172417019"><a name="p90172417019"></a><a name="p90172417019"></a>-</p>
</td>
</tr>
<tr id="row905245020"><td class="cellrowborder" valign="top" width="22.680000000000003%" headers="mcps1.2.8.1.1 "><p id="p150142413015"><a name="p150142413015"></a><a name="p150142413015"></a>I<sub id="sub14735103019375"><a name="sub14735103019375"></a><a name="sub14735103019375"></a>L</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.590000000000003%" headers="mcps1.2.8.1.2 "><p id="p16012241012"><a name="p16012241012"></a><a name="p16012241012"></a>输入漏电流</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p2023120466202"><a name="p2023120466202"></a><a name="p2023120466202"></a>0.12</p>
</td>
<td class="cellrowborder" valign="top" width="11.330000000000002%" headers="mcps1.2.8.1.4 "><p id="p162311046182014"><a name="p162311046182014"></a><a name="p162311046182014"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.320000000000002%" headers="mcps1.2.8.1.5 "><p id="p8658732102012"><a name="p8658732102012"></a><a name="p8658732102012"></a>68.29</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p20624901"><a name="p20624901"></a><a name="p20624901"></a>nA</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p2032418015"><a name="p2032418015"></a><a name="p2032418015"></a>-</p>
</td>
</tr>
<tr id="row2019241105"><td class="cellrowborder" valign="top" width="22.680000000000003%" headers="mcps1.2.8.1.1 "><p id="p11020246010"><a name="p11020246010"></a><a name="p11020246010"></a>I<sub id="sub16735193015374"><a name="sub16735193015374"></a><a name="sub16735193015374"></a>OZ</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.590000000000003%" headers="mcps1.2.8.1.2 "><p id="p1702241809"><a name="p1702241809"></a><a name="p1702241809"></a>三态输出漏电流</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p42311346142012"><a name="p42311346142012"></a><a name="p42311346142012"></a>0.38</p>
</td>
<td class="cellrowborder" valign="top" width="11.330000000000002%" headers="mcps1.2.8.1.4 "><p id="p172301946142019"><a name="p172301946142019"></a><a name="p172301946142019"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="10.320000000000002%" headers="mcps1.2.8.1.5 "><p id="p15641203222010"><a name="p15641203222010"></a><a name="p15641203222010"></a>127.5</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p2010241502"><a name="p2010241502"></a><a name="p2010241502"></a>nA</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p17016241801"><a name="p17016241801"></a><a name="p17016241801"></a>-</p>
</td>
</tr>
<tr id="row140132413017"><td class="cellrowborder" valign="top" width="22.680000000000003%" headers="mcps1.2.8.1.1 "><p id="p70172420019"><a name="p70172420019"></a><a name="p70172420019"></a>V<sub id="sub1273663083719"><a name="sub1273663083719"></a><a name="sub1273663083719"></a>OH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.590000000000003%" headers="mcps1.2.8.1.2 "><p id="p1804241304"><a name="p1804241304"></a><a name="p1804241304"></a>高电平输出电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p4042419011"><a name="p4042419011"></a><a name="p4042419011"></a>2.4</p>
</td>
<td class="cellrowborder" valign="top" width="11.330000000000002%" headers="mcps1.2.8.1.4 "><p id="p1503241012"><a name="p1503241012"></a><a name="p1503241012"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.320000000000002%" headers="mcps1.2.8.1.5 "><p id="p1502241609"><a name="p1502241609"></a><a name="p1502241609"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p4017241309"><a name="p4017241309"></a><a name="p4017241309"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p12111241809"><a name="p12111241809"></a><a name="p12111241809"></a>-</p>
</td>
</tr>
<tr id="row13162410010"><td class="cellrowborder" valign="top" width="22.680000000000003%" headers="mcps1.2.8.1.1 "><p id="p715241705"><a name="p715241705"></a><a name="p715241705"></a>V<sub id="sub0736430143720"><a name="sub0736430143720"></a><a name="sub0736430143720"></a>OL</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.590000000000003%" headers="mcps1.2.8.1.2 "><p id="p161102415013"><a name="p161102415013"></a><a name="p161102415013"></a>低电平输出电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p18112411010"><a name="p18112411010"></a><a name="p18112411010"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.330000000000002%" headers="mcps1.2.8.1.4 "><p id="p17110243018"><a name="p17110243018"></a><a name="p17110243018"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.320000000000002%" headers="mcps1.2.8.1.5 "><p id="p15112241507"><a name="p15112241507"></a><a name="p15112241507"></a>0.4</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p161102411019"><a name="p161102411019"></a><a name="p161102411019"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p4120241806"><a name="p4120241806"></a><a name="p4120241806"></a>-</p>
</td>
</tr>
<tr id="row1811024805"><td class="cellrowborder" valign="top" width="22.680000000000003%" headers="mcps1.2.8.1.1 "><p id="p11112243016"><a name="p11112243016"></a><a name="p11112243016"></a>R<sub id="sub18736133013376"><a name="sub18736133013376"></a><a name="sub18736133013376"></a>PU</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.590000000000003%" headers="mcps1.2.8.1.2 "><p id="p61122416016"><a name="p61122416016"></a><a name="p61122416016"></a>内部上拉电阻</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p1490113521482"><a name="p1490113521482"></a><a name="p1490113521482"></a>50.36</p>
</td>
<td class="cellrowborder" valign="top" width="11.330000000000002%" headers="mcps1.2.8.1.4 "><p id="p6901175218820"><a name="p6901175218820"></a><a name="p6901175218820"></a>60.72</p>
</td>
<td class="cellrowborder" valign="top" width="10.320000000000002%" headers="mcps1.2.8.1.5 "><p id="p199019521684"><a name="p199019521684"></a><a name="p199019521684"></a>74.71</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p17132418011"><a name="p17132418011"></a><a name="p17132418011"></a>kΩ</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p311924506"><a name="p311924506"></a><a name="p311924506"></a>-</p>
</td>
</tr>
<tr id="row1911241309"><td class="cellrowborder" valign="top" width="22.680000000000003%" headers="mcps1.2.8.1.1 "><p id="p411246015"><a name="p411246015"></a><a name="p411246015"></a>R<sub id="sub1737183012375"><a name="sub1737183012375"></a><a name="sub1737183012375"></a>PD</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.590000000000003%" headers="mcps1.2.8.1.2 "><p id="p2192415020"><a name="p2192415020"></a><a name="p2192415020"></a>内部下拉电阻</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p990013528813"><a name="p990013528813"></a><a name="p990013528813"></a>47.84</p>
</td>
<td class="cellrowborder" valign="top" width="11.330000000000002%" headers="mcps1.2.8.1.4 "><p id="p1290045210816"><a name="p1290045210816"></a><a name="p1290045210816"></a>57.42</p>
</td>
<td class="cellrowborder" valign="top" width="10.320000000000002%" headers="mcps1.2.8.1.5 "><p id="p188842521289"><a name="p188842521289"></a><a name="p188842521289"></a>70.73</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p1514243012"><a name="p1514243012"></a><a name="p1514243012"></a>kΩ</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p14122413013"><a name="p14122413013"></a><a name="p14122413013"></a>-</p>
</td>
</tr>
<tr id="row13182413016"><td class="cellrowborder" rowspan="4" valign="top" width="22.680000000000003%" headers="mcps1.2.8.1.1 "><p id="p71724805"><a name="p71724805"></a><a name="p71724805"></a>I<sub id="sub473783016371"><a name="sub473783016371"></a><a name="sub473783016371"></a>OH</sub></p>
</td>
<td class="cellrowborder" rowspan="4" valign="top" width="19.590000000000003%" headers="mcps1.2.8.1.2 "><p id="p12111242007"><a name="p12111242007"></a><a name="p12111242007"></a>高电平输出电流</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p20632022382"><a name="p20632022382"></a><a name="p20632022382"></a>3.59</p>
</td>
<td class="cellrowborder" valign="top" width="11.330000000000002%" headers="mcps1.2.8.1.4 "><p id="p1970719511695"><a name="p1970719511695"></a><a name="p1970719511695"></a>7.95</p>
</td>
<td class="cellrowborder" valign="top" width="10.320000000000002%" headers="mcps1.2.8.1.5 "><p id="p17707195118913"><a name="p17707195118913"></a><a name="p17707195118913"></a>13.69</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p101122412019"><a name="p101122412019"></a><a name="p101122412019"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p151124308"><a name="p151124308"></a><a name="p151124308"></a>4驱IO档位1</p>
</td>
</tr>
<tr id="row21724003"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p14634221688"><a name="p14634221688"></a><a name="p14634221688"></a>7.16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p1270714511199"><a name="p1270714511199"></a><a name="p1270714511199"></a>15.83</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p2070785110912"><a name="p2070785110912"></a><a name="p2070785110912"></a>27.24</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p10112240012"><a name="p10112240012"></a><a name="p10112240012"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1162417010"><a name="p1162417010"></a><a name="p1162417010"></a>4驱IO档位2</p>
</td>
</tr>
<tr id="row15112247014"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p66310229815"><a name="p66310229815"></a><a name="p66310229815"></a>10.75</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p47063512920"><a name="p47063512920"></a><a name="p47063512920"></a>23.75</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p1870614511591"><a name="p1870614511591"></a><a name="p1870614511591"></a>40.87</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p511824201"><a name="p511824201"></a><a name="p511824201"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p51112420010"><a name="p51112420010"></a><a name="p51112420010"></a>4驱IO档位3</p>
</td>
</tr>
<tr id="row1916242016"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p06219221984"><a name="p06219221984"></a><a name="p06219221984"></a>14.28</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p137068512910"><a name="p137068512910"></a><a name="p137068512910"></a>31.52</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p66891751692"><a name="p66891751692"></a><a name="p66891751692"></a>54.2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p5118241603"><a name="p5118241603"></a><a name="p5118241603"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p121152414019"><a name="p121152414019"></a><a name="p121152414019"></a>4驱IO档位4</p>
</td>
</tr>
<tr id="row1516247014"><td class="cellrowborder" rowspan="4" valign="top" width="22.680000000000003%" headers="mcps1.2.8.1.1 "><p id="p310245019"><a name="p310245019"></a><a name="p310245019"></a>I<sub id="sub4739203011374"><a name="sub4739203011374"></a><a name="sub4739203011374"></a>OL</sub></p>
</td>
<td class="cellrowborder" rowspan="4" valign="top" width="19.590000000000003%" headers="mcps1.2.8.1.2 "><p id="p21172411019"><a name="p21172411019"></a><a name="p21172411019"></a>低电平输出电流</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p79189191783"><a name="p79189191783"></a><a name="p79189191783"></a>2.88</p>
</td>
<td class="cellrowborder" valign="top" width="11.330000000000002%" headers="mcps1.2.8.1.4 "><p id="p11326929191015"><a name="p11326929191015"></a><a name="p11326929191015"></a>4.76</p>
</td>
<td class="cellrowborder" valign="top" width="10.320000000000002%" headers="mcps1.2.8.1.5 "><p id="p15325429151010"><a name="p15325429151010"></a><a name="p15325429151010"></a>6.72</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p1011324107"><a name="p1011324107"></a><a name="p1011324107"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p10111242012"><a name="p10111242012"></a><a name="p10111242012"></a>4驱IO档位1</p>
</td>
</tr>
<tr id="row318248018"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1391761914816"><a name="p1391761914816"></a><a name="p1391761914816"></a>5.75</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p8325129111012"><a name="p8325129111012"></a><a name="p8325129111012"></a>9.49</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p103251929101010"><a name="p103251929101010"></a><a name="p103251929101010"></a>13.32</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p10111241107"><a name="p10111241107"></a><a name="p10111241107"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p9182415020"><a name="p9182415020"></a><a name="p9182415020"></a>4驱IO档位2</p>
</td>
</tr>
<tr id="row215245014"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p209171419288"><a name="p209171419288"></a><a name="p209171419288"></a>8.63</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p17325202914101"><a name="p17325202914101"></a><a name="p17325202914101"></a>14.25</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p432542951012"><a name="p432542951012"></a><a name="p432542951012"></a>20.03</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1717241301"><a name="p1717241301"></a><a name="p1717241301"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p9192420012"><a name="p9192420012"></a><a name="p9192420012"></a>4驱IO档位3</p>
</td>
</tr>
<tr id="row19117241600"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p5917919289"><a name="p5917919289"></a><a name="p5917919289"></a>11.51</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p1732462981013"><a name="p1732462981013"></a><a name="p1732462981013"></a>18.97</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p1308132915108"><a name="p1308132915108"></a><a name="p1308132915108"></a>26.61</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p821241507"><a name="p821241507"></a><a name="p821241507"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p6214244013"><a name="p6214244013"></a><a name="p6214244013"></a>4驱IO档位4</p>
</td>
</tr>
</tbody>
</table>

**表 3**  DC电气参数表 （VDDIO=3.3V GPIO 功能--SDIO专用\)

<a name="table1643441510247"></a>
<table><thead align="left"><tr id="row184341415142412"><th class="cellrowborder" valign="top" width="22.650000000000002%" id="mcps1.2.8.1.1"><p id="p4434191512417"><a name="p4434191512417"></a><a name="p4434191512417"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="19.620000000000005%" id="mcps1.2.8.1.2"><p id="p17434121502420"><a name="p17434121502420"></a><a name="p17434121502420"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="11.340000000000002%" id="mcps1.2.8.1.3"><p id="p34343155241"><a name="p34343155241"></a><a name="p34343155241"></a>最小值</p>
</th>
<th class="cellrowborder" valign="top" width="11.340000000000002%" id="mcps1.2.8.1.4"><p id="p184341415142410"><a name="p184341415142410"></a><a name="p184341415142410"></a>典型值</p>
</th>
<th class="cellrowborder" valign="top" width="10.31%" id="mcps1.2.8.1.5"><p id="p14346157249"><a name="p14346157249"></a><a name="p14346157249"></a>最大值</p>
</th>
<th class="cellrowborder" valign="top" width="9.280000000000001%" id="mcps1.2.8.1.6"><p id="p1434171552416"><a name="p1434171552416"></a><a name="p1434171552416"></a>单位</p>
</th>
<th class="cellrowborder" valign="top" width="15.46%" id="mcps1.2.8.1.7"><p id="p19434615122419"><a name="p19434615122419"></a><a name="p19434615122419"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row1743412159243"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p1258218324712"><a name="p1258218324712"></a><a name="p1258218324712"></a>VDDPST</p>
</td>
<td class="cellrowborder" valign="top" width="19.620000000000005%" headers="mcps1.2.8.1.2 "><p id="p125821839478"><a name="p125821839478"></a><a name="p125821839478"></a>接口电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p1758253164715"><a name="p1758253164715"></a><a name="p1758253164715"></a>2.97</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p9410172954812"><a name="p9410172954812"></a><a name="p9410172954812"></a>3.3</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p15822036475"><a name="p15822036475"></a><a name="p15822036475"></a>3.63</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p558219314472"><a name="p558219314472"></a><a name="p558219314472"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p114341915152410"><a name="p114341915152410"></a><a name="p114341915152410"></a>-</p>
</td>
</tr>
<tr id="row11434161532410"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p1943410154245"><a name="p1943410154245"></a><a name="p1943410154245"></a>V<sub id="sub10434181512418"><a name="sub10434181512418"></a><a name="sub10434181512418"></a>IH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.620000000000005%" headers="mcps1.2.8.1.2 "><p id="p144341415132411"><a name="p144341415132411"></a><a name="p144341415132411"></a>高电平输入电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p10434615202413"><a name="p10434615202413"></a><a name="p10434615202413"></a>2.0</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p343481517243"><a name="p343481517243"></a><a name="p343481517243"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p74351215192415"><a name="p74351215192415"></a><a name="p74351215192415"></a>3.63</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p943517157247"><a name="p943517157247"></a><a name="p943517157247"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 ">&nbsp;&nbsp;</td>
</tr>
<tr id="row17435141512247"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p4435161522412"><a name="p4435161522412"></a><a name="p4435161522412"></a>V<sub id="sub134351715202410"><a name="sub134351715202410"></a><a name="sub134351715202410"></a>IL</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.620000000000005%" headers="mcps1.2.8.1.2 "><p id="p6435141592419"><a name="p6435141592419"></a><a name="p6435141592419"></a>低电平输入电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p19435315102420"><a name="p19435315102420"></a><a name="p19435315102420"></a>–0.3</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p1643501515240"><a name="p1643501515240"></a><a name="p1643501515240"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p3435121510249"><a name="p3435121510249"></a><a name="p3435121510249"></a>0.8</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p18435101513245"><a name="p18435101513245"></a><a name="p18435101513245"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p144359150246"><a name="p144359150246"></a><a name="p144359150246"></a>-</p>
</td>
</tr>
<tr id="row9435191510246"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p0435161512247"><a name="p0435161512247"></a><a name="p0435161512247"></a>I<sub id="sub164351415172415"><a name="sub164351415172415"></a><a name="sub164351415172415"></a>L</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.620000000000005%" headers="mcps1.2.8.1.2 "><p id="p10435121519244"><a name="p10435121519244"></a><a name="p10435121519244"></a>输入漏电流</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p979514072611"><a name="p979514072611"></a><a name="p979514072611"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p194355152247"><a name="p194355152247"></a><a name="p194355152247"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p843541514248"><a name="p843541514248"></a><a name="p843541514248"></a>&plusmn;10</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p1443516150244"><a name="p1443516150244"></a><a name="p1443516150244"></a>μA</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p2435141515248"><a name="p2435141515248"></a><a name="p2435141515248"></a>-</p>
</td>
</tr>
<tr id="row154355156240"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p34351315162413"><a name="p34351315162413"></a><a name="p34351315162413"></a>I<sub id="sub1543531552418"><a name="sub1543531552418"></a><a name="sub1543531552418"></a>OZ</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.620000000000005%" headers="mcps1.2.8.1.2 "><p id="p24351515152415"><a name="p24351515152415"></a><a name="p24351515152415"></a>三态输出漏电流</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p161331122192617"><a name="p161331122192617"></a><a name="p161331122192617"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p1211311228267"><a name="p1211311228267"></a><a name="p1211311228267"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p9435915162418"><a name="p9435915162418"></a><a name="p9435915162418"></a>&plusmn;10</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p1443511519244"><a name="p1443511519244"></a><a name="p1443511519244"></a>nA</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p10435141517249"><a name="p10435141517249"></a><a name="p10435141517249"></a>-</p>
</td>
</tr>
<tr id="row843511154242"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p143561510246"><a name="p143561510246"></a><a name="p143561510246"></a>V<sub id="sub1843531518240"><a name="sub1843531518240"></a><a name="sub1843531518240"></a>OH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.620000000000005%" headers="mcps1.2.8.1.2 "><p id="p17435111512244"><a name="p17435111512244"></a><a name="p17435111512244"></a>高电平输出电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p1643561510244"><a name="p1643561510244"></a><a name="p1643561510244"></a>2.4</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p5435131515241"><a name="p5435131515241"></a><a name="p5435131515241"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p134358150245"><a name="p134358150245"></a><a name="p134358150245"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p74351715152413"><a name="p74351715152413"></a><a name="p74351715152413"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p1343511592416"><a name="p1343511592416"></a><a name="p1343511592416"></a>-</p>
</td>
</tr>
<tr id="row443581532412"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p174358151243"><a name="p174358151243"></a><a name="p174358151243"></a>V<sub id="sub3435111518241"><a name="sub3435111518241"></a><a name="sub3435111518241"></a>OL</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.620000000000005%" headers="mcps1.2.8.1.2 "><p id="p2435141532416"><a name="p2435141532416"></a><a name="p2435141532416"></a>低电平输出电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p10435181532415"><a name="p10435181532415"></a><a name="p10435181532415"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p443510153248"><a name="p443510153248"></a><a name="p443510153248"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p5435315142417"><a name="p5435315142417"></a><a name="p5435315142417"></a>0.4</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p1343551514248"><a name="p1343551514248"></a><a name="p1343551514248"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p1543661592413"><a name="p1543661592413"></a><a name="p1543661592413"></a>-</p>
</td>
</tr>
<tr id="row2436101518240"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p44364158248"><a name="p44364158248"></a><a name="p44364158248"></a>R<sub id="sub34361115142412"><a name="sub34361115142412"></a><a name="sub34361115142412"></a>PU</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.620000000000005%" headers="mcps1.2.8.1.2 "><p id="p74361615152418"><a name="p74361615152418"></a><a name="p74361615152418"></a>内部上拉电阻</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p9117756162618"><a name="p9117756162618"></a><a name="p9117756162618"></a>19</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p311625612614"><a name="p311625612614"></a><a name="p311625612614"></a>25</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p191167567266"><a name="p191167567266"></a><a name="p191167567266"></a>31</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p12436111518249"><a name="p12436111518249"></a><a name="p12436111518249"></a>kΩ</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p14436181542419"><a name="p14436181542419"></a><a name="p14436181542419"></a>-</p>
</td>
</tr>
<tr id="row104362015202414"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p1343631510243"><a name="p1343631510243"></a><a name="p1343631510243"></a>R<sub id="sub14436015182416"><a name="sub14436015182416"></a><a name="sub14436015182416"></a>PD</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.620000000000005%" headers="mcps1.2.8.1.2 "><p id="p14436151562411"><a name="p14436151562411"></a><a name="p14436151562411"></a>内部下拉电阻</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p1911595632613"><a name="p1911595632613"></a><a name="p1911595632613"></a>19</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p1811555672615"><a name="p1811555672615"></a><a name="p1811555672615"></a>25</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p1611485619266"><a name="p1611485619266"></a><a name="p1611485619266"></a>31</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p14361015162418"><a name="p14361015162418"></a><a name="p14361015162418"></a>kΩ</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p174366155249"><a name="p174366155249"></a><a name="p174366155249"></a>-</p>
</td>
</tr>
<tr id="row12837191018418"><td class="cellrowborder" rowspan="16" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p64251791418"><a name="p64251791418"></a><a name="p64251791418"></a>I<sub id="sub17425199746"><a name="sub17425199746"></a><a name="sub17425199746"></a>OH</sub></p>
</td>
<td class="cellrowborder" rowspan="16" valign="top" width="19.620000000000005%" headers="mcps1.2.8.1.2 "><p id="p15425591945"><a name="p15425591945"></a><a name="p15425591945"></a>高电平输出电流</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p11715134611514"><a name="p11715134611514"></a><a name="p11715134611514"></a>46.31</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p3425597411"><a name="p3425597411"></a><a name="p3425597411"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p144261390417"><a name="p144261390417"></a><a name="p144261390417"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p184261395412"><a name="p184261395412"></a><a name="p184261395412"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p164261590414"><a name="p164261590414"></a><a name="p164261590414"></a>16驱IO档位0</p>
</td>
</tr>
<tr id="row083741013413"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p17159461518"><a name="p17159461518"></a><a name="p17159461518"></a>43.59</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p144261991545"><a name="p144261991545"></a><a name="p144261991545"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p124261916419"><a name="p124261916419"></a><a name="p124261916419"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p144261592040"><a name="p144261592040"></a><a name="p144261592040"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p12426119644"><a name="p12426119644"></a><a name="p12426119644"></a>16驱IO档位1</p>
</td>
</tr>
<tr id="row2837111013410"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1671564611518"><a name="p1671564611518"></a><a name="p1671564611518"></a>40.86</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p8426694411"><a name="p8426694411"></a><a name="p8426694411"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p84261491243"><a name="p84261491243"></a><a name="p84261491243"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p4426593417"><a name="p4426593417"></a><a name="p4426593417"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p10426599418"><a name="p10426599418"></a><a name="p10426599418"></a>16驱IO档位2</p>
</td>
</tr>
<tr id="row78373102411"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p171518465515"><a name="p171518465515"></a><a name="p171518465515"></a>38.14</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p3426119647"><a name="p3426119647"></a><a name="p3426119647"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p14271091743"><a name="p14271091743"></a><a name="p14271091743"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p4428189443"><a name="p4428189443"></a><a name="p4428189443"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1428791245"><a name="p1428791245"></a><a name="p1428791245"></a>16驱IO档位3</p>
</td>
</tr>
<tr id="row583701013415"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p57141246559"><a name="p57141246559"></a><a name="p57141246559"></a>35.42</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p2428491417"><a name="p2428491417"></a><a name="p2428491417"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p442810914412"><a name="p442810914412"></a><a name="p442810914412"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p17428991742"><a name="p17428991742"></a><a name="p17428991742"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p164281490415"><a name="p164281490415"></a><a name="p164281490415"></a>16驱IO档位4</p>
</td>
</tr>
<tr id="row158376103415"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1871419468511"><a name="p1871419468511"></a><a name="p1871419468511"></a>32.69</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p14281915420"><a name="p14281915420"></a><a name="p14281915420"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p1742819913419"><a name="p1742819913419"></a><a name="p1742819913419"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p44287917416"><a name="p44287917416"></a><a name="p44287917416"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p11428199443"><a name="p11428199443"></a><a name="p11428199443"></a>16驱IO档位5</p>
</td>
</tr>
<tr id="row98373101543"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1071434610520"><a name="p1071434610520"></a><a name="p1071434610520"></a>29.97</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p204288919413"><a name="p204288919413"></a><a name="p204288919413"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p0428149047"><a name="p0428149047"></a><a name="p0428149047"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1142813917418"><a name="p1142813917418"></a><a name="p1142813917418"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p8428891847"><a name="p8428891847"></a><a name="p8428891847"></a>16驱IO档位6</p>
</td>
</tr>
<tr id="row1083713107412"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p187148467519"><a name="p187148467519"></a><a name="p187148467519"></a>27.74</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p184281491245"><a name="p184281491245"></a><a name="p184281491245"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p54282911417"><a name="p54282911417"></a><a name="p54282911417"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p242817915415"><a name="p242817915415"></a><a name="p242817915415"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p194285917413"><a name="p194285917413"></a><a name="p194285917413"></a>16驱IO档位7</p>
</td>
</tr>
<tr id="row683713101142"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p27131446755"><a name="p27131446755"></a><a name="p27131446755"></a>24.52</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p1242919911414"><a name="p1242919911414"></a><a name="p1242919911414"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p13429592416"><a name="p13429592416"></a><a name="p13429592416"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p124290917417"><a name="p124290917417"></a><a name="p124290917417"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p18429189442"><a name="p18429189442"></a><a name="p18429189442"></a>16驱IO档位8</p>
</td>
</tr>
<tr id="row1183731020411"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p187131246355"><a name="p187131246355"></a><a name="p187131246355"></a>21.79</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p20429191145"><a name="p20429191145"></a><a name="p20429191145"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p15429591148"><a name="p15429591148"></a><a name="p15429591148"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p7429292047"><a name="p7429292047"></a><a name="p7429292047"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p194293919418"><a name="p194293919418"></a><a name="p194293919418"></a>16驱IO档位9</p>
</td>
</tr>
<tr id="row78375102411"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p10713144614516"><a name="p10713144614516"></a><a name="p10713144614516"></a>19.07</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p74291691543"><a name="p74291691543"></a><a name="p74291691543"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p942959846"><a name="p942959846"></a><a name="p942959846"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p94291191440"><a name="p94291191440"></a><a name="p94291191440"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p04296919413"><a name="p04296919413"></a><a name="p04296919413"></a>16驱IO档位10</p>
</td>
</tr>
<tr id="row148371110349"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p171215468513"><a name="p171215468513"></a><a name="p171215468513"></a>16.35</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p24292912419"><a name="p24292912419"></a><a name="p24292912419"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p9429393415"><a name="p9429393415"></a><a name="p9429393415"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p154291291143"><a name="p154291291143"></a><a name="p154291291143"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p04290913410"><a name="p04290913410"></a><a name="p04290913410"></a>16驱IO档位11</p>
</td>
</tr>
<tr id="row188375102412"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p97124461752"><a name="p97124461752"></a><a name="p97124461752"></a>13.62</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p342913913417"><a name="p342913913417"></a><a name="p342913913417"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p54295910412"><a name="p54295910412"></a><a name="p54295910412"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p184292091643"><a name="p184292091643"></a><a name="p184292091643"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p12429199844"><a name="p12429199844"></a><a name="p12429199844"></a>16驱IO档位12</p>
</td>
</tr>
<tr id="row2837151015415"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p571214463512"><a name="p571214463512"></a><a name="p571214463512"></a>10.9</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p2430391040"><a name="p2430391040"></a><a name="p2430391040"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p14430169047"><a name="p14430169047"></a><a name="p14430169047"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p18430192410"><a name="p18430192410"></a><a name="p18430192410"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1543020914418"><a name="p1543020914418"></a><a name="p1543020914418"></a>16驱IO档位13</p>
</td>
</tr>
<tr id="row118377101645"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1771220461751"><a name="p1771220461751"></a><a name="p1771220461751"></a>8.18</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p1943010912419"><a name="p1943010912419"></a><a name="p1943010912419"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p15430791847"><a name="p15430791847"></a><a name="p15430791847"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1243010920411"><a name="p1243010920411"></a><a name="p1243010920411"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1143069749"><a name="p1143069749"></a><a name="p1143069749"></a>16驱IO档位14</p>
</td>
</tr>
<tr id="row583751013417"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p669464616515"><a name="p669464616515"></a><a name="p669464616515"></a>5.45</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p1243012913415"><a name="p1243012913415"></a><a name="p1243012913415"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p144301091842"><a name="p144301091842"></a><a name="p144301091842"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1143029543"><a name="p1143029543"></a><a name="p1143029543"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p15430179048"><a name="p15430179048"></a><a name="p15430179048"></a>16驱IO档位15</p>
</td>
</tr>
<tr id="row17837131019410"><td class="cellrowborder" rowspan="16" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p143017911416"><a name="p143017911416"></a><a name="p143017911416"></a>I<sub id="sub20430797414"><a name="sub20430797414"></a><a name="sub20430797414"></a>OL</sub></p>
</td>
<td class="cellrowborder" rowspan="16" valign="top" width="19.620000000000005%" headers="mcps1.2.8.1.2 "><p id="p154301196414"><a name="p154301196414"></a><a name="p154301196414"></a>低电平输出电流</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.3 "><p id="p12430591419"><a name="p12430591419"></a><a name="p12430591419"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.340000000000002%" headers="mcps1.2.8.1.4 "><p id="p154301198412"><a name="p154301198412"></a><a name="p154301198412"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p1549762341014"><a name="p1549762341014"></a><a name="p1549762341014"></a>36.27</p>
</td>
<td class="cellrowborder" valign="top" width="9.280000000000001%" headers="mcps1.2.8.1.6 "><p id="p17430129043"><a name="p17430129043"></a><a name="p17430129043"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" width="15.46%" headers="mcps1.2.8.1.7 "><p id="p164308913418"><a name="p164308913418"></a><a name="p164308913418"></a>16驱IO档位0</p>
</td>
</tr>
<tr id="row883712104413"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p84301791048"><a name="p84301791048"></a><a name="p84301791048"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p5431491040"><a name="p5431491040"></a><a name="p5431491040"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p194968237106"><a name="p194968237106"></a><a name="p194968237106"></a>34.13</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p174313912415"><a name="p174313912415"></a><a name="p174313912415"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p12431291443"><a name="p12431291443"></a><a name="p12431291443"></a>16驱IO档位1</p>
</td>
</tr>
<tr id="row18837310442"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p643119242"><a name="p643119242"></a><a name="p643119242"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p1743119913410"><a name="p1743119913410"></a><a name="p1743119913410"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p11495182311012"><a name="p11495182311012"></a><a name="p11495182311012"></a>32.0</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p20431991845"><a name="p20431991845"></a><a name="p20431991845"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p154311991546"><a name="p154311991546"></a><a name="p154311991546"></a>16驱IO档位2</p>
</td>
</tr>
<tr id="row4837181012419"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p74318910417"><a name="p74318910417"></a><a name="p74318910417"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p4431169948"><a name="p4431169948"></a><a name="p4431169948"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p16495523131013"><a name="p16495523131013"></a><a name="p16495523131013"></a>29.86</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1543114919414"><a name="p1543114919414"></a><a name="p1543114919414"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p34311991841"><a name="p34311991841"></a><a name="p34311991841"></a>16驱IO档位3</p>
</td>
</tr>
<tr id="row1883720101144"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p5431497413"><a name="p5431497413"></a><a name="p5431497413"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p154311491542"><a name="p154311491542"></a><a name="p154311491542"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p04949235101"><a name="p04949235101"></a><a name="p04949235101"></a>27.73</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p16431691545"><a name="p16431691545"></a><a name="p16431691545"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p04311691142"><a name="p04311691142"></a><a name="p04311691142"></a>16驱IO档位4</p>
</td>
</tr>
<tr id="row158371410444"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p11431149745"><a name="p11431149745"></a><a name="p11431149745"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p1143110918411"><a name="p1143110918411"></a><a name="p1143110918411"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p1149492318100"><a name="p1149492318100"></a><a name="p1149492318100"></a>25.6</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p194321996414"><a name="p194321996414"></a><a name="p194321996414"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p443212911412"><a name="p443212911412"></a><a name="p443212911412"></a>16驱IO档位5</p>
</td>
</tr>
<tr id="row1483714108410"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p194321796414"><a name="p194321796414"></a><a name="p194321796414"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p1432891149"><a name="p1432891149"></a><a name="p1432891149"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p14931623161010"><a name="p14931623161010"></a><a name="p14931623161010"></a>23.47</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p104321391745"><a name="p104321391745"></a><a name="p104321391745"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p15432391748"><a name="p15432391748"></a><a name="p15432391748"></a>16驱IO档位6</p>
</td>
</tr>
<tr id="row138371610545"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p134322099419"><a name="p134322099419"></a><a name="p134322099419"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p74321091343"><a name="p74321091343"></a><a name="p74321091343"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p1249272314105"><a name="p1249272314105"></a><a name="p1249272314105"></a>21.33</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1443217915413"><a name="p1443217915413"></a><a name="p1443217915413"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1143214919413"><a name="p1143214919413"></a><a name="p1143214919413"></a>16驱IO档位7</p>
</td>
</tr>
<tr id="row15837111019411"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p184321693411"><a name="p184321693411"></a><a name="p184321693411"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p16432891143"><a name="p16432891143"></a><a name="p16432891143"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p18492122320108"><a name="p18492122320108"></a><a name="p18492122320108"></a>19.2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p20432893411"><a name="p20432893411"></a><a name="p20432893411"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p64326913414"><a name="p64326913414"></a><a name="p64326913414"></a>16驱IO档位8</p>
</td>
</tr>
<tr id="row6837141016415"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p164321891045"><a name="p164321891045"></a><a name="p164321891045"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p15432591744"><a name="p15432591744"></a><a name="p15432591744"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p549132311016"><a name="p549132311016"></a><a name="p549132311016"></a>17.07</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p144321493416"><a name="p144321493416"></a><a name="p144321493416"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p843213915410"><a name="p843213915410"></a><a name="p843213915410"></a>16驱IO档位9</p>
</td>
</tr>
<tr id="row1483741019411"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1843379243"><a name="p1843379243"></a><a name="p1843379243"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p164332917413"><a name="p164332917413"></a><a name="p164332917413"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p149115231103"><a name="p149115231103"></a><a name="p149115231103"></a>14.93</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p12433398417"><a name="p12433398417"></a><a name="p12433398417"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p5433199349"><a name="p5433199349"></a><a name="p5433199349"></a>16驱IO档位10</p>
</td>
</tr>
<tr id="row1837810441"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p5441791944"><a name="p5441791944"></a><a name="p5441791944"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p114411918418"><a name="p114411918418"></a><a name="p114411918418"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p17490132331015"><a name="p17490132331015"></a><a name="p17490132331015"></a>12.8</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p8441691410"><a name="p8441691410"></a><a name="p8441691410"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1644118917416"><a name="p1644118917416"></a><a name="p1644118917416"></a>16驱IO档位11</p>
</td>
</tr>
<tr id="row16837810047"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p114411891245"><a name="p114411891245"></a><a name="p114411891245"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p174414915419"><a name="p174414915419"></a><a name="p174414915419"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p449082301013"><a name="p449082301013"></a><a name="p449082301013"></a>10.67</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p124412913419"><a name="p124412913419"></a><a name="p124412913419"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1441696413"><a name="p1441696413"></a><a name="p1441696413"></a>16驱IO档位12</p>
</td>
</tr>
<tr id="row12837510340"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p64416916418"><a name="p64416916418"></a><a name="p64416916418"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p1441791345"><a name="p1441791345"></a><a name="p1441791345"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p19489182315106"><a name="p19489182315106"></a><a name="p19489182315106"></a>8.535</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p3442119642"><a name="p3442119642"></a><a name="p3442119642"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1442297410"><a name="p1442297410"></a><a name="p1442297410"></a>16驱IO档位13</p>
</td>
</tr>
<tr id="row15836111019419"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p144211910411"><a name="p144211910411"></a><a name="p144211910411"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p154421992414"><a name="p154421992414"></a><a name="p154421992414"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p1348812233104"><a name="p1348812233104"></a><a name="p1348812233104"></a>6.401</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p8442149544"><a name="p8442149544"></a><a name="p8442149544"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1944269848"><a name="p1944269848"></a><a name="p1944269848"></a>16驱IO档位14</p>
</td>
</tr>
<tr id="row683514102420"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p15442691247"><a name="p15442691247"></a><a name="p15442691247"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p9442191143"><a name="p9442191143"></a><a name="p9442191143"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p1847022391014"><a name="p1847022391014"></a><a name="p1847022391014"></a>4.268</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p844259542"><a name="p844259542"></a><a name="p844259542"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p3442139343"><a name="p3442139343"></a><a name="p3442139343"></a>16驱IO档位15</p>
</td>
</tr>
</tbody>
</table>

**表 4**  DC电气参数表 （VDDIO=1.8V GPIO 功能--SDIO专用\)

<a name="table673792515312"></a>
<table><thead align="left"><tr id="row19737172583119"><th class="cellrowborder" valign="top" width="22.650000000000002%" id="mcps1.2.8.1.1"><p id="p14737132513119"><a name="p14737132513119"></a><a name="p14737132513119"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="19.62%" id="mcps1.2.8.1.2"><p id="p15737325133118"><a name="p15737325133118"></a><a name="p15737325133118"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="11.33%" id="mcps1.2.8.1.3"><p id="p11737162520317"><a name="p11737162520317"></a><a name="p11737162520317"></a>最小值</p>
</th>
<th class="cellrowborder" valign="top" width="11.35%" id="mcps1.2.8.1.4"><p id="p3737925163117"><a name="p3737925163117"></a><a name="p3737925163117"></a>典型值</p>
</th>
<th class="cellrowborder" valign="top" width="10.31%" id="mcps1.2.8.1.5"><p id="p87371225173117"><a name="p87371225173117"></a><a name="p87371225173117"></a>最大值</p>
</th>
<th class="cellrowborder" valign="top" width="9.28%" id="mcps1.2.8.1.6"><p id="p67371025163113"><a name="p67371025163113"></a><a name="p67371025163113"></a>单位</p>
</th>
<th class="cellrowborder" valign="top" width="15.459999999999999%" id="mcps1.2.8.1.7"><p id="p117371825103111"><a name="p117371825103111"></a><a name="p117371825103111"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row97371252314"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p0737182514316"><a name="p0737182514316"></a><a name="p0737182514316"></a>VDDPST</p>
</td>
<td class="cellrowborder" valign="top" width="19.62%" headers="mcps1.2.8.1.2 "><p id="p8737525123115"><a name="p8737525123115"></a><a name="p8737525123115"></a>接口电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.33%" headers="mcps1.2.8.1.3 "><p id="p973772553115"><a name="p973772553115"></a><a name="p973772553115"></a>1.62</p>
</td>
<td class="cellrowborder" valign="top" width="11.35%" headers="mcps1.2.8.1.4 "><p id="p45821232472"><a name="p45821232472"></a><a name="p45821232472"></a>1.8</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p1873732573111"><a name="p1873732573111"></a><a name="p1873732573111"></a>1.98</p>
</td>
<td class="cellrowborder" valign="top" width="9.28%" headers="mcps1.2.8.1.6 "><p id="p2073832573115"><a name="p2073832573115"></a><a name="p2073832573115"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.2.8.1.7 "><p id="p473822533116"><a name="p473822533116"></a><a name="p473822533116"></a>-</p>
</td>
</tr>
<tr id="row10738152513315"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p973817253316"><a name="p973817253316"></a><a name="p973817253316"></a>V<sub id="sub373817257313"><a name="sub373817257313"></a><a name="sub373817257313"></a>IH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.62%" headers="mcps1.2.8.1.2 "><p id="p1773816252315"><a name="p1773816252315"></a><a name="p1773816252315"></a>高电平输入电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.33%" headers="mcps1.2.8.1.3 "><p id="p11738925113118"><a name="p11738925113118"></a><a name="p11738925113118"></a>1.2</p>
</td>
<td class="cellrowborder" valign="top" width="11.35%" headers="mcps1.2.8.1.4 "><p id="p20738192583118"><a name="p20738192583118"></a><a name="p20738192583118"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p5738925173110"><a name="p5738925173110"></a><a name="p5738925173110"></a>1.98</p>
</td>
<td class="cellrowborder" valign="top" width="9.28%" headers="mcps1.2.8.1.6 "><p id="p1373812251318"><a name="p1373812251318"></a><a name="p1373812251318"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.2.8.1.7 ">&nbsp;&nbsp;</td>
</tr>
<tr id="row37381425173115"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p9738192520316"><a name="p9738192520316"></a><a name="p9738192520316"></a>V<sub id="sub1373872520319"><a name="sub1373872520319"></a><a name="sub1373872520319"></a>IL</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.62%" headers="mcps1.2.8.1.2 "><p id="p18738182533110"><a name="p18738182533110"></a><a name="p18738182533110"></a>低电平输入电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.33%" headers="mcps1.2.8.1.3 "><p id="p473810256319"><a name="p473810256319"></a><a name="p473810256319"></a>–0.3</p>
</td>
<td class="cellrowborder" valign="top" width="11.35%" headers="mcps1.2.8.1.4 "><p id="p67388255313"><a name="p67388255313"></a><a name="p67388255313"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p1973813253315"><a name="p1973813253315"></a><a name="p1973813253315"></a>0.6</p>
</td>
<td class="cellrowborder" valign="top" width="9.28%" headers="mcps1.2.8.1.6 "><p id="p57381425123111"><a name="p57381425123111"></a><a name="p57381425123111"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.2.8.1.7 "><p id="p473811255316"><a name="p473811255316"></a><a name="p473811255316"></a>-</p>
</td>
</tr>
<tr id="row207388254316"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p1738152513115"><a name="p1738152513115"></a><a name="p1738152513115"></a>I<sub id="sub673817250311"><a name="sub673817250311"></a><a name="sub673817250311"></a>L</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.62%" headers="mcps1.2.8.1.2 "><p id="p137388251314"><a name="p137388251314"></a><a name="p137388251314"></a>输入漏电流</p>
</td>
<td class="cellrowborder" valign="top" width="11.33%" headers="mcps1.2.8.1.3 "><p id="p913212511042"><a name="p913212511042"></a><a name="p913212511042"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.35%" headers="mcps1.2.8.1.4 "><p id="p9739152593115"><a name="p9739152593115"></a><a name="p9739152593115"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p773982543117"><a name="p773982543117"></a><a name="p773982543117"></a>&plusmn;10</p>
</td>
<td class="cellrowborder" valign="top" width="9.28%" headers="mcps1.2.8.1.6 "><p id="p17739825103112"><a name="p17739825103112"></a><a name="p17739825103112"></a>μA</p>
</td>
<td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.2.8.1.7 "><p id="p77391725123118"><a name="p77391725123118"></a><a name="p77391725123118"></a>-</p>
</td>
</tr>
<tr id="row17391925163113"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p3739925123117"><a name="p3739925123117"></a><a name="p3739925123117"></a>I<sub id="sub47397258311"><a name="sub47397258311"></a><a name="sub47397258311"></a>OZ</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.62%" headers="mcps1.2.8.1.2 "><p id="p97392250311"><a name="p97392250311"></a><a name="p97392250311"></a>三态输出漏电流</p>
</td>
<td class="cellrowborder" valign="top" width="11.33%" headers="mcps1.2.8.1.3 "><p id="p115010515420"><a name="p115010515420"></a><a name="p115010515420"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.35%" headers="mcps1.2.8.1.4 ">&nbsp;&nbsp;</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p1973902520317"><a name="p1973902520317"></a><a name="p1973902520317"></a>&plusmn;10</p>
</td>
<td class="cellrowborder" valign="top" width="9.28%" headers="mcps1.2.8.1.6 "><p id="p87391625143117"><a name="p87391625143117"></a><a name="p87391625143117"></a>nA</p>
</td>
<td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.2.8.1.7 "><p id="p177397255314"><a name="p177397255314"></a><a name="p177397255314"></a>-</p>
</td>
</tr>
<tr id="row11739132519314"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p3739162533119"><a name="p3739162533119"></a><a name="p3739162533119"></a>V<sub id="sub13739525193113"><a name="sub13739525193113"></a><a name="sub13739525193113"></a>OH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.62%" headers="mcps1.2.8.1.2 "><p id="p20739122583116"><a name="p20739122583116"></a><a name="p20739122583116"></a>高电平输出电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.33%" headers="mcps1.2.8.1.3 "><p id="p1773972511315"><a name="p1773972511315"></a><a name="p1773972511315"></a>VDDPST-0.45</p>
</td>
<td class="cellrowborder" valign="top" width="11.35%" headers="mcps1.2.8.1.4 "><p id="p11739112573110"><a name="p11739112573110"></a><a name="p11739112573110"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p13739625123118"><a name="p13739625123118"></a><a name="p13739625123118"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.28%" headers="mcps1.2.8.1.6 "><p id="p11739152515318"><a name="p11739152515318"></a><a name="p11739152515318"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.2.8.1.7 "><p id="p17391525153113"><a name="p17391525153113"></a><a name="p17391525153113"></a>VDDPST=1.8V&plusmn;10%</p>
</td>
</tr>
<tr id="row1973972533114"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p117391325113113"><a name="p117391325113113"></a><a name="p117391325113113"></a>V<sub id="sub1073916253318"><a name="sub1073916253318"></a><a name="sub1073916253318"></a>OL</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.62%" headers="mcps1.2.8.1.2 "><p id="p27396255312"><a name="p27396255312"></a><a name="p27396255312"></a>低电平输出电压</p>
</td>
<td class="cellrowborder" valign="top" width="11.33%" headers="mcps1.2.8.1.3 "><p id="p11740162513319"><a name="p11740162513319"></a><a name="p11740162513319"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.35%" headers="mcps1.2.8.1.4 "><p id="p17401625163120"><a name="p17401625163120"></a><a name="p17401625163120"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p10740192593114"><a name="p10740192593114"></a><a name="p10740192593114"></a>0.45</p>
</td>
<td class="cellrowborder" valign="top" width="9.28%" headers="mcps1.2.8.1.6 "><p id="p16740192573110"><a name="p16740192573110"></a><a name="p16740192573110"></a>V</p>
</td>
<td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.2.8.1.7 "><p id="p2740102573116"><a name="p2740102573116"></a><a name="p2740102573116"></a>-</p>
</td>
</tr>
<tr id="row7740142573119"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p874072517314"><a name="p874072517314"></a><a name="p874072517314"></a>R<sub id="sub16740325193117"><a name="sub16740325193117"></a><a name="sub16740325193117"></a>PU</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.62%" headers="mcps1.2.8.1.2 "><p id="p274013258315"><a name="p274013258315"></a><a name="p274013258315"></a>内部上拉电阻</p>
</td>
<td class="cellrowborder" valign="top" width="11.33%" headers="mcps1.2.8.1.3 "><p id="p2740142514316"><a name="p2740142514316"></a><a name="p2740142514316"></a>19</p>
</td>
<td class="cellrowborder" valign="top" width="11.35%" headers="mcps1.2.8.1.4 "><p id="p1274042503111"><a name="p1274042503111"></a><a name="p1274042503111"></a>25</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p274017257319"><a name="p274017257319"></a><a name="p274017257319"></a>31</p>
</td>
<td class="cellrowborder" valign="top" width="9.28%" headers="mcps1.2.8.1.6 "><p id="p15740202512312"><a name="p15740202512312"></a><a name="p15740202512312"></a>kΩ</p>
</td>
<td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.2.8.1.7 "><p id="p16740172518314"><a name="p16740172518314"></a><a name="p16740172518314"></a>-</p>
</td>
</tr>
<tr id="row147401925113113"><td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p10740162543112"><a name="p10740162543112"></a><a name="p10740162543112"></a>R<sub id="sub7740172520315"><a name="sub7740172520315"></a><a name="sub7740172520315"></a>PD</sub></p>
</td>
<td class="cellrowborder" valign="top" width="19.62%" headers="mcps1.2.8.1.2 "><p id="p2740132543113"><a name="p2740132543113"></a><a name="p2740132543113"></a>内部下拉电阻</p>
</td>
<td class="cellrowborder" valign="top" width="11.33%" headers="mcps1.2.8.1.3 "><p id="p2074022573114"><a name="p2074022573114"></a><a name="p2074022573114"></a>19</p>
</td>
<td class="cellrowborder" valign="top" width="11.35%" headers="mcps1.2.8.1.4 "><p id="p1974015255319"><a name="p1974015255319"></a><a name="p1974015255319"></a>25</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p1474072533116"><a name="p1474072533116"></a><a name="p1474072533116"></a>31</p>
</td>
<td class="cellrowborder" valign="top" width="9.28%" headers="mcps1.2.8.1.6 "><p id="p1774092517311"><a name="p1774092517311"></a><a name="p1774092517311"></a>kΩ</p>
</td>
<td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.2.8.1.7 "><p id="p77403252316"><a name="p77403252316"></a><a name="p77403252316"></a>-</p>
</td>
</tr>
<tr id="row6740132503118"><td class="cellrowborder" rowspan="16" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p9740162520312"><a name="p9740162520312"></a><a name="p9740162520312"></a>I<sub id="sub1674032573113"><a name="sub1674032573113"></a><a name="sub1674032573113"></a>OH</sub></p>
</td>
<td class="cellrowborder" rowspan="16" valign="top" width="19.62%" headers="mcps1.2.8.1.2 "><p id="p117402255317"><a name="p117402255317"></a><a name="p117402255317"></a>高电平输出电流</p>
</td>
<td class="cellrowborder" valign="top" width="11.33%" headers="mcps1.2.8.1.3 "><p id="p274032583115"><a name="p274032583115"></a><a name="p274032583115"></a>18.97</p>
</td>
<td class="cellrowborder" valign="top" width="11.35%" headers="mcps1.2.8.1.4 "><p id="p1992653945"><a name="p1992653945"></a><a name="p1992653945"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p15617548415"><a name="p15617548415"></a><a name="p15617548415"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.28%" headers="mcps1.2.8.1.6 "><p id="p17412254317"><a name="p17412254317"></a><a name="p17412254317"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.2.8.1.7 "><p id="p10741142543116"><a name="p10741142543116"></a><a name="p10741142543116"></a>16驱IO档位0</p>
</td>
</tr>
<tr id="row8741202543117"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p574172593111"><a name="p574172593111"></a><a name="p574172593111"></a>17.85</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p2228548413"><a name="p2228548413"></a><a name="p2228548413"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p183610541545"><a name="p183610541545"></a><a name="p183610541545"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p13741725123118"><a name="p13741725123118"></a><a name="p13741725123118"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p97411325173120"><a name="p97411325173120"></a><a name="p97411325173120"></a>16驱IO档位1</p>
</td>
</tr>
<tr id="row174118255313"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p9741132523110"><a name="p9741132523110"></a><a name="p9741132523110"></a>16.73</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p10493541745"><a name="p10493541745"></a><a name="p10493541745"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p126125411413"><a name="p126125411413"></a><a name="p126125411413"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1174132511317"><a name="p1174132511317"></a><a name="p1174132511317"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p18741102511319"><a name="p18741102511319"></a><a name="p18741102511319"></a>16驱IO档位2</p>
</td>
</tr>
<tr id="row1582420245372"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p18825172403710"><a name="p18825172403710"></a><a name="p18825172403710"></a>15.62</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p1173125416416"><a name="p1173125416416"></a><a name="p1173125416416"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p15853544415"><a name="p15853544415"></a><a name="p15853544415"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p4825142412374"><a name="p4825142412374"></a><a name="p4825142412374"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p178251624193719"><a name="p178251624193719"></a><a name="p178251624193719"></a>16驱IO档位3</p>
</td>
</tr>
<tr id="row1021736154013"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1621714654011"><a name="p1621714654011"></a><a name="p1621714654011"></a>14.5</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p797654946"><a name="p797654946"></a><a name="p797654946"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p91101054148"><a name="p91101054148"></a><a name="p91101054148"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p19964146124411"><a name="p19964146124411"></a><a name="p19964146124411"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p721714644014"><a name="p721714644014"></a><a name="p721714644014"></a>16驱IO档位4</p>
</td>
</tr>
<tr id="row1748913115405"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1048910118403"><a name="p1048910118403"></a><a name="p1048910118403"></a>13.39</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p151217549410"><a name="p151217549410"></a><a name="p151217549410"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p13133155415420"><a name="p13133155415420"></a><a name="p13133155415420"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p79647614449"><a name="p79647614449"></a><a name="p79647614449"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p2048914112401"><a name="p2048914112401"></a><a name="p2048914112401"></a>16驱IO档位5</p>
</td>
</tr>
<tr id="row1878159194012"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1578118919400"><a name="p1578118919400"></a><a name="p1578118919400"></a>12.27</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p214545415412"><a name="p214545415412"></a><a name="p214545415412"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p7156154341"><a name="p7156154341"></a><a name="p7156154341"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1696436124419"><a name="p1696436124419"></a><a name="p1696436124419"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p127811998405"><a name="p127811998405"></a><a name="p127811998405"></a>16驱IO档位6</p>
</td>
</tr>
<tr id="row419514854016"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p3196387406"><a name="p3196387406"></a><a name="p3196387406"></a>11.16</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p76331256647"><a name="p76331256647"></a><a name="p76331256647"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p1465105615417"><a name="p1465105615417"></a><a name="p1465105615417"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p996436204410"><a name="p996436204410"></a><a name="p996436204410"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p4196686405"><a name="p4196686405"></a><a name="p4196686405"></a>16驱IO档位7</p>
</td>
</tr>
<tr id="row8216134194016"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p121744144019"><a name="p121744144019"></a><a name="p121744144019"></a>10.04</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p166717561542"><a name="p166717561542"></a><a name="p166717561542"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p1468155614415"><a name="p1468155614415"></a><a name="p1468155614415"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p59071970447"><a name="p59071970447"></a><a name="p59071970447"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p15217134104012"><a name="p15217134104012"></a><a name="p15217134104012"></a>16驱IO档位8</p>
</td>
</tr>
<tr id="row1353113153919"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p83531531183916"><a name="p83531531183916"></a><a name="p83531531183916"></a>8.93</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p2069405612419"><a name="p2069405612419"></a><a name="p2069405612419"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p147061568414"><a name="p147061568414"></a><a name="p147061568414"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p149072774416"><a name="p149072774416"></a><a name="p149072774416"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p53533317398"><a name="p53533317398"></a><a name="p53533317398"></a>16驱IO档位9</p>
</td>
</tr>
<tr id="row16801142813910"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1580182873920"><a name="p1580182873920"></a><a name="p1580182873920"></a>7.81</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p14718656444"><a name="p14718656444"></a><a name="p14718656444"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p14731756244"><a name="p14731756244"></a><a name="p14731756244"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p5907197114413"><a name="p5907197114413"></a><a name="p5907197114413"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1580112813913"><a name="p1580112813913"></a><a name="p1580112813913"></a>16驱IO档位10</p>
</td>
</tr>
<tr id="row8648126173914"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p8649102616397"><a name="p8649102616397"></a><a name="p8649102616397"></a>6.69</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p197449567415"><a name="p197449567415"></a><a name="p197449567415"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p1375620566415"><a name="p1375620566415"></a><a name="p1375620566415"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1890711794420"><a name="p1890711794420"></a><a name="p1890711794420"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p464917269399"><a name="p464917269399"></a><a name="p464917269399"></a>16驱IO档位11</p>
</td>
</tr>
<tr id="row18801172423917"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p6801524113910"><a name="p6801524113910"></a><a name="p6801524113910"></a>5.58</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p076915561344"><a name="p076915561344"></a><a name="p076915561344"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p10782656948"><a name="p10782656948"></a><a name="p10782656948"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p0995111184416"><a name="p0995111184416"></a><a name="p0995111184416"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p10801172415394"><a name="p10801172415394"></a><a name="p10801172415394"></a>16驱IO档位12</p>
</td>
</tr>
<tr id="row58621522193916"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p14862152219399"><a name="p14862152219399"></a><a name="p14862152219399"></a>4.46</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p13795456542"><a name="p13795456542"></a><a name="p13795456542"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p128071456243"><a name="p128071456243"></a><a name="p128071456243"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p199519112444"><a name="p199519112444"></a><a name="p199519112444"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p4862182211398"><a name="p4862182211398"></a><a name="p4862182211398"></a>16驱IO档位13</p>
</td>
</tr>
<tr id="row11530112810372"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p453102815374"><a name="p453102815374"></a><a name="p453102815374"></a>3.35</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p0820456542"><a name="p0820456542"></a><a name="p0820456542"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p98331564415"><a name="p98331564415"></a><a name="p98331564415"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p17995611194413"><a name="p17995611194413"></a><a name="p17995611194413"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p653120286371"><a name="p653120286371"></a><a name="p653120286371"></a>16驱IO档位14</p>
</td>
</tr>
<tr id="row6947733193714"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1794793317378"><a name="p1794793317378"></a><a name="p1794793317378"></a>2.23</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p38460561147"><a name="p38460561147"></a><a name="p38460561147"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p58589561444"><a name="p58589561444"></a><a name="p58589561444"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p390316137449"><a name="p390316137449"></a><a name="p390316137449"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p12947633163717"><a name="p12947633163717"></a><a name="p12947633163717"></a>16驱IO档位15</p>
</td>
</tr>
<tr id="row1474114256311"><td class="cellrowborder" rowspan="16" valign="top" width="22.650000000000002%" headers="mcps1.2.8.1.1 "><p id="p074122523119"><a name="p074122523119"></a><a name="p074122523119"></a>I<sub id="sub574182515311"><a name="sub574182515311"></a><a name="sub574182515311"></a>OL</sub></p>
</td>
<td class="cellrowborder" rowspan="16" valign="top" width="19.62%" headers="mcps1.2.8.1.2 "><p id="p2741152523110"><a name="p2741152523110"></a><a name="p2741152523110"></a>低电平输出电流</p>
</td>
<td class="cellrowborder" valign="top" width="11.33%" headers="mcps1.2.8.1.3 "><p id="p101581201059"><a name="p101581201059"></a><a name="p101581201059"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="11.35%" headers="mcps1.2.8.1.4 "><p id="p3174801359"><a name="p3174801359"></a><a name="p3174801359"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.8.1.5 "><p id="p71276558314"><a name="p71276558314"></a><a name="p71276558314"></a>17.14</p>
</td>
<td class="cellrowborder" valign="top" width="9.28%" headers="mcps1.2.8.1.6 "><p id="p5742152513313"><a name="p5742152513313"></a><a name="p5742152513313"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.2.8.1.7 "><p id="p1974314844410"><a name="p1974314844410"></a><a name="p1974314844410"></a>16驱IO档位0</p>
</td>
</tr>
<tr id="row1742325113110"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p12189500510"><a name="p12189500510"></a><a name="p12189500510"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p520114017512"><a name="p520114017512"></a><a name="p520114017512"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p1172719811323"><a name="p1172719811323"></a><a name="p1172719811323"></a>16.13</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p17421225153120"><a name="p17421225153120"></a><a name="p17421225153120"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p574384810443"><a name="p574384810443"></a><a name="p574384810443"></a>16驱IO档位1</p>
</td>
</tr>
<tr id="row17953103115431"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1021311014517"><a name="p1021311014517"></a><a name="p1021311014517"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p142251020511"><a name="p142251020511"></a><a name="p142251020511"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p14815310153211"><a name="p14815310153211"></a><a name="p14815310153211"></a>15.13</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1697824904519"><a name="p1697824904519"></a><a name="p1697824904519"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1074474814448"><a name="p1074474814448"></a><a name="p1074474814448"></a>16驱IO档位2</p>
</td>
</tr>
<tr id="row4539348124314"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p623790756"><a name="p623790756"></a><a name="p623790756"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p8252170552"><a name="p8252170552"></a><a name="p8252170552"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p2495234133216"><a name="p2495234133216"></a><a name="p2495234133216"></a>14.12</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1697916494454"><a name="p1697916494454"></a><a name="p1697916494454"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p674424834417"><a name="p674424834417"></a><a name="p674424834417"></a>16驱IO档位3</p>
</td>
</tr>
<tr id="row5897135412433"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p192651701259"><a name="p192651701259"></a><a name="p192651701259"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p15278709516"><a name="p15278709516"></a><a name="p15278709516"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p09042040153218"><a name="p09042040153218"></a><a name="p09042040153218"></a>13.11</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1997984914510"><a name="p1997984914510"></a><a name="p1997984914510"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p18744154844413"><a name="p18744154844413"></a><a name="p18744154844413"></a>16驱IO档位4</p>
</td>
</tr>
<tr id="row1718510537437"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p72891901854"><a name="p72891901854"></a><a name="p72891901854"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p183011506511"><a name="p183011506511"></a><a name="p183011506511"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p16184154712325"><a name="p16184154712325"></a><a name="p16184154712325"></a>12.1</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1497944917451"><a name="p1497944917451"></a><a name="p1497944917451"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p16744154814411"><a name="p16744154814411"></a><a name="p16744154814411"></a>16驱IO档位5</p>
</td>
</tr>
<tr id="row988117506433"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p183129011514"><a name="p183129011514"></a><a name="p183129011514"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p153241601858"><a name="p153241601858"></a><a name="p153241601858"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p188255024315"><a name="p188255024315"></a><a name="p188255024315"></a></p>
<p id="p143771353153211"><a name="p143771353153211"></a><a name="p143771353153211"></a>11.09</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p19979184916459"><a name="p19979184916459"></a><a name="p19979184916459"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p15744154819446"><a name="p15744154819446"></a><a name="p15744154819446"></a>16驱IO档位6</p>
</td>
</tr>
<tr id="row13609164644317"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p6335502055"><a name="p6335502055"></a><a name="p6335502055"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p1034613012517"><a name="p1034613012517"></a><a name="p1034613012517"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p86093469438"><a name="p86093469438"></a><a name="p86093469438"></a>10.08</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p9979549194519"><a name="p9979549194519"></a><a name="p9979549194519"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p97441748144413"><a name="p97441748144413"></a><a name="p97441748144413"></a>16驱IO档位7</p>
</td>
</tr>
<tr id="row36519440430"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1735780654"><a name="p1735780654"></a><a name="p1735780654"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p5367100958"><a name="p5367100958"></a><a name="p5367100958"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p165114419436"><a name="p165114419436"></a><a name="p165114419436"></a>9.08</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p99791449144519"><a name="p99791449144519"></a><a name="p99791449144519"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p374434804417"><a name="p374434804417"></a><a name="p374434804417"></a>16驱IO档位8</p>
</td>
</tr>
<tr id="row10388194215437"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p18378190253"><a name="p18378190253"></a><a name="p18378190253"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p1538914019518"><a name="p1538914019518"></a><a name="p1538914019518"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p45911952103212"><a name="p45911952103212"></a><a name="p45911952103212"></a>8.07</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p11979184934515"><a name="p11979184934515"></a><a name="p11979184934515"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p4744164810446"><a name="p4744164810446"></a><a name="p4744164810446"></a>16驱IO档位9</p>
</td>
</tr>
<tr id="row23144074310"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p44001020520"><a name="p44001020520"></a><a name="p44001020520"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p74117010513"><a name="p74117010513"></a><a name="p74117010513"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p1931174034319"><a name="p1931174034319"></a><a name="p1931174034319"></a></p>
<p id="p12569104817321"><a name="p12569104817321"></a><a name="p12569104817321"></a>7.06</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p149798492456"><a name="p149798492456"></a><a name="p149798492456"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p147441448124418"><a name="p147441448124418"></a><a name="p147441448124418"></a>16驱IO档位10</p>
</td>
</tr>
<tr id="row10129183874315"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1422180052"><a name="p1422180052"></a><a name="p1422180052"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p134331301450"><a name="p134331301450"></a><a name="p134331301450"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p11302383432"><a name="p11302383432"></a><a name="p11302383432"></a></p>
<p id="p10266104217322"><a name="p10266104217322"></a><a name="p10266104217322"></a>6.05</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p12979204913455"><a name="p12979204913455"></a><a name="p12979204913455"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p19744204864410"><a name="p19744204864410"></a><a name="p19744204864410"></a>16驱IO档位11</p>
</td>
</tr>
<tr id="row52761236174319"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p1844420451"><a name="p1844420451"></a><a name="p1844420451"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p13455501554"><a name="p13455501554"></a><a name="p13455501554"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p102761236164312"><a name="p102761236164312"></a><a name="p102761236164312"></a></p>
<p id="p81651036153216"><a name="p81651036153216"></a><a name="p81651036153216"></a>5.04</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p69809496454"><a name="p69809496454"></a><a name="p69809496454"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p187448486448"><a name="p187448486448"></a><a name="p187448486448"></a>16驱IO档位12</p>
</td>
</tr>
<tr id="row1012283454315"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p4466180655"><a name="p4466180655"></a><a name="p4466180655"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p14477706517"><a name="p14477706517"></a><a name="p14477706517"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p16782151283211"><a name="p16782151283211"></a><a name="p16782151283211"></a>4.03</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p7980104954516"><a name="p7980104954516"></a><a name="p7980104954516"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p12744164884419"><a name="p12744164884419"></a><a name="p12744164884419"></a>16驱IO档位13</p>
</td>
</tr>
<tr id="row57451429144315"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p194881601450"><a name="p194881601450"></a><a name="p194881601450"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p10499401151"><a name="p10499401151"></a><a name="p10499401151"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p210216683215"><a name="p210216683215"></a><a name="p210216683215"></a>3.03</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p0980049174518"><a name="p0980049174518"></a><a name="p0980049174518"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p15745184824417"><a name="p15745184824417"></a><a name="p15745184824417"></a>16驱IO档位14</p>
</td>
</tr>
<tr id="row7857182718436"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p175111508519"><a name="p175111508519"></a><a name="p175111508519"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.2 "><p id="p1752212011512"><a name="p1752212011512"></a><a name="p1752212011512"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p1785832711436"><a name="p1785832711436"></a><a name="p1785832711436"></a></p>
<p id="p0791758163117"><a name="p0791758163117"></a><a name="p0791758163117"></a>2.02</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1090115380453"><a name="p1090115380453"></a><a name="p1090115380453"></a>mA</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p117451748104418"><a name="p117451748104418"></a><a name="p117451748104418"></a>16驱IO档位15</p>
</td>
</tr>
</tbody>
</table>

## 上下电要求<a name="ZH-CN_TOPIC_0000001762979362"></a>

![](figures/上电时序.png)

1.  外部电池电源VBAT、IO电源VDDIO处于下电状态，芯片处于下电状态。
2.  外部电源VBAT、VDDIO上电（推荐同时上电）。其中VBAT可能存在慢上电场景、VBAT上电稳定约40μs\~10ms。
3.  VBAT和VDDIO上电后约20ms后、CLDO上电稳定、开始CRG解复位。
4.  WS53V100开机电源系统上无Power-on信号、POR模块主要是对VBAT和内部电源进行检测、当两者都在位时、才会送出芯片内部的解复位信号。
5.  VBAT上电阈值：2.5V；

    VBAT下电阈值： 1.4V。

6.  WS53V100开机电源系统上无Power-on信号、外部有RST\_N负责全芯片复位、其状态由板级电路维护。
7.  VBAT欠压或者撤离时、POR检查到掉电、会复位整个芯片、从而实现安全下电。

>![](public_sys-resources/icon-note.gif) **说明：** 
>-   PMU电源对应管脚：VDD\_VBAT1、VDD\_VBAT2、AVDD33。
>-   VDDIO对应管脚：VDDIO。
>-   当芯片掉电后，需要保证VDDIO和VBAT电平低于200mV。
>-   单板复位通过RST\_N管脚实现。RST\_N行为为拉低、后拉高。其中RST\_N拉低时间需要持续10ms以上。

# 原理图设计建议<a name="ZH-CN_TOPIC_0000001456082716"></a>

-   **[小系统设计建议](#ZH-CN_TOPIC_0000001505842481)**  

-   **[电源参考设计](#ZH-CN_TOPIC_0000001505842445)**  

-   **[外围接口设计建议](#ZH-CN_TOPIC_0000001505603517)**  

-   **[控制信号及低功耗应用参考设计](#ZH-CN_TOPIC_0000001505842493)**  

## 小系统设计建议<a name="ZH-CN_TOPIC_0000001505842481"></a>

小系统指芯片电路能够正常工作的最小外围电路配置，此部分的电路主要包括：时钟电路、复位电路。

-   **[参考时钟设计](#ZH-CN_TOPIC_0000001505842485)**  

-   **[RTC时钟](#ZH-CN_TOPIC_0000002018433230)**  

-   **[复位电路](#ZH-CN_TOPIC_0000001456082748)**  

### 参考时钟设计<a name="ZH-CN_TOPIC_0000001505842485"></a>

晶体时钟支持32MHz，在使用外部晶体时，电路结构如[图1](#fig1341612873619)所示。其中，Cload电容默认不上件，XIN，XOUT串联0Ω电阻，用于调节晶体寄生电容，30Ω为限流电阻（根据晶体的DL参数决定是否上件）。

**图 1**  使用Crystal输入参考时钟的参考电路图<a name="fig1341612873619"></a>  
![](figures/使用Crystal输入参考时钟的参考电路图.png "使用Crystal输入参考时钟的参考电路图")

外部Crystal电气特性的要求如[表1](#table8856940134)所示。

**表 1**  Crystal电气特性要求

<a name="table8856940134"></a>
<table><thead align="left"><tr id="row88573400318"><th class="cellrowborder" valign="top" id="mcps1.2.9.1.1"><p id="p10701195120311"><a name="p10701195120311"></a><a name="p10701195120311"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.9.1.2"><p id="p170111519319"><a name="p170111519319"></a><a name="p170111519319"></a>符号</p>
</th>
<th class="cellrowborder" colspan="4" valign="top" id="mcps1.2.9.1.3"><p id="p167032664017"><a name="p167032664017"></a><a name="p167032664017"></a>晶体选型规格</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.9.1.4"><p id="p370216511932"><a name="p370216511932"></a><a name="p370216511932"></a>单位</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.9.1.5"><p id="p77026518310"><a name="p77026518310"></a><a name="p77026518310"></a>备注</p>
</th>
</tr>
</thead>
<tbody><tr id="row169487812717"><td class="cellrowborder" valign="top" width="14.48855114488551%" headers="mcps1.2.9.1.1 "><p id="p494808102718"><a name="p494808102718"></a><a name="p494808102718"></a>标称频率</p>
</td>
<td class="cellrowborder" valign="top" width="11.908809119088092%" headers="mcps1.2.9.1.2 "><p id="p129480818274"><a name="p129480818274"></a><a name="p129480818274"></a>f</p>
</td>
<td class="cellrowborder" valign="top" width="10.64893510648935%" headers="mcps1.2.9.1.3 "><p id="p1128144943617"><a name="p1128144943617"></a><a name="p1128144943617"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="12.1987801219878%" headers="mcps1.2.9.1.3 "><p id="p14948168172719"><a name="p14948168172719"></a><a name="p14948168172719"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="11.668833116688331%" headers="mcps1.2.9.1.3 "><p id="p1148265153615"><a name="p1148265153615"></a><a name="p1148265153615"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="11.50884911508849%" headers="mcps1.2.9.1.3 "><p id="p132931610114018"><a name="p132931610114018"></a><a name="p132931610114018"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="10.608939106089391%" headers="mcps1.2.9.1.4 "><p id="p494818811271"><a name="p494818811271"></a><a name="p494818811271"></a>MHz</p>
</td>
<td class="cellrowborder" valign="top" width="16.96830316968303%" headers="mcps1.2.9.1.5 "><p id="p59481086277"><a name="p59481086277"></a><a name="p59481086277"></a>-</p>
</td>
</tr>
<tr id="row7702643123810"><td class="cellrowborder" valign="top" width="14.48855114488551%" headers="mcps1.2.9.1.1 "><p id="p1783644716265"><a name="p1783644716265"></a><a name="p1783644716265"></a>负载电容</p>
</td>
<td class="cellrowborder" valign="top" width="11.908809119088092%" headers="mcps1.2.9.1.2 "><p id="p38372470262"><a name="p38372470262"></a><a name="p38372470262"></a>CL</p>
</td>
<td class="cellrowborder" valign="top" width="10.64893510648935%" headers="mcps1.2.9.1.3 "><p id="p128371647132620"><a name="p128371647132620"></a><a name="p128371647132620"></a>7</p>
</td>
<td class="cellrowborder" valign="top" width="12.1987801219878%" headers="mcps1.2.9.1.3 "><p id="p138371347142610"><a name="p138371347142610"></a><a name="p138371347142610"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="11.668833116688331%" headers="mcps1.2.9.1.3 "><p id="p1583713475264"><a name="p1583713475264"></a><a name="p1583713475264"></a>9</p>
</td>
<td class="cellrowborder" valign="top" width="11.50884911508849%" headers="mcps1.2.9.1.3 "><p id="p71951951113917"><a name="p71951951113917"></a><a name="p71951951113917"></a>12[1]</p>
</td>
<td class="cellrowborder" valign="top" width="10.608939106089391%" headers="mcps1.2.9.1.4 "><p id="p1683754752616"><a name="p1683754752616"></a><a name="p1683754752616"></a>pF</p>
</td>
<td class="cellrowborder" valign="top" width="16.96830316968303%" headers="mcps1.2.9.1.5 "><p id="p7837347112614"><a name="p7837347112614"></a><a name="p7837347112614"></a>-</p>
</td>
</tr>
<tr id="row1458152642016"><td class="cellrowborder" valign="top" width="14.48855114488551%" headers="mcps1.2.9.1.1 "><p id="p0458626122011"><a name="p0458626122011"></a><a name="p0458626122011"></a>Xout串联电容</p>
</td>
<td class="cellrowborder" valign="top" width="11.908809119088092%" headers="mcps1.2.9.1.2 "><p id="p8458826152016"><a name="p8458826152016"></a><a name="p8458826152016"></a>C</p>
</td>
<td class="cellrowborder" valign="top" width="10.64893510648935%" headers="mcps1.2.9.1.3 "><p id="p1345815265203"><a name="p1345815265203"></a><a name="p1345815265203"></a>18</p>
</td>
<td class="cellrowborder" valign="top" width="12.1987801219878%" headers="mcps1.2.9.1.3 "><p id="p5458126122010"><a name="p5458126122010"></a><a name="p5458126122010"></a>18</p>
</td>
<td class="cellrowborder" valign="top" width="11.668833116688331%" headers="mcps1.2.9.1.3 "><p id="p17458426152020"><a name="p17458426152020"></a><a name="p17458426152020"></a>27</p>
</td>
<td class="cellrowborder" valign="top" width="11.50884911508849%" headers="mcps1.2.9.1.3 "><p id="p2458826202016"><a name="p2458826202016"></a><a name="p2458826202016"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.608939106089391%" headers="mcps1.2.9.1.4 "><p id="p545832662013"><a name="p545832662013"></a><a name="p545832662013"></a>pF</p>
</td>
<td class="cellrowborder" valign="top" width="16.96830316968303%" headers="mcps1.2.9.1.5 "><p id="p19939195216242"><a name="p19939195216242"></a><a name="p19939195216242"></a>XOUT预留0Ω电阻串位，用于调节晶体寄生电容。其中12pF晶体无需串联电容。</p>
</td>
</tr>
<tr id="row1225143142718"><td class="cellrowborder" valign="top" width="14.48855114488551%" headers="mcps1.2.9.1.1 "><p id="p322615302716"><a name="p322615302716"></a><a name="p322615302716"></a>频率容差</p>
</td>
<td class="cellrowborder" valign="top" width="11.908809119088092%" headers="mcps1.2.9.1.2 "><p id="p1722633182710"><a name="p1722633182710"></a><a name="p1722633182710"></a>f_tol</p>
</td>
<td class="cellrowborder" valign="top" width="10.64893510648935%" headers="mcps1.2.9.1.3 "><p id="p922693122716"><a name="p922693122716"></a><a name="p922693122716"></a>&plusmn;10</p>
</td>
<td class="cellrowborder" valign="top" width="12.1987801219878%" headers="mcps1.2.9.1.3 "><p id="p1150718356371"><a name="p1150718356371"></a><a name="p1150718356371"></a>&plusmn;10</p>
</td>
<td class="cellrowborder" valign="top" width="11.668833116688331%" headers="mcps1.2.9.1.3 "><p id="p122266312710"><a name="p122266312710"></a><a name="p122266312710"></a>&plusmn;10</p>
</td>
<td class="cellrowborder" valign="top" width="11.50884911508849%" headers="mcps1.2.9.1.3 "><p id="p9994187104018"><a name="p9994187104018"></a><a name="p9994187104018"></a>&plusmn;10</p>
</td>
<td class="cellrowborder" valign="top" width="10.608939106089391%" headers="mcps1.2.9.1.4 "><p id="p1422643152712"><a name="p1422643152712"></a><a name="p1422643152712"></a>ppm</p>
</td>
<td class="cellrowborder" valign="top" width="16.96830316968303%" headers="mcps1.2.9.1.5 "><p id="p2022615382715"><a name="p2022615382715"></a><a name="p2022615382715"></a>晶体初始频偏</p>
</td>
</tr>
<tr id="row842213547374"><td class="cellrowborder" valign="top" width="14.48855114488551%" headers="mcps1.2.9.1.1 "><p id="p316114153254"><a name="p316114153254"></a><a name="p316114153254"></a>频率稳定性</p>
</td>
<td class="cellrowborder" valign="top" width="11.908809119088092%" headers="mcps1.2.9.1.2 "><p id="p7161101502519"><a name="p7161101502519"></a><a name="p7161101502519"></a>f_temp</p>
</td>
<td class="cellrowborder" valign="top" width="10.64893510648935%" headers="mcps1.2.9.1.3 "><p id="p98991554164118"><a name="p98991554164118"></a><a name="p98991554164118"></a>&plusmn;10</p>
</td>
<td class="cellrowborder" valign="top" width="12.1987801219878%" headers="mcps1.2.9.1.3 "><p id="p168991454174117"><a name="p168991454174117"></a><a name="p168991454174117"></a>&plusmn;10</p>
</td>
<td class="cellrowborder" valign="top" width="11.668833116688331%" headers="mcps1.2.9.1.3 "><p id="p20899185414112"><a name="p20899185414112"></a><a name="p20899185414112"></a>&plusmn;10</p>
</td>
<td class="cellrowborder" valign="top" width="11.50884911508849%" headers="mcps1.2.9.1.3 "><p id="p68999540413"><a name="p68999540413"></a><a name="p68999540413"></a>&plusmn;10</p>
</td>
<td class="cellrowborder" valign="top" width="10.608939106089391%" headers="mcps1.2.9.1.4 "><p id="p989945454110"><a name="p989945454110"></a><a name="p989945454110"></a>ppm</p>
</td>
<td class="cellrowborder" valign="top" width="16.96830316968303%" headers="mcps1.2.9.1.5 "><p id="p1216161518253"><a name="p1216161518253"></a><a name="p1216161518253"></a>晶体温漂</p>
</td>
</tr>
<tr id="row199381515399"><td class="cellrowborder" valign="top" width="14.48855114488551%" headers="mcps1.2.9.1.1 "><p id="p3716143915403"><a name="p3716143915403"></a><a name="p3716143915403"></a>激励功率</p>
</td>
<td class="cellrowborder" valign="top" width="11.908809119088092%" headers="mcps1.2.9.1.2 "><p id="p197166392406"><a name="p197166392406"></a><a name="p197166392406"></a>DL[2]</p>
</td>
<td class="cellrowborder" valign="top" width="10.64893510648935%" headers="mcps1.2.9.1.3 "><p id="p77161391404"><a name="p77161391404"></a><a name="p77161391404"></a>≥100</p>
</td>
<td class="cellrowborder" valign="top" width="12.1987801219878%" headers="mcps1.2.9.1.3 "><p id="p115741385420"><a name="p115741385420"></a><a name="p115741385420"></a>≥100</p>
</td>
<td class="cellrowborder" valign="top" width="11.668833116688331%" headers="mcps1.2.9.1.3 "><p id="p10588386428"><a name="p10588386428"></a><a name="p10588386428"></a>≥100</p>
</td>
<td class="cellrowborder" valign="top" width="11.50884911508849%" headers="mcps1.2.9.1.3 "><p id="p059910864214"><a name="p059910864214"></a><a name="p059910864214"></a>≥100</p>
</td>
<td class="cellrowborder" valign="top" width="10.608939106089391%" headers="mcps1.2.9.1.4 "><p id="p171715395400"><a name="p171715395400"></a><a name="p171715395400"></a>&micro;W</p>
</td>
<td class="cellrowborder" valign="top" width="16.96830316968303%" headers="mcps1.2.9.1.5 "><p id="p1717183964012"><a name="p1717183964012"></a><a name="p1717183964012"></a>-</p>
</td>
</tr>
<tr id="row37385612615"><td class="cellrowborder" valign="top" width="14.48855114488551%" headers="mcps1.2.9.1.1 "><p id="p11733561265"><a name="p11733561265"></a><a name="p11733561265"></a>等效电阻</p>
</td>
<td class="cellrowborder" valign="top" width="11.908809119088092%" headers="mcps1.2.9.1.2 "><p id="p373165614264"><a name="p373165614264"></a><a name="p373165614264"></a>ESR</p>
</td>
<td class="cellrowborder" valign="top" width="10.64893510648935%" headers="mcps1.2.9.1.3 "><p id="p873145682611"><a name="p873145682611"></a><a name="p873145682611"></a>≤60 max</p>
</td>
<td class="cellrowborder" valign="top" width="12.1987801219878%" headers="mcps1.2.9.1.3 "><p id="p1270719210378"><a name="p1270719210378"></a><a name="p1270719210378"></a>≤60 max</p>
</td>
<td class="cellrowborder" valign="top" width="11.668833116688331%" headers="mcps1.2.9.1.3 "><p id="p147091121193712"><a name="p147091121193712"></a><a name="p147091121193712"></a>≤60 max</p>
</td>
<td class="cellrowborder" valign="top" width="11.50884911508849%" headers="mcps1.2.9.1.3 "><p id="p20368924174516"><a name="p20368924174516"></a><a name="p20368924174516"></a>≤60 max</p>
</td>
<td class="cellrowborder" valign="top" width="10.608939106089391%" headers="mcps1.2.9.1.4 "><p id="p473125672618"><a name="p473125672618"></a><a name="p473125672618"></a>Ω</p>
</td>
<td class="cellrowborder" valign="top" width="16.96830316968303%" headers="mcps1.2.9.1.5 "><p id="p47315613260"><a name="p47315613260"></a><a name="p47315613260"></a>-</p>
</td>
</tr>
<tr id="row17436126192517"><td class="cellrowborder" valign="top" width="14.48855114488551%" headers="mcps1.2.9.1.1 "><p id="p43131133142915"><a name="p43131133142915"></a><a name="p43131133142915"></a>动态电感</p>
</td>
<td class="cellrowborder" valign="top" width="11.908809119088092%" headers="mcps1.2.9.1.2 "><p id="p1331313342913"><a name="p1331313342913"></a><a name="p1331313342913"></a>Lm[3]</p>
</td>
<td class="cellrowborder" valign="top" width="10.64893510648935%" headers="mcps1.2.9.1.3 "><p id="p3313183311293"><a name="p3313183311293"></a><a name="p3313183311293"></a>8.3~10.8</p>
</td>
<td class="cellrowborder" valign="top" width="12.1987801219878%" headers="mcps1.2.9.1.3 "><p id="p533213437343"><a name="p533213437343"></a><a name="p533213437343"></a>7.1~10.0</p>
</td>
<td class="cellrowborder" valign="top" width="11.668833116688331%" headers="mcps1.2.9.1.3 "><p id="p5331144313415"><a name="p5331144313415"></a><a name="p5331144313415"></a>5.8~11.7</p>
</td>
<td class="cellrowborder" valign="top" width="11.50884911508849%" headers="mcps1.2.9.1.3 "><p id="p1919510518392"><a name="p1919510518392"></a><a name="p1919510518392"></a>5.8~9.2</p>
</td>
<td class="cellrowborder" valign="top" width="10.608939106089391%" headers="mcps1.2.9.1.4 "><p id="p133112435349"><a name="p133112435349"></a><a name="p133112435349"></a>mH</p>
</td>
<td class="cellrowborder" valign="top" width="16.96830316968303%" headers="mcps1.2.9.1.5 "><p id="p5313163311297"><a name="p5313163311297"></a><a name="p5313163311297"></a>-</p>
</td>
</tr>
<tr id="row89247481254"><td class="cellrowborder" valign="top" width="14.48855114488551%" headers="mcps1.2.9.1.1 "><p id="p15924124815251"><a name="p15924124815251"></a><a name="p15924124815251"></a>动态电容</p>
</td>
<td class="cellrowborder" valign="top" width="11.908809119088092%" headers="mcps1.2.9.1.2 "><p id="p19924204815259"><a name="p19924204815259"></a><a name="p19924204815259"></a>C1[3]</p>
</td>
<td class="cellrowborder" valign="top" width="10.64893510648935%" headers="mcps1.2.9.1.3 "><p id="p1924194882513"><a name="p1924194882513"></a><a name="p1924194882513"></a>2.3~3</p>
</td>
<td class="cellrowborder" valign="top" width="12.1987801219878%" headers="mcps1.2.9.1.3 "><p id="p1792416481251"><a name="p1792416481251"></a><a name="p1792416481251"></a>2.48~3.5</p>
</td>
<td class="cellrowborder" valign="top" width="11.668833116688331%" headers="mcps1.2.9.1.3 "><p id="p89248488258"><a name="p89248488258"></a><a name="p89248488258"></a>2.12~4.29</p>
</td>
<td class="cellrowborder" valign="top" width="11.50884911508849%" headers="mcps1.2.9.1.3 "><p id="p19196751153914"><a name="p19196751153914"></a><a name="p19196751153914"></a>2.7~5.55</p>
</td>
<td class="cellrowborder" valign="top" width="10.608939106089391%" headers="mcps1.2.9.1.4 "><p id="p2924164832518"><a name="p2924164832518"></a><a name="p2924164832518"></a>fF</p>
</td>
<td class="cellrowborder" valign="top" width="16.96830316968303%" headers="mcps1.2.9.1.5 "><p id="p1992444822519"><a name="p1992444822519"></a><a name="p1992444822519"></a>-</p>
</td>
</tr>
<tr id="row17215133516257"><td class="cellrowborder" valign="top" width="14.48855114488551%" headers="mcps1.2.9.1.1 "><p id="p1421510351258"><a name="p1421510351258"></a><a name="p1421510351258"></a>静态电容</p>
</td>
<td class="cellrowborder" valign="top" width="11.908809119088092%" headers="mcps1.2.9.1.2 "><p id="p8215183592511"><a name="p8215183592511"></a><a name="p8215183592511"></a>C0</p>
</td>
<td class="cellrowborder" valign="top" width="10.64893510648935%" headers="mcps1.2.9.1.3 "><p id="p17215193512258"><a name="p17215193512258"></a><a name="p17215193512258"></a>≤2</p>
</td>
<td class="cellrowborder" valign="top" width="12.1987801219878%" headers="mcps1.2.9.1.3 "><p id="p1717414614353"><a name="p1717414614353"></a><a name="p1717414614353"></a>≤2</p>
</td>
<td class="cellrowborder" valign="top" width="11.668833116688331%" headers="mcps1.2.9.1.3 "><p id="p11205117133511"><a name="p11205117133511"></a><a name="p11205117133511"></a>≤2</p>
</td>
<td class="cellrowborder" valign="top" width="11.50884911508849%" headers="mcps1.2.9.1.3 "><p id="p145081588357"><a name="p145081588357"></a><a name="p145081588357"></a>≤2</p>
</td>
<td class="cellrowborder" valign="top" width="10.608939106089391%" headers="mcps1.2.9.1.4 "><p id="p1066761284519"><a name="p1066761284519"></a><a name="p1066761284519"></a>pF</p>
</td>
<td class="cellrowborder" valign="top" width="16.96830316968303%" headers="mcps1.2.9.1.5 "><p id="p221513542510"><a name="p221513542510"></a><a name="p221513542510"></a>-</p>
</td>
</tr>
<tr id="row19416113931217"><td class="cellrowborder" valign="top" width="14.48855114488551%" headers="mcps1.2.9.1.1 "><p id="p4417039101215"><a name="p4417039101215"></a><a name="p4417039101215"></a>工作温度</p>
</td>
<td class="cellrowborder" valign="top" width="11.908809119088092%" headers="mcps1.2.9.1.2 "><p id="p5417153910125"><a name="p5417153910125"></a><a name="p5417153910125"></a>T</p>
</td>
<td class="cellrowborder" valign="top" width="10.64893510648935%" headers="mcps1.2.9.1.3 "><p id="p1241713396129"><a name="p1241713396129"></a><a name="p1241713396129"></a>-30~+85</p>
</td>
<td class="cellrowborder" valign="top" width="12.1987801219878%" headers="mcps1.2.9.1.3 "><p id="p0667175514412"><a name="p0667175514412"></a><a name="p0667175514412"></a>-30~+85</p>
</td>
<td class="cellrowborder" valign="top" width="11.668833116688331%" headers="mcps1.2.9.1.3 "><p id="p106724557448"><a name="p106724557448"></a><a name="p106724557448"></a>-30~+85</p>
</td>
<td class="cellrowborder" valign="top" width="11.50884911508849%" headers="mcps1.2.9.1.3 "><p id="p7674155194413"><a name="p7674155194413"></a><a name="p7674155194413"></a>-30~+85</p>
</td>
<td class="cellrowborder" valign="top" width="10.608939106089391%" headers="mcps1.2.9.1.4 "><p id="p124187398128"><a name="p124187398128"></a><a name="p124187398128"></a>℃</p>
</td>
<td class="cellrowborder" valign="top" width="16.96830316968303%" headers="mcps1.2.9.1.5 "><p id="p4857640172319"><a name="p4857640172319"></a><a name="p4857640172319"></a>-</p>
</td>
</tr>
<tr id="row18471555104114"><td class="cellrowborder" valign="top" width="14.48855114488551%" headers="mcps1.2.9.1.1 "><p id="p11471165544115"><a name="p11471165544115"></a><a name="p11471165544115"></a>存储温度</p>
</td>
<td class="cellrowborder" valign="top" width="11.908809119088092%" headers="mcps1.2.9.1.2 "><p id="p2047116559410"><a name="p2047116559410"></a><a name="p2047116559410"></a>T_s</p>
</td>
<td class="cellrowborder" valign="top" width="10.64893510648935%" headers="mcps1.2.9.1.3 "><p id="p04711655134120"><a name="p04711655134120"></a><a name="p04711655134120"></a>-40~+125</p>
</td>
<td class="cellrowborder" valign="top" width="12.1987801219878%" headers="mcps1.2.9.1.3 "><p id="p10740152111489"><a name="p10740152111489"></a><a name="p10740152111489"></a>-40~+125</p>
</td>
<td class="cellrowborder" valign="top" width="11.668833116688331%" headers="mcps1.2.9.1.3 "><p id="p375492144813"><a name="p375492144813"></a><a name="p375492144813"></a>-40~+125</p>
</td>
<td class="cellrowborder" valign="top" width="11.50884911508849%" headers="mcps1.2.9.1.3 "><p id="p1876562104814"><a name="p1876562104814"></a><a name="p1876562104814"></a>-40~+125</p>
</td>
<td class="cellrowborder" valign="top" width="10.608939106089391%" headers="mcps1.2.9.1.4 "><p id="p19174162434812"><a name="p19174162434812"></a><a name="p19174162434812"></a>℃</p>
</td>
<td class="cellrowborder" valign="top" width="16.96830316968303%" headers="mcps1.2.9.1.5 "><p id="p825504034819"><a name="p825504034819"></a><a name="p825504034819"></a>-</p>
</td>
</tr>
</tbody>
</table>

其中：

-   CL：Crystal负载电容。
-   ESR：Crystal等效串联电阻。
-   推荐晶体参数：CL 8pF，ESR 60Ω\(max\)，Lm 9.97mH，C1 2.48fF，C0 0.7pF。
-   1612封装因为C1和Lm差异较大，频偏校准范围只支持±20ppm。
-   XIN和XOUT管脚PKG+PCB寄生电容≤1pF。
-   负载电容CL=\(C1×C2\)/\(C1+C2\)+Cs，其中C1为XIN管脚对地总电容，C2为XOUT管脚对地总电容，Cs为XIN和XOUT管脚之间寄生电容，如C1和C2均为14pF，Cs为1pF，则晶体的负载电容为8pF。
-   标注\[1\]：CL为12pF的晶体，XO支撑以慢启方式启动。
-   标注\[2\]：建议晶体选型时DL（max）≥100μW，若晶体DL（max）小于100μW，须在XOUT处串联30Ω电阻R，并且XO频偏校准范围为±20ppm。
-   标注\[3\]：表格里是Type值，Lm和C1覆盖范围是type值±10%。

### RTC时钟<a name="ZH-CN_TOPIC_0000002018433230"></a>

>![](public_sys-resources/icon-note.gif) **说明：** 
>使用此功能前，需确认芯片版本是否支持此功能，详见《芯片用户指南》或《订购须知》描述。

WS53V100支持外部提供32.768kHz RTC时钟，用于低功耗处理。对32.768kHz RTC时钟的电气特性要求如[表1](#table1518714490175)所示。

**表 1**  RTC无源时钟电气特性要求

<a name="table1518714490175"></a>
<table><thead align="left"><tr id="row1318794915173"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.1"><p id="p31871149151718"><a name="p31871149151718"></a><a name="p31871149151718"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.2"><p id="p5187249151716"><a name="p5187249151716"></a><a name="p5187249151716"></a>最小值</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.3"><p id="p17187204915179"><a name="p17187204915179"></a><a name="p17187204915179"></a>典型值</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.4"><p id="p61871749151713"><a name="p61871749151713"></a><a name="p61871749151713"></a>最大值</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.5"><p id="p1418717499179"><a name="p1418717499179"></a><a name="p1418717499179"></a>单位</p>
</th>
</tr>
</thead>
<tbody><tr id="row918718497171"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p81872049141713"><a name="p81872049141713"></a><a name="p81872049141713"></a>时钟频率</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p1718764919176"><a name="p1718764919176"></a><a name="p1718764919176"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p1118764912172"><a name="p1118764912172"></a><a name="p1118764912172"></a>32.768</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p131871949181711"><a name="p131871949181711"></a><a name="p131871949181711"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p418754915174"><a name="p418754915174"></a><a name="p418754915174"></a>kHz</p>
</td>
</tr>
<tr id="row418764951711"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p171871549101715"><a name="p171871549101715"></a><a name="p171871549101715"></a>频率误差</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p318774921715"><a name="p318774921715"></a><a name="p318774921715"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p81878491173"><a name="p81878491173"></a><a name="p81878491173"></a>≤&plusmn;100</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p151871649171711"><a name="p151871649171711"></a><a name="p151871649171711"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p11187114961715"><a name="p11187114961715"></a><a name="p11187114961715"></a>ppm</p>
</td>
</tr>
<tr id="row15187204911714"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p4187249201715"><a name="p4187249201715"></a><a name="p4187249201715"></a>负载电容（CL）</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p15187194919173"><a name="p15187194919173"></a><a name="p15187194919173"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p151879497175"><a name="p151879497175"></a><a name="p151879497175"></a>7</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p201871649141715"><a name="p201871649141715"></a><a name="p201871649141715"></a>12.5</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p181879497177"><a name="p181879497177"></a><a name="p181879497177"></a>pF</p>
</td>
</tr>
<tr id="row11871749151715"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p818718490176"><a name="p818718490176"></a><a name="p818718490176"></a>激励功率<span id="ph7346843153912"><a name="ph7346843153912"></a><a name="ph7346843153912"></a>DL</span><span id="ph614510221720"><a name="ph614510221720"></a><a name="ph614510221720"></a>（max）</span></p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p17188124941714"><a name="p17188124941714"></a><a name="p17188124941714"></a>0.5</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p518874981717"><a name="p518874981717"></a><a name="p518874981717"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p318894912176"><a name="p318894912176"></a><a name="p318894912176"></a>1.5</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p1818804919177"><a name="p1818804919177"></a><a name="p1818804919177"></a>μW</p>
</td>
</tr>
</tbody>
</table>

RTC无源时钟参考电路设计如[图1](#fig59311429311)所示，其中C1&C2可以基于晶体负载电容CL计算，典型C1=C2=CL\*2，考虑封装和板级寄生，C1&C2取值可以略小；

**图 1**  RTC无源时钟参考设计电路<a name="fig59311429311"></a>  
![](figures/RTC无源时钟参考设计电路.png "RTC无源时钟参考设计电路")

针对无源时钟，需要根据所选晶体的ESR参数，选择相对应的驱动能力，详细参考[表2](#table121851430171013)；

**表 2**  驱动能力与ESR对照表

<a name="table121851430171013"></a>
<table><thead align="left"><tr id="row20186103013104"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p6186143021012"><a name="p6186143021012"></a><a name="p6186143021012"></a>CL</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1618615306102"><a name="p1618615306102"></a><a name="p1618615306102"></a>DS1:DS0</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p618613017100"><a name="p618613017100"></a><a name="p618613017100"></a>ESR_Max</p>
</th>
</tr>
</thead>
<tbody><tr id="row118603081019"><td class="cellrowborder" rowspan="4" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p818620301104"><a name="p818620301104"></a><a name="p818620301104"></a>7p</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15186193071015"><a name="p15186193071015"></a><a name="p15186193071015"></a>00</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p201861930101010"><a name="p201861930101010"></a><a name="p201861930101010"></a>50kΩ</p>
</td>
</tr>
<tr id="row1418616308107"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p61861130171010"><a name="p61861130171010"></a><a name="p61861130171010"></a>01</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p16232437191212"><a name="p16232437191212"></a><a name="p16232437191212"></a>90kΩ</p>
</td>
</tr>
<tr id="row3186103081017"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p17186203012102"><a name="p17186203012102"></a><a name="p17186203012102"></a>10</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p6905143714122"><a name="p6905143714122"></a><a name="p6905143714122"></a>130kΩ</p>
</td>
</tr>
<tr id="row61869301102"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1618612305101"><a name="p1618612305101"></a><a name="p1618612305101"></a>11</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p05456387120"><a name="p05456387120"></a><a name="p05456387120"></a>170kΩ</p>
</td>
</tr>
<tr id="row18186103091014"><td class="cellrowborder" rowspan="4" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1018620305109"><a name="p1018620305109"></a><a name="p1018620305109"></a>12.5p</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5186153051014"><a name="p5186153051014"></a><a name="p5186153051014"></a>00</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15121237191318"><a name="p15121237191318"></a><a name="p15121237191318"></a>20kΩ</p>
</td>
</tr>
<tr id="row1718693013102"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p161861530141011"><a name="p161861530141011"></a><a name="p161861530141011"></a>01</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1892216419137"><a name="p1892216419137"></a><a name="p1892216419137"></a>35kΩ</p>
</td>
</tr>
<tr id="row41863309107"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p318683051014"><a name="p318683051014"></a><a name="p318683051014"></a>10</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1031313327139"><a name="p1031313327139"></a><a name="p1031313327139"></a>50kΩ</p>
</td>
</tr>
<tr id="row73111716111319"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p6311191612132"><a name="p6311191612132"></a><a name="p6311191612132"></a>11</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p10969103311139"><a name="p10969103311139"></a><a name="p10969103311139"></a>70kΩ</p>
</td>
</tr>
</tbody>
</table>

### 复位电路<a name="ZH-CN_TOPIC_0000001456082748"></a>

WS53V100集成内部 POR （Power On Reset ）电路以及 Watchdog。

**图 1**  WS53V100 RST\_N电路<a name="fig19289164313226"></a>  
![](figures/WS53V100-RST_N电路.png "WS53V100-RST_N电路")

## 电源参考设计<a name="ZH-CN_TOPIC_0000001505842445"></a>

>![](public_sys-resources/icon-note.gif) **说明：** 
>系统电源的设计，详细请参见《WS53V100 DEMO板原理图》。

-   **[电源规格](#ZH-CN_TOPIC_0000001505882577)**  

-   **[VBAT电源](#ZH-CN_TOPIC_0000001505603553)**  

-   **[VDDIO电源](#ZH-CN_TOPIC_0000001455763056)**  

-   **[内部电源滤波电路](#ZH-CN_TOPIC_0000001505603525)**  

-   **[RFLDO1](#ZH-CN_TOPIC_0000001505882541)**  

-   **[BUCK/LDO电源](#ZH-CN_TOPIC_0000001505882569)**  

-   **[PA供电](#ZH-CN_TOPIC_0000001505603537)**  

-   **[注意事项](#ZH-CN_TOPIC_0000001456082736)**  

### 电源规格<a name="ZH-CN_TOPIC_0000001505882577"></a>

WS53V100需要的外部电源包括：

-   电池电源VBAT
-   IO电源VDDIO

芯片内部主要集成了BUCK和多个低压差线性稳压器（LDO）：

-   BUCK：作为一个中间的电源平面给多个LDO提供电源。
-   LDO：分为给数字提供电源的LDO和低噪声LDO。
-   PMU内部有一个BUCK提供1.3V电源。

    推荐工作条件如[表1](#table52313500)所示。

**表 1**  推荐工作条件

<a name="table52313500"></a>
<table><thead align="left"><tr id="row39909729"><th class="cellrowborder" valign="top" width="7.5200000000000005%" id="mcps1.2.7.1.1"><p id="p8899165692717"><a name="p8899165692717"></a><a name="p8899165692717"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="17.47%" id="mcps1.2.7.1.2"><p id="p11462616"><a name="p11462616"></a><a name="p11462616"></a>管脚名称</p>
</th>
<th class="cellrowborder" valign="top" width="36.059999999999995%" id="mcps1.2.7.1.3"><p id="p56056695"><a name="p56056695"></a><a name="p56056695"></a>参数说明</p>
</th>
<th class="cellrowborder" valign="top" width="13.01%" id="mcps1.2.7.1.4"><p id="p44298471"><a name="p44298471"></a><a name="p44298471"></a>最小值（V）</p>
</th>
<th class="cellrowborder" valign="top" width="12.64%" id="mcps1.2.7.1.5"><p id="p14222289"><a name="p14222289"></a><a name="p14222289"></a>典型值（V）</p>
</th>
<th class="cellrowborder" valign="top" width="13.3%" id="mcps1.2.7.1.6"><p id="p33283626"><a name="p33283626"></a><a name="p33283626"></a>最大值（V）</p>
</th>
</tr>
</thead>
<tbody><tr id="row37463758"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p68341505546"><a name="p68341505546"></a><a name="p68341505546"></a>9</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p178349010549"><a name="p178349010549"></a><a name="p178349010549"></a>VDD_VBAT2</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p5834809545"><a name="p5834809545"></a><a name="p5834809545"></a>INTLDO和XLDO输入电源，由外部电源提供</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p19339155813399"><a name="p19339155813399"></a><a name="p19339155813399"></a>3.16</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p10089792"><a name="p10089792"></a><a name="p10089792"></a>3.3</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p11966832"><a name="p11966832"></a><a name="p11966832"></a>3.6</p>
</td>
</tr>
<tr id="row15277157193513"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p16834100145411"><a name="p16834100145411"></a><a name="p16834100145411"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p48357055413"><a name="p48357055413"></a><a name="p48357055413"></a>VDD_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p138352007548"><a name="p138352007548"></a><a name="p138352007548"></a>RFLDO1，RFLDO2输入电源</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p692032795419"><a name="p692032795419"></a><a name="p692032795419"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p189201427185416"><a name="p189201427185416"></a><a name="p189201427185416"></a>1.3</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p992018277549"><a name="p992018277549"></a><a name="p992018277549"></a>-</p>
</td>
</tr>
<tr id="row7800184553718"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p883580135412"><a name="p883580135412"></a><a name="p883580135412"></a>13</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p1483517012544"><a name="p1483517012544"></a><a name="p1483517012544"></a>VDD_WL_RF_TRX_1P1</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p148351005547"><a name="p148351005547"></a><a name="p148351005547"></a>芯片内部TRX相关模块输入电源</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p822273516333"><a name="p822273516333"></a><a name="p822273516333"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p1922303513317"><a name="p1922303513317"></a><a name="p1922303513317"></a>1.15</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p112237354338"><a name="p112237354338"></a><a name="p112237354338"></a>-</p>
</td>
</tr>
<tr id="row429912404329"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p1683517085413"><a name="p1683517085413"></a><a name="p1683517085413"></a>14</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p1083512015417"><a name="p1083512015417"></a><a name="p1083512015417"></a>VDD_WL_RF_PA_3P3</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p168354011545"><a name="p168354011545"></a><a name="p168354011545"></a>WiFi PA供电电源，由外部电源提供</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p34080294119"><a name="p34080294119"></a><a name="p34080294119"></a>3.16</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p24094387352"><a name="p24094387352"></a><a name="p24094387352"></a>3.3</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p640993843510"><a name="p640993843510"></a><a name="p640993843510"></a>3.6</p>
</td>
</tr>
<tr id="row40592626"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p78351501545"><a name="p78351501545"></a><a name="p78351501545"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p38356016545"><a name="p38356016545"></a><a name="p38356016545"></a>VDD_RF_RX_1P1</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p1483530165419"><a name="p1483530165419"></a><a name="p1483530165419"></a>芯片LNA输入电源</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p320523733319"><a name="p320523733319"></a><a name="p320523733319"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p2020533710338"><a name="p2020533710338"></a><a name="p2020533710338"></a>1.15</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p16205133720336"><a name="p16205133720336"></a><a name="p16205133720336"></a>-</p>
</td>
</tr>
<tr id="row635014154358"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p1683550205413"><a name="p1683550205413"></a><a name="p1683550205413"></a>17</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p283517012541"><a name="p283517012541"></a><a name="p283517012541"></a>VDD_BSLE_RF_PA_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p48351107549"><a name="p48351107549"></a><a name="p48351107549"></a>BSLE LDO输入电源</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p39460615"><a name="p39460615"></a><a name="p39460615"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p42193260"><a name="p42193260"></a><a name="p42193260"></a>1.3</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p62210885"><a name="p62210885"></a><a name="p62210885"></a>-</p>
</td>
</tr>
<tr id="row18313622173510"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p183518012549"><a name="p183518012549"></a><a name="p183518012549"></a>19</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p683515015416"><a name="p683515015416"></a><a name="p683515015416"></a>VDD_BSLE_RF_DRV_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p28351005548"><a name="p28351005548"></a><a name="p28351005548"></a>BSLE LDO输入电源</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p1731402214358"><a name="p1731402214358"></a><a name="p1731402214358"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p1531422216353"><a name="p1531422216353"></a><a name="p1531422216353"></a>1.3</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p1531492263511"><a name="p1531492263511"></a><a name="p1531492263511"></a>-</p>
</td>
</tr>
<tr id="row16809195611366"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p1883520055417"><a name="p1883520055417"></a><a name="p1883520055417"></a>20</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p283612095415"><a name="p283612095415"></a><a name="p283612095415"></a>VDD_BSLE_PLL_DCO_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p128361606547"><a name="p128361606547"></a><a name="p128361606547"></a>BSLE LDO输入电源</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p20661154154611"><a name="p20661154154611"></a><a name="p20661154154611"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p466195464614"><a name="p466195464614"></a><a name="p466195464614"></a>1.3</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p1066195412468"><a name="p1066195412468"></a><a name="p1066195412468"></a>-</p>
</td>
</tr>
<tr id="row54786185354"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p1283617015413"><a name="p1283617015413"></a><a name="p1283617015413"></a>37</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p178361606540"><a name="p178361606540"></a><a name="p178361606540"></a>VDDIO</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p48369075419"><a name="p48369075419"></a><a name="p48369075419"></a>IO电源，由外部电源提供</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p38910283"><a name="p38910283"></a><a name="p38910283"></a>1.71</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p64725258"><a name="p64725258"></a><a name="p64725258"></a>1.8/3.3</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p8254578"><a name="p8254578"></a><a name="p8254578"></a>3.465</p>
</td>
</tr>
<tr id="row7182340"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p1783610016540"><a name="p1783610016540"></a><a name="p1783610016540"></a>38</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p12836701547"><a name="p12836701547"></a><a name="p12836701547"></a>AVDD33</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p1483611016549"><a name="p1483611016549"></a><a name="p1483611016549"></a>LSADC和REF供电电源，由外部电源提供</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p4328114194115"><a name="p4328114194115"></a><a name="p4328114194115"></a>3.16</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p1296543711352"><a name="p1296543711352"></a><a name="p1296543711352"></a>3.3</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p16942165115385"><a name="p16942165115385"></a><a name="p16942165115385"></a>3.465</p>
</td>
</tr>
<tr id="row133815122351"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p48366013544"><a name="p48366013544"></a><a name="p48366013544"></a>39</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p38366095410"><a name="p38366095410"></a><a name="p38366095410"></a>VDD_VBAT1</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p7836200105412"><a name="p7836200105412"></a><a name="p7836200105412"></a>芯片BUCK输入电源，由外部电源提供</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p14156165144115"><a name="p14156165144115"></a><a name="p14156165144115"></a>3.16</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p14570153917543"><a name="p14570153917543"></a><a name="p14570153917543"></a>3.3</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p13557135313814"><a name="p13557135313814"></a><a name="p13557135313814"></a>3.465</p>
</td>
</tr>
<tr id="row3288825"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p1183617018544"><a name="p1183617018544"></a><a name="p1183617018544"></a>41</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p1683640145414"><a name="p1683640145414"></a><a name="p1683640145414"></a>VDD1P3_PMU1</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p1083617095415"><a name="p1083617095415"></a><a name="p1083617095415"></a>芯片BUCK反馈及CLDO输入</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p33254639"><a name="p33254639"></a><a name="p33254639"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p9271271"><a name="p9271271"></a><a name="p9271271"></a>1.3</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p356757133710"><a name="p356757133710"></a><a name="p356757133710"></a>-</p>
</td>
</tr>
<tr id="row16175844143619"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p38361602546"><a name="p38361602546"></a><a name="p38361602546"></a>6</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p783614075419"><a name="p783614075419"></a><a name="p783614075419"></a>XLDO_OUT</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p1683619065414"><a name="p1683619065414"></a><a name="p1683619065414"></a>芯片XLDO decap管脚，接板级滤波电容</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p13222323184911"><a name="p13222323184911"></a><a name="p13222323184911"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p1222292324910"><a name="p1222292324910"></a><a name="p1222292324910"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p122221239493"><a name="p122221239493"></a><a name="p122221239493"></a>-</p>
</td>
</tr>
<tr id="row189292416368"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p15836110205417"><a name="p15836110205417"></a><a name="p15836110205417"></a>11</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p1383616016540"><a name="p1383616016540"></a><a name="p1383616016540"></a>VDD_RFLDO1</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p383617095412"><a name="p383617095412"></a><a name="p383617095412"></a>内部LDO电源，输出提供给VDD_WL_RF_TRX_1P1、</p>
<p id="p1983650145414"><a name="p1983650145414"></a><a name="p1983650145414"></a>VDD_RF_RX_1P1</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p9385930115013"><a name="p9385930115013"></a><a name="p9385930115013"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p638613305508"><a name="p638613305508"></a><a name="p638613305508"></a>1.15</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p123867304505"><a name="p123867304505"></a><a name="p123867304505"></a>-</p>
</td>
</tr>
<tr id="row1539134317380"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p38362015419"><a name="p38362015419"></a><a name="p38362015419"></a>12</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p1837160175418"><a name="p1837160175418"></a><a name="p1837160175418"></a>VDD_RFLDO2</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p1283717095416"><a name="p1283717095416"></a><a name="p1283717095416"></a>RFLDO2电源decap管脚，接板级滤波电容</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p18942300502"><a name="p18942300502"></a><a name="p18942300502"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p9413102253317"><a name="p9413102253317"></a><a name="p9413102253317"></a>1.15</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p1389483085016"><a name="p1389483085016"></a><a name="p1389483085016"></a>-</p>
</td>
</tr>
<tr id="row076412389"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p6837409542"><a name="p6837409542"></a><a name="p6837409542"></a>18</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p683714019540"><a name="p683714019540"></a><a name="p683714019540"></a>VDD_BSLE_DPALDO</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p78375011542"><a name="p78375011542"></a><a name="p78375011542"></a>芯片内部BSLE电源decap管脚，接板级滤波电容</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p156811115175213"><a name="p156811115175213"></a><a name="p156811115175213"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p156821815165210"><a name="p156821815165210"></a><a name="p156821815165210"></a>1.1</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p206820157526"><a name="p206820157526"></a><a name="p206820157526"></a>-</p>
</td>
</tr>
<tr id="row14777133919361"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p2837204542"><a name="p2837204542"></a><a name="p2837204542"></a>40</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p183760205413"><a name="p183760205413"></a><a name="p183760205413"></a>BUCK_LX</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p483714075414"><a name="p483714075414"></a><a name="p483714075414"></a>芯片BUCK LX输出1.3V，接板级电感、电容滤波</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p33525997"><a name="p33525997"></a><a name="p33525997"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p31251245"><a name="p31251245"></a><a name="p31251245"></a>1.3</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p48322897"><a name="p48322897"></a><a name="p48322897"></a>-</p>
</td>
</tr>
<tr id="row17225737101817"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.7.1.1 "><p id="p1283710011548"><a name="p1283710011548"></a><a name="p1283710011548"></a>42</p>
</td>
<td class="cellrowborder" valign="top" width="17.47%" headers="mcps1.2.7.1.2 "><p id="p8837150195419"><a name="p8837150195419"></a><a name="p8837150195419"></a>VDD_CLDO</p>
</td>
<td class="cellrowborder" valign="top" width="36.059999999999995%" headers="mcps1.2.7.1.3 "><p id="p183720165419"><a name="p183720165419"></a><a name="p183720165419"></a>芯片内部数字电源，外接1μF滤波电容</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.7.1.4 "><p id="p13225163713188"><a name="p13225163713188"></a><a name="p13225163713188"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12.64%" headers="mcps1.2.7.1.5 "><p id="p0225163719180"><a name="p0225163719180"></a><a name="p0225163719180"></a>1.0</p>
</td>
<td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.7.1.6 "><p id="p1722510374181"><a name="p1722510374181"></a><a name="p1722510374181"></a>-</p>
</td>
</tr>
</tbody>
</table>

**表 2**  内部DC-DC产生的1P3电源外围器件要求

<a name="table6682139122219"></a>
<table><thead align="left"><tr id="row17758113912223"><th class="cellrowborder" valign="top" width="41.349999999999994%" id="mcps1.2.3.1.1"><p id="p1875873992214"><a name="p1875873992214"></a><a name="p1875873992214"></a>器件名称</p>
</th>
<th class="cellrowborder" valign="top" width="58.650000000000006%" id="mcps1.2.3.1.2"><p id="p575912399227"><a name="p575912399227"></a><a name="p575912399227"></a>大小</p>
</th>
</tr>
</thead>
<tbody><tr id="row18759193992214"><td class="cellrowborder" valign="top" width="41.349999999999994%" headers="mcps1.2.3.1.1 "><p id="p1075973915227"><a name="p1075973915227"></a><a name="p1075973915227"></a>电感</p>
</td>
<td class="cellrowborder" valign="top" width="58.650000000000006%" headers="mcps1.2.3.1.2 "><p id="p10759133912227"><a name="p10759133912227"></a><a name="p10759133912227"></a>2.2μH</p>
</td>
</tr>
<tr id="row10759143932219"><td class="cellrowborder" valign="top" width="41.349999999999994%" headers="mcps1.2.3.1.1 "><p id="p6759173910222"><a name="p6759173910222"></a><a name="p6759173910222"></a>电容</p>
</td>
<td class="cellrowborder" valign="top" width="58.650000000000006%" headers="mcps1.2.3.1.2 "><p id="p14759183942214"><a name="p14759183942214"></a><a name="p14759183942214"></a>10μF</p>
</td>
</tr>
</tbody>
</table>

### VBAT电源<a name="ZH-CN_TOPIC_0000001505603553"></a>

WS53V100包含2个VBAT电源输入管脚：

-   VDD\_VBAT1：BUCK的输入电源。
-   VDD\_VBAT2：INTLDO和XLDO输入电源。

VBAT支持3～3.6 V输入，VBAT电源可以由外部PMU芯片或者外部BUCK电路生成提供。

-   **[VBAT参考电路](#ZH-CN_TOPIC_0000001505722801)**  

-   **[VBAT输入电源要求](#ZH-CN_TOPIC_0000001455763052)**  

#### VBAT参考电路<a name="ZH-CN_TOPIC_0000001505722801"></a>

VBAT给芯片提供工作电源，VDD\_VBAT1和VDD\_VBAT2每个输入管脚各放一个电容用于储能滤波。参考电路图如[图1 WS53V100 VBAT输入电路](#toc528421851)所示。

<a name="table50845041"></a>
<table><thead align="left"><tr id="row62429864"><th class="cellrowborder" valign="top" width="7.5200000000000005%" id="mcps1.1.4.1.1"><p id="p1466142719111"><a name="p1466142719111"></a><a name="p1466142719111"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.1.4.1.2"><p id="p23654198"><a name="p23654198"></a><a name="p23654198"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="72.28%" id="mcps1.1.4.1.3"><p id="p17214411"><a name="p17214411"></a><a name="p17214411"></a>设计建议</p>
</th>
</tr>
</thead>
<tbody><tr id="row52190020"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.1.4.1.1 "><p id="p106613275112"><a name="p106613275112"></a><a name="p106613275112"></a>39</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.1.4.1.2 "><p id="p810452985618"><a name="p810452985618"></a><a name="p810452985618"></a>VDD_VBAT1</p>
</td>
<td class="cellrowborder" valign="top" width="72.28%" headers="mcps1.1.4.1.3 "><p id="p48481036"><a name="p48481036"></a><a name="p48481036"></a>外接4.7μF电容，耐压值≥6.3V。</p>
</td>
</tr>
<tr id="row64182307"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.1.4.1.1 "><p id="p5661127111118"><a name="p5661127111118"></a><a name="p5661127111118"></a>9</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.1.4.1.2 "><p id="p31384387"><a name="p31384387"></a><a name="p31384387"></a>VDD_VBAT2</p>
</td>
<td class="cellrowborder" valign="top" width="72.28%" headers="mcps1.1.4.1.3 "><p id="p1456104412563"><a name="p1456104412563"></a><a name="p1456104412563"></a>外接1μF电容，耐压值≥6.3V。</p>
</td>
</tr>
<tr id="row52661449185512"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.1.4.1.1 "><p id="p84811563554"><a name="p84811563554"></a><a name="p84811563554"></a>38</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.1.4.1.2 "><p id="p5481256115520"><a name="p5481256115520"></a><a name="p5481256115520"></a>AVDD33</p>
</td>
<td class="cellrowborder" valign="top" width="72.28%" headers="mcps1.1.4.1.3 "><p id="p927916517567"><a name="p927916517567"></a><a name="p927916517567"></a>外接1μF电容，耐压值≥6.3V，布局空间受限可以考虑和VDD_VBAT1共用4.7uF滤波电容。</p>
</td>
</tr>
</tbody>
</table>

**图 1**  WS53V100 VBAT输入电路<a name="toc528421851"></a>  

![](figures/zh-cn_image_0000001762963404.png)

#### VBAT输入电源要求<a name="ZH-CN_TOPIC_0000001455763052"></a>

WS53V100的VBAT输入电源要求如下：

-   要求电源噪声峰峰值在±3%以内。
-   选择合适的电感和输出滤波电容，能够更有效抑制纹波和谐波干扰。

### VDDIO电源<a name="ZH-CN_TOPIC_0000001455763056"></a>

WS53V100有1个VDDIO电源输入管脚：

-   VDDIO

支持1.8V/3.3V电压，推荐设计建议如[表1](#table50845041)所示，参考电路图如[图1](#fig118162314710)所示。

**表 1**  VDDIO电源设计建议

<a name="table50845041"></a>
<table><thead align="left"><tr id="row62429864"><th class="cellrowborder" valign="top" width="7.5200000000000005%" id="mcps1.2.4.1.1"><p id="p76001646201118"><a name="p76001646201118"></a><a name="p76001646201118"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.2.4.1.2"><p id="p23654198"><a name="p23654198"></a><a name="p23654198"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="72.28%" id="mcps1.2.4.1.3"><p id="p17214411"><a name="p17214411"></a><a name="p17214411"></a>设计建议</p>
</th>
</tr>
</thead>
<tbody><tr id="row52190020"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p1360011466115"><a name="p1360011466115"></a><a name="p1360011466115"></a>37</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.2 "><p id="p66642053"><a name="p66642053"></a><a name="p66642053"></a>VDDIO</p>
</td>
<td class="cellrowborder" valign="top" width="72.28%" headers="mcps1.2.4.1.3 "><p id="p48481036"><a name="p48481036"></a><a name="p48481036"></a>外接1μF电容，耐压值≥6.3V。</p>
</td>
</tr>
</tbody>
</table>

**图 1**  VDDIO输入电路<a name="fig118162314710"></a>  
![](figures/VDDIO输入电路.png "VDDIO输入电路")

### 内部电源滤波电路<a name="ZH-CN_TOPIC_0000001505603525"></a>

内部电源中的VDD\_CLDO、VDD\_RFLDO2需要外接滤波电容，推荐设计建议如[表1](#table1033313212284)所示，参考电路图如[图1](#toc528421854)所示。

**表 1**  内部电源滤波电路设计建议

<a name="table1033313212284"></a>
<table><thead align="left"><tr id="row333420214287"><th class="cellrowborder" valign="top" width="7.5200000000000005%" id="mcps1.2.4.1.1"><p id="p5968453191613"><a name="p5968453191613"></a><a name="p5968453191613"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.2.4.1.2"><p id="p10806148102816"><a name="p10806148102816"></a><a name="p10806148102816"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.2.4.1.3"><p id="p1680613822812"><a name="p1680613822812"></a><a name="p1680613822812"></a>设计建议</p>
</th>
</tr>
</thead>
<tbody><tr id="row3845610121710"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p20211901711"><a name="p20211901711"></a><a name="p20211901711"></a>6</p>
</td>
<td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.2 "><p id="p17211901715"><a name="p17211901715"></a><a name="p17211901715"></a>XLDO_OUT</p>
</td>
<td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p98451910191710"><a name="p98451910191710"></a><a name="p98451910191710"></a>芯片XLDO decap管脚，需外接1μF滤波电容。</p>
</td>
</tr>
<tr id="row13748121331711"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p1951152310170"><a name="p1951152310170"></a><a name="p1951152310170"></a>12</p>
</td>
<td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.2 "><p id="p35111123131713"><a name="p35111123131713"></a><a name="p35111123131713"></a>VDD_RFLDO2</p>
</td>
<td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p13748413181714"><a name="p13748413181714"></a><a name="p13748413181714"></a>芯片RFLDO2 decap管脚，需外接1μF滤波电容。</p>
</td>
</tr>
<tr id="row123375216287"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p1531242714179"><a name="p1531242714179"></a><a name="p1531242714179"></a>42</p>
</td>
<td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.2 "><p id="p1131222719174"><a name="p1131222719174"></a><a name="p1131222719174"></a>VDD_CLDO</p>
</td>
<td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p18808389285"><a name="p18808389285"></a><a name="p18808389285"></a>芯片数字电源decap管脚，需外接1μF滤波电容。</p>
</td>
</tr>
</tbody>
</table>

**图 1**  内部电源滤波电路<a name="toc528421854"></a>  

![](figures/zh-cn_image_0000001762964660.png)

### RFLDO1<a name="ZH-CN_TOPIC_0000001505882541"></a>

RFLDO1电源由WS53V100 管脚VDD\_RFLDO1输出，输出滤波电容1μF。RFLDO1给2个管脚供电，分别是VDD\_RF\_RX\_1P1 和VDD\_WL\_RF\_TRX\_1P1，推荐设计建议如[表1](#table10224544)所示，参考电路见[图1](#fig8285114720720)所示。

**表 1**  RFLDO1电源设计建议

<a name="table10224544"></a>
<table><thead align="left"><tr id="row43104852"><th class="cellrowborder" valign="top" width="7.5200000000000005%" id="mcps1.2.4.1.1"><p id="p8352153514406"><a name="p8352153514406"></a><a name="p8352153514406"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="34.42%" id="mcps1.2.4.1.2"><p id="p1832125"><a name="p1832125"></a><a name="p1832125"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="58.06%" id="mcps1.2.4.1.3"><p id="p5418456"><a name="p5418456"></a><a name="p5418456"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row49904360"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p1352203513402"><a name="p1352203513402"></a><a name="p1352203513402"></a>11</p>
</td>
<td class="cellrowborder" valign="top" width="34.42%" headers="mcps1.2.4.1.2 "><p id="p15721389"><a name="p15721389"></a><a name="p15721389"></a>VDD_RFLDO1</p>
</td>
<td class="cellrowborder" valign="top" width="58.06%" headers="mcps1.2.4.1.3 "><p id="p40322854"><a name="p40322854"></a><a name="p40322854"></a>RFLDO1输出，外接1μF滤波电容。</p>
</td>
</tr>
<tr id="row1678420"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p66625568404"><a name="p66625568404"></a><a name="p66625568404"></a>13</p>
</td>
<td class="cellrowborder" valign="top" width="34.42%" headers="mcps1.2.4.1.2 "><p id="p0662656144013"><a name="p0662656144013"></a><a name="p0662656144013"></a>VDD_WL_RF_TRX_1P1</p>
</td>
<td class="cellrowborder" valign="top" width="58.06%" headers="mcps1.2.4.1.3 "><p id="p49157836"><a name="p49157836"></a><a name="p49157836"></a>芯片内部TRX相关模块输入电源，外接1μF滤波电容。</p>
</td>
</tr>
<tr id="row67038639"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p1927015015410"><a name="p1927015015410"></a><a name="p1927015015410"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="34.42%" headers="mcps1.2.4.1.2 "><p id="p142705014119"><a name="p142705014119"></a><a name="p142705014119"></a>VDD_RF_RX_1P1</p>
</td>
<td class="cellrowborder" valign="top" width="58.06%" headers="mcps1.2.4.1.3 "><p id="p956144618442"><a name="p956144618442"></a><a name="p956144618442"></a>芯片LNA输入电源，外接1μF滤波电容。</p>
</td>
</tr>
</tbody>
</table>

**图 1**  RFLDO1参考电路<a name="fig8285114720720"></a>  

![](figures/zh-cn_image_0000001762966700.png)

### BUCK/LDO电源<a name="ZH-CN_TOPIC_0000001505882569"></a>

WS53V100包含4个1P3电源输入管脚：

-   VDD\_1P3
-   VDD\_BSLE\_RF\_PA\_1P3
-   VDD\_BSLE\_RF\_DRV\_1P3
-   VDD\_BSLE\_PLL\_DCO\_1P3

该1P3电源可以由芯片内部BUCK（BUCK\_LX）提供

**表 1**  BUCK电源设计建议

<a name="table31324986"></a>
<table><thead align="left"><tr id="row6586990"><th class="cellrowborder" valign="top" width="7.5200000000000005%" id="mcps1.2.4.1.1"><p id="p135311034205014"><a name="p135311034205014"></a><a name="p135311034205014"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="32.89%" id="mcps1.2.4.1.2"><p id="p63784147"><a name="p63784147"></a><a name="p63784147"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="59.589999999999996%" id="mcps1.2.4.1.3"><p id="p19703316"><a name="p19703316"></a><a name="p19703316"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row52689776"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p9531203495013"><a name="p9531203495013"></a><a name="p9531203495013"></a>40</p>
</td>
<td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.4.1.2 "><p id="p40013493"><a name="p40013493"></a><a name="p40013493"></a>BUCK_LX</p>
</td>
<td class="cellrowborder" valign="top" width="59.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p44592174"><a name="p44592174"></a><a name="p44592174"></a>BUCK LX输出，外接2.2μH电感，10uF电容</p>
</td>
</tr>
<tr id="row137672065117"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p8162172445112"><a name="p8162172445112"></a><a name="p8162172445112"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.4.1.2 "><p id="p16162152420516"><a name="p16162152420516"></a><a name="p16162152420516"></a>VDD_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="59.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p1816219249513"><a name="p1816219249513"></a><a name="p1816219249513"></a>RFLDO1，RFLDO2输入电源</p>
</td>
</tr>
<tr id="row1160116371317"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p065231611513"><a name="p065231611513"></a><a name="p065231611513"></a>17</p>
</td>
<td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.4.1.2 "><p id="p26524164512"><a name="p26524164512"></a><a name="p26524164512"></a>VDD_BSLE_RF_PA_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="59.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p1265291612513"><a name="p1265291612513"></a><a name="p1265291612513"></a>BSLE LDO输入电源，外接1μF滤波电容</p>
</td>
</tr>
<tr id="row132331258145018"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p665221613514"><a name="p665221613514"></a><a name="p665221613514"></a>19</p>
</td>
<td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.4.1.2 "><p id="p16522016125120"><a name="p16522016125120"></a><a name="p16522016125120"></a>VDD_BSLE_RF_DRV_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="59.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p165221655119"><a name="p165221655119"></a><a name="p165221655119"></a>BSLE LDO输入电源，外接1μF滤波电容（可以和Pin17管脚共用1μF电容）</p>
</td>
</tr>
<tr id="row27004956"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p1065261619512"><a name="p1065261619512"></a><a name="p1065261619512"></a>20</p>
</td>
<td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.4.1.2 "><p id="p18652181615118"><a name="p18652181615118"></a><a name="p18652181615118"></a>VDD_BSLE_PLL_DCO_1P3</p>
</td>
<td class="cellrowborder" valign="top" width="59.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p56523161510"><a name="p56523161510"></a><a name="p56523161510"></a>BSLE LDO输入电源，外接1μF滤波电容</p>
</td>
</tr>
<tr id="row99501048122511"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p995116494294"><a name="p995116494294"></a><a name="p995116494294"></a>18</p>
</td>
<td class="cellrowborder" valign="top" width="32.89%" headers="mcps1.2.4.1.2 "><p id="p1951849182917"><a name="p1951849182917"></a><a name="p1951849182917"></a>VDD_BSLE_DPALDO</p>
</td>
<td class="cellrowborder" valign="top" width="59.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p69502487253"><a name="p69502487253"></a><a name="p69502487253"></a>芯片内部BSLE电源decap管脚，接板级滤波电容</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **说明：** 
>BUCK电感推荐约束条件：
>-   电感值2.2μH，±20%。
>-   直流电阻（Rdc）≤0.3Ω。
>-   饱和电流≥800mA。
>-   Rdc增大会导致功耗增加，效率变低。
>-   Rdc从0.1Ω增加到0.2Ω，重载效率会降低1\~2个百分点。

内部BUCK由VDD\_VBAT1提供输入电压，由BUCK\_LX输出开关信号，因此需要外接电感和输出电容。

参考电路图如[图1](#fig11667124685)所示。

**图 1**  内置BUCK参考电路<a name="fig11667124685"></a>  
![](figures/内置BUCK参考电路.png "内置BUCK参考电路")

### PA供电<a name="ZH-CN_TOPIC_0000001505603537"></a>

外部提供给VDD\_WL\_RF\_PA\_3P3供电，可与VBAT电源接在一起，设计建议如[表1](#table556428)所示，参考电路图如[图1](#fig13232739986)所示。

**表 1**  PA供电设计建议

<a name="table556428"></a>
<table><thead align="left"><tr id="row9244222"><th class="cellrowborder" valign="top" width="7.5200000000000005%" id="mcps1.2.4.1.1"><p id="p16600151242116"><a name="p16600151242116"></a><a name="p16600151242116"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="20.03%" id="mcps1.2.4.1.2"><p id="p10584494"><a name="p10584494"></a><a name="p10584494"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="72.45%" id="mcps1.2.4.1.3"><p id="p21821544"><a name="p21821544"></a><a name="p21821544"></a>设计建议</p>
</th>
</tr>
</thead>
<tbody><tr id="row59416926"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p15357142162113"><a name="p15357142162113"></a><a name="p15357142162113"></a>14</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p535782114218"><a name="p535782114218"></a><a name="p535782114218"></a>VDD_WL_RF_PA_3P3</p>
</td>
<td class="cellrowborder" valign="top" width="72.45%" headers="mcps1.2.4.1.3 "><p id="p1717614044010"><a name="p1717614044010"></a><a name="p1717614044010"></a>WLAN PA供电电源，由外部电源提供，VBAT供电，外接1μF、100nF（预留）（靠近芯片从小到大排列）。</p>
</td>
</tr>
</tbody>
</table>

**图 1**  PA供电电路设计参考<a name="fig13232739986"></a>  
![](figures/PA供电电路设计参考.png "PA供电电路设计参考")

### 注意事项<a name="ZH-CN_TOPIC_0000001456082736"></a>

-   **[RST\_N电路](#ZH-CN_TOPIC_0000001456082712)**  

#### RST\_N电路<a name="ZH-CN_TOPIC_0000001456082712"></a>

RST\_N为上电使能管脚，该管脚上拉到VDDIO电源。

**图 1**  RST\_N参考电路<a name="fig2019417147576"></a>  
![](figures/RST_N参考电路.png "RST_N参考电路")

## 外围接口设计建议<a name="ZH-CN_TOPIC_0000001505603517"></a>

-   **[SDIO接口参考设计](#ZH-CN_TOPIC_0000001455763072)**  

-   **[UART接口参考设计](#ZH-CN_TOPIC_0000001456242652)**  

-   **[PWM接口参考设计](#ZH-CN_TOPIC_0000001505722789)**  

-   **[I2S接口参考设计](#ZH-CN_TOPIC_0000001505882553)**  

-   **[SPI接口参考设计](#ZH-CN_TOPIC_0000001505722793)**  

-   **[I2C接口参考设计](#ZH-CN_TOPIC_0000001455922812)**  

-   **[ADC接口参考设计](#ZH-CN_TOPIC_0000001455922820)**  

-   **[PTA接口设计](#ZH-CN_TOPIC_0000001456082708)**  

-   **[天线选择接口](#ZH-CN_TOPIC_0000001734928077)**  

-   **[超低功耗接口设计](#ZH-CN_TOPIC_0000001505603533)**  

### SDIO接口参考设计<a name="ZH-CN_TOPIC_0000001455763072"></a>

WS53V100通过SDIO与Host通信。SDIO电平支持1.8V和3.3V，要求Host端也必须是1.8V或3.3V电平；否则两者之间需要增加电平转换器件，选用的电平转换芯片需要符合SDIO速率（50MHz）的传输要求。设计建议如[表1](#table13407557192520)所示。

**表 1**  SDIO接口设计建议

<a name="table13407557192520"></a>
<table><thead align="left"><tr id="row64081557142515"><th class="cellrowborder" valign="top" width="7.519248075192481%" id="mcps1.2.6.1.1"><p id="p8969461393"><a name="p8969461393"></a><a name="p8969461393"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="15.218478152184781%" id="mcps1.2.6.1.2"><p id="p1285713852611"><a name="p1285713852611"></a><a name="p1285713852611"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="16.90830916908309%" id="mcps1.2.6.1.3"><p id="p8857148132611"><a name="p8857148132611"></a><a name="p8857148132611"></a>上下拉</p>
</th>
<th class="cellrowborder" valign="top" width="16.20837916208379%" id="mcps1.2.6.1.4"><p id="p285738112618"><a name="p285738112618"></a><a name="p285738112618"></a>VDDIO</p>
</th>
<th class="cellrowborder" valign="top" width="44.14558544145585%" id="mcps1.2.6.1.5"><p id="p2857084261"><a name="p2857084261"></a><a name="p2857084261"></a>连接方式</p>
</th>
</tr>
</thead>
<tbody><tr id="row1841419576251"><td class="cellrowborder" valign="top" width="7.519248075192481%" headers="mcps1.2.6.1.1 "><p id="p8969176203918"><a name="p8969176203918"></a><a name="p8969176203918"></a>34</p>
</td>
<td class="cellrowborder" valign="top" width="15.218478152184781%" headers="mcps1.2.6.1.2 "><p id="p66542544012"><a name="p66542544012"></a><a name="p66542544012"></a>SDIO_CLK</p>
</td>
<td class="cellrowborder" valign="top" width="16.90830916908309%" headers="mcps1.2.6.1.3 "><p id="p13858128192618"><a name="p13858128192618"></a><a name="p13858128192618"></a>NA</p>
</td>
<td class="cellrowborder" valign="top" width="16.20837916208379%" headers="mcps1.2.6.1.4 "><p id="p485819816264"><a name="p485819816264"></a><a name="p485819816264"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.14558544145585%" headers="mcps1.2.6.1.5 "><p id="p7858683260"><a name="p7858683260"></a><a name="p7858683260"></a>源端串33Ω电阻，走线≤5inch。芯片端预留一个10pF电容。</p>
</td>
</tr>
<tr id="row1941595782510"><td class="cellrowborder" valign="top" width="7.519248075192481%" headers="mcps1.2.6.1.1 "><p id="p89691169398"><a name="p89691169398"></a><a name="p89691169398"></a>33</p>
</td>
<td class="cellrowborder" valign="top" width="15.218478152184781%" headers="mcps1.2.6.1.2 "><p id="p173431214124018"><a name="p173431214124018"></a><a name="p173431214124018"></a>SDIO_CMD</p>
</td>
<td class="cellrowborder" valign="top" width="16.90830916908309%" headers="mcps1.2.6.1.3 "><p id="p9858108112614"><a name="p9858108112614"></a><a name="p9858108112614"></a>NA</p>
</td>
<td class="cellrowborder" valign="top" width="16.20837916208379%" headers="mcps1.2.6.1.4 "><p id="p1985917818264"><a name="p1985917818264"></a><a name="p1985917818264"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.14558544145585%" headers="mcps1.2.6.1.5 "><p id="p08591386268"><a name="p08591386268"></a><a name="p08591386268"></a>VDDIO=3.3V：终端串33/0Ω电阻，走线≤5inch；</p>
<p id="p985978172610"><a name="p985978172610"></a><a name="p985978172610"></a>VDDIO=1.8V：终端串33/0Ω电阻，走线≤3.5inch。</p>
</td>
</tr>
<tr id="row18415357172511"><td class="cellrowborder" valign="top" width="7.519248075192481%" headers="mcps1.2.6.1.1 "><p id="p896913633913"><a name="p896913633913"></a><a name="p896913633913"></a>35</p>
<p id="p14779135534013"><a name="p14779135534013"></a><a name="p14779135534013"></a>36</p>
<p id="p1466515018414"><a name="p1466515018414"></a><a name="p1466515018414"></a>31</p>
<p id="p1457511415419"><a name="p1457511415419"></a><a name="p1457511415419"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="15.218478152184781%" headers="mcps1.2.6.1.2 "><p id="p1585911819265"><a name="p1585911819265"></a><a name="p1585911819265"></a>SDIO_D0</p>
<p id="p1785988172614"><a name="p1785988172614"></a><a name="p1785988172614"></a>SDIO_D1</p>
<p id="p5483138134011"><a name="p5483138134011"></a><a name="p5483138134011"></a>SDIO_D2</p>
<p id="p188591387263"><a name="p188591387263"></a><a name="p188591387263"></a>SDIO_D3</p>
</td>
<td class="cellrowborder" valign="top" width="16.90830916908309%" headers="mcps1.2.6.1.3 "><p id="p2861178132610"><a name="p2861178132610"></a><a name="p2861178132610"></a>芯片内置25kΩ上拉，建议单板预留一个上拉电阻位用于调试、建议47kΩ。</p>
</td>
<td class="cellrowborder" valign="top" width="16.20837916208379%" headers="mcps1.2.6.1.4 "><p id="p286118818265"><a name="p286118818265"></a><a name="p286118818265"></a>3.3/1.8</p>
</td>
<td class="cellrowborder" valign="top" width="44.14558544145585%" headers="mcps1.2.6.1.5 "><p id="p1561734611514"><a name="p1561734611514"></a><a name="p1561734611514"></a>VDDIO=3.3V：终端串33/0Ω电阻，走线≤5inch；</p>
<p id="p136178461150"><a name="p136178461150"></a><a name="p136178461150"></a>VDDIO=1.8V：终端串33/0Ω电阻，走线≤3.5inch。</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-notice.gif) **须知：** 
>在使用SDIO一线模式时，SDIO\_D2和SDIO\_D3需要保持悬空状态，不能复用为其它功能。

### UART接口参考设计<a name="ZH-CN_TOPIC_0000001456242652"></a>

WS53V100支持三组UART信号，UART\_L0用于WS53V100维测打印。UART\_H0和UART\_H1用于与其他设备对接，管脚电平与VDDIO保持一致。设计建议如[表1](#table50417177)所示。

**表 1**  UART接口设计建议

<a name="table50417177"></a>
<table><thead align="left"><tr id="row54249298"><th class="cellrowborder" valign="top" width="14.93%" id="mcps1.2.4.1.1"><p id="p1024018499313"><a name="p1024018499313"></a><a name="p1024018499313"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="38.35%" id="mcps1.2.4.1.2"><p id="p32117021"><a name="p32117021"></a><a name="p32117021"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="46.72%" id="mcps1.2.4.1.3"><p id="p63270821"><a name="p63270821"></a><a name="p63270821"></a>设计建议</p>
</th>
</tr>
</thead>
<tbody><tr id="row24662915"><td class="cellrowborder" valign="top" width="14.93%" headers="mcps1.2.4.1.1 "><p id="p22405497317"><a name="p22405497317"></a><a name="p22405497317"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.4.1.2 "><p id="p8406510193015"><a name="p8406510193015"></a><a name="p8406510193015"></a>UART_L0_TXD</p>
</td>
<td class="cellrowborder" valign="top" width="46.72%" headers="mcps1.2.4.1.3 "><p id="p21925900"><a name="p21925900"></a><a name="p21925900"></a>直连，走线≤5inch</p>
</td>
</tr>
<tr id="row63115372"><td class="cellrowborder" valign="top" width="14.93%" headers="mcps1.2.4.1.1 "><p id="p1424011497318"><a name="p1424011497318"></a><a name="p1424011497318"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.4.1.2 "><p id="p124062010133014"><a name="p124062010133014"></a><a name="p124062010133014"></a>UART_L0_RXD</p>
</td>
<td class="cellrowborder" valign="top" width="46.72%" headers="mcps1.2.4.1.3 "><p id="p53000234"><a name="p53000234"></a><a name="p53000234"></a>直连，走线≤5inch</p>
</td>
</tr>
<tr id="row12200154931317"><td class="cellrowborder" valign="top" width="14.93%" headers="mcps1.2.4.1.1 "><p id="p224024913312"><a name="p224024913312"></a><a name="p224024913312"></a>4/24</p>
</td>
<td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.4.1.2 "><p id="p195461851203010"><a name="p195461851203010"></a><a name="p195461851203010"></a>UART_H1_RXD</p>
</td>
<td class="cellrowborder" valign="top" width="46.72%" headers="mcps1.2.4.1.3 "><p id="p9200849141311"><a name="p9200849141311"></a><a name="p9200849141311"></a>直连，走线≤5inch</p>
</td>
</tr>
<tr id="row83661434237"><td class="cellrowborder" valign="top" width="14.93%" headers="mcps1.2.4.1.1 "><p id="p3241114953114"><a name="p3241114953114"></a><a name="p3241114953114"></a>5/23</p>
</td>
<td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.4.1.2 "><p id="p15546651153011"><a name="p15546651153011"></a><a name="p15546651153011"></a>UART_H1_TXD</p>
</td>
<td class="cellrowborder" valign="top" width="46.72%" headers="mcps1.2.4.1.3 "><p id="p736814342320"><a name="p736814342320"></a><a name="p736814342320"></a>直连，走线≤5inch</p>
</td>
</tr>
<tr id="row85391720181315"><td class="cellrowborder" valign="top" width="14.93%" headers="mcps1.2.4.1.1 "><p id="p72411849143110"><a name="p72411849143110"></a><a name="p72411849143110"></a>21/43</p>
</td>
<td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.4.1.2 "><p id="p4546551133017"><a name="p4546551133017"></a><a name="p4546551133017"></a>UART_H1_CTS</p>
</td>
<td class="cellrowborder" valign="top" width="46.72%" headers="mcps1.2.4.1.3 "><p id="p19540220141316"><a name="p19540220141316"></a><a name="p19540220141316"></a>直连，走线≤5inch</p>
</td>
</tr>
<tr id="row1245314265308"><td class="cellrowborder" valign="top" width="14.93%" headers="mcps1.2.4.1.1 "><p id="p13241144913113"><a name="p13241144913113"></a><a name="p13241144913113"></a>22/30</p>
</td>
<td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.4.1.2 "><p id="p2054618516302"><a name="p2054618516302"></a><a name="p2054618516302"></a>UART_H1_RTS</p>
</td>
<td class="cellrowborder" valign="top" width="46.72%" headers="mcps1.2.4.1.3 "><p id="p172451920312"><a name="p172451920312"></a><a name="p172451920312"></a>直连，走线≤5inch</p>
</td>
</tr>
<tr id="row16549833133014"><td class="cellrowborder" valign="top" width="14.93%" headers="mcps1.2.4.1.1 "><p id="p162411249133110"><a name="p162411249133110"></a><a name="p162411249133110"></a>25/52</p>
</td>
<td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.4.1.2 "><p id="p2113165843018"><a name="p2113165843018"></a><a name="p2113165843018"></a>UART_H0_CTS</p>
</td>
<td class="cellrowborder" valign="top" width="46.72%" headers="mcps1.2.4.1.3 "><p id="p10650129173114"><a name="p10650129173114"></a><a name="p10650129173114"></a>直连，走线≤5inch</p>
</td>
</tr>
<tr id="row16499182911301"><td class="cellrowborder" valign="top" width="14.93%" headers="mcps1.2.4.1.1 "><p id="p182419494319"><a name="p182419494319"></a><a name="p182419494319"></a>26/48</p>
</td>
<td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.4.1.2 "><p id="p191136585309"><a name="p191136585309"></a><a name="p191136585309"></a>UART_H0_TXD</p>
</td>
<td class="cellrowborder" valign="top" width="46.72%" headers="mcps1.2.4.1.3 "><p id="p16561810133118"><a name="p16561810133118"></a><a name="p16561810133118"></a>直连，走线≤5inch</p>
</td>
</tr>
<tr id="row174814277246"><td class="cellrowborder" valign="top" width="14.93%" headers="mcps1.2.4.1.1 "><p id="p1424194918318"><a name="p1424194918318"></a><a name="p1424194918318"></a>27/49</p>
</td>
<td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.4.1.2 "><p id="p1111385863011"><a name="p1111385863011"></a><a name="p1111385863011"></a>UART_H0_RXD</p>
</td>
<td class="cellrowborder" valign="top" width="46.72%" headers="mcps1.2.4.1.3 "><p id="p144992712249"><a name="p144992712249"></a><a name="p144992712249"></a>直连，走线≤5inch</p>
</td>
</tr>
<tr id="row99530197316"><td class="cellrowborder" valign="top" width="14.93%" headers="mcps1.2.4.1.1 "><p id="p152411049123113"><a name="p152411049123113"></a><a name="p152411049123113"></a>28/46</p>
</td>
<td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.4.1.2 "><p id="p99161834193114"><a name="p99161834193114"></a><a name="p99161834193114"></a>UART_H0_RTS</p>
</td>
<td class="cellrowborder" valign="top" width="46.72%" headers="mcps1.2.4.1.3 "><p id="p19998163913115"><a name="p19998163913115"></a><a name="p19998163913115"></a>直连，走线≤5inch</p>
</td>
</tr>
</tbody>
</table>

### PWM接口参考设计<a name="ZH-CN_TOPIC_0000001505722789"></a>

WS53V100支持8个PWM接口信号输出，PWM0-PWM3为3组互补PWM接口，SPWM 为2个为安全PWM接口，输出电平与VDDIO电平保持一致，占空比输出范围（0-100%），最高可达到30khz以上，步进100Hz。

设计建议如[表1](#table6991874)所示。

**表 1**  PWM接口设计建议

<a name="table6991874"></a>
<table><thead align="left"><tr id="row37854045"><th class="cellrowborder" valign="top" width="7.5200000000000005%" id="mcps1.2.4.1.1"><p id="p156392539352"><a name="p156392539352"></a><a name="p156392539352"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="47.21%" id="mcps1.2.4.1.2"><p id="p46278819"><a name="p46278819"></a><a name="p46278819"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="45.269999999999996%" id="mcps1.2.4.1.3"><p id="p46972752"><a name="p46972752"></a><a name="p46972752"></a>设计建议</p>
</th>
</tr>
</thead>
<tbody><tr id="row46696577"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p1248081514215"><a name="p1248081514215"></a><a name="p1248081514215"></a>21/2</p>
</td>
<td class="cellrowborder" valign="top" width="47.21%" headers="mcps1.2.4.1.2 "><p id="p1799021714185"><a name="p1799021714185"></a><a name="p1799021714185"></a>PWM0_P</p>
</td>
<td class="cellrowborder" valign="top" width="45.269999999999996%" headers="mcps1.2.4.1.3 "><p id="p13940726153915"><a name="p13940726153915"></a><a name="p13940726153915"></a>直连，走线≤5inch</p>
</td>
</tr>
<tr id="row10306693"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p1248017156211"><a name="p1248017156211"></a><a name="p1248017156211"></a>22/3</p>
</td>
<td class="cellrowborder" valign="top" width="47.21%" headers="mcps1.2.4.1.2 "><p id="p1023311910161"><a name="p1023311910161"></a><a name="p1023311910161"></a>PWM0_N</p>
</td>
<td class="cellrowborder" valign="top" width="45.269999999999996%" headers="mcps1.2.4.1.3 "><p id="p10940162663917"><a name="p10940162663917"></a><a name="p10940162663917"></a>直连，走线≤5inch</p>
</td>
</tr>
<tr id="row144483412593"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p1044473445914"><a name="p1044473445914"></a><a name="p1044473445914"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="47.21%" headers="mcps1.2.4.1.2 "><p id="p05951430595"><a name="p05951430595"></a><a name="p05951430595"></a>PWM2_P</p>
</td>
<td class="cellrowborder" valign="top" width="45.269999999999996%" headers="mcps1.2.4.1.3 "><p id="p1759524314595"><a name="p1759524314595"></a><a name="p1759524314595"></a>直连，走线≤5inch</p>
</td>
</tr>
<tr id="row18556931185917"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p655617313595"><a name="p655617313595"></a><a name="p655617313595"></a>51</p>
</td>
<td class="cellrowborder" valign="top" width="47.21%" headers="mcps1.2.4.1.2 "><p id="p14595343115910"><a name="p14595343115910"></a><a name="p14595343115910"></a>PWM2_N</p>
</td>
<td class="cellrowborder" valign="top" width="45.269999999999996%" headers="mcps1.2.4.1.3 "><p id="p8595843125916"><a name="p8595843125916"></a><a name="p8595843125916"></a>直连，走线≤5inch</p>
</td>
</tr>
<tr id="row25625616"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p463919534359"><a name="p463919534359"></a><a name="p463919534359"></a>43</p>
</td>
<td class="cellrowborder" valign="top" width="47.21%" headers="mcps1.2.4.1.2 "><p id="p876594419599"><a name="p876594419599"></a><a name="p876594419599"></a>PWM3_P</p>
</td>
<td class="cellrowborder" valign="top" width="45.269999999999996%" headers="mcps1.2.4.1.3 "><p id="p20765144435912"><a name="p20765144435912"></a><a name="p20765144435912"></a>直连，走线≤5inch</p>
</td>
</tr>
<tr id="row1323954121615"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p116391453193513"><a name="p116391453193513"></a><a name="p116391453193513"></a>47</p>
</td>
<td class="cellrowborder" valign="top" width="47.21%" headers="mcps1.2.4.1.2 "><p id="p87651744145911"><a name="p87651744145911"></a><a name="p87651744145911"></a>PWM3_N</p>
</td>
<td class="cellrowborder" valign="top" width="45.269999999999996%" headers="mcps1.2.4.1.3 "><p id="p157659442596"><a name="p157659442596"></a><a name="p157659442596"></a>直连，走线≤5inch</p>
</td>
</tr>
<tr id="row105672238175"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p76399535356"><a name="p76399535356"></a><a name="p76399535356"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="47.21%" headers="mcps1.2.4.1.2 "><p id="p15849356155913"><a name="p15849356155913"></a><a name="p15849356155913"></a>SPWM1P</p>
</td>
<td class="cellrowborder" valign="top" width="45.269999999999996%" headers="mcps1.2.4.1.3 "><p id="p168491356125917"><a name="p168491356125917"></a><a name="p168491356125917"></a>直连，走线≤5inch</p>
</td>
</tr>
<tr id="row14438155417599"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p1438195495919"><a name="p1438195495919"></a><a name="p1438195495919"></a>25</p>
</td>
<td class="cellrowborder" valign="top" width="47.21%" headers="mcps1.2.4.1.2 "><p id="p7759154112017"><a name="p7759154112017"></a><a name="p7759154112017"></a>SPWM1N</p>
</td>
<td class="cellrowborder" valign="top" width="45.269999999999996%" headers="mcps1.2.4.1.3 "><p id="p158490560590"><a name="p158490560590"></a><a name="p158490560590"></a>直连，走线≤5inch</p>
</td>
</tr>
</tbody>
</table>

### I2S接口参考设计<a name="ZH-CN_TOPIC_0000001505882553"></a>

WS53V100支持一组I2S接口，输入输出电平应与VDDIO电平保持一致。设计建议如[表1](#table6991874)所示。

**表 1**  I2S接口设计建议

<a name="table6991874"></a>
<table><thead align="left"><tr id="row37854045"><th class="cellrowborder" valign="top" width="15.58%" id="mcps1.2.4.1.1"><p id="p641715121044"><a name="p641715121044"></a><a name="p641715121044"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="39.589999999999996%" id="mcps1.2.4.1.2"><p id="p46278819"><a name="p46278819"></a><a name="p46278819"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="44.83%" id="mcps1.2.4.1.3"><p id="p43662144"><a name="p43662144"></a><a name="p43662144"></a>设计建议</p>
</th>
</tr>
</thead>
<tbody><tr id="row46696577"><td class="cellrowborder" valign="top" width="15.58%" headers="mcps1.2.4.1.1 "><p id="p343034520512"><a name="p343034520512"></a><a name="p343034520512"></a>21/51</p>
</td>
<td class="cellrowborder" valign="top" width="39.589999999999996%" headers="mcps1.2.4.1.2 "><p id="p1799021714185"><a name="p1799021714185"></a><a name="p1799021714185"></a>I2S_WS</p>
</td>
<td class="cellrowborder" valign="top" width="44.83%" headers="mcps1.2.4.1.3 "><p id="p6327123218272"><a name="p6327123218272"></a><a name="p6327123218272"></a>直连，包地处理。</p>
</td>
</tr>
<tr id="row119544818514"><td class="cellrowborder" valign="top" width="15.58%" headers="mcps1.2.4.1.1 "><p id="p64301745852"><a name="p64301745852"></a><a name="p64301745852"></a>22/48</p>
</td>
<td class="cellrowborder" valign="top" width="39.589999999999996%" headers="mcps1.2.4.1.2 "><p id="p62408979"><a name="p62408979"></a><a name="p62408979"></a>I2S_BCLK</p>
</td>
<td class="cellrowborder" valign="top" width="44.83%" headers="mcps1.2.4.1.3 "><p id="p1178414131271"><a name="p1178414131271"></a><a name="p1178414131271"></a>芯片端串33Ω电阻，包地处理。</p>
</td>
</tr>
<tr id="row10306693"><td class="cellrowborder" valign="top" width="15.58%" headers="mcps1.2.4.1.1 "><p id="p943013456517"><a name="p943013456517"></a><a name="p943013456517"></a>23/50</p>
</td>
<td class="cellrowborder" valign="top" width="39.589999999999996%" headers="mcps1.2.4.1.2 "><p id="p29535834"><a name="p29535834"></a><a name="p29535834"></a>I2S_DI</p>
</td>
<td class="cellrowborder" valign="top" width="44.83%" headers="mcps1.2.4.1.3 "><p id="p5852191712717"><a name="p5852191712717"></a><a name="p5852191712717"></a>直连。</p>
</td>
</tr>
<tr id="row19169181358"><td class="cellrowborder" valign="top" width="15.58%" headers="mcps1.2.4.1.1 "><p id="p144308455517"><a name="p144308455517"></a><a name="p144308455517"></a>24/49</p>
</td>
<td class="cellrowborder" valign="top" width="39.589999999999996%" headers="mcps1.2.4.1.2 "><p id="p53942452"><a name="p53942452"></a><a name="p53942452"></a>I2S_D0</p>
</td>
<td class="cellrowborder" valign="top" width="44.83%" headers="mcps1.2.4.1.3 "><p id="p7939121572713"><a name="p7939121572713"></a><a name="p7939121572713"></a>直连。</p>
</td>
</tr>
</tbody>
</table>

### SPI接口参考设计<a name="ZH-CN_TOPIC_0000001505722793"></a>

WS53V100支持两组SPI接口，一组SPI接口，一组QSPI接口，输入输出电平应与VDDIO电平保持一致。设计建议如[表1](#table6991874)所示。

**表 1**  SPI接口设计建议

<a name="table6991874"></a>
<table><thead align="left"><tr id="row37854045"><th class="cellrowborder" valign="top" width="15.879999999999999%" id="mcps1.2.4.1.1"><p id="p1143153313613"><a name="p1143153313613"></a><a name="p1143153313613"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.4.1.2"><p id="p46278819"><a name="p46278819"></a><a name="p46278819"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="53.190000000000005%" id="mcps1.2.4.1.3"><p id="p43662144"><a name="p43662144"></a><a name="p43662144"></a>设计建议</p>
</th>
</tr>
</thead>
<tbody><tr id="row46696577"><td class="cellrowborder" valign="top" width="15.879999999999999%" headers="mcps1.2.4.1.1 "><p id="p1896516287114"><a name="p1896516287114"></a><a name="p1896516287114"></a>33/23/28</p>
</td>
<td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.4.1.2 "><p id="p0472133711112"><a name="p0472133711112"></a><a name="p0472133711112"></a>SPI0_DI</p>
</td>
<td class="cellrowborder" valign="top" width="53.190000000000005%" headers="mcps1.2.4.1.3 "><p id="p6327123218272"><a name="p6327123218272"></a><a name="p6327123218272"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row10306693"><td class="cellrowborder" valign="top" width="15.879999999999999%" headers="mcps1.2.4.1.1 "><p id="p5965122891118"><a name="p5965122891118"></a><a name="p5965122891118"></a>34/22/26</p>
</td>
<td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.4.1.2 "><p id="p2047243711119"><a name="p2047243711119"></a><a name="p2047243711119"></a>SPI0_CLK</p>
</td>
<td class="cellrowborder" valign="top" width="53.190000000000005%" headers="mcps1.2.4.1.3 "><p id="p4193142133513"><a name="p4193142133513"></a><a name="p4193142133513"></a>芯片端串接一个33Ω电阻，单根走线包地处理，走线≤5inch。</p>
</td>
</tr>
<tr id="row47890712"><td class="cellrowborder" valign="top" width="15.879999999999999%" headers="mcps1.2.4.1.1 "><p id="p10965132871120"><a name="p10965132871120"></a><a name="p10965132871120"></a>35/24/27</p>
</td>
<td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.4.1.2 "><p id="p1473163791115"><a name="p1473163791115"></a><a name="p1473163791115"></a>SPI0_DO</p>
</td>
<td class="cellrowborder" valign="top" width="53.190000000000005%" headers="mcps1.2.4.1.3 "><p id="p138891046141918"><a name="p138891046141918"></a><a name="p138891046141918"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row884411371117"><td class="cellrowborder" valign="top" width="15.879999999999999%" headers="mcps1.2.4.1.1 "><p id="p1596592810115"><a name="p1596592810115"></a><a name="p1596592810115"></a>36/21/52</p>
</td>
<td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.4.1.2 "><p id="p7473637101115"><a name="p7473637101115"></a><a name="p7473637101115"></a>SPI0_CS0</p>
</td>
<td class="cellrowborder" valign="top" width="53.190000000000005%" headers="mcps1.2.4.1.3 "><p id="p1132171812018"><a name="p1132171812018"></a><a name="p1132171812018"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row2844191341116"><td class="cellrowborder" valign="top" width="15.879999999999999%" headers="mcps1.2.4.1.1 "><p id="p676685311215"><a name="p676685311215"></a><a name="p676685311215"></a>47</p>
</td>
<td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.4.1.2 "><p id="p1331614576121"><a name="p1331614576121"></a><a name="p1331614576121"></a>QSPI1_D3</p>
</td>
<td class="cellrowborder" valign="top" width="53.190000000000005%" headers="mcps1.2.4.1.3 "><p id="p109181836192010"><a name="p109181836192010"></a><a name="p109181836192010"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row12844013191117"><td class="cellrowborder" valign="top" width="15.879999999999999%" headers="mcps1.2.4.1.1 "><p id="p157661653111220"><a name="p157661653111220"></a><a name="p157661653111220"></a>48</p>
</td>
<td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.4.1.2 "><p id="p12316105721217"><a name="p12316105721217"></a><a name="p12316105721217"></a>QSPI1_CLK</p>
</td>
<td class="cellrowborder" valign="top" width="53.190000000000005%" headers="mcps1.2.4.1.3 "><p id="p12369183410208"><a name="p12369183410208"></a><a name="p12369183410208"></a>芯片端串接一个33Ω电阻，单根走线包地处理，走线≤5inch。</p>
</td>
</tr>
<tr id="row2135819111110"><td class="cellrowborder" valign="top" width="15.879999999999999%" headers="mcps1.2.4.1.1 "><p id="p17766553101212"><a name="p17766553101212"></a><a name="p17766553101212"></a>49</p>
</td>
<td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.4.1.2 "><p id="p2031675717127"><a name="p2031675717127"></a><a name="p2031675717127"></a>QSPI1_D0</p>
</td>
<td class="cellrowborder" valign="top" width="53.190000000000005%" headers="mcps1.2.4.1.3 "><p id="p10333153732020"><a name="p10333153732020"></a><a name="p10333153732020"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row7135111910113"><td class="cellrowborder" valign="top" width="15.879999999999999%" headers="mcps1.2.4.1.1 "><p id="p20766105331211"><a name="p20766105331211"></a><a name="p20766105331211"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.4.1.2 "><p id="p7316457121213"><a name="p7316457121213"></a><a name="p7316457121213"></a>QSPI1_D1</p>
</td>
<td class="cellrowborder" valign="top" width="53.190000000000005%" headers="mcps1.2.4.1.3 "><p id="p571515375207"><a name="p571515375207"></a><a name="p571515375207"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row151351219101110"><td class="cellrowborder" valign="top" width="15.879999999999999%" headers="mcps1.2.4.1.1 "><p id="p5766653191216"><a name="p5766653191216"></a><a name="p5766653191216"></a>51</p>
</td>
<td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.4.1.2 "><p id="p17316145717123"><a name="p17316145717123"></a><a name="p17316145717123"></a>QSPI1_CS</p>
</td>
<td class="cellrowborder" valign="top" width="53.190000000000005%" headers="mcps1.2.4.1.3 "><p id="p920173814203"><a name="p920173814203"></a><a name="p920173814203"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row71857507125"><td class="cellrowborder" valign="top" width="15.879999999999999%" headers="mcps1.2.4.1.1 "><p id="p11766155311217"><a name="p11766155311217"></a><a name="p11766155311217"></a>52</p>
</td>
<td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.4.1.2 "><p id="p11317185714127"><a name="p11317185714127"></a><a name="p11317185714127"></a>QSPI1_D2</p>
</td>
<td class="cellrowborder" valign="top" width="53.190000000000005%" headers="mcps1.2.4.1.3 "><p id="p13773638172011"><a name="p13773638172011"></a><a name="p13773638172011"></a>直连，走线≤5inch。</p>
</td>
</tr>
</tbody>
</table>

### I2C接口参考设计<a name="ZH-CN_TOPIC_0000001455922812"></a>

WS53V100支持两组I2C接口，输入输出电平应与VDDIO电平保持一致。设计建议如[表1](#table6991874)所示。

**表 1**  I2C接口设计建议

<a name="table6991874"></a>
<table><thead align="left"><tr id="row37854045"><th class="cellrowborder" valign="top" width="7.5200000000000005%" id="mcps1.2.4.1.1"><p id="p20404101142410"><a name="p20404101142410"></a><a name="p20404101142410"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="39.67%" id="mcps1.2.4.1.2"><p id="p46278819"><a name="p46278819"></a><a name="p46278819"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="52.81%" id="mcps1.2.4.1.3"><p id="p46972752"><a name="p46972752"></a><a name="p46972752"></a>设计建议</p>
</th>
</tr>
</thead>
<tbody><tr id="row46696577"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p19404715242"><a name="p19404715242"></a><a name="p19404715242"></a>24/46</p>
</td>
<td class="cellrowborder" valign="top" width="39.67%" headers="mcps1.2.4.1.2 "><p id="p1799021714185"><a name="p1799021714185"></a><a name="p1799021714185"></a>I2C0_SCL</p>
</td>
<td class="cellrowborder" valign="top" width="52.81%" headers="mcps1.2.4.1.3 "><p id="p13940726153915"><a name="p13940726153915"></a><a name="p13940726153915"></a>直连，走线≤5inch，上拉1kΩ电阻到VDDIO。</p>
</td>
</tr>
<tr id="row10306693"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p194048112248"><a name="p194048112248"></a><a name="p194048112248"></a>25/43</p>
</td>
<td class="cellrowborder" valign="top" width="39.67%" headers="mcps1.2.4.1.2 "><p id="p29535834"><a name="p29535834"></a><a name="p29535834"></a>I2C0_SDA</p>
</td>
<td class="cellrowborder" valign="top" width="52.81%" headers="mcps1.2.4.1.3 "><p id="p10940162663917"><a name="p10940162663917"></a><a name="p10940162663917"></a>直连，走线≤5inch，上拉1kΩ电阻到VDDIO。</p>
</td>
</tr>
<tr id="row15247133217247"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p15247103216249"><a name="p15247103216249"></a><a name="p15247103216249"></a>3/26</p>
</td>
<td class="cellrowborder" valign="top" width="39.67%" headers="mcps1.2.4.1.2 "><p id="p1683440152416"><a name="p1683440152416"></a><a name="p1683440152416"></a>I2C1_SCL</p>
</td>
<td class="cellrowborder" valign="top" width="52.81%" headers="mcps1.2.4.1.3 "><p id="p1900650112519"><a name="p1900650112519"></a><a name="p1900650112519"></a>直连，走线≤5inch，上拉1kΩ电阻到VDDIO。</p>
</td>
</tr>
<tr id="row019011366241"><td class="cellrowborder" valign="top" width="7.5200000000000005%" headers="mcps1.2.4.1.1 "><p id="p19190936162411"><a name="p19190936162411"></a><a name="p19190936162411"></a>4/27</p>
</td>
<td class="cellrowborder" valign="top" width="39.67%" headers="mcps1.2.4.1.2 "><p id="p18310403245"><a name="p18310403245"></a><a name="p18310403245"></a>I2C1_SDA</p>
</td>
<td class="cellrowborder" valign="top" width="52.81%" headers="mcps1.2.4.1.3 "><p id="p1690011506251"><a name="p1690011506251"></a><a name="p1690011506251"></a>直连，走线≤5inch，上拉1kΩ电阻到VDDIO。</p>
</td>
</tr>
</tbody>
</table>

### ADC接口参考设计<a name="ZH-CN_TOPIC_0000001455922820"></a>

WS53V100支持7个ADC接口，ADC电压输入范围0Ｖ～1.715V。设计建议如[表1](#table6991874)所示。ADC输入信号可以通过UART\_L0串口读出信号电平的大小。

**表 1**  ADC接口设计建议

<a name="table6991874"></a>
<table><thead align="left"><tr id="row37854045"><th class="cellrowborder" valign="top" width="9.04%" id="mcps1.2.4.1.1"><p id="p15018481331"><a name="p15018481331"></a><a name="p15018481331"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="38.65%" id="mcps1.2.4.1.2"><p id="p46278819"><a name="p46278819"></a><a name="p46278819"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="52.31%" id="mcps1.2.4.1.3"><p id="p46972752"><a name="p46972752"></a><a name="p46972752"></a>设计建议</p>
</th>
</tr>
</thead>
<tbody><tr id="row46696577"><td class="cellrowborder" valign="top" width="9.04%" headers="mcps1.2.4.1.1 "><p id="p15064812339"><a name="p15064812339"></a><a name="p15064812339"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="38.65%" headers="mcps1.2.4.1.2 "><p id="p197021624052"><a name="p197021624052"></a><a name="p197021624052"></a>ADC_CH0</p>
</td>
<td class="cellrowborder" valign="top" width="52.31%" headers="mcps1.2.4.1.3 "><p id="p13940726153915"><a name="p13940726153915"></a><a name="p13940726153915"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row10306693"><td class="cellrowborder" valign="top" width="9.04%" headers="mcps1.2.4.1.1 "><p id="p1014823317"><a name="p1014823317"></a><a name="p1014823317"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="38.65%" headers="mcps1.2.4.1.2 "><p id="p67015249520"><a name="p67015249520"></a><a name="p67015249520"></a>ADC_CH1</p>
</td>
<td class="cellrowborder" valign="top" width="52.31%" headers="mcps1.2.4.1.3 "><p id="p10940162663917"><a name="p10940162663917"></a><a name="p10940162663917"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row47890712"><td class="cellrowborder" valign="top" width="9.04%" headers="mcps1.2.4.1.1 "><p id="p170104893314"><a name="p170104893314"></a><a name="p170104893314"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="38.65%" headers="mcps1.2.4.1.2 "><p id="p970152412511"><a name="p970152412511"></a><a name="p970152412511"></a>ADC_CH2</p>
</td>
<td class="cellrowborder" valign="top" width="52.31%" headers="mcps1.2.4.1.3 "><p id="p19939172633911"><a name="p19939172633911"></a><a name="p19939172633911"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row13910478"><td class="cellrowborder" valign="top" width="9.04%" headers="mcps1.2.4.1.1 "><p id="p226194774012"><a name="p226194774012"></a><a name="p226194774012"></a>43</p>
</td>
<td class="cellrowborder" valign="top" width="38.65%" headers="mcps1.2.4.1.2 "><p id="p1699142410514"><a name="p1699142410514"></a><a name="p1699142410514"></a>ADC_CH4</p>
</td>
<td class="cellrowborder" valign="top" width="52.31%" headers="mcps1.2.4.1.3 "><p id="p199161126153917"><a name="p199161126153917"></a><a name="p199161126153917"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row17318639114020"><td class="cellrowborder" valign="top" width="9.04%" headers="mcps1.2.4.1.1 "><p id="p200124813330"><a name="p200124813330"></a><a name="p200124813330"></a>26</p>
</td>
<td class="cellrowborder" valign="top" width="38.65%" headers="mcps1.2.4.1.2 "><p id="p1269815241553"><a name="p1269815241553"></a><a name="p1269815241553"></a>ADC_CH5</p>
</td>
<td class="cellrowborder" valign="top" width="52.31%" headers="mcps1.2.4.1.3 "><p id="p73181839104015"><a name="p73181839104015"></a><a name="p73181839104015"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row1015434794019"><td class="cellrowborder" valign="top" width="9.04%" headers="mcps1.2.4.1.1 "><p id="p18054816337"><a name="p18054816337"></a><a name="p18054816337"></a>27</p>
</td>
<td class="cellrowborder" valign="top" width="38.65%" headers="mcps1.2.4.1.2 "><p id="p169720241852"><a name="p169720241852"></a><a name="p169720241852"></a>ADC_CH6</p>
</td>
<td class="cellrowborder" valign="top" width="52.31%" headers="mcps1.2.4.1.3 "><p id="p181542047124014"><a name="p181542047124014"></a><a name="p181542047124014"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row1941015223417"><td class="cellrowborder" valign="top" width="9.04%" headers="mcps1.2.4.1.1 "><p id="p5010482335"><a name="p5010482335"></a><a name="p5010482335"></a>28</p>
</td>
<td class="cellrowborder" valign="top" width="38.65%" headers="mcps1.2.4.1.2 "><p id="p134101052163414"><a name="p134101052163414"></a><a name="p134101052163414"></a>ADC_CH7</p>
</td>
<td class="cellrowborder" valign="top" width="52.31%" headers="mcps1.2.4.1.3 "><p id="p2039251716416"><a name="p2039251716416"></a><a name="p2039251716416"></a>直连，走线≤5inch。</p>
</td>
</tr>
</tbody>
</table>

### PTA接口设计<a name="ZH-CN_TOPIC_0000001456082708"></a>

WS53V100支持1个PTA（包流量仲裁）接口，用于WIFI和BT的共存管理如[图1](#fig179201718201011)[PTA接口设计](#ZH-CN_TOPIC_0000001456082708)，输入输出电平应与VDDIO电平保持一致。设计建议如[表1](#table6991874)所示。

PTA介于WIFI MAC和BT之间，接收WIFI MAC和BT的TX/RX请求和状态输入，并且输出仲裁结果给WIFI 和BT。

**图 1**  PTA接口设计原理框图<a name="fig179201718201011"></a>  

![](figures/zh-cn_image_0000002581597206.png)

**表 1**  PTA接口设计建议

<a name="table6991874"></a>
<table><thead align="left"><tr id="row37854045"><th class="cellrowborder" valign="top" width="9.8%" id="mcps1.2.4.1.1"><p id="p0466167112919"><a name="p0466167112919"></a><a name="p0466167112919"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="36.97%" id="mcps1.2.4.1.2"><p id="p46278819"><a name="p46278819"></a><a name="p46278819"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="53.23%" id="mcps1.2.4.1.3"><p id="p46972752"><a name="p46972752"></a><a name="p46972752"></a>设计建议</p>
</th>
</tr>
</thead>
<tbody><tr id="row46696577"><td class="cellrowborder" valign="top" width="9.8%" headers="mcps1.2.4.1.1 "><p id="p84664714299"><a name="p84664714299"></a><a name="p84664714299"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="36.97%" headers="mcps1.2.4.1.2 "><p id="p1799021714185"><a name="p1799021714185"></a><a name="p1799021714185"></a>BT_FREQ</p>
</td>
<td class="cellrowborder" valign="top" width="53.23%" headers="mcps1.2.4.1.3 "><p id="p13940726153915"><a name="p13940726153915"></a><a name="p13940726153915"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row10306693"><td class="cellrowborder" valign="top" width="9.8%" headers="mcps1.2.4.1.1 "><p id="p1446616732915"><a name="p1446616732915"></a><a name="p1446616732915"></a>49/30</p>
</td>
<td class="cellrowborder" valign="top" width="36.97%" headers="mcps1.2.4.1.2 "><p id="p29535834"><a name="p29535834"></a><a name="p29535834"></a>BT_STATUS</p>
</td>
<td class="cellrowborder" valign="top" width="53.23%" headers="mcps1.2.4.1.3 "><p id="p10940162663917"><a name="p10940162663917"></a><a name="p10940162663917"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row25625616"><td class="cellrowborder" valign="top" width="9.8%" headers="mcps1.2.4.1.1 "><p id="p1246647162913"><a name="p1246647162913"></a><a name="p1246647162913"></a>48/25</p>
</td>
<td class="cellrowborder" valign="top" width="36.97%" headers="mcps1.2.4.1.2 "><p id="p5411350122710"><a name="p5411350122710"></a><a name="p5411350122710"></a>BT_ACTIVE</p>
</td>
<td class="cellrowborder" valign="top" width="53.23%" headers="mcps1.2.4.1.3 "><p id="p6938152673916"><a name="p6938152673916"></a><a name="p6938152673916"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row1399374314274"><td class="cellrowborder" valign="top" width="9.8%" headers="mcps1.2.4.1.1 "><p id="p14466872294"><a name="p14466872294"></a><a name="p14466872294"></a>51</p>
</td>
<td class="cellrowborder" valign="top" width="36.97%" headers="mcps1.2.4.1.2 "><p id="p1799484342711"><a name="p1799484342711"></a><a name="p1799484342711"></a>WLAN_ACTIVE</p>
</td>
<td class="cellrowborder" valign="top" width="53.23%" headers="mcps1.2.4.1.3 "><p id="p129948436277"><a name="p129948436277"></a><a name="p129948436277"></a>直连，走线≤5inch。</p>
</td>
</tr>
</tbody>
</table>

### 天线选择接口<a name="ZH-CN_TOPIC_0000001734928077"></a>

WS53V100有4个天线选择管脚，输出电平应与VDDIO电平保持一致。设计建议如[表1](#table14517951317)所示。

**表 1**  智能天线接口

<a name="table14517951317"></a>
<table><thead align="left"><tr id="row1352179161312"><th class="cellrowborder" valign="top" width="12.73%" id="mcps1.2.4.1.1"><p id="p47518413502"><a name="p47518413502"></a><a name="p47518413502"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="33.82%" id="mcps1.2.4.1.2"><p id="p145214961312"><a name="p145214961312"></a><a name="p145214961312"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="53.449999999999996%" id="mcps1.2.4.1.3"><p id="p25289191313"><a name="p25289191313"></a><a name="p25289191313"></a>设计建议</p>
</th>
</tr>
</thead>
<tbody><tr id="row205279191319"><td class="cellrowborder" valign="top" width="12.73%" headers="mcps1.2.4.1.1 "><p id="p115518459506"><a name="p115518459506"></a><a name="p115518459506"></a>21</p>
</td>
<td class="cellrowborder" valign="top" width="33.82%" headers="mcps1.2.4.1.2 "><p id="p2551194565014"><a name="p2551194565014"></a><a name="p2551194565014"></a>ANT_SEL3</p>
</td>
<td class="cellrowborder" valign="top" width="53.449999999999996%" headers="mcps1.2.4.1.3 "><p id="p3667172465119"><a name="p3667172465119"></a><a name="p3667172465119"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row15513911318"><td class="cellrowborder" valign="top" width="12.73%" headers="mcps1.2.4.1.1 "><p id="p632584845011"><a name="p632584845011"></a><a name="p632584845011"></a>23</p>
</td>
<td class="cellrowborder" valign="top" width="33.82%" headers="mcps1.2.4.1.2 "><p id="p203252482509"><a name="p203252482509"></a><a name="p203252482509"></a>ANT_SEL4</p>
</td>
<td class="cellrowborder" valign="top" width="53.449999999999996%" headers="mcps1.2.4.1.3 "><p id="p180322165112"><a name="p180322165112"></a><a name="p180322165112"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row1916085515504"><td class="cellrowborder" valign="top" width="12.73%" headers="mcps1.2.4.1.1 "><p id="p1758711185111"><a name="p1758711185111"></a><a name="p1758711185111"></a>43</p>
</td>
<td class="cellrowborder" valign="top" width="33.82%" headers="mcps1.2.4.1.2 "><p id="p358717155111"><a name="p358717155111"></a><a name="p358717155111"></a>ANT_SEL5</p>
</td>
<td class="cellrowborder" valign="top" width="53.449999999999996%" headers="mcps1.2.4.1.3 "><p id="p8416192545114"><a name="p8416192545114"></a><a name="p8416192545114"></a>直连，走线≤5inch。</p>
</td>
</tr>
<tr id="row1176155865017"><td class="cellrowborder" valign="top" width="12.73%" headers="mcps1.2.4.1.1 "><p id="p794019325111"><a name="p794019325111"></a><a name="p794019325111"></a>52</p>
</td>
<td class="cellrowborder" valign="top" width="33.82%" headers="mcps1.2.4.1.2 "><p id="p89401311519"><a name="p89401311519"></a><a name="p89401311519"></a>ANT_SEL2</p>
</td>
<td class="cellrowborder" valign="top" width="53.449999999999996%" headers="mcps1.2.4.1.3 "><p id="p1193452514519"><a name="p1193452514519"></a><a name="p1193452514519"></a>直连，走线≤5inch。</p>
</td>
</tr>
</tbody>
</table>

### 超低功耗接口设计<a name="ZH-CN_TOPIC_0000001505603533"></a>

WS53V100支持9个AON GPIO，输入电平应与VDDIO电平保持一致。设计建议如[表1](#table14517951317)所示。

**表 1**  超低功耗接口设计建议

<a name="table14517951317"></a>
<table><thead align="left"><tr id="row1352179161312"><th class="cellrowborder" valign="top" width="11.07%" id="mcps1.2.5.1.1"><p id="p38745125217"><a name="p38745125217"></a><a name="p38745125217"></a>Pin</p>
</th>
<th class="cellrowborder" valign="top" width="17.630000000000003%" id="mcps1.2.5.1.2"><p id="p145214961312"><a name="p145214961312"></a><a name="p145214961312"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="31.22%" id="mcps1.2.5.1.3"><p id="p25289191313"><a name="p25289191313"></a><a name="p25289191313"></a>设计建议</p>
</th>
<th class="cellrowborder" valign="top" width="40.08%" id="mcps1.2.5.1.4"><p id="p179831022162111"><a name="p179831022162111"></a><a name="p179831022162111"></a>备注</p>
</th>
</tr>
</thead>
<tbody><tr id="row18012005312"><td class="cellrowborder" valign="top" width="11.07%" headers="mcps1.2.5.1.1 "><p id="p1728142155314"><a name="p1728142155314"></a><a name="p1728142155314"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="17.630000000000003%" headers="mcps1.2.5.1.2 "><p id="p972810218533"><a name="p972810218533"></a><a name="p972810218533"></a>AGPIO1</p>
</td>
<td class="cellrowborder" valign="top" width="31.22%" headers="mcps1.2.5.1.3 "><p id="p151101158537"><a name="p151101158537"></a><a name="p151101158537"></a>直连，走线≤5inch。</p>
</td>
<td class="cellrowborder" valign="top" width="40.08%" headers="mcps1.2.5.1.4 "><p id="p898382220216"><a name="p898382220216"></a><a name="p898382220216"></a>深睡模式下，支持输入唤醒或输出。</p>
</td>
</tr>
<tr id="row164911358165219"><td class="cellrowborder" valign="top" width="11.07%" headers="mcps1.2.5.1.1 "><p id="p1572816295320"><a name="p1572816295320"></a><a name="p1572816295320"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="17.630000000000003%" headers="mcps1.2.5.1.2 "><p id="p272819217539"><a name="p272819217539"></a><a name="p272819217539"></a>AGPIO2</p>
</td>
<td class="cellrowborder" valign="top" width="31.22%" headers="mcps1.2.5.1.3 "><p id="p2886121565312"><a name="p2886121565312"></a><a name="p2886121565312"></a>直连，走线≤5inch。</p>
</td>
<td class="cellrowborder" valign="top" width="40.08%" headers="mcps1.2.5.1.4 "><p id="p1534120318358"><a name="p1534120318358"></a><a name="p1534120318358"></a>深睡模式下，支持输入唤醒或输出。</p>
</td>
</tr>
<tr id="row815045615215"><td class="cellrowborder" valign="top" width="11.07%" headers="mcps1.2.5.1.1 "><p id="p97281923537"><a name="p97281923537"></a><a name="p97281923537"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="17.630000000000003%" headers="mcps1.2.5.1.2 "><p id="p18728182135315"><a name="p18728182135315"></a><a name="p18728182135315"></a>AGPIO3</p>
</td>
<td class="cellrowborder" valign="top" width="31.22%" headers="mcps1.2.5.1.3 "><p id="p1129441695317"><a name="p1129441695317"></a><a name="p1129441695317"></a>直连，走线≤5inch。</p>
</td>
<td class="cellrowborder" valign="top" width="40.08%" headers="mcps1.2.5.1.4 "><p id="p196613473511"><a name="p196613473511"></a><a name="p196613473511"></a>深睡模式下，支持输入唤醒或输出。</p>
</td>
</tr>
<tr id="row16107054205210"><td class="cellrowborder" valign="top" width="11.07%" headers="mcps1.2.5.1.1 "><p id="p127284225319"><a name="p127284225319"></a><a name="p127284225319"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="17.630000000000003%" headers="mcps1.2.5.1.2 "><p id="p137287216536"><a name="p137287216536"></a><a name="p137287216536"></a>AGPIO4</p>
</td>
<td class="cellrowborder" valign="top" width="31.22%" headers="mcps1.2.5.1.3 "><p id="p2683181645318"><a name="p2683181645318"></a><a name="p2683181645318"></a>直连，走线≤5inch。</p>
</td>
<td class="cellrowborder" valign="top" width="40.08%" headers="mcps1.2.5.1.4 "><p id="p292719143515"><a name="p292719143515"></a><a name="p292719143515"></a>深睡模式下，支持输入唤醒或输出。</p>
</td>
</tr>
<tr id="row15513911318"><td class="cellrowborder" valign="top" width="11.07%" headers="mcps1.2.5.1.1 "><p id="p99031219165216"><a name="p99031219165216"></a><a name="p99031219165216"></a>22</p>
</td>
<td class="cellrowborder" valign="top" width="17.630000000000003%" headers="mcps1.2.5.1.2 "><p id="p129031519135220"><a name="p129031519135220"></a><a name="p129031519135220"></a>MGPIO11</p>
</td>
<td class="cellrowborder" valign="top" width="31.22%" headers="mcps1.2.5.1.3 "><p id="p16304320175315"><a name="p16304320175315"></a><a name="p16304320175315"></a>直连，走线≤5inch。</p>
</td>
<td class="cellrowborder" valign="top" width="40.08%" headers="mcps1.2.5.1.4 "><p id="p1698392282115"><a name="p1698392282115"></a><a name="p1698392282115"></a>深睡模式下，仅支持输入唤醒，不支持输出。</p>
</td>
</tr>
<tr id="row55929111319"><td class="cellrowborder" valign="top" width="11.07%" headers="mcps1.2.5.1.1 "><p id="p12667162325212"><a name="p12667162325212"></a><a name="p12667162325212"></a>28</p>
</td>
<td class="cellrowborder" valign="top" width="17.630000000000003%" headers="mcps1.2.5.1.2 "><p id="p137852017423"><a name="p137852017423"></a><a name="p137852017423"></a>MGPIO6</p>
</td>
<td class="cellrowborder" valign="top" width="31.22%" headers="mcps1.2.5.1.3 "><p id="p6572921165311"><a name="p6572921165311"></a><a name="p6572921165311"></a>直连，走线≤5inch。</p>
</td>
<td class="cellrowborder" valign="top" width="40.08%" headers="mcps1.2.5.1.4 "><p id="p1492554419351"><a name="p1492554419351"></a><a name="p1492554419351"></a>深睡模式下，仅支持输入唤醒，不支持输出。</p>
</td>
</tr>
<tr id="row39412282524"><td class="cellrowborder" valign="top" width="11.07%" headers="mcps1.2.5.1.1 "><p id="p19782113715525"><a name="p19782113715525"></a><a name="p19782113715525"></a>36</p>
</td>
<td class="cellrowborder" valign="top" width="17.630000000000003%" headers="mcps1.2.5.1.2 "><p id="p16782143710529"><a name="p16782143710529"></a><a name="p16782143710529"></a>AGPIO5</p>
</td>
<td class="cellrowborder" valign="top" width="31.22%" headers="mcps1.2.5.1.3 "><p id="p0649122365315"><a name="p0649122365315"></a><a name="p0649122365315"></a>直连，走线≤5inch。</p>
</td>
<td class="cellrowborder" valign="top" width="40.08%" headers="mcps1.2.5.1.4 "><p id="p187181953133512"><a name="p187181953133512"></a><a name="p187181953133512"></a>深睡模式下，支持输入唤醒或输出。</p>
</td>
</tr>
<tr id="row396813425211"><td class="cellrowborder" valign="top" width="11.07%" headers="mcps1.2.5.1.1 "><p id="p5601104110521"><a name="p5601104110521"></a><a name="p5601104110521"></a>47</p>
</td>
<td class="cellrowborder" valign="top" width="17.630000000000003%" headers="mcps1.2.5.1.2 "><p id="p13931154984218"><a name="p13931154984218"></a><a name="p13931154984218"></a>MGPIO16</p>
</td>
<td class="cellrowborder" valign="top" width="31.22%" headers="mcps1.2.5.1.3 "><p id="p1488112445316"><a name="p1488112445316"></a><a name="p1488112445316"></a>直连，走线≤5inch。</p>
</td>
<td class="cellrowborder" valign="top" width="40.08%" headers="mcps1.2.5.1.4 "><p id="p1441514479353"><a name="p1441514479353"></a><a name="p1441514479353"></a>深睡模式下，仅支持输入唤醒，不支持输出。</p>
</td>
</tr>
<tr id="row79695310529"><td class="cellrowborder" valign="top" width="11.07%" headers="mcps1.2.5.1.1 "><p id="p81977443522"><a name="p81977443522"></a><a name="p81977443522"></a>52</p>
</td>
<td class="cellrowborder" valign="top" width="17.630000000000003%" headers="mcps1.2.5.1.2 "><p id="p427212134316"><a name="p427212134316"></a><a name="p427212134316"></a>MGPIO7</p>
</td>
<td class="cellrowborder" valign="top" width="31.22%" headers="mcps1.2.5.1.3 "><p id="p053742420535"><a name="p053742420535"></a><a name="p053742420535"></a>直连，走线≤5inch。</p>
</td>
<td class="cellrowborder" valign="top" width="40.08%" headers="mcps1.2.5.1.4 "><p id="p18131649123517"><a name="p18131649123517"></a><a name="p18131649123517"></a>深睡模式下，仅支持输入唤醒，不支持输出。</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-notice.gif) **须知：** 
>在使用MGIO16作为输入唤醒功能时，建议默认状态保持高电平，使用低电平或者下降沿唤醒.

## 控制信号及低功耗应用参考设计<a name="ZH-CN_TOPIC_0000001505842493"></a>

-   **[SDIO四线模式](#ZH-CN_TOPIC_0000001505722797)**  

-   **[SDIO一线模式](#ZH-CN_TOPIC_0000001456242664)**  

### SDIO四线模式<a name="ZH-CN_TOPIC_0000001505722797"></a>

WS53V100 SDIO四线模式根据中断方式可以分成两种：一种是GPIO中断方式，另一种是SDIO中断方式，推荐使用SDIO中断，其中：

-   方式一：GPIO中断方式需要7个Pin脚（SDIO\_CLK，SDIO\_CMD，SDIO\_DATA0，SDIO\_DATA1，SDIO\_DATA2，SDIO\_DATA3，MGPIO13），WS53V100可使用MGPIO13作为中断。
-   方式二：SDIO中断方式需要6个Pin脚（SDIO\_CLK，SDIO\_CMD，SDIO\_DATA0，SDIO\_DATA1，SDIO\_DATA2，SDIO\_DATA3），WS53V100也可使用SDIO\_DATA1中断。

其他控制信号及低功耗应用如[表1](#table59088265)所示。

**表 1**  控制信号及低功耗应用参考设计建议

<a name="table59088265"></a>
<table><thead align="left"><tr id="row19465302"><th class="cellrowborder" valign="top" width="37.82%" id="mcps1.2.3.1.1"><p id="p33185659"><a name="p33185659"></a><a name="p33185659"></a>名称</p>
</th>
<th class="cellrowborder" valign="top" width="62.18%" id="mcps1.2.3.1.2"><p id="p65714292"><a name="p65714292"></a><a name="p65714292"></a>设计建议</p>
</th>
</tr>
</thead>
<tbody><tr id="row44130051"><td class="cellrowborder" valign="top" width="37.82%" headers="mcps1.2.3.1.1 "><p id="p17764396"><a name="p17764396"></a><a name="p17764396"></a>VBAT</p>
</td>
<td class="cellrowborder" valign="top" width="62.18%" headers="mcps1.2.3.1.2 "><p id="p66758712"><a name="p66758712"></a><a name="p66758712"></a>WS53V100芯片电源，由板级供电。</p>
</td>
</tr>
<tr id="row73943159579"><td class="cellrowborder" valign="top" width="37.82%" headers="mcps1.2.3.1.1 "><p id="p6394141510570"><a name="p6394141510570"></a><a name="p6394141510570"></a>RST_N</p>
</td>
<td class="cellrowborder" valign="top" width="62.18%" headers="mcps1.2.3.1.2 "><p id="p1539451585714"><a name="p1539451585714"></a><a name="p1539451585714"></a>复位管脚，由板级或HOST控制。</p>
</td>
</tr>
<tr id="row31476327"><td class="cellrowborder" valign="top" width="37.82%" headers="mcps1.2.3.1.1 "><p id="p66554590"><a name="p66554590"></a><a name="p66554590"></a>DEVICE_WK_HOST</p>
</td>
<td class="cellrowborder" valign="top" width="62.18%" headers="mcps1.2.3.1.2 "><p id="p14324384484"><a name="p14324384484"></a><a name="p14324384484"></a>与HOST芯片直连，用于WS53V100唤醒HOST。</p>
</td>
</tr>
<tr id="row212115416435"><td class="cellrowborder" valign="top" width="37.82%" headers="mcps1.2.3.1.1 "><p id="p51245494314"><a name="p51245494314"></a><a name="p51245494314"></a>HOST_WK_DEVICE</p>
</td>
<td class="cellrowborder" valign="top" width="62.18%" headers="mcps1.2.3.1.2 "><p id="p33981615124414"><a name="p33981615124414"></a><a name="p33981615124414"></a>与HOST芯片直连，用于HOST唤醒WS53V100。</p>
</td>
</tr>
<tr id="row185701344201513"><td class="cellrowborder" valign="top" width="37.82%" headers="mcps1.2.3.1.1 "><p id="p1957014416157"><a name="p1957014416157"></a><a name="p1957014416157"></a>SDIO INTERRUPT</p>
</td>
<td class="cellrowborder" valign="top" width="62.18%" headers="mcps1.2.3.1.2 "><p id="p257094441513"><a name="p257094441513"></a><a name="p257094441513"></a>作为SDIO的中断信号。WS53V100可使用SDIO的DATA1作为中断信号、也可用GPIO充当。</p>
</td>
</tr>
</tbody>
</table>

如果需要低功耗应用，则必须考虑以下设计要求：

-   DEVICE\_WK\_HOST必须连接到HOST常供电的GPIO。
-   HOST\_WK\_DEVICE必须连接到DEVICE常供电的GPIO。
-   
低功耗应用系统连接参考框如[图1](#fig18907620135117)所示。

**图 1**  SDIO四线模式低功耗应用系统连接参考框图<a name="fig18907620135117"></a>  

![](figures/zh-cn_image_0000002581593992.png)

### SDIO一线模式<a name="ZH-CN_TOPIC_0000001456242664"></a>

WS53V100 SDIO一线模式根据中断方式可以分成两种：一种是GPIO中断方式，另一种是SDIO中断方式，其中:

-   方式一：GPIO中断方式需要4个Pin脚（SDIO\_CLK，SDIO\_CMD，DATA0，MGPIO13），可使用MGPIO13作为中断。
-   方式二：SDIO中断方式需要4个Pin脚（SDIO\_CLK，SDIO\_CMD，DATA0，SDIO\_DATA1），可使用SDIO\_DATA1中断。

其他控制管脚和四线模式一致，低功耗应用系统连接参考框图如[图1](#fig10071935011)所示。

**图 1**  SDIO一线模式低功耗应用系统连接参考框图<a name="fig10071935011"></a>  

![](figures/zh-cn_image_0000002581753536.png)

# PCB设计建议<a name="ZH-CN_TOPIC_0000001455763048"></a>

-   **[叠层和布局](#ZH-CN_TOPIC_0000001505722829)**  

-   **[Fanout封装设计建议](#ZH-CN_TOPIC_0000001505603545)**  

-   **[PCB布局](#ZH-CN_TOPIC_0000001455763044)**  

-   **[电源](#ZH-CN_TOPIC_0000001455763036)**  

-   **[RF布线指导](#ZH-CN_TOPIC_0000001455922808)**  

-   **[CMU布线指导](#ZH-CN_TOPIC_0000001455763076)**  

-   **[DBB布线指导](#ZH-CN_TOPIC_0000001505882573)**  

-   **[SDIO接口布线指导](#ZH-CN_TOPIC_0000001505842453)**  

-   **[GND布线指导](#ZH-CN_TOPIC_0000001505603541)**  

## 叠层和布局<a name="ZH-CN_TOPIC_0000001505722829"></a>

WS53V100封装大小，QFN52 6×6mm，PCB支持4层板，支持器件单面贴设计。

-   TOP层：信号走线，信号线尽量走TOP层。
-   L2层：地平面层，保持一个完整的地平面层。
-   L3层：电源平面层，电源走线尽量走第三层，且电源之间需要用地隔开。
-   BOTTOM 层：可以走少量的信号线，尽量保持BOTTOM层为一个完整的地平面层。

PCB设计注意事项：

-   推荐PCB板厚On Board方案一般≥1mm，防止翘曲，过孔10mil/22mil。
-   PCB 典型材料FR4介电常数为4.0\~4.3，表层铜箔厚度建议为1.2mil \(0.5 oz+plating\)，PCB板厚度一般≥1.0mm，典型值为1.2mm，可选用1.0mm。

常用的叠层设计和阻抗控制可参考[表1](#table189541251132311)。

**表 1**  4层板1.2mm参考叠层信息参考

<a name="table189541251132311"></a>
<table><thead align="left"><tr id="row96955272313"><th class="cellrowborder" valign="top" id="mcps1.2.8.1.1"><p id="p13692523237"><a name="p13692523237"></a><a name="p13692523237"></a>层标识</p>
</th>
<th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.8.1.2"><p id="p86985252311"><a name="p86985252311"></a><a name="p86985252311"></a>层叠图示</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.8.1.3"><p id="p06995210239"><a name="p06995210239"></a><a name="p06995210239"></a>RC</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.8.1.4"><p id="p1769135215238"><a name="p1769135215238"></a><a name="p1769135215238"></a>设计厚度(μm)</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.8.1.5"><p id="p1269652122314"><a name="p1269652122314"></a><a name="p1269652122314"></a>PCB板厂调整厚度(μm)</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.8.1.6"><p id="p16945252315"><a name="p16945252315"></a><a name="p16945252315"></a>厂内控制公差(μm)</p>
</th>
</tr>
</thead>
<tbody><tr id="row14696527232"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p146965217233"><a name="p146965217233"></a><a name="p146965217233"></a>阻焊</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.8.1.2 "><p id="p4691452172312"><a name="p4691452172312"></a><a name="p4691452172312"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p12696528230"><a name="p12696528230"></a><a name="p12696528230"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p167095211236"><a name="p167095211236"></a><a name="p167095211236"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p197018520234"><a name="p197018520234"></a><a name="p197018520234"></a>20</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.6 "><p id="p9707529233"><a name="p9707529233"></a><a name="p9707529233"></a>20&plusmn;15</p>
</td>
</tr>
<tr id="row0701652102311"><td class="cellrowborder" rowspan="2" valign="top" headers="mcps1.2.8.1.1 "><p id="p470652162315"><a name="p470652162315"></a><a name="p470652162315"></a>Art01</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.8.1.2 "><p id="p18701752182312"><a name="p18701752182312"></a><a name="p18701752182312"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p67055222313"><a name="p67055222313"></a><a name="p67055222313"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p770115213232"><a name="p770115213232"></a><a name="p770115213232"></a>1/2oz+plating</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1570352202317"><a name="p1570352202317"></a><a name="p1570352202317"></a>40</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.6 "><p id="p1170452152312"><a name="p1170452152312"></a><a name="p1170452152312"></a>40&plusmn;15</p>
</td>
</tr>
<tr id="row1670155292317"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.8.1.2 "><p id="p14705525231"><a name="p14705525231"></a><a name="p14705525231"></a>PP_7628</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p1670552112319"><a name="p1670552112319"></a><a name="p1670552112319"></a>50%</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1270145222319"><a name="p1270145222319"></a><a name="p1270145222319"></a>208</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p177012526231"><a name="p177012526231"></a><a name="p177012526231"></a>215</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.6 "><p id="p1701652142314"><a name="p1701652142314"></a><a name="p1701652142314"></a>215&plusmn;20</p>
</td>
</tr>
<tr id="row2701152182318"><td class="cellrowborder" rowspan="2" valign="top" headers="mcps1.2.8.1.1 "><p id="p127045272310"><a name="p127045272310"></a><a name="p127045272310"></a>Art02</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.8.1.2 "><p id="p170195214231"><a name="p170195214231"></a><a name="p170195214231"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p17011527235"><a name="p17011527235"></a><a name="p17011527235"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1070205218239"><a name="p1070205218239"></a><a name="p1070205218239"></a>30</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p7701452122314"><a name="p7701452122314"></a><a name="p7701452122314"></a>30</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.6 "><p id="p18700523234"><a name="p18700523234"></a><a name="p18700523234"></a>30&plusmn;5</p>
</td>
</tr>
<tr id="row07055219236"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.8.1.2 "><p id="p12708524232"><a name="p12708524232"></a><a name="p12708524232"></a>core (exclude copper)</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p77055217239"><a name="p77055217239"></a><a name="p77055217239"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p670452202318"><a name="p670452202318"></a><a name="p670452202318"></a>600</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p170175215234"><a name="p170175215234"></a><a name="p170175215234"></a>600</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.6 "><p id="p117065292311"><a name="p117065292311"></a><a name="p117065292311"></a>600&plusmn;64</p>
</td>
</tr>
<tr id="row127017529232"><td class="cellrowborder" rowspan="2" valign="top" headers="mcps1.2.8.1.1 "><p id="p15704529234"><a name="p15704529234"></a><a name="p15704529234"></a>Art03</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.8.1.2 "><p id="p1170195252312"><a name="p1170195252312"></a><a name="p1170195252312"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p4716527238"><a name="p4716527238"></a><a name="p4716527238"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p671052102315"><a name="p671052102315"></a><a name="p671052102315"></a>30</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p47117523233"><a name="p47117523233"></a><a name="p47117523233"></a>30</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.6 "><p id="p871352172315"><a name="p871352172315"></a><a name="p871352172315"></a>30&plusmn;5</p>
</td>
</tr>
<tr id="row1871452122318"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.8.1.2 "><p id="p471552162314"><a name="p471552162314"></a><a name="p471552162314"></a>PP_7628</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p4711852142310"><a name="p4711852142310"></a><a name="p4711852142310"></a>50%</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1471175212238"><a name="p1471175212238"></a><a name="p1471175212238"></a>208</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p157155282317"><a name="p157155282317"></a><a name="p157155282317"></a>214</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.6 "><p id="p137125215235"><a name="p137125215235"></a><a name="p137125215235"></a>214&plusmn;20</p>
</td>
</tr>
<tr id="row197135212314"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p167114523232"><a name="p167114523232"></a><a name="p167114523232"></a>Art04</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.8.1.2 "><p id="p171175222320"><a name="p171175222320"></a><a name="p171175222320"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p97165252312"><a name="p97165252312"></a><a name="p97165252312"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1271195262311"><a name="p1271195262311"></a><a name="p1271195262311"></a>1/2oz+plating</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1771852192315"><a name="p1771852192315"></a><a name="p1771852192315"></a>40</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.6 "><p id="p177114521238"><a name="p177114521238"></a><a name="p177114521238"></a>40&plusmn;15</p>
</td>
</tr>
<tr id="row071155232316"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p97175219235"><a name="p97175219235"></a><a name="p97175219235"></a>阻焊</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.8.1.2 "><p id="p117452036181811"><a name="p117452036181811"></a><a name="p117452036181811"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p37116525237"><a name="p37116525237"></a><a name="p37116525237"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p107145213230"><a name="p107145213230"></a><a name="p107145213230"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p9719526237"><a name="p9719526237"></a><a name="p9719526237"></a>20</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.6 "><p id="p87115213237"><a name="p87115213237"></a><a name="p87115213237"></a>20&plusmn;15</p>
</td>
</tr>
<tr id="row471125214234"><td class="cellrowborder" valign="top" headers="mcps1.2.8.1.1 "><p id="p67165216231"><a name="p67165216231"></a><a name="p67165216231"></a>板厚</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.8.1.2 "><p id="p785725510189"><a name="p785725510189"></a><a name="p785725510189"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.3 "><p id="p2711152192313"><a name="p2711152192313"></a><a name="p2711152192313"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.4 "><p id="p1071105202320"><a name="p1071105202320"></a><a name="p1071105202320"></a>1.2&plusmn;0.12mm</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.5 "><p id="p1671145252313"><a name="p1671145252313"></a><a name="p1671145252313"></a>1.2&plusmn;0.12mm</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.8.1.6 "><p id="p071152162315"><a name="p071152162315"></a><a name="p071152162315"></a>-</p>
</td>
</tr>
</tbody>
</table>

**表 2**  单线线宽、阻抗、参考层控制信息

<a name="table6486103461920"></a>
<table><thead align="left"><tr id="row948713431916"><th class="cellrowborder" valign="top" width="16.666666666666664%" id="mcps1.2.7.1.1"><p id="p1974134618195"><a name="p1974134618195"></a><a name="p1974134618195"></a>信号层</p>
</th>
<th class="cellrowborder" valign="top" width="16.666666666666664%" id="mcps1.2.7.1.2"><p id="p199744469194"><a name="p199744469194"></a><a name="p199744469194"></a>接地层</p>
</th>
<th class="cellrowborder" valign="top" width="16.666666666666664%" id="mcps1.2.7.1.3"><p id="p497416464193"><a name="p497416464193"></a><a name="p497416464193"></a>阻抗目标</p>
</th>
<th class="cellrowborder" valign="top" width="16.666666666666664%" id="mcps1.2.7.1.4"><p id="p19975346111918"><a name="p19975346111918"></a><a name="p19975346111918"></a>阻抗公差</p>
</th>
<th class="cellrowborder" valign="top" width="16.666666666666664%" id="mcps1.2.7.1.5"><p id="p69751346131910"><a name="p69751346131910"></a><a name="p69751346131910"></a>设计线宽（mil）</p>
</th>
<th class="cellrowborder" valign="top" width="16.666666666666664%" id="mcps1.2.7.1.6"><p id="p1097514617197"><a name="p1097514617197"></a><a name="p1097514617197"></a>距铜（mil）</p>
</th>
</tr>
</thead>
<tbody><tr id="row9488934131915"><td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.1 "><p id="p109751046101915"><a name="p109751046101915"></a><a name="p109751046101915"></a>L1</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.2 "><p id="p11975174612199"><a name="p11975174612199"></a><a name="p11975174612199"></a>L1&L2</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.3 "><p id="p1597554671911"><a name="p1597554671911"></a><a name="p1597554671911"></a>50Ω</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.4 "><p id="p11975164610199"><a name="p11975164610199"></a><a name="p11975164610199"></a>10%</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.5 "><p id="p19975134671918"><a name="p19975134671918"></a><a name="p19975134671918"></a>11</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666664%" headers="mcps1.2.7.1.6 "><p id="p17976144651916"><a name="p17976144651916"></a><a name="p17976144651916"></a>6</p>
</td>
</tr>
</tbody>
</table>

## Fanout封装设计建议<a name="ZH-CN_TOPIC_0000001505603545"></a>

WS53V100 四层板Fanout如[图1](#fig20338107123018)所示。

**图 1**  PCB 四层板Fanout参考设计<a name="fig20338107123018"></a>  
![](figures/PCB-四层板Fanout参考设计.png "PCB-四层板Fanout参考设计")

其中：

-   黄色：VDD\_RF\_RX\_1P1、VDD\_WL\_RF\_TRX\_1P1、VDD\_RFLDO1
-   绿色：VDD\_WL\_RF\_PA\_3P3、VDD\_VBAT1、VDD\_VBAT2、AVDD33
-   蓝色：VDDIO
-   紫色：VDD\_1P3、VDD\_BSLE\_RF\_PA\_1P3、VDD\_BSLE\_RF\_DRV\_1P3、VDD\_BSLE\_PLL\_DCO\_1P3、VDD1P3\_PMU1
-   白色：VDD\_RFLDO2、VDD\_BSLE\_DPALDO、VDD\_CLDO
-   橙色：BUCK\_LX
-   淡蓝色：RF

## PCB布局<a name="ZH-CN_TOPIC_0000001455763044"></a>

WS53V100应用支持On Board和模组两种方案。

-   On Board方案
    -   支持4层板设计
    -   贴片器件建议为0201封装（inch）

-   SDIO模组
    -   4层板
    -   贴片器件建议用0201封装（inch）

-   IPC用户

    考虑小型化，一般建议选用模组

-   IOT产品
    -   考虑到板子空间比较小，建议用0201单面贴

PCB设计以 SDIO模组四层板为例，参考设计如[图1](#fig165311918113011)所示。

**图 1**  SDIO模组PCB布局参考<a name="fig165311918113011"></a>  

![](figures/zh-cn_image_0000001763318282.png)

其中：

-   黄色：VDD\_RF\_RX\_1P1，VDD\_WL\_RF\_TRX\_1P1，VDD\_RFLDO1
-   绿色：VDD\_WL\_RF\_PA\_3P3，VDD\_VBAT1，VDD\_VBAT2，AVDD33
-   蓝色：VDDIO
-   紫色：VDD\_1P3，VDD\_BSLE\_RF\_PA\_1P3，VDD\_BSLE\_RF\_DRV\_1P3，VDD1P3\_PMU1
-   白色：VDD\_RFLDO2，VDD\_BSLE\_DPALDO，VDD\_CLDO
-   橙色：BUCK\_LX
-   淡蓝色：RF

## 电源<a name="ZH-CN_TOPIC_0000001455763036"></a>

-   **[VBAT布线指导](#ZH-CN_TOPIC_0000001505882565)**  

-   **[BUCK布线指导](#ZH-CN_TOPIC_0000001455763080)**  

### VBAT布线指导<a name="ZH-CN_TOPIC_0000001505882565"></a>

VBAT布线建议如下：

-   VDD\_VBAT1峰值电流500mA，基于100mA/4mil原则，VBAT1电源走线线宽需≥20mil。滤波电容4.7μF需要靠近管脚放置。
-   VDD\_VBAT2峰值电流50mA。滤波电容1μF需要靠近管脚放置，且电源走线须先经过滤波电容再到芯片的电源管脚。
-   AVDD33峰值电流80mA。有空间单独放置1uF滤波电容，模组空间紧凑可以和VDD\_VBAT1 共用4.7uF电容
-   VDD\_CLDO滤波电容靠近管脚放置，峰值电流300mA，走线线宽建议≥12mil。

电源管脚的滤波电容摆放位置如[图1](#fig15632742191213)所示。

**图 1**  四层板VBAT布线参考<a name="fig15632742191213"></a>  

![](figures/zh-cn_image_0000001810168349.png)

### BUCK布线指导<a name="ZH-CN_TOPIC_0000001455763080"></a>

BUCK的输出、BUCK电感、滤波电容及地形成的最短回流通路十分重要。该环路中包含大量高频开关电流成分，因此PCB走线时应该最小化环路面积。BUCK回流环路面积越大，磁场辐射越强，这将成为噪声扩散的主要来源。

BUCK与RF正好在芯片的对角处，主要为了避免BUCK的电源噪声影响RF（左下方）和模拟部分，因此布局时外接功率电感尽量远离WS53V100的RF和模拟部分，以减少BUCK对射频性能的影响。

PCB走线约束如下：

-   BUCK\_LX：是强干扰源，需要与其他敏感信号保持距离，输出峰值电流500mA，线宽需要≥20mil，且能够尽量包地处理，包地线尽量粗且多打地孔。
-   VDD1P3\_PMU1：BUCK输出反馈给芯片内部CLDO输入，峰值电流300mA，线宽需要≥12mil，滤波电容4.7μF靠近管脚放置。走线源头从1P3的输出电容上取电。走线两端尽量包地处理，包地线尽量粗且多打地孔。
-   VDD\_1P3： BUCK输入给芯片内部RFLDO供电，峰值电流100mA，滤波电容1μF靠近管脚放置。走线源头从1P3的输出电容上取电。走线两端尽量包地处理，包地线尽量粗且多打地孔，背面走线远离芯片Epad，请勿割裂参考地平面。
-   VDD\_BSLE\_RF\_PA\_1P3：BSLE LDO输入电源，峰值电流300mA，滤波电容1μF靠近管脚放置。走线源头从1P3的输出电容上取电。走线两端尽量包地处理，包地线尽量粗且多打地孔，背面走线远离芯片Epad，请勿割裂参考地平面。
-   VDD\_BSLE\_RF\_DRV\_1P3：BSLE LDO输入电源，峰值电流70mA，滤波电容1μF靠近管脚放置（模组空间受限，可以考虑共用VDD\_BSLE\_RF\_PA\_1P3电源的1uF电容）。走线源头从1P3的输出电容上取电。走线两端尽量包地处理，包地线尽量粗且多打地孔，背面走线远离芯片Epad，请勿割裂参考地平面。
-   VDD\_BSLE\_PLL\_DCO\_1P3：BSLE LDO输入电源，峰值电流40mA，滤波电容1μF靠近管脚放置。走线源头从1P3的输出电容上取电。走线两端尽量包地处理，包地线尽量粗且多打地孔，背面走线远离芯片Epad，请勿割裂参考地平面。

**图 1**  四层板BUCK走线参考<a name="fig15484173511126"></a>  

![](figures/zh-cn_image_0000001810169653.png)

## RF布线指导<a name="ZH-CN_TOPIC_0000001455922808"></a>

RF布线建议如下：

-   RFLDO1电源走线支持串行走线，但星型走线可以带来更好的性能，[图1](#fig13838185716128)中黄色走线即为星形走线。
-   VDD\_RFLDO2外接一个1μF的电容，给芯片内部的RFLDO2电源滤波。
-   VDD\_RFLDO1是芯片内部LDO输出，输出1.15V给RF供电，峰值电流50mA，线宽需要≥5mil。
-   VDD\_WL\_RF\_PA\_3P3给WiFi的PA供电，可以直接连接到VBAT；滤波电容靠芯片管脚放置。
-   PA电源滤波电容放置以及出线不要有过孔，建议与芯片同层出线布局，避免过孔带来寄生参数。走线压降要求<30mV。峰值电流500mA，线宽需要≥20mil。
-   VDD\_RF\_RX\_1P1是给LNA供电的电源，走线要避开RF信号干扰。
-   VDD\_WL\_RF\_TRX\_1P1是芯片内部TRX相关模块输入电源，，走线要避开RF信号干扰。
-   VDD\_RFLDO1、VDD\_RF\_RX\_1P1、VDD\_WL\_RF\_TRX\_1P1、VDD\_WL\_RF\_PA\_3P3给电源走线间尽量错开，避免相互间干扰。
-   WiFi RF前端匹配电路尽量靠近芯片放置，ESD防护电感可以靠近天线端。
-   RF信号线走线尽量短，控制阻抗50Ω，走线两边包地多打地孔。
-   RF射频线远离高速时钟线和电源线，保持射频走线参考面完整；如果射频线参考面被分割，需要通过0Ω电阻跨接保持连通性。
-   射频走线的参考地与芯片主地须保持良好连通，地回路不好的情况下，射频性能会恶化。芯片EPAD需要从两个脚拉出与外部的地连接保持连接。
-   RF匹配滤波电路：如有空间，可以预留trap电路，参考电路如[图2](#fig148115216132)，匹配值需要根据不同Layout和PCB叠层进行实测调整。如模组空间有限，可以采用π型滤波电路。滤波电容需要单点接地不能直接接在TOP层，需要打一个过孔连接到BOTTOM层，如果是多层板过孔不与中间层的地相连，过孔在中间层需要跟TOP层一样做禁空处理。这样处理之后的过孔在RF频率上过孔相当于一个小电感与电容一起组成一个LC电路，起到抑制谐波辐射的目的。前面PCB布局有提到这两个过孔的位置不能太近最好能分布在RF线的两边。

**图 1**  四层板RFLDO1及RF走线布线参考<a name="fig13838185716128"></a>  

![](figures/zh-cn_image_0000001810170405.png)

**图 2**  RF匹配电路参考电路图<a name="fig148115216132"></a>  
![](figures/RF匹配电路参考电路图.png "RF匹配电路参考电路图")

## CMU布线指导<a name="ZH-CN_TOPIC_0000001455763076"></a>

CMU（时钟管理单元）布线建议如下：

-   WiFi系统对时钟要求很高，晶体布局以及XIN和XOUT走线须远离噪声源（RF和BUCK）和热源，避免噪声干扰引起系统相噪变差，或者热源辐射引起晶体温漂。
-   建议在XOUT走线靠近芯片端预留电阻焊盘，用于串接一个30Ω电阻限流。
-   PCB为4层板时，晶体的GND pad建议在TOP层和其他地分割，通过过孔连接到主地，防止单板上的器件发热影响时钟精度；信号pad下面挖空到主地层，减小pad的寄生电容。
-   XIN/XOUT走线尽量短，XIN/XOUT走线寄生电容＜1pF，建议能够包地处理，包地线尽量粗且多打地孔。
-   如果是On Board设计且是双面贴，可以考虑将晶体放到BOTTOM层，XIN/XOUT在靠近芯片管脚处打过孔上来连接到芯片。
-   XIN/XOUT与VBAT之间用地过孔分隔开。

CMU布局及布线参考如[图1](#fig9975133431312)所示。

**图 1**  四层板CMU布线参考<a name="fig9975133431312"></a>  

![](figures/zh-cn_image_0000001763177188.png)

## DBB布线指导<a name="ZH-CN_TOPIC_0000001505882573"></a>

DBB（数字基带）布线建议如下：

-   VDDIO电源滤波电容尽量靠近管脚放置。
-   数字信号设计规则相对宽松，仅需避开敏感的电源、RF和模拟部分。
-   MGPIO16管脚有负电压输入时，可能会导致芯片复位，使用时应避免该管脚出现负压；PCB设计有长走线时，建议走内层，避免受到外部干扰。

## SDIO接口布线指导<a name="ZH-CN_TOPIC_0000001505842453"></a>

接口布线建议如下：

-   SDIO最高支持50MHz，要求布局布线远离敏感的电源、RF和模拟部分，且走线线长尽可能短不要超过5inch。
-   SDIO走线线距严格按照3W原则，即信号与信号线之间保持3倍线宽，避免信号间的串扰；SDIO\_CLK信号包地处理，包地线尽量粗且走线两侧多打地孔。
-   SDIO\_CLK靠近源端串33Ω电阻。
-   SDIO\_DATA（0～3）预留上拉电阻的一端直接接到信号线上，另一端连接到VDDIO。这样可以减少信号的反射。

## GND布线指导<a name="ZH-CN_TOPIC_0000001505603541"></a>

除接地管脚外，WS53V100还需要将Epad焊盘接地。

GND布线建议如下：

-   参考地平面尽量完整，尽量使得每个接地管脚、电容接地都能够和芯片Epad以及系统主地有良好的地回路。
-   Epad焊盘上打通孔，孔中心距一般约23～40 mil，一般情况下建议28mil。

**图 1**  四层板Epad布线参考（Top层）<a name="fig1614010171419"></a>  
![](figures/四层板Epad布线参考（Top层）.png "四层板Epad布线参考（Top层）")

**图 2**  Epad布线参考（Bottom层）<a name="fig135742310147"></a>  
![](figures/Epad布线参考（Bottom层）.png "Epad布线参考（Bottom层）")

# 热设计建议<a name="ZH-CN_TOPIC_0000001456082728"></a>

-   **[工作条件](#ZH-CN_TOPIC_0000001455922824)**  

-   **[电路热设计参考](#ZH-CN_TOPIC_0000001505603529)**  

## 工作条件<a name="ZH-CN_TOPIC_0000001455922824"></a>

>![](public_sys-resources/icon-notice.gif) **须知：** 
>-   芯片的极限结温的最大值为125℃，任何条件下芯片的结温都不能大于该数值。
>-   芯片的长期工作结温的最大值为105℃，正常工作条件下芯片的结温应该小于该数值。
>-   在短期工作条件下，芯片可以容忍超过105℃（长期工作结温的最大值）而小于125℃（极限结温的最大值）的高温，但长时间工作在超过105℃（长期工作结温的最大值）结温下会导致芯片寿命缩减。
>-   根据GR-63-CORE标准，短期工作条件定义为每次持续时间不超过96小时，并且每年累计时间不超过15天。

**表 1**  芯片的结温要求

<a name="table18701719219"></a>
<table><thead align="left"><tr id="row1710037529"><th class="cellrowborder" valign="top" width="11.41%" id="mcps1.2.7.1.1"><p id="p16100167424"><a name="p16100167424"></a><a name="p16100167424"></a>封装形式</p>
</th>
<th class="cellrowborder" valign="top" width="17.76%" id="mcps1.2.7.1.2"><p id="p610012714213"><a name="p610012714213"></a><a name="p610012714213"></a>正常工作结温下限(℃)</p>
</th>
<th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.7.1.3"><p id="p1100107526"><a name="p1100107526"></a><a name="p1100107526"></a>长期工作最大结温(℃)</p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.7.1.4"><p id="p151001673210"><a name="p151001673210"></a><a name="p151001673210"></a>短期工作上限结温(℃)</p>
</th>
<th class="cellrowborder" valign="top" width="14.979999999999999%" id="mcps1.2.7.1.5"><p id="p4100571925"><a name="p4100571925"></a><a name="p4100571925"></a>破坏性最大结温(℃)</p>
</th>
<th class="cellrowborder" valign="top" width="20.16%" id="mcps1.2.7.1.6"><p id="p10100875217"><a name="p10100875217"></a><a name="p10100875217"></a>生命周期定义</p>
</th>
</tr>
</thead>
<tbody><tr id="row15100127525"><td class="cellrowborder" valign="top" width="11.41%" headers="mcps1.2.7.1.1 "><p id="p9100472219"><a name="p9100472219"></a><a name="p9100472219"></a>QFN</p>
</td>
<td class="cellrowborder" valign="top" width="17.76%" headers="mcps1.2.7.1.2 "><p id="p1910067427"><a name="p1910067427"></a><a name="p1910067427"></a>-40</p>
</td>
<td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.7.1.3 "><p id="p201001977214"><a name="p201001977214"></a><a name="p201001977214"></a>105</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.7.1.4 "><p id="p010012718212"><a name="p010012718212"></a><a name="p010012718212"></a>125</p>
</td>
<td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.7.1.5 "><p id="p171001171026"><a name="p171001171026"></a><a name="p171001171026"></a>125</p>
</td>
<td class="cellrowborder" valign="top" width="20.16%" headers="mcps1.2.7.1.6 "><p id="p1210017718212"><a name="p1210017718212"></a><a name="p1210017718212"></a>10年</p>
</td>
</tr>
</tbody>
</table>

**表 2**  芯片的封装热阻

<a name="table1096004514427"></a>
<table><thead align="left"><tr id="row81154694219"><th class="cellrowborder" valign="top" id="mcps1.2.6.1.1"><p id="p611146184213"><a name="p611146184213"></a><a name="p611146184213"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.6.1.2"><p id="p51246124219"><a name="p51246124219"></a><a name="p51246124219"></a>符号</p>
</th>
<th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.6.1.3"><p id="p1011946104212"><a name="p1011946104212"></a><a name="p1011946104212"></a>WS53V100</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.6.1.4"><p id="p1419462421"><a name="p1419462421"></a><a name="p1419462421"></a>单位</p>
</th>
</tr>
</thead>
<tbody><tr id="row12174694218"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p911460429"><a name="p911460429"></a><a name="p911460429"></a>Junction-to-ambient thermal resistance</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p121184694213"><a name="p121184694213"></a><a name="p121184694213"></a>θ<sub id="sub623295020"><a name="sub623295020"></a><a name="sub623295020"></a>JA</sub></p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.3 "><p id="p41164611422"><a name="p41164611422"></a><a name="p41164611422"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p414464421"><a name="p414464421"></a><a name="p414464421"></a>℃/W</p>
</td>
</tr>
<tr id="row1216465422"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p5194614210"><a name="p5194614210"></a><a name="p5194614210"></a>Junction-to-case thermal resistance</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p10144611424"><a name="p10144611424"></a><a name="p10144611424"></a>θ<sub id="sub536291600"><a name="sub536291600"></a><a name="sub536291600"></a>JC</sub></p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.3 "><p id="p152246154210"><a name="p152246154210"></a><a name="p152246154210"></a>28.0</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p1722046164218"><a name="p1722046164218"></a><a name="p1722046164218"></a>℃/W</p>
</td>
</tr>
<tr id="row82146184219"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p82104615423"><a name="p82104615423"></a><a name="p82104615423"></a>Junction-to-top center of case thermal resistance</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p19274619425"><a name="p19274619425"></a><a name="p19274619425"></a>Ψ<sub id="sub1310291602"><a name="sub1310291602"></a><a name="sub1310291602"></a>JT</sub></p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.3 "><p id="p42204615426"><a name="p42204615426"></a><a name="p42204615426"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p12213463427"><a name="p12213463427"></a><a name="p12213463427"></a>℃/W</p>
</td>
</tr>
<tr id="row827466424"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p16244664213"><a name="p16244664213"></a><a name="p16244664213"></a>Junction-to-board thermal resistance</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p102104674211"><a name="p102104674211"></a><a name="p102104674211"></a>θ<sub id="sub2038298015"><a name="sub2038298015"></a><a name="sub2038298015"></a>JB</sub></p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.3 "><p id="p1728464424"><a name="p1728464424"></a><a name="p1728464424"></a>19.5</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p15204612428"><a name="p15204612428"></a><a name="p15204612428"></a>℃/W</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **说明：** 
>热阻基于JEDEC JESD51-2标准给出，应用时的系统设计及环境可能与JEDEC JESD51-2标准不同，需要根据应用条件作出分析。

上述封装热阻参数仿真环境是JEDEC标准的4层PCB，如[图1](#fig207135617436)所示。

**图 1**  JEDEC标准的4层PCB参数<a name="fig207135617436"></a>  
![](figures/JEDEC标准的4层PCB参数.png "JEDEC标准的4层PCB参数")

## 电路热设计参考<a name="ZH-CN_TOPIC_0000001505603529"></a>

-   **[器件布局](#ZH-CN_TOPIC_0000001455922792)**  

-   **[PCB](#ZH-CN_TOPIC_0000001505603549)**  

### 器件布局<a name="ZH-CN_TOPIC_0000001455922792"></a>

结合产品结构和热设计，器件布局建议如下：

-   单板上大功耗且易产生热量器件要均匀分布，避免局部过热，影响器件可靠性和散热效率。
-   合理设计结构，保证产品内部与外界有热交换途径。
-   对单板关键发热器件充分进行极端应用场景的温升测试，确保器件在安全的温度范围内长期可靠工作。
-   必要情况下，关键发热器件可以增加散热片，进一步提升散热效果。

### PCB<a name="ZH-CN_TOPIC_0000001505603549"></a>

走线热设计建议如下：

-   芯片底下的过孔采用FULL孔连接，而不是普通的花孔连接，以提高单板散热效率。
-   在热量大的器件正下方和周边尽量增大铜皮面积，发热器件背面的地平面尽量减少分割，完整地平面能够有效分散热量，提高整体散热效果。另外，如果结构允许，将芯片正背面附近地平面进行亮铜处理，也能够进一步提升散热效果。

# 焊接工艺<a name="ZH-CN_TOPIC_0000001455922844"></a>

-   **[概述](#ZH-CN_TOPIC_0000001505842449)**  

-   **[无铅回流焊工艺参数要求](#ZH-CN_TOPIC_0000001455922828)**  

-   **[混合回流焊工艺参数要求](#ZH-CN_TOPIC_0000001456242672)**  

## 概述<a name="ZH-CN_TOPIC_0000001505842449"></a>

本章主要介绍客户端在使用芯片做回流焊时工艺控制：主要是无铅工艺和混合工艺两类。

定义说明：

-   芯片：给客户的芯片均为ROHS产品，均满足无铅要求。
-   无铅工艺：所有器件\(主板/所有IC/电容电阻等\)均为无铅器件，并使用无铅锡膏的纯无铅工艺。

## 无铅回流焊工艺参数要求<a name="ZH-CN_TOPIC_0000001455922828"></a>

无铅回流焊接工艺曲线如[图1](#fig11189932125217)所示。

**图 1**  无铅回流焊接工艺曲线<a name="fig11189932125217"></a>  
![](figures/无铅回流焊接工艺曲线.jpg "无铅回流焊接工艺曲线")

无铅回流焊工艺参数如[表1](#table7961631185211)所示。

**表 1**  无铅回流焊工艺参数

<a name="table7961631185211"></a>
<table><thead align="left"><tr id="row219073225214"><th class="cellrowborder" valign="top" width="26.44%" id="mcps1.2.6.1.1"><p id="p191901832105216"><a name="p191901832105216"></a><a name="p191901832105216"></a>区域</p>
</th>
<th class="cellrowborder" valign="top" width="13.22%" id="mcps1.2.6.1.2"><p id="p1319093211526"><a name="p1319093211526"></a><a name="p1319093211526"></a>时间</p>
</th>
<th class="cellrowborder" valign="top" width="14.77%" id="mcps1.2.6.1.3"><p id="p1219017328529"><a name="p1219017328529"></a><a name="p1219017328529"></a>升温速率</p>
</th>
<th class="cellrowborder" valign="top" width="13.22%" id="mcps1.2.6.1.4"><p id="p13190133205217"><a name="p13190133205217"></a><a name="p13190133205217"></a>峰值温度</p>
</th>
<th class="cellrowborder" valign="top" width="32.35%" id="mcps1.2.6.1.5"><p id="p519053285219"><a name="p519053285219"></a><a name="p519053285219"></a>降温速率</p>
</th>
</tr>
</thead>
<tbody><tr id="row1519016329524"><td class="cellrowborder" valign="top" width="26.44%" headers="mcps1.2.6.1.1 "><p id="p0190183215525"><a name="p0190183215525"></a><a name="p0190183215525"></a>预热区（40～150℃）</p>
</td>
<td class="cellrowborder" valign="top" width="13.22%" headers="mcps1.2.6.1.2 "><p id="p3190163215524"><a name="p3190163215524"></a><a name="p3190163215524"></a>60～150 s</p>
</td>
<td class="cellrowborder" valign="top" width="14.77%" headers="mcps1.2.6.1.3 "><p id="p21903327521"><a name="p21903327521"></a><a name="p21903327521"></a>≤2.0℃/s</p>
</td>
<td class="cellrowborder" valign="top" width="13.22%" headers="mcps1.2.6.1.4 "><p id="p3190432205217"><a name="p3190432205217"></a><a name="p3190432205217"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="32.35%" headers="mcps1.2.6.1.5 "><p id="p11190832155212"><a name="p11190832155212"></a><a name="p11190832155212"></a>-</p>
</td>
</tr>
<tr id="row8190832135212"><td class="cellrowborder" valign="top" width="26.44%" headers="mcps1.2.6.1.1 "><p id="p81909324526"><a name="p81909324526"></a><a name="p81909324526"></a>均温区（150～200℃）</p>
</td>
<td class="cellrowborder" valign="top" width="13.22%" headers="mcps1.2.6.1.2 "><p id="p619019327528"><a name="p619019327528"></a><a name="p619019327528"></a>60～120 s</p>
</td>
<td class="cellrowborder" valign="top" width="14.77%" headers="mcps1.2.6.1.3 "><p id="p1190143285212"><a name="p1190143285212"></a><a name="p1190143285212"></a>＜1.0℃/s</p>
</td>
<td class="cellrowborder" valign="top" width="13.22%" headers="mcps1.2.6.1.4 "><p id="p18190153245213"><a name="p18190153245213"></a><a name="p18190153245213"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="32.35%" headers="mcps1.2.6.1.5 "><p id="p2190173245210"><a name="p2190173245210"></a><a name="p2190173245210"></a>-</p>
</td>
</tr>
<tr id="row1819063212524"><td class="cellrowborder" valign="top" width="26.44%" headers="mcps1.2.6.1.1 "><p id="p181901532155218"><a name="p181901532155218"></a><a name="p181901532155218"></a>回流区（＞217℃）</p>
</td>
<td class="cellrowborder" valign="top" width="13.22%" headers="mcps1.2.6.1.2 "><p id="p519019328520"><a name="p519019328520"></a><a name="p519019328520"></a>60～90 s</p>
</td>
<td class="cellrowborder" valign="top" width="14.77%" headers="mcps1.2.6.1.3 "><p id="p14191153210523"><a name="p14191153210523"></a><a name="p14191153210523"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="13.22%" headers="mcps1.2.6.1.4 "><p id="p61911832145220"><a name="p61911832145220"></a><a name="p61911832145220"></a>230-260 ℃</p>
</td>
<td class="cellrowborder" valign="top" width="32.35%" headers="mcps1.2.6.1.5 "><p id="p11191232135214"><a name="p11191232135214"></a><a name="p11191232135214"></a>-</p>
</td>
</tr>
<tr id="row519114325526"><td class="cellrowborder" valign="top" width="26.44%" headers="mcps1.2.6.1.1 "><p id="p6191143217527"><a name="p6191143217527"></a><a name="p6191143217527"></a>冷却区（Tmax～180℃）</p>
</td>
<td class="cellrowborder" valign="top" width="13.22%" headers="mcps1.2.6.1.2 "><p id="p119153215213"><a name="p119153215213"></a><a name="p119153215213"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="14.77%" headers="mcps1.2.6.1.3 "><p id="p11191123245220"><a name="p11191123245220"></a><a name="p11191123245220"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="13.22%" headers="mcps1.2.6.1.4 "><p id="p7191103235217"><a name="p7191103235217"></a><a name="p7191103235217"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="32.35%" headers="mcps1.2.6.1.5 "><p id="p121917323525"><a name="p121917323525"></a><a name="p121917323525"></a>1.0℃/s≤Slope≤4.0℃/s</p>
</td>
</tr>
</tbody>
</table>

说明：

-   预热区：温度由40℃～150℃，温度上升速率控制在2℃/s左右，该温区时间为60～150 s。
-   均温区：温度由150℃～200℃，稳定缓慢升温，温度上升速率小于1℃/s，且该区域时间控制在60～120 s**（注意：该区域一定缓慢受热，否则易导致焊接不良）**。
-   回流区：温度由217℃～Tmax～217℃，整个区间时间控制在60～90 s。
-   冷却区：温度由Tmax～180℃，温度下降速率最大不能超过4℃/s。
-   温度从室温25℃升温到250℃时间不应该超过6分钟。
-   该回流焊曲线仅为推荐值，客户端需根据实际生产情况做相应调整。
-   回流时间以60～90 s为目标，对于一些热容较大无法满足时间要求的单板可将回流时间放宽至120s。封装体耐温标准参考IPC/JEDEC J-STD-020D标准，封装体测温方法参考JEP 140标准。

IPC/JEDEC J-STD-020D标准，封装体测温方法按照JEP 140标准要求：IPC/JEDEC 020D中的无铅器件封装体耐温标准如[表2](#table141320324529)所示。

**表 2**  IPC/JEDEC 020D中的无铅器件封装体耐温标准

<a name="table141320324529"></a>
<table><thead align="left"><tr id="row11192133218527"><th class="cellrowborder" valign="top" width="23.25232523252325%" id="mcps1.2.5.1.1"><p id="p1319253212527"><a name="p1319253212527"></a><a name="p1319253212527"></a>Package</p>
<p id="p1519253245216"><a name="p1519253245216"></a><a name="p1519253245216"></a>Thickness</p>
</th>
<th class="cellrowborder" valign="top" width="24.952495249524954%" id="mcps1.2.5.1.2"><p id="p171921532175220"><a name="p171921532175220"></a><a name="p171921532175220"></a>Volume  mm<sup id="sup953901711211"><a name="sup953901711211"></a><a name="sup953901711211"></a>3</sup></p>
<p id="p2192163205214"><a name="p2192163205214"></a><a name="p2192163205214"></a>＜350</p>
</th>
<th class="cellrowborder" valign="top" width="24.952495249524954%" id="mcps1.2.5.1.3"><p id="p219213217521"><a name="p219213217521"></a><a name="p219213217521"></a>Volume  mm<sup id="sup3539417161220"><a name="sup3539417161220"></a><a name="sup3539417161220"></a>3</sup></p>
<p id="p171923323521"><a name="p171923323521"></a><a name="p171923323521"></a>350～2000</p>
</th>
<th class="cellrowborder" valign="top" width="26.842684268426847%" id="mcps1.2.5.1.4"><p id="p1419283218525"><a name="p1419283218525"></a><a name="p1419283218525"></a>Volume  mm<sup id="sup125408172125"><a name="sup125408172125"></a><a name="sup125408172125"></a>3</sup></p>
<p id="p419263225213"><a name="p419263225213"></a><a name="p419263225213"></a>＞2000</p>
</th>
</tr>
</thead>
<tbody><tr id="row171925327523"><td class="cellrowborder" valign="top" width="23.25232523252325%" headers="mcps1.2.5.1.1 "><p id="p13192113235214"><a name="p13192113235214"></a><a name="p13192113235214"></a>＜1.6mm</p>
</td>
<td class="cellrowborder" valign="top" width="24.952495249524954%" headers="mcps1.2.5.1.2 "><p id="p11192123215525"><a name="p11192123215525"></a><a name="p11192123215525"></a>260℃</p>
</td>
<td class="cellrowborder" valign="top" width="24.952495249524954%" headers="mcps1.2.5.1.3 "><p id="p10192632155216"><a name="p10192632155216"></a><a name="p10192632155216"></a>260℃</p>
</td>
<td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.5.1.4 "><p id="p161921232145217"><a name="p161921232145217"></a><a name="p161921232145217"></a>260℃</p>
</td>
</tr>
<tr id="row141928322526"><td class="cellrowborder" valign="top" width="23.25232523252325%" headers="mcps1.2.5.1.1 "><p id="p111923325522"><a name="p111923325522"></a><a name="p111923325522"></a>1.6mm～2.5mm</p>
</td>
<td class="cellrowborder" valign="top" width="24.952495249524954%" headers="mcps1.2.5.1.2 "><p id="p1419219328522"><a name="p1419219328522"></a><a name="p1419219328522"></a>260℃</p>
</td>
<td class="cellrowborder" valign="top" width="24.952495249524954%" headers="mcps1.2.5.1.3 "><p id="p91923328526"><a name="p91923328526"></a><a name="p91923328526"></a>250℃</p>
</td>
<td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.5.1.4 "><p id="p18192203211520"><a name="p18192203211520"></a><a name="p18192203211520"></a>245℃</p>
</td>
</tr>
<tr id="row21921032115218"><td class="cellrowborder" valign="top" width="23.25232523252325%" headers="mcps1.2.5.1.1 "><p id="p12193103211528"><a name="p12193103211528"></a><a name="p12193103211528"></a>＞2.5mm</p>
</td>
<td class="cellrowborder" valign="top" width="24.952495249524954%" headers="mcps1.2.5.1.2 "><p id="p151931632135211"><a name="p151931632135211"></a><a name="p151931632135211"></a>250℃</p>
</td>
<td class="cellrowborder" valign="top" width="24.952495249524954%" headers="mcps1.2.5.1.3 "><p id="p1119319324523"><a name="p1119319324523"></a><a name="p1119319324523"></a>245℃</p>
</td>
<td class="cellrowborder" valign="top" width="26.842684268426847%" headers="mcps1.2.5.1.4 "><p id="p1193153275212"><a name="p1193153275212"></a><a name="p1193153275212"></a>245℃</p>
</td>
</tr>
</tbody>
</table>

体积计算中不计入器件焊端（焊球，引脚）和外部散热片。

回流焊接工艺曲线测量方法：

JEP140推荐：对于厚度较小的器件，测量封装体温度时，直接将热电偶贴放在器件表面，对于厚度较大的器件，在器件表面钻孔埋入热电偶进行测量。由于量化器件厚度的要求，推荐全部采用在封装体表面钻孔埋入热电偶的方式（特别薄器件，无法钻孔除外）。如[图2](#fig51931632205219)所示。

**图 2**  封装体测温示意图<a name="fig51931632205219"></a>  
![](figures/封装体测温示意图.png "封装体测温示意图")

>![](public_sys-resources/icon-note.gif) **说明：** 
>如果是QFP封装的芯片，直接将测温探头放在管脚处即可。

## 混合回流焊工艺参数要求<a name="ZH-CN_TOPIC_0000001456242672"></a>

回流焊接过程中，如果出现器件混装现象，应首先保证无铅器件的正常焊接。具体要求如[表1](#table1143116301540)所示。

**表 1**  混装回流焊工艺参数表

<a name="table1143116301540"></a>
<table><thead align="left"><tr id="row85661306546"><th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.6.1.1"><p id="p12566143075410"><a name="p12566143075410"></a><a name="p12566143075410"></a>数值要求</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.6.1.2"><p id="p0566530175410"><a name="p0566530175410"></a><a name="p0566530175410"></a>有铅BGA</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.6.1.3"><p id="p956612303545"><a name="p956612303545"></a><a name="p956612303545"></a>无铅BGA</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.6.1.4"><p id="p4566133017543"><a name="p4566133017543"></a><a name="p4566133017543"></a>其它器件</p>
</th>
</tr>
</thead>
<tbody><tr id="row7566830145419"><td class="cellrowborder" rowspan="2" valign="top" headers="mcps1.2.6.1.1 "><p id="p19566163019545"><a name="p19566163019545"></a><a name="p19566163019545"></a>预热区（40～150 ℃）</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p165661730175419"><a name="p165661730175419"></a><a name="p165661730175419"></a>时间</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.6.1.2 mcps1.2.6.1.3 mcps1.2.6.1.4 "><p id="p125661030175412"><a name="p125661030175412"></a><a name="p125661030175412"></a>60～150 s</p>
</td>
</tr>
<tr id="row0566123013543"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p7566203085420"><a name="p7566203085420"></a><a name="p7566203085420"></a>升温斜率</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.6.1.2 mcps1.2.6.1.3 mcps1.2.6.1.4 "><p id="p115661530125414"><a name="p115661530125414"></a><a name="p115661530125414"></a>＜2.5℃/s</p>
</td>
</tr>
<tr id="row3566153075419"><td class="cellrowborder" rowspan="2" valign="top" headers="mcps1.2.6.1.1 "><p id="p656693017543"><a name="p656693017543"></a><a name="p656693017543"></a>均温区（150～183 ℃）</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p9567133019547"><a name="p9567133019547"></a><a name="p9567133019547"></a>时间</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.6.1.2 mcps1.2.6.1.3 mcps1.2.6.1.4 "><p id="p1756713307548"><a name="p1756713307548"></a><a name="p1756713307548"></a>30～90 s</p>
</td>
</tr>
<tr id="row1356703065417"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p75671130195414"><a name="p75671130195414"></a><a name="p75671130195414"></a>升温斜率</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.6.1.2 mcps1.2.6.1.3 mcps1.2.6.1.4 "><p id="p656710303542"><a name="p656710303542"></a><a name="p656710303542"></a>＜1.0℃/s</p>
</td>
</tr>
<tr id="row20567123045420"><td class="cellrowborder" rowspan="2" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.1 "><p id="p19567163010545"><a name="p19567163010545"></a><a name="p19567163010545"></a>回流区（＞183 ℃）</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.1 "><p id="p45671930115417"><a name="p45671930115417"></a><a name="p45671930115417"></a>峰值温度</p>
</td>
<td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.6.1.2 "><p id="p556783013542"><a name="p556783013542"></a><a name="p556783013542"></a>210~240 ℃</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.6.1.3 "><p id="p756703015418"><a name="p756703015418"></a><a name="p756703015418"></a>220~240 ℃</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.6.1.4 "><p id="p9567163014542"><a name="p9567163014542"></a><a name="p9567163014542"></a>210~245 ℃</p>
</td>
</tr>
<tr id="row1556803085417"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1456863012540"><a name="p1456863012540"></a><a name="p1456863012540"></a>时间</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p17568203010540"><a name="p17568203010540"></a><a name="p17568203010540"></a>30~120 s</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p65689303544"><a name="p65689303544"></a><a name="p65689303544"></a>60~120 s</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p10568123035415"><a name="p10568123035415"></a><a name="p10568123035415"></a>30~120 s</p>
</td>
</tr>
<tr id="row1568103085411"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p14568163017548"><a name="p14568163017548"></a><a name="p14568163017548"></a>冷却区（Tmax～150 ℃）</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p105686302546"><a name="p105686302546"></a><a name="p105686302546"></a>降温斜率</p>
</td>
<td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.6.1.2 mcps1.2.6.1.3 mcps1.2.6.1.4 "><p id="p756853025411"><a name="p756853025411"></a><a name="p756853025411"></a>1.0℃/s≤Slope≤4.0℃/s</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **说明：** 
>以上工艺参数要求均针对焊点温度。单板上焊点最热点和最冷点均需要满足以上规范要求。

曲线调制中，还需要满足单板上元器件的封装体耐温要求。封装体耐温标准按照IPC/JEDEC J-STD-020D标准，封装体测温方法按照JEP 140标准。

IPC/JEDEC 020D中的有铅器件封装体耐温标准如[表2](#table2471123095420)所示。

**表 2**  IPC/JEDEC 020D中的有铅器件封装体耐温标准

<a name="table2471123095420"></a>
<table><thead align="left"><tr id="row185681930165417"><th class="cellrowborder" valign="top" width="30.246975302469753%" id="mcps1.2.4.1.1"><p id="p65684301544"><a name="p65684301544"></a><a name="p65684301544"></a>Package</p>
<p id="p195681330165419"><a name="p195681330165419"></a><a name="p195681330165419"></a>Thickness</p>
</th>
<th class="cellrowborder" valign="top" width="34.02659734026597%" id="mcps1.2.4.1.2"><p id="p19568163055410"><a name="p19568163055410"></a><a name="p19568163055410"></a>Volume  mm<sup id="sup1993219164169"><a name="sup1993219164169"></a><a name="sup1993219164169"></a>3</sup></p>
<p id="p656817307541"><a name="p656817307541"></a><a name="p656817307541"></a>＜350</p>
</th>
<th class="cellrowborder" valign="top" width="35.72642735726427%" id="mcps1.2.4.1.3"><p id="p12568330175419"><a name="p12568330175419"></a><a name="p12568330175419"></a>Volume  mm<sup id="sup4932216101610"><a name="sup4932216101610"></a><a name="sup4932216101610"></a>3</sup></p>
<p id="p75694307543"><a name="p75694307543"></a><a name="p75694307543"></a>≥350</p>
</th>
</tr>
</thead>
<tbody><tr id="row7569330145418"><td class="cellrowborder" valign="top" width="30.246975302469753%" headers="mcps1.2.4.1.1 "><p id="p15691309544"><a name="p15691309544"></a><a name="p15691309544"></a>＜2.5mm</p>
</td>
<td class="cellrowborder" valign="top" width="34.02659734026597%" headers="mcps1.2.4.1.2 "><p id="p1569430175410"><a name="p1569430175410"></a><a name="p1569430175410"></a>235℃</p>
</td>
<td class="cellrowborder" valign="top" width="35.72642735726427%" headers="mcps1.2.4.1.3 "><p id="p1956912306544"><a name="p1956912306544"></a><a name="p1956912306544"></a>220℃</p>
</td>
</tr>
<tr id="row656910308544"><td class="cellrowborder" valign="top" width="30.246975302469753%" headers="mcps1.2.4.1.1 "><p id="p175691630115411"><a name="p175691630115411"></a><a name="p175691630115411"></a>≥2.5mm</p>
</td>
<td class="cellrowborder" valign="top" width="34.02659734026597%" headers="mcps1.2.4.1.2 "><p id="p1256918305547"><a name="p1256918305547"></a><a name="p1256918305547"></a>220℃</p>
</td>
<td class="cellrowborder" valign="top" width="35.72642735726427%" headers="mcps1.2.4.1.3 "><p id="p13570330105412"><a name="p13570330105412"></a><a name="p13570330105412"></a>220℃</p>
</td>
</tr>
</tbody>
</table>

体积计算中不计入器件焊端（焊球，引脚）和外部散热片。

JEP140标准规定测量封装体温度方法同无铅工艺，请参考[无铅回流焊工艺参数](#ZH-CN_TOPIC_0000001455922828)要求详细说明。

# 潮敏参数<a name="ZH-CN_TOPIC_0000001505722805"></a>

-   **[存放与使用](#ZH-CN_TOPIC_0000001456242656)**  

-   **[重新烘烤](#ZH-CN_TOPIC_0000001505882581)**  

## 存放与使用<a name="ZH-CN_TOPIC_0000001456242656"></a>

**【**使用范围】

所有IC（潮敏产品）的存放和使用。

**【**存放环境】

建议产品真空包装存放，存放温度范围：大于等于-40℃，小于等于150℃。推荐存放在25℃的环境温度下。

**【**存储期限】（shelf life）

存放环境<30°C/60% RH下，真空包装存放，存储期限\(shelf life\)不少于12个月。

**【**车间寿命】（floor life）

在环境条件<30°C/60%下，floor life参照表如[表1](#table1614748174417)所示。

**表 1**  车间寿命（floor life）参照表

<a name="table1614748174417"></a>
<table><thead align="left"><tr id="row18148198134415"><th class="cellrowborder" valign="top" width="14.09%" id="mcps1.2.3.1.1"><p id="p87813359547"><a name="p87813359547"></a><a name="p87813359547"></a>潮湿敏感等级</p>
<p id="p82332247442"><a name="p82332247442"></a><a name="p82332247442"></a>（MSL）</p>
</th>
<th class="cellrowborder" valign="top" width="85.91%" id="mcps1.2.3.1.2"><p id="p1123352404410"><a name="p1123352404410"></a><a name="p1123352404410"></a>含义（即拆分后放存条件及最长时间）</p>
</th>
</tr>
</thead>
<tbody><tr id="row141482814447"><td class="cellrowborder" valign="top" width="14.09%" headers="mcps1.2.3.1.1 "><p id="p1323352410446"><a name="p1323352410446"></a><a name="p1323352410446"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="85.91%" headers="mcps1.2.3.1.2 "><p id="p323442434419"><a name="p323442434419"></a><a name="p323442434419"></a>无限制，环境温湿度≦30℃/85% RH（Relative Humidity）</p>
</td>
</tr>
<tr id="row914819854413"><td class="cellrowborder" valign="top" width="14.09%" headers="mcps1.2.3.1.1 "><p id="p16234102412441"><a name="p16234102412441"></a><a name="p16234102412441"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="85.91%" headers="mcps1.2.3.1.2 "><p id="p1823482484416"><a name="p1823482484416"></a><a name="p1823482484416"></a>1year，30℃/60%RH。</p>
</td>
</tr>
<tr id="row181483819448"><td class="cellrowborder" valign="top" width="14.09%" headers="mcps1.2.3.1.1 "><p id="p1123432444411"><a name="p1123432444411"></a><a name="p1123432444411"></a>2a</p>
</td>
<td class="cellrowborder" valign="top" width="85.91%" headers="mcps1.2.3.1.2 "><p id="p162346244441"><a name="p162346244441"></a><a name="p162346244441"></a>4week，30℃/60%RH。</p>
</td>
</tr>
<tr id="row201488824415"><td class="cellrowborder" valign="top" width="14.09%" headers="mcps1.2.3.1.1 "><p id="p2023412434411"><a name="p2023412434411"></a><a name="p2023412434411"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="85.91%" headers="mcps1.2.3.1.2 "><p id="p2234162494417"><a name="p2234162494417"></a><a name="p2234162494417"></a>1week，30℃/60%RH。</p>
</td>
</tr>
<tr id="row714818894411"><td class="cellrowborder" valign="top" width="14.09%" headers="mcps1.2.3.1.1 "><p id="p15234132417448"><a name="p15234132417448"></a><a name="p15234132417448"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="85.91%" headers="mcps1.2.3.1.2 "><p id="p12472124432318"><a name="p12472124432318"></a><a name="p12472124432318"></a>72h，30℃/60%RH。</p>
</td>
</tr>
<tr id="row114818814444"><td class="cellrowborder" valign="top" width="14.09%" headers="mcps1.2.3.1.1 "><p id="p1423432413448"><a name="p1423432413448"></a><a name="p1423432413448"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="85.91%" headers="mcps1.2.3.1.2 "><p id="p4234132416445"><a name="p4234132416445"></a><a name="p4234132416445"></a>48h，30℃/60%RH。</p>
</td>
</tr>
<tr id="row171490819447"><td class="cellrowborder" valign="top" width="14.09%" headers="mcps1.2.3.1.1 "><p id="p19234112417442"><a name="p19234112417442"></a><a name="p19234112417442"></a>5a</p>
</td>
<td class="cellrowborder" valign="top" width="85.91%" headers="mcps1.2.3.1.2 "><p id="p17235132419444"><a name="p17235132419444"></a><a name="p17235132419444"></a>24h，30℃/60%RH。</p>
</td>
</tr>
<tr id="row5442814124415"><td class="cellrowborder" valign="top" width="14.09%" headers="mcps1.2.3.1.1 "><p id="p152355242446"><a name="p152355242446"></a><a name="p152355242446"></a>6</p>
</td>
<td class="cellrowborder" valign="top" width="85.91%" headers="mcps1.2.3.1.2 "><p id="p623542418448"><a name="p623542418448"></a><a name="p623542418448"></a>Time on Label，30℃/60%RH。</p>
</td>
</tr>
</tbody>
</table>

**【**潮敏产品的使用】

-   产品在≦30℃/60%RH下连续或累计暴露超过2个小时，建议进行重新烘烤后再真空干燥包装。
-   产品在≦30℃/60%RH下暴露累计没有超过2个小时，可以不用重新烘烤，但要更换新的干燥剂，进行真空干燥包装。
-   本产品的潮敏参数等级为3级。

本文没有提到的存储及使用原则，请直接参考JEDEC J-STD-033A。

## 重新烘烤<a name="ZH-CN_TOPIC_0000001505882581"></a>

【适用产品】

所有潮敏产品

【使用范围】

需要重新烘烤的潮敏产品

【重新烘烤参考表】

**表 1**  重新烘烤参考表

<a name="table13529172754517"></a>
<table><thead align="left"><tr id="row105305278453"><th class="cellrowborder" valign="top" width="17.98%" id="mcps1.2.6.1.1"><p id="p848714173462"><a name="p848714173462"></a><a name="p848714173462"></a>芯片厚度</p>
</th>
<th class="cellrowborder" valign="top" width="11.77%" id="mcps1.2.6.1.2"><p id="p94871117144617"><a name="p94871117144617"></a><a name="p94871117144617"></a>MSL潮敏等级</p>
</th>
<th class="cellrowborder" valign="top" width="20.59%" id="mcps1.2.6.1.3"><p id="p134881917184613"><a name="p134881917184613"></a><a name="p134881917184613"></a>烘烤125℃</p>
</th>
<th class="cellrowborder" valign="top" width="25.729999999999997%" id="mcps1.2.6.1.4"><p id="p8488111719462"><a name="p8488111719462"></a><a name="p8488111719462"></a>烘烤90℃/≦5% RH</p>
</th>
<th class="cellrowborder" valign="top" width="23.93%" id="mcps1.2.6.1.5"><p id="p1488717204610"><a name="p1488717204610"></a><a name="p1488717204610"></a>烘烤40℃/≦5% RH</p>
</th>
</tr>
</thead>
<tbody><tr id="row20530127124519"><td class="cellrowborder" rowspan="5" valign="top" width="17.98%" headers="mcps1.2.6.1.1 "><p id="p34888175468"><a name="p34888175468"></a><a name="p34888175468"></a>≤1.4mm</p>
</td>
<td class="cellrowborder" valign="top" width="11.77%" headers="mcps1.2.6.1.2 "><p id="p12488111784617"><a name="p12488111784617"></a><a name="p12488111784617"></a>2a</p>
</td>
<td class="cellrowborder" valign="top" width="20.59%" headers="mcps1.2.6.1.3 "><p id="p17488181717464"><a name="p17488181717464"></a><a name="p17488181717464"></a>3h</p>
</td>
<td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.2.6.1.4 "><p id="p148815172466"><a name="p148815172466"></a><a name="p148815172466"></a>11h</p>
</td>
<td class="cellrowborder" valign="top" width="23.93%" headers="mcps1.2.6.1.5 "><p id="p124891017134619"><a name="p124891017134619"></a><a name="p124891017134619"></a>5day</p>
</td>
</tr>
<tr id="row25313271450"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p10489191724617"><a name="p10489191724617"></a><a name="p10489191724617"></a>3</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1748991715462"><a name="p1748991715462"></a><a name="p1748991715462"></a>7h</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p124891217164610"><a name="p124891217164610"></a><a name="p124891217164610"></a>23h</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p11489141734611"><a name="p11489141734611"></a><a name="p11489141734611"></a>9day</p>
</td>
</tr>
<tr id="row105312027114518"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p648917170465"><a name="p648917170465"></a><a name="p648917170465"></a>4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1348941714462"><a name="p1348941714462"></a><a name="p1348941714462"></a>7h</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p7490101704619"><a name="p7490101704619"></a><a name="p7490101704619"></a>23h</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p1490617124618"><a name="p1490617124618"></a><a name="p1490617124618"></a>9day</p>
</td>
</tr>
<tr id="row17531427144514"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p249018178468"><a name="p249018178468"></a><a name="p249018178468"></a>5</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1749051734614"><a name="p1749051734614"></a><a name="p1749051734614"></a>7h</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p249081711463"><a name="p249081711463"></a><a name="p249081711463"></a>24h</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p9490151719465"><a name="p9490151719465"></a><a name="p9490151719465"></a>10day</p>
</td>
</tr>
<tr id="row753182794516"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1949161711462"><a name="p1949161711462"></a><a name="p1949161711462"></a>5a</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p19491617184612"><a name="p19491617184612"></a><a name="p19491617184612"></a>10h</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1549114172465"><a name="p1549114172465"></a><a name="p1549114172465"></a>24h</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p64911717144611"><a name="p64911717144611"></a><a name="p64911717144611"></a>10day</p>
</td>
</tr>
<tr id="row105326274454"><td class="cellrowborder" rowspan="5" valign="top" width="17.98%" headers="mcps1.2.6.1.1 "><p id="p19491817184614"><a name="p19491817184614"></a><a name="p19491817184614"></a>≤2.0mm</p>
</td>
<td class="cellrowborder" valign="top" width="11.77%" headers="mcps1.2.6.1.2 "><p id="p14491131734613"><a name="p14491131734613"></a><a name="p14491131734613"></a>2a</p>
</td>
<td class="cellrowborder" valign="top" width="20.59%" headers="mcps1.2.6.1.3 "><p id="p84911917134612"><a name="p84911917134612"></a><a name="p84911917134612"></a>16h</p>
</td>
<td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.2.6.1.4 "><p id="p34911117134614"><a name="p34911117134614"></a><a name="p34911117134614"></a>2day</p>
</td>
<td class="cellrowborder" valign="top" width="23.93%" headers="mcps1.2.6.1.5 "><p id="p2491191714468"><a name="p2491191714468"></a><a name="p2491191714468"></a>22day</p>
</td>
</tr>
<tr id="row1853232764518"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p6492101716464"><a name="p6492101716464"></a><a name="p6492101716464"></a>3</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p64921117124615"><a name="p64921117124615"></a><a name="p64921117124615"></a>17h</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p124926179462"><a name="p124926179462"></a><a name="p124926179462"></a>2day</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p8492121714615"><a name="p8492121714615"></a><a name="p8492121714615"></a>23day</p>
</td>
</tr>
<tr id="row0738135174517"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p6493017164617"><a name="p6493017164617"></a><a name="p6493017164617"></a>4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p134931417184612"><a name="p134931417184612"></a><a name="p134931417184612"></a>20h</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p14931217114617"><a name="p14931217114617"></a><a name="p14931217114617"></a>3day</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p1849321724614"><a name="p1849321724614"></a><a name="p1849321724614"></a>28day</p>
</td>
</tr>
<tr id="row1435295244519"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p104935174467"><a name="p104935174467"></a><a name="p104935174467"></a>5</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p12493191711467"><a name="p12493191711467"></a><a name="p12493191711467"></a>25h</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p8493171719461"><a name="p8493171719461"></a><a name="p8493171719461"></a>4day</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p17493141764613"><a name="p17493141764613"></a><a name="p17493141764613"></a>35day</p>
</td>
</tr>
<tr id="row14915152124512"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1493141724610"><a name="p1493141724610"></a><a name="p1493141724610"></a>5a</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1949381714462"><a name="p1949381714462"></a><a name="p1949381714462"></a>40h</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p6494131744611"><a name="p6494131744611"></a><a name="p6494131744611"></a>6day</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p184941717154610"><a name="p184941717154610"></a><a name="p184941717154610"></a>56day</p>
</td>
</tr>
<tr id="row20453175344512"><td class="cellrowborder" rowspan="5" valign="top" width="17.98%" headers="mcps1.2.6.1.1 "><p id="p144941717134619"><a name="p144941717134619"></a><a name="p144941717134619"></a>≤4.5mm</p>
</td>
<td class="cellrowborder" valign="top" width="11.77%" headers="mcps1.2.6.1.2 "><p id="p6494111734614"><a name="p6494111734614"></a><a name="p6494111734614"></a>2a</p>
</td>
<td class="cellrowborder" valign="top" width="20.59%" headers="mcps1.2.6.1.3 "><p id="p74941517184619"><a name="p74941517184619"></a><a name="p74941517184619"></a>48h</p>
</td>
<td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.2.6.1.4 "><p id="p204942175469"><a name="p204942175469"></a><a name="p204942175469"></a>7day</p>
</td>
<td class="cellrowborder" valign="top" width="23.93%" headers="mcps1.2.6.1.5 "><p id="p24941817144611"><a name="p24941817144611"></a><a name="p24941817144611"></a>67day</p>
</td>
</tr>
<tr id="row543115415453"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p14494717164620"><a name="p14494717164620"></a><a name="p14494717164620"></a>3</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p149521711460"><a name="p149521711460"></a><a name="p149521711460"></a>48h</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p13495191774613"><a name="p13495191774613"></a><a name="p13495191774613"></a>8day</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p049531784620"><a name="p049531784620"></a><a name="p049531784620"></a>67day</p>
</td>
</tr>
<tr id="row115461654194514"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p9495517144619"><a name="p9495517144619"></a><a name="p9495517144619"></a>4</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1049571744611"><a name="p1049571744611"></a><a name="p1049571744611"></a>48h</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p204951817154614"><a name="p204951817154614"></a><a name="p204951817154614"></a>10day</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p949531784610"><a name="p949531784610"></a><a name="p949531784610"></a>67day</p>
</td>
</tr>
<tr id="row111221155164515"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p104968173463"><a name="p104968173463"></a><a name="p104968173463"></a>5</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p3496111724619"><a name="p3496111724619"></a><a name="p3496111724619"></a>48h</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1149613177469"><a name="p1149613177469"></a><a name="p1149613177469"></a>10day</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p8496131724610"><a name="p8496131724610"></a><a name="p8496131724610"></a>67day</p>
</td>
</tr>
<tr id="row9649185519456"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p9496111715462"><a name="p9496111715462"></a><a name="p9496111715462"></a>5a</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p15496161724615"><a name="p15496161724615"></a><a name="p15496161724615"></a>48h</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p134961117104618"><a name="p134961117104618"></a><a name="p134961117104618"></a>10day</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p134961717134611"><a name="p134961717134611"></a><a name="p134961717134611"></a>67day</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **说明：** 
>-   此表中显示的均是受潮后，必须的最小的烘烤时间；
>-   重新烘烤优先选择低温烘烤；
>-   详细情况请参考JEDEC。

# 接口时序<a name="ZH-CN_TOPIC_0000001505722825"></a>

-   **[UART接口时序](#ZH-CN_TOPIC_0000001505882549)**  

-   **[I2C时序](#ZH-CN_TOPIC_0000001456082752)**  

-   **[I2S时序](#ZH-CN_TOPIC_0000001455763060)**  

-   **[SDIO时序](#ZH-CN_TOPIC_0000001505882545)**  

-   **[SPI接口时序](#ZH-CN_TOPIC_0000001456242668)**  

## UART接口时序<a name="ZH-CN_TOPIC_0000001505882549"></a>

WS53V100芯片 支持3组UART接口，其中UART\_L0支持两线连接（RXD、TXD），不支持流控模式，UART\_H0和UART\_H1支持四线的协议（RXD、TXD、CTS、RTS），其中RXD和TXD用于数据传送，RTS和CTS用于流控。

UART接口支持多种波特率，波特率大小和传送速率之间成正比关系，支持的波特率从9600bit/s到5Mbit/s，其速率可以通过寄存器进行配置。

UART\_L0支持最大速率2Mbit/s，UART\_H0和UART\_H1支持最大速率5Mbit/s。

波特率和误码率如[表1](#table14102645174016)所示。

**表 1**  UART接口波特率和误码率

<a name="table14102645174016"></a>
<table><thead align="left"><tr id="row41471145204014"><th class="cellrowborder" valign="top" width="33.673367336733676%" id="mcps1.2.4.1.1"><p id="p8147134594012"><a name="p8147134594012"></a><a name="p8147134594012"></a>Desired Rate</p>
</th>
<th class="cellrowborder" valign="top" width="33.673367336733676%" id="mcps1.2.4.1.2"><p id="p1714719457403"><a name="p1714719457403"></a><a name="p1714719457403"></a>Actual Rate</p>
</th>
<th class="cellrowborder" valign="top" width="32.653265326532654%" id="mcps1.2.4.1.3"><p id="p131487455407"><a name="p131487455407"></a><a name="p131487455407"></a>Error（%）</p>
</th>
</tr>
</thead>
<tbody><tr id="row14979840104916"><td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.1 "><p id="p482811417494"><a name="p482811417494"></a><a name="p482811417494"></a>5000000</p>
</td>
<td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p982819414492"><a name="p982819414492"></a><a name="p982819414492"></a>5000000</p>
</td>
<td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.3 "><p id="p11828154174915"><a name="p11828154174915"></a><a name="p11828154174915"></a>0.00</p>
</td>
</tr>
<tr id="row1914814454403"><td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.1 "><p id="p81482455405"><a name="p81482455405"></a><a name="p81482455405"></a>4000000</p>
</td>
<td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p131481445204013"><a name="p131481445204013"></a><a name="p131481445204013"></a>4000000</p>
</td>
<td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.3 "><p id="p514814451402"><a name="p514814451402"></a><a name="p514814451402"></a>0.00</p>
</td>
</tr>
<tr id="row1148134519405"><td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.1 "><p id="p101481645194011"><a name="p101481645194011"></a><a name="p101481645194011"></a>3000000</p>
</td>
<td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p21481045164013"><a name="p21481045164013"></a><a name="p21481045164013"></a>3000000</p>
</td>
<td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.3 "><p id="p151481645204017"><a name="p151481645204017"></a><a name="p151481645204017"></a>0.00</p>
</td>
</tr>
<tr id="row514864524018"><td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.1 "><p id="p7148104517402"><a name="p7148104517402"></a><a name="p7148104517402"></a>2000000</p>
</td>
<td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p3148144544015"><a name="p3148144544015"></a><a name="p3148144544015"></a>2000000</p>
</td>
<td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.3 "><p id="p914854515403"><a name="p914854515403"></a><a name="p914854515403"></a>0.00</p>
</td>
</tr>
<tr id="row1014854517408"><td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.1 "><p id="p10148144512406"><a name="p10148144512406"></a><a name="p10148144512406"></a>1500000</p>
</td>
<td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p1914834574014"><a name="p1914834574014"></a><a name="p1914834574014"></a>1500000</p>
</td>
<td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.3 "><p id="p201481245134010"><a name="p201481245134010"></a><a name="p201481245134010"></a>0.00</p>
</td>
</tr>
<tr id="row91484456403"><td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.1 "><p id="p214819459408"><a name="p214819459408"></a><a name="p214819459408"></a>1444444</p>
</td>
<td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p1114812452404"><a name="p1114812452404"></a><a name="p1114812452404"></a>1454544</p>
</td>
<td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.3 "><p id="p111482045154015"><a name="p111482045154015"></a><a name="p111482045154015"></a>0.70</p>
</td>
</tr>
<tr id="row6148184516402"><td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.1 "><p id="p81481445124015"><a name="p81481445124015"></a><a name="p81481445124015"></a>921600</p>
</td>
<td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p11481945134011"><a name="p11481945134011"></a><a name="p11481945134011"></a>923077</p>
</td>
<td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.3 "><p id="p714819456400"><a name="p714819456400"></a><a name="p714819456400"></a>0.16</p>
</td>
</tr>
<tr id="row11148545164010"><td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.1 "><p id="p714824512402"><a name="p714824512402"></a><a name="p714824512402"></a>460800</p>
</td>
<td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p20148144574015"><a name="p20148144574015"></a><a name="p20148144574015"></a>461538</p>
</td>
<td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.3 "><p id="p2148184511407"><a name="p2148184511407"></a><a name="p2148184511407"></a>0.16</p>
</td>
</tr>
<tr id="row7148845124018"><td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.1 "><p id="p17148154564014"><a name="p17148154564014"></a><a name="p17148154564014"></a>230400</p>
</td>
<td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p3148845174015"><a name="p3148845174015"></a><a name="p3148845174015"></a>230796</p>
</td>
<td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.3 "><p id="p31481345164010"><a name="p31481345164010"></a><a name="p31481345164010"></a>0.17</p>
</td>
</tr>
<tr id="row4148445194012"><td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.1 "><p id="p71481945114018"><a name="p71481945114018"></a><a name="p71481945114018"></a>115200</p>
</td>
<td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p18148545194014"><a name="p18148545194014"></a><a name="p18148545194014"></a>115385</p>
</td>
<td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.3 "><p id="p1148184524015"><a name="p1148184524015"></a><a name="p1148184524015"></a>0.16</p>
</td>
</tr>
<tr id="row1114854516404"><td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.1 "><p id="p1614817456409"><a name="p1614817456409"></a><a name="p1614817456409"></a>57600</p>
</td>
<td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p1814812454400"><a name="p1814812454400"></a><a name="p1814812454400"></a>57692</p>
</td>
<td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.3 "><p id="p13148114554018"><a name="p13148114554018"></a><a name="p13148114554018"></a>0.16</p>
</td>
</tr>
<tr id="row814894511405"><td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.1 "><p id="p1914854544010"><a name="p1914854544010"></a><a name="p1914854544010"></a>38400</p>
</td>
<td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p114814512403"><a name="p114814512403"></a><a name="p114814512403"></a>38400</p>
</td>
<td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.3 "><p id="p1314804520402"><a name="p1314804520402"></a><a name="p1314804520402"></a>0.00</p>
</td>
</tr>
<tr id="row18148194515408"><td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.1 "><p id="p20148174554010"><a name="p20148174554010"></a><a name="p20148174554010"></a>28800</p>
</td>
<td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p19148945194020"><a name="p19148945194020"></a><a name="p19148945194020"></a>28846</p>
</td>
<td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.3 "><p id="p141488454407"><a name="p141488454407"></a><a name="p141488454407"></a>0.16</p>
</td>
</tr>
<tr id="row514824554014"><td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.1 "><p id="p914817456405"><a name="p914817456405"></a><a name="p914817456405"></a>19200</p>
</td>
<td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p10148114515408"><a name="p10148114515408"></a><a name="p10148114515408"></a>19220</p>
</td>
<td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.3 "><p id="p131481145124014"><a name="p131481145124014"></a><a name="p131481145124014"></a>0.00</p>
</td>
</tr>
<tr id="row9148545144011"><td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.1 "><p id="p16148945164015"><a name="p16148945164015"></a><a name="p16148945164015"></a>14400</p>
</td>
<td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p7148194518404"><a name="p7148194518404"></a><a name="p7148194518404"></a>14423</p>
</td>
<td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.3 "><p id="p8148104594018"><a name="p8148104594018"></a><a name="p8148104594018"></a>0.16</p>
</td>
</tr>
<tr id="row161481845134015"><td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.1 "><p id="p1314854513404"><a name="p1314854513404"></a><a name="p1314854513404"></a>9600</p>
</td>
<td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p51484453405"><a name="p51484453405"></a><a name="p51484453405"></a>9600</p>
</td>
<td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.3 "><p id="p16148164511409"><a name="p16148164511409"></a><a name="p16148164511409"></a>0.00</p>
</td>
</tr>
</tbody>
</table>

UART接口的的时序如[图1](#fig170185617418)所示。

**图 1**  UART接口时序图<a name="fig170185617418"></a>  
![](figures/UART接口时序图.png "UART接口时序图")

注：图中虚线的信号上升沿按照0.7×VDD，下降沿按照0.3×VDD选取。VDDIO电压为1.8V/3.3V

其中：

-   标注1为CTS信号拉低到TXD信号有效的最大延时。
-   标注2为结束位的中点到CTS信号拉高需要保持的最大时间。
-   标注3为结束位的中点到RTS信号拉高的最大延时。

UART时序约束如[表2](#table104754234216)所示。

**表 2**  UART时序约束表

<a name="table104754234216"></a>
<table><thead align="left"><tr id="row1583142114218"><th class="cellrowborder" valign="top" width="8.25%" id="mcps1.2.7.1.1"><p id="p188311427428"><a name="p188311427428"></a><a name="p188311427428"></a>Ref No</p>
</th>
<th class="cellrowborder" valign="top" width="31.96%" id="mcps1.2.7.1.2"><p id="p68334213427"><a name="p68334213427"></a><a name="p68334213427"></a>Characteristics</p>
</th>
<th class="cellrowborder" valign="top" width="12.370000000000001%" id="mcps1.2.7.1.3"><p id="p188374234215"><a name="p188374234215"></a><a name="p188374234215"></a>Min.</p>
</th>
<th class="cellrowborder" valign="top" width="13.4%" id="mcps1.2.7.1.4"><p id="p1683942144214"><a name="p1683942144214"></a><a name="p1683942144214"></a>Typical</p>
</th>
<th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.2.7.1.5"><p id="p5831042184213"><a name="p5831042184213"></a><a name="p5831042184213"></a>Max.</p>
</th>
<th class="cellrowborder" valign="top" width="19.59%" id="mcps1.2.7.1.6"><p id="p1083942134215"><a name="p1083942134215"></a><a name="p1083942134215"></a>Unit</p>
</th>
</tr>
</thead>
<tbody><tr id="row1483144264217"><td class="cellrowborder" valign="top" width="8.25%" headers="mcps1.2.7.1.1 "><p id="p783134224212"><a name="p783134224212"></a><a name="p783134224212"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.2 "><p id="p08384264218"><a name="p08384264218"></a><a name="p08384264218"></a>CTS low to TXD valid</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.7.1.3 "><p id="p59190216202"><a name="p59190216202"></a><a name="p59190216202"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="13.4%" headers="mcps1.2.7.1.4 "><p id="p10918162162013"><a name="p10918162162013"></a><a name="p10918162162013"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.7.1.5 "><p id="p49184212207"><a name="p49184212207"></a><a name="p49184212207"></a>1.5</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.7.1.6 "><p id="p083442204219"><a name="p083442204219"></a><a name="p083442204219"></a>Bit Periods</p>
</td>
</tr>
<tr id="row198324214427"><td class="cellrowborder" valign="top" width="8.25%" headers="mcps1.2.7.1.1 "><p id="p28314234213"><a name="p28314234213"></a><a name="p28314234213"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.2 "><p id="p0830424427"><a name="p0830424427"></a><a name="p0830424427"></a>CTS high before mid of stop bit</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.7.1.3 "><p id="p159174282015"><a name="p159174282015"></a><a name="p159174282015"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="13.4%" headers="mcps1.2.7.1.4 "><p id="p19916192192016"><a name="p19916192192016"></a><a name="p19916192192016"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.7.1.5 "><p id="p159159222018"><a name="p159159222018"></a><a name="p159159222018"></a>0.5</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.7.1.6 "><p id="p1383164217428"><a name="p1383164217428"></a><a name="p1383164217428"></a>Bit Periods</p>
</td>
</tr>
<tr id="row1583134217427"><td class="cellrowborder" valign="top" width="8.25%" headers="mcps1.2.7.1.1 "><p id="p7831442144213"><a name="p7831442144213"></a><a name="p7831442144213"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.2 "><p id="p1083164210425"><a name="p1083164210425"></a><a name="p1083164210425"></a>Mid of stop bit to RTS high</p>
</td>
<td class="cellrowborder" valign="top" width="12.370000000000001%" headers="mcps1.2.7.1.3 "><p id="p10914132182019"><a name="p10914132182019"></a><a name="p10914132182019"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="13.4%" headers="mcps1.2.7.1.4 "><p id="p491472142020"><a name="p491472142020"></a><a name="p491472142020"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.7.1.5 "><p id="p59026213202"><a name="p59026213202"></a><a name="p59026213202"></a>0.5</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.7.1.6 "><p id="p584342154216"><a name="p584342154216"></a><a name="p584342154216"></a>Bit Periods</p>
</td>
</tr>
</tbody>
</table>

## I2C时序<a name="ZH-CN_TOPIC_0000001456082752"></a>

I<sup>2</sup>C传输时序如[图1](#toc528421881)所示。

**图 1**  I<sup>2</sup>C传输时序图<a name="toc528421881"></a>  
![](figures/I2C传输时序图.png "I2C传输时序图")

I<sup>2</sup>C接口时序参数如[表1](#table288661152411)所示。

**表 1**  I<sup>2</sup>C接口时序参数表

<a name="table288661152411"></a>
<table><thead align="left"><tr id="row198897115241"><th class="cellrowborder" valign="top" width="18.330000000000002%" id="mcps1.2.10.1.1"><p id="p37717561716"><a name="p37717561716"></a><a name="p37717561716"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="10.930000000000001%" id="mcps1.2.10.1.2"><p id="p4771105161720"><a name="p4771105161720"></a><a name="p4771105161720"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="10.500000000000002%" id="mcps1.2.10.1.3"><p id="p9984633168"><a name="p9984633168"></a><a name="p9984633168"></a>标准模式（最小值）</p>
</th>
<th class="cellrowborder" valign="top" width="9.38%" id="mcps1.2.10.1.4"><p id="p19701112712250"><a name="p19701112712250"></a><a name="p19701112712250"></a>标准模式（最大值）</p>
</th>
<th class="cellrowborder" valign="top" width="9.680000000000001%" id="mcps1.2.10.1.5"><p id="p18721422151617"><a name="p18721422151617"></a><a name="p18721422151617"></a>快速模式（最小值）</p>
</th>
<th class="cellrowborder" valign="top" width="12.270000000000001%" id="mcps1.2.10.1.6"><p id="p1092031551616"><a name="p1092031551616"></a><a name="p1092031551616"></a>快速模式（最大值）</p>
</th>
<th class="cellrowborder" valign="top" width="9.900000000000002%" id="mcps1.2.10.1.7"><p id="p19400643121610"><a name="p19400643121610"></a><a name="p19400643121610"></a>快速+模式（最小值）</p>
</th>
<th class="cellrowborder" valign="top" width="10.500000000000002%" id="mcps1.2.10.1.8"><p id="p38301816161713"><a name="p38301816161713"></a><a name="p38301816161713"></a>快速+模式（最大值）</p>
</th>
<th class="cellrowborder" valign="top" width="8.510000000000002%" id="mcps1.2.10.1.9"><p id="p1556581151719"><a name="p1556581151719"></a><a name="p1556581151719"></a>单位</p>
</th>
</tr>
</thead>
<tbody><tr id="row17990182714242"><td class="cellrowborder" valign="top" width="18.330000000000002%" headers="mcps1.2.10.1.1 "><p id="p187024273255"><a name="p187024273255"></a><a name="p187024273255"></a>SCL时钟频率</p>
</td>
<td class="cellrowborder" valign="top" width="10.930000000000001%" headers="mcps1.2.10.1.2 "><p id="p17021627152518"><a name="p17021627152518"></a><a name="p17021627152518"></a>f<sub id="sub63661524181414"><a name="sub63661524181414"></a><a name="sub63661524181414"></a>SCL</sub></p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.3 "><p id="p34374310181"><a name="p34374310181"></a><a name="p34374310181"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.38%" headers="mcps1.2.10.1.4 "><p id="p14436831181815"><a name="p14436831181815"></a><a name="p14436831181815"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="9.680000000000001%" headers="mcps1.2.10.1.5 "><p id="p143533131818"><a name="p143533131818"></a><a name="p143533131818"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12.270000000000001%" headers="mcps1.2.10.1.6 "><p id="p1143410317185"><a name="p1143410317185"></a><a name="p1143410317185"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9.900000000000002%" headers="mcps1.2.10.1.7 "><p id="p973917573515"><a name="p973917573515"></a><a name="p973917573515"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.8 "><p id="p697013095215"><a name="p697013095215"></a><a name="p697013095215"></a>1000</p>
</td>
<td class="cellrowborder" valign="top" width="8.510000000000002%" headers="mcps1.2.10.1.9 "><p id="p1870213278250"><a name="p1870213278250"></a><a name="p1870213278250"></a>kHz</p>
</td>
</tr>
<tr id="row759052862410"><td class="cellrowborder" valign="top" width="18.330000000000002%" headers="mcps1.2.10.1.1 "><p id="p12702192716259"><a name="p12702192716259"></a><a name="p12702192716259"></a>启动保持时间</p>
</td>
<td class="cellrowborder" valign="top" width="10.930000000000001%" headers="mcps1.2.10.1.2 "><p id="p1770213276258"><a name="p1770213276258"></a><a name="p1770213276258"></a>t<sub id="sub43669246141"><a name="sub43669246141"></a><a name="sub43669246141"></a>HD;STA</sub></p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.3 "><p id="p134348311182"><a name="p134348311182"></a><a name="p134348311182"></a>4.0</p>
</td>
<td class="cellrowborder" valign="top" width="9.38%" headers="mcps1.2.10.1.4 "><p id="p11433113114187"><a name="p11433113114187"></a><a name="p11433113114187"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.680000000000001%" headers="mcps1.2.10.1.5 "><p id="p943263101818"><a name="p943263101818"></a><a name="p943263101818"></a>0.6</p>
</td>
<td class="cellrowborder" valign="top" width="12.270000000000001%" headers="mcps1.2.10.1.6 "><p id="p124318313184"><a name="p124318313184"></a><a name="p124318313184"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.900000000000002%" headers="mcps1.2.10.1.7 "><p id="p1673945713515"><a name="p1673945713515"></a><a name="p1673945713515"></a>0.26</p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.8 "><p id="p1597017017524"><a name="p1597017017524"></a><a name="p1597017017524"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.510000000000002%" headers="mcps1.2.10.1.9 "><p id="p17702132742510"><a name="p17702132742510"></a><a name="p17702132742510"></a>μs</p>
</td>
</tr>
<tr id="row1811462952412"><td class="cellrowborder" valign="top" width="18.330000000000002%" headers="mcps1.2.10.1.1 "><p id="p670252711254"><a name="p670252711254"></a><a name="p670252711254"></a>SCL低电平周期</p>
</td>
<td class="cellrowborder" valign="top" width="10.930000000000001%" headers="mcps1.2.10.1.2 "><p id="p070319272251"><a name="p070319272251"></a><a name="p070319272251"></a>t<sub id="sub163672024101411"><a name="sub163672024101411"></a><a name="sub163672024101411"></a>LOW</sub></p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.3 "><p id="p108253021511"><a name="p108253021511"></a><a name="p108253021511"></a>4.7</p>
</td>
<td class="cellrowborder" valign="top" width="9.38%" headers="mcps1.2.10.1.4 "><p id="p12811830181516"><a name="p12811830181516"></a><a name="p12811830181516"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.680000000000001%" headers="mcps1.2.10.1.5 "><p id="p1805302158"><a name="p1805302158"></a><a name="p1805302158"></a>1.3</p>
</td>
<td class="cellrowborder" valign="top" width="12.270000000000001%" headers="mcps1.2.10.1.6 "><p id="p9808309152"><a name="p9808309152"></a><a name="p9808309152"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.900000000000002%" headers="mcps1.2.10.1.7 "><p id="p19739557105114"><a name="p19739557105114"></a><a name="p19739557105114"></a>0.5</p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.8 "><p id="p1197040115212"><a name="p1197040115212"></a><a name="p1197040115212"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.510000000000002%" headers="mcps1.2.10.1.9 "><p id="p207035279254"><a name="p207035279254"></a><a name="p207035279254"></a>μs</p>
</td>
</tr>
<tr id="row1069012292248"><td class="cellrowborder" valign="top" width="18.330000000000002%" headers="mcps1.2.10.1.1 "><p id="p2703172718252"><a name="p2703172718252"></a><a name="p2703172718252"></a>SCL高电平周期</p>
</td>
<td class="cellrowborder" valign="top" width="10.930000000000001%" headers="mcps1.2.10.1.2 "><p id="p2703182772514"><a name="p2703182772514"></a><a name="p2703182772514"></a>t<sub id="sub113671324181410"><a name="sub113671324181410"></a><a name="sub113671324181410"></a>HIGH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.3 "><p id="p479113061511"><a name="p479113061511"></a><a name="p479113061511"></a>4.0</p>
</td>
<td class="cellrowborder" valign="top" width="9.38%" headers="mcps1.2.10.1.4 "><p id="p1478153041517"><a name="p1478153041517"></a><a name="p1478153041517"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.680000000000001%" headers="mcps1.2.10.1.5 "><p id="p778133018152"><a name="p778133018152"></a><a name="p778133018152"></a>0.6</p>
</td>
<td class="cellrowborder" valign="top" width="12.270000000000001%" headers="mcps1.2.10.1.6 "><p id="p37719309154"><a name="p37719309154"></a><a name="p37719309154"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.900000000000002%" headers="mcps1.2.10.1.7 "><p id="p273955745112"><a name="p273955745112"></a><a name="p273955745112"></a>0.26</p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.8 "><p id="p59708045214"><a name="p59708045214"></a><a name="p59708045214"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.510000000000002%" headers="mcps1.2.10.1.9 "><p id="p270312712512"><a name="p270312712512"></a><a name="p270312712512"></a>μs</p>
</td>
</tr>
<tr id="row5298830112413"><td class="cellrowborder" valign="top" width="18.330000000000002%" headers="mcps1.2.10.1.1 "><p id="p17037274254"><a name="p17037274254"></a><a name="p17037274254"></a>启动建立时间</p>
</td>
<td class="cellrowborder" valign="top" width="10.930000000000001%" headers="mcps1.2.10.1.2 "><p id="p15703182782519"><a name="p15703182782519"></a><a name="p15703182782519"></a>t<sub id="sub636772441419"><a name="sub636772441419"></a><a name="sub636772441419"></a>SU;STA</sub></p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.3 "><p id="p107743031516"><a name="p107743031516"></a><a name="p107743031516"></a>4.7</p>
</td>
<td class="cellrowborder" valign="top" width="9.38%" headers="mcps1.2.10.1.4 "><p id="p137653017152"><a name="p137653017152"></a><a name="p137653017152"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.680000000000001%" headers="mcps1.2.10.1.5 "><p id="p775153014151"><a name="p775153014151"></a><a name="p775153014151"></a>0.6</p>
</td>
<td class="cellrowborder" valign="top" width="12.270000000000001%" headers="mcps1.2.10.1.6 "><p id="p137516302158"><a name="p137516302158"></a><a name="p137516302158"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.900000000000002%" headers="mcps1.2.10.1.7 "><p id="p207398576517"><a name="p207398576517"></a><a name="p207398576517"></a>0.26</p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.8 "><p id="p16970140205218"><a name="p16970140205218"></a><a name="p16970140205218"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.510000000000002%" headers="mcps1.2.10.1.9 "><p id="p970422712510"><a name="p970422712510"></a><a name="p970422712510"></a>μs</p>
</td>
</tr>
<tr id="row384243052420"><td class="cellrowborder" valign="top" width="18.330000000000002%" headers="mcps1.2.10.1.1 "><p id="p17704132713253"><a name="p17704132713253"></a><a name="p17704132713253"></a>数据保持时间</p>
</td>
<td class="cellrowborder" valign="top" width="10.930000000000001%" headers="mcps1.2.10.1.2 "><p id="p1570416270253"><a name="p1570416270253"></a><a name="p1570416270253"></a>t<sub id="sub636852421411"><a name="sub636852421411"></a><a name="sub636852421411"></a>HD;DAT</sub></p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.3 "><p id="p1874113001513"><a name="p1874113001513"></a><a name="p1874113001513"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="9.38%" headers="mcps1.2.10.1.4 "><p id="p7738301154"><a name="p7738301154"></a><a name="p7738301154"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.680000000000001%" headers="mcps1.2.10.1.5 "><p id="p67323081516"><a name="p67323081516"></a><a name="p67323081516"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="12.270000000000001%" headers="mcps1.2.10.1.6 "><p id="p18723309151"><a name="p18723309151"></a><a name="p18723309151"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.900000000000002%" headers="mcps1.2.10.1.7 "><p id="p1973919579515"><a name="p1973919579515"></a><a name="p1973919579515"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.8 "><p id="p20970103521"><a name="p20970103521"></a><a name="p20970103521"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.510000000000002%" headers="mcps1.2.10.1.9 "><p id="p1970462715255"><a name="p1970462715255"></a><a name="p1970462715255"></a>μs</p>
</td>
</tr>
<tr id="row3466231192416"><td class="cellrowborder" valign="top" width="18.330000000000002%" headers="mcps1.2.10.1.1 "><p id="p47042027112510"><a name="p47042027112510"></a><a name="p47042027112510"></a>数据建立时间</p>
</td>
<td class="cellrowborder" valign="top" width="10.930000000000001%" headers="mcps1.2.10.1.2 "><p id="p14704202717250"><a name="p14704202717250"></a><a name="p14704202717250"></a>t<sub id="sub1236872414144"><a name="sub1236872414144"></a><a name="sub1236872414144"></a>SU;DAT</sub></p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.3 "><p id="p1771183061514"><a name="p1771183061514"></a><a name="p1771183061514"></a>250</p>
</td>
<td class="cellrowborder" valign="top" width="9.38%" headers="mcps1.2.10.1.4 "><p id="p19714307153"><a name="p19714307153"></a><a name="p19714307153"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.680000000000001%" headers="mcps1.2.10.1.5 "><p id="p1701230101510"><a name="p1701230101510"></a><a name="p1701230101510"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="12.270000000000001%" headers="mcps1.2.10.1.6 "><p id="p14691130121510"><a name="p14691130121510"></a><a name="p14691130121510"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.900000000000002%" headers="mcps1.2.10.1.7 "><p id="p17391157155116"><a name="p17391157155116"></a><a name="p17391157155116"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.8 "><p id="p49701403525"><a name="p49701403525"></a><a name="p49701403525"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.510000000000002%" headers="mcps1.2.10.1.9 "><p id="p17705142719257"><a name="p17705142719257"></a><a name="p17705142719257"></a>ns</p>
</td>
</tr>
<tr id="row1743143216248"><td class="cellrowborder" valign="top" width="18.330000000000002%" headers="mcps1.2.10.1.1 "><p id="p137052027152518"><a name="p137052027152518"></a><a name="p137052027152518"></a>SDA、SCL上升时间</p>
</td>
<td class="cellrowborder" valign="top" width="10.930000000000001%" headers="mcps1.2.10.1.2 "><p id="p137051527122520"><a name="p137051527122520"></a><a name="p137051527122520"></a>t<sub id="sub336817244141"><a name="sub336817244141"></a><a name="sub336817244141"></a>r</sub></p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.3 "><p id="p206914308156"><a name="p206914308156"></a><a name="p206914308156"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.38%" headers="mcps1.2.10.1.4 "><p id="p768123061511"><a name="p768123061511"></a><a name="p768123061511"></a>1000</p>
</td>
<td class="cellrowborder" valign="top" width="9.680000000000001%" headers="mcps1.2.10.1.5 "><p id="p367930151516"><a name="p367930151516"></a><a name="p367930151516"></a>20+0.1C<sub id="sub236822491418"><a name="sub236822491418"></a><a name="sub236822491418"></a>b</sub></p>
</td>
<td class="cellrowborder" valign="top" width="12.270000000000001%" headers="mcps1.2.10.1.6 "><p id="p1167173013155"><a name="p1167173013155"></a><a name="p1167173013155"></a>300</p>
</td>
<td class="cellrowborder" valign="top" width="9.900000000000002%" headers="mcps1.2.10.1.7 "><p id="p19739155719514"><a name="p19739155719514"></a><a name="p19739155719514"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.8 "><p id="p29701902521"><a name="p29701902521"></a><a name="p29701902521"></a>120</p>
</td>
<td class="cellrowborder" valign="top" width="8.510000000000002%" headers="mcps1.2.10.1.9 "><p id="p177051627122514"><a name="p177051627122514"></a><a name="p177051627122514"></a>ns</p>
</td>
</tr>
<tr id="row108904192416"><td class="cellrowborder" valign="top" width="18.330000000000002%" headers="mcps1.2.10.1.1 "><p id="p18705027122519"><a name="p18705027122519"></a><a name="p18705027122519"></a>SDA、SCL下降时间</p>
</td>
<td class="cellrowborder" valign="top" width="10.930000000000001%" headers="mcps1.2.10.1.2 "><p id="p9705192772511"><a name="p9705192772511"></a><a name="p9705192772511"></a>t<sub id="sub3368624111415"><a name="sub3368624111415"></a><a name="sub3368624111415"></a>f</sub></p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.3 "><p id="p146615306159"><a name="p146615306159"></a><a name="p146615306159"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.38%" headers="mcps1.2.10.1.4 "><p id="p10653306157"><a name="p10653306157"></a><a name="p10653306157"></a>300</p>
</td>
<td class="cellrowborder" valign="top" width="9.680000000000001%" headers="mcps1.2.10.1.5 "><p id="p19655304156"><a name="p19655304156"></a><a name="p19655304156"></a>20+0.1C<sub id="sub1436972491411"><a name="sub1436972491411"></a><a name="sub1436972491411"></a>b</sub></p>
</td>
<td class="cellrowborder" valign="top" width="12.270000000000001%" headers="mcps1.2.10.1.6 "><p id="p13646303150"><a name="p13646303150"></a><a name="p13646303150"></a>300</p>
</td>
<td class="cellrowborder" valign="top" width="9.900000000000002%" headers="mcps1.2.10.1.7 "><p id="p6740165725113"><a name="p6740165725113"></a><a name="p6740165725113"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.8 "><p id="p99704015526"><a name="p99704015526"></a><a name="p99704015526"></a>120</p>
</td>
<td class="cellrowborder" valign="top" width="8.510000000000002%" headers="mcps1.2.10.1.9 "><p id="p5706427132517"><a name="p5706427132517"></a><a name="p5706427132517"></a>ns</p>
</td>
</tr>
<tr id="row18912011247"><td class="cellrowborder" valign="top" width="18.330000000000002%" headers="mcps1.2.10.1.1 "><p id="p20706102782513"><a name="p20706102782513"></a><a name="p20706102782513"></a>结束建立时间</p>
</td>
<td class="cellrowborder" valign="top" width="10.930000000000001%" headers="mcps1.2.10.1.2 "><p id="p170672719258"><a name="p170672719258"></a><a name="p170672719258"></a>t<sub id="sub183694243148"><a name="sub183694243148"></a><a name="sub183694243148"></a>SU;STO</sub></p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.3 "><p id="p1463230111518"><a name="p1463230111518"></a><a name="p1463230111518"></a>4.0</p>
</td>
<td class="cellrowborder" valign="top" width="9.38%" headers="mcps1.2.10.1.4 "><p id="p463113019159"><a name="p463113019159"></a><a name="p463113019159"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.680000000000001%" headers="mcps1.2.10.1.5 "><p id="p2628302158"><a name="p2628302158"></a><a name="p2628302158"></a>0.6</p>
</td>
<td class="cellrowborder" valign="top" width="12.270000000000001%" headers="mcps1.2.10.1.6 "><p id="p10628301156"><a name="p10628301156"></a><a name="p10628301156"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.900000000000002%" headers="mcps1.2.10.1.7 "><p id="p3740105718513"><a name="p3740105718513"></a><a name="p3740105718513"></a>0.26</p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.8 "><p id="p13970507524"><a name="p13970507524"></a><a name="p13970507524"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.510000000000002%" headers="mcps1.2.10.1.9 "><p id="p19706182762519"><a name="p19706182762519"></a><a name="p19706182762519"></a>μs</p>
</td>
</tr>
<tr id="row12891181152416"><td class="cellrowborder" valign="top" width="18.330000000000002%" headers="mcps1.2.10.1.1 "><p id="p14706132742514"><a name="p14706132742514"></a><a name="p14706132742514"></a>开始与结束之间的总线释放时间</p>
</td>
<td class="cellrowborder" valign="top" width="10.930000000000001%" headers="mcps1.2.10.1.2 "><p id="p5706132782516"><a name="p5706132782516"></a><a name="p5706132782516"></a>t<sub id="sub4369624181420"><a name="sub4369624181420"></a><a name="sub4369624181420"></a>BUF</sub></p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.3 "><p id="p16183051511"><a name="p16183051511"></a><a name="p16183051511"></a>4.7</p>
</td>
<td class="cellrowborder" valign="top" width="9.38%" headers="mcps1.2.10.1.4 "><p id="p1560330141514"><a name="p1560330141514"></a><a name="p1560330141514"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.680000000000001%" headers="mcps1.2.10.1.5 "><p id="p1060103020156"><a name="p1060103020156"></a><a name="p1060103020156"></a>1.3</p>
</td>
<td class="cellrowborder" valign="top" width="12.270000000000001%" headers="mcps1.2.10.1.6 "><p id="p11596306153"><a name="p11596306153"></a><a name="p11596306153"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.900000000000002%" headers="mcps1.2.10.1.7 "><p id="p474085725112"><a name="p474085725112"></a><a name="p474085725112"></a>0.5</p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.8 "><p id="p297010075210"><a name="p297010075210"></a><a name="p297010075210"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.510000000000002%" headers="mcps1.2.10.1.9 "><p id="p1870662722515"><a name="p1870662722515"></a><a name="p1870662722515"></a>μs</p>
</td>
</tr>
<tr id="row148928115249"><td class="cellrowborder" valign="top" width="18.330000000000002%" headers="mcps1.2.10.1.1 "><p id="p47071927102513"><a name="p47071927102513"></a><a name="p47071927102513"></a>总线负载</p>
</td>
<td class="cellrowborder" valign="top" width="10.930000000000001%" headers="mcps1.2.10.1.2 "><p id="p18707182711250"><a name="p18707182711250"></a><a name="p18707182711250"></a>C<sub id="sub5369152410144"><a name="sub5369152410144"></a><a name="sub5369152410144"></a>b</sub></p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.3 "><p id="p1658133019159"><a name="p1658133019159"></a><a name="p1658133019159"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.38%" headers="mcps1.2.10.1.4 "><p id="p14571230201513"><a name="p14571230201513"></a><a name="p14571230201513"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9.680000000000001%" headers="mcps1.2.10.1.5 "><p id="p145713013152"><a name="p145713013152"></a><a name="p145713013152"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="12.270000000000001%" headers="mcps1.2.10.1.6 "><p id="p15623010153"><a name="p15623010153"></a><a name="p15623010153"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9.900000000000002%" headers="mcps1.2.10.1.7 "><p id="p4740557115115"><a name="p4740557115115"></a><a name="p4740557115115"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.8 "><p id="p497019055219"><a name="p497019055219"></a><a name="p497019055219"></a>550</p>
</td>
<td class="cellrowborder" valign="top" width="8.510000000000002%" headers="mcps1.2.10.1.9 "><p id="p19707627142511"><a name="p19707627142511"></a><a name="p19707627142511"></a>pF</p>
</td>
</tr>
<tr id="row78929142412"><td class="cellrowborder" valign="top" width="18.330000000000002%" headers="mcps1.2.10.1.1 "><p id="p9707827162516"><a name="p9707827162516"></a><a name="p9707827162516"></a>低电平噪声容限</p>
</td>
<td class="cellrowborder" valign="top" width="10.930000000000001%" headers="mcps1.2.10.1.2 "><p id="p8707142712514"><a name="p8707142712514"></a><a name="p8707142712514"></a>V<sub id="sub1537082410145"><a name="sub1537082410145"></a><a name="sub1537082410145"></a>nL</sub></p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.3 "><p id="p135503010153"><a name="p135503010153"></a><a name="p135503010153"></a>0.1V<sub id="sub163701924181415"><a name="sub163701924181415"></a><a name="sub163701924181415"></a>DD</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.38%" headers="mcps1.2.10.1.4 "><p id="p55515300156"><a name="p55515300156"></a><a name="p55515300156"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.680000000000001%" headers="mcps1.2.10.1.5 "><p id="p554130131514"><a name="p554130131514"></a><a name="p554130131514"></a>0.1V<sub id="sub1370924121411"><a name="sub1370924121411"></a><a name="sub1370924121411"></a>DD</sub></p>
</td>
<td class="cellrowborder" valign="top" width="12.270000000000001%" headers="mcps1.2.10.1.6 "><p id="p1153530151519"><a name="p1153530151519"></a><a name="p1153530151519"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.900000000000002%" headers="mcps1.2.10.1.7 "><p id="p1374065713512"><a name="p1374065713512"></a><a name="p1374065713512"></a>0.1V<sub id="sub0754121161318"><a name="sub0754121161318"></a><a name="sub0754121161318"></a>DD</sub></p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.8 "><p id="p149708025213"><a name="p149708025213"></a><a name="p149708025213"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.510000000000002%" headers="mcps1.2.10.1.9 "><p id="p1670832772514"><a name="p1670832772514"></a><a name="p1670832772514"></a>V</p>
</td>
</tr>
<tr id="row13893171202412"><td class="cellrowborder" valign="top" width="18.330000000000002%" headers="mcps1.2.10.1.1 "><p id="p7708202722510"><a name="p7708202722510"></a><a name="p7708202722510"></a>高电平噪声容限</p>
</td>
<td class="cellrowborder" valign="top" width="10.930000000000001%" headers="mcps1.2.10.1.2 "><p id="p1170882712254"><a name="p1170882712254"></a><a name="p1170882712254"></a>V<sub id="sub17370102491417"><a name="sub17370102491417"></a><a name="sub17370102491417"></a>nH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.3 "><p id="p853113013158"><a name="p853113013158"></a><a name="p853113013158"></a>0.2V<sub id="sub1537042411147"><a name="sub1537042411147"></a><a name="sub1537042411147"></a>DD</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.38%" headers="mcps1.2.10.1.4 "><p id="p752113071510"><a name="p752113071510"></a><a name="p752113071510"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.680000000000001%" headers="mcps1.2.10.1.5 "><p id="p15117301158"><a name="p15117301158"></a><a name="p15117301158"></a>0.2V<sub id="sub15370724121418"><a name="sub15370724121418"></a><a name="sub15370724121418"></a>DD</sub></p>
</td>
<td class="cellrowborder" valign="top" width="12.270000000000001%" headers="mcps1.2.10.1.6 "><p id="p114018303154"><a name="p114018303154"></a><a name="p114018303154"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.900000000000002%" headers="mcps1.2.10.1.7 "><p id="p10740175775120"><a name="p10740175775120"></a><a name="p10740175775120"></a>0.2V<sub id="sub8755132114134"><a name="sub8755132114134"></a><a name="sub8755132114134"></a>DD</sub></p>
</td>
<td class="cellrowborder" valign="top" width="10.500000000000002%" headers="mcps1.2.10.1.8 "><p id="p11970120105213"><a name="p11970120105213"></a><a name="p11970120105213"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="8.510000000000002%" headers="mcps1.2.10.1.9 "><p id="p7708527162511"><a name="p7708527162511"></a><a name="p7708527162511"></a>V</p>
</td>
</tr>
</tbody>
</table>

## I2S时序<a name="ZH-CN_TOPIC_0000001455763060"></a>

I2S接口支持Master模式，支持Slave模式。I2S的时序图如[图1](#fig161821713162418)所示。

**图 1**  I2S接口时序<a name="fig161821713162418"></a>  
![](figures/I2S接口时序.png "I2S接口时序")

注：图中虚线的信号上升沿按照0.7×VDD，下降沿按照0.3×VDD选取。VDDIO默认l电压为1.8V/3.3V。

图中I2S\_DI、I2S\_DO表示从自身角度而言的输入/输出端口。

上图中的参数定义：

-   tclk：I2S接口时钟的一个周期时间。
-   tw：I2S接口时钟一个周期内的高电平或者低电平时间。
-   tis：输入信号的建立时间，即输入数据在时钟采样前需要的稳定时间。
-   tih：输入的保持时间，即输入数据在时钟采样后需要的保持不变的时间。
-   top：输出信号的输出传输时间。

I2S作为Master的接口时序约束如[表1](#table85071843112515)所示。

**表 1**  I2S的master时序约束

<a name="table85071843112515"></a>
<table><thead align="left"><tr id="row3548543112511"><th class="cellrowborder" valign="top" width="10.311031103110311%" id="mcps1.2.7.1.1"><p id="p454834311254"><a name="p454834311254"></a><a name="p454834311254"></a>Symbol</p>
</th>
<th class="cellrowborder" valign="top" width="21.332133213321335%" id="mcps1.2.7.1.2"><p id="p254811435258"><a name="p254811435258"></a><a name="p254811435258"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.051205120512053%" id="mcps1.2.7.1.3"><p id="p354814313254"><a name="p354814313254"></a><a name="p354814313254"></a>Condition</p>
</th>
<th class="cellrowborder" valign="top" width="24.702470247024706%" id="mcps1.2.7.1.4"><p id="p5548104318252"><a name="p5548104318252"></a><a name="p5548104318252"></a>Min</p>
</th>
<th class="cellrowborder" valign="top" width="23.292329232923294%" id="mcps1.2.7.1.5"><p id="p25481143122513"><a name="p25481143122513"></a><a name="p25481143122513"></a>Max</p>
</th>
<th class="cellrowborder" valign="top" width="8.310831083108312%" id="mcps1.2.7.1.6"><p id="p1548543112514"><a name="p1548543112514"></a><a name="p1548543112514"></a>Unit</p>
</th>
</tr>
</thead>
<tbody><tr id="row175481343152514"><td class="cellrowborder" valign="top" width="10.311031103110311%" headers="mcps1.2.7.1.1 "><p id="p854894372519"><a name="p854894372519"></a><a name="p854894372519"></a>t<sub id="sub179613261147"><a name="sub179613261147"></a><a name="sub179613261147"></a>clk</sub></p>
</td>
<td class="cellrowborder" valign="top" width="21.332133213321335%" headers="mcps1.2.7.1.2 "><p id="p35481043192517"><a name="p35481043192517"></a><a name="p35481043192517"></a>Cycle time</p>
</td>
<td class="cellrowborder" valign="top" width="12.051205120512053%" headers="mcps1.2.7.1.3 "><p id="p6548144362519"><a name="p6548144362519"></a><a name="p6548144362519"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="24.702470247024706%" headers="mcps1.2.7.1.4 "><p id="p1454844315256"><a name="p1454844315256"></a><a name="p1454844315256"></a>100@1.1V</p>
<p id="p20996159205313"><a name="p20996159205313"></a><a name="p20996159205313"></a>125@1.0V</p>
</td>
<td class="cellrowborder" valign="top" width="23.292329232923294%" headers="mcps1.2.7.1.5 "><p id="p15548043102510"><a name="p15548043102510"></a><a name="p15548043102510"></a>-</p>
</td>
<td class="cellrowborder" rowspan="6" valign="top" width="8.310831083108312%" headers="mcps1.2.7.1.6 "><p id="p145484434258"><a name="p145484434258"></a><a name="p145484434258"></a>ns</p>
</td>
</tr>
<tr id="row12548154332514"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p13548144319251"><a name="p13548144319251"></a><a name="p13548144319251"></a>t<sub id="sub37961226111414"><a name="sub37961226111414"></a><a name="sub37961226111414"></a>w</sub></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p205481543142516"><a name="p205481543142516"></a><a name="p205481543142516"></a>pulse width</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1954815438258"><a name="p1954815438258"></a><a name="p1954815438258"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p3404413161613"><a name="p3404413161613"></a><a name="p3404413161613"></a>0.45×t<sub id="sub107969261143"><a name="sub107969261143"></a><a name="sub107969261143"></a>clk</sub></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p34031813201616"><a name="p34031813201616"></a><a name="p34031813201616"></a>0.55×t<sub id="sub679662631419"><a name="sub679662631419"></a><a name="sub679662631419"></a>clk</sub></p>
</td>
</tr>
<tr id="row1254814318254"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p45481043192519"><a name="p45481043192519"></a><a name="p45481043192519"></a>t<sub id="sub1279792681411"><a name="sub1279792681411"></a><a name="sub1279792681411"></a>is</sub></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p4548174312255"><a name="p4548174312255"></a><a name="p4548174312255"></a>I2S_DI setup time</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p19548843182515"><a name="p19548843182515"></a><a name="p19548843182515"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p768792824811"><a name="p768792824811"></a><a name="p768792824811"></a>25.74ns    @1.1V</p>
<p id="p1261515373510"><a name="p1261515373510"></a><a name="p1261515373510"></a>35.86ns    @1.0V</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p8402151391611"><a name="p8402151391611"></a><a name="p8402151391611"></a>-</p>
</td>
</tr>
<tr id="row1454817439253"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p14548243132514"><a name="p14548243132514"></a><a name="p14548243132514"></a>t<sub id="sub19797182641413"><a name="sub19797182641413"></a><a name="sub19797182641413"></a>ih</sub></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p145481843122511"><a name="p145481843122511"></a><a name="p145481843122511"></a>I2S_DI hold time</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p15548443152512"><a name="p15548443152512"></a><a name="p15548443152512"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p14674837463"><a name="p14674837463"></a><a name="p14674837463"></a>0</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p74011613131619"><a name="p74011613131619"></a><a name="p74011613131619"></a>-</p>
</td>
</tr>
<tr id="row17548043182516"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p4548943202518"><a name="p4548943202518"></a><a name="p4548943202518"></a>t<sub id="sub97971226171416"><a name="sub97971226171416"></a><a name="sub97971226171416"></a>op</sub></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1854884312517"><a name="p1854884312517"></a><a name="p1854884312517"></a>I2S_DO propagation time</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1554834332514"><a name="p1554834332514"></a><a name="p1554834332514"></a>10 pF load</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p142971581650"><a name="p142971581650"></a><a name="p142971581650"></a>0.05</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p15141192617519"><a name="p15141192617519"></a><a name="p15141192617519"></a>10.25ns @1.1V</p>
<p id="p126112815215"><a name="p126112815215"></a><a name="p126112815215"></a>18.82ns @1.0V</p>
</td>
</tr>
<tr id="row754864317256"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p5548154392512"><a name="p5548154392512"></a><a name="p5548154392512"></a>t<sub id="sub480012618147"><a name="sub480012618147"></a><a name="sub480012618147"></a>op</sub></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p105485437256"><a name="p105485437256"></a><a name="p105485437256"></a>I2S_WS propagation time</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p5548164392520"><a name="p5548164392520"></a><a name="p5548164392520"></a>10 pF load</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p8399613131614"><a name="p8399613131614"></a><a name="p8399613131614"></a>0.05</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p3809111081217"><a name="p3809111081217"></a><a name="p3809111081217"></a>10.25ns @1.1V</p>
<p id="p20809210151212"><a name="p20809210151212"></a><a name="p20809210151212"></a>18.82ns @1.0V</p>
</td>
</tr>
</tbody>
</table>

I2S作为Slave的接口时序约束如[表2](#table4251121502713)所示。

**表 2**  I2S的slave时序约束

<a name="table4251121502713"></a>
<table><thead align="left"><tr id="row10290121516277"><th class="cellrowborder" valign="top" width="11.341134113411341%" id="mcps1.2.7.1.1"><p id="p52902015102717"><a name="p52902015102717"></a><a name="p52902015102717"></a>Symbol</p>
</th>
<th class="cellrowborder" valign="top" width="20.54205420542054%" id="mcps1.2.7.1.2"><p id="p429013158277"><a name="p429013158277"></a><a name="p429013158277"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.681168116811682%" id="mcps1.2.7.1.3"><p id="p1929091516271"><a name="p1929091516271"></a><a name="p1929091516271"></a>Condition</p>
</th>
<th class="cellrowborder" valign="top" width="26.422642264226422%" id="mcps1.2.7.1.4"><p id="p8290111562710"><a name="p8290111562710"></a><a name="p8290111562710"></a>Min</p>
</th>
<th class="cellrowborder" valign="top" width="21.33213321332133%" id="mcps1.2.7.1.5"><p id="p1829081514275"><a name="p1829081514275"></a><a name="p1829081514275"></a>Max</p>
</th>
<th class="cellrowborder" valign="top" width="8.680868086808681%" id="mcps1.2.7.1.6"><p id="p12904154276"><a name="p12904154276"></a><a name="p12904154276"></a>Unit</p>
</th>
</tr>
</thead>
<tbody><tr id="row529011592714"><td class="cellrowborder" valign="top" width="11.341134113411341%" headers="mcps1.2.7.1.1 "><p id="p12290115112715"><a name="p12290115112715"></a><a name="p12290115112715"></a>t<sub id="sub168004262146"><a name="sub168004262146"></a><a name="sub168004262146"></a>clk</sub></p>
</td>
<td class="cellrowborder" valign="top" width="20.54205420542054%" headers="mcps1.2.7.1.2 "><p id="p729015157274"><a name="p729015157274"></a><a name="p729015157274"></a>Cycle time</p>
</td>
<td class="cellrowborder" valign="top" width="11.681168116811682%" headers="mcps1.2.7.1.3 "><p id="p112901415142716"><a name="p112901415142716"></a><a name="p112901415142716"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="26.422642264226422%" headers="mcps1.2.7.1.4 "><p id="p20856133265310"><a name="p20856133265310"></a><a name="p20856133265310"></a>100@1.1V</p>
<p id="p13856732115313"><a name="p13856732115313"></a><a name="p13856732115313"></a>125@1.0V</p>
</td>
<td class="cellrowborder" valign="top" width="21.33213321332133%" headers="mcps1.2.7.1.5 "><p id="p75617165177"><a name="p75617165177"></a><a name="p75617165177"></a>-</p>
</td>
<td class="cellrowborder" rowspan="7" valign="top" width="8.680868086808681%" headers="mcps1.2.7.1.6 "><p id="p129081532715"><a name="p129081532715"></a><a name="p129081532715"></a>ns</p>
</td>
</tr>
<tr id="row7290715132711"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p2029071582718"><a name="p2029071582718"></a><a name="p2029071582718"></a>t<sub id="sub18801122681410"><a name="sub18801122681410"></a><a name="sub18801122681410"></a>w</sub></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1629121552718"><a name="p1629121552718"></a><a name="p1629121552718"></a>pulse width</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p329131532720"><a name="p329131532720"></a><a name="p329131532720"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1756011651710"><a name="p1756011651710"></a><a name="p1756011651710"></a>0.45×t<sub id="sub1180182671417"><a name="sub1180182671417"></a><a name="sub1180182671417"></a>CLK</sub></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p05602167174"><a name="p05602167174"></a><a name="p05602167174"></a>0.55×t<sub id="sub980162601420"><a name="sub980162601420"></a><a name="sub980162601420"></a>CLK</sub></p>
</td>
</tr>
<tr id="row8291161517270"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p13291415192716"><a name="p13291415192716"></a><a name="p13291415192716"></a>t<sub id="sub19801112661417"><a name="sub19801112661417"></a><a name="sub19801112661417"></a>is</sub></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p1629171522716"><a name="p1629171522716"></a><a name="p1629171522716"></a>I2S_DI setup time</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p8291115182711"><a name="p8291115182711"></a><a name="p8291115182711"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p6527145152118"><a name="p6527145152118"></a><a name="p6527145152118"></a>20.14ns  @1.1V</p>
<p id="p195561741105810"><a name="p195561741105810"></a><a name="p195561741105810"></a>28.98ns @1.0V</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p1355811611172"><a name="p1355811611172"></a><a name="p1355811611172"></a>-</p>
</td>
</tr>
<tr id="row15291101542718"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p1229161513274"><a name="p1229161513274"></a><a name="p1229161513274"></a>t<sub id="sub12801132691420"><a name="sub12801132691420"></a><a name="sub12801132691420"></a>ih</sub></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p129151512717"><a name="p129151512717"></a><a name="p129151512717"></a>I2S_DI hold time</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p52911815102714"><a name="p52911815102714"></a><a name="p52911815102714"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p5993164742414"><a name="p5993164742414"></a><a name="p5993164742414"></a>0</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 ">&nbsp;&nbsp;</td>
</tr>
<tr id="row6291111517274"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p152911615142713"><a name="p152911615142713"></a><a name="p152911615142713"></a>t<sub id="sub4802192619147"><a name="sub4802192619147"></a><a name="sub4802192619147"></a>is</sub></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p2291161512713"><a name="p2291161512713"></a><a name="p2291161512713"></a>I2S_WS setup time</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p1291615122717"><a name="p1291615122717"></a><a name="p1291615122717"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p1140104501311"><a name="p1140104501311"></a><a name="p1140104501311"></a>20.14ns  @1.1V</p>
<p id="p9140045171317"><a name="p9140045171317"></a><a name="p9140045171317"></a>28.98ns @1.0V</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p35561916131712"><a name="p35561916131712"></a><a name="p35561916131712"></a>-</p>
</td>
</tr>
<tr id="row14291515122719"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p20291151513274"><a name="p20291151513274"></a><a name="p20291151513274"></a>t<sub id="sub480211266148"><a name="sub480211266148"></a><a name="sub480211266148"></a>ih</sub></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p7291715122718"><a name="p7291715122718"></a><a name="p7291715122718"></a>I2S_WS hold time</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p15291115102714"><a name="p15291115102714"></a><a name="p15291115102714"></a>-</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p476275320138"><a name="p476275320138"></a><a name="p476275320138"></a>0</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 ">&nbsp;&nbsp;</td>
</tr>
<tr id="row52911815152714"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="p142913153273"><a name="p142913153273"></a><a name="p142913153273"></a>t<sub id="sub280202681411"><a name="sub280202681411"></a><a name="sub280202681411"></a>op</sub></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="p18291121542711"><a name="p18291121542711"></a><a name="p18291121542711"></a>I2S_DO propagation time</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p13151632113617"><a name="p13151632113617"></a><a name="p13151632113617"></a>10 pF load</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p194839582132"><a name="p194839582132"></a><a name="p194839582132"></a>0.05</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="p165333383252"><a name="p165333383252"></a><a name="p165333383252"></a>25.08ns @1.1V</p>
<p id="p77421651407"><a name="p77421651407"></a><a name="p77421651407"></a>37.86ns @1.0V</p>
</td>
</tr>
</tbody>
</table>

## SDIO时序<a name="ZH-CN_TOPIC_0000001505882545"></a>

WS53V100的SIDO固定充当device，SDIO支持3种SDIO工作模式：

在CLDO为1.1V时、最大接口速度为50MHz。

-   Default speed模式（DS）

    接口时钟频率最高25MHz，包括1bit和4bit两种模式。

-   High speed模式（HS）

    接口时钟频率最高50MHz。

-   SDR25模式

    接口时钟最高频率50MHz。

    >![](public_sys-resources/icon-notice.gif) **须知：** 
    >对接host芯片的CLK约束：为了保证SDIO的正常工作，需要host持续提供SDIO CLK，并且没有时钟中断，否则可能导致SDIO业务数据异常。

**Default speed模式<a name="section19379164312112"></a>**

Default speed模式为SDIO上电之后的默认模式，为了与各种HOST器件保持兼容性，此模式要求的工作速率较低，时钟只支持到25MHz，对时钟的要求如[表1](#table177553920324)所示。

**表 1**  Default speed模式时钟参数表 （VDDIO=3.3V）

<a name="table177553920324"></a>
<table><thead align="left"><tr id="row1777633913324"><th class="cellrowborder" valign="top" width="31.96%" id="mcps1.2.7.1.1"><p id="p207761939113218"><a name="p207761939113218"></a><a name="p207761939113218"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="10.31%" id="mcps1.2.7.1.2"><p id="p77761139163212"><a name="p77761139163212"></a><a name="p77761139163212"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="9.55%" id="mcps1.2.7.1.3"><p id="p1877663913210"><a name="p1877663913210"></a><a name="p1877663913210"></a>最小值</p>
</th>
<th class="cellrowborder" valign="top" width="10.36%" id="mcps1.2.7.1.4"><p id="p6241749144913"><a name="p6241749144913"></a><a name="p6241749144913"></a>最大值</p>
</th>
<th class="cellrowborder" valign="top" width="9.31%" id="mcps1.2.7.1.5"><p id="p209571752194920"><a name="p209571752194920"></a><a name="p209571752194920"></a>单位</p>
</th>
<th class="cellrowborder" valign="top" width="28.51%" id="mcps1.2.7.1.6"><p id="p477613910324"><a name="p477613910324"></a><a name="p477613910324"></a>备注</p>
</th>
</tr>
</thead>
<tbody><tr id="row677623923220"><td class="cellrowborder" colspan="6" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.1.2 mcps1.2.7.1.3 mcps1.2.7.1.4 mcps1.2.7.1.5 mcps1.2.7.1.6 "><p id="p660011219488"><a name="p660011219488"></a><a name="p660011219488"></a>Clock CLK（All value are referred to min(V<sub id="sub8645629191410"><a name="sub8645629191410"></a><a name="sub8645629191410"></a>IH</sub>) and max(V<sub id="sub146451729161414"><a name="sub146451729161414"></a><a name="sub146451729161414"></a>IL</sub>)）</p>
</td>
</tr>
<tr id="row86261946144713"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p1062710460477"><a name="p1062710460477"></a><a name="p1062710460477"></a>Clock frequency Date Transfer Mode</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p10627946184714"><a name="p10627946184714"></a><a name="p10627946184714"></a>f<sub id="sub1564502919145"><a name="sub1564502919145"></a><a name="sub1564502919145"></a>PP</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p13627154617472"><a name="p13627154617472"></a><a name="p13627154617472"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p202415498494"><a name="p202415498494"></a><a name="p202415498494"></a>25</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p189561752154916"><a name="p189561752154916"></a><a name="p189561752154916"></a>MHz</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p14627164611477"><a name="p14627164611477"></a><a name="p14627164611477"></a>C<sub id="sub19646029181419"><a name="sub19646029181419"></a><a name="sub19646029181419"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row197761839143214"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p377610392324"><a name="p377610392324"></a><a name="p377610392324"></a>Clock frequency Identification Mode</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p13776939163211"><a name="p13776939163211"></a><a name="p13776939163211"></a>f<sub id="sub186467299144"><a name="sub186467299144"></a><a name="sub186467299144"></a>OD</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p1677623916328"><a name="p1677623916328"></a><a name="p1677623916328"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p52403491494"><a name="p52403491494"></a><a name="p52403491494"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p395695219492"><a name="p395695219492"></a><a name="p395695219492"></a>KHz</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p1860812159503"><a name="p1860812159503"></a><a name="p1860812159503"></a>C<sub id="sub3646329151414"><a name="sub3646329151414"></a><a name="sub3646329151414"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row12776183913328"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p97761839123216"><a name="p97761839123216"></a><a name="p97761839123216"></a>Clock low time</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p16776113917324"><a name="p16776113917324"></a><a name="p16776113917324"></a>t<sub id="sub26464295146"><a name="sub26464295146"></a><a name="sub26464295146"></a>WL</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p877611397325"><a name="p877611397325"></a><a name="p877611397325"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p1523904918496"><a name="p1523904918496"></a><a name="p1523904918496"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p16954165210499"><a name="p16954165210499"></a><a name="p16954165210499"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p186081615105019"><a name="p186081615105019"></a><a name="p186081615105019"></a>C<sub id="sub464662901419"><a name="sub464662901419"></a><a name="sub464662901419"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row8588122754716"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p105881277477"><a name="p105881277477"></a><a name="p105881277477"></a>Clock high time</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p1058819279472"><a name="p1058819279472"></a><a name="p1058819279472"></a>t<sub id="sub10646429101412"><a name="sub10646429101412"></a><a name="sub10646429101412"></a>WH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p958862744712"><a name="p958862744712"></a><a name="p958862744712"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p10239349104913"><a name="p10239349104913"></a><a name="p10239349104913"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p11953185218491"><a name="p11953185218491"></a><a name="p11953185218491"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p11588027154720"><a name="p11588027154720"></a><a name="p11588027154720"></a>C<sub id="sub664614299145"><a name="sub664614299145"></a><a name="sub664614299145"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row9588327144718"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p8588152719472"><a name="p8588152719472"></a><a name="p8588152719472"></a>Clock rise time</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p19588132715475"><a name="p19588132715475"></a><a name="p19588132715475"></a>t<sub id="sub10646629121417"><a name="sub10646629121417"></a><a name="sub10646629121417"></a>TLH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p20588182764715"><a name="p20588182764715"></a><a name="p20588182764715"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p16238649184916"><a name="p16238649184916"></a><a name="p16238649184916"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p19528528495"><a name="p19528528495"></a><a name="p19528528495"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p058813274479"><a name="p058813274479"></a><a name="p058813274479"></a>C<sub id="sub19646229191410"><a name="sub19646229191410"></a><a name="sub19646229191410"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row75881827174715"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p9589172734714"><a name="p9589172734714"></a><a name="p9589172734714"></a>Clock fall time</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p658982718474"><a name="p658982718474"></a><a name="p658982718474"></a>t<sub id="sub1764742941415"><a name="sub1764742941415"></a><a name="sub1764742941415"></a>THL</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p958952720479"><a name="p958952720479"></a><a name="p958952720479"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p10227164954919"><a name="p10227164954919"></a><a name="p10227164954919"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p295115217494"><a name="p295115217494"></a><a name="p295115217494"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p14589427124716"><a name="p14589427124716"></a><a name="p14589427124716"></a>C<sub id="sub11647929101416"><a name="sub11647929101416"></a><a name="sub11647929101416"></a>CARD</sub>≤10pF</p>
</td>
</tr>
</tbody>
</table>

Default speed模式输入数据时序如[图1](#fig109983594569)所示。其中，tISU为建立时间，即此模式下SDIO接口要求的数据在时钟采样前的稳定时间，tIH为保持时间，即此模式下SDIO接口要求的数据在时钟采样后的保持原电平的时间。

**图 1**  Default speed模式输入时序<a name="fig109983594569"></a>  

![](figures/zh-cn_image_0000001456082788.png)

Default speed模式输出数据时序如[图2](#fig5952450155817)所示。其中，tODLY（max）为输出数据相对于时钟上升沿，出现在接口上的最大时延，tODLY（min）为输出数据相对于时钟上升沿，出现在接口上的最小时延。

**图 2**  Default speed模式输出时序<a name="fig5952450155817"></a>  

![](figures/zh-cn_image_0000001455763124.png)

Default speed模式的时序约束如[表2](#table792495118592)所示。

**表 2**  Default speed模式时序约束表

<a name="table792495118592"></a>
<table><thead align="left"><tr id="row392513517594"><th class="cellrowborder" valign="top" width="31.96%" id="mcps1.2.7.1.1"><p id="p79254516591"><a name="p79254516591"></a><a name="p79254516591"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="10.31%" id="mcps1.2.7.1.2"><p id="p4925155115917"><a name="p4925155115917"></a><a name="p4925155115917"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="9.55%" id="mcps1.2.7.1.3"><p id="p12925125195914"><a name="p12925125195914"></a><a name="p12925125195914"></a>最小值</p>
</th>
<th class="cellrowborder" valign="top" width="10.36%" id="mcps1.2.7.1.4"><p id="p892520515593"><a name="p892520515593"></a><a name="p892520515593"></a>最大值</p>
</th>
<th class="cellrowborder" valign="top" width="9.31%" id="mcps1.2.7.1.5"><p id="p12925165105917"><a name="p12925165105917"></a><a name="p12925165105917"></a>单位</p>
</th>
<th class="cellrowborder" valign="top" width="28.51%" id="mcps1.2.7.1.6"><p id="p1392565117599"><a name="p1392565117599"></a><a name="p1392565117599"></a>备注</p>
</th>
</tr>
</thead>
<tbody><tr id="row29251518599"><td class="cellrowborder" colspan="6" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.1.2 mcps1.2.7.1.3 mcps1.2.7.1.4 mcps1.2.7.1.5 mcps1.2.7.1.6 "><p id="p2092555175919"><a name="p2092555175919"></a><a name="p2092555175919"></a>Inputs CMD, DAT（referred to CLK）</p>
</td>
</tr>
<tr id="row89251951205918"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p136981749407"><a name="p136981749407"></a><a name="p136981749407"></a>Input set-up time</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p176981741318"><a name="p176981741318"></a><a name="p176981741318"></a>t<sub id="sub3649929181414"><a name="sub3649929181414"></a><a name="sub3649929181414"></a>ISU</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p1064410103294"><a name="p1064410103294"></a><a name="p1064410103294"></a>5ns@1.1V</p>
<p id="p168627972313"><a name="p168627972313"></a><a name="p168627972313"></a>7ns@1.0V</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p89254518597"><a name="p89254518597"></a><a name="p89254518597"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p15925185118599"><a name="p15925185118599"></a><a name="p15925185118599"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p199255514597"><a name="p199255514597"></a><a name="p199255514597"></a>C<sub id="sub66509295147"><a name="sub66509295147"></a><a name="sub66509295147"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row19925251135910"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p3697849209"><a name="p3697849209"></a><a name="p3697849209"></a>Input hold time</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p5698543116"><a name="p5698543116"></a><a name="p5698543116"></a>t<sub id="sub10650142951411"><a name="sub10650142951411"></a><a name="sub10650142951411"></a>IH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p59250516597"><a name="p59250516597"></a><a name="p59250516597"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p1992518515599"><a name="p1992518515599"></a><a name="p1992518515599"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p1992515105910"><a name="p1992515105910"></a><a name="p1992515105910"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p18925185116599"><a name="p18925185116599"></a><a name="p18925185116599"></a>C<sub id="sub1665072916146"><a name="sub1665072916146"></a><a name="sub1665072916146"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row692575135913"><td class="cellrowborder" colspan="6" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.1.2 mcps1.2.7.1.3 mcps1.2.7.1.4 mcps1.2.7.1.5 mcps1.2.7.1.6 "><p id="p1720516231111"><a name="p1720516231111"></a><a name="p1720516231111"></a>Outputs CMD, DAT(referenced to CLK)</p>
</td>
</tr>
<tr id="row149251251115910"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p1069611491300"><a name="p1069611491300"></a><a name="p1069611491300"></a>Output Delay time during Data Transfer Mode</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p1869504515"><a name="p1869504515"></a><a name="p1869504515"></a>t<sub id="sub176509296143"><a name="sub176509296143"></a><a name="sub176509296143"></a>ODLY</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p1392555125916"><a name="p1392555125916"></a><a name="p1392555125916"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p20255122272515"><a name="p20255122272515"></a><a name="p20255122272515"></a>14ns@1.1V</p>
<p id="p1225592216259"><a name="p1225592216259"></a><a name="p1225592216259"></a>17ns@1.0V</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p1792512512598"><a name="p1792512512598"></a><a name="p1792512512598"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p10925115113596"><a name="p10925115113596"></a><a name="p10925115113596"></a>C<sub id="sub10650162919140"><a name="sub10650162919140"></a><a name="sub10650162919140"></a>L</sub>≤40pF</p>
</td>
</tr>
<tr id="row17925185125917"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p4696144913017"><a name="p4696144913017"></a><a name="p4696144913017"></a>Output Delay time during Identification Mode</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p2693114418"><a name="p2693114418"></a><a name="p2693114418"></a>t<sub id="sub1565052910140"><a name="sub1565052910140"></a><a name="sub1565052910140"></a>ODLY</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p892505185915"><a name="p892505185915"></a><a name="p892505185915"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p18925651135920"><a name="p18925651135920"></a><a name="p18925651135920"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p1925135118593"><a name="p1925135118593"></a><a name="p1925135118593"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p199261851135913"><a name="p199261851135913"></a><a name="p199261851135913"></a>C<sub id="sub5650132915142"><a name="sub5650132915142"></a><a name="sub5650132915142"></a>L</sub>≤40pF</p>
</td>
</tr>
</tbody>
</table>

说明：T<sub>clk</sub>为SDIO CLOCK时钟周期。

**High speed模式<a name="section156584181537"></a>**

High speed模式为SDIO上电经过初始化之后，为了使用更高的速率，通过模式切换而进入的模式，此模式要求的工作速率比default speed模式高，其时钟支持到50MHz，对时钟的约束见[表3](#table10852122958)所示。

**表 3**  High speed模式时钟参数表 （VDDIO=3.3V）

<a name="table10852122958"></a>
<table><thead align="left"><tr id="row38531521513"><th class="cellrowborder" valign="top" width="31.919999999999998%" id="mcps1.2.7.1.1"><p id="p13853102557"><a name="p13853102557"></a><a name="p13853102557"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="10.34%" id="mcps1.2.7.1.2"><p id="p585319212513"><a name="p585319212513"></a><a name="p585319212513"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="9.56%" id="mcps1.2.7.1.3"><p id="p58537217514"><a name="p58537217514"></a><a name="p58537217514"></a>最小值</p>
</th>
<th class="cellrowborder" valign="top" width="10.36%" id="mcps1.2.7.1.4"><p id="p1585342158"><a name="p1585342158"></a><a name="p1585342158"></a>最大值</p>
</th>
<th class="cellrowborder" valign="top" width="9.31%" id="mcps1.2.7.1.5"><p id="p28531421055"><a name="p28531421055"></a><a name="p28531421055"></a>单位</p>
</th>
<th class="cellrowborder" valign="top" width="28.51%" id="mcps1.2.7.1.6"><p id="p6853521550"><a name="p6853521550"></a><a name="p6853521550"></a>备注</p>
</th>
</tr>
</thead>
<tbody><tr id="row128537218515"><td class="cellrowborder" colspan="6" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.1.2 mcps1.2.7.1.3 mcps1.2.7.1.4 mcps1.2.7.1.5 mcps1.2.7.1.6 "><p id="p5853526515"><a name="p5853526515"></a><a name="p5853526515"></a>Clock CLK（All value are referred to min(V<sub id="sub1565132971417"><a name="sub1565132971417"></a><a name="sub1565132971417"></a>IH</sub>) and max(V<sub id="sub206511299147"><a name="sub206511299147"></a><a name="sub206511299147"></a>IL</sub>)）</p>
</td>
</tr>
<tr id="row178531521655"><td class="cellrowborder" valign="top" width="31.919999999999998%" headers="mcps1.2.7.1.1 "><p id="p38531421557"><a name="p38531421557"></a><a name="p38531421557"></a>Clock frequency Date Transfer Mode</p>
</td>
<td class="cellrowborder" valign="top" width="10.34%" headers="mcps1.2.7.1.2 "><p id="p885352259"><a name="p885352259"></a><a name="p885352259"></a>f<sub id="sub1651162920147"><a name="sub1651162920147"></a><a name="sub1651162920147"></a>PP</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.56%" headers="mcps1.2.7.1.3 "><p id="p88531921256"><a name="p88531921256"></a><a name="p88531921256"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p4853825513"><a name="p4853825513"></a><a name="p4853825513"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p1885352956"><a name="p1885352956"></a><a name="p1885352956"></a>MHz</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p18853152756"><a name="p18853152756"></a><a name="p18853152756"></a>C<sub id="sub26511129161419"><a name="sub26511129161419"></a><a name="sub26511129161419"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row17853122552"><td class="cellrowborder" valign="top" width="31.919999999999998%" headers="mcps1.2.7.1.1 "><p id="p58533215511"><a name="p58533215511"></a><a name="p58533215511"></a>Clock low time</p>
</td>
<td class="cellrowborder" valign="top" width="10.34%" headers="mcps1.2.7.1.2 "><p id="p16853192558"><a name="p16853192558"></a><a name="p16853192558"></a>t<sub id="sub56511829191417"><a name="sub56511829191417"></a><a name="sub56511829191417"></a>WL</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.56%" headers="mcps1.2.7.1.3 "><p id="p9853926514"><a name="p9853926514"></a><a name="p9853926514"></a>7</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p0853921953"><a name="p0853921953"></a><a name="p0853921953"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p6853221520"><a name="p6853221520"></a><a name="p6853221520"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p185320210513"><a name="p185320210513"></a><a name="p185320210513"></a>C<sub id="sub86515297146"><a name="sub86515297146"></a><a name="sub86515297146"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row158531522518"><td class="cellrowborder" valign="top" width="31.919999999999998%" headers="mcps1.2.7.1.1 "><p id="p4853132855"><a name="p4853132855"></a><a name="p4853132855"></a>Clock high time</p>
</td>
<td class="cellrowborder" valign="top" width="10.34%" headers="mcps1.2.7.1.2 "><p id="p168531422520"><a name="p168531422520"></a><a name="p168531422520"></a>t<sub id="sub156511729121417"><a name="sub156511729121417"></a><a name="sub156511729121417"></a>WH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.56%" headers="mcps1.2.7.1.3 "><p id="p118531721513"><a name="p118531721513"></a><a name="p118531721513"></a>7</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p38537216511"><a name="p38537216511"></a><a name="p38537216511"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p38531425516"><a name="p38531425516"></a><a name="p38531425516"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p17853132256"><a name="p17853132256"></a><a name="p17853132256"></a>C<sub id="sub13651429141415"><a name="sub13651429141415"></a><a name="sub13651429141415"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row58531025518"><td class="cellrowborder" valign="top" width="31.919999999999998%" headers="mcps1.2.7.1.1 "><p id="p48531021157"><a name="p48531021157"></a><a name="p48531021157"></a>Clock rise time</p>
</td>
<td class="cellrowborder" valign="top" width="10.34%" headers="mcps1.2.7.1.2 "><p id="p0853521515"><a name="p0853521515"></a><a name="p0853521515"></a>t<sub id="sub1565110295141"><a name="sub1565110295141"></a><a name="sub1565110295141"></a>TLH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.56%" headers="mcps1.2.7.1.3 "><p id="p178531923516"><a name="p178531923516"></a><a name="p178531923516"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p6853821520"><a name="p6853821520"></a><a name="p6853821520"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p178532214511"><a name="p178532214511"></a><a name="p178532214511"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p5853102959"><a name="p5853102959"></a><a name="p5853102959"></a>C<sub id="sub5652122912146"><a name="sub5652122912146"></a><a name="sub5652122912146"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row108531022516"><td class="cellrowborder" valign="top" width="31.919999999999998%" headers="mcps1.2.7.1.1 "><p id="p9853721150"><a name="p9853721150"></a><a name="p9853721150"></a>Clock fall time</p>
</td>
<td class="cellrowborder" valign="top" width="10.34%" headers="mcps1.2.7.1.2 "><p id="p1853112356"><a name="p1853112356"></a><a name="p1853112356"></a>t<sub id="sub15652182961417"><a name="sub15652182961417"></a><a name="sub15652182961417"></a>THL</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.56%" headers="mcps1.2.7.1.3 "><p id="p785311217516"><a name="p785311217516"></a><a name="p785311217516"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p208541621253"><a name="p208541621253"></a><a name="p208541621253"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p158541022056"><a name="p158541022056"></a><a name="p158541022056"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p14854142751"><a name="p14854142751"></a><a name="p14854142751"></a>C<sub id="sub16528292141"><a name="sub16528292141"></a><a name="sub16528292141"></a>CARD</sub>≤10pF</p>
</td>
</tr>
</tbody>
</table>

High speed模式输入数据时序如[图3](#fig128551821657)所示。其中，tISU为建立时间，即此模式下SDIO接口要求的数据在时钟采样前的稳定时间，tIH为保持时间，即此模式下SDIO接口要求的数据在时钟采样后的保持原电平的时间。

**图 3**  High speed模式输入时序<a name="fig128551821657"></a>  

![](figures/zh-cn_image_0000001505722869.png)

High speed模式输出数据时序如[图4](#fig148558215512)所示。其中，tODLY（max）为输出数据相对于时钟上升沿，出现在接口上的最大时延，tOH为输出数据相对于时钟上升沿，出现在接口上的最小时延。

**图 4**  High speed模式输出时序<a name="fig148558215512"></a>  

![](figures/zh-cn_image_0000001455763128.png)

High speed模式的时序约束如[表4](#table138551211514)所示。

**表 4**  High speed模式时序约束表 \(VDDIO=3.3V\)

<a name="table138551211514"></a>
<table><thead align="left"><tr id="row15855112459"><th class="cellrowborder" valign="top" width="31.96%" id="mcps1.2.7.1.1"><p id="p1085582652"><a name="p1085582652"></a><a name="p1085582652"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="10.31%" id="mcps1.2.7.1.2"><p id="p1585515218512"><a name="p1585515218512"></a><a name="p1585515218512"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="9.55%" id="mcps1.2.7.1.3"><p id="p17855321518"><a name="p17855321518"></a><a name="p17855321518"></a>最小值</p>
</th>
<th class="cellrowborder" valign="top" width="10.35%" id="mcps1.2.7.1.4"><p id="p38551421459"><a name="p38551421459"></a><a name="p38551421459"></a>最大值</p>
</th>
<th class="cellrowborder" valign="top" width="9.32%" id="mcps1.2.7.1.5"><p id="p1985513210519"><a name="p1985513210519"></a><a name="p1985513210519"></a>单位</p>
</th>
<th class="cellrowborder" valign="top" width="28.51%" id="mcps1.2.7.1.6"><p id="p148552021353"><a name="p148552021353"></a><a name="p148552021353"></a>备注</p>
</th>
</tr>
</thead>
<tbody><tr id="row198550213518"><td class="cellrowborder" colspan="6" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.1.2 mcps1.2.7.1.3 mcps1.2.7.1.4 mcps1.2.7.1.5 mcps1.2.7.1.6 "><p id="p5855828516"><a name="p5855828516"></a><a name="p5855828516"></a>Inputs CMD, DAT（referred to CLK）</p>
</td>
</tr>
<tr id="row78551211518"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p685514218512"><a name="p685514218512"></a><a name="p685514218512"></a>Input set-up time</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p16855722512"><a name="p16855722512"></a><a name="p16855722512"></a>t<sub id="sub665562914148"><a name="sub665562914148"></a><a name="sub665562914148"></a>ISU</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p479011715537"><a name="p479011715537"></a><a name="p479011715537"></a>5ns@1.1V</p>
<p id="p84737615245"><a name="p84737615245"></a><a name="p84737615245"></a>7ns@1.0V</p>
</td>
<td class="cellrowborder" valign="top" width="10.35%" headers="mcps1.2.7.1.4 "><p id="p138551125512"><a name="p138551125512"></a><a name="p138551125512"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.32%" headers="mcps1.2.7.1.5 "><p id="p1585518215510"><a name="p1585518215510"></a><a name="p1585518215510"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p158551721159"><a name="p158551721159"></a><a name="p158551721159"></a>C<sub id="sub46551129111412"><a name="sub46551129111412"></a><a name="sub46551129111412"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row15855102151"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p6856128516"><a name="p6856128516"></a><a name="p6856128516"></a>Input hold time</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p5856625518"><a name="p5856625518"></a><a name="p5856625518"></a>t<sub id="sub1665514295142"><a name="sub1665514295142"></a><a name="sub1665514295142"></a>IH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p17856024510"><a name="p17856024510"></a><a name="p17856024510"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="10.35%" headers="mcps1.2.7.1.4 "><p id="p885632457"><a name="p885632457"></a><a name="p885632457"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.32%" headers="mcps1.2.7.1.5 "><p id="p108561121550"><a name="p108561121550"></a><a name="p108561121550"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p1856121518"><a name="p1856121518"></a><a name="p1856121518"></a>C<sub id="sub365572951410"><a name="sub365572951410"></a><a name="sub365572951410"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row1856102256"><td class="cellrowborder" colspan="6" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.1.2 mcps1.2.7.1.3 mcps1.2.7.1.4 mcps1.2.7.1.5 mcps1.2.7.1.6 "><p id="p352615071215"><a name="p352615071215"></a><a name="p352615071215"></a>Outputs CMD, DAT(referenced to CLK)</p>
</td>
</tr>
<tr id="row08565215511"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p18856192654"><a name="p18856192654"></a><a name="p18856192654"></a>Output Delay time during Data Transfer Mode</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p4856122652"><a name="p4856122652"></a><a name="p4856122652"></a>t<sub id="sub865572910140"><a name="sub865572910140"></a><a name="sub865572910140"></a>ODLY</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p10856142957"><a name="p10856142957"></a><a name="p10856142957"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.35%" headers="mcps1.2.7.1.4 "><p id="p12856132853"><a name="p12856132853"></a><a name="p12856132853"></a>14ns@1.1V</p>
<p id="p184741159132417"><a name="p184741159132417"></a><a name="p184741159132417"></a>17ns@1.0V</p>
</td>
<td class="cellrowborder" valign="top" width="9.32%" headers="mcps1.2.7.1.5 "><p id="p188564213517"><a name="p188564213517"></a><a name="p188564213517"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p58565215515"><a name="p58565215515"></a><a name="p58565215515"></a>C<sub id="sub20655142981416"><a name="sub20655142981416"></a><a name="sub20655142981416"></a>L</sub>≤40pF</p>
</td>
</tr>
<tr id="row885615216513"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p158561424510"><a name="p158561424510"></a><a name="p158561424510"></a>Output Hold time</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p108561829511"><a name="p108561829511"></a><a name="p108561829511"></a>t<sub id="sub17655172971414"><a name="sub17655172971414"></a><a name="sub17655172971414"></a>OH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p159910818174"><a name="p159910818174"></a><a name="p159910818174"></a>1.55ns</p>
</td>
<td class="cellrowborder" valign="top" width="10.35%" headers="mcps1.2.7.1.4 "><p id="p1285611214518"><a name="p1285611214518"></a><a name="p1285611214518"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.32%" headers="mcps1.2.7.1.5 "><p id="p13856725513"><a name="p13856725513"></a><a name="p13856725513"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p11856121854"><a name="p11856121854"></a><a name="p11856121854"></a>C<sub id="sub7656329141418"><a name="sub7656329141418"></a><a name="sub7656329141418"></a>L</sub>≤15pF</p>
</td>
</tr>
<tr id="row1067619190123"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p2067719194123"><a name="p2067719194123"></a><a name="p2067719194123"></a>Total System Capacitance for each line</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p1667713197123"><a name="p1667713197123"></a><a name="p1667713197123"></a>C<sub id="sub136561829181414"><a name="sub136561829181414"></a><a name="sub136561829181414"></a>L</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p10677719111218"><a name="p10677719111218"></a><a name="p10677719111218"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.35%" headers="mcps1.2.7.1.4 "><p id="p17677151941213"><a name="p17677151941213"></a><a name="p17677151941213"></a>40</p>
</td>
<td class="cellrowborder" valign="top" width="9.32%" headers="mcps1.2.7.1.5 "><p id="p067711981219"><a name="p067711981219"></a><a name="p067711981219"></a>pF</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p12677919101210"><a name="p12677919101210"></a><a name="p12677919101210"></a>1 card</p>
</td>
</tr>
</tbody>
</table>

说明：High speed模式的数据信号时序，其输出数据和输入数据都是由时钟的上升沿为参考。

**SDR25模式<a name="section197651817359"></a>**

SDR25模式为SDIO经过电压切换流程之后才能进入的模式，此模式要接口时钟最大支持到50MHz。对时钟的约束如下表所示。

**表 5**  SDR25模式时钟参数表 （VDDIO=1.8V）

<a name="table165341455158"></a>
<table><thead align="left"><tr id="row1453417458156"><th class="cellrowborder" valign="top" width="31.96%" id="mcps1.2.7.1.1"><p id="p1253434519156"><a name="p1253434519156"></a><a name="p1253434519156"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="10.31%" id="mcps1.2.7.1.2"><p id="p19534445131519"><a name="p19534445131519"></a><a name="p19534445131519"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="9.55%" id="mcps1.2.7.1.3"><p id="p4535104519155"><a name="p4535104519155"></a><a name="p4535104519155"></a>最小值</p>
</th>
<th class="cellrowborder" valign="top" width="10.35%" id="mcps1.2.7.1.4"><p id="p753584551520"><a name="p753584551520"></a><a name="p753584551520"></a>最大值</p>
</th>
<th class="cellrowborder" valign="top" width="9.32%" id="mcps1.2.7.1.5"><p id="p115351945131520"><a name="p115351945131520"></a><a name="p115351945131520"></a>单位</p>
</th>
<th class="cellrowborder" valign="top" width="28.51%" id="mcps1.2.7.1.6"><p id="p18535194519152"><a name="p18535194519152"></a><a name="p18535194519152"></a>备注</p>
</th>
</tr>
</thead>
<tbody><tr id="row353513452152"><td class="cellrowborder" colspan="6" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.1.2 mcps1.2.7.1.3 mcps1.2.7.1.4 mcps1.2.7.1.5 mcps1.2.7.1.6 "><p id="p13535204512158"><a name="p13535204512158"></a><a name="p13535204512158"></a>Clock CLK（All value are referred to min(V<sub id="sub7658182911415"><a name="sub7658182911415"></a><a name="sub7658182911415"></a>IH</sub>) and max(V<sub id="sub1165822941415"><a name="sub1165822941415"></a><a name="sub1165822941415"></a>IL</sub>)）</p>
</td>
</tr>
<tr id="row2053516454157"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p15351045161510"><a name="p15351045161510"></a><a name="p15351045161510"></a>Clock frequency Date Transfer Mode</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p0535745141518"><a name="p0535745141518"></a><a name="p0535745141518"></a>f<sub id="sub565812917143"><a name="sub565812917143"></a><a name="sub565812917143"></a>PP</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p17535124518158"><a name="p17535124518158"></a><a name="p17535124518158"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.35%" headers="mcps1.2.7.1.4 "><p id="p16535154561517"><a name="p16535154561517"></a><a name="p16535154561517"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="9.32%" headers="mcps1.2.7.1.5 "><p id="p14535645131510"><a name="p14535645131510"></a><a name="p14535645131510"></a>MHz</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p1753584514156"><a name="p1753584514156"></a><a name="p1753584514156"></a>C<sub id="sub2065972931418"><a name="sub2065972931418"></a><a name="sub2065972931418"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row13535645111517"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p8535144512152"><a name="p8535144512152"></a><a name="p8535144512152"></a>Clock low time</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p115351945161513"><a name="p115351945161513"></a><a name="p115351945161513"></a>t<sub id="sub06591629141415"><a name="sub06591629141415"></a><a name="sub06591629141415"></a>WL</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p253564541512"><a name="p253564541512"></a><a name="p253564541512"></a>3.6</p>
</td>
<td class="cellrowborder" valign="top" width="10.35%" headers="mcps1.2.7.1.4 "><p id="p153519456156"><a name="p153519456156"></a><a name="p153519456156"></a>8.4</p>
</td>
<td class="cellrowborder" valign="top" width="9.32%" headers="mcps1.2.7.1.5 "><p id="p85351945201513"><a name="p85351945201513"></a><a name="p85351945201513"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p353554516151"><a name="p353554516151"></a><a name="p353554516151"></a>C<sub id="sub10659172981416"><a name="sub10659172981416"></a><a name="sub10659172981416"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row653514541514"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p1753514457157"><a name="p1753514457157"></a><a name="p1753514457157"></a>Clock high time</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p8535154515155"><a name="p8535154515155"></a><a name="p8535154515155"></a>t<sub id="sub156591729111414"><a name="sub156591729111414"></a><a name="sub156591729111414"></a>WH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p1953534511155"><a name="p1953534511155"></a><a name="p1953534511155"></a>3.6</p>
</td>
<td class="cellrowborder" valign="top" width="10.35%" headers="mcps1.2.7.1.4 "><p id="p195351845121519"><a name="p195351845121519"></a><a name="p195351845121519"></a>8.4</p>
</td>
<td class="cellrowborder" valign="top" width="9.32%" headers="mcps1.2.7.1.5 "><p id="p145351454159"><a name="p145351454159"></a><a name="p145351454159"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p12535184516159"><a name="p12535184516159"></a><a name="p12535184516159"></a>C<sub id="sub106591429131414"><a name="sub106591429131414"></a><a name="sub106591429131414"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row65351445131516"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p1453524511519"><a name="p1453524511519"></a><a name="p1453524511519"></a>Clock rise time</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p18535134511519"><a name="p18535134511519"></a><a name="p18535134511519"></a>t<sub id="sub1365922991412"><a name="sub1365922991412"></a><a name="sub1365922991412"></a>TLH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p353524571514"><a name="p353524571514"></a><a name="p353524571514"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.35%" headers="mcps1.2.7.1.4 "><p id="p12535945111511"><a name="p12535945111511"></a><a name="p12535945111511"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="9.32%" headers="mcps1.2.7.1.5 "><p id="p18535174571516"><a name="p18535174571516"></a><a name="p18535174571516"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p175355451152"><a name="p175355451152"></a><a name="p175355451152"></a>C<sub id="sub12659162919149"><a name="sub12659162919149"></a><a name="sub12659162919149"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row353664517150"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p953694520150"><a name="p953694520150"></a><a name="p953694520150"></a>Clock fall time</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p1353654561519"><a name="p1353654561519"></a><a name="p1353654561519"></a>t<sub id="sub10659122961413"><a name="sub10659122961413"></a><a name="sub10659122961413"></a>THL</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p453664517154"><a name="p453664517154"></a><a name="p453664517154"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.35%" headers="mcps1.2.7.1.4 "><p id="p49671629134617"><a name="p49671629134617"></a><a name="p49671629134617"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="9.32%" headers="mcps1.2.7.1.5 "><p id="p15536154521514"><a name="p15536154521514"></a><a name="p15536154521514"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p1553619457150"><a name="p1553619457150"></a><a name="p1553619457150"></a>C<sub id="sub146604291143"><a name="sub146604291143"></a><a name="sub146604291143"></a>CARD</sub>≤10pF</p>
</td>
</tr>
</tbody>
</table>

**表 6**  SDR25模式时序约束表 \(VDDIO=1.8V\)

<a name="table3538204591518"></a>
<table><thead align="left"><tr id="row8538164541510"><th class="cellrowborder" valign="top" width="31.96%" id="mcps1.2.7.1.1"><p id="p1953811450151"><a name="p1953811450151"></a><a name="p1953811450151"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="10.31%" id="mcps1.2.7.1.2"><p id="p135381145171513"><a name="p135381145171513"></a><a name="p135381145171513"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="9.55%" id="mcps1.2.7.1.3"><p id="p4538184561517"><a name="p4538184561517"></a><a name="p4538184561517"></a>最小值</p>
</th>
<th class="cellrowborder" valign="top" width="10.36%" id="mcps1.2.7.1.4"><p id="p15538745111520"><a name="p15538745111520"></a><a name="p15538745111520"></a>最大值</p>
</th>
<th class="cellrowborder" valign="top" width="9.31%" id="mcps1.2.7.1.5"><p id="p1253834516154"><a name="p1253834516154"></a><a name="p1253834516154"></a>单位</p>
</th>
<th class="cellrowborder" valign="top" width="28.51%" id="mcps1.2.7.1.6"><p id="p19538174520159"><a name="p19538174520159"></a><a name="p19538174520159"></a>备注</p>
</th>
</tr>
</thead>
<tbody><tr id="row16538184511159"><td class="cellrowborder" colspan="6" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.1.2 mcps1.2.7.1.3 mcps1.2.7.1.4 mcps1.2.7.1.5 mcps1.2.7.1.6 "><p id="p105382045131511"><a name="p105382045131511"></a><a name="p105382045131511"></a>Inputs CMD, DAT（referred to CLK）</p>
</td>
</tr>
<tr id="row1553834561517"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p753814452156"><a name="p753814452156"></a><a name="p753814452156"></a>Input set-up time</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p1353844517154"><a name="p1353844517154"></a><a name="p1353844517154"></a>t<sub id="sub266022915141"><a name="sub266022915141"></a><a name="sub266022915141"></a>ISU</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p84301035152710"><a name="p84301035152710"></a><a name="p84301035152710"></a>4.5ns@1.1V</p>
<p id="p144301835142715"><a name="p144301835142715"></a><a name="p144301835142715"></a>7.0ns@1.0V</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p85382457153"><a name="p85382457153"></a><a name="p85382457153"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p353834511519"><a name="p353834511519"></a><a name="p353834511519"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p175381845101515"><a name="p175381845101515"></a><a name="p175381845101515"></a>C<sub id="sub1266042981410"><a name="sub1266042981410"></a><a name="sub1266042981410"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row205382045181517"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p18538144531519"><a name="p18538144531519"></a><a name="p18538144531519"></a>Input hold time</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p45381045161518"><a name="p45381045161518"></a><a name="p45381045161518"></a>t<sub id="sub1366012297145"><a name="sub1366012297145"></a><a name="sub1366012297145"></a>IH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p8538245131512"><a name="p8538245131512"></a><a name="p8538245131512"></a>0.8ns</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p10538745131518"><a name="p10538745131518"></a><a name="p10538745131518"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p2538145111511"><a name="p2538145111511"></a><a name="p2538145111511"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p14538104571519"><a name="p14538104571519"></a><a name="p14538104571519"></a>C<sub id="sub11660162931418"><a name="sub11660162931418"></a><a name="sub11660162931418"></a>CARD</sub>≤10pF</p>
</td>
</tr>
<tr id="row1553815457154"><td class="cellrowborder" colspan="6" valign="top" headers="mcps1.2.7.1.1 mcps1.2.7.1.2 mcps1.2.7.1.3 mcps1.2.7.1.4 mcps1.2.7.1.5 mcps1.2.7.1.6 "><p id="p35389455159"><a name="p35389455159"></a><a name="p35389455159"></a>Outputs CMD, DAT(referenced to CLK)</p>
</td>
</tr>
<tr id="row205382045201513"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p1453915451157"><a name="p1453915451157"></a><a name="p1453915451157"></a>Output Delay time during Data Transfer Mode</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p14539184513151"><a name="p14539184513151"></a><a name="p14539184513151"></a>t<sub id="sub866114295149"><a name="sub866114295149"></a><a name="sub866114295149"></a>ODLY</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p553964518152"><a name="p553964518152"></a><a name="p553964518152"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p76728238324"><a name="p76728238324"></a><a name="p76728238324"></a>14ns@1.1V</p>
<p id="p17672723163212"><a name="p17672723163212"></a><a name="p17672723163212"></a>17ns@1.0V</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p10539164516153"><a name="p10539164516153"></a><a name="p10539164516153"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p17539194551516"><a name="p17539194551516"></a><a name="p17539194551516"></a>C<sub id="sub56611229191412"><a name="sub56611229191412"></a><a name="sub56611229191412"></a>L</sub>≤10pF</p>
</td>
</tr>
<tr id="row053913454157"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p145394451150"><a name="p145394451150"></a><a name="p145394451150"></a>Output Hold time</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p1053917454155"><a name="p1053917454155"></a><a name="p1053917454155"></a>t<sub id="sub1661172991418"><a name="sub1661172991418"></a><a name="sub1661172991418"></a>OH</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p712535173211"><a name="p712535173211"></a><a name="p712535173211"></a>1.55ns</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p1153914456157"><a name="p1153914456157"></a><a name="p1153914456157"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p15539345101512"><a name="p15539345101512"></a><a name="p15539345101512"></a>ns</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p15539645131518"><a name="p15539645131518"></a><a name="p15539645131518"></a>C<sub id="sub7661129111413"><a name="sub7661129111413"></a><a name="sub7661129111413"></a>L</sub>≤15pF</p>
</td>
</tr>
<tr id="row253964510157"><td class="cellrowborder" valign="top" width="31.96%" headers="mcps1.2.7.1.1 "><p id="p953924510152"><a name="p953924510152"></a><a name="p953924510152"></a>Total System Capacitance for each line</p>
</td>
<td class="cellrowborder" valign="top" width="10.31%" headers="mcps1.2.7.1.2 "><p id="p1553984541516"><a name="p1553984541516"></a><a name="p1553984541516"></a>C<sub id="sub10661122941419"><a name="sub10661122941419"></a><a name="sub10661122941419"></a>L</sub></p>
</td>
<td class="cellrowborder" valign="top" width="9.55%" headers="mcps1.2.7.1.3 "><p id="p95391845191511"><a name="p95391845191511"></a><a name="p95391845191511"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="10.36%" headers="mcps1.2.7.1.4 "><p id="p65398452152"><a name="p65398452152"></a><a name="p65398452152"></a>40</p>
</td>
<td class="cellrowborder" valign="top" width="9.31%" headers="mcps1.2.7.1.5 "><p id="p1853914581513"><a name="p1853914581513"></a><a name="p1853914581513"></a>pF</p>
</td>
<td class="cellrowborder" valign="top" width="28.51%" headers="mcps1.2.7.1.6 "><p id="p10539345141516"><a name="p10539345141516"></a><a name="p10539345141516"></a>1 card</p>
</td>
</tr>
</tbody>
</table>

## SPI接口时序<a name="ZH-CN_TOPIC_0000001456242668"></a>

>![](public_sys-resources/icon-note.gif) **说明：** 
>以下缩略语或字母含义：
>-   MSB：Most Significant Bit
>-   LSB：Least Significant Bit
>-   SPI\_CK\(0\)：spo=0
>-   SPI\_CK\(1\)：spo=1

SPI接口时钟时序如[图1](#fig18479195119258)所示。

**图 1**  SPI接口时序图<a name="fig18479195119258"></a>  
![](figures/SPI接口时序图.png "SPI接口时序图")

注：

用作Master时，时钟周期最小值为33.3ns@1.1V \(30MHz\)、62.5ns@1.0V（16MHz）；

用作Slave时，时钟周期最小值为80ns@1.1V\(12.5Mhz\)、200ns@1.0V（5Mhz）。

SPO（SPICLKOUT Polarity）表示SPICLKOUT极性，SPH（SPICLKOUT Phase）表示SPICLKOUT相位。

**表 1**  SPI接口时序参数表

<a name="table3538204591518"></a>
<table><thead align="left"><tr id="row8538164541510"><th class="cellrowborder" valign="top" width="34.94%" id="mcps1.2.6.1.1"><p id="p1953811450151"><a name="p1953811450151"></a><a name="p1953811450151"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="11.940000000000001%" id="mcps1.2.6.1.2"><p id="p135381145171513"><a name="p135381145171513"></a><a name="p135381145171513"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="12.120000000000001%" id="mcps1.2.6.1.3"><p id="p4538184561517"><a name="p4538184561517"></a><a name="p4538184561517"></a>最小值</p>
</th>
<th class="cellrowborder" valign="top" width="23.03%" id="mcps1.2.6.1.4"><p id="p15538745111520"><a name="p15538745111520"></a><a name="p15538745111520"></a>最大值</p>
</th>
<th class="cellrowborder" valign="top" width="17.97%" id="mcps1.2.6.1.5"><p id="p1253834516154"><a name="p1253834516154"></a><a name="p1253834516154"></a>单位</p>
</th>
</tr>
</thead>
<tbody><tr id="row1553834561517"><td class="cellrowborder" valign="top" width="34.94%" headers="mcps1.2.6.1.1 "><p id="p1375184014276"><a name="p1375184014276"></a><a name="p1375184014276"></a>Master输出数据延迟</p>
</td>
<td class="cellrowborder" valign="top" width="11.940000000000001%" headers="mcps1.2.6.1.2 "><p id="p1353844517154"><a name="p1353844517154"></a><a name="p1353844517154"></a>T<sub id="sub188891032151419"><a name="sub188891032151419"></a><a name="sub188891032151419"></a>dd</sub></p>
</td>
<td class="cellrowborder" valign="top" width="12.120000000000001%" headers="mcps1.2.6.1.3 "><p id="p165381477298"><a name="p165381477298"></a><a name="p165381477298"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="23.03%" headers="mcps1.2.6.1.4 "><p id="p11355139165217"><a name="p11355139165217"></a><a name="p11355139165217"></a>6.58ns @1.1V</p>
<p id="p6687177185514"><a name="p6687177185514"></a><a name="p6687177185514"></a>14.42ns @1.0V</p>
</td>
<td class="cellrowborder" valign="top" width="17.97%" headers="mcps1.2.6.1.5 "><p id="p353834511519"><a name="p353834511519"></a><a name="p353834511519"></a>ns</p>
</td>
</tr>
<tr id="row1263883151012"><td class="cellrowborder" valign="top" width="34.94%" headers="mcps1.2.6.1.1 "><p id="p14830143261020"><a name="p14830143261020"></a><a name="p14830143261020"></a>Slave输出数据延迟</p>
</td>
<td class="cellrowborder" valign="top" width="11.940000000000001%" headers="mcps1.2.6.1.2 "><p id="p188301532131020"><a name="p188301532131020"></a><a name="p188301532131020"></a>T<sub id="sub158303327108"><a name="sub158303327108"></a><a name="sub158303327108"></a>dd</sub></p>
</td>
<td class="cellrowborder" valign="top" width="12.120000000000001%" headers="mcps1.2.6.1.3 "><p id="p78301932141017"><a name="p78301932141017"></a><a name="p78301932141017"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="23.03%" headers="mcps1.2.6.1.4 "><p id="p1830452112520"><a name="p1830452112520"></a><a name="p1830452112520"></a>24.8ns @1.1V</p>
<p id="p143611955610"><a name="p143611955610"></a><a name="p143611955610"></a>84.8ns @1.0V</p>
</td>
<td class="cellrowborder" valign="top" width="17.97%" headers="mcps1.2.6.1.5 "><p id="p17830123216101"><a name="p17830123216101"></a><a name="p17830123216101"></a>ns</p>
</td>
</tr>
<tr id="row205382045181517"><td class="cellrowborder" valign="top" width="34.94%" headers="mcps1.2.6.1.1 "><p id="p1375110408274"><a name="p1375110408274"></a><a name="p1375110408274"></a>输入控制信号建立时间(master)</p>
</td>
<td class="cellrowborder" valign="top" width="11.940000000000001%" headers="mcps1.2.6.1.2 "><p id="p189591125192914"><a name="p189591125192914"></a><a name="p189591125192914"></a>T<sub id="sub12889132121417"><a name="sub12889132121417"></a><a name="sub12889132121417"></a>ds</sub></p>
</td>
<td class="cellrowborder" valign="top" width="12.120000000000001%" headers="mcps1.2.6.1.3 "><p id="p15993512185314"><a name="p15993512185314"></a><a name="p15993512185314"></a>1.64ns @1.1V</p>
<p id="p871575335611"><a name="p871575335611"></a><a name="p871575335611"></a>6.06ns @1.0V</p>
</td>
<td class="cellrowborder" valign="top" width="23.03%" headers="mcps1.2.6.1.4 "><p id="p8536947132913"><a name="p8536947132913"></a><a name="p8536947132913"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="17.97%" headers="mcps1.2.6.1.5 "><p id="p2538145111511"><a name="p2538145111511"></a><a name="p2538145111511"></a>ns</p>
</td>
</tr>
<tr id="row205382045201513"><td class="cellrowborder" valign="top" width="34.94%" headers="mcps1.2.6.1.1 "><p id="p65301314152810"><a name="p65301314152810"></a><a name="p65301314152810"></a>输入控制信号保持时间(master)</p>
</td>
<td class="cellrowborder" valign="top" width="11.940000000000001%" headers="mcps1.2.6.1.2 "><p id="p155233252911"><a name="p155233252911"></a><a name="p155233252911"></a>T<sub id="sub8889193220149"><a name="sub8889193220149"></a><a name="sub8889193220149"></a>dh</sub></p>
</td>
<td class="cellrowborder" valign="top" width="12.120000000000001%" headers="mcps1.2.6.1.3 "><p id="p14183182635314"><a name="p14183182635314"></a><a name="p14183182635314"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="23.03%" headers="mcps1.2.6.1.4 "><p id="p155351947152912"><a name="p155351947152912"></a><a name="p155351947152912"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="17.97%" headers="mcps1.2.6.1.5 "><p id="p10539164516153"><a name="p10539164516153"></a><a name="p10539164516153"></a>ns</p>
</td>
</tr>
<tr id="row053913454157"><td class="cellrowborder" valign="top" width="34.94%" headers="mcps1.2.6.1.1 "><p id="p7673144017283"><a name="p7673144017283"></a><a name="p7673144017283"></a>输入控制信号建立时间(slave)</p>
</td>
<td class="cellrowborder" valign="top" width="11.940000000000001%" headers="mcps1.2.6.1.2 "><p id="p148933243293"><a name="p148933243293"></a><a name="p148933243293"></a>T<sub id="sub18890133241418"><a name="sub18890133241418"></a><a name="sub18890133241418"></a>ds</sub></p>
</td>
<td class="cellrowborder" valign="top" width="12.120000000000001%" headers="mcps1.2.6.1.3 "><p id="p4730175017530"><a name="p4730175017530"></a><a name="p4730175017530"></a>34.8ns @1.1V</p>
<p id="p01391155715"><a name="p01391155715"></a><a name="p01391155715"></a>94.8ns @1.0V</p>
</td>
<td class="cellrowborder" valign="top" width="23.03%" headers="mcps1.2.6.1.4 "><p id="p9533124782918"><a name="p9533124782918"></a><a name="p9533124782918"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="17.97%" headers="mcps1.2.6.1.5 "><p id="p15539345101512"><a name="p15539345101512"></a><a name="p15539345101512"></a>ns</p>
</td>
</tr>
<tr id="row253964510157"><td class="cellrowborder" valign="top" width="34.94%" headers="mcps1.2.6.1.1 "><p id="p2509454102819"><a name="p2509454102819"></a><a name="p2509454102819"></a>输入控制信号保持时间(slave)</p>
</td>
<td class="cellrowborder" valign="top" width="11.940000000000001%" headers="mcps1.2.6.1.2 "><p id="p888242412920"><a name="p888242412920"></a><a name="p888242412920"></a>T<sub id="sub189017322145"><a name="sub189017322145"></a><a name="sub189017322145"></a>dh</sub></p>
</td>
<td class="cellrowborder" valign="top" width="12.120000000000001%" headers="mcps1.2.6.1.3 "><p id="p132601843396"><a name="p132601843396"></a><a name="p132601843396"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="23.03%" headers="mcps1.2.6.1.4 "><p id="p16520194710292"><a name="p16520194710292"></a><a name="p16520194710292"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="17.97%" headers="mcps1.2.6.1.5 "><p id="p1853914581513"><a name="p1853914581513"></a><a name="p1853914581513"></a>ns</p>
</td>
</tr>
</tbody>
</table>

# 注意事项<a name="ZH-CN_TOPIC_0000001505722813"></a>

-   **[硬件设计](#ZH-CN_TOPIC_0000001456242632)**  

-   **[单板生产工艺](#ZH-CN_TOPIC_0000001505842457)**  

## 硬件设计<a name="ZH-CN_TOPIC_0000001456242632"></a>

在硬件设计中的几个注意事项：

-   针对RST\_N管脚需要做外部上拉，为了满足低功耗设计，建议使用1MΩ电阻，在较强干扰环境，可适当减小阻值增强上拉抗扰能力。
-   支持外置RTC功能的芯片，当硬件方案不使用外置RTC时，RTC\_IN管脚板级预留接地电阻位置，若芯片应用场景存在环境或板级干扰，建议RTC\_IN管脚板级接地，RTC\_OUT管脚保持悬空，增强抗干扰能力。板级禁止RTC\_IN和OUT管脚同时接地。
-   针对硬件配置字等GPIO（比如MGPIO14/15）需要做外部上下拉时，建议使用10kΩ电阻；而且当需要深睡保活时，建议睡眠之前配置该GPIO为高阻（复用成GPIO模式后先配置输入态再关闭IE）且无拉状态，目的是为了降低深睡漏电流。
-   MGPIO16管脚有负电压输入时，可能会导致芯片复位，使用时应避免该管脚出现负压；PCB设计有长走线时，建议走内层，避免受到外部干扰；在使用该IO作为输入唤醒功能时，建议默认状态保持高电平，使用低电平或者下降沿唤醒。
-   当需要在深睡保活状态针对某GPIO进行上拉唤醒时，需要在睡眠之前对该GPIO配置为输入且无拉状态。
-   WS53V100的参考设计单板经过发射EVM、接收灵敏度、认证等WiFi射频指标测试。围绕WS53V100芯片的去耦电容容值及摆放位置尽量不要变动，如果必须修改，需要针对单板发射EVM、接收灵敏度、认证等WiFi射频指标进行详细摸底测试。
-   RF链路使用LC组成的π形低通滤波器建议不要更改，尤其是接地电容的地焊盘和地孔处理方式。
-   建议在RF链路上添加接地的ESD射频电感，感值为10nH，摆放位置靠近天线端。
-   提供的参考设计与器件选型主要是实验室测试与样品测试。用户在量产导入时，建议进行全面的产品硬件测试与评估，按照量产流程逐步完成导入。

## 单板生产工艺<a name="ZH-CN_TOPIC_0000001505842457"></a>

单板生产工艺的几个注意事项：

-   单板分板需要使用机器分板，严禁手工分板。
-   手工焊接前请做好静电放电处理，佩戴静电手镯。
-   PCB存储条件建议：
    -   OSP（Organic Solderability Preservative）板

        真空包装前后的存放条件：温度20℃～30℃，相对湿度50%。真空包装后寿命3个月～1年。储存时间超过6个月时，通常拆封后即可组装，但为了避免板材储藏湿气造成爆板，可以烘烤方式来去除板内湿气，烘烤条件为110℃～120℃，1h（最长时间不要超过1.5h）。

    -   喷锡板

        真空包装前后的存放条件：温度25℃，相对湿度60%。真空包装后寿命1年。储存时间超过6个月时，通常拆封后即可组装，但为了避免板材储藏湿气造成爆板，可以烘烤方式来去除板内湿气，烘烤条件为120℃，1h（最长时间不要超过1.5h）。

# 缩略语<a name="ZH-CN_TOPIC_0000001456242660"></a>

<a name="table834819511416"></a>
<table><tbody><tr id="row753095115412"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1853018513418"><a name="p1853018513418"></a><a name="p1853018513418"></a><strong id="b1028613391353"><a name="b1028613391353"></a><a name="b1028613391353"></a>A</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row253055114416"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p7530115116412"><a name="p7530115116412"></a><a name="p7530115116412"></a><strong id="b1928633912356"><a name="b1928633912356"></a><a name="b1928633912356"></a>AC</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p45307513414"><a name="p45307513414"></a><a name="p45307513414"></a>Alternating Current</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p053012512414"><a name="p053012512414"></a><a name="p053012512414"></a>交流（电）</p>
</td>
</tr>
<tr id="row10530151847"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p553019514412"><a name="p553019514412"></a><a name="p553019514412"></a><strong id="b328620399355"><a name="b328620399355"></a><a name="b328620399355"></a>ADC</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p185306511547"><a name="p185306511547"></a><a name="p185306511547"></a>Analog to Digital Converter</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p15304511143"><a name="p15304511143"></a><a name="p15304511143"></a>模数转换器</p>
</td>
</tr>
<tr id="row20530851649"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1053018511344"><a name="p1053018511344"></a><a name="p1053018511344"></a><strong id="b12861539113511"><a name="b12861539113511"></a><a name="b12861539113511"></a>AGC</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p95301151949"><a name="p95301151949"></a><a name="p95301151949"></a>Automatic Gain Control</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1253015512412"><a name="p1253015512412"></a><a name="p1253015512412"></a>自动增益控制</p>
</td>
</tr>
<tr id="row55301451149"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p453014518410"><a name="p453014518410"></a><a name="p453014518410"></a><strong id="b428718393358"><a name="b428718393358"></a><a name="b428718393358"></a>ALE</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p13530195113417"><a name="p13530195113417"></a><a name="p13530195113417"></a>Address Latch Enable</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p175304513418"><a name="p175304513418"></a><a name="p175304513418"></a>地址锁存使能</p>
</td>
</tr>
<tr id="row053019511647"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p65301351147"><a name="p65301351147"></a><a name="p65301351147"></a><strong id="b172874391354"><a name="b172874391354"></a><a name="b172874391354"></a>AO</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1953019515415"><a name="p1953019515415"></a><a name="p1953019515415"></a>Audio Output</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p11530145112411"><a name="p11530145112411"></a><a name="p11530145112411"></a>音频输出</p>
</td>
</tr>
<tr id="row1153017514413"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p18530651849"><a name="p18530651849"></a><a name="p18530651849"></a><strong id="b102871739193513"><a name="b102871739193513"></a><a name="b102871739193513"></a>ARM</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p115301751244"><a name="p115301751244"></a><a name="p115301751244"></a>Advanced RISC Machine</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p19530145115417"><a name="p19530145115417"></a><a name="p19530145115417"></a>高级精简指令集处理器</p>
</td>
</tr>
<tr id="row1753055116410"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p10530551948"><a name="p10530551948"></a><a name="p10530551948"></a><strong id="b5287153911351"><a name="b5287153911351"></a><a name="b5287153911351"></a></strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row11530155119412"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p55301551542"><a name="p55301551542"></a><a name="p55301551542"></a><strong id="b112871639183518"><a name="b112871639183518"></a><a name="b112871639183518"></a>C</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row155301551245"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p145305516419"><a name="p145305516419"></a><a name="p145305516419"></a><strong id="b8287153903520"><a name="b8287153903520"></a><a name="b8287153903520"></a>CODEC</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p15531115113418"><a name="p15531115113418"></a><a name="p15531115113418"></a>Coder Decoder</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1653118511546"><a name="p1653118511546"></a><a name="p1653118511546"></a>编码解码器</p>
</td>
</tr>
<tr id="row45314514412"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1553125114412"><a name="p1553125114412"></a><a name="p1553125114412"></a><strong id="b19287123973513"><a name="b19287123973513"></a><a name="b19287123973513"></a>CPU</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p153119511243"><a name="p153119511243"></a><a name="p153119511243"></a>Central Processing Unit</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p145319512415"><a name="p145319512415"></a><a name="p145319512415"></a>中央处理单元</p>
</td>
</tr>
<tr id="row353112514415"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p9531151445"><a name="p9531151445"></a><a name="p9531151445"></a><strong id="b52882391354"><a name="b52882391354"></a><a name="b52882391354"></a>CS</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p653113511546"><a name="p653113511546"></a><a name="p653113511546"></a>Chip Select</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p11531155117414"><a name="p11531155117414"></a><a name="p11531155117414"></a>片选</p>
</td>
</tr>
<tr id="row145311351347"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p4531105115413"><a name="p4531105115413"></a><a name="p4531105115413"></a><strong id="b19288143993512"><a name="b19288143993512"></a><a name="b19288143993512"></a></strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row453165110414"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1153119513412"><a name="p1153119513412"></a><a name="p1153119513412"></a><strong id="b1728843919352"><a name="b1728843919352"></a><a name="b1728843919352"></a>D</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row95314511640"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1253114511748"><a name="p1253114511748"></a><a name="p1253114511748"></a><strong id="b5288113903515"><a name="b5288113903515"></a><a name="b5288113903515"></a>DAC</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p85311851644"><a name="p85311851644"></a><a name="p85311851644"></a>Digital Analog Converter</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p153113511242"><a name="p153113511242"></a><a name="p153113511242"></a>数字模拟转换器</p>
</td>
</tr>
<tr id="row65315511846"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p105317518415"><a name="p105317518415"></a><a name="p105317518415"></a><strong id="b142881398352"><a name="b142881398352"></a><a name="b142881398352"></a>DC</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p25311151642"><a name="p25311151642"></a><a name="p25311151642"></a>Direct Current</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p553111512044"><a name="p553111512044"></a><a name="p553111512044"></a>直流(电)</p>
</td>
</tr>
<tr id="row5531151342"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p35311751247"><a name="p35311751247"></a><a name="p35311751247"></a><strong id="b628833993516"><a name="b628833993516"></a><a name="b628833993516"></a>DDR</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p125311511649"><a name="p125311511649"></a><a name="p125311511649"></a>Double Data Rate</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p55314516417"><a name="p55314516417"></a><a name="p55314516417"></a>双数据速率</p>
</td>
</tr>
<tr id="row14531851147"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p85316511040"><a name="p85316511040"></a><a name="p85316511040"></a><strong id="b1628893915353"><a name="b1628893915353"></a><a name="b1628893915353"></a>E</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row75311351242"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p14531195111414"><a name="p14531195111414"></a><a name="p14531195111414"></a><strong id="b13289639163514"><a name="b13289639163514"></a><a name="b13289639163514"></a>EBI</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p2531145119418"><a name="p2531145119418"></a><a name="p2531145119418"></a>External Bus Interface</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p205310511347"><a name="p205310511347"></a><a name="p205310511347"></a>外部总线接口</p>
</td>
</tr>
<tr id="row18531151240"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p2531851344"><a name="p2531851344"></a><a name="p2531851344"></a><strong id="b52891039193517"><a name="b52891039193517"></a><a name="b52891039193517"></a>ECC</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p853120516418"><a name="p853120516418"></a><a name="p853120516418"></a>Error Checking and Correction</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p553110511642"><a name="p553110511642"></a><a name="p553110511642"></a>差错校验纠正</p>
</td>
</tr>
<tr id="row153125113410"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p11531151944"><a name="p11531151944"></a><a name="p11531151944"></a><strong id="b14289193953510"><a name="b14289193953510"></a><a name="b14289193953510"></a>ETH</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p3531185120417"><a name="p3531185120417"></a><a name="p3531185120417"></a>Ethernet</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p35311951442"><a name="p35311951442"></a><a name="p35311951442"></a>以太网</p>
</td>
</tr>
<tr id="row1253155110415"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1853114511344"><a name="p1853114511344"></a><a name="p1853114511344"></a><strong id="b14289439163519"><a name="b14289439163519"></a><a name="b14289439163519"></a></strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row1253115111419"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p953119511948"><a name="p953119511948"></a><a name="p953119511948"></a><strong id="b2289163914351"><a name="b2289163914351"></a><a name="b2289163914351"></a>F</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row1053111511142"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p12532651546"><a name="p12532651546"></a><a name="p12532651546"></a><strong id="b628983923511"><a name="b628983923511"></a><a name="b628983923511"></a>FLASH</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1053216511041"><a name="p1053216511041"></a><a name="p1053216511041"></a>FLASH memory</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p353216511744"><a name="p353216511744"></a><a name="p353216511744"></a>闪速存储器</p>
</td>
</tr>
<tr id="row1553211514419"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p85321351642"><a name="p85321351642"></a><a name="p85321351642"></a><strong id="b3289193933514"><a name="b3289193933514"></a><a name="b3289193933514"></a></strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row14532105111415"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p125328511546"><a name="p125328511546"></a><a name="p125328511546"></a><strong id="b4290143917359"><a name="b4290143917359"></a><a name="b4290143917359"></a>I</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row1053212511246"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p653285114417"><a name="p653285114417"></a><a name="p653285114417"></a><strong id="b18290153911353"><a name="b18290153911353"></a><a name="b18290153911353"></a>I2C</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p05329511745"><a name="p05329511745"></a><a name="p05329511745"></a>The Inter-Integrated Circuit</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p105321551944"><a name="p105321551944"></a><a name="p105321551944"></a>一种串行总线协议标准</p>
</td>
</tr>
<tr id="row9532115111412"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1053214511045"><a name="p1053214511045"></a><a name="p1053214511045"></a><strong id="b22900397357"><a name="b22900397357"></a><a name="b22900397357"></a>I2S</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p05328511646"><a name="p05328511646"></a><a name="p05328511646"></a>Inter-IC Sound</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p353211517416"><a name="p353211517416"></a><a name="p353211517416"></a>一种音频数据传输总线标准</p>
</td>
</tr>
<tr id="row165321151640"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p25327511145"><a name="p25327511145"></a><a name="p25327511145"></a><strong id="b192901739193516"><a name="b192901739193516"></a><a name="b192901739193516"></a>IO</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p14532155118411"><a name="p14532155118411"></a><a name="p14532155118411"></a>Input Output</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1153217510413"><a name="p1153217510413"></a><a name="p1153217510413"></a>输入输出</p>
</td>
</tr>
<tr id="row105325510411"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p55321051342"><a name="p55321051342"></a><a name="p55321051342"></a><strong id="b1129093943518"><a name="b1129093943518"></a><a name="b1129093943518"></a>IPU</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p185321251341"><a name="p185321251341"></a><a name="p185321251341"></a>Internal Pull-Up</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p653217511417"><a name="p653217511417"></a><a name="p653217511417"></a>内部上拉</p>
</td>
</tr>
<tr id="row105329511147"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1953215116414"><a name="p1953215116414"></a><a name="p1953215116414"></a><strong id="b729073911351"><a name="b729073911351"></a><a name="b729073911351"></a>IR</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1453245115418"><a name="p1453245115418"></a><a name="p1453245115418"></a>Infrared Ray</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p0532251942"><a name="p0532251942"></a><a name="p0532251942"></a>红外线</p>
</td>
</tr>
<tr id="row135327511545"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p553215115419"><a name="p553215115419"></a><a name="p553215115419"></a><strong id="b16290103917354"><a name="b16290103917354"></a><a name="b16290103917354"></a></strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row953216511943"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p10532165110410"><a name="p10532165110410"></a><a name="p10532165110410"></a><strong id="b3291103917353"><a name="b3291103917353"></a><a name="b3291103917353"></a>J</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row1653219515419"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p65321851845"><a name="p65321851845"></a><a name="p65321851845"></a><strong id="b429113399354"><a name="b429113399354"></a><a name="b429113399354"></a>JEDEC</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p153217511741"><a name="p153217511741"></a><a name="p153217511741"></a>Joint Electron Device Engineering Council</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p05321251840"><a name="p05321251840"></a><a name="p05321251840"></a>电子元件工业联合会</p>
</td>
</tr>
<tr id="row155325511249"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p175321516412"><a name="p175321516412"></a><a name="p175321516412"></a><strong id="b42911439133514"><a name="b42911439133514"></a><a name="b42911439133514"></a>JTAG</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1953285111411"><a name="p1953285111411"></a><a name="p1953285111411"></a>Joint Test Action Group</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p553213511741"><a name="p553213511741"></a><a name="p553213511741"></a>联合测试行动小组</p>
</td>
</tr>
<tr id="row115326511342"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p35321751346"><a name="p35321751346"></a><a name="p35321751346"></a><strong id="b1329183920352"><a name="b1329183920352"></a><a name="b1329183920352"></a></strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row953210511447"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p13532151143"><a name="p13532151143"></a><a name="p13532151143"></a><strong id="b92911939123514"><a name="b92911939123514"></a><a name="b92911939123514"></a>L</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row453217511148"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p3532135111416"><a name="p3532135111416"></a><a name="p3532135111416"></a><strong id="b72911539163519"><a name="b72911539163519"></a><a name="b72911539163519"></a>LCD</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1153310511942"><a name="p1153310511942"></a><a name="p1153310511942"></a>Liquid Crystal Display</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1353311514414"><a name="p1353311514414"></a><a name="p1353311514414"></a>液晶显示屏</p>
</td>
</tr>
<tr id="row15533115111417"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p453316518411"><a name="p453316518411"></a><a name="p453316518411"></a><strong id="b122918395351"><a name="b122918395351"></a><a name="b122918395351"></a>LED</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1553314512410"><a name="p1553314512410"></a><a name="p1553314512410"></a>Light Emitting Diode</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1253319517412"><a name="p1253319517412"></a><a name="p1253319517412"></a>发光二极管</p>
</td>
</tr>
<tr id="row1253315511242"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p75339511048"><a name="p75339511048"></a><a name="p75339511048"></a><strong id="b11292173911353"><a name="b11292173911353"></a><a name="b11292173911353"></a>LSB</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1653312516411"><a name="p1653312516411"></a><a name="p1653312516411"></a>Least Significant Byte</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p653314511145"><a name="p653314511145"></a><a name="p653314511145"></a>最低有效字节</p>
</td>
</tr>
<tr id="row18533135114419"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p2053315119410"><a name="p2053315119410"></a><a name="p2053315119410"></a><strong id="b329223912351"><a name="b329223912351"></a><a name="b329223912351"></a>LVCMOS</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p353316511446"><a name="p353316511446"></a><a name="p353316511446"></a>Low Voltage Complementary Metal Oxide Semiconductor Transistor</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p8533165111414"><a name="p8533165111414"></a><a name="p8533165111414"></a>低压互补型金属氧化物半导体</p>
</td>
</tr>
<tr id="row753319515410"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p7533551442"><a name="p7533551442"></a><a name="p7533551442"></a><strong id="b10292133912358"><a name="b10292133912358"></a><a name="b10292133912358"></a></strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row953305115419"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p20533451149"><a name="p20533451149"></a><a name="p20533451149"></a><strong id="b1729273914358"><a name="b1729273914358"></a><a name="b1729273914358"></a>M</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row8533145117420"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1053311514419"><a name="p1053311514419"></a><a name="p1053311514419"></a><strong id="b1292143993512"><a name="b1292143993512"></a><a name="b1292143993512"></a>MDC</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p55335517414"><a name="p55335517414"></a><a name="p55335517414"></a>Message Distribution Center</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p853355117419"><a name="p853355117419"></a><a name="p853355117419"></a>消息分发中心</p>
</td>
</tr>
<tr id="row4533195120419"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1753314512416"><a name="p1753314512416"></a><a name="p1753314512416"></a><strong id="b92931639183520"><a name="b92931639183520"></a><a name="b92931639183520"></a>MDIO</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p195338511743"><a name="p195338511743"></a><a name="p195338511743"></a>Management Data Input/Output</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1853385116417"><a name="p1853385116417"></a><a name="p1853385116417"></a>管理数据输入输出接口</p>
</td>
</tr>
<tr id="row453312511412"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p05334511944"><a name="p05334511944"></a><a name="p05334511944"></a><strong id="b729353943516"><a name="b729353943516"></a><a name="b729353943516"></a>MDX</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p15333511147"><a name="p15333511147"></a><a name="p15333511147"></a>Multidimensional Expressions</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p95333513410"><a name="p95333513410"></a><a name="p95333513410"></a>多维表达式</p>
</td>
</tr>
<tr id="row75331751845"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1853312511140"><a name="p1853312511140"></a><a name="p1853312511140"></a><strong id="b11293123973511"><a name="b11293123973511"></a><a name="b11293123973511"></a>MII</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p18533105110413"><a name="p18533105110413"></a><a name="p18533105110413"></a>Media Independent Interface</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1953320511948"><a name="p1953320511948"></a><a name="p1953320511948"></a>媒质独立接口</p>
</td>
</tr>
<tr id="row125337511548"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p253312511540"><a name="p253312511540"></a><a name="p253312511540"></a><strong id="b02933393353"><a name="b02933393353"></a><a name="b02933393353"></a>MLC</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1253315513416"><a name="p1253315513416"></a><a name="p1253315513416"></a>Multi-Level Cell</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p195331051444"><a name="p195331051444"></a><a name="p195331051444"></a>多bit存储单元</p>
</td>
</tr>
<tr id="row11533195110413"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p15533115114411"><a name="p15533115114411"></a><a name="p15533115114411"></a><strong id="b122934394352"><a name="b122934394352"></a><a name="b122934394352"></a>MSB</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p105339512041"><a name="p105339512041"></a><a name="p105339512041"></a>Most Significant Bit</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p45336519413"><a name="p45336519413"></a><a name="p45336519413"></a>最高位</p>
</td>
</tr>
<tr id="row5533155111411"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1253375111411"><a name="p1253375111411"></a><a name="p1253375111411"></a><strong id="b11294193963519"><a name="b11294193963519"></a><a name="b11294193963519"></a></strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row5533151546"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p2533151246"><a name="p2533151246"></a><a name="p2533151246"></a><strong id="b2294163993519"><a name="b2294163993519"></a><a name="b2294163993519"></a>N</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row17533751943"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p153445116419"><a name="p153445116419"></a><a name="p153445116419"></a><strong id="b72941839103516"><a name="b72941839103516"></a><a name="b72941839103516"></a>NC</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p65342516418"><a name="p65342516418"></a><a name="p65342516418"></a>No Connection</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p853495114415"><a name="p853495114415"></a><a name="p853495114415"></a>未连接</p>
</td>
</tr>
<tr id="row953417513415"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p8534651240"><a name="p8534651240"></a><a name="p8534651240"></a><strong id="b192941439123510"><a name="b192941439123510"></a><a name="b192941439123510"></a>NF</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p15534151849"><a name="p15534151849"></a><a name="p15534151849"></a>NAND Flash</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p115340517417"><a name="p115340517417"></a><a name="p115340517417"></a>NAND Flash存储器</p>
</td>
</tr>
<tr id="row1553420511141"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1153417511644"><a name="p1153417511644"></a><a name="p1153417511644"></a><strong id="b17294113919354"><a name="b17294113919354"></a><a name="b17294113919354"></a></strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row1953415516410"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p153412519413"><a name="p153412519413"></a><a name="p153412519413"></a><strong id="b1294173911355"><a name="b1294173911355"></a><a name="b1294173911355"></a>O</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row1153435113410"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1353410519417"><a name="p1353410519417"></a><a name="p1353410519417"></a><strong id="b9295143915358"><a name="b9295143915358"></a><a name="b9295143915358"></a>OD</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p125341551149"><a name="p125341551149"></a><a name="p125341551149"></a>Open Drain</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p453414511448"><a name="p453414511448"></a><a name="p453414511448"></a>漏极开路门</p>
</td>
</tr>
<tr id="row1053412511045"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p45348511843"><a name="p45348511843"></a><a name="p45348511843"></a><strong id="b629533915354"><a name="b629533915354"></a><a name="b629533915354"></a>OOD</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p753414514419"><a name="p753414514419"></a><a name="p753414514419"></a>Object-Oriented Database</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p15534951642"><a name="p15534951642"></a><a name="p15534951642"></a>面向对象数据库</p>
</td>
</tr>
<tr id="row165340511941"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p75341551740"><a name="p75341551740"></a><a name="p75341551740"></a><strong id="b18295739163513"><a name="b18295739163513"></a><a name="b18295739163513"></a>OTP</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p125341951243"><a name="p125341951243"></a><a name="p125341951243"></a>One TimePrograming</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1553412511413"><a name="p1553412511413"></a><a name="p1553412511413"></a>一次性编程</p>
</td>
</tr>
<tr id="row125341951248"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p35341512420"><a name="p35341512420"></a><a name="p35341512420"></a><strong id="b4295143916352"><a name="b4295143916352"></a><a name="b4295143916352"></a></strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row3534175118418"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p753418511541"><a name="p753418511541"></a><a name="p753418511541"></a><strong id="b729533963518"><a name="b729533963518"></a><a name="b729533963518"></a>P</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row105344512412"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p55343515420"><a name="p55343515420"></a><a name="p55343515420"></a><strong id="b12295143973519"><a name="b12295143973519"></a><a name="b12295143973519"></a>PBGA</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1153415511141"><a name="p1153415511141"></a><a name="p1153415511141"></a>Plastic Ball Grid Array</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p19534851141"><a name="p19534851141"></a><a name="p19534851141"></a>塑封球栅阵列</p>
</td>
</tr>
<tr id="row10534155114415"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p3534105112411"><a name="p3534105112411"></a><a name="p3534105112411"></a><strong id="b1629517399353"><a name="b1629517399353"></a><a name="b1629517399353"></a>PCB</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p175341511349"><a name="p175341511349"></a><a name="p175341511349"></a>Physical Control Block</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p165343511147"><a name="p165343511147"></a><a name="p165343511147"></a>物理控制块</p>
</td>
</tr>
<tr id="row553414515418"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p17534115114419"><a name="p17534115114419"></a><a name="p17534115114419"></a><strong id="b152961539163512"><a name="b152961539163512"></a><a name="b152961539163512"></a>PCI</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1853425117411"><a name="p1853425117411"></a><a name="p1853425117411"></a>Peripheral Component Interconnect</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p135347511749"><a name="p135347511749"></a><a name="p135347511749"></a>外设部件互连</p>
</td>
</tr>
<tr id="row253415110417"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p105349515411"><a name="p105349515411"></a><a name="p105349515411"></a><strong id="b92963394354"><a name="b92963394354"></a><a name="b92963394354"></a>PCM</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1253410510419"><a name="p1253410510419"></a><a name="p1253410510419"></a>Pulse Code Modulation</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p2534195115412"><a name="p2534195115412"></a><a name="p2534195115412"></a>脉冲编码调制</p>
</td>
</tr>
<tr id="row1853415110414"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p2534175111412"><a name="p2534175111412"></a><a name="p2534175111412"></a><strong id="b182967391354"><a name="b182967391354"></a><a name="b182967391354"></a>PHY</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p65340511415"><a name="p65340511415"></a><a name="p65340511415"></a>Physical Sublayer & Physical Layer</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p125341511742"><a name="p125341511742"></a><a name="p125341511742"></a>物理子层,物理层</p>
</td>
</tr>
<tr id="row13534551341"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1653518513412"><a name="p1653518513412"></a><a name="p1653518513412"></a><strong id="b10296123913352"><a name="b10296123913352"></a><a name="b10296123913352"></a>PLL</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p135354519420"><a name="p135354519420"></a><a name="p135354519420"></a>Phase-Locked Loop</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1453545111412"><a name="p1453545111412"></a><a name="p1453545111412"></a>锁相环</p>
</td>
</tr>
<tr id="row553519514416"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p35354519417"><a name="p35354519417"></a><a name="p35354519417"></a><strong id="b1429613983518"><a name="b1429613983518"></a><a name="b1429613983518"></a>PWM</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p753565112420"><a name="p753565112420"></a><a name="p753565112420"></a>Pulse Width Modulation</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p165356512044"><a name="p165356512044"></a><a name="p165356512044"></a>脉宽调制</p>
</td>
</tr>
<tr id="row05357515411"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p853575114412"><a name="p853575114412"></a><a name="p853575114412"></a><strong id="b6297113912351"><a name="b6297113912351"></a><a name="b6297113912351"></a></strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row16535251446"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1153518511247"><a name="p1153518511247"></a><a name="p1153518511247"></a><strong id="b19297113923510"><a name="b19297113923510"></a><a name="b19297113923510"></a>Q</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row13535135111418"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p75357519416"><a name="p75357519416"></a><a name="p75357519416"></a><strong id="b1529713911354"><a name="b1529713911354"></a><a name="b1529713911354"></a>QAM</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p753519511246"><a name="p753519511246"></a><a name="p753519511246"></a>Quadrature Amplitude Modulation</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1753519511745"><a name="p1753519511745"></a><a name="p1753519511745"></a>正交幅度调制、正交调幅</p>
</td>
</tr>
<tr id="row115359511448"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1453512511941"><a name="p1453512511941"></a><a name="p1453512511941"></a><strong id="b3297163973517"><a name="b3297163973517"></a><a name="b3297163973517"></a></strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row1553515511743"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p953519510411"><a name="p953519510411"></a><a name="p953519510411"></a><strong id="b11297163913356"><a name="b11297163913356"></a><a name="b11297163913356"></a>R</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row95351351641"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p145351351546"><a name="p145351351546"></a><a name="p145351351546"></a><strong id="b1129743916357"><a name="b1129743916357"></a><a name="b1129743916357"></a>RAM</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p11535165116418"><a name="p11535165116418"></a><a name="p11535165116418"></a>Random Access Memory</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p25351751445"><a name="p25351751445"></a><a name="p25351751445"></a>随机存取存储器</p>
</td>
</tr>
<tr id="row553519514411"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p165356516415"><a name="p165356516415"></a><a name="p165356516415"></a><strong id="b1329773912352"><a name="b1329773912352"></a><a name="b1329773912352"></a>RC</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p553511511745"><a name="p553511511745"></a><a name="p553511511745"></a>Readable Only and Self Cleaning after Reading</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p8535451144"><a name="p8535451144"></a><a name="p8535451144"></a>读清</p>
</td>
</tr>
<tr id="row1553555117417"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p115351651347"><a name="p115351651347"></a><a name="p115351651347"></a><strong id="b0297173953515"><a name="b0297173953515"></a><a name="b0297173953515"></a>RMII</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p0535451149"><a name="p0535451149"></a><a name="p0535451149"></a>Reduced Media Independent Interface</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p2053511515411"><a name="p2053511515411"></a><a name="p2053511515411"></a>简化的介质无关接口</p>
</td>
</tr>
<tr id="row25351251841"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1353505111411"><a name="p1353505111411"></a><a name="p1353505111411"></a><strong id="b1329833943510"><a name="b1329833943510"></a><a name="b1329833943510"></a>RO</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p35356517418"><a name="p35356517418"></a><a name="p35356517418"></a>Read Only</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1053565119419"><a name="p1053565119419"></a><a name="p1053565119419"></a>只读</p>
</td>
</tr>
<tr id="row15535165112418"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p75351451741"><a name="p75351451741"></a><a name="p75351451741"></a><strong id="b2029811392353"><a name="b2029811392353"></a><a name="b2029811392353"></a>ROM</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p17535195113412"><a name="p17535195113412"></a><a name="p17535195113412"></a>Read Only Memory</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1453520512411"><a name="p1453520512411"></a><a name="p1453520512411"></a>只读存储器</p>
</td>
</tr>
<tr id="row205350516418"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p155353518419"><a name="p155353518419"></a><a name="p155353518419"></a><strong id="b122985399357"><a name="b122985399357"></a><a name="b122985399357"></a>RPU</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p18535175118413"><a name="p18535175118413"></a><a name="p18535175118413"></a>Routing Proccess Unit</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p85359511649"><a name="p85359511649"></a><a name="p85359511649"></a>路由协议处理模块</p>
</td>
</tr>
<tr id="row17535651241"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p115353515417"><a name="p115353515417"></a><a name="p115353515417"></a><strong id="b122984397356"><a name="b122984397356"></a><a name="b122984397356"></a>RST</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1553515511748"><a name="p1553515511748"></a><a name="p1553515511748"></a>Reset</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p653511517411"><a name="p653511517411"></a><a name="p653511517411"></a>复位</p>
</td>
</tr>
<tr id="row12535155113412"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p953517511647"><a name="p953517511647"></a><a name="p953517511647"></a><strong id="b8298439113518"><a name="b8298439113518"></a><a name="b8298439113518"></a>RTT</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p155362511045"><a name="p155362511045"></a><a name="p155362511045"></a>Radio Transmission Technology</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1253610515412"><a name="p1253610515412"></a><a name="p1253610515412"></a>无线传输技术</p>
</td>
</tr>
<tr id="row20536151144"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p553614511649"><a name="p553614511649"></a><a name="p553614511649"></a><strong id="b15298639123517"><a name="b15298639123517"></a><a name="b15298639123517"></a>RX</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1753685115411"><a name="p1753685115411"></a><a name="p1753685115411"></a>Reception</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p153613518412"><a name="p153613518412"></a><a name="p153613518412"></a>接收</p>
</td>
</tr>
<tr id="row1653614511443"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p16536205111413"><a name="p16536205111413"></a><a name="p16536205111413"></a><strong id="b1329853973517"><a name="b1329853973517"></a><a name="b1329853973517"></a></strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row155363517418"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p3536951948"><a name="p3536951948"></a><a name="p3536951948"></a><strong id="b32996392350"><a name="b32996392350"></a><a name="b32996392350"></a>S</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row45361513420"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p95361351143"><a name="p95361351143"></a><a name="p95361351143"></a><strong id="b2299123910359"><a name="b2299123910359"></a><a name="b2299123910359"></a>SATA</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p17536175118412"><a name="p17536175118412"></a><a name="p17536175118412"></a>Serial Advanced Technology Attachment</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1953675117410"><a name="p1953675117410"></a><a name="p1953675117410"></a>串行高级连接器</p>
</td>
</tr>
<tr id="row1553616512415"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p253610511843"><a name="p253610511843"></a><a name="p253610511843"></a><strong id="b72992393354"><a name="b72992393354"></a><a name="b72992393354"></a>SCI</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p115360511247"><a name="p115360511247"></a><a name="p115360511247"></a>Smart Card Interface</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p195361851947"><a name="p195361851947"></a><a name="p195361851947"></a>智能卡接口</p>
</td>
</tr>
<tr id="row653611511147"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p3536651345"><a name="p3536651345"></a><a name="p3536651345"></a><strong id="b162991539103510"><a name="b162991539103510"></a><a name="b162991539103510"></a>SCL</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1153685119410"><a name="p1153685119410"></a><a name="p1153685119410"></a>Serial Clock Line</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1253618516416"><a name="p1253618516416"></a><a name="p1253618516416"></a>串行时钟线</p>
</td>
</tr>
<tr id="row1353618514415"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p175369511147"><a name="p175369511147"></a><a name="p175369511147"></a><strong id="b529920399352"><a name="b529920399352"></a><a name="b529920399352"></a>SDA</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p125361051243"><a name="p125361051243"></a><a name="p125361051243"></a>Serial Data and Address</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1953616511540"><a name="p1953616511540"></a><a name="p1953616511540"></a>串行数据地址线</p>
</td>
</tr>
<tr id="row45369511349"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p453618511848"><a name="p453618511848"></a><a name="p453618511848"></a><strong id="b11299143919353"><a name="b11299143919353"></a><a name="b11299143919353"></a>SDH</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p253618511249"><a name="p253618511249"></a><a name="p253618511249"></a>Synchronous Digital Hierarchy</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1353665117417"><a name="p1353665117417"></a><a name="p1353665117417"></a>同步数字体系</p>
</td>
</tr>
<tr id="row95364511649"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p165361451546"><a name="p165361451546"></a><a name="p165361451546"></a><strong id="b1429983914358"><a name="b1429983914358"></a><a name="b1429983914358"></a>SDI</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p15536195117412"><a name="p15536195117412"></a><a name="p15536195117412"></a>Service Defect Indication</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p953655116413"><a name="p953655116413"></a><a name="p953655116413"></a>服务缺陷指示</p>
</td>
</tr>
<tr id="row1853655116420"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p125361951748"><a name="p125361951748"></a><a name="p125361951748"></a><strong id="b1029903993517"><a name="b1029903993517"></a><a name="b1029903993517"></a>SDRAM</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p153619510419"><a name="p153619510419"></a><a name="p153619510419"></a>Synchronous Dynamic Random Access Memory</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p25361651248"><a name="p25361651248"></a><a name="p25361651248"></a>同步动态随机存储器</p>
</td>
</tr>
<tr id="row1653617517411"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p145361351445"><a name="p145361351445"></a><a name="p145361351445"></a><strong id="b1230013914356"><a name="b1230013914356"></a><a name="b1230013914356"></a>SF</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p195361512043"><a name="p195361512043"></a><a name="p195361512043"></a>Spreading Factor</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p153618511242"><a name="p153618511242"></a><a name="p153618511242"></a>扩频因子</p>
</td>
</tr>
<tr id="row135363512415"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p155369511942"><a name="p155369511942"></a><a name="p155369511942"></a><strong id="b93004390354"><a name="b93004390354"></a><a name="b93004390354"></a>SIM</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p15536851145"><a name="p15536851145"></a><a name="p15536851145"></a>Subscriber Identity Module</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p453711518412"><a name="p453711518412"></a><a name="p453711518412"></a>用户标识模块</p>
</td>
</tr>
<tr id="row05371517420"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p35376519412"><a name="p35376519412"></a><a name="p35376519412"></a><strong id="b33001639153516"><a name="b33001639153516"></a><a name="b33001639153516"></a>SIO</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1953718511449"><a name="p1953718511449"></a><a name="p1953718511449"></a>Serial Input / Output</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p35378517418"><a name="p35378517418"></a><a name="p35378517418"></a>串行输入输出接口</p>
</td>
</tr>
<tr id="row7537155110410"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p18537251443"><a name="p18537251443"></a><a name="p18537251443"></a><strong id="b73008391359"><a name="b73008391359"></a><a name="b73008391359"></a>SLC</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p5537175112418"><a name="p5537175112418"></a><a name="p5537175112418"></a>Single level cell</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p853745117414"><a name="p853745117414"></a><a name="p853745117414"></a>单bit存储单元</p>
</td>
</tr>
<tr id="row11537251841"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p14537451540"><a name="p14537451540"></a><a name="p14537451540"></a><strong id="b9301739173516"><a name="b9301739173516"></a><a name="b9301739173516"></a>SMI</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p125378511648"><a name="p125378511648"></a><a name="p125378511648"></a>Short Message Identifier</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p553812518415"><a name="p553812518415"></a><a name="p553812518415"></a>短消息标识</p>
</td>
</tr>
<tr id="row1538251041"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1953815511547"><a name="p1953815511547"></a><a name="p1953815511547"></a><strong id="b163014398353"><a name="b163014398353"></a><a name="b163014398353"></a>SPDIF</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p2053814512418"><a name="p2053814512418"></a><a name="p2053814512418"></a>Sony Philips Digital Interface</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p17538145112410"><a name="p17538145112410"></a><a name="p17538145112410"></a>索尼/菲利普数字音频接口</p>
</td>
</tr>
<tr id="row1553813518418"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p185382512410"><a name="p185382512410"></a><a name="p185382512410"></a><strong id="b10301739143514"><a name="b10301739143514"></a><a name="b10301739143514"></a>SPI</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p953811511541"><a name="p953811511541"></a><a name="p953811511541"></a>SDH Physical Interface</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1953813511245"><a name="p1953813511245"></a><a name="p1953813511245"></a>SDH物理接口</p>
</td>
</tr>
<tr id="row185382512410"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1538651841"><a name="p1538651841"></a><a name="p1538651841"></a><strong id="b113018398359"><a name="b113018398359"></a><a name="b113018398359"></a>SSTL</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1053814511646"><a name="p1053814511646"></a><a name="p1053814511646"></a>Stub Series Terminated Logic</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1453810512413"><a name="p1453810512413"></a><a name="p1453810512413"></a>残余连续终结逻辑</p>
</td>
</tr>
<tr id="row25389511046"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p55381651042"><a name="p55381651042"></a><a name="p55381651042"></a><strong id="b330118396353"><a name="b330118396353"></a><a name="b330118396353"></a>STA</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p145382512413"><a name="p145382512413"></a><a name="p145382512413"></a>Static Timing Analysis</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p453819514410"><a name="p453819514410"></a><a name="p453819514410"></a>静态时序分析</p>
</td>
</tr>
<tr id="row1953805114415"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p10538951540"><a name="p10538951540"></a><a name="p10538951540"></a><strong id="b133011239203516"><a name="b133011239203516"></a><a name="b133011239203516"></a>STR</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p353845114417"><a name="p353845114417"></a><a name="p353845114417"></a>System Test Report</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p453815511541"><a name="p453815511541"></a><a name="p453815511541"></a>系统测试报告</p>
</td>
</tr>
<tr id="row1653812511448"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1553835113417"><a name="p1553835113417"></a><a name="p1553835113417"></a><strong id="b930143993511"><a name="b930143993511"></a><a name="b930143993511"></a>SYNC</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p4538125119412"><a name="p4538125119412"></a><a name="p4538125119412"></a>Synchronization (network)</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p953814511342"><a name="p953814511342"></a><a name="p953814511342"></a>同步（网）</p>
</td>
</tr>
<tr id="row195381351249"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p853825116418"><a name="p853825116418"></a><a name="p853825116418"></a><strong id="b230211396351"><a name="b230211396351"></a><a name="b230211396351"></a></strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row115386513411"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p12538205117419"><a name="p12538205117419"></a><a name="p12538205117419"></a><strong id="b9302439193510"><a name="b9302439193510"></a><a name="b9302439193510"></a>T</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row15538195117413"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1853865112419"><a name="p1853865112419"></a><a name="p1853865112419"></a><strong id="b1530273923520"><a name="b1530273923520"></a><a name="b1530273923520"></a>TFT</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1753811515412"><a name="p1753811515412"></a><a name="p1753811515412"></a>Thin Film Transistor</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p95387511942"><a name="p95387511942"></a><a name="p95387511942"></a>薄膜晶体管</p>
</td>
</tr>
<tr id="row1253835116410"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p6538051848"><a name="p6538051848"></a><a name="p6538051848"></a><strong id="b10303639133518"><a name="b10303639133518"></a><a name="b10303639133518"></a>TSI</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p145381951745"><a name="p145381951745"></a><a name="p145381951745"></a>Time Slot Interchange</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p25385511846"><a name="p25385511846"></a><a name="p25385511846"></a>时隙交换</p>
</td>
</tr>
<tr id="row5538951347"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p053818511345"><a name="p053818511345"></a><a name="p053818511345"></a><strong id="b6303193913516"><a name="b6303193913516"></a><a name="b6303193913516"></a></strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row12538751147"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p18538125117414"><a name="p18538125117414"></a><a name="p18538125117414"></a><strong id="b1330353993515"><a name="b1330353993515"></a><a name="b1330353993515"></a>U</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row75386515418"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p165389513419"><a name="p165389513419"></a><a name="p165389513419"></a><strong id="b16303103903518"><a name="b16303103903518"></a><a name="b16303103903518"></a>UART</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p75385512415"><a name="p75385512415"></a><a name="p75385512415"></a>Universal Asynchronous Receiver & Transmitter</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p253819511046"><a name="p253819511046"></a><a name="p253819511046"></a>通用异步收发器</p>
</td>
</tr>
<tr id="row4538135113418"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p20538195112412"><a name="p20538195112412"></a><a name="p20538195112412"></a><strong id="b17304039113518"><a name="b17304039113518"></a><a name="b17304039113518"></a>USB</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1553919511240"><a name="p1553919511240"></a><a name="p1553919511240"></a>Universal Serial Bus</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p14539951246"><a name="p14539951246"></a><a name="p14539951246"></a>通用串行总线</p>
</td>
</tr>
<tr id="row0539145112411"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p253925112418"><a name="p253925112418"></a><a name="p253925112418"></a><strong id="b2304153910359"><a name="b2304153910359"></a><a name="b2304153910359"></a></strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row95391751343"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p253912512411"><a name="p253912512411"></a><a name="p253912512411"></a><strong id="b630414394354"><a name="b630414394354"></a><a name="b630414394354"></a>V</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row195390511548"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p125395511647"><a name="p125395511647"></a><a name="p125395511647"></a><strong id="b930423915352"><a name="b930423915352"></a><a name="b930423915352"></a>VI</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p1353915518414"><a name="p1353915518414"></a><a name="p1353915518414"></a>Video Input</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p35394511649"><a name="p35394511649"></a><a name="p35394511649"></a>视频输入</p>
</td>
</tr>
<tr id="row55391751941"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p15539185116413"><a name="p15539185116413"></a><a name="p15539185116413"></a><strong id="b1130453953520"><a name="b1130453953520"></a><a name="b1130453953520"></a>VO</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p16539195120410"><a name="p16539195120410"></a><a name="p16539195120410"></a>Video Output</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p16539155118413"><a name="p16539155118413"></a><a name="p16539155118413"></a>视频输出</p>
</td>
</tr>
<tr id="row125391512418"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p15539151448"><a name="p15539151448"></a><a name="p15539151448"></a><strong id="b1330419394350"><a name="b1330419394350"></a><a name="b1330419394350"></a>VOU</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p2053945116411"><a name="p2053945116411"></a><a name="p2053945116411"></a>Video Output Unit</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p17539115116412"><a name="p17539115116412"></a><a name="p17539115116412"></a>视频输出单元</p>
</td>
</tr>
<tr id="row35396511346"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p175392511041"><a name="p175392511041"></a><a name="p175392511041"></a><strong id="b12304113916358"><a name="b12304113916358"></a><a name="b12304113916358"></a></strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row1153918512418"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1053913514416"><a name="p1053913514416"></a><a name="p1053913514416"></a><strong id="b2305143910352"><a name="b2305143910352"></a><a name="b2305143910352"></a>W</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%">&nbsp;&nbsp;</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%">&nbsp;&nbsp;</td>
</tr>
<tr id="row85391251249"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p9539105119417"><a name="p9539105119417"></a><a name="p9539105119417"></a><strong id="b193054391358"><a name="b193054391358"></a><a name="b193054391358"></a>WDG</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p2053975117410"><a name="p2053975117410"></a><a name="p2053975117410"></a>Watch Dog</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p1453919519418"><a name="p1453919519418"></a><a name="p1453919519418"></a>看门狗</p>
</td>
</tr>
<tr id="row553914511849"><td class="nocellnorowborder" style="border:none" valign="top" width="21.84%"><p id="p1153945112417"><a name="p1153945112417"></a><a name="p1153945112417"></a><strong id="b10305183920353"><a name="b10305183920353"></a><a name="b10305183920353"></a>WE</strong></p>
</td>
<td class="nocellnorowborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p16539125112415"><a name="p16539125112415"></a><a name="p16539125112415"></a>Wrap Enable</p>
</td>
<td class="cell-norowborder" style="border:none" valign="top" width="39%"><p id="p25391515410"><a name="p25391515410"></a><a name="p25391515410"></a>倒换使能</p>
</td>
</tr>
<tr id="row15539851849"><td class="row-nocellborder" style="border:none" valign="top" width="21.84%"><p id="p153912511041"><a name="p153912511041"></a><a name="p153912511041"></a><strong id="b1530553913355"><a name="b1530553913355"></a><a name="b1530553913355"></a>WP</strong></p>
</td>
<td class="row-nocellborder" style="border:none" valign="top" width="39.160000000000004%"><p id="p553914517411"><a name="p553914517411"></a><a name="p553914517411"></a>Wireless Profile</p>
</td>
<td class="cellrowborder" style="border:none" valign="top" width="39%"><p id="p15539115114418"><a name="p15539115114418"></a><a name="p15539115114418"></a>无线适配的</p>
</td>
</tr>
</tbody>
</table>

