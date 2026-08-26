# GUI指南<a name="ZH-CN_TOPIC_0000002399739733"></a>

HiSpark Studio支持创建GUI工程和GUI模拟器的使用。按照“新建工程”指导新建Brandy工程后，单击工具栏菜单下的“创建GUI应用”图标可在Brandy的工程中创建GUI工程。

> ![](public_sys-resources/icon-note.gif) **说明：**
> Linux/WSL环境下不支持本章节功能。
> 仅Brandy/3322系列芯片支持本章节功能。

**图 1** 创建GUI工程<a name="fig1874373411538"></a>
<img style="display:block;" src="figures/创建GUI工程.png" width="700" alt="创建GUI工程">

- 像素值：默认454×454对应生成的画布大小，在形状为circle（圆形）时，分辨率为直径×直径，当创建圆形且分辨率的两个像素值不相等时，取默认466×466，在形状为rectangle（矩形）时，分辨率为长×宽。像素值可以自定义，取值范围为1～1024。
- 形状：分为circle（圆形）和rectangle（矩形），如果不主动选择，默认为圆形。

> ![](public_sys-resources/icon-note.gif) **说明：**
> 使用GUI模拟器前，需要将对应的资源res复制到“software\\code\\sdk\\application\\wearable”中。HiDiTing SDK不需要进行上述复制操作。

- **GUI界面介绍**
- **模拟器效果展示方法**
- **图形工具介绍**
- **GUI工程使用常见问题**

## GUI界面介绍<a name="ZH-CN_TOPIC_0000002366099950"></a>

- **GUI拖拽界面介绍**
- **页面树介绍**
- **组件介绍**

### GUI拖拽界面介绍<a name="ZH-CN_TOPIC_0000002399619865"></a>

GUI工程创建后，会在工程目录“application/wearable/nativeapp/nativeui/应用名”下创建一个以工程名命名的GUI文件，打开后会呈现表盘形状，可自定义表盘内容。

当前支持的组件包括Button、Image、Progress、List、Label、ToggleButton、CheckBox、RadioButton、LabelButton、ScrollView、CircleProgress、ArcLabel、SwipeView、TextureMapper、Slider、Picker、TimePicker、Chart、EditText、ImageAnimator、DigitalClock、Qrcode、AnalogClock、SweepClock、Coverflow、Barcode、CardPage、CrossView、MapView、RollerView、HexagonsList、IcosahedronView、CanvasExt、TransformList、SlipflowView、TransformGroup、Coverflow2、ParticleView组件和Root组件。

**图 1** GUI拖拽界面<a name="fig1973444016553"></a>

<img style="display:block;" src="figures/gui8.png" width="700">

- FileTree：页面树，可以选择添加、删除页面、修改页面标题、设置主页面。
- UI Control：UI组件栏，可以将相应的组件选中并拖动到画布（Canvas）中，实现组件的添加。
- Component Tree：组件树，在低代码开发界面中，开发者可以直观地看到组件的层级结构和摘要信息。开发者可以通过选中组件树中的组件（画布中对应的组件被同步选中），实现画布内组件的快速定位；单击组件后的“<img src="figures/Y.png" width="17">”，可以隐藏/显示相应的组件。
- Panel：功能面板，包括CrossView、Coverflow2组件用到的子组件切换，以及常用的画布缩小放大、组件左对齐、垂直居中对齐、右对齐、顶对齐、水平居中对齐、底对齐、图层切换、撤销、显示/隐藏组件虚拟边框、一键生成C++代码等。
- Canvas：画布，开发者可在此区域对组件进行拖拽、拉伸等可视化操作，构建UI界面布局效果。
- Attributes & Styles：属性样式栏，选中画布中的相应组件后，在右侧属性样式栏可以对该组件的属性样式进行配置。
  - General：对应图标<img src="figures/zh-cn_image_0000002366100070.png" width="17">，用于设置Width、Height、Background、Position、Display等常规样式。
  - Feature：对应图标<img src="figures/zh-cn_image_0000002399619989.png" width="27">，用于设置组件的特有样式，如描述Text组件文字大小的FontSize样式等。
  - Events：对应图标<img src="figures/zh-cn_image_0000002365940174.png" width="22">，为组件绑定相关事件，并设置绑定事件的回调函数。

### 页面树介绍<a name="ZH-CN_TOPIC_0000002484446082"></a>

- **页面的新增删除修改标题设置主页**

#### 页面的新增删除修改标题设置主页<a name="ZH-CN_TOPIC_0000002516526041"></a>

- 页面新增

  点击FileTree新增页面按钮，可新增空白页面。

  **图 1** 页面新增<a name="fig84442050152819"></a>
  <img style="display:block;" src="figures/页面新增.png" width="700" alt="页面新增">

- 页面删除

  将鼠标悬浮在需要删除的页面右侧，弹出操作框后，点击Delete按钮，可删除页面。

  **图 2** 页面删除<a name="fig854641933212"></a>
  <img style="display:block;" src="figures/页面删除.png" width="700" alt="页面删除">

- 页面修改标题

  将鼠标悬浮在需要修改标题的页面右侧，弹出操作框后，点击Rename按钮，可修改标题。重命名只能包含字母（A-Z，a-z）、数字（0-9）和下划线（\_），必须以字母开头。

  **图 3** 页面修改标题<a name="fig99631158173419"></a>
  <img style="display:block;" src="figures/页面修改标题.png" width="700" alt="页面修改标题">

- 页面设置主页

  将鼠标悬浮在需要设置主页的页面右侧，弹出操作框后，点击Set HomePage按钮，可设置主页。

  **图 4** 页面设置主页<a name="fig5146716103813"></a>
  <img style="display:block;" src="figures/页面设置主页.png" width="700" alt="页面设置主页">

### 组件介绍<a name="ZH-CN_TOPIC_0000002365940054"></a>

- **组件的复制粘贴删除**
- **组件的共有属性**
- **Button组件**
- **Image组件**
- **Progress组件**
- **List组件**
- **Label组件**
- **ToggleButton组件**
- **CheckBox组件**
- **RadioButton组件**
- **LabelButton组件**
- **ScrollView组件**
- **CircleProgress组件**
- **ArcLabel组件**
- **SwipeView组件**
- **TextureMapper组件**
- **Slider组件**
- **Picker组件**
- **TimePicker组件**
- **Chart组件**
- **EditText组件**
- **DigitalClock组件**
- **ImageAnimator组件**
- **Qrcode组件**
- **AnalogClock组件**
- **SweepClock组件**
- **Coverflow组件**
- **Barcode组件**
- **CardPage组件**
- **CrossView组件**
- **MapView组件**
- **RollerView组件**
- **HexagonsList组件**
- **IcosahedronView组件**
- **CanvasExt组件**
- **TransformList组件**
- **SlipflowView组件**
- **TransformGroup组件**
- **Coverflow2组件**
- **ParticleView组件**
- **LabelExt组件**
- **ChartPillarExt组件**
- **ListNested组件**
- **SwipeViewNested组件**
- **LottieView组件**
- **Root组件**
- **用户代码编辑**
- **组件对齐**
- **组件层级移动**
- **高斯模糊属性**

#### 组件的复制粘贴删除<a name="ZH-CN_TOPIC_0000002399739737"></a>

以Button组件为例，在画布内已经拖入Button组件的前提下进行操作：

- 组件删除

  组件可以通过两种方式删除：
  - 右键点击画布中的Button组件显示操作栏，在弹出的操作栏点击Delete。
  - 选中Button组件，通过键盘Del键删除。

  **图 1** 组件删除<a name="fig1276601114010"></a>
  <img style="display:block;" src="figures/组件删除.png" width="700" alt="组件删除">

- 组件复制

  组件可以通过两种方式复制：
  - 右键点击画布中的Button组件显示操作栏，在弹出的操作栏点击Copy，再次右键后点击Paste，实现复制粘贴。
  - 选中Button组件，通过键盘Ctrl+C和Ctrl+V实现复制粘贴。

  **图 2** 组件复制<a name="fig1175415591409"></a>
  <img style="display:block;" src="figures/组件复制.png" width="700" alt="组件复制">

  **图 3** 组件粘贴<a name="fig14301013164114"></a>
  <img style="display:block;" src="figures/组件粘贴.png" width="700" alt="组件粘贴">

#### 组件的共有属性<a name="ZH-CN_TOPIC_0000002366099954"></a>

以Button组件为例，选中组件栏中的Button组件，将其拖拽至中央画布区域，松开鼠标，实现一个Button组件的添加。（组件会生成在画布上坐标(100,100)的位置）。

**图 1** 拖拽组件<a name="fig10331115148"></a>
<img style="display:block;" src="figures/拖拽组件.png" width="700" alt="拖拽组件">

以下操作需在画布内已经拖入Button组件的前提下进行操作。

- 选中画布内的Button组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399739865.png" width="20">样式图标（General），在展开的General栏中修改Button组件的ID。ID并非生成代码时的变量名，因此多个组件可以设置同一个ID。

  **图 2** 通用属性配置：Id<a name="fig1333343519513"></a>
  <img style="display:block;" src="figures/通用属性配置-Id.png" width="700" alt="通用属性配置-Id">

- 选中画布内的Button组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399620009.png" width="20">样式图标（General），在展开的General栏中修改Button组件的宽高、位置；另外还可以通过拖拽的方式放大缩小Button组件以及改变组件的位置。

  **图 3** 通用属性的配置<a name="fig9966191695113"></a>
  <img style="display:block;" src="figures/通用属性的配置.png" width="700" alt="通用属性的配置">

- 选中Button组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399739869.png" width="20">样式图标（General），在展开的General栏中修改Button组件的BackgroundColor属性改变背景颜色。

  **图 4** 修改背景颜色<a name="fig759121615415"></a>
  <img style="display:block;" src="figures/修改背景颜色.png" width="700" alt="修改背景颜色">

- 选中画布内的Button组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399620013.png" width="20">样式图标（General），在展开的General栏中修改Button组件GaussOption框中的FullScreenState、GaussianBlur属性以改变组件的高斯模糊。该操作需在同时选中两个组件的前提下进行。FullScreenState为false时高斯模糊设置不生效，FullScreenState为true时高斯模糊设置生效。GaussianBlur属性控制高斯模糊的模糊程度。详情请参见“高斯模糊属性”。

  **图 5** 高斯模糊<a name="fig48601252103118"></a>
  <img style="display:block;" src="figures/高斯模糊.png" width="700" alt="高斯模糊">

- 选中画布内的Button组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399739877.png" width="20">样式图标（General），在展开的General栏中修改Button组件Border框中的Width、Color、Radius属性改变边框的样式。

  **图 6** 修改组件边框样式<a name="fig421010341275"></a>
  <img style="display:block;" src="figures/修改组件边框样式.png" width="700" alt="修改组件边框样式">

- 选中Button组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399620017.png" width="20">样式图标（General），在展开的General栏中修改Button组件Margin框中的MarginTop和MarginLeft属性调整组件相对表盘的位置。

  **图 7** 修改组件相对窗口位置<a name="fig19389527155313"></a>
  <img style="display:block;" src="figures/修改组件相对窗口位置.png" width="700" alt="修改组件相对窗口位置">

- 选中Button组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399739897.png" width="20">样式图标（General），在展开的General栏中修改Padding改变组件padding部分四个方向的宽度。

  **图 8** 组件相对边框位置<a name="fig88161839549"></a>
  <img style="display:block;" src="figures/组件相对边框位置.png" width="700" alt="组件相对边框位置">

#### Button组件<a name="ZH-CN_TOPIC_0000002399619869"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中画布内的Button组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399620053.png" width="36">样式图标（Feature），在展开的Feature栏中修改Button组件的DefaultImgSrc属性加载图片。

  **图 1** DefaultImgSrc属性配置<a name="fig1930105513132"></a>
  <img style="display:block;" src="figures/DefaultImgSrc属性配置.png" width="700" alt="DefaultImgSrc属性配置">

- 选中画布内的Button组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399739953.png" width="36">样式图标（Feature），在展开的Feature栏中修改Button组件的ImageX和ImageY属性调整图片位置（修改前需要设置DefaultImgSrc属性）。

  **图 2** ImageX/ImageY属性配置<a name="fig11684412161613"></a>
  <img style="display:block;" src="figures/ImageX-ImageY属性配置.png" width="700" alt="ImageX-ImageY属性配置">

- 选中画布内的Button组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399620097.png" width="36">样式图标（Feature），在展开的Feature栏中修改Button组件的ImageOpacity属性调整图片透明度（需要设置DefaultImgSrc）。

  **图 3** ImageOpacity属性配置<a name="fig11511623928"></a>
  <img style="display:block;" src="figures/ImageOpacity属性配置.png" width="700" alt="ImageOpacity属性配置">

- 选中画布内的Button组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399739961.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  Button组件支持的事件有：OnClick、OnLongPress、OnPress、OnCancel和OnRelease。

  **图 4** 回调事件配置<a name="fig141561846154620"></a>
  <img style="display:block;" src="figures/回调事件配置.png" width="700" alt="回调事件配置">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的MarginBottom属性和MarginRight属性无界面渲染效果。
> - Feature页面下的TriggeredImgSrc属性、TriggeredBackgroundColor属性、TriggeredBorderColor属性无界面渲染效果，可以在模拟器上查看渲染效果。
> - DefaultImgSrc和TriggeredImgSrc不支持中文路径。

#### Image组件<a name="ZH-CN_TOPIC_0000002365940058"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中画布内的Image组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399620105.png" width="36">样式图标（Feature），在展开的Feature栏中修改Image组件的ImagePath属性加载图片。
  在已有选中图片情况下再次选择相同图片，或者在浏览文件时关闭窗口或单击取消时，界面渲染效果将不会改变。需要清空图片可以删除输入框中的文本。
  **图 1** 特有属性配置：ImagePath<a name="fig1383616220353"></a>
  <img style="display:block;" src="figures/特有属性配置-ImagePath.png" width="700" alt="特有属性配置-ImagePath">
  > ![](public_sys-resources/icon-note.gif) **说明：**
  > ImagePath不支持中文路径。
  > 导入的Bin文件必须是图片转的Bin，否则模拟器会异常。
- 选中画布内的Image组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399739965.png" width="36">样式图标（Feature），在展开的Feature栏中修改Image组件的ImageOpacity属性调整图片透明度。

  **图 2** 特有属性配置：ImageOpacity<a name="fig19953128113813"></a>
  <img style="display:block;" src="figures/特有属性配置-ImageOpacity.png" width="700" alt="特有属性配置-ImageOpacity">

- 选中画布内的Image组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399620109.png" width="36">样式图标（Feature），在展开的Feature栏中修改Image组件的AutoEnable属性。
  - AutoEnable属性设置为true时，组件会被限制为图片本身的大小，无法通过拖拽组件或直接修改Width/Height值来修改组件的显示效果。
  - AutoEnable属性设置为false时，会按照组件大小展示图片，设置不同的ImageResizeMode属性值可以呈现不同的显示效果。

  **图 3** 特有属性配置：AutoEnable<a name="fig32031181480"></a>
  <img style="display:block;" src="figures/特有属性配置-AutoEnable.png" width="700" alt="特有属性配置-AutoEnable">

- 选中画布内的Image组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399739969.png" width="36">样式图标（Feature），在展开的Feature栏中修改Image组件的ImageResizeMode属性。
  - AutoEnable属性设置为true时，ImageResizeMode属性不生效。
  - AutoEnable属性设置为false时，ImageResizeMode生效，对应不同的显示效果。
  当前共有6种模式对应的效果示例如下（图片原始尺寸为80×80）：
  - ImageResizeMode - None

    **图 4** 图片平铺（图中组件大小为200×200）<a name="fig137143716018"></a>
    <img style="display:block;" src="figures/图片平铺（图中组件大小为200-200）.png" width="700" alt="图片平铺（图中组件大小为200-200）">

  - ImageResizeMode - Cover

    **图 5** 图片覆盖组件1（图中组件大小为100×200）<a name="fig203183291602"></a>
    <img style="display:block;" src="figures/图片覆盖组件1（图中组件大小为100-200）.png" width="700" alt="图片覆盖组件1（图中组件大小为100-200）">

    **图 6** 图片覆盖组件2（图中组件大小为200×100）<a name="fig119815431203"></a>
    <img style="display:block;" src="figures/图片覆盖组件2（图中组件大小为200-100）.png" width="700" alt="图片覆盖组件2（图中组件大小为200-100）">

  - ImageResizeMode - Contain

    **图 7** 图片被组件包含在内（图中组件大小为100×200）<a name="fig9776119513"></a>
    <img style="display:block;" src="figures/图片被组件包含在内（图中组件大小为100-200）.png" width="700" alt="图片被组件包含在内（图中组件大小为100-200）">

    **图 8** 图片被组件包含在内（图中组件大小为200×100）<a name="fig1741815478118"></a>
    <img style="display:block;" src="figures/图片被组件包含在内（图中组件大小为200-100）.png" width="700" alt="图片被组件包含在内（图中组件大小为200-100）">

  - ImageResizeMode - Fill

    **图 9** 图片填满组件（图中组件大小为200×100）<a name="fig143226171166"></a>
    <img style="display:block;" src="figures/图片填满组件（图中组件大小为200-100）.png" width="700" alt="图片填满组件（图中组件大小为200-100）">

  - ImageResizeMode - Center
        **图 10**  图片处在组件中心（图中组件大小为100×100）<a name="fig78523241168"></a>
    <img style="display:block;" src="figures/图片处在组件中心（图中组件大小为100-100）.png" width="700" alt="图片处在组件中心（图中组件大小为100-100）">
        
        > ![](public_sys-resources/icon-note.gif) **说明：**
        > 组件宽高任一为0时，图片隐藏。
  - ImageResizeMode - Scale Down

    **图 11** 组件宽高较大时，图片按原有尺寸显示<a name="fig1319195718418"></a>
    <img style="display:block;" src="figures/组件宽高较大时-图片按原有尺寸显示.png" width="700" alt="组件宽高较大时-图片按原有尺寸显示">

    **图 12** 组件宽高较小时，图片会缩小并被组件包含在内<a name="fig89661415359"></a>
    <img style="display:block;" src="figures/组件宽高较小时-图片会缩小并被组件包含在内.png" width="700" alt="组件宽高较小时-图片会缩小并被组件包含在内">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - 组件的特有属性ImagePath未设置时，模拟器中不会显示组件。
> - General页面下的MarginBottom属性和MarginRight属性没有任何界面渲染效果，可在模拟器上查看效果。
> - Feature页面下的BlurLevel属性和Algorithm属性没有任何界面渲染效果，可在模拟器上查看效果。
> - Image组件不支持配置回调事件。

#### Progress组件<a name="ZH-CN_TOPIC_0000002399739741"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中Progress组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399620153.png" width="36">样式图标（Feature），在展开的Feature栏中ForegroundStyle窗口中修改Progress组件的前景色。

  **图 1** 修改前景色<a name="fig117331435123510"></a>
  <img style="display:block;" src="figures/修改前景色.png" width="700" alt="修改前景色">

- 选中Progress组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399740017.png" width="36">样式图标（Feature），在展开的Feature栏中BackgroundStyle窗口中修改Progress组件的背景色。

  **图 2** 修改背景色<a name="fig879142417363"></a>
  <img style="display:block;" src="figures/修改背景色.png" width="700" alt="修改背景色">

- 选中Progress组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399620157.png" width="36">样式图标（Feature），在展开的Feature栏中修改Progress组件的ProgressWidth和ProgressHeight属性改变组件的宽度和高度。

  **图 3** 修改组件宽高<a name="fig119251539922"></a>
  <img style="display:block;" src="figures/修改组件宽高.png" width="700" alt="修改组件宽高">

- 选中Progress组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399740029.png" width="36">样式图标（Feature），在展开的Feature栏中修改Progress组件的Direction属性以修改进度条方向。

  **图 4** 修改进度条方向<a name="fig4795118183012"></a>
  <img style="display:block;" src="figures/修改进度条方向.png" width="700" alt="修改进度条方向">

- 选中Progress组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399620269.png" width="36">样式图标（Feature），在展开的Feature栏中修改Progress组件的Value属性以修改进度。

  **图 5** 修改进度<a name="fig18362191916365"></a>
  <img style="display:block;" src="figures/修改进度.png" width="700" alt="修改进度">

- 选中Progress组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399740281.png" width="36">样式图标（Feature），在展开的Feature栏中修改Progress组件的ForeImage属性添加已走过进度的图片和BackImage属性添加进度条整体的图片。路径不能为空，不支持中文路径。

  **图 6** 添加图片<a name="fig9386125012810"></a>
  <img style="display:block;" src="figures/添加图片.png" width="700" alt="添加图片">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的BackgroungColor属性，MarginBottom属性和MarginRight属性暂无渲染效果。
> - Feature页面下的ForegroundStyle和BackgroundStyle的子属性BorderWidth、BorderColor、BorderRadius、LineWidth、LineHeight、LineColor、ImageOpacity属性暂无渲染效果。
> - Progress组件不支持配置回调事件。

#### List组件<a name="ZH-CN_TOPIC_0000002366099958"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中List组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399620549.png" width="36">样式图标（Feature），在展开的Feature栏中修改itemHeight属性设置所有子项的高度；修改itemWidth属性设置所有子项的宽度；修改imageWidth属性设置所有子项图片的宽度；修改imageHeight属性设置所有子项图片的高度；修改FontSize属性设置所有子项的字体大小；点击Item栏右侧的加号添加子项，修改子项中的Text属性和ImagePath属性添加文本和图片。

  **图 1** 添加子项<a name="fig28061923305"></a>
  <img style="display:block;" src="figures/添加子项.png" width="700" alt="添加子项">

- 选中List组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399740433.png" width="36">样式图标（Feature），在展开的Feature栏中修改List组件的OffsetX属性设置所有子项的横向偏移，修改OffsetY属性设置所有子项的纵向偏移。

  **图 2** 修改子项的偏移<a name="fig1020210122313"></a>
  <img style="display:block;" src="figures/修改子项的偏移.png" width="700" alt="修改子项的偏移">

- 选中List组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399620589.png" width="36">样式图标（Feature），在展开的Feature栏中修改List组件的Direction属性设置列表的排列方向。

  **图 3** 修改列表的排列方向<a name="fig56791215114412"></a>
  <img style="display:block;" src="figures/修改列表的排列方向.png" width="700" alt="修改列表的排列方向">

- 选中画布内的List组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399740481.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  List组件支持的事件有：OnClick、OnLongPress、OnDrag、OnDragStart、OnDragEnd、OnPress、OnCancel、OnRelease、OnFocus和OnBlur。

  **图 4** 回调事件配置<a name="fig186332171075"></a>
  <img style="display:block;" src="figures/回调事件配置-1.png" width="700" alt="回调事件配置-1">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的MarginBottom属性和MarginRight属性无渲染效果。
> - Feature页面下的Isloop属性、Autoalign属性、Aligntime属性、Startindex属性均没有界面渲染效果，在添加子元素后可在模拟器查看效果。
> - 目前删除子项的最后一个元素会出现无法删除的问题，如需删除，可以在关闭界面的状态下在index.visual中将属性listItemText和listItemPath删除。

#### Label组件<a name="ZH-CN_TOPIC_0000002399619873"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中画布内的Label组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399620633.png" width="36">样式图标（Feature），在展开的Feature栏中修改Label组件的Text属性来编辑文本内容（新添加组件默认文本内容为“default”）。

  **图 1** 特有属性配置：Text文本内容<a name="fig455274919252"></a>
  <img style="display:block;" src="figures/特有属性配置-Text文本内容.png" width="700" alt="特有属性配置-Text文本内容">

- 选中画布内的Label组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399740537.png" width="36">样式图标（Feature），在展开的Feature栏中设置Label组件的Font属性：
  - Color：字体颜色
  - Size：字体大小
  - LetterSpace：字母间距
  - LineSpace：行间距
  - LineHeight：行高（行高小于字体大小时将以字体大小为准，最终行高＝行高＋行间距）
  - TextDirection：文本方向

  **图 2** 通用属性配置：文本相关属性<a name="fig15826115915219"></a>
  <img style="display:block;" src="figures/通用属性配置-文本相关属性.png" width="700" alt="通用属性配置-文本相关属性">

- 选中画布内的Label组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399620677.png" width="36">样式图标（Feature），在展开的Feature栏中修改Label组件的TextAlign属性改变文字的横向与纵向排布。

  **图 3** 改变文字排布<a name="fig195425918268"></a>
  <img style="display:block;" src="figures/改变文字排布.png" width="700" alt="改变文字排布">

- 选中画布内的Label组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399740593.png" width="36">样式图标（Feature），在展开的Feature栏中修改Label组件的LineBreakMode属性。LineBreakMode对应6种换行模式，详细介绍如下：
  - Adapt：组件大小自适应文本，且不会对文本做自动换行。

    > ![](public_sys-resources/icon-note.gif) **说明：**
    > 组件宽高不受通用属性Width/Height值影响，因此不可通过拖拽组件或直接修改Width/Height值的方式改变组件宽高。

    **图 4** LineBreakMode - Adapt<a name="fig1679161320461"></a>
    <img style="display:block;" src="figures/LineBreakMode---Adapt.png" width="700" alt="LineBreakMode---Adapt">

  - Stretch：组件高度按照设置的Height值显示，宽度由文本中最长的行决定，文本不会自动换行。

    > ![](public_sys-resources/icon-note.gif) **说明：**
    > 组件宽度不受通用属性Width值影响，因此不可通过拖拽组件或直接修改Width值的方式改变组件宽度。

    **图 5** LineBreakMode - Stretch<a name="fig8791181319462"></a>
    <img style="display:block;" src="figures/LineBreakMode---Stretch.png" width="700" alt="LineBreakMode---Stretch">

  - Wrap：组件宽度按照设置的Width值显示，文本自动换行，组件高度由文本行数决定。

    > ![](public_sys-resources/icon-note.gif) **说明：**
    > 组件高度不受通用属性Height值影响，因此不可通过拖拽组件或直接修改Height值的方式改变组件高度。

    **图 6** LineBreakMode - Wrap<a name="fig177911513124619"></a>
    <img style="display:block;" src="figures/LineBreakMode---Wrap.png" width="700" alt="LineBreakMode---Wrap">

  - Ellipsis：组件大小按照设置的Height和Width值显示，文本自动换行，超出组件的文本将在末尾以省略号的形式显示。

    **图 7** LineBreakMode - Ellipsis<a name="fig1179181314462"></a>
    <img style="display:block;" src="figures/LineBreakMode---Ellipsis.png" width="700" alt="LineBreakMode---Ellipsis">

  - Clip：组件大小按照设置的Height和Width值显示，文本自动换行，超出组件的文本将在末尾自动隐藏。

    **图 8** LineBreakMode - Clip<a name="fig14791191324610"></a>
    <img style="display:block;" src="figures/LineBreakMode---Clip.png" width="700" alt="LineBreakMode---Clip">

  - Marquee：组件大小按照设置的Height和Width值显示，文本不自动换行，超出组件的文本将自动隐藏。

    > ![](public_sys-resources/icon-note.gif) **说明：**
    > 此模式下如果单行文本长度不超出组件时，文本按照设置的TextAlign进行对齐。
    > 文本长度超出组件时，文本会自动向左循环滚动播放。

    **图 9** LineBreakMode - Marquee<a name="fig530611174710"></a>
    <img style="display:block;" src="figures/LineBreakMode---Marquee.png" width="700" alt="LineBreakMode---Marquee">

- 选中画布内的Label组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941030.png" width="36">样式图标（Feature），在展开的Feature栏中修改Label组件的RollAnimation属性。

  RollAnimation属性只在LineBreakMode为Marquee且文本长度超出时生效。RollAnimation包含滚动速度（Speed）和滚动起始位置（Pos）。

  **图 10** 特有属性配置：RollAnimation<a name="fig19196141194615"></a>
  <img style="display:block;" src="figures/特有属性配置-RollAnimation.png" width="700" alt="特有属性配置-RollAnimation">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的MarginBottom属性和MarginRight属性没有任何界面渲染效果，可在模拟器上查看效果。
> - Label组件不支持配置回调事件。

#### ToggleButton组件<a name="ZH-CN_TOPIC_0000002365940062"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中画布内的ToggleButton组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366100938.png" width="36">样式图标（Feature），在展开的Feature栏中修改ToggleButton组件的ImageOpacity属性以修改图片透明度。

  **图 1** 修改图片透明度<a name="fig18996545134711"></a>
  <img style="display:block;" src="figures/修改图片透明度.png" width="700" alt="修改图片透明度">

- 选中ToggleButton组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941090.png" width="36">样式图标（Feature），在展开的Feature栏中修改ToggleButton组件的State属性改变组件的状态，当属性值为true时为选中状态，反之为未选中状态。

  **图 2** 修改组件状态<a name="fig28061923305"></a>
  <img style="display:block;" src="figures/修改组件状态.png" width="700" alt="修改组件状态">

- 选中ToggleButton组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366100998.png" width="36">样式图标（Feature），在展开的Feature栏中修改ToggleButton组件的UnSelectedImg属性添加未选中时的图片和SelectedImg属性添加选中时的图片，两张图片必须同时存在时才会产生渲染效果，通过将属性UnSelectedImg和SelectedImg恢复成空（手动删除），可以实现图片的删除。

  > ![](public_sys-resources/icon-note.gif) **说明：**
  > 图片不支持中文路径，且路径中不能包含空格。

  **图 3** 添加图片<a name="fig1150615503413"></a>
  <img style="display:block;" src="figures/添加图片-2.png" width="700" alt="添加图片-2">

- 选中画布内的ToggleButton组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941142.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  ToggleButton组件支持的事件有：OnClick、OnLongPress、OnPress、OnCancel、OnRelease和OnChange。

  **图 4** 回调事件配置<a name="fig560310204504"></a>
  <img style="display:block;" src="figures/回调事件配置-3.png" width="700" alt="回调事件配置-3">

> ![](public_sys-resources/icon-note.gif) **说明：**
> General页面下的MarginBottom属性、MarginRight属性暂无渲染效果。

#### CheckBox组件<a name="ZH-CN_TOPIC_0000002399739745"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中画布内的CheckBox组件，在已经添加图片的前提下，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101018.png" width="36">样式图标（Feature），在展开的Feature栏中修改CheckBox组件的ImageOpacity属性以修改图片透明度。

  **图 1** 修改图片透明度<a name="fig2853208115915"></a>
  <img style="display:block;" src="figures/修改图片透明度-4.png" width="700" alt="修改图片透明度-4">

- 选中CheckBox组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941146.png" width="36">样式图标（Feature），在展开的Feature栏中修改CheckBox组件的State属性改变组件的状态，当属性值为Selected时为选中状态，反之为未选中状态。

  **图 2** 修改组件状态<a name="fig3771124145810"></a>
  <img style="display:block;" src="figures/修改组件状态-5.png" width="700" alt="修改组件状态-5">

- 选中CheckBox组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101022.png" width="36">样式图标（Feature），在展开的Feature栏中修改CheckBox组件的UnSelectedImg属性添加未选中时的图片和SelectedImg属性添加选中时的图片，两张图片必须同时存在才会产生渲染效果，通过将属性UnSelectedImg和SelectedImg恢复成空（手动删除），可以实现图片的删除。

  > ![](public_sys-resources/icon-note.gif) **说明：**
  > 图片不支持中文路径，且路径中不能包含空格。

  **图 3** 添加图片<a name="fig1581184025416"></a>
  <img style="display:block;" src="figures/添加图片-6.png" width="700" alt="添加图片-6">

- 选中画布内的CheckBox组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941150.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  CheckBox组件支持的事件有：OnClick、OnLongPress、OnPress、OnCancel、OnRelease和OnChange。

  **图 4** 回调事件配置<a name="fig15393131421110"></a>
  <img style="display:block;" src="figures/回调事件配置-7.png" width="700" alt="回调事件配置-7">

> ![](public_sys-resources/icon-note.gif) **说明：**
> General页面下的MarginTop属性、MarginRight属性无渲染效果。

#### RadioButton组件<a name="ZH-CN_TOPIC_0000002366099962"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中画布内的RadioButton组件，在已经添加图片的前提下，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101026.png" width="36">样式图标（Feature），在展开的Feature栏中修改RadioButton组件的ImageOpacity属性以修改图片透明度。

  **图 1** 修改图片透明度<a name="fig2853208115915"></a>
  <img style="display:block;" src="figures/修改图片透明度-8.png" width="700" alt="修改图片透明度-8">

- 选中RadioButton组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941158.png" width="36">样式图标（Feature），在展开的Feature栏中修改RadioButton组件的State改变组件的状态，当属性值为Selected时为选中状态，反之为未选中状态。

  **图 2** 修改组件状态<a name="fig82077222339"></a>
  <img style="display:block;" src="figures/修改组件状态-9.png" width="700" alt="修改组件状态-9">

- 选中RadioButton组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101034.png" width="36">样式图标（Feature），在展开的Feature栏中修改RadioButton组件的SelectedImg属性添加选中时的图片和UnSelectedImg属性添加未选中时的图片，两张图片必须同时存在才会产生渲染效果，通过将SelectedImg和UnSelectedImg属性恢复成空（手动删除），可以实现图片的删除。
  **图 3** 添加图片效果展示<a name="fig02076225333"></a>
  <img style="display:block;" src="figures/添加图片效果展示.png" width="700" alt="添加图片效果展示">
  > ![](public_sys-resources/icon-note.gif) **说明：**
  > SelectedImg属性和UnSelectedImg属性不支持中文路径。
- 选中画布内的RadioButton组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941162.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  RadioButton组件支持的事件有：OnClick、OnLongPress、OnPress、OnCancel、OnRelease和OnChange。

  **图 4** 回调事件配置<a name="fig14875143917147"></a>
  <img style="display:block;" src="figures/回调事件配置-10.png" width="700" alt="回调事件配置-10">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的MarginBottom属性和MarginRight属性无渲染效果。
> - Feature页面下的Name属性没有任何界面渲染效果。当界面上有2个组件，并且Name属性一样时，模拟器才可以实现状态的切换。

#### LabelButton组件<a name="ZH-CN_TOPIC_0000002399619877"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中LabelButton组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101038.png" width="36">样式图标（Feature），在展开的Feature栏中修改LabelButton组件的ImageOpacity属性可以修改图片的透明度。

  **图 1** 修改图片透明度<a name="fig59341711182514"></a>
  <img style="display:block;" src="figures/修改图片透明度-11.png" width="700" alt="修改图片透明度-11">

- 选中LabelButton组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941166.png" width="36">样式图标（Feature），在展开的Feature栏中修改LabelButton组件的ImageX属性和ImageY属性可以对图片的位置进行调整。

  **图 2** 修改ImageX属性和ImageY属性的效果<a name="fig1747911404612"></a>
  <img style="display:block;" src="figures/修改ImageX属性和ImageY属性的效果.png" width="700" alt="修改ImageX属性和ImageY属性的效果">

- 选中LabelButton组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101042.png" width="36">样式图标（Feature），在展开的Feature栏中修改LabelButton组件的Text属性添加文本。

  **图 3** 添加文本<a name="fig115151856956"></a>
  <img style="display:block;" src="figures/添加文本.png" width="700" alt="添加文本">

- 选中LabelButton组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941170.png" width="36">样式图标（Feature），在展开的Feature栏中设置LabelButton组件的Font属性：
  - Color：字体颜色
  - FontSize：字体大小
  - TextDirection：文本方向

  **图 4** 文本相关属性<a name="fig11349122424720"></a>
  <img style="display:block;" src="figures/文本相关属性.png" width="700" alt="文本相关属性">

- 选中LabelButton组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101046.png" width="36">样式图标（Feature），在展开的Feature栏中修改LabelButton组件的Text Xoffset属性和Text Yoffset属性对文字的位置进行调整。

  **图 5** 对文字位置进行调整<a name="fig335933815438"></a>
  <img style="display:block;" src="figures/对文字位置进行调整.png" width="700" alt="对文字位置进行调整">

- 选中LabelButton组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941186.png" width="36">样式图标（Feature），在展开的Feature栏中修改LabelButton组件的TextAlign属性对文字的水平对齐方式进行调整。

  **图 6** 修改文字的对齐方式<a name="fig0812161817195"></a>
  <img style="display:block;" src="figures/修改文字的对齐方式.png" width="700" alt="修改文字的对齐方式">

- 选中LabelButton组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101066.png" width="36">样式图标（Feature），在展开的Feature栏中修改LabelButton组件的DefaultImgSrc属性可以添加图片，通过将属性DefaultImgSrc恢复成空（手动删除），可以实现图片的删除。
  **图 7** 添加图片<a name="fig245413171610"></a>
  <img style="display:block;" src="figures/添加图片-12.png" width="700" alt="添加图片-12">
  > ![](public_sys-resources/icon-note.gif) **说明：**
  > DefaultImgSrc属性不支持中文路径。
- 选中画布内的LabelButton组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941198.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  LabelButton组件支持的事件有：OnClick、OnLongPress、OnPress、OnCancel和OnRelease。

  **图 8** 回调事件配置<a name="fig1068120358476"></a>
  <img style="display:block;" src="figures/回调事件配置-13.png" width="700" alt="回调事件配置-13">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的MarginBottom属性和MarginRight属性没有任何的渲染效果。
> - Feature页面下的TriggeredImgSrc属性、TriggeredBackgroundColor属性、TriggeredborderColor属性没有任何界面渲染效果，可在模拟器上查看效果。

#### ScrollView组件<a name="ZH-CN_TOPIC_0000002365940066"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中组件栏中的其他组件，可以将其拖入ScrollView组件中，并且对其他组件进行样式调整。子组件的位置是相对于父容器的左上角，当组件已经存在于界面上时，点击组件中心位置可以将组件拖入容器中。

  **图 1** 将其他组件拖入ScrollView组件中<a name="fig192648563920"></a>
  <img style="display:block;" src="figures/将其他组件拖入ScrollView组件中.png" width="700" alt="将其他组件拖入ScrollView组件中">

- 选中ScrollView组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621001.png" width="36">样式图标（Feature），在展开的Feature栏中修改ScrollView组件的Direction属性可以控制组件哪个方向可以滚动。

  **图 2** 修改组件状态<a name="fig1335145711333"></a>
  <img style="display:block;" src="figures/修改组件状态-14.png" width="700" alt="修改组件状态-14">

- 选中画布内的ScrollView组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399740877.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  ScrollView组件支持的事件有：OnDrag、OnDragStart、OnDragEnd、OnFocus、OnBlur和OnScroll。

  **图 3** 回调事件配置<a name="fig159041157202714"></a>
  <img style="display:block;" src="figures/回调事件配置-15.png" width="700" alt="回调事件配置-15">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - 当其他组件不是直接从左侧UI Control栏拖入时可能会发生其他组件出现在ScrollView组件外面且无法看到的情况，并且当多次从左侧UI Control栏拖入组件时，它们会重复出现在画布(100,100)坐标位置。
> - General页面下的MarginBottom属性和MarginRight属性没有任何的渲染效果。
> - Feature页面下的除Direction属性外其他属性均没有界面渲染效果，可在模拟器上查看效果。
> - ScrollView的滚动条一直处于隐藏状态，但仍保持正常的拖拽方式。

#### CircleProgress组件<a name="ZH-CN_TOPIC_0000002399739749"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中画布内的CircleProgress组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621005.png" width="36">样式图标（Feature），在展开的Feature栏中修改CircleProgress组件的ForegroundStyle和BackgroundStyle窗口中LineWidth属性改变进度条宽度；修改LineColor属性改变进度条颜色。

  **图 1** 修改进度条宽度<a name="fig815243422317"></a>
  <img style="display:block;" src="figures/修改进度条宽度.png" width="700" alt="修改进度条宽度">

  **图 2** 修改进度条颜色<a name="fig969345712413"></a>
  <img style="display:block;" src="figures/修改进度条颜色.png" width="700" alt="修改进度条颜色">

- 选中画布内的CircleProgress组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101078.png" width="36">样式图标（Feature），在展开的Feature栏中修改CircleProgress组件的RangeMax和RangeMin用来限制进度条的value，修改value来改变进度值。

  **图 3** 修改进度值<a name="fig762919369274"></a>
  <img style="display:block;" src="figures/修改进度值.png" width="700" alt="修改进度值">

- 选中画布内的CircleProgress组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941210.png" width="36">样式图标（Feature），在展开的Feature栏中修改CircleProgress组件的Radius和CenterX属性和CenterY用来限定圆环。

  **图 4** 修改圆环大小<a name="fig1581711211515"></a>
  <img style="display:block;" src="figures/修改圆环大小.png" width="700" alt="修改圆环大小">

- 选中画布内的CircleProgress组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101082.png" width="36">样式图标（Feature），在展开的Feature栏中修改CircleProgress组件的StartAngel和EndAngel属性用来限制绘制角度。

  **图 5** 修改角度<a name="fig1267654717373"></a>
  <img style="display:block;" src="figures/修改角度.png" width="700" alt="修改角度">

- 选中画布内的CircleProgress组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941214.png" width="36">样式图标（Feature），在展开的Feature栏中修改CircleProgress组件的ForeImage或者BackImage的子属性来添加前景或者背景图片并且修改图片位置。

  > ![](public_sys-resources/icon-note.gif) **说明：**
  > 图片不支持中文路径，且路径中不能包含空格。

  **图 6** 添加图片<a name="fig836417515157"></a>
  <img style="display:block;" src="figures/添加图片-16.png" width="700" alt="添加图片-16">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的MarginBottom属性、MarginRight属性无渲染效果。
> - Feature页面下的ForegroundStyle和BackgroundStyle的子属性BackgroundColor、BorderWidth、BorderColor、BorderRadius、LineHeight、ImageOpacity无渲染效果。
> - CircleProgress组件不支持回调事件配置。

#### ArcLabel组件<a name="ZH-CN_TOPIC_0000002366099966"></a>

本组件的共有属性不包含Position属性与Size属性，其他共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中画布内的ArcLabel组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101086.png" width="36">样式图标（Feature），在展开的Feature栏中修改ArcLabel组件的LetterSpace属性来修改文本之间的间隔。

  **图 1** 修改文字颜色<a name="fig19959125910167"></a>
  <img style="display:block;" src="figures/修改文字颜色.png" width="700" alt="修改文字颜色">

- 选中画布内的ArcLabel组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941218.png" width="36">样式图标（Feature），在展开的Feature栏中修改ArcLabel组件的TextAlign属性改变文本在圆环上的对齐方式。

  **图 2** 文本对齐方式修改<a name="fig6210165422115"></a>
  <img style="display:block;" src="figures/文本对齐方式修改.png" width="700" alt="文本对齐方式修改">

- 选中画布内的ArcLabel组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101094.png" width="36">样式图标（Feature），在展开的Feature栏中修改ArcLabel组件的Text属性来改变显示的文本。

  **图 3** 显示文本的修改<a name="fig10896149152219"></a>
  <img style="display:block;" src="figures/显示文本的修改.png" width="700" alt="显示文本的修改">

- 选中画布内的ArcLabel组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941222.png" width="36">样式图标（Feature），在展开的Feature栏中修改ArcLabel组件的TextColor属性来修改文字的颜色。

  **图 4** 修改文字颜色<a name="fig181046357190"></a>
  <img style="display:block;" src="figures/修改文字颜色-17.png" width="700" alt="修改文字颜色-17">

- 选中画布内的ArcLabel组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101098.png" width="36">样式图标（Feature），在展开的Feature栏中修改ArcLabel组件的TextSize改变文本中文字的大小。

  **图 5** 文本中文字大小修改<a name="fig13754615153218"></a>
  <img style="display:block;" src="figures/文本中文字大小修改.png" width="700" alt="文本中文字大小修改">

- 选中画布内的ArcLabel组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941230.png" width="36">样式图标（Feature），在展开的Feature栏中修改ArcLabel组件的CenterX、CenterY属性改变文字所在圆的圆心位置。

  **图 6** 文本所在圆圆心修改<a name="fig16333532113418"></a>
  <img style="display:block;" src="figures/文本所在圆圆心修改.png" width="700" alt="文本所在圆圆心修改">

- 选中画布内的ArcLabel组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101102.png" width="36">样式图标（Feature），在展开的Feature栏中修改ArcLabel组件的TextRadius改变文字所在圆的半径。

  **图 7** 文本所在圆半径修改<a name="fig13296111602013"></a>
  <img style="display:block;" src="figures/文本所在圆半径修改.png" width="700" alt="文本所在圆半径修改">

- 选中画布内的ArcLabel组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941234.png" width="36">样式图标（Feature），在展开的Feature栏中修改ArcLabel组件的StartAngle、EndAngle属性改变文本在圆中出现的范围。

  **图 8** 文本出现在圆上的范围修改<a name="fig1867192510273"></a>
  <img style="display:block;" src="figures/文本出现在圆上的范围修改.png" width="700" alt="文本出现在圆上的范围修改">

- 选中画布内的ArcLabel组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101106.png" width="36">样式图标（Feature），在展开的Feature栏中修改ArcLabel组件的TextOrientation改变文本的朝向。

  **图 9** 文本朝向修改<a name="fig035742622712"></a>
  <img style="display:block;" src="figures/文本朝向修改.png" width="700" alt="文本朝向修改">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的MarginBottom属性和MarginRight属性无任何渲染效果。
> - ArcLabel组件不支持回调事件配置。

#### SwipeView组件<a name="ZH-CN_TOPIC_0000002399619881"></a>

本组件的共有属性不包含Border属性、Margin属性与Padding属性，其他共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中SwipeView组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941238.png" width="36">样式图标（Feature），在展开的Feature栏中修改SwipeView组件的Direction属性改变组件的滚动方向。子组件的位置是相对于父容器的左上角，当组件已经存在于界面上时，点击组件中心位置可以将组件拖入容器中。

  **图 1** 修改滚动条位置<a name="fig85221029131212"></a>
  <img style="display:block;" src="figures/修改滚动条位置.png" width="700" alt="修改滚动条位置">

  <img style="display:block;" src="figures/1.png" width="700">

  > ![](public_sys-resources/icon-note.gif) **说明：**
  > 滚动条已被隐藏，当容器内的子组件超出范围时可拖动，HORIZONTAL是水平滚动，VERTICAL是垂直滚动。

- 选中画布内的SwipeView组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621041.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  SwipeView组件支持的事件有：OnDrag、OnDragStart、OnDragEnd、OnSwipe。

  **图 2** 回调事件配置<a name="fig968711173355"></a>
  <img style="display:block;" src="figures/回调事件配置-18.png" width="700" alt="回调事件配置-18">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - Feature页面下的Isloop属性、AlignMode属性、TickTime属性暂无渲染效果。
> - 在水平模式下上方工具栏的顶部对齐<img src="figures/zh-cn_image_0000002399740917.png" width="28">、底部对齐<img src="figures/zh-cn_image_0000002366101114.png" width="33">、上下居中对齐<img src="figures/zh-cn_image_0000002399621045.png" width="29">不可用。
> - 在垂直模式下上方工具栏的左对齐<img src="figures/zh-cn_image_0000002365941246.png" width="35">、右对齐<img src="figures/zh-cn_image_0000002399740925.png" width="24">、左右居中对齐<img src="figures/zh-cn_image_0000002366101122.png" width="27">不可用。
> - SwipeView的滚动条一直处于隐藏状态，但仍保持正常的拖拽方式。

#### TextureMapper组件<a name="ZH-CN_TOPIC_0000002365940070"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中TextureMapper组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621069.png" width="36">样式图标（Feature），在展开的Feature栏通过修改TextureMapper组件的ImagePath属性添加图片，通过将ImagePath属性恢复成空（手动删除），可以实现图片的删除。
  **图 1** 添加图片<a name="fig15600147102714"></a>
  <img style="display:block;" src="figures/添加图片-19.png" width="700" alt="添加图片-19">
  > ![](public_sys-resources/icon-note.gif) **说明：**
  > ImagePath属性不支持中文路径。
- 选中TextureMapper组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101150.png" width="36">样式图标（Feature），在展开的Feature栏通过修改TextureMapper组件的ImageOpacity属性修改图片的透明度。

  **图 2** 修改图片透明度<a name="fig1859224515129"></a>
  <img style="display:block;" src="figures/修改图片透明度-20.png" width="700" alt="修改图片透明度-20">

- 选中画布内的TextureMapper组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399740985.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  TextureMapper组件支持的事件有：OnMapper。

  **图 3** 回调事件配置<a name="fig833815411471"></a>
  <img style="display:block;" src="figures/回调事件配置-21.png" width="700" alt="回调事件配置-21">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的MarginBottom属性和MarginRight属性均无渲染效果。
> - Feature页面下除ImagePath属性外其他属性均没有界面渲染效果，可在模拟器上查看效果。请在展示动画效果前先添加图片并且Feature页面的IsStart属性为true。
> - 组件的大小在添加图片后固定为图片的大小，且修改组件宽高不生效。

#### Slider组件<a name="ZH-CN_TOPIC_0000002399739753"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中Slider组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621121.png" width="36">样式图标（Feature），在展开的Feature栏中修改Slider组件的SliderValue属性改变滑块的位置。

  **图 1** 修改滑块位置<a name="fig520210134916"></a>
  <img style="display:block;" src="figures/修改滑块位置.png" width="700" alt="修改滑块位置">

- 选中Slider组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741001.png" width="36">样式图标（Feature），在展开的Feature栏中修改Slider组件的SliderWidth属性改变滑槽的宽度。

  **图 2** 修改滑槽宽度<a name="fig19400118164911"></a>
  <img style="display:block;" src="figures/修改滑槽宽度.png" width="700" alt="修改滑槽宽度">

- 选中Slider组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621137.png" width="36">样式图标（Feature），在展开的Feature栏中修改Slider组件的SliderHeight属性改变滑槽的高度。SliderHeight不能超出边框的高度。

  **图 3** 修改滑槽高度<a name="fig54931822183517"></a>
  <img style="display:block;" src="figures/修改滑槽高度.png" width="700" alt="修改滑槽高度">

- 选中Slider组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741017.png" width="36">样式图标（Feature），在展开的Feature栏中修改Slider组件的Direction属性改变滑槽的方向。

  **图 4** 修改滑动方向<a name="fig1164616545365"></a>
  <img style="display:block;" src="figures/修改滑方向.png" width="700" alt="修改滑方向">

- 选中Slider组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621145.png" width="36">样式图标（Feature），在展开的Feature栏中修改Slider组件的KnobWidth属性改变滑块的宽度。

  **图 5** 修改滑块大小<a name="fig2041221915013"></a>
  <img style="display:block;" src="figures/修改滑块大小.png" width="700" alt="修改滑块大小">

- 选中Slider组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741033.png" width="36">样式图标（Feature），在展开的Feature栏中修改Slider组件的BackGroundImage属性改变滑槽的背景图片；修改Slider组件的BackGroundColor属性改变滑槽的背景色。

  > ![](public_sys-resources/icon-note.gif) **说明：**
  > 图片不支持中文路径，且路径中不能包含空格。

  **图 6** 添加图片<a name="fig20840845145018"></a>
  <img style="display:block;" src="figures/添加图片-22.png" width="700" alt="添加图片-22">

  **图 7** 设置颜色<a name="fig1623652355120"></a>
  <img style="display:block;" src="figures/设置颜色.png" width="700" alt="设置颜色">

- 选中Slider组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941362.png" width="36">样式图标（Feature），在展开的Feature栏的ForeStyle窗口中修改Slider组件的ForeImg属性改变滑槽的前景图片；修改ForeGroundColor改变滑槽的前景颜色。

  > ![](public_sys-resources/icon-note.gif) **说明：**
  > 图片不支持中文路径，且路径中不能包含空格。

  **图 8** 添加图片<a name="fig71361938195220"></a>
  <img style="display:block;" src="figures/添加图片-23.png" width="700" alt="添加图片-23">

  **图 9** 修改背景颜色<a name="fig53181218398"></a>
  <img style="display:block;" src="figures/修改背景颜色-24.png" width="700" alt="修改背景颜色-24">

- 选中Slider组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621173.png" width="36">样式图标（Feature），在展开的Feature栏KnobStyle窗口中修改Slider组件的KnobImage属性添加图片；修改KnobBackGroundColor属性改变滑块的颜色；修改KnobRadius属性改变滑块的边框弧度。
  **图 10** 添加图片<a name="fig4198162695412"></a>
  <img style="display:block;" src="figures/添加图片-25.png" width="700" alt="添加图片-25">
  > ![](public_sys-resources/icon-note.gif) **说明：**
  > 图片不支持中文路径，且路径中不能包含空格。
  **图 11** 修改背景颜色<a name="fig561313503547"></a>
  <img style="display:block;" src="figures/修改背景颜色-26.png" width="700" alt="修改背景颜色-26">
  **图 12** 修改弧度<a name="fig620717512485"></a>
  <img style="display:block;" src="figures/修改弧度.png" width="700" alt="修改弧度">
- 选中画布内的Slider组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941390.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  Slider组件支持的事件有：OnClick、OnLongPress、OnDrag、OnDragStart、OnDragEnd、OnPress、OnCancel、OnRelease、OnFocus、OnBlur。

  **图 13** 回调事件配置<a name="fig325561020"></a>
  <img style="display:block;" src="figures/回调事件配置-27.png" width="700" alt="回调事件配置-27">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的GaussianBlur属性、MarginBottom属性和MarginRight属性均无渲染效果。
> - 组件的大小在添加图片后固定为图片的大小，且修改组件宽高不生效。

#### Picker组件<a name="ZH-CN_TOPIC_0000002366099970"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中Picker组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101302.png" width="36">样式图标（Feature），在展开的Feature栏中修改Picker组件的Normal属性改变组件未选中字体颜色。

  **图 1** 修改未选中字体颜色<a name="fig19778846182613"></a>
  <img style="display:block;" src="figures/修改未选中字体颜色.png" width="700" alt="修改未选中字体颜色">

- 选中Picker组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941414.png" width="36">样式图标（Feature），在展开的Feature栏中修改Picker组件的HighLight属性改变组件选中字体颜色。

  **图 2** 修改选中字体颜色<a name="fig13923214192715"></a>
  <img style="display:block;" src="figures/修改选中字体颜色.png" width="700" alt="修改选中字体颜色">

- 选中Picker组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101314.png" width="36">样式图标（Feature），在展开的Feature栏中修改Picker组件的ItemHeight属性改变组件条目高度。

  **图 3** 修改条目高度<a name="fig1048834002714"></a>
  <img style="display:block;" src="figures/修改条目高度.png" width="700" alt="修改条目高度">

- 选中Picker组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941430.png" width="36">样式图标（Feature），在展开的Feature栏中修改Picker组件的LoopState属性使组件内容循环。

  **图 4** 设置循环<a name="fig5493192817"></a>
  <img style="display:block;" src="figures/设置循环.png" width="700" alt="设置循环">

- 选中Picker组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101326.png" width="36">样式图标（Feature），在展开的Feature栏中修改Picker组件的Values属性改变组件显示文本，数据格式为："x1", "x2", "x3"...（必须带""）

  **图 5** 修改文本<a name="fig1959462262820"></a>
  <img style="display:block;" src="figures/修改文本.png" width="700" alt="修改文本">

- 选中Picker组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941446.png" width="36">样式图标（Feature），在展开的Feature栏中同步Count属性值（必须与输入数组子元素个数相等）。

  **图 6** 添加元素个数值<a name="fig9995037194619"></a>
  <img style="display:block;" src="figures/添加元素个数值.png" width="700" alt="添加元素个数值">

- 选中Picker组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101334.png" width="36">样式图标（Feature），在展开的Feature栏中修改Picker组件的TextDirection属性值改变文本的书写方向。LTR表示文字方向为从左至右，RTL为从右至左。如图7所示，第一个值为“12345”，通过设置TextDirection属性值为RTL后，画布中显示的文字为“54321”。

  **图 7** 修改文本方向<a name="fig0726183665610"></a>
  <img style="display:block;" src="figures/修改文本方向.png" width="700" alt="修改文本方向">

- 选中画布内的Picker组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941450.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  Picker组件支持的事件有：OnFocus和OnBlur。

  **图 8** 回调事件配置<a name="fig325561020"></a>
  <img style="display:block;" src="figures/回调事件配置-28.png" width="700" alt="回调事件配置-28">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的MarginBottom属性和MarginRight属性均无渲染效果。
> - Count属性值与数组元素个数保持一致。

#### TimePicker组件<a name="ZH-CN_TOPIC_0000002399619885"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中TimePicker组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101338.png" width="36">样式图标（Feature），在展开的Feature栏中修改TimePicker组件的ItemHeight属性改变组件条目高度。

  **图 1** 修改条目高度<a name="fig13492156123017"></a>
  <img style="display:block;" src="figures/修改条目高度-29.png" width="700" alt="修改条目高度-29">

- 选中TimePicker组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941454.png" width="36">样式图标（Feature），在展开的Feature栏中修改TimePicker组件的Values属性改变组件显示文本。

  **图 2** 修改文本<a name="fig1536141613118"></a>
  <img style="display:block;" src="figures/修改文本-30.png" width="700" alt="修改文本-30">

- 选中TimePicker组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101342.png" width="36">样式图标（Feature），在展开的Feature栏中修改TimePicker组件的HourLoop属性改变组件小时窗口是否循环。

  **图 3** 设置循环<a name="fig172573812312"></a>
  <img style="display:block;" src="figures/设置循环-31.png" width="700" alt="设置循环-31">

- 选中TimePicker组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941458.png" width="36">样式图标（Feature），在展开的Feature栏中修改TimePicker组件的MinLoop属性改变组件分钟窗口是否循环。

  **图 4** 设置循环<a name="fig1741193616326"></a>
  <img style="display:block;" src="figures/设置循环-32.png" width="700" alt="设置循环-32">

- 选中TimePicker组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101350.png" width="36">样式图标（Feature），在展开的Feature栏中修改TimePicker组件的SecLoop属性改变组件秒窗口是否循环。（在SecShows属性为true情况下）

  **图 5** 设置循环<a name="fig1031192215331"></a>
  <img style="display:block;" src="figures/设置循环-33.png" width="700" alt="设置循环-33">

- 选中TimePicker组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941462.png" width="36">样式图标（Feature），在展开的Feature栏中修改TimePicker组件的NormalColor属性改变组件未选中字体颜色。

  **图 6** 修改字体颜色<a name="fig689444916334"></a>
  <img style="display:block;" src="figures/修改字体颜色.png" width="700" alt="修改字体颜色">

- 选中TimePicker组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101354.png" width="36">样式图标（Feature），在展开的Feature栏中修改TimePicker组件的HighLightColor属性改变组件选中字体颜色。

  **图 7** 修改字体颜色<a name="fig1820476173413"></a>
  <img style="display:block;" src="figures/修改字体颜色-34.png" width="700" alt="修改字体颜色-34">

- 选中TimePicker组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941466.png" width="36">样式图标（Feature），在展开的Feature栏中修改TimePicker组件的SecShow属性设置秒窗口是否显示。

  **图 8** 设置秒窗口显示<a name="fig732614223349"></a>
  <img style="display:block;" src="figures/设置秒窗口显示.png" width="700" alt="设置秒窗口显示">

- 选中TimePicker组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101358.png" width="36">样式图标（Feature），在展开的Feature栏中修改TimePicker组件的BackgroundFontsize属性改变组件未选中字体大小。

  **图 9** 设置字体大小<a name="fig7257450143415"></a>
  <img style="display:block;" src="figures/设置字体大小.png" width="700" alt="设置字体大小">

- 选中TimePicker组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941470.png" width="36">样式图标（Feature），在展开的Feature栏中修改TimePicker组件的HighlightFontsize属性改变组件选中字体大小。

  **图 10** 设置字体大小<a name="fig1568281294514"></a>
  <img style="display:block;" src="figures/设置字体大小-35.png" width="700" alt="设置字体大小-35">

- 选中画布内的TimePicker组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101362.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  TimePicker组件支持的事件有：OnFocus和OnBlur。

  **图 11** 回调事件配置<a name="fig325561020"></a>
  <img style="display:block;" src="figures/回调事件配置-36.png" width="700" alt="回调事件配置-36">

> ![](public_sys-resources/icon-note.gif) **说明：**
> General页面下的MarginBottom属性和MarginRight属性均无渲染效果。

#### Chart组件<a name="ZH-CN_TOPIC_0000002365940078"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中Chart组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941478.png" width="36">样式图标（Feature），在展开的Feature栏中修改XAxis栏中的属性改变横坐标的样式。
  - MarkNum属性：改变坐标轴上点的数量
  - RangMin和RangMax：改变坐标轴的取值范围
  - Color：改变坐标轴的颜色
  - Visible：控制坐标轴的可见与否

  **图 1** 修改横坐标属性<a name="fig8661439164210"></a>
  <img style="display:block;" src="figures/修改横坐标属性.png" width="700" alt="修改横坐标属性">

- 选中Chart组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621289.png" width="36">样式图标（Feature），在展开的Feature栏中修改YAxis栏中的属性改变纵坐标样式，具体修改与横坐标相同，请参考图2。

  **图 2** 修改纵坐标样式<a name="fig16661839194210"></a>
  <img style="display:block;" src="figures/修改纵坐标样式.png" width="700" alt="修改纵坐标样式">

- 选中Chart组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741189.png" width="36">样式图标（Feature），在展开的Feature栏中点击DataSerial属性右侧的加号添加数据，可以添加多组数据。

  **图 3** 添加数据<a name="fig10661113994214"></a>
  <img style="display:block;" src="figures/添加数据.png" width="700" alt="添加数据">

- 选中Chart组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621297.png" width="36">样式图标（Feature），在展开的Feature栏中添加数据然后改变数据的样式，其中Data属性是要填入的数据，DataCount属性是数据的个数，FillColor是填充渐变色的颜色，LineColor是线的颜色，EnableGradient属性控制是否填充渐变色。

  **图 4** 添加数据效果展示<a name="fig96611939204217"></a>
  <img style="display:block;" src="figures/添加数据效果展示.png" width="700" alt="添加数据效果展示">

- 选中Chart组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741197.png" width="36">样式图标（Feature），在展开的Feature栏中ColorGradient窗口中MinOpa和MaxOpa属性改变渐变色的范围，MaxOpa控制上面的渐变色透明度，MinOpa控制下面的渐变色透明度。

  **图 5** 修改透明度渐变色<a name="fig46611739184215"></a>
  <img style="display:block;" src="figures/修改透明度渐变色.png" width="700" alt="修改透明度渐变色">

- 选中Chart组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621305.png" width="36">样式图标（Feature），在展开的Feature栏中修改Chart组件的Type属性改变图的类型。

  **图 6** 修改图的类型<a name="fig19661139164218"></a>
  <img style="display:block;" src="figures/修改图的类型.png" width="700" alt="修改图的类型">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的MarginBottom属性和MarginRight属性均无渲染效果。
> - 添加数据时的格式为： \{x1,y1\},\{x2,y2\};
>   数据中不能有空格，横坐标应从0开始依次递增，DataCount属性中的数字不能比数据个数小。当DataCount属性中的数字比数据个数大时，会自动补连\{0,0\}，柱状图时横坐标的MarkNum也不能比数据个数小。
> - ColorGradient属性只有在折线图时有用。
> - 目前Chart首次修改DataSerial属性时，属性界面可能无法发生变化，通过再次修改DataSerial属性中的其他属性可使界面发生变化。
> - Chart组件不支持回调事件的配置。

#### EditText组件<a name="ZH-CN_TOPIC_0000002399739757"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中EditText组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741209.png" width="36">样式图标（Feature），在展开的Feature栏中修改EditText组件的Placeholder属性以修改背景提示文字。

  **图 1** 修改背景提示文字<a name="fig688611508216"></a>
  <img style="display:block;" src="figures/修改背景提示文字.png" width="700" alt="修改背景提示文字">

- 选中EditText组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621313.png" width="36">样式图标（Feature），在展开的Feature栏中修改EditText组件的Text属性以修改前景文字的内容，并且当前景文字存在时无法显示背景文字。

  **图 2** 修改前景文字<a name="fig18400183213561"></a>
  <img style="display:block;" src="figures/修改前景文字.png" width="700" alt="修改前景文字">

- 选中EditText组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741217.png" width="36">样式图标（Feature），在展开的Feature栏中修改EditText组件的EditTextColor属性以修改前景文字的颜色。

  **图 3** 修改前景文字颜色<a name="fig581421214573"></a>
  <img style="display:block;" src="figures/修改前景文字颜色.png" width="700" alt="修改前景文字颜色">

- 选中EditText组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621333.png" width="36">样式图标（Feature），在展开的Feature栏中修改EditText组件的MaxLength属性来限制前景文字输入长度。

  **图 4** 限制前景文字长度<a name="fig8651102555710"></a>
  <img style="display:block;" src="figures/限制前景文字长度.png" width="700" alt="限制前景文字长度">

- 选中EditText组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741233.png" width="36">样式图标（Feature），在展开的Feature栏中修改EditText组件的InputType属性来改变输入模式。
  - text模式：输入的文本正常显示
  - password模式：输入的文本以密码模式显示（被“·”代替）

  **图 5** 改变输入模式<a name="fig13869958175715"></a>
  <img style="display:block;" src="figures/改变输入模式.png" width="700" alt="改变输入模式">

- 选中EditText组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621357.png" width="36">样式图标（Feature），在展开的Feature栏中修改EditText组件的PlaceholderColor属性以修改背景提示文字的颜色。

  **图 6** 修改背景提示文字颜色<a name="fig1530813191564"></a>
  <img style="display:block;" src="figures/修改背景提示文字颜色.png" width="700" alt="修改背景提示文字颜色">

- 选中EditText组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741261.png" width="36">样式图标（Feature），在展开的Feature栏中修改EditText组件的CursorColor属性来修改光标的颜色。

  **图 7** 光标颜色<a name="fig14857161318582"></a>
  <img style="display:block;" src="figures/光标颜色.png" width="700" alt="光标颜色">

- 选中画布内的EditText组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621385.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  EditText组件支持的事件有：OnClick、OnLongPress、OnPress、OnCancel、OnRelease。

  **图 8** 回调事件配置<a name="fig325561020"></a>
  <img style="display:block;" src="figures/回调事件配置-37.png" width="700" alt="回调事件配置-37">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的MarginBottom属性和MarginRight属性均无渲染效果。
> - 文字修改只能通过右侧的特有属性进行，在界面上通过键盘删除文字时会出现将组件删除的问题，修改前景文本请通过右侧的Text文本进行。

#### DigitalClock组件<a name="ZH-CN_TOPIC_0000002366099978"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中DigitalClock组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741285.png" width="36">样式图标（Feature），在展开的Feature栏中修改DigitalClock组件的Color属性改变字体颜色。

  **图 1** 修改字体颜色<a name="fig28061923305"></a>
  <img style="display:block;" src="figures/修改字体颜色-38.png" width="700" alt="修改字体颜色-38">

- 选中DigitalClock组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621393.png" width="36">样式图标（Feature），在展开的Feature栏中修改DigitalClock组件的DisplayMode属性改变组件显示状态。

  **图 2** 组件显示状态<a name="fig13710344441"></a>
  <img style="display:block;" src="figures/组件显示状态.png" width="700" alt="组件显示状态">

- 选中DigitalClock组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741297.png" width="36">样式图标（Feature），在展开的Feature栏中修改DigitalClock组件的DisplayLeadigZero属性设置是否在小时前面加0。

  **图 3** 是否添加0<a name="fig9371123494418"></a>
  <img style="display:block;" src="figures/是否添加0.png" width="700" alt="是否添加0">

- 选中DigitalClock组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621397.png" width="36">样式图标（Feature），在展开的Feature栏中修改DigitalClock组件的Hour属性设置小时。

  **图 4** 设置小时<a name="fig67661353475"></a>
  <img style="display:block;" src="figures/设置小时.png" width="700" alt="设置小时">

- 选中DigitalClock组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741301.png" width="36">样式图标（Feature），在展开的Feature栏中修改DigitalClock组件的Minute属性设置分钟。

  **图 5** 设置分钟<a name="fig711219924715"></a>
  <img style="display:block;" src="figures/设置分钟.png" width="700" alt="设置分钟">

- 选中DigitalClock组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621401.png" width="36">样式图标（Feature），在展开的Feature栏中修改DigitalClock组件的Second属性设置秒。

  **图 6** 设置秒<a name="fig177318106475"></a>
  <img style="display:block;" src="figures/设置秒.png" width="700" alt="设置秒">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的MarginBottom属性和MarginRight属性均无渲染效果。
> - DigitalClock不支持回调事件的配置。

#### ImageAnimator组件<a name="ZH-CN_TOPIC_0000002399619889"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中ImageAnimator组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741305.png" width="36">样式图标（Feature），在展开的Feature栏中添加图片路径。

  **图 1** 图片路径<a name="fig28061923305"></a>
  <img style="display:block;" src="figures/图片路径.png" width="700" alt="图片路径">

- 选中ImageAnimator组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621409.png" width="36">样式图标（Feature），在展开的Feature栏中修改ImageAnimator组件的ImageNum属性保证显示图片的个数与输入图片路径的个数相等。

  **图 2** 图片的个数<a name="fig13710344441"></a>
  <img style="display:block;" src="figures/图片的个数.png" width="700" alt="图片的个数">

- 选中ImageAnimator组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741313.png" width="36">样式图标（Feature），在展开的Feature栏中修改ImageAnimator组件的Times属性控制循环次数。该属性只有在Repeat为false情况下生效。

  **图 3** 循环次数<a name="fig9371123494418"></a>
  <img style="display:block;" src="figures/循环次数.png" width="700" alt="循环次数">

- 选中ImageAnimator组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621413.png" width="36">样式图标（Feature），在展开的Feature栏中修改ImageAnimator组件的Fixed属性用来适应图片大小。

  **图 4** 是否适应图片大小<a name="fig67661353475"></a>
  <img style="display:block;" src="figures/是否适应图片大小.png" width="700" alt="是否适应图片大小">

- 选中ImageAnimator组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741317.png" width="36">样式图标（Feature），在展开的Feature栏中修改ImageAnimator组件的Repeat属性控制图片是否循环。

  **图 5** 设置图片是否循环<a name="fig711219924715"></a>
  <img style="display:block;" src="figures/设置图片是否循环.png" width="700" alt="设置图片是否循环">

- 选中ImageAnimator组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621417.png" width="36">样式图标（Feature），在展开的Feature栏中修改ImageAnimator组件的Reverse属性设置图片循环方向。

  **图 6** 设置图片循环方向<a name="fig137012812132"></a>
  <img style="display:block;" src="figures/设置图片循环方向.png" width="700" alt="设置图片循环方向">

- 选中ImageAnimator组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741321.png" width="36">样式图标（Feature），在展开的Feature栏中修改ImageAnimator组件的FillMode属性设置动画最后一帧显示的图片，true为当前循环模式下动画的第一张图片，false为最后一张。其中，Reverse属性值影响循环动画的图片先后顺序。

  **图 7** 设置最后一帧<a name="fig142541859122517"></a>
  <img style="display:block;" src="figures/设置最后一帧.png" width="700" alt="设置最后一帧">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的MarginBottom属性和MarginRight属性均无渲染效果。
> - Feature页面下的TimeOfUpdate属性和TimeOfPause属性无渲染效果。
> - ImageAnimator组件不支持回调事件的配置。

#### Qrcode组件<a name="ZH-CN_TOPIC_0000002365940082"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中画布内的Qrcode组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621421.png" width="36">样式图标（Feature），在展开的Feature栏中修改Qrcode组件的ImageOpacity属性来修改二维码的透明度。

  **图 1** 修改二维码透明度<a name="fig19959125910167"></a>
  <img style="display:block;" src="figures/修改二维码透明度.png" width="700" alt="修改二维码透明度">

- 选中画布内的Qrcode组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741325.png" width="36">样式图标（Feature），在展开的Feature栏中修改Qrcode组件的BackColor属性修改二维码的背景颜色。

  **图 2** 修改背景色<a name="fig6210165422115"></a>
  <img style="display:block;" src="figures/修改背景色-39.png" width="700" alt="修改背景色-39">

- 选中画布内的Qrcode组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621425.png" width="36">样式图标（Feature），在展开的Feature栏中修改Qrcode组件的QrcodeColor属性修改二维码的颜色。

  **图 3** 修改二维码颜色<a name="fig10896149152219"></a>
  <img style="display:block;" src="figures/修改二维码颜色.png" width="700" alt="修改二维码颜色">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的BackgroungColor属性、MarginBottom属性和MarginRight属性均无渲染效果。
> - Feature页面下的Text属性无界面渲染效果，具体效果可在模拟器查看。
> - Qrcode组件不支持回调事件的配置。

#### AnalogClock组件<a name="ZH-CN_TOPIC_0000002399739761"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中AnalogClock组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741329.png" width="36">样式图标（Feature），在展开的Feature栏中修改Hour窗口中的PositionX属性和PositionY属性来修改时针的位置，同时，Minute窗口和Second窗口中的PositionX属性和PositionY属性可以分别修改分针和秒针的位置。

  **图 1** 修改指针的位置<a name="fig678011363619"></a>
  <img style="display:block;" src="figures/修改指针的位置.png" width="700" alt="修改指针的位置">

- 选中AnalogClock组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621429.png" width="36">样式图标（Feature），在展开的Feature栏中修改Hour窗口中的CenterX属性和CenterY属性来修改时针的旋转中心（该坐标以PositionX和PositionY所在点为原点，相对于表针位置而非组件左上角）同时，Minute窗口和Second窗口中的CenterX属性和CenterY属性可以分别修改分针和秒针的旋转中心。

  **图 2** 修改指针的旋转中心<a name="fig821320214408"></a>
  <img style="display:block;" src="figures/修改指针的旋转中心.png" width="700" alt="修改指针的旋转中心">

- 选中AnalogClock组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741333.png" width="36">样式图标（Feature），在展开的Feature栏中修改Hour窗口中的Color属性来修改时针的颜色，同时，Minute窗口和Second窗口中的Color属性可以分别修改分针和秒针的颜色。

  **图 3** 修改指针的颜色<a name="fig16383193311422"></a>
  <img style="display:block;" src="figures/修改指针的颜色.png" width="700" alt="修改指针的颜色">

- 选中AnalogClock组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621433.png" width="36">样式图标（Feature），在展开的Feature栏中修改Hour窗口中的Width属性来修改时针的宽度，同时，Minute窗口和Second窗口中的Width属性可以分别修改分针和秒针的宽度。

  **图 4** 修改指针的宽度<a name="fig133511819144416"></a>
  <img style="display:block;" src="figures/修改指针的宽度.png" width="700" alt="修改指针的宽度">

- 选中AnalogClock组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741337.png" width="36">样式图标（Feature），在展开的Feature栏中修改Hour窗口中的Length属性来修改时针的长度，同时，Minute窗口和Second窗口中的Length属性可以分别修改分针和秒针的长度。

  **图 5** 修改指针的长度<a name="fig189181575451"></a>
  <img style="display:block;" src="figures/修改指针的长度.png" width="700" alt="修改指针的长度">

- 选中AnalogClock组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621437.png" width="36">样式图标（Feature），在展开的Feature栏中修改Hour窗口中的Opacity属性来修改时针的颜色透明度，同时，Minute窗口和Second窗口中的Opacity属性可以分别修改分针和秒针的颜色透明度。

  **图 6** 修改指针的颜色透明度<a name="fig1717814924613"></a>
  <img style="display:block;" src="figures/修改指针的颜色透明度.png" width="700" alt="修改指针的颜色透明度">

- 选中AnalogClock组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741341.png" width="36">样式图标（Feature），在展开的Feature栏中修改Hour窗口中的LineImage属性来为时针添加图片，同时，Minute窗口和Second窗口中的LineImage属性可以分别为分针和秒针添加图片。
  **图 7** 为指针添加图片<a name="fig194842357484"></a>
  <img style="display:block;" src="figures/为指针添加图片.png" width="700" alt="为指针添加图片">
  > ![](public_sys-resources/icon-note.gif) **说明：**
  > LineImage属性不支持中文路径。
- 选中AnalogClock组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621445.png" width="36">样式图标（Feature），在展开的Feature栏中修改AnalogClock组件的NewMode属性来控制秒针的显示。

  **图 8** 控制秒针的显示<a name="fig7341154611512"></a>
  <img style="display:block;" src="figures/控制秒针的显示.png" width="700" alt="控制秒针的显示">

- 选中画布内的AnalogClock组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741345.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  AnalogClock组件支持的事件有：OnClick、OnLongPress、OnPress、OnCancel和OnRelease。

  **图 9** 回调事件配置<a name="fig052871717486"></a>
  <img style="display:block;" src="figures/回调事件配置-40.png" width="700" alt="回调事件配置-40">

- 选中组件栏中的其他组件，可以将其拖入AnalogClock组件中，并且对其他组件进行样式调整。子组件的位置是相对于父容器的左上角，当组件已经存在于界面上时，单击组件中心位置可以将组件拖入容器中。

  **图 10** 将其他组件拖入AnalogClock组件中<a name="fig192648563920"></a>
  <img style="display:block;" src="figures/将其他组件拖入AnalogClock组件中.png" width="700" alt="将其他组件拖入AnalogClock组件中">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的MarginBottom属性和MarginRight属性均无渲染效果。
> - Feature页面下的Am属性无界面渲染效果。

#### SweepClock组件<a name="ZH-CN_TOPIC_0000002366099982"></a>

本组件包含AnalogClock组件的所有属性，与其类似，因此相同属性不再赘述，请参见“AnalogClock组件”描述。

- 选中SweepClock组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941658.png" width="36">样式图标（Feature），在展开的Feature栏中修改Hour窗口中的CenterImage属性，为时针中心点添加图片，同时，Minute窗口和Second窗口中的CenterImage属性可以分别修改分针和秒针的中心点添加图片。
  **图 1** 为中心圆圈添加图片<a name="fig194842357484"></a>
  <img style="display:block;" src="figures/为中心圆圈添加图片.png" width="700" alt="为中心圆圈添加图片">
  > ![](public_sys-resources/icon-note.gif) **说明：**
  > CenterImage属性不支持中文路径。
- 选中SweepClock组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101542.png" width="36">样式图标（Feature），在展开的Feature栏中修改Hour窗口中的CenterImageX属性和CenterImageY属性，修改时针中心图片的位置。同时，Minute窗口和Second窗口中的CenterImage属性可以分别修改分针和秒针的中心图片的位置。

  **图 2** 控制秒针的显示<a name="fig7341154611512"></a>
  <img style="display:block;" src="figures/控制秒针的显示-41.png" width="700" alt="控制秒针的显示-41">

- 选中组件栏中的其他组件，可以将其拖入SweepClock组件中，并且对其他组件进行样式调整。子组件的位置是相对于父容器的左上角，当组件已经存在于界面上时，单击组件中心位置可以将组件拖入容器中。

  **图 3** 将其他组件拖入SweepClock组件中<a name="fig192648563920"></a>
  <img style="display:block;" src="figures/将其他组件拖入SweepClock组件中.png" width="700" alt="将其他组件拖入SweepClock组件中">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的MarginBottom属性和MarginRight属性均无渲染效果。
> - Feature页面下的Am属性无界面渲染效果。
> - SweepClock不支持回调事件的配置。

#### Coverflow组件<a name="ZH-CN_TOPIC_0000002399619893"></a>

本组件的共有属性不包含Border属性、Margin属性与Padding属性，其他共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中Coverflow组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741357.png" width="36">样式图标（Feature），在展开的Feature栏导入一张或者多张图片（可以调整画布大小，使图片显示效果更好），第一张图片默认位于画布正中间。
  **图 1** 特有属性配置：ImagePath<a name="fig144651235202314"></a>
  <img style="display:block;" src="figures/特有属性配置-ImagePath-42.png" width="700" alt="特有属性配置-ImagePath-42">
  > ![](public_sys-resources/icon-note.gif) **说明：**
  > ImagePath不支持中文路径。
  > 导入的Bin文件必须是图片转的Bin，否则模拟器会异常。
- 选中画布内的Coverflow组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399621461.png" width="36">样式图标（Feature），在展开的Feature栏中修改Coverflow组件中的ImgWidth和ImgHeight可以调整图片宽高。

  更改图片宽高后，所有导入Coverflow组件的图片宽高随之改变，且第一张图片始终位于组件的正中间。

  **图 2** 特有属性配置：ImgWidth和ImgHeight<a name="fig1549113615248"></a>
  <img style="display:block;" src="figures/特有属性配置-ImgWidth和ImgHeight.png" width="700" alt="特有属性配置-ImgWidth和ImgHeight">

- 选中画布内的Coverflow组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399741361.png" width="36">样式图标（Feature），在展开的Feature栏中修改Coverflow组件中的RotateAngle调整旋转角度。

  **图 3** 特有属性配置：RotateAngle<a name="fig1917017159243"></a>
  <img style="display:block;" src="figures/特有属性配置-RotateAngle.png" width="700" alt="特有属性配置-RotateAngle">

- 选中画布内的Coverflow组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399621465.png" width="36">样式图标（Feature），在展开的Feature栏中修改Coverflow组件中的Padding调整图片之间的间距。

  **图 4** 特有属性配置：Padding<a name="fig2142192232415"></a>
  <img style="display:block;" src="figures/特有属性配置-Padding.png" width="700" alt="特有属性配置-Padding">

- 选中画布内的Coverflow组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399741365.png" width="36">样式图标（Feature），在展开的Feature栏中修改Coverflow组件中的IsShowMirrorImg设置是否显示图片镜像。

  **图 5** 特有属性配置：IsShowMirrorImg<a name="fig25262913248"></a>
  <img style="display:block;" src="figures/特有属性配置-IsShowMirrorImg.png" width="700" alt="特有属性配置-IsShowMirrorImg">

- 选中画布内的Coverflow组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399621473.png" width="36">样式图标（Feature），在展开的Feature栏中修改Coverflow组件中的MirrorOpa设置图片镜像的透明度。

  **图 6** 特有属性配置：MirrorOpa<a name="fig96581036102413"></a>
  <img style="display:block;" src="figures/特有属性配置-MirrorOpa.png" width="700" alt="特有属性配置-MirrorOpa">

- 选中画布内的Coverflow组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741373.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  Coverflow组件支持的事件有：OnDrag、OnDragStart、OnDragEnd和OnCoverflow。

  **图 7** 回调事件配置<a name="fig4163730162310"></a>
  <img style="display:block;" src="figures/回调事件配置-43.png" width="700" alt="回调事件配置-43">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - Feature页面下的RotateAngle、IsShowMirrorImg和MirrorOpa暂无渲染效果，具体效果可以在模拟器查看。
> - Coverflow的回调事件在生成的XXXPresenter.cpp文件中的回调函数名称为“OnScroll（）”。

#### Barcode组件<a name="ZH-CN_TOPIC_0000002365940086"></a>

共有属性使用方法请参见“11.1.2.2 组件的共有属性”章节内容。

选中画布内的Barcode组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941686.png" width="36">样式图标（Feature），在展开的Feature栏中有一个BarcodeInfo属性，提供Barcode的信息，且不能设置为空，如果设置为空，生成代码后，在模拟器中会显示条形码失败。

**图 1** 特有属性配置：BarcodeInfo<a name="fig191081212257"></a>
<img style="display:block;" src="figures/特有属性配置-BarcodeInfo.png" width="700" alt="特有属性配置-BarcodeInfo">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - Feature页面下的BarcodeInfo属性无页面渲染效果。
> - Barcode组件不支持回调事件的配置。
> - BarcodeInfo不能设置为空，且不支持中文，如果设置为空或者为中文，模拟器中显示条形码失败。
> - BarcodeInfo设置完成后请点击其他位置后，再生成代码。

#### CardPage组件<a name="ZH-CN_TOPIC_0000002399739765"></a>

本组件的General属性请参见“11.1.2.2 组件的共有属性”描述。

- 选中画布内的CardPage组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621509.png" width="36"> 样式图标（Feature），在展开的Feature栏中有一个IsCoverable属性，默认为false，它的作用是设置拖动其他CardPage组件展示时是否覆盖上一个。

  **图 1** 特有属性配置：IsCoverable<a name="fig195722386343"></a>
  <img style="display:block;" src="figures/特有属性配置-IsCoverable.png" width="700" alt="特有属性配置-IsCoverable">

- 选中画布内的CardPage组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101610.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  CardPage组件支持的事件类型有：OnClick、OnLongPress、OnDrag、OnDragStart、OnDragEnd、OnPress、OnCancel、OnRelease、OnFocus、OnBlur、OnRotate、OnRotateStart、OnRotateEnd。

  **图 2** 回调事件配置<a name="fig1790072115352"></a>
  <img style="display:block;" src="figures/回调事件配置-44.png" width="700" alt="回调事件配置-44">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - Feature页面下的属性无界面渲染效果。
> - CardPage是一个容器组件，主要作为CrossView的子组件使用。

#### CrossView组件<a name="ZH-CN_TOPIC_0000002366099986"></a>

本组件的General属性请参见“11.1.2.2 组件的共有属性”描述。

- 选中CrossView组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741433.png" width="36">样式图标（Feature），在展开的Feature栏中可以看到EnableScreenCap属性，会弹出一个设定bool变量值的下拉框，它决定切换卡片时是否使能截图模式。

  **图 1** 特有属性配置：EnableScreenCap<a name="fig1358134319354"></a>

  <img style="display:block;" src="figures/zh-cn_image_0000002366101638.png" width="700">

- 选中CrossView组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941766.png" width="36">样式图标（Feature），在展开的Feature栏中可以看到SetAnimatorTime属性，它决定模拟器中松手动画时间，其单位为毫秒（ms）。

  **图 2** 特有属性配置：SetAnimatorTime<a name="fig2959881495"></a>

  <img style="display:block;" src="figures/zh-cn_image_0000002366101662.png" width="700">

- 选中CrossView组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621581.png" width="36">样式图标（Feature），在展开的Feature栏中可以看到DragDirection属性，它决定子组件拖拽来的方向。

  **图 3** 特有属性配置：DragDirection<a name="fig1772818954716"></a>

  <img style="display:block;" src="figures/zh-cn_image_0000002365941782.png" width="700">

  当拖拽来的组件不是CardPage类型时，右下角会有“Only supports cardpage component”或“仅支持拖拽CardPage组件”提示，并且拖入的子组件不会在画布上展示。

  **图 4** 特有属性配置：DragDirection（仅支持拖拽CardPage类型的子组件）<a name="fig634965194814"></a>
  <img style="display:block;" src="figures/特有属性配置-DragDirection（仅支持拖拽CardPage类型的子组件）.png" width="700" alt="特有属性配置-DragDirection（仅支持拖拽CardPage类型的子组件）">

  CrossView组件前端渲染界面仅会展示其某一个CardPage子组件：
  - 当新增CardPage组件时，默认会展示最新拖拽进来的CardPage组件，隐藏掉之前的；
  - 当删除CardPage组件时，默认会展示上个被拖入的CardPage组件，并隐藏掉其他的。

  如果想实现切换，可以点击“GUI拖拽界面介绍”中所介绍的Panel面板的<img src="figures/zh-cn_image_0000002366101686.png" width="49">按钮，该按钮使用说明如下：
  1. 左右切换会分别显示拖拽来的上一个和下一个CardPage子组件。
  2. 是否支持组件间的循环切换和模拟器的设定规则保持一致，可以在Feature栏的Isloop中选择True或False。当置为False时，第一个组件单击左按钮和最后一个组件单击右按钮时不会有切换效果；当置为True时，第一个组件单击左按钮和最后一个组件单击右按钮时会实现彼此切换。
  3. 切换按钮仅在选中父组件为CrossView的CardPage子组件时生效，选中操作可以通过单击左侧组件树中的CardPage，或在渲染界面单击CardPage后单击左右按钮，从而展示被选中组件的前一个和后一个，如图5所示。
  4. 切换按钮如果选的不是父组件为CrossView的CardPage子组件时，会弹窗提示，如图6所示。

  **图 5** 特有属性配置：DragDirection（CardPage切换展示逻辑）<a name="fig10608162418201"></a>
  <img style="display:block;" src="figures/特有属性配置-DragDirection（CardPage切换展示逻辑）.png" width="700" alt="特有属性配置-DragDirection（CardPage切换展示逻辑）">

  **图 6** 特有属性配置：DragDirection（非CrossView子组件切换的弹窗提醒）<a name="fig560918241207"></a>
  <img style="display:block;" src="figures/特有属性配置-DragDirection（非CrossView子组件切换的弹窗提醒）.png" width="700" alt="特有属性配置-DragDirection（非CrossView子组件切换的弹窗提醒）">

  当选择DragDirection为Horizontal方向时，拖拽CardPage组件，CardPage个数不做限制，每次拖拽入新的都会隐藏掉其他的CardPage子组件。

  **图 7** 特有属性配置：DragDirection（水平方向拖拽来的CardPage类型子组件）<a name="fig12609112419209"></a>
  <img style="display:block;" src="figures/特有属性配置-DragDirection（水平方向拖拽来的CardPage类型子组件）.png" width="700" alt="特有属性配置-DragDirection（水平方向拖拽来的CardPage类型子组件）">

  当选择DragDirection为Vertical-Up方向时，拖拽CardPage组件，拖拽新的组件时也会隐藏掉其他的CardPage子组件，但仅支持拖拽一个，当再次拖拽该方向的CardPage子组件时右下角会有“UpPage direction only supports one component”或“竖直上方向的CardPage组件仅支持拖拽一个”提示。

  **图 8** 特有属性配置：DragDirectio（竖直上方向仅支持拖拽一个子组件）<a name="fig1260952419208"></a>
  <img style="display:block;" src="figures/特有属性配置-DragDirectio（竖直上方向仅支持拖拽一个子组件）.png" width="700" alt="特有属性配置-DragDirectio（竖直上方向仅支持拖拽一个子组件）">

  当选择DragDirection为Vertical-Down方向时，拖拽CardPage组件，拖拽新的组件时也会隐藏掉其他的CardPage子组件，且仅支持拖拽的个数为一个，当再次拖拽该方向的CardPage子组件时右下角会有“DownPage direction only supports one component”或“竖直下方向的CardPage组件仅支持拖拽一个”提示。

  **图 9** 特有属性配置：DragDirection（竖直下方向仅支持拖拽一个子组件）<a name="fig16609142412208"></a>
  <img style="display:block;" src="figures/特有属性配置-DragDirection（竖直下方向仅支持拖拽一个子组件）.png" width="700" alt="特有属性配置-DragDirection（竖直下方向仅支持拖拽一个子组件）">

- 选中CrossView组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941822.png" width="36">样式图标（Feature），在展开的Feature栏中点击Isloop属性，会弹出一个设定bool变量值的下拉框，它决定是否开启水平卡片循环模式。

  **图 10** 特有属性配置：Isloop<a name="fig18540511191815"></a>

  <img style="display:block;" src="figures/zh-cn_image_0000002399741541.png" width="700">

- 选中CrossView组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101718.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  CrossView组件支持的事件有：OnClick、OnLongPress、OnDrag、OnDragStart、OnDragEnd、OnPress、OnCancel、OnRelease、OnFocus、OnBlur、OnRotate、OnRotateStart、OnRotateEnd、OnSwipe。其中OnSwipe默认为True。

  **图 11** 回调事件配置<a name="fig5540511151817"></a>

  <img style="display:block;" src="figures/zh-cn_image_0000002399621633.png" width="700">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - Feature界面除DragDirection的特性和Isloop与GUI界面前端渲染关联外，其他属性无界面渲染效果，可在模拟器中查看。
> - CrossView组件仅支持CardPage类型的子组件拖拽。
> - CrossView组件的所有弹窗均支持中英文适配。

#### MapView组件<a name="ZH-CN_TOPIC_0000002399619897"></a>

本组件的General属性请参见“11.1.2.2 组件的共有属性”描述。

> ![](public_sys-resources/icon-notice.gif) **须知：**
> 使用MapView前，需要将随SDK携带的map_convert_tool复制到“tools\\simulator”目录下。

- 选中MapView组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941846.png" width="36">样式图标（Feature），在展开的Feature栏中单击SvgPath右侧的图标，会弹出一个选择Svg文件的界面，解压地图对应的Svg文件到任意目录，单击选择后，再次打开该目录，刷新，可以看到会生成一个与Svg文件同名的bin文件，该文件用于模拟器读取并展示。同时该地图文件会绘制到画布中。

  **图 1** 特有属性配置：SvgPath-选择Svg文件<a name="fig1556381810504"></a>
  <img style="display:block;" src="figures/特有属性配置-SvgPath-选择Svg文件.png" width="700" alt="特有属性配置-SvgPath-选择Svg文件">

  **图 2** 特有属性配置：SvgPath-绘制Svg图片<a name="fig761210910508"></a>
  <img style="display:block;" src="figures/特有属性配置-SvgPath-绘制Svg图片.png" width="700" alt="特有属性配置-SvgPath-绘制Svg图片">

- 选中MapView组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621645.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  MapView组件支持的事件有：OnClick、OnLongPress、OnDrag、OnDragStart、OnDragEnd、OnPress、OnCancel、OnRelease、OnFocus、OnBlur、OnRotate、OnRotateStart、OnRotateEnd和OnPOIClick。

  **图 3** 回调事件配置<a name="fig982152854217"></a>
  <img style="display:block;" src="figures/回调事件配置-45.png" width="700" alt="回调事件配置-45">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - MapView是地图组件，应将地图文件展示到画布和模拟器中。
> - MapView的General属性仅包含ID、Position两个选项可供用户设置，工具和模拟器会默认展示该Svg图片的原始大小，用户可以根据模拟器实际效果调整Position参数。

#### RollerView组件<a name="ZH-CN_TOPIC_0000002365940090"></a>

本组件的共有属性不包含Border属性、Margin属性与Padding属性，其他共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中RollerView组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741561.png" width="36">样式图标（Feature），在展开的Feature栏导入一张或者多张图片（可以调整画布大小，使图片显示效果更好），第一张图片默认位于画布正中间。
  **图 1** 特有属性配置：ImagePath<a name="fig144651235202314"></a>
  <img style="display:block;" src="figures/特有属性配置-ImagePath-46.png" width="700" alt="特有属性配置-ImagePath-46">
  > ![](public_sys-resources/icon-note.gif) **说明：**
  > ImagePath不支持中文路径。
  > 导入的Bin文件必须是图片转的Bin，否则模拟器会异常。
- 选中画布内的RollerView组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399621649.png" width="36">样式图标（Feature），在展开的Feature栏中修改RollerView组件中的ImageWidth和ImageHeight可以调整图片宽高。

  更改图片宽高后，所有导入RollerView组件的图片宽高随之改变，且第一张图片始终位于组件的正中间。

  **图 2** 特有属性配置：ImageWidth和ImageHeight<a name="fig1549113615248"></a>
  <img style="display:block;" src="figures/特有属性配置-ImageWidth和ImageHeight.png" width="700" alt="特有属性配置-ImageWidth和ImageHeight">

- 选中画布内的RollerView组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002474130925.png" width="36">样式图标（Feature），在展开的Feature栏中修改RollerView组件中的MirrorOpacity调整滚筒元素镜像图的透明度。

  **图 3** 特有属性配置：MirrorOpacity<a name="fig514874910116"></a>
  <img style="display:block;" src="figures/特有属性配置-MirrorOpacity.png" width="700" alt="特有属性配置-MirrorOpacity">

- 选中画布内的RollerView组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002440730820.png" width="36">样式图标（Feature），在展开的Feature栏中修改RollerView组件中的SensitivityFactor调整滚筒灵敏度。

  **图 4** 特有属性配置：SensitivityFactor<a name="fig2991158101319"></a>
  <img style="display:block;" src="figures/特有属性配置-SensitivityFactor.png" width="700" alt="特有属性配置-SensitivityFactor">

- 选中画布内的RollerView组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399741565.png" width="36">样式图标（Feature），在展开的Feature栏中修改RollerView组件中的Padding调整图片之间的间距。

  **图 5** 特有属性配置：Padding<a name="fig2142192232415"></a>
  <img style="display:block;" src="figures/特有属性配置-Padding-47.png" width="700" alt="特有属性配置-Padding-47">

- 选中画布内的RollerView组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399621653.png" width="36">样式图标（Feature），在展开的Feature栏中修改RollerView组件中的CameraDistance设置模拟器中相机的距离。

  **图 6** 特有属性配置：CameraDistance<a name="fig25262913248"></a>
  <img style="display:block;" src="figures/特有属性配置-CameraDistance.png" width="700" alt="特有属性配置-CameraDistance">

- 选中画布内的RollerView组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399741569.png" width="36">样式图标（Feature），在展开的Feature栏中修改RollerView组件中的CamY设置模拟器中相机的Y坐标。

  **图 7** 特有属性配置：CamY<a name="fig96581036102413"></a>
  <img style="display:block;" src="figures/特有属性配置-CamY.png" width="700" alt="特有属性配置-CamY">

- 选中画布内的RollerView组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621657.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  RollerView组件支持的事件有：OnClick、OnLongPress、OnDrag、OnDragStart、OnDragEnd、OnPress、OnCancel、OnRelease、OnFocus、OnBlur、OnScroll、OnModeChange。

  **图 8** 回调事件配置<a name="fig17698142911119"></a>
  <img style="display:block;" src="figures/回调事件配置-48.png" width="700" alt="回调事件配置-48">

> ![](public_sys-resources/icon-note.gif) **说明：**
> Feature页面下的CameraDistance和CamY暂无渲染效果，具体效果可以在模拟器查看。
> RollerView组件在模拟器中可以实现水平方向上将图片按照滚筒的形式排布并支持滚动交互。

#### HexagonsList组件<a name="ZH-CN_TOPIC_0000002399739769"></a>

本组件的共有属性不包含Border属性、Margin属性与Padding属性，其他共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中HexagonsList组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741573.png" width="36">样式图标（Feature），在展开的Feature栏导入一张或者多张图片（可以调整画布大小，使图片显示效果更好），第一张图片默认位于画布正中间。
  **图 1** 特有属性配置：ImagePath<a name="fig144651235202314"></a>
  <img style="display:block;" src="figures/特有属性配置-ImagePath-49.png" width="700" alt="特有属性配置-ImagePath-49">
  > ![](public_sys-resources/icon-note.gif) **说明：**
  > ImagePath不支持中文路径。
  > 导入的Bin文件必须是图片转的Bin，否则模拟器会异常。
- 选中画布内的HexagonsList组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399621661.png" width="36">样式图标（Feature），在展开的Feature栏中修改HexagonsList组件中的ImageWidth和ImageHeight可以调整图片宽高。

  更改图片宽高后，所有导入HexagonsList组件的图片宽高随之改变，且第一张图片始终位于组件的正中间。

  **图 2** 特有属性配置：ImageWidth和ImageHeight<a name="fig1549113615248"></a>
  <img style="display:block;" src="figures/特有属性配置-ImageWidth和ImageHeight-50.png" width="700" alt="特有属性配置-ImageWidth和ImageHeight-50">

- 选中画布内的HexagonsList组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399741577.png" width="36">样式图标（Feature），在展开的Feature栏中修改HexagonsList组件中的Padding调整图片之间的间距。

  **图 3** 特有属性配置：Padding<a name="fig2142192232415"></a>
  <img style="display:block;" src="figures/特有属性配置-Padding-51.png" width="700" alt="特有属性配置-Padding-51">

- 选中画布内的HexagonsList组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399621673.png" width="36">样式图标（Feature），在展开的Feature栏中修改HexagonsList组件中的OriImgDistance属性来设置模拟器中两个相邻图像中心之间的原始图像距离。

  **图 4** 特有属性配置：OriImgDistance<a name="fig25262913248"></a>
  <img style="display:block;" src="figures/特有属性配置-OriImgDistance.png" width="700" alt="特有属性配置-OriImgDistance">

- 选中画布内的HexagonsList组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399741585.png" width="36">样式图标（Feature），在展开的Feature栏中修改HexagonsList组件中的ImgSizeInCenter属性来设置模拟器中图像位于中心位置的大小。

  **图 5** 特有属性配置：ImgSizeInCenter<a name="fig9701121017913"></a>
  <img style="display:block;" src="figures/特有属性配置-ImgSizeInCenter.png" width="700" alt="特有属性配置-ImgSizeInCenter">

- 选中画布内的HexagonsList组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399621681.png" width="36">样式图标（Feature），在展开的Feature栏中修改HexagonsList组件中的ReboundedSize属性来设置回弹大小，即拖拽到列表边缘之外再释放后回弹至列表边缘移动的距离。

  **图 6** 特有属性配置：ReboundedSize<a name="fig17864205617814"></a>
  <img style="display:block;" src="figures/特有属性配置-ReboundedSize.png" width="700" alt="特有属性配置-ReboundedSize">

- 选中画布内的HexagonsList组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399741589.png" width="36">样式图标（Feature），在展开的Feature栏中修改HexagonsList组件中的ScrollBlankSize属性来设置模拟器中组件滚动视图时的空白大小。

  **图 7** 特有属性配置：ScrollBlankSizec<a name="fig1256315491283"></a>
  <img style="display:block;" src="figures/特有属性配置-ScrollBlankSizec.png" width="700" alt="特有属性配置-ScrollBlankSizec">

- 选中画布内的HexagonsList组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621689.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  HexagonsList组件支持的事件有：OnClick、OnLongPress、OnDrag、OnDragStart、OnDragEnd、OnPress、OnCancel、OnRelease、OnFocus、OnBlur、OnRotate、OnRotateStart、OnRotateEnd。

  **图 8** 回调事件配置<a name="fig17698142911119"></a>
  <img style="display:block;" src="figures/回调事件配置-52.png" width="700" alt="回调事件配置-52">

> ![](public_sys-resources/icon-note.gif) **说明：**
> Feature页面下的OriImgDistance、ImgSizeInCenter、ReboundedSize和ScrollBlankSize暂无渲染效果，具体效果可以在模拟器查看。
> ImageWidth、Padding，ImageHeight可以用于用户在界面展示多个组件时设置图片大小。
> Rebounded和ScrollBlankSize的初始值为227，是默认组件的Position为\(0, 0, 454, 454\)，即整个表盘。具体的取值大小可以根据实际模拟器展示效果进行调整，通常这个取值为组件宽度的一半。
> OriImgDistance和ImgSizeInCenter属性与组件宽度的乘积，决定了模拟器中图片的摆放位置关系。

#### IcosahedronView组件<a name="ZH-CN_TOPIC_0000002366099990"></a>

本组件的共有属性不包含Position属性、Border属性、Margin属性与Padding属性，其他共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中IcosahedronView组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741597.png" width="36">样式图标（Feature），在展开的Feature栏导入一张图片（可以调整画布大小，使图片显示效果更好），图片会默认填满整个画布。

  **图 1** 特有属性配置：DefaultSrc<a name="fig1411916381693"></a>
  <img style="display:block;" src="figures/特有属性配置-DefaultSrc.png" width="700" alt="特有属性配置-DefaultSrc">

- 选中IcosahedronView组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621693.png" width="36">样式图标（Feature），在展开的Feature栏中修改IcosahedronView组件中的LuminanceFactor属性来设置模拟器中亮度补偿因子，调整亮度。

  **图 2** 特有属性配置：LuminanceFactor<a name="fig51391045174012"></a>
  <img style="display:block;" src="figures/特有属性配置-LuminanceFactor.png" width="700" alt="特有属性配置-LuminanceFactor">

- IcosahedronView组件仅支持Image组件导入。IcosahedronView组件的DefaultSrc属性设置了默认图片，如果导入的Image组件的图片个数少于20张，则使用该默认图片填充，达到类似足球样式的模拟器效果图。

  **图 3** 仅支持导入Image组件<a name="fig14703195575718"></a>
  <img style="display:block;" src="figures/仅支持导入Image组件.png" width="700" alt="仅支持导入Image组件">

- 选中画布内的IcosahedronView组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101774.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  IcosahedronView组件支持的事件有：OnClick、OnLongPress、OnDrag、OnDragStart、OnDragEnd、OnPress、OnCancel、OnRelease、OnFocus、OnBlur、OnRotate、OnRotateStart、OnRotateEnd。

  **图 4** 回调事件配置<a name="fig1859035515919"></a>
  <img style="display:block;" src="figures/回调事件配置-53.png" width="700" alt="回调事件配置-53">

> ![](public_sys-resources/icon-note.gif) **说明：**
> IcosahedronView组件仅支持width和height调节，其坐标位置固定。

#### CanvasExt组件<a name="ZH-CN_TOPIC_0000002399619901"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中画布内的CanvasExt组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941902.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。CanvasExt组件支持的事件有：OnClick、OnLongPress、OnPress、OnCancel和OnRelease。

  **图 1** 回调事件配置<a name="fig863319505301"></a>
  <img style="display:block;" src="figures/回调事件配置-54.png" width="700" alt="回调事件配置-54">

#### TransformList组件<a name="ZH-CN_TOPIC_0000002365940094"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中TransformList组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101786.png" width="36">样式图标（Feature），在展开的Feature栏中修改itemHeight属性设置所有子项的高度；修改itemWidth属性设置所有子项的宽度；修改itemSpace属性设置子项之间的间隙；修改imageHeight属性设置所有子项图片的高度；修改FontSize属性设置所有子项的字体大小；点击Item栏右侧的加号添加子项，修改子项中的Text属性和ImagePath属性添加文本和图片。

  **图 1** 添加子项<a name="fig1424214304315"></a>
  <img style="display:block;" src="figures/添加子项-55.png" width="700" alt="添加子项-55">

- 选中TransformList组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941910.png" width="36">样式图标（Feature），在展开的Feature栏中修改List组件的OffsetX属性设置所有子项的横向偏移，修改OffsetY属性设置所有子项的纵向偏移。

  **图 2** 修改子项的偏移<a name="fig8644443123216"></a>
  <img style="display:block;" src="figures/修改子项的偏移-56.png" width="700" alt="修改子项的偏移-56">

- 选中TransformList组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002366101790.png" width="36">样式图标（Feature），在展开的Feature栏中修改TransformList组件的Direction属性设置列表的排列方向。

  **图 3** 修改列表的排列方向<a name="fig640685910323"></a>
  <img style="display:block;" src="figures/修改列表的排列方向-57.png" width="700" alt="修改列表的排列方向-57">

- 选中画布内的TransformList组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365941914.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  TransformList组件支持的事件有：OnClick、OnLongPress、OnDrag、OnDragStart、OnDragEnd、OnPress、OnCancel、OnRelease、OnFocus和OnBlur。

  **图 4** 回调事件配置<a name="fig186332171075"></a>
  <img style="display:block;" src="figures/回调事件配置-58.png" width="700" alt="回调事件配置-58">

#### SlipflowView组件<a name="ZH-CN_TOPIC_0000002399739773"></a>

本组件的共有属性不包含Position属性、Size属性、GaussOption属性、Border属性、Margin属性与Padding属性，其他共有属性使用方法请参见“11.1.2.2 组件的共有属性”描述。

- 选中画布内的SlipflowView组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002366101794.png" width="36">样式图标（Feature），在展开的Feature栏中修改SlipflowView组件中的ImgWidth和ImgHeight可以调整图片宽高。

  更改图片宽高后，所有导入SlipflowView组件的图片宽高随之改变，且第一张图片始终位于组件的正中间。

  **图 1** 特有属性配置：ImgWidth和ImgHeight<a name="fig186308234339"></a>
  <img style="display:block;" src="figures/特有属性配置-ImgWidth和ImgHeight-59.png" width="700" alt="特有属性配置-ImgWidth和ImgHeight-59">

- 选中画布内的SlipflowView组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399741625.png" width="36">样式图标（Feature），在展开的Feature栏中修改SlipflowView组件中的isEnableBackImage可以控制是否使能背景图片。

  **图 2** 特有属性配置：isEnableBackImage<a name="fig951023617338"></a>
  <img style="display:block;" src="figures/特有属性配置-isEnableBackImage.png" width="700" alt="特有属性配置-isEnableBackImage">

- 选中SlipflowView组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621717.png" width="36">样式图标（Feature），在展开的Feature栏中修改SlipflowView组件中的backImagePath可以设置背景图片资源路径。

  **图 3** 特有属性配置：backImagePath<a name="fig1650517572334"></a>
  <img style="display:block;" src="figures/特有属性配置-backImagePath.png" width="700" alt="特有属性配置-backImagePath">

- 选中SlipflowView组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741629.png" width="36">样式图标（Feature），在展开的Feature栏导入一张或者多张图片（可以调整画布大小，使图片显示效果更好），第一张图片默认位于画布正中间。

  **图 4** 特有属性配置：ImagePath<a name="fig144651235202314"></a>

  <img style="display:block;" src="figures/zh-cn_image_0000002366101802.png" width="700">

  > ![](public_sys-resources/icon-note.gif) **说明：**
  > ImagePath不支持中文路径。
  > 导入的Bin文件必须是图片转的Bin，否则模拟器会异常。

- 选中画布内的SlipflowView组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399621721.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  SlipflowView组件支持的事件有：OnClick、OnLongPress、OnPress、OnCancel、OnRelease、OnScroll、OnScrollUpStart、OnScrollUpEnd、OnRemove和OnRefreshPageOpaScale。

  **图 5** 回调事件配置<a name="fig4163730162310"></a>
  <img style="display:block;" src="figures/回调事件配置-60.png" width="700" alt="回调事件配置-60">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - SlipflowView组件坐标位置固定，大小固定。
> - Feature页面下的isEnableBackImage和backImagePath暂无渲染效果，具体效果可以在模拟器查看。

#### TransformGroup组件<a name="ZH-CN_TOPIC_0000002366099994"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中画布内的TransformGroup组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002399741665.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  TransformGroup组件支持的事件类型有：OnClick、OnLongPress、OnPress、OnCancel、OnRelease。

  **图 1** 回调事件配置<a name="fig1790072115352"></a>
  <img style="display:block;" src="figures/回调事件配置-61.png" width="700" alt="回调事件配置-61">

> ![](public_sys-resources/icon-note.gif) **说明：**
> TransformGroup是一个容器组件，主要作为Coverflow2的子组件使用。

#### Coverflow2组件<a name="ZH-CN_TOPIC_0000002399619905"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中画布内的Coverflow2组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399621761.png" width="36">样式图标（Feature），在展开的Feature栏中修改Coverflow2组件中的RotateAngle调整旋转角度。

  **图 1** 特有属性配置：RotateAngle<a name="fig1917017159243"></a>

  <img style="display:block;" src="figures/zh-cn_image_0000002365941966.png" width="700">

- 选中画布内的Coverflow2组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399741673.png" width="36">样式图标（Feature），在展开的Feature栏中修改Coverflow2组件中的Padding调整图片之间的间距。

  **图 2** 特有属性配置：Padding<a name="fig2142192232415"></a>

  <img style="display:block;" src="figures/zh-cn_image_0000002366101846.png" width="700">

- 选中画布内的Coverflow2组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399621765.png" width="36">样式图标（Feature），在展开的Feature栏中修改Coverflow2组件中的IsShowMirrorImg设置是否显示图片镜像。

  **图 3** 特有属性配置：IsShowMirrorImg<a name="fig25262913248"></a>

  <img style="display:block;" src="figures/zh-cn_image_0000002365941970.png" width="700">

- 选中画布内的Coverflow2组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002399741677.png" width="36">样式图标（Feature），在展开的Feature栏中修改Coverflow2组件中的MirrorOpa设置图片镜像的透明度。

  **图 4** 特有属性配置：MirrorOpa<a name="fig96581036102413"></a>

  <img style="display:block;" src="figures/zh-cn_image_0000002366101850.png" width="700">

  当拖拽来的组件不是TransformGroup类型时，右下角会有“Only supports transformgroup component”或“仅支持拖拽TransformGroup组件”提示，并且拖入的子组件不会在画布上展示。

  **图 5** 组件拖入Coverflow2组件中<a name="fig1535915143218"></a>
  <img style="display:block;" src="figures/组件拖入Coverflow2组件中.png" width="700" alt="组件拖入Coverflow2组件中">

Coverflow2组件前端渲染界面仅会展示其某一个TransformGroup子组件：

- 当新增TransformGroup组件时，默认会展示最新拖拽进来的TransformGroup组件，隐藏掉之前的；
- 当删除TransformGroup组件时，默认会展示上个被拖入的TransformGroup组件，并隐藏掉其他的。

如果想实现切换，可以单击“GUI拖拽界面介绍”中的Panel面板的<img src="figures/zh-cn_image_0000002365941974.png" width="49">按钮，该按钮使用说明如下：

1. 左右切换会分别显示拖拽来的上一个和下一个TransformGroup子组件。
2. 切换按钮在选中父组件为Coverflow2的TransformGroup子组件时生效，选中操作可以通过单击左侧组件树中的TransformGroup，或在渲染界面单击TransformGroup后单击左右按钮，从而展示被选中组件的前一个和后一个，如图6所示。
3. 切换按钮如果选的不是父组件为Coverflow2的TransformGroup子组件时，会弹窗提示，如图7所示。

**图 6** TransformGroup切换展示逻辑<a name="fig14330923143518"></a>
<img style="display:block;" src="figures/TransformGroup切换展示逻辑.png" width="700" alt="TransformGroup切换展示逻辑">

**图 7** 非Coverflow2子组件切换的弹窗提醒<a name="fig1459413716407"></a>
<img style="display:block;" src="figures/非Coverflow2子组件切换的弹窗提醒.png" width="700" alt="非Coverflow2子组件切换的弹窗提醒">

#### ParticleView组件<a name="ZH-CN_TOPIC_0000002414912630"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中画布内的ParticleView组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002415072518.png" width="36">样式图标（Feature），在展开的Feature栏中修改ParticleView组件中的birthRateRatio调整粒子生产率系数，该系数将与ParticleCell定义的粒子生产率相乘。

  **图 1** 特有属性配置：birthRateRatio<a name="fig910505382912"></a>
  <img style="display:block;" src="figures/特有属性配置-birthRateRatio.png" width="700" alt="特有属性配置-birthRateRatio">

- 选中画布内的ParticleView组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002414912694.png" width="36">样式图标（Feature），在展开的Feature栏中修改ParticleView组件中的lifeTimeRatio调整粒子生命周期系数，该系数将与ParticleCell定义的粒子生命周期相乘。

  **图 2** 特有属性配置：lifeTimeRatio<a name="fig121968624213"></a>
  <img style="display:block;" src="figures/特有属性配置-lifeTimeRatio.png" width="700" alt="特有属性配置-lifeTimeRatio">

- 选中画布内的ParticleView组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002415072510.png" width="36">样式图标（Feature），在展开的Feature栏中修改ParticleView组件中的scaleRatio调整粒子缩放系数，该系数将与ParticleCell定义的粒子缩放倍数相乘。

  **图 3** 特有属性配置：scaleRatio<a name="fig1273042764519"></a>
  <img style="display:block;" src="figures/特有属性配置-scaleRatio.png" width="700" alt="特有属性配置-scaleRatio">

- 选中画布内的ParticleView组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002414912690.png" width="36">样式图标（Feature），在展开的Feature栏中修改ParticleView组件中的velocityRatio调整粒子速度系数，该系数将与ParticleCell定义的粒子速度相乘。

  **图 4** 特有属性配置：velocityRatio<a name="fig2389147184815"></a>
  <img style="display:block;" src="figures/特有属性配置-velocityRatio.png" width="700" alt="特有属性配置-velocityRatio">

- 选中画布内的ParticleView组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002415072506.png" width="36">样式图标（Feature），在展开的Feature栏中修改ParticleView组件中的Repeat调整粒子动画是否重复运行。

  **图 5** 特有属性配置：Repeat<a name="fig174436186489"></a>
  <img style="display:block;" src="figures/特有属性配置-Repeat.png" width="700" alt="特有属性配置-Repeat">

- 选中画布内的ParticleView组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002414912682.png" width="36">样式图标（Feature），在展开的Feature栏中修改ParticleView组件中的Time调整粒子动画运行周期。

  **图 6** 特有属性配置：Time<a name="fig18017328563"></a>
  <img style="display:block;" src="figures/特有属性配置-Time.png" width="700" alt="特有属性配置-Time">

- 选中画布内的ParticleView组件，通过右侧属性样式中的<img src="figures/zh-cn_image_0000002415072502.png" width="36">样式图标（Feature），在展开的Feature栏中点击ImagePath右侧的加号，导入一张或多张图片，并设置各项参数。

  **图 7** 特有属性配置：ImagePath<a name="fig913100132315"></a>
  <img style="display:block;" src="figures/特有属性配置-ImagePath-62.png" width="700" alt="特有属性配置-ImagePath-62">

  **表 1** 特有属性配置：ImagePath参数说明

  <a name="table17204037152519"></a>

  <table><thead align="left"><tr id="row22041537192514"><th class="cellrowborder" valign="top" width="37.230000000000004%" id="mcps1.2.3.1.1"><p id="p6204237152515"><a name="p6204237152515"></a><a name="p6204237152515"></a>属性</p>
  </th>
  <th class="cellrowborder" valign="top" width="62.77%" id="mcps1.2.3.1.2"><p id="p102046372256"><a name="p102046372256"></a><a name="p102046372256"></a>介绍</p>
  </th>
  </tr>
  </thead>
  <tbody><tr id="row3204143710258"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p72041371252"><a name="p72041371252"></a><a name="p72041371252"></a>Path</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p620413742511"><a name="p620413742511"></a><a name="p620413742511"></a>设置粒子图源。</p>
  </td>
  </tr>
  <tr id="row1020573782513"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p42051837172513"><a name="p42051837172513"></a><a name="p42051837172513"></a>CellWidth</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p891114132611"><a name="p891114132611"></a><a name="p891114132611"></a>设置粒子初始宽度。</p>
  </td>
  </tr>
  <tr id="row8205203717253"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p420516373255"><a name="p420516373255"></a><a name="p420516373255"></a>CellHeight</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p2205337152519"><a name="p2205337152519"></a><a name="p2205337152519"></a>设置粒子初始高度。</p>
  </td>
  </tr>
  <tr id="row4521651152719"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p9521105116271"><a name="p9521105116271"></a><a name="p9521105116271"></a>CellSizeRange</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p1152145142711"><a name="p1152145142711"></a><a name="p1152145142711"></a>设置粒子初始宽高上下浮动范围。</p>
  </td>
  </tr>
  <tr id="row779724562716"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p1379754572718"><a name="p1379754572718"></a><a name="p1379754572718"></a>PosX</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p279824552719"><a name="p279824552719"></a><a name="p279824552719"></a>设置粒子横向初始位置。</p>
  </td>
  </tr>
  <tr id="row420516372256"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p1720593716256"><a name="p1720593716256"></a><a name="p1720593716256"></a>PosY</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p226662423115"><a name="p226662423115"></a><a name="p226662423115"></a>设置粒子纵向初始位置。</p>
  </td>
  </tr>
  <tr id="row122051037172511"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p4205183718259"><a name="p4205183718259"></a><a name="p4205183718259"></a>PosXRange</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p82052037122517"><a name="p82052037122517"></a><a name="p82052037122517"></a>设置粒子横向初始位置上下浮动范围。</p>
  </td>
  </tr>
  <tr id="row720520373257"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p5205337122517"><a name="p5205337122517"></a><a name="p5205337122517"></a>PosYRange</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p911463613217"><a name="p911463613217"></a><a name="p911463613217"></a>设置粒子纵向初始位置上下浮动范围。</p>
  </td>
  </tr>
  <tr id="row19675194919321"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p467512494322"><a name="p467512494322"></a><a name="p467512494322"></a>Lifetime</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p10675134963217"><a name="p10675134963217"></a><a name="p10675134963217"></a>设置粒子生命周期。</p>
  </td>
  </tr>
  <tr id="row155488567324"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p854865615326"><a name="p854865615326"></a><a name="p854865615326"></a>LifetimeRange</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p2054825615324"><a name="p2054825615324"></a><a name="p2054825615324"></a>设置粒子生命周期上下浮动范围。</p>
  </td>
  </tr>
  <tr id="row396681173310"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p196615123319"><a name="p196615123319"></a><a name="p196615123319"></a>BirthRate</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p15966121133314"><a name="p15966121133314"></a><a name="p15966121133314"></a>设置粒子生产率：每个动画周期生产多少粒子。</p>
  </td>
  </tr>
  <tr id="row173016612331"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p1773016613317"><a name="p1773016613317"></a><a name="p1773016613317"></a>Velocity</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p12730126173314"><a name="p12730126173314"></a><a name="p12730126173314"></a>设置粒子速度。</p>
  </td>
  </tr>
  <tr id="row371125313218"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p117219532321"><a name="p117219532321"></a><a name="p117219532321"></a>VelocityRange</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p8722053163211"><a name="p8722053163211"></a><a name="p8722053163211"></a>设置粒子速度上下浮动范围。</p>
  </td>
  </tr>
  <tr id="row1855533544119"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p355653594111"><a name="p355653594111"></a><a name="p355653594111"></a>StartAlpha</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p1655613524111"><a name="p1655613524111"></a><a name="p1655613524111"></a>设置粒子起始透明度。</p>
  </td>
  </tr>
  <tr id="row58065391415"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p13807153918410"><a name="p13807153918410"></a><a name="p13807153918410"></a>FinalAlpha</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p1780733944116"><a name="p1780733944116"></a><a name="p1780733944116"></a>设置粒子最终透明度。</p>
  </td>
  </tr>
  <tr id="row812554594114"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p6125104519419"><a name="p6125104519419"></a><a name="p6125104519419"></a>AlphaRange</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p4125145184117"><a name="p4125145184117"></a><a name="p4125145184117"></a>设置粒子起始和最终透明度上下浮动范围。</p>
  </td>
  </tr>
  <tr id="row1168020714411"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p176806714413"><a name="p176806714413"></a><a name="p176806714413"></a>ScaleX</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p18681197204417"><a name="p18681197204417"></a><a name="p18681197204417"></a>设置粒子横向最终缩放倍数。</p>
  </td>
  </tr>
  <tr id="row17731911194415"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p12731711144417"><a name="p12731711144417"></a><a name="p12731711144417"></a>ScaleY</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p1073191113448"><a name="p1073191113448"></a><a name="p1073191113448"></a>设置粒子纵向最终缩放倍数。</p>
  </td>
  </tr>
  <tr id="row175261522134418"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p5526182213448"><a name="p5526182213448"></a><a name="p5526182213448"></a>ScaleRange</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p1152619221441"><a name="p1152619221441"></a><a name="p1152619221441"></a>设置粒子最终缩放倍数上下浮动范围。</p>
  </td>
  </tr>
  <tr id="row98292018114415"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p188291188445"><a name="p188291188445"></a><a name="p188291188445"></a>AccelerationX</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p8681252194818"><a name="p8681252194818"></a><a name="p8681252194818"></a>设置粒子横向加速度。</p>
  </td>
  </tr>
  <tr id="row13179101524415"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p3179161515447"><a name="p3179161515447"></a><a name="p3179161515447"></a>AccelerationY</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p73541316134911"><a name="p73541316134911"></a><a name="p73541316134911"></a>设置粒子纵向加速度。</p>
  </td>
  </tr>
  <tr id="row1330413394413"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p0304123344415"><a name="p0304123344415"></a><a name="p0304123344415"></a>EmissionAngle</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p1304113312447"><a name="p1304113312447"></a><a name="p1304113312447"></a>设置粒子发射角度。</p>
  </td>
  </tr>
  <tr id="row1052213317498"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p1152203112496"><a name="p1152203112496"></a><a name="p1152203112496"></a>EmissionRange</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p9522133134910"><a name="p9522133134910"></a><a name="p9522133134910"></a>设置粒子发射角度上下浮动范围。</p>
  </td>
  </tr>
  <tr id="row17855163519497"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p18551635154910"><a name="p18551635154910"></a><a name="p18551635154910"></a>TotalPeriod</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p16855183518497"><a name="p16855183518497"></a><a name="p16855183518497"></a>设置ParticleCell活跃周期。仅在活跃周期内的ParticleCell可以生产粒子。</p>
  </td>
  </tr>
  <tr id="row1667124013494"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p567154010498"><a name="p567154010498"></a><a name="p567154010498"></a>Spin</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p196711440194912"><a name="p196711440194912"></a><a name="p196711440194912"></a>设置粒子周期性旋转度数。</p>
  </td>
  </tr>
  <tr id="row6951194210499"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p795184214919"><a name="p795184214919"></a><a name="p795184214919"></a>SpinMode</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p095110422498"><a name="p095110422498"></a><a name="p095110422498"></a>设置粒子周期性旋转模式。</p>
  </td>
  </tr>
  <tr id="row15625194512496"><td class="cellrowborder" valign="top" width="37.230000000000004%" headers="mcps1.2.3.1.1 "><p id="p562514584911"><a name="p562514584911"></a><a name="p562514584911"></a>SpinRange</p>
  </td>
  <td class="cellrowborder" valign="top" width="62.77%" headers="mcps1.2.3.1.2 "><p id="p5625174594917"><a name="p5625174594917"></a><a name="p5625174594917"></a>设置粒子周期性旋转度数上下浮动范围。</p>
  </td>
  </tr>
  </tbody>
  </table>

#### LabelExt组件<a name="ZH-CN_TOPIC_0000002484375920"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中画布内的LabelExt组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002484376794.png" width="36">样式图标（Feature），在展开的Feature栏中修改LabelExt组件的Text属性来编辑文本内容（新添加组件默认文本内容为“default”）。

  **图 1** 特有属性配置：Text文本内容<a name="fig455274919252"></a>
  <img style="display:block;" src="figures/特有属性配置-Text文本内容-63.png" width="700" alt="特有属性配置-Text文本内容-63">

- 选中画布内的LabelExt组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002516736717.png" width="36">样式图标（Feature），在展开的Feature栏中设置LabelExt组件的Font属性：
  - Color：字体颜色
  - Size：字体大小
  - LetterSpace：字母间距
  - LineSpace：行间距
  - LineHeight：行高（行高小于字体大小时将以字体大小为准，最终行高＝行高＋行间距）
  - TextDirection：文本方向

  **图 2** 通用属性配置：文本相关属性<a name="fig15826115915219"></a>
  <img style="display:block;" src="figures/通用属性配置-文本相关属性-64.png" width="700" alt="通用属性配置-文本相关属性-64">

- 选中画布内的LabelExt组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002484376796.png" width="36">样式图标（Feature），在展开的Feature栏中修改LabelExt组件的TextAlign属性改变文字的横向与纵向排布。

  **图 3** 改变文字排布<a name="fig195425918268"></a>
  <img style="display:block;" src="figures/改变文字排布-65.png" width="700" alt="改变文字排布-65">

- 选中画布内的LabelExt组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002516736719.png" width="36">样式图标（Feature），在展开的Feature栏中修改LabelExt组件的LineBreakMode属性。LineBreakMode对应6种换行模式，详细介绍如下：
  - Adapt：组件大小自适应文本，且不会对文本做自动换行。

    > ![](public_sys-resources/icon-note.gif) **说明：**
    > 组件宽高不受通用属性Width/Height值影响，因此不可通过拖拽组件或直接修改Width/Height值的方式改变组件宽高。

    **图 4** LineBreakMode - Adapt<a name="fig1679161320461"></a>
    <img style="display:block;" src="figures/LineBreakMode---Adapt-66.png" width="700" alt="LineBreakMode---Adapt-66">

  - Stretch：组件高度按照设置的Height值显示，宽度由文本中最长的行决定，文本不会自动换行。

    > ![](public_sys-resources/icon-note.gif) **说明：**
    > 组件宽度不受通用属性Width值影响，因此不可通过拖拽组件或直接修改Width值的方式改变组件宽度。

    **图 5** LineBreakMode - Stretch<a name="fig8791181319462"></a>
    <img style="display:block;" src="figures/LineBreakMode---Stretch-67.png" width="700" alt="LineBreakMode---Stretch-67">

  - Wrap：组件宽度按照设置的Width值显示，文本自动换行，组件高度由文本行数决定。

    > ![](public_sys-resources/icon-note.gif) **说明：**
    > 组件高度不受通用属性Height值影响，因此不可通过拖拽组件或直接修改Height值的方式改变组件高度。

    **图 6** LineBreakMode - Wrap<a name="fig177911513124619"></a>
    <img style="display:block;" src="figures/LineBreakMode---Wrap-68.png" width="700" alt="LineBreakMode---Wrap-68">

  - Ellipsis：组件大小按照设置的Height和Width值显示，文本自动换行，超出组件的文本将在末尾以省略号的形式显示。

    **图 7** LineBreakMode - Ellipsis<a name="fig1179181314462"></a>
    <img style="display:block;" src="figures/LineBreakMode---Ellipsis-69.png" width="700" alt="LineBreakMode---Ellipsis-69">

  - Clip：组件大小按照设置的Height和Width值显示，文本自动换行，超出组件的文本将在末尾自动隐藏。

    **图 8** LineBreakMode - Clip<a name="fig14791191324610"></a>
    <img style="display:block;" src="figures/LineBreakMode---Clip-70.png" width="700" alt="LineBreakMode---Clip-70">

  - Marquee：组件大小按照设置的Height和Width值显示，文本不自动换行，超出组件的文本将自动隐藏。

    > ![](public_sys-resources/icon-note.gif) **说明：**
    > 此模式下当单行文本长度不超出组件时，文本按照设置的TextAlign进行对齐。
    > 文本长度超出组件时，文本会自动向左循环滚动播放。

    **图 9** LineBreakMode - Marquee<a name="fig530611174710"></a>
    <img style="display:block;" src="figures/LineBreakMode---Marquee-71.png" width="700" alt="LineBreakMode---Marquee-71">

- 选中画布内的LabelExt组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002516616733.png" width="36">样式图标（Feature），在展开的Feature栏中修改LabelExt组件的RollAnimation属性。
  RollAnimation属性只在LineBreakMode为Marquee且文本长度超出时生效。RollAnimation包含滚动速度（Speed）和滚动起始位置（Pos）。
  **图 10** 特有属性配置：RollAnimation<a name="fig19196141194615"></a>
  <img style="display:block;" src="figures/特有属性配置-RollAnimation-72.png" width="700" alt="特有属性配置-RollAnimation-72">
  > ![](public_sys-resources/icon-note.gif) **说明：**
  >
  > - General页面下的MarginBottom属性和MarginRight属性没有任何界面渲染效果，可在模拟器上查看效果。
  > - LabelExt组件不支持配置回调事件。
- 选中画布内的LabelExt组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002516744281.png" width="36">样式图标（Feature），在展开的Feature栏中修改LabelExt组件的TextId属性，设置TextId，该功能需用户手动注册多语言功能，否则界面无法正常显示。

  **图 11** 特有属性配置：TextId<a name="fig156815014613"></a>
  <img style="display:block;" src="figures/特有属性配置-TextId.png" width="700" alt="特有属性配置-TextId">

- 选中画布内的LabelExt组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002484544338.png" width="36">样式图标（Feature），在展开的Feature栏中修改LabelExt组件的ForceResetText属性，强制根据控件内部的TextId设置文本内容，该功能需用户手动注册多语言功能，否则界面无法正常显示。

  **图 12** 特有属性配置：ForceResetText<a name="fig3903715204816"></a>
  <img style="display:block;" src="figures/特有属性配置-ForceResetText.png" width="700" alt="特有属性配置-ForceResetText">

#### ChartPillarExt组件<a name="ZH-CN_TOPIC_0000002555963293"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中ChartPillarExt组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002555963639.png" width="36">样式图标（Feature），在展开的Feature栏中修改XAxis栏中的属性改变横坐标的样式。
  - MarkNum属性：改变坐标轴上点的数量
  - RangMin和RangMax：改变坐标轴的取值范围
  - Color：改变坐标轴的颜色
  - Visible：控制坐标轴的可见与否

  **图 1** 修改横坐标属性<a name="fig123829568359"></a>
  <img style="display:block;" src="figures/修改横坐标属性-73.png" width="700" alt="修改横坐标属性-73">

- 选中ChartPillarExt组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002555964027.png" width="36">样式图标（Feature），在展开的Feature栏中修改YAxis栏中的属性改变纵坐标样式，具体设置与横坐标相同，请参考图2。

  **图 2** 修改纵坐标样式<a name="fig18433110133716"></a>
  <img style="display:block;" src="figures/修改纵坐标样式-74.png" width="700" alt="修改纵坐标样式-74">

- 选中ChartPillarExt组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002555964189.png" width="36">样式图标（Feature），在展开的Feature栏中单击DataSerial属性右侧的加号添加数据，可以添加多组数据。

  **图 3** 添加数据<a name="fig1728417410386"></a>
  <img style="display:block;" src="figures/添加数据-75.png" width="700" alt="添加数据-75">

- 选中ChartPillarExt组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002555964417.png" width="36">样式图标（Feature），在展开的Feature栏中添加数据然后改变数据的样式，其中Data属性是要填入的数据，DataCount属性是数据的个数，FillColor是填充颜色。

  **图 4** 添加数据效果展示<a name="fig187731248123814"></a>
  <img style="display:block;" src="figures/添加数据效果展示-76.png" width="700" alt="添加数据效果展示-76">

- 选中ChartPillarExt组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002555805449.png" width="36">样式图标（Feature），在展开的Feature栏中修改ChartPillarExt组件的PillarType属性改变图的类型。

  **图 5** 修改图的类型<a name="fig1353005014615"></a>
  <img style="display:block;" src="figures/修改图的类型-77.png" width="700" alt="修改图的类型-77">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的MarginBottom属性和MarginRight属性均无渲染效果。
> - 添加数据时的格式为： \{x1,y1\},\{x2,y2\};
>   数据中不能有空格，横坐标应从0开始依次递增，DataCount属性中的数字不能比数据个数小。当DataCount属性中的数字比数据个数大时，会自动补连\{0,0\}，柱状图时横坐标的MarkNum也不能比数据个数小。
> - 目前ChartPillarExt会有第一次修改DataSerial属性里的属性界面无法发生变化的问题，通过再次修改DataSerial属性中的其他属性的方式可以使界面发生变化。
> - ChartPillarExt组件不支持回调事件的配置。

#### ListNested组件<a name="ZH-CN_TOPIC_0000002555803331"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中ListNested组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002555965917.png" width="36">样式图标（Feature），在展开的Feature栏中修改itemHeight属性设置所有子项的高度；修改itemWidth属性设置所有子项的宽度；修改imageWidth属性设置所有子项图片的宽度；修改imageHeight属性设置所有子项图片的高度；修改FontSize属性设置所有子项的字体大小；单击Item栏右侧的加号添加子项，修改子项中的Text属性和ImagePath属性添加文本和图片。

  **图 1** 添加子项<a name="fig12369193710485"></a>
  <img style="display:block;" src="figures/添加子项-78.png" width="700" alt="添加子项-78">

- 选中ListNested组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002555805947.png" width="36">样式图标（Feature），在展开的Feature栏中修改ListNested组件的OffsetX属性设置所有子项的横向偏移，修改OffsetY属性设置所有子项的纵向偏移。

  **图 2** 修改子项的偏移<a name="fig18329101454916"></a>
  <img style="display:block;" src="figures/修改子项的偏移-79.png" width="700" alt="修改子项的偏移-79">

- 选中ListNested组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002524885994.png" width="36">样式图标（Feature），在展开的Feature栏中修改ListNested组件的InterceptDireaction属性设置拦截方向，修改IsIntercept属性设置是否拦截上抛事件。

  **图 3** 修改拦截事件相关属性<a name="fig11609952204914"></a>
  <img style="display:block;" src="figures/修改拦截事件相关属性.png" width="700" alt="修改拦截事件相关属性">

- 选中ListNested组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002524726044.png" width="36">样式图标（Feature），在展开的Feature栏中修改ListNested组件的Direction属性设置列表的排列方向。

  **图 4** 修改列表的排列方向<a name="fig115271937135017"></a>
  <img style="display:block;" src="figures/修改列表的排列方向-80.png" width="700" alt="修改列表的排列方向-80">

- 选中画布内的ListNested组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002555965859.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  ListNested组件支持的事件有：OnClick、OnLongPress、OnDrag、OnDragStart、OnDragEnd、OnPress、OnCancel、OnRelease、OnFocus和OnBlur。

  **图 5** 回调事件配置<a name="fig112356202517"></a>
  <img style="display:block;" src="figures/回调事件配置-81.png" width="700" alt="回调事件配置-81">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - General页面下的MarginBottom属性和MarginRight属性无渲染效果。
> - Feature页面下的Isloop属性、Autoalign属性、Aligntime属性、Startindex属性均没有界面渲染效果，在添加子元素后可在模拟器查看效果。

#### SwipeViewNested组件<a name="ZH-CN_TOPIC_0000002524723440"></a>

本组件的共有属性不包含Border属性、Margin属性与Padding属性，其他共有属性使用方法请参见“组件的共有属性”章节内容。

- 选中SwipeViewNested组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002524887776.png" width="36">样式图标（Feature），在展开的Feature栏中修改SwipeViewNested组件的Direction属性改变组件的滚动方向。子组件的位置是相对于父容器的左上角，当组件已经存在于界面上时，单击组件中心位置可以将组件拖入容器中。

  **图 1** 修改滚动条位置<a name="fig5584141412577"></a>
  <img style="display:block;" src="figures/修改滚动条位置-82.png" width="700" alt="修改滚动条位置-82">

  <img style="display:block;" src="figures/zh-cn_image_0000002555807703.png" width="700">

  > ![](public_sys-resources/icon-note.gif) **说明：**
  > 滚动条已被隐藏，当容器内的子组件超出范围时可拖动，HORIZONTAL是水平滚动，VERTICAL是垂直滚动。

- 选中SwipeViewNested组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002524887828.png" width="36">样式图标（Feature），在展开的Feature栏中修改SwipeViewNested组件的InterceptDireaction属性设置拦截方向，修改IsIntercept属性设置是否拦截上抛事件。

  **图 2** 修改拦截事件相关属性<a name="fig118081242145818"></a>
  <img style="display:block;" src="figures/修改拦截时间相关属性.png" width="700" alt="修改拦截时间相关属性">

- 选中画布内的SwipeViewNested组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002524727874.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  SwipeViewNested组件支持的事件有：OnDrag、OnDragStart、OnDragEnd、OnSwipe。

  **图 3** 回调事件配置<a name="fig1473842595917"></a>
  <img style="display:block;" src="figures/回调事件配置-83.png" width="700" alt="回调事件配置-83">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - Feature页面下的Isloop属性、AlignMode属性、TickTime属性暂无渲染效果。
> - 在水平模式下上方工具栏的顶部对齐<img src="figures/zh-cn_image_0000002555811581.png" width="28">、底部对齐<img src="figures/zh-cn_image_0000002555971545.png" width="33">、上下居中对齐<img src="figures/zh-cn_image_0000002555811585.png" width="29">不可用。
> - 在垂直模式下上方工具栏的左对齐<img src="figures/zh-cn_image_0000002555811583.png" width="35">、右对齐<img src="figures/zh-cn_image_0000002555971547.png" width="24">、左右居中对齐<img src="figures/zh-cn_image_0000002524731690.png" width="27">不可用。
> - SwipeViewNested的滚动条一直处于隐藏状态，但仍保持正常的拖拽方式。

#### LottieView组件<a name="ZH-CN_TOPIC_0000002524883390"></a>

共有属性使用方法请参见“组件的共有属性”章节内容。

> ![](public_sys-resources/icon-notice.gif) **须知：**
> 使用LottieView前，需要将随SDK携带的flatbuffertool复制到“tools\\simulator”目录下。

- 选中LottieView组件，单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002524891800.png" width="36">样式图标（Feature），在展开的Feature栏中单击LottiePath右侧的图标，会弹出一个选择Json文件的界面，选择Lottie对应的json文件，单击选择后，再次打开该目录、刷新，可以看到会生成一个与json文件同名的bin文件，该文件用于被模拟器读取并展示。同时画布中会显示Lottie图标。

  **图 1** 特有属性配置：LottiePath-选择Json文件<a name="fig1868010119219"></a>
  <img style="display:block;" src="figures/特有属性配置-LottiePath-选择Json文件.png" width="700" alt="特有属性配置-LottiePath-选择Json文件">

  **图 2** 特有属性配置：LottiePath-绘制lottie图标<a name="fig1664912213319"></a>
  <img style="display:block;" src="figures/特有属性配置-LottiePath-绘制lottie图标.png" width="700" alt="特有属性配置-LottiePath-绘制lottie图标">

- 选中LottieView组件，通过右侧属性样式栏中的<img src="figures/zh-cn_image_0000002555811967.png" width="23">样式图标（Events），在展开的Events栏中配置回调事件。

  LottieView组件支持的事件有：OnClick、OnLongPress、OnDrag、OnDragStart、OnDragEnd、OnPress、OnCancel、OnRelease、OnFocus、OnBlur、OnRotate、OnRotateStart、OnRotateEnd。

  **图 3** 回调事件配置<a name="fig1833365416315"></a>
  <img style="display:block;" src="figures/回调事件配置-84.png" width="700" alt="回调事件配置-84">

#### Root组件<a name="ZH-CN_TOPIC_0000002365940098"></a>

本组件为中央区域的背景画布。

**图 1** Root组件<a name="fig1548711534020"></a>
<img style="display:block;" src="figures/Root组件.png" width="700" alt="Root组件">

选中Root组件，在右侧展开的General栏中修改BackgroundColor属性，可以修改Root组件的颜色。

**图 2** 修改背景色<a name="fig1728445112456"></a>
<img style="display:block;" src="figures/修改背景色-85.png" width="700" alt="修改背景色-85">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - Root组件是所有组件的父组件。
> - Root组件是唯一的、自动创建的，不可进行除改变颜色外的其他操作。

#### 用户代码编辑<a name="ZH-CN_TOPIC_0000002399739777"></a>

用户单击画布右上角“Convert to C++ files”，会在工程中生成与界面样式对应的代码。

**图 1** 生成代码按钮<a name="fig36701735185010"></a>
<img style="display:block;" src="figures/生成代码按钮.png" width="700" alt="生成代码按钮">

以工程名为aaaa的aaaa.gui工程和Button组件为例，生成的代码目录位于工程目录下“application/wearable/nativeapp/gui工程名”，具体结构如图2所示。用户可自行在xxxPresenter.cpp文件中按照模板添加自己的回调事件，模板代码如图3所示，其余部分都是自动生成的，每次点击生成代码按钮都会刷新。

**图 2** 生成代码目录结构<a name="fig084021814113"></a>
<img style="display:block;" src="figures/生成代码目录结构.png" width="239" alt="生成代码目录结构">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - 从其他组件切成CrossView组件，或者从CrossView组件切成其他组件，而后去生成代码时，由于CrossView组件添加子组件的特殊性，需要先手动删除当前已有的“/src/$\{AppName\}View.cpp”后，再单击转换生成代码。
> - 其余“ui_xxView.h”格式的文件不可修改，GUI每次单击生成代码都会覆盖生成。

**图 3** 回调事件模板代码<a name="fig113311395104"></a>
<img style="display:block;" src="figures/回调事件模板代码.png" width="700" alt="回调事件模板代码">

以click的回调事件为例，如果当前画布中只有一个组件的click回调被置为true，用户可直接在OnClick的回调函数中添加回调事件，如果当前画布中有多个组件的click回调被置为true，则用户需要按照提示来区分组件实现各自的回调，如图4所示。

**图 4** 多个组件同一回调事件代码实现<a name="fig171118207109"></a>
<img style="display:block;" src="figures/多个组件同一回调事件代码实现.png" width="700" alt="多个组件同一回调事件代码实现">

#### 组件对齐<a name="ZH-CN_TOPIC_0000002366099998"></a>

组件对齐通过选中组件再单击界面上方工具栏中的对齐按钮<img style="display:block;" src="figures/zh-cn_image_0000002399741701.png" width="177">实现。

对齐效果分别为左对齐<img src="figures/zh-cn_image_0000002366101870.png" width="35">，左右居中对齐<img src="figures/zh-cn_image_0000002399621797.png" width="27">，右对齐<img src="figures/zh-cn_image_0000002365942006.png" width="24">，顶部对齐<img src="figures/zh-cn_image_0000002399741709.png" width="28">，上下居中对齐<img src="figures/zh-cn_image_0000002366101906.png" width="29">和底部对齐<img src="figures/zh-cn_image_0000002399621837.png" width="33">六种。

根据选中的组件个数不同，对齐操作分为两种：

- 选中一个组件

  只选中一个组件时，会将被选中的组件作为需要对齐的组件，以其父组件作为参照物进行对齐。可以通过组件树（Component Tree）查看组件的父子关系。

  > ![](public_sys-resources/icon-note.gif) **说明：**
  > 只选中Root组件时无效。

- 选中多个组件（通过按住Ctrl键单击多个组件）

  当被选中的组件不止一个时，将会以最后一个被选中的组件作为参照物，其他被选中的组件作为需要对齐的组件进行对齐。

  > ![](public_sys-resources/icon-note.gif) **说明：**
  > 被选中的组件只能为Root组件或其直接子组件。

#### 组件层级移动<a name="ZH-CN_TOPIC_0000002399619909"></a>

组件层级移动通过选中组件再单击界面上方工具栏中的层级移动按钮实现。

**图 1** 组件层级移动<a name="fig84841225105411"></a>
<img style="display:block;" src="figures/组件层级移动.png" width="700" alt="组件层级移动">

<img src="figures/zh-cn_image_0000002366101930.png" width="28">为前进一层，<img src="figures/zh-cn_image_0000002399621861.png" width="25">为后退一层。

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - 每次单击操作只能使组件向前/向后一层。
> - 同时选中多个组件时层级移动操作只对最后一个选中的组件生效。
> - 层级移动无法调整当前组件的父组件（如当前组件是ScrollView/SwipeView的子组件，层级移动操作无法将组件移出父组件）。
> - 组件树中越靠近顶端的组件层级越低，越靠近底部的组件层级越高。

#### 高斯模糊属性<a name="ZH-CN_TOPIC_0000002365940102"></a>

组件的高斯模糊属性通过单击右侧属性样式栏中的<img src="figures/zh-cn_image_0000002365942066.png" width="20">样式图标（General），在展开的General栏中修改组件的GaussianBlur属性以设置高斯模糊，如图1所示。

**图 1** 高斯模糊<a name="fig12812852164217"></a>
<img style="display:block;" src="figures/高斯模糊-86.png" width="339" alt="高斯模糊-86">

组件设置高斯模糊之后，会将层级低于该组件的其他组件模糊处理。如图2所示。

**图 2** 高斯模糊效果范例<a name="fig17715201710478"></a>
<img style="display:block;" src="figures/高斯模糊效果范例.png" width="700" alt="高斯模糊效果范例">

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - 只有同时满足FullScreenState为true且GaussianBlur不为0时，高斯模糊才会生效。
> - 因渲染方式不同，GUI界面中组件渲染效果会与模拟器中实际效果存在一定差异。
> - 多个组件均设置高斯模糊效果时，仅最下层组件的高斯模糊生效。
> - 组件层级可通过组件树查看，层级移动方式和详细说明参考“组件层级移动”。
> - GaussianBlur属性决定不同程度的高斯模糊效果，合理的范围是\[0, 32\]。
> - 事件添加：当前版本在控件的Events属性中使能事件不会生成事件代码，需用户手动添加事件代码，具体添加方法是在应用代码（以应用名为gui6为例，在SDK根目录/application/wearable/nativeapp/nativeui/gui6/include/ui_gui6View.h）的setupUi方法中，对指定控件添加所需事件，如需要给id名称为“button1”的控件添加OnLongPress事件，则在setupUi方法末尾增加“button1-\>SetOnLongPressListener\(gui6presenter\_\);”，其中“button1\_”为控件在代码中的变量名，“gui6presenter\_”为与应用名关联的在代码中自动生成的指针。

## 模拟器效果展示方法<a name="ZH-CN_TOPIC_0000002399739781"></a>

- **Demo运行**
- **调试运行**
- **经过GUI界面拖拽生成代码运行**
- **模拟器尺寸与形状设置**

### Demo运行<a name="ZH-CN_TOPIC_0000002366100002"></a>

单击图示中的“App Debug”，会启动编译调试并展示模拟器，运行默认Demo效果如图2所示。

运行过程中的日志信息记录在当前打开的工程根目录下的“simulator_build/error.txt”文件中。

**图 1** App Debug按钮<a name="fig599934320100"></a>
<img style="display:block;" src="figures/App-Debug按钮.png" width="700" alt="App-Debug按钮">

**图 2** 模拟器效果展示<a name="fig771416101317"></a>
<img style="display:block;" src="figures/模拟器效果展示.png" width="582" alt="模拟器效果展示">

### 调试运行<a name="ZH-CN_TOPIC_0000002399619913"></a>

单击“App Debug”按钮后，会自动启动编译和调试功能，用户可自行添加断点并进行调试。调试功能请参见“工程调试”章节。

**图 1** 调试功能展示<a name="fig28521758191013"></a>
<img style="display:block;" src="figures/调试功能展示.png" width="700" alt="调试功能展示">

### 经过GUI界面拖拽生成代码运行<a name="ZH-CN_TOPIC_0000002365940106"></a>

用户在画布中添加组件、更改属性或使能回调后，启动模拟器，即可按照图1操作看到画布中添加的功能列表。

**图 1** 从模拟器查看添加的组件功能<a name="fig18197143416124"></a>
<img style="display:block;" src="figures/从模拟器查看添加的组件功能.png" width="619" alt="从模拟器查看添加的组件功能">

> ![](public_sys-resources/icon-note.gif) **说明：**
> 当模拟器显示主界面时，单击右上角按钮，会自动跳到功能列表页面，列表最前面即为添加组件列表；当模拟器显示非主界面时，单击右上角按钮，会自动跳到主界面。

从图中可以看出，当前添加的功能名称默认为创建的GUI工程名称，图标默认为“示例”图标。如果想要修改模拟器中GUI工程的图标和名称，可以在对应GUI工程的生成代码目录下的“Register.cpp”文件中进行修改。

**图 2** 修改默认GUI工程名称和列表前的图标<a name="fig21411933131311"></a>
<img style="display:block;" src="figures/修改默认GUI工程名称和列表前的图标.png" width="700" alt="修改默认GUI工程名称和列表前的图标">

在对应的cpp文件中，修改这四个参数可以修改模拟器中对应组件的图标或者名称。

①：桌面中选择图标模式（默认模式）对应的图标显示，格式为.bin的文件。

②：桌面中选择蜂窝模式对应的图标显示，格式为.bin的文件。

③：桌面中对应足球模式对应的图标显示，格式为.bin的文件。

④：组件对应的名称。

对于默认选择的图标模式，只需要更改①和④中的参数，即可修改模拟器中组件对应的图标和组件名。

### 模拟器尺寸与形状设置<a name="ZH-CN_TOPIC_0000002399739785"></a>

用户创建GUI工程后，若需重新改变画布或模拟器的尺寸与形状，可以在工程中搜索“graphic_config.h”文件，该文件位于工程目录下的“application/brandy/simulator/libui”目录下，更改HORIZONTAL_RESOLUTION、VERTICAL_RESOLUTION以及DEVICE_SHAPE这三个参数，分别对应模拟器的直径（长宽）以及模拟器的形状。

**图 1** 更改模拟器的尺寸与形状<a name="fig5357185214137"></a>
<img style="display:block;" src="figures/更改模拟器的尺寸与形状.png" width="700" alt="更改模拟器的尺寸与形状">

## 图形工具介绍<a name="ZH-CN_TOPIC_0000002366100006"></a>

图形工具用到的脚本在tools/graphic_tools.tar.gz的压缩包中，需提前解压供后续使用。单击插件页面或者状态栏中的“Graphics Tools”图标。

**图 1** 插件页面或者状态栏中的“Graphics Tools”图标<a name="fig135900300384"></a>

<img style="display:block;" src="figures/zh-cn_image_0000002404301777.png" width="700">

弹出功能页签，当前包含“图片解压缩”和“视频首帧提取”两个功能。

**图 2** “GUI图形工具”页签<a name="fig5647114212381"></a>

<img style="display:block;" src="figures/zh-cn_image_0000002488087200.png" width="700">

- **环境配置**
- **图片解压缩工具**
- **视频首帧提取工具**
- **3D建模工具**
- **蒙版工具**

### 环境配置<a name="ZH-CN_TOPIC_0000002399619917"></a>

在使用“Graphics Tools”图形工具功能之前，需要配置Python环境，请参考“工具链配置”。

Python安装成功后需要安装pip的依赖模块。

- opencv模块
- numpy模块
- Pillow模块
- ffmpeg-python

Python环境可以通过在选择的工具链下载目录中tools目录下的python目录如“D:\\toolchain\\tools\\python”路径下打开cmd（命令提示符）窗口中进行验证。执行“.\\python.exe --version”输出结果为‘Python 3.11.4’，以及执行“python.exe ..\\..\\downloads\\pip.pyz list”命令输出结果显示有opencv-python、numpy以及pillow这些pip.pyz的依赖及其对应版本，则说明Python环境配置正确。

**图 1** Python环境验证<a name="fig17189163271318"></a>
<img style="display:block;" src="figures/python环境验证-87.png" width="617" alt="python环境验证-87">

### 图片解压缩工具<a name="ZH-CN_TOPIC_0000002365940110"></a>

图片解压缩工具的功能：依据xml文件配置的压缩算法以及像素格式信息，将指定目录下的每一个子目录都打包成一个资源文件并且生成资源索引文件“ImageResources.cpp”；或者将指定目录下的每一个图片文件都打包成一个资源文件。解压模式下会将.bin文件的图片解压为.png格式的图片；压缩模式下会将.png、.jpg或者.bmp文件格式的图片压缩为.bin文件格式。

**图 1** 图片解压缩界面<a name="fig2012249183513"></a>
<img style="display:block;" src="figures/图片解压缩界面.png" width="700" alt="图片解压缩界面">

- 脚本路径：需选择“images_convert.py”脚本所在的文件夹路径，一般为“graphic_tools\\image_converter_tool”。
- 解/压缩模式：指定解压、压缩模式，默认选择压缩模式。
- 打包方式：分为文件打包方式和文件夹打包方式，默认选择文件打包方式。
  - 文件打包方式：以每个图片为单位进行打包。
  - 文件夹打包方式：将图片进行打包后，再以子文件夹为单位将其包含的已打包图片一并打包。

- 压缩模式：默认为手动压缩模式。
- alpha压缩模式：0：非压缩；1：压缩。默认为1：压缩模式。
- rgb压缩模式：0：非压缩；1：压缩。默认为1：压缩模式。
- 压缩单元宽度：4--4x4；6--6x4；8--8x4；16--16x4，也叫压缩倍率，在ARGB8888格式时分别对应4倍压缩、6倍压缩、8倍压缩、16倍压缩；在RGB888时分别对应3倍压缩，4.5倍压缩，6倍压缩，12倍压缩；在RGB565时分别对应2倍压缩，3倍压缩，4倍压缩，8倍压缩。默认为6倍压缩。
- 图片输入路径：指定待处理图片的根目录，图片目录下的图片可以为“.jpg、.png、.bmp”等格式。
- 图片输出路径：指定输出的文件夹。

> ![](public_sys-resources/icon-notice.gif) **须知：**
>
> - 图片压缩仅支持.png、.bmp、.jpg文件的压缩，且图片分辨率大小不能超过1280\*800（宽\*高）。
> - 子文件夹名以及文件名必须为数字以及字母的组合。
> - 解/压缩模式选择为解压模式时，压缩模式、alpha压缩模式、rgb压缩模式和压缩单元宽度选项隐藏。
> - alpha和rgb同时为0是非压缩模式请注意适配。
> - 压缩倍率是与裸数据大小进行对比，而非与源文件大小对比，例如466×466的RGBA图片，无压缩大小为848KB，6倍压缩时为142KB，16倍压缩时大约为54KB。
> - 压缩操作为有损压缩，压缩倍率越大，图损越大。
> - 图片输出路径建议与图片输入路径保持一致，否则执行功能时会删除“图片输出路径”的文件夹，再自动创建一个同名文件夹保存输出的图片。

**压缩模式样例<a name="section19664105194515"></a>**

**图 2** 图片压缩具体选择样例<a name="fig611581334117"></a>
<img style="display:block;" src="figures/图片压缩具体选择样例.png" width="700" alt="图片压缩具体选择样例">

各选项均选择后，单击完成，执行压缩功能，终端界面输出显示内容如下：

**图 3** 图片压缩执行时终端界面输出<a name="fig753304214242"></a>
<img style="display:block;" src="figures/图片压缩执行时终端界面输出.png" width="321" alt="图片压缩执行时终端界面输出">

“Conversion Success!”说明压缩成功。图片所在文件夹前后对比如下，成功将两张png格式图片转换成bin文件格式：

**图 4** 图片压缩前后效果展示<a name="fig954913529412"></a>
<img style="display:block;" src="figures/图片压缩前后效果展示.png" width="402" alt="图片压缩前后效果展示">

<img style="display:block;" src="figures/zh-cn_image_0000002366102030.png" width="381">

**解压模式样例<a name="section15836552114418"></a>**

将解/压缩模式选择为解压模式，压缩模式、alpha压缩模式、rgb压缩模式和压缩单元宽度选项隐藏。

**图 5** 图片解压具体选择样例<a name="fig7235124264318"></a>
<img style="display:block;" src="figures/图片解压具体选择样例.png" width="700" alt="图片解压具体选择样例">

各选项均选择后，单击完成，执行解压功能，终端界面输出显示内容如下：

**图 6** 图片解压执行时终端界面输出<a name="fig188091156104319"></a>
<img style="display:block;" src="figures/图片解压执行时终端界面输出.png" width="333" alt="图片解压执行时终端界面输出">

“Decmpress Success”说明解压成功。图片所在文件夹前后对比如下，成功将两张bin格式图片解压为png文件格式：

**图 7** 图片解压前后对比<a name="fig5433744191910"></a>
<img style="display:block;" src="figures/图片解压前后对比.png" width="388" alt="图片解压前后对比">

<img style="display:block;" src="figures/zh-cn_image_0000002366102034.png" width="487">

### 视频首帧提取工具<a name="ZH-CN_TOPIC_0000002399739789"></a>

视频在未加载前，首帧为黑帧，需要用户手动设置一张起始预览图，该功能提供提取视频首帧并将其转换为BMP格式图片的能力。

**图 1** 视频首帧提取工具页面<a name="fig111561422134515"></a>
<img style="display:block;" src="figures/视频首帧提取工具页面.png" width="700" alt="视频首帧提取工具页面">

- 脚本路径：需选择“convert_2_bmp.py”脚本所在的文件夹路径，一般为“graphic_tools\\convert_2_bmp”。
- 视频路径：需要提取的视频文件路径。
- 视频帧宽/视频帧高：指定视频帧的宽高，需要与视频资源一致，且需要用户手动输入。
- 图片生成路径：图片生成路径。

> ![](public_sys-resources/icon-caution.gif) **注意：**
>
> - 视频格式当前仅支持YUV444和YUV420这两种。
> - 视频仅支持MJPEG编码及.mp4封装，调整视频格式及大小可借助ffmpeg工具， 例："ffmpeg -i video.mp4 -vf crop=454:454 -b:v 4228k -vcodec mjpeg out.mp4"。
> - 视频帧宽/高可以在视频的属性--\>详细信息中查看。如果视频帧宽高与实际不一致，生成的图片会产生花屏。

视频首帧提取样例：

**图 2** 视频首帧提取具体选项样例<a name="fig28171353184518"></a>
<img style="display:block;" src="figures/视频首帧提取具体选项样例.png" width="700" alt="视频首帧提取具体选项样例">

各选项均选择后，单击完成，执行视频首帧提取功能，终端界面输出显示内容如下：

**图 3** 视频首帧提取执行时终端界面输出<a name="fig1474664164615"></a>
<img style="display:block;" src="figures/视频首帧提取执行时终端界面输出.png" width="512" alt="视频首帧提取执行时终端界面输出">

“success”说明提取成功。视频所在文件夹前后对比如下，成功将mp4格式视频的首帧提取出来并保存为bmp格式的图片：

**图 4** 适配转换前后对比<a name="fig7243352114711"></a>
<img style="display:block;" src="figures/适配转换前后对比.png" width="358" alt="适配转换前后对比">

<img style="display:block;" src="figures/zh-cn_image_0000002399621957.png" width="448">

如果执行功能时终端中提示“未检测到 FFmpeg”，如图5所示。

**图 5** 未安装ffmepg提示信息<a name="fig1170385182419"></a>
<img style="display:block;" src="figures/未安装ffmepg提示信息.png" width="622" alt="未安装ffmepg提示信息">

需要手动下载安装[ffmepg工具](https://www.gyan.dev/ffmpeg/builds/)并添加至环境变量中，然后关闭所有的VS Code工具，再次打开执行视频首帧提取功能。

**图 6** ffmpeg下载<a name="fig184311426162816"></a>
<img style="display:block;" src="figures/ffmpeg下载.png" width="700" alt="ffmpeg下载">

配置环境变量：编辑系统环境变量-\>环境变量-\>Path-\>将解压后的绝对路径“\\ffmpeg-7.1.1-full_build-shared\\bin”添加到环境变量中。

### 3D建模工具<a name="ZH-CN_TOPIC_0000002366100010"></a>

- **使用方法**
- **参数表**

#### 使用方法<a name="ZH-CN_TOPIC_0000002399619921"></a>

**运行<a name="section1992610916599"></a>**

单击COMMANDS里面的Modeling Tools，在上方选择“3D Modeling Tool”。

<img style="display:block;" src="figures/zh-cn_image_0000002456945685.png" width="601">

**界面介绍<a name="section114256515596"></a>**

- **工具启动主界面**

  启动后工具主界面如图所示：

  **图 1** 3D建模工具启动主界面<a name="fig14212923556"></a>
  <img style="display:block;" src="figures/3D建模工具启动主界面.png" width="700" alt="3D建模工具启动主界面">

  按钮功能介绍如下：
  - 模型类型：选择当前要使用的模型（球面：sphere；网格：mesh；平面：cylinder），会自动加载默认参数并运行。
  - 纹理导入：选择纹理素材文件。
  - 模型导入：选择模型文件。
  - 模型创建：打开子界面，进行模型参数配置并生成模型。
  - 模型导出：将工具中对应模式下生成的模型文件导出到本地。
  - 运行：运行对应模式下的用例并显示运行效果。
  - 默认参数：一键恢复所有参数到其默认值。
  - 参数导出：根据当前界面配置的模式，调整参数，获得理想效果后，可将该模式下的该组参数保存到一个文件中。
  - 显示日志/隐藏日志：打开/关闭下方的日志框。

- **模型创建界面**

  ①mesh界面：在模型选择中选择网格后，单击模型创建，弹出如图所示界面：

  **图 2** mesh界面<a name="fig179479235556"></a>
  <img style="display:block;" src="figures/mesh界面.png" width="473" alt="mesh界面">

  ②cylinder界面：在模型选择中选择平面后，单击模型创建，弹出如图所示界面：

  **图 3** cylinder界面<a name="fig1460543113556"></a>
  <img style="display:block;" src="figures/cylinder界面.png" width="465" alt="cylinder界面">

  ③sphere界面：在模型选择中选择球面后，单击模型创建，弹出如图所示界面：

  **图 4** sphere界面<a name="fig18331542125514"></a>
  <img style="display:block;" src="figures/sphere界面.png" width="466" alt="sphere界面">

  单击保存按钮保存配置值，当单击完保存后，子窗体自动关闭。

**操作步骤<a name="section1371818221405"></a>**

- **mesh模式：**

  mesh分为7种子模式，其中type0和type6属于强交互模式，模型在线生成，无需离线生成和载入；type1～type5属于弱交互模式，运行用例之前需要离线生成模型或者载入模型，二者选一即可。
  1. 单击主界面网格单选按钮，选中网格模式。
  2. 单击主界面模型创建按钮，进行模型参数设置。
  3. 单击type输入框进行子模式选择，并进行相关参数配置：

     type0：thr建议配置为1.0，len建议配置为5，cx、cy建议配置在非中心点位置，其他参数建议保持默认值

     type1：len建议配置为0.0，cx、cy只支持配置在中心点，其他参数建议保持默认值

     type2：len建议配置为4.52，cx、cy只支持配置在中心点，其他参数建议保持默认值

     type3：len建议配置为1，cx、cy只支持配置在中心点，其他参数建议保持默认值

     type4：len建议配置为3，cx、cy只支持配置在中心点，其他参数建议保持默认值

     type5：len建议配置为9.33，cx、cy只支持配置在中心点，其他参数建议保持默认值

     type6：thr建议配置为0.1，其他参数建议保持默认值

  4. 单击保存按钮保存，并返回主界面。
  5. 单击主界面纹理导入按钮选择纹理素材。
  6. 单击运行按钮。
  7. 拖动右侧mesh_ctrl滑块，观察效果。

- **cylinder模式：**
  1. 单击主界面平面单选按钮，选中cylinder模式。
  2. 单击主界面模型创建按钮，进行模型参数设置，建议使用默认值。
  3. 单击保存按钮保存，并返回主界面。
  4. 单击纹理导入按钮选择纹理素材。
  5. 单击运行按钮。
  6. 拖动右侧cylinder_ctrl滑块（主要滑动的是cylinder_ctl），观察效果。

- **sphere模式：**
  1. 单击主界面球面单选按钮，选中sphere模式。
  2. 单击主界面模型创建按钮，进行模型参数设置，建议使用默认值。
  3. 单击保存按钮保存，并返回主界面。
  4. 单击纹理导入按钮选择纹理素材。
  5. 单击运行按钮。
  6. 拖动右侧angel_x、angel_y、angel_z三个滑块，观察效果。

**素材默认路径<a name="section88057444012"></a>**

> ![](public_sys-resources/icon-notice.gif) **须知：**
> 以下路径不能删除，否则会导致程序运行错误。

- 默认纹理素材路径：C:/Users/$\{用户名\}/.vscode/extensions/hispark.hisparkstudio-$\{版本号\}/dist/source_file/texture/
- 默认模型素材路径：C:/Users/$\{用户名\}/.vscode/extensions/hispark.hisparkstudio-$\{版本号\}/dist/source_file/model/，即模型创建完成之后的默认保存路径
- 默认蒙版素材路径：C:/Users/$\{用户名\}/.vscode/extensions/hispark.hisparkstudio-$\{版本号\}/dist/source_file/mask/，此路径仅供sphere模式使用，目的是使纹理与模型叠加时在连接处能够保持平滑过渡；生成的球蒙版宽高要和dst_width/dst_height一致，且球蒙版为ARGB8888。
- 其中$\{用户名\}为当前Windows登录账号用户名，$\{版本号\}为本插件版本号。

#### 参数表<a name="ZH-CN_TOPIC_0000002365940114"></a>

**滚筒日历<a name="section19555544673"></a>**

**表 1** 滚筒日历模型参数

<a name="table9440155420336"></a>

<table><thead align="left"><tr id="row2587354183315"><th class="cellrowborder" valign="top" width="12.98%" id="mcps1.2.5.1.1"><p id="p165871154173319"><a name="p165871154173319"></a><a name="p165871154173319"></a>序号</p>
</th>
<th class="cellrowborder" valign="top" width="24.2%" id="mcps1.2.5.1.2"><p id="p18587205433319"><a name="p18587205433319"></a><a name="p18587205433319"></a>参数名</p>
</th>
<th class="cellrowborder" valign="top" width="26.3%" id="mcps1.2.5.1.3"><p id="p558755412337"><a name="p558755412337"></a><a name="p558755412337"></a>参数含义</p>
</th>
<th class="cellrowborder" valign="top" width="36.52%" id="mcps1.2.5.1.4"><p id="p6587155473316"><a name="p6587155473316"></a><a name="p6587155473316"></a>范围&demo参数</p>
</th>
</tr>
</thead>
<tbody><tr id="row12587205417331"><td class="cellrowborder" valign="top" width="12.98%" headers="mcps1.2.5.1.1 "><p id="p135878543337"><a name="p135878543337"></a><a name="p135878543337"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="24.2%" headers="mcps1.2.5.1.2 "><p id="p15587654143310"><a name="p15587654143310"></a><a name="p15587654143310"></a>dst_width</p>
</td>
<td class="cellrowborder" valign="top" width="26.3%" headers="mcps1.2.5.1.3 "><p id="p4587145443312"><a name="p4587145443312"></a><a name="p4587145443312"></a>屏幕的宽</p>
</td>
<td class="cellrowborder" valign="top" width="36.52%" headers="mcps1.2.5.1.4 "><p id="p11587195473319"><a name="p11587195473319"></a><a name="p11587195473319"></a>-</p>
</td>
</tr>
<tr id="row1758785413339"><td class="cellrowborder" valign="top" width="12.98%" headers="mcps1.2.5.1.1 "><p id="p1558714540336"><a name="p1558714540336"></a><a name="p1558714540336"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="24.2%" headers="mcps1.2.5.1.2 "><p id="p2587185415330"><a name="p2587185415330"></a><a name="p2587185415330"></a>dst_height</p>
</td>
<td class="cellrowborder" valign="top" width="26.3%" headers="mcps1.2.5.1.3 "><p id="p18587125412333"><a name="p18587125412333"></a><a name="p18587125412333"></a>屏幕的高</p>
</td>
<td class="cellrowborder" valign="top" width="36.52%" headers="mcps1.2.5.1.4 "><p id="p55871054173311"><a name="p55871054173311"></a><a name="p55871054173311"></a>-</p>
</td>
</tr>
<tr id="row3587105412330"><td class="cellrowborder" valign="top" width="12.98%" headers="mcps1.2.5.1.1 "><p id="p1058712545336"><a name="p1058712545336"></a><a name="p1058712545336"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="24.2%" headers="mcps1.2.5.1.2 "><p id="p1587115423310"><a name="p1587115423310"></a><a name="p1587115423310"></a>cylinder_radius</p>
</td>
<td class="cellrowborder" valign="top" width="26.3%" headers="mcps1.2.5.1.3 "><p id="p758725417337"><a name="p758725417337"></a><a name="p758725417337"></a>圆柱体半径</p>
</td>
<td class="cellrowborder" valign="top" width="36.52%" headers="mcps1.2.5.1.4 "><p id="p1588195410337"><a name="p1588195410337"></a><a name="p1588195410337"></a>(0,cylinder_dst_width]; 230</p>
</td>
</tr>
<tr id="row1858865413338"><td class="cellrowborder" valign="top" width="12.98%" headers="mcps1.2.5.1.1 "><p id="p25882544336"><a name="p25882544336"></a><a name="p25882544336"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="24.2%" headers="mcps1.2.5.1.2 "><p id="p155881854133320"><a name="p155881854133320"></a><a name="p155881854133320"></a>cylinder_width</p>
</td>
<td class="cellrowborder" valign="top" width="26.3%" headers="mcps1.2.5.1.3 "><p id="p658815544331"><a name="p658815544331"></a><a name="p658815544331"></a>圆柱体宽</p>
</td>
<td class="cellrowborder" valign="top" width="36.52%" headers="mcps1.2.5.1.4 "><p id="p1588145410335"><a name="p1588145410335"></a><a name="p1588145410335"></a>(0,cylinder_dst_height]; 230</p>
</td>
</tr>
<tr id="row8588654143319"><td class="cellrowborder" valign="top" width="12.98%" headers="mcps1.2.5.1.1 "><p id="p16588754123314"><a name="p16588754123314"></a><a name="p16588754123314"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="24.2%" headers="mcps1.2.5.1.2 "><p id="p1958819542339"><a name="p1958819542339"></a><a name="p1958819542339"></a>cylinder_height</p>
</td>
<td class="cellrowborder" valign="top" width="26.3%" headers="mcps1.2.5.1.3 "><p id="p1458845493318"><a name="p1458845493318"></a><a name="p1458845493318"></a>圆柱体高</p>
</td>
<td class="cellrowborder" valign="top" width="36.52%" headers="mcps1.2.5.1.4 "><p id="p1558855403315"><a name="p1558855403315"></a><a name="p1558855403315"></a>(0,cylinder_dst_height]; 230</p>
</td>
</tr>
<tr id="row65881054173318"><td class="cellrowborder" valign="top" width="12.98%" headers="mcps1.2.5.1.1 "><p id="p458895415338"><a name="p458895415338"></a><a name="p458895415338"></a>6</p>
</td>
<td class="cellrowborder" valign="top" width="24.2%" headers="mcps1.2.5.1.2 "><p id="p1258865418336"><a name="p1258865418336"></a><a name="p1258865418336"></a>cylinder_x_step</p>
</td>
<td class="cellrowborder" valign="top" width="26.3%" headers="mcps1.2.5.1.3 "><p id="p105881954173311"><a name="p105881954173311"></a><a name="p105881954173311"></a>模型x方向采样步长</p>
</td>
<td class="cellrowborder" valign="top" width="36.52%" headers="mcps1.2.5.1.4 "><p id="p058818544336"><a name="p058818544336"></a><a name="p058818544336"></a>[4 ,8];4</p>
</td>
</tr>
<tr id="row8588135415332"><td class="cellrowborder" valign="top" width="12.98%" headers="mcps1.2.5.1.1 "><p id="p3588754193314"><a name="p3588754193314"></a><a name="p3588754193314"></a>7</p>
</td>
<td class="cellrowborder" valign="top" width="24.2%" headers="mcps1.2.5.1.2 "><p id="p158845483312"><a name="p158845483312"></a><a name="p158845483312"></a>cylinder_y_step</p>
</td>
<td class="cellrowborder" valign="top" width="26.3%" headers="mcps1.2.5.1.3 "><p id="p958814542335"><a name="p958814542335"></a><a name="p958814542335"></a>模型y方向采样步长</p>
</td>
<td class="cellrowborder" valign="top" width="36.52%" headers="mcps1.2.5.1.4 "><p id="p6588254103318"><a name="p6588254103318"></a><a name="p6588254103318"></a>[4 , 8];4</p>
</td>
</tr>
</tbody>
</table>

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - cylinder_x_step：逻辑约束cylinder_dst_width / cylinder_x_step
> - cylinder_y_step：逻辑约束cylinder_dst_height /cylinder_y_step
>   注意：对于cylinder模式的素材，建议宽为屏幕的1/2，高至少为2048。

**表 2** 滚筒日历demo参数

<a name="table13448145419338"></a>

<table><thead align="left"><tr id="row185881054183311"><th class="cellrowborder" valign="top" width="14.41%" id="mcps1.2.5.1.1"><p id="p35881654133318"><a name="p35881654133318"></a><a name="p35881654133318"></a>序号</p>
</th>
<th class="cellrowborder" valign="top" width="23.16%" id="mcps1.2.5.1.2"><p id="p18588115433315"><a name="p18588115433315"></a><a name="p18588115433315"></a>参数名</p>
</th>
<th class="cellrowborder" valign="top" width="26.040000000000003%" id="mcps1.2.5.1.3"><p id="p135881654163320"><a name="p135881654163320"></a><a name="p135881654163320"></a>参数含义</p>
</th>
<th class="cellrowborder" valign="top" width="36.39%" id="mcps1.2.5.1.4"><p id="p175881154133315"><a name="p175881154133315"></a><a name="p175881154133315"></a>范围&demo参数</p>
</th>
</tr>
</thead>
<tbody><tr id="row16588205417333"><td class="cellrowborder" valign="top" width="14.41%" headers="mcps1.2.5.1.1 "><p id="p1158825411336"><a name="p1158825411336"></a><a name="p1158825411336"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="23.16%" headers="mcps1.2.5.1.2 "><p id="p15588175415335"><a name="p15588175415335"></a><a name="p15588175415335"></a>angle</p>
</td>
<td class="cellrowborder" valign="top" width="26.040000000000003%" headers="mcps1.2.5.1.3 "><p id="p13588175415334"><a name="p13588175415334"></a><a name="p13588175415334"></a>旋转角度</p>
</td>
<td class="cellrowborder" valign="top" width="36.39%" headers="mcps1.2.5.1.4 "><p id="p1658865413318"><a name="p1658865413318"></a><a name="p1658865413318"></a>[-180,180]； 0</p>
</td>
</tr>
<tr id="row8588654173319"><td class="cellrowborder" valign="top" width="14.41%" headers="mcps1.2.5.1.1 "><p id="p3588105415334"><a name="p3588105415334"></a><a name="p3588105415334"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="23.16%" headers="mcps1.2.5.1.2 "><p id="p758811546331"><a name="p758811546331"></a><a name="p758811546331"></a>v_fov</p>
</td>
<td class="cellrowborder" valign="top" width="26.040000000000003%" headers="mcps1.2.5.1.3 "><p id="p115881554113315"><a name="p115881554113315"></a><a name="p115881554113315"></a>视口</p>
</td>
<td class="cellrowborder" valign="top" width="36.39%" headers="mcps1.2.5.1.4 "><p id="p10588454163311"><a name="p10588454163311"></a><a name="p10588454163311"></a>[1,200]； 102.674</p>
</td>
</tr>
<tr id="row15588125419334"><td class="cellrowborder" valign="top" width="14.41%" headers="mcps1.2.5.1.1 "><p id="p195891054143319"><a name="p195891054143319"></a><a name="p195891054143319"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="23.16%" headers="mcps1.2.5.1.2 "><p id="p758985453318"><a name="p758985453318"></a><a name="p758985453318"></a>aspect_ratio</p>
</td>
<td class="cellrowborder" valign="top" width="26.040000000000003%" headers="mcps1.2.5.1.3 "><p id="p1958925453315"><a name="p1958925453315"></a><a name="p1958925453315"></a>屏幕长宽比</p>
</td>
<td class="cellrowborder" valign="top" width="36.39%" headers="mcps1.2.5.1.4 "><p id="p1758915548334"><a name="p1758915548334"></a><a name="p1758915548334"></a>(0,2]； 0.46</p>
</td>
</tr>
<tr id="row12589854183313"><td class="cellrowborder" valign="top" width="14.41%" headers="mcps1.2.5.1.1 "><p id="p185890543339"><a name="p185890543339"></a><a name="p185890543339"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="23.16%" headers="mcps1.2.5.1.2 "><p id="p1058920549333"><a name="p1058920549333"></a><a name="p1058920549333"></a>z_near</p>
</td>
<td class="cellrowborder" valign="top" width="26.040000000000003%" headers="mcps1.2.5.1.3 "><p id="p16589195414334"><a name="p16589195414334"></a><a name="p16589195414334"></a>近平面</p>
</td>
<td class="cellrowborder" valign="top" width="36.39%" headers="mcps1.2.5.1.4 "><p id="p8589175433317"><a name="p8589175433317"></a><a name="p8589175433317"></a>[-400,400]； -10</p>
</td>
</tr>
<tr id="row75891854203313"><td class="cellrowborder" valign="top" width="14.41%" headers="mcps1.2.5.1.1 "><p id="p1758914549336"><a name="p1758914549336"></a><a name="p1758914549336"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="23.16%" headers="mcps1.2.5.1.2 "><p id="p10589155423314"><a name="p10589155423314"></a><a name="p10589155423314"></a>z_far</p>
</td>
<td class="cellrowborder" valign="top" width="26.040000000000003%" headers="mcps1.2.5.1.3 "><p id="p1858925411336"><a name="p1858925411336"></a><a name="p1858925411336"></a>远平面</p>
</td>
<td class="cellrowborder" valign="top" width="36.39%" headers="mcps1.2.5.1.4 "><p id="p16589754193318"><a name="p16589754193318"></a><a name="p16589754193318"></a>[-400,400]； -70</p>
</td>
</tr>
<tr id="row14589205453312"><td class="cellrowborder" valign="top" width="14.41%" headers="mcps1.2.5.1.1 "><p id="p75891054113312"><a name="p75891054113312"></a><a name="p75891054113312"></a>6</p>
</td>
<td class="cellrowborder" valign="top" width="23.16%" headers="mcps1.2.5.1.2 "><p id="p7589135403316"><a name="p7589135403316"></a><a name="p7589135403316"></a>axis_x</p>
</td>
<td class="cellrowborder" valign="top" width="26.040000000000003%" headers="mcps1.2.5.1.3 "><p id="p5589155423311"><a name="p5589155423311"></a><a name="p5589155423311"></a>三维空间的旋转轴x</p>
</td>
<td class="cellrowborder" valign="top" width="36.39%" headers="mcps1.2.5.1.4 "><p id="p115891754113319"><a name="p115891754113319"></a><a name="p115891754113319"></a>[-1,1]； 1</p>
</td>
</tr>
<tr id="row2589135433312"><td class="cellrowborder" valign="top" width="14.41%" headers="mcps1.2.5.1.1 "><p id="p35895542331"><a name="p35895542331"></a><a name="p35895542331"></a>7</p>
</td>
<td class="cellrowborder" valign="top" width="23.16%" headers="mcps1.2.5.1.2 "><p id="p1058985414334"><a name="p1058985414334"></a><a name="p1058985414334"></a>axis_y</p>
</td>
<td class="cellrowborder" valign="top" width="26.040000000000003%" headers="mcps1.2.5.1.3 "><p id="p4589175418339"><a name="p4589175418339"></a><a name="p4589175418339"></a>三维空间的旋转轴y</p>
</td>
<td class="cellrowborder" valign="top" width="36.39%" headers="mcps1.2.5.1.4 "><p id="p19589854203319"><a name="p19589854203319"></a><a name="p19589854203319"></a>[-1,1]； 0</p>
</td>
</tr>
<tr id="row1158985493315"><td class="cellrowborder" valign="top" width="14.41%" headers="mcps1.2.5.1.1 "><p id="p11589115493317"><a name="p11589115493317"></a><a name="p11589115493317"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="23.16%" headers="mcps1.2.5.1.2 "><p id="p1458917549335"><a name="p1458917549335"></a><a name="p1458917549335"></a>axis_z</p>
</td>
<td class="cellrowborder" valign="top" width="26.040000000000003%" headers="mcps1.2.5.1.3 "><p id="p13589125413331"><a name="p13589125413331"></a><a name="p13589125413331"></a>三维空间的旋转轴z</p>
</td>
<td class="cellrowborder" valign="top" width="36.39%" headers="mcps1.2.5.1.4 "><p id="p658910548333"><a name="p658910548333"></a><a name="p658910548333"></a>[-1,1]； 0</p>
</td>
</tr>
<tr id="row165892544337"><td class="cellrowborder" valign="top" width="14.41%" headers="mcps1.2.5.1.1 "><p id="p1458985414333"><a name="p1458985414333"></a><a name="p1458985414333"></a>9</p>
</td>
<td class="cellrowborder" valign="top" width="23.16%" headers="mcps1.2.5.1.2 "><p id="p125892545332"><a name="p125892545332"></a><a name="p125892545332"></a>scale_x</p>
</td>
<td class="cellrowborder" valign="top" width="26.040000000000003%" headers="mcps1.2.5.1.3 "><p id="p18589155411334"><a name="p18589155411334"></a><a name="p18589155411334"></a>沿x轴缩放系数</p>
</td>
<td class="cellrowborder" valign="top" width="36.39%" headers="mcps1.2.5.1.4 "><p id="p155891754193314"><a name="p155891754193314"></a><a name="p155891754193314"></a>(0,10]；1</p>
</td>
</tr>
<tr id="row1358917549338"><td class="cellrowborder" valign="top" width="14.41%" headers="mcps1.2.5.1.1 "><p id="p13589125493313"><a name="p13589125493313"></a><a name="p13589125493313"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="23.16%" headers="mcps1.2.5.1.2 "><p id="p1558913549335"><a name="p1558913549335"></a><a name="p1558913549335"></a>scale_y</p>
</td>
<td class="cellrowborder" valign="top" width="26.040000000000003%" headers="mcps1.2.5.1.3 "><p id="p8589654153310"><a name="p8589654153310"></a><a name="p8589654153310"></a>沿y轴缩放系数</p>
</td>
<td class="cellrowborder" valign="top" width="36.39%" headers="mcps1.2.5.1.4 "><p id="p958965423314"><a name="p958965423314"></a><a name="p958965423314"></a>(0,10]；1</p>
</td>
</tr>
<tr id="row558995412336"><td class="cellrowborder" valign="top" width="14.41%" headers="mcps1.2.5.1.1 "><p id="p8589105423315"><a name="p8589105423315"></a><a name="p8589105423315"></a>11</p>
</td>
<td class="cellrowborder" valign="top" width="23.16%" headers="mcps1.2.5.1.2 "><p id="p1758925412330"><a name="p1758925412330"></a><a name="p1758925412330"></a>scale_z</p>
</td>
<td class="cellrowborder" valign="top" width="26.040000000000003%" headers="mcps1.2.5.1.3 "><p id="p155901654143315"><a name="p155901654143315"></a><a name="p155901654143315"></a>沿z轴缩放系数</p>
</td>
<td class="cellrowborder" valign="top" width="36.39%" headers="mcps1.2.5.1.4 "><p id="p19590145463313"><a name="p19590145463313"></a><a name="p19590145463313"></a>(0,10]；1</p>
</td>
</tr>
<tr id="row0590054193316"><td class="cellrowborder" valign="top" width="14.41%" headers="mcps1.2.5.1.1 "><p id="p85901854113310"><a name="p85901854113310"></a><a name="p85901854113310"></a>12</p>
</td>
<td class="cellrowborder" valign="top" width="23.16%" headers="mcps1.2.5.1.2 "><p id="p175901542333"><a name="p175901542333"></a><a name="p175901542333"></a>translation_x</p>
</td>
<td class="cellrowborder" valign="top" width="26.040000000000003%" headers="mcps1.2.5.1.3 "><p id="p9590454133312"><a name="p9590454133312"></a><a name="p9590454133312"></a>沿x轴平移系数</p>
</td>
<td class="cellrowborder" valign="top" width="36.39%" headers="mcps1.2.5.1.4 "><p id="p459035415339"><a name="p459035415339"></a><a name="p459035415339"></a>[-400, 400]; 0</p>
</td>
</tr>
<tr id="row19590115412339"><td class="cellrowborder" valign="top" width="14.41%" headers="mcps1.2.5.1.1 "><p id="p1559016549337"><a name="p1559016549337"></a><a name="p1559016549337"></a>13</p>
</td>
<td class="cellrowborder" valign="top" width="23.16%" headers="mcps1.2.5.1.2 "><p id="p2590135473316"><a name="p2590135473316"></a><a name="p2590135473316"></a>translation_y</p>
</td>
<td class="cellrowborder" valign="top" width="26.040000000000003%" headers="mcps1.2.5.1.3 "><p id="p12590155418336"><a name="p12590155418336"></a><a name="p12590155418336"></a>沿y轴平移系数</p>
</td>
<td class="cellrowborder" valign="top" width="36.39%" headers="mcps1.2.5.1.4 "><p id="p1159085413333"><a name="p1159085413333"></a><a name="p1159085413333"></a>[-400, 400]; 0</p>
</td>
</tr>
<tr id="row0590135493314"><td class="cellrowborder" valign="top" width="14.41%" headers="mcps1.2.5.1.1 "><p id="p1759005417330"><a name="p1759005417330"></a><a name="p1759005417330"></a>14</p>
</td>
<td class="cellrowborder" valign="top" width="23.16%" headers="mcps1.2.5.1.2 "><p id="p1059095483312"><a name="p1059095483312"></a><a name="p1059095483312"></a>translation_z</p>
</td>
<td class="cellrowborder" valign="top" width="26.040000000000003%" headers="mcps1.2.5.1.3 "><p id="p17590854103310"><a name="p17590854103310"></a><a name="p17590854103310"></a>沿z轴平移系数</p>
</td>
<td class="cellrowborder" valign="top" width="36.39%" headers="mcps1.2.5.1.4 "><p id="p35901954173320"><a name="p35901954173320"></a><a name="p35901954173320"></a>[-400, 400]; 0</p>
</td>
</tr>
<tr id="row20590185463311"><td class="cellrowborder" valign="top" width="14.41%" headers="mcps1.2.5.1.1 "><p id="p6590115416332"><a name="p6590115416332"></a><a name="p6590115416332"></a>15</p>
</td>
<td class="cellrowborder" valign="top" width="23.16%" headers="mcps1.2.5.1.2 "><p id="p959020544338"><a name="p959020544338"></a><a name="p959020544338"></a>look_from_x</p>
</td>
<td class="cellrowborder" valign="top" width="26.040000000000003%" headers="mcps1.2.5.1.3 "><p id="p459095418332"><a name="p459095418332"></a><a name="p459095418332"></a>camera位置x轴的坐标</p>
</td>
<td class="cellrowborder" valign="top" width="36.39%" headers="mcps1.2.5.1.4 "><p id="p8590145416339"><a name="p8590145416339"></a><a name="p8590145416339"></a>[-400, 400]; 0</p>
</td>
</tr>
<tr id="row12590115473311"><td class="cellrowborder" valign="top" width="14.41%" headers="mcps1.2.5.1.1 "><p id="p7590205413334"><a name="p7590205413334"></a><a name="p7590205413334"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="23.16%" headers="mcps1.2.5.1.2 "><p id="p1359045443317"><a name="p1359045443317"></a><a name="p1359045443317"></a>look_from_y</p>
</td>
<td class="cellrowborder" valign="top" width="26.040000000000003%" headers="mcps1.2.5.1.3 "><p id="p11590554133312"><a name="p11590554133312"></a><a name="p11590554133312"></a>camera位置y轴的坐标</p>
</td>
<td class="cellrowborder" valign="top" width="36.39%" headers="mcps1.2.5.1.4 "><p id="p15590125463312"><a name="p15590125463312"></a><a name="p15590125463312"></a>[-400, 400]; 0</p>
</td>
</tr>
<tr id="row115901954113311"><td class="cellrowborder" valign="top" width="14.41%" headers="mcps1.2.5.1.1 "><p id="p959055414331"><a name="p959055414331"></a><a name="p959055414331"></a>17</p>
</td>
<td class="cellrowborder" valign="top" width="23.16%" headers="mcps1.2.5.1.2 "><p id="p10590454163312"><a name="p10590454163312"></a><a name="p10590454163312"></a>look_from_z</p>
</td>
<td class="cellrowborder" valign="top" width="26.040000000000003%" headers="mcps1.2.5.1.3 "><p id="p1159016541335"><a name="p1159016541335"></a><a name="p1159016541335"></a>camera位置z轴坐标</p>
</td>
<td class="cellrowborder" valign="top" width="36.39%" headers="mcps1.2.5.1.4 "><p id="p185903542332"><a name="p185903542332"></a><a name="p185903542332"></a>[-400, 400]; 0</p>
</td>
</tr>
</tbody>
</table>

**月相星球表盘<a name="section1102111018816"></a>**

**表 3** 月相星球表盘模型参数

<a name="table20462115423315"></a>

<table><thead align="left"><tr id="row115901354193313"><th class="cellrowborder" valign="top" width="14.149999999999999%" id="mcps1.2.5.1.1"><p id="p145901544335"><a name="p145901544335"></a><a name="p145901544335"></a>序号</p>
</th>
<th class="cellrowborder" valign="top" width="22.64%" id="mcps1.2.5.1.2"><p id="p1759045415333"><a name="p1759045415333"></a><a name="p1759045415333"></a>参数名</p>
</th>
<th class="cellrowborder" valign="top" width="26.56%" id="mcps1.2.5.1.3"><p id="p195901354133313"><a name="p195901354133313"></a><a name="p195901354133313"></a>参数含义</p>
</th>
<th class="cellrowborder" valign="top" width="36.65%" id="mcps1.2.5.1.4"><p id="p5590185473317"><a name="p5590185473317"></a><a name="p5590185473317"></a>范围& demo参数</p>
</th>
</tr>
</thead>
<tbody><tr id="row559015413316"><td class="cellrowborder" valign="top" width="14.149999999999999%" headers="mcps1.2.5.1.1 "><p id="p135901354143316"><a name="p135901354143316"></a><a name="p135901354143316"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="22.64%" headers="mcps1.2.5.1.2 "><p id="p1590135415333"><a name="p1590135415333"></a><a name="p1590135415333"></a>dst_width</p>
</td>
<td class="cellrowborder" valign="top" width="26.56%" headers="mcps1.2.5.1.3 "><p id="p7591185418339"><a name="p7591185418339"></a><a name="p7591185418339"></a>屏幕的宽</p>
</td>
<td class="cellrowborder" valign="top" width="36.65%" headers="mcps1.2.5.1.4 "><p id="p2059135473315"><a name="p2059135473315"></a><a name="p2059135473315"></a>-</p>
</td>
</tr>
<tr id="row1759114541331"><td class="cellrowborder" valign="top" width="14.149999999999999%" headers="mcps1.2.5.1.1 "><p id="p45911054103312"><a name="p45911054103312"></a><a name="p45911054103312"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="22.64%" headers="mcps1.2.5.1.2 "><p id="p105916548338"><a name="p105916548338"></a><a name="p105916548338"></a>dst_height</p>
</td>
<td class="cellrowborder" valign="top" width="26.56%" headers="mcps1.2.5.1.3 "><p id="p2591254113316"><a name="p2591254113316"></a><a name="p2591254113316"></a>屏幕的高</p>
</td>
<td class="cellrowborder" valign="top" width="36.65%" headers="mcps1.2.5.1.4 "><p id="p8591175420334"><a name="p8591175420334"></a><a name="p8591175420334"></a>-</p>
</td>
</tr>
<tr id="row759115413320"><td class="cellrowborder" valign="top" width="14.149999999999999%" headers="mcps1.2.5.1.1 "><p id="p5591205420334"><a name="p5591205420334"></a><a name="p5591205420334"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="22.64%" headers="mcps1.2.5.1.2 "><p id="p18591175415335"><a name="p18591175415335"></a><a name="p18591175415335"></a>sphere_radius</p>
</td>
<td class="cellrowborder" valign="top" width="26.56%" headers="mcps1.2.5.1.3 "><p id="p125914547331"><a name="p125914547331"></a><a name="p125914547331"></a>球半径</p>
</td>
<td class="cellrowborder" valign="top" width="36.65%" headers="mcps1.2.5.1.4 "><p id="p1259118541334"><a name="p1259118541334"></a><a name="p1259118541334"></a>(0, +∞) ；150</p>
</td>
</tr>
<tr id="row1591254163317"><td class="cellrowborder" valign="top" width="14.149999999999999%" headers="mcps1.2.5.1.1 "><p id="p2059185413332"><a name="p2059185413332"></a><a name="p2059185413332"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="22.64%" headers="mcps1.2.5.1.2 "><p id="p1159155493310"><a name="p1159155493310"></a><a name="p1159155493310"></a>sphere_cx</p>
</td>
<td class="cellrowborder" valign="top" width="26.56%" headers="mcps1.2.5.1.3 "><p id="p15591205483317"><a name="p15591205483317"></a><a name="p15591205483317"></a>球心x坐标</p>
</td>
<td class="cellrowborder" valign="top" width="36.65%" headers="mcps1.2.5.1.4 "><p id="p105911754133319"><a name="p105911754133319"></a><a name="p105911754133319"></a>(0, +∞) ；dst_surface中心</p>
</td>
</tr>
<tr id="row155914542335"><td class="cellrowborder" valign="top" width="14.149999999999999%" headers="mcps1.2.5.1.1 "><p id="p1359115413338"><a name="p1359115413338"></a><a name="p1359115413338"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="22.64%" headers="mcps1.2.5.1.2 "><p id="p959105453310"><a name="p959105453310"></a><a name="p959105453310"></a>sphere_cy</p>
</td>
<td class="cellrowborder" valign="top" width="26.56%" headers="mcps1.2.5.1.3 "><p id="p85911754123316"><a name="p85911754123316"></a><a name="p85911754123316"></a>球心y坐标</p>
</td>
<td class="cellrowborder" valign="top" width="36.65%" headers="mcps1.2.5.1.4 "><p id="p1591185443315"><a name="p1591185443315"></a><a name="p1591185443315"></a>(0, +∞) ；dst_surface中心</p>
</td>
</tr>
<tr id="row1259113549337"><td class="cellrowborder" valign="top" width="14.149999999999999%" headers="mcps1.2.5.1.1 "><p id="p195914548331"><a name="p195914548331"></a><a name="p195914548331"></a>6</p>
</td>
<td class="cellrowborder" valign="top" width="22.64%" headers="mcps1.2.5.1.2 "><p id="p1459120548337"><a name="p1459120548337"></a><a name="p1459120548337"></a>sphere_step_x</p>
</td>
<td class="cellrowborder" valign="top" width="26.56%" headers="mcps1.2.5.1.3 "><p id="p8591115416339"><a name="p8591115416339"></a><a name="p8591115416339"></a>模型x方向采样步长</p>
</td>
<td class="cellrowborder" valign="top" width="36.65%" headers="mcps1.2.5.1.4 "><p id="p1591175411337"><a name="p1591175411337"></a><a name="p1591175411337"></a>[4, 8];4；</p>
</td>
</tr>
<tr id="row19591354173315"><td class="cellrowborder" valign="top" width="14.149999999999999%" headers="mcps1.2.5.1.1 "><p id="p1591195410337"><a name="p1591195410337"></a><a name="p1591195410337"></a>7</p>
</td>
<td class="cellrowborder" valign="top" width="22.64%" headers="mcps1.2.5.1.2 "><p id="p7591054193314"><a name="p7591054193314"></a><a name="p7591054193314"></a>sphere_step_y</p>
</td>
<td class="cellrowborder" valign="top" width="26.56%" headers="mcps1.2.5.1.3 "><p id="p1659116547335"><a name="p1659116547335"></a><a name="p1659116547335"></a>模型y方向采样步长</p>
</td>
<td class="cellrowborder" valign="top" width="36.65%" headers="mcps1.2.5.1.4 "><p id="p4591175423311"><a name="p4591175423311"></a><a name="p4591175423311"></a>[4, 8];4；</p>
</td>
</tr>
</tbody>
</table>

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - sphere_step_x：逻辑约束dst_height / sphere_step_x< 128
> - sphere_step_y：逻辑约束dst_width / sphere_step_y < 128

**表 4** 月相星球表盘demo参数

<a name="table4468175418337"></a>

<table><thead align="left"><tr id="row4591454193316"><th class="cellrowborder" valign="top" width="14.799999999999999%" id="mcps1.2.5.1.1"><p id="p19591115473310"><a name="p19591115473310"></a><a name="p19591115473310"></a>序号</p>
</th>
<th class="cellrowborder" valign="top" width="24.34%" id="mcps1.2.5.1.2"><p id="p4591105413316"><a name="p4591105413316"></a><a name="p4591105413316"></a>参数名</p>
</th>
<th class="cellrowborder" valign="top" width="26.169999999999998%" id="mcps1.2.5.1.3"><p id="p9591115433319"><a name="p9591115433319"></a><a name="p9591115433319"></a>参数含义</p>
</th>
<th class="cellrowborder" valign="top" width="34.69%" id="mcps1.2.5.1.4"><p id="p259111541331"><a name="p259111541331"></a><a name="p259111541331"></a>范围&demo值</p>
</th>
</tr>
</thead>
<tbody><tr id="row11591554153319"><td class="cellrowborder" valign="top" width="14.799999999999999%" headers="mcps1.2.5.1.1 "><p id="p1959113544330"><a name="p1959113544330"></a><a name="p1959113544330"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="24.34%" headers="mcps1.2.5.1.2 "><p id="p175924548336"><a name="p175924548336"></a><a name="p175924548336"></a>sphere_angle_x</p>
</td>
<td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p8592175433314"><a name="p8592175433314"></a><a name="p8592175433314"></a>沿x旋转角度</p>
</td>
<td class="cellrowborder" valign="top" width="34.69%" headers="mcps1.2.5.1.4 "><p id="p4592145423319"><a name="p4592145423319"></a><a name="p4592145423319"></a>[0,360];0</p>
</td>
</tr>
<tr id="row15592854163311"><td class="cellrowborder" valign="top" width="14.799999999999999%" headers="mcps1.2.5.1.1 "><p id="p3592165418335"><a name="p3592165418335"></a><a name="p3592165418335"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="24.34%" headers="mcps1.2.5.1.2 "><p id="p14592185473314"><a name="p14592185473314"></a><a name="p14592185473314"></a>sphere_angle_y</p>
</td>
<td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p659265433312"><a name="p659265433312"></a><a name="p659265433312"></a>沿y轴旋转角度</p>
</td>
<td class="cellrowborder" valign="top" width="34.69%" headers="mcps1.2.5.1.4 "><p id="p1959214546339"><a name="p1959214546339"></a><a name="p1959214546339"></a>[0,360];0</p>
</td>
</tr>
<tr id="row1659245411332"><td class="cellrowborder" valign="top" width="14.799999999999999%" headers="mcps1.2.5.1.1 "><p id="p205921454103319"><a name="p205921454103319"></a><a name="p205921454103319"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="24.34%" headers="mcps1.2.5.1.2 "><p id="p1959210549334"><a name="p1959210549334"></a><a name="p1959210549334"></a>sphere_angle_z</p>
</td>
<td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p759235493317"><a name="p759235493317"></a><a name="p759235493317"></a>沿z轴旋转角度</p>
</td>
<td class="cellrowborder" valign="top" width="34.69%" headers="mcps1.2.5.1.4 "><p id="p115923542337"><a name="p115923542337"></a><a name="p115923542337"></a>[0,360];0</p>
</td>
</tr>
</tbody>
</table>

**MESH表盘互动<a name="section178548341816"></a>**

**表 5** MESH表盘互动模型参数

<a name="table14471185473311"></a>

<table><thead align="left"><tr id="row105922547330"><th class="cellrowborder" valign="top" width="15.45%" id="mcps1.2.5.1.1"><p id="p14592125413316"><a name="p14592125413316"></a><a name="p14592125413316"></a>序号</p>
</th>
<th class="cellrowborder" valign="top" width="24.6%" id="mcps1.2.5.1.2"><p id="p65921549331"><a name="p65921549331"></a><a name="p65921549331"></a>参数名</p>
</th>
<th class="cellrowborder" valign="top" width="25.650000000000002%" id="mcps1.2.5.1.3"><p id="p13592155453318"><a name="p13592155453318"></a><a name="p13592155453318"></a>参数含义</p>
</th>
<th class="cellrowborder" valign="top" width="34.300000000000004%" id="mcps1.2.5.1.4"><p id="p4592105473314"><a name="p4592105473314"></a><a name="p4592105473314"></a>范围&demo值</p>
</th>
</tr>
</thead>
<tbody><tr id="row1459285463317"><td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.1 "><p id="p659255410338"><a name="p659255410338"></a><a name="p659255410338"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="24.6%" headers="mcps1.2.5.1.2 "><p id="p8592054113314"><a name="p8592054113314"></a><a name="p8592054113314"></a>src_width</p>
</td>
<td class="cellrowborder" valign="top" width="25.650000000000002%" headers="mcps1.2.5.1.3 "><p id="p17592254163317"><a name="p17592254163317"></a><a name="p17592254163317"></a>素材的宽</p>
</td>
<td class="cellrowborder" valign="top" width="34.300000000000004%" headers="mcps1.2.5.1.4 "><p id="p19592175493313"><a name="p19592175493313"></a><a name="p19592175493313"></a>建议与屏幕的宽保持一致</p>
</td>
</tr>
<tr id="row95923541336"><td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.1 "><p id="p155921454133314"><a name="p155921454133314"></a><a name="p155921454133314"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="24.6%" headers="mcps1.2.5.1.2 "><p id="p959215443320"><a name="p959215443320"></a><a name="p959215443320"></a>src_height</p>
</td>
<td class="cellrowborder" valign="top" width="25.650000000000002%" headers="mcps1.2.5.1.3 "><p id="p85921545334"><a name="p85921545334"></a><a name="p85921545334"></a>素材的高</p>
</td>
<td class="cellrowborder" valign="top" width="34.300000000000004%" headers="mcps1.2.5.1.4 "><p id="p259285413311"><a name="p259285413311"></a><a name="p259285413311"></a>建议与屏幕的高保持一致</p>
</td>
</tr>
<tr id="row16592115411335"><td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.1 "><p id="p45929540334"><a name="p45929540334"></a><a name="p45929540334"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="24.6%" headers="mcps1.2.5.1.2 "><p id="p1459225413331"><a name="p1459225413331"></a><a name="p1459225413331"></a>dst_width</p>
</td>
<td class="cellrowborder" valign="top" width="25.650000000000002%" headers="mcps1.2.5.1.3 "><p id="p3592145418335"><a name="p3592145418335"></a><a name="p3592145418335"></a>屏幕的宽</p>
</td>
<td class="cellrowborder" valign="top" width="34.300000000000004%" headers="mcps1.2.5.1.4 "><p id="p1259255463313"><a name="p1259255463313"></a><a name="p1259255463313"></a>-</p>
</td>
</tr>
<tr id="row6593954203313"><td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.1 "><p id="p75931254143316"><a name="p75931254143316"></a><a name="p75931254143316"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="24.6%" headers="mcps1.2.5.1.2 "><p id="p16593154113316"><a name="p16593154113316"></a><a name="p16593154113316"></a>dst_height</p>
</td>
<td class="cellrowborder" valign="top" width="25.650000000000002%" headers="mcps1.2.5.1.3 "><p id="p45931542336"><a name="p45931542336"></a><a name="p45931542336"></a>屏幕的高</p>
</td>
<td class="cellrowborder" valign="top" width="34.300000000000004%" headers="mcps1.2.5.1.4 "><p id="p17593145423318"><a name="p17593145423318"></a><a name="p17593145423318"></a>-</p>
</td>
</tr>
<tr id="row159355410334"><td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.1 "><p id="p6593115413315"><a name="p6593115413315"></a><a name="p6593115413315"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="24.6%" headers="mcps1.2.5.1.2 "><p id="p1959395416337"><a name="p1959395416337"></a><a name="p1959395416337"></a>mesh_x_block_num</p>
</td>
<td class="cellrowborder" valign="top" width="25.650000000000002%" headers="mcps1.2.5.1.3 "><p id="p195931054123319"><a name="p195931054123319"></a><a name="p195931054123319"></a>水平方向划分块数量</p>
</td>
<td class="cellrowborder" valign="top" width="34.300000000000004%" headers="mcps1.2.5.1.4 "><p id="p20593105414335"><a name="p20593105414335"></a><a name="p20593105414335"></a>(0,32];32</p>
</td>
</tr>
<tr id="row19593115453312"><td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.1 "><p id="p95931454123317"><a name="p95931454123317"></a><a name="p95931454123317"></a>6</p>
</td>
<td class="cellrowborder" valign="top" width="24.6%" headers="mcps1.2.5.1.2 "><p id="p185931954153319"><a name="p185931954153319"></a><a name="p185931954153319"></a>mesh_y_block_num</p>
</td>
<td class="cellrowborder" valign="top" width="25.650000000000002%" headers="mcps1.2.5.1.3 "><p id="p13593185418335"><a name="p13593185418335"></a><a name="p13593185418335"></a>垂直方向划分块数量</p>
</td>
<td class="cellrowborder" valign="top" width="34.300000000000004%" headers="mcps1.2.5.1.4 "><p id="p45931545332"><a name="p45931545332"></a><a name="p45931545332"></a>(0,32];32</p>
</td>
</tr>
<tr id="row1259314540335"><td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.1 "><p id="p195931154143312"><a name="p195931154143312"></a><a name="p195931154143312"></a>7</p>
</td>
<td class="cellrowborder" valign="top" width="24.6%" headers="mcps1.2.5.1.2 "><p id="p1359345419339"><a name="p1359345419339"></a><a name="p1359345419339"></a>mesh_cx</p>
</td>
<td class="cellrowborder" valign="top" width="25.650000000000002%" headers="mcps1.2.5.1.3 "><p id="p559315413337"><a name="p559315413337"></a><a name="p559315413337"></a>形变中心点x坐标</p>
</td>
<td class="cellrowborder" valign="top" width="34.300000000000004%" headers="mcps1.2.5.1.4 "><p id="p3207730201312"><a name="p3207730201312"></a><a name="p3207730201312"></a>弱互动：mesh_dst_width / 2</p>
<p id="p115931454113310"><a name="p115931454113310"></a><a name="p115931454113310"></a>强互动建议在[0,mesh_dst_width)</p>
</td>
</tr>
<tr id="row1259335414335"><td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.1 "><p id="p15593554133315"><a name="p15593554133315"></a><a name="p15593554133315"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="24.6%" headers="mcps1.2.5.1.2 "><p id="p359395418333"><a name="p359395418333"></a><a name="p359395418333"></a>mesh_cy</p>
</td>
<td class="cellrowborder" valign="top" width="25.650000000000002%" headers="mcps1.2.5.1.3 "><p id="p1593754173320"><a name="p1593754173320"></a><a name="p1593754173320"></a>形变中心点y坐标</p>
</td>
<td class="cellrowborder" valign="top" width="34.300000000000004%" headers="mcps1.2.5.1.4 "><p id="p986613280132"><a name="p986613280132"></a><a name="p986613280132"></a>弱互动：mesh_dst_height / 2</p>
<p id="p125931854203313"><a name="p125931854203313"></a><a name="p125931854203313"></a>强互动建议在[0,mesh_dst_height)</p>
</td>
</tr>
<tr id="row15593454133310"><td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.1 "><p id="p175931954143320"><a name="p175931954143320"></a><a name="p175931954143320"></a>9</p>
</td>
<td class="cellrowborder" valign="top" width="24.6%" headers="mcps1.2.5.1.2 "><p id="p3593115416333"><a name="p3593115416333"></a><a name="p3593115416333"></a>mesh_len</p>
</td>
<td class="cellrowborder" valign="top" width="25.650000000000002%" headers="mcps1.2.5.1.3 "><p id="p1759316549330"><a name="p1759316549330"></a><a name="p1759316549330"></a>形变程度</p>
</td>
<td class="cellrowborder" valign="top" width="34.300000000000004%" headers="mcps1.2.5.1.4 "><p id="p759365443318"><a name="p759365443318"></a><a name="p759365443318"></a>[0,10]；</p>
</td>
</tr>
<tr id="row359315547335"><td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.1 "><p id="p13593254183312"><a name="p13593254183312"></a><a name="p13593254183312"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="24.6%" headers="mcps1.2.5.1.2 "><p id="p559325417331"><a name="p559325417331"></a><a name="p559325417331"></a>mesh_thr</p>
</td>
<td class="cellrowborder" valign="top" width="25.650000000000002%" headers="mcps1.2.5.1.3 "><p id="p15593155463319"><a name="p15593155463319"></a><a name="p15593155463319"></a>形变阈值</p>
</td>
<td class="cellrowborder" valign="top" width="34.300000000000004%" headers="mcps1.2.5.1.4 "><p id="p75937548334"><a name="p75937548334"></a><a name="p75937548334"></a>[0,10]；</p>
</td>
</tr>
<tr id="row12593175413336"><td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.1 "><p id="p2593125453317"><a name="p2593125453317"></a><a name="p2593125453317"></a>11</p>
</td>
<td class="cellrowborder" valign="top" width="24.6%" headers="mcps1.2.5.1.2 "><p id="p959413544336"><a name="p959413544336"></a><a name="p959413544336"></a>mesh_type</p>
</td>
<td class="cellrowborder" valign="top" width="25.650000000000002%" headers="mcps1.2.5.1.3 "><p id="p85942054163319"><a name="p85942054163319"></a><a name="p85942054163319"></a>mesh模型类别</p>
</td>
<td class="cellrowborder" valign="top" width="34.300000000000004%" headers="mcps1.2.5.1.4 "><p id="p1459417542333"><a name="p1459417542333"></a><a name="p1459417542333"></a>支持[0,6]共7种模型，其中type=0/6为强互动模型</p>
</td>
</tr>
<tr id="row2594165413312"><td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.1 "><p id="p1159415548334"><a name="p1159415548334"></a><a name="p1159415548334"></a>12</p>
</td>
<td class="cellrowborder" valign="top" width="24.6%" headers="mcps1.2.5.1.2 "><p id="p259417540332"><a name="p259417540332"></a><a name="p259417540332"></a>region_w</p>
</td>
<td class="cellrowborder" valign="top" width="25.650000000000002%" headers="mcps1.2.5.1.3 "><p id="p15941254143320"><a name="p15941254143320"></a><a name="p15941254143320"></a>动画显示区域宽度</p>
</td>
<td class="cellrowborder" valign="top" width="34.300000000000004%" headers="mcps1.2.5.1.4 "><p id="p15594854143312"><a name="p15594854143312"></a><a name="p15594854143312"></a>[0,32]</p>
</td>
</tr>
<tr id="row9594105453317"><td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.1 "><p id="p15594105483315"><a name="p15594105483315"></a><a name="p15594105483315"></a>13</p>
</td>
<td class="cellrowborder" valign="top" width="24.6%" headers="mcps1.2.5.1.2 "><p id="p359465417338"><a name="p359465417338"></a><a name="p359465417338"></a>region_h</p>
</td>
<td class="cellrowborder" valign="top" width="25.650000000000002%" headers="mcps1.2.5.1.3 "><p id="p1459495415334"><a name="p1459495415334"></a><a name="p1459495415334"></a>动画显示区域高度</p>
</td>
<td class="cellrowborder" valign="top" width="34.300000000000004%" headers="mcps1.2.5.1.4 "><p id="p25941054123312"><a name="p25941054123312"></a><a name="p25941054123312"></a>[0,32]</p>
</td>
</tr>
</tbody>
</table>

> ![](public_sys-resources/icon-note.gif) **说明：**
>
> - mesh_x_block_num：逻辑约束mesh_dst_width / x_step < 128， 软算法性能约束不超过32。
> - mesh_y_block_num：逻辑约束mesh_dst_height / y_step < 128， 软算法性能约束不超过32。
>   弱互动：只转动表冠；需要载入模型。
>   强互动：支持触屏；不需要载入模型。

**表 6** MESH表盘互动demo参数

<a name="table1148016549337"></a>

<table><thead align="left"><tr id="row659465413334"><th class="cellrowborder" valign="top" width="18.45%" id="mcps1.2.5.1.1"><p id="p1559495412335"><a name="p1559495412335"></a><a name="p1559495412335"></a>序号</p>
</th>
<th class="cellrowborder" valign="top" width="25.119999999999997%" id="mcps1.2.5.1.2"><p id="p7594654103317"><a name="p7594654103317"></a><a name="p7594654103317"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="31.430000000000003%" id="mcps1.2.5.1.3"><p id="p185945548335"><a name="p185945548335"></a><a name="p185945548335"></a>解释</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p85941754143315"><a name="p85941754143315"></a><a name="p85941754143315"></a>范围&demo值</p>
</th>
</tr>
</thead>
<tbody><tr id="row759412543330"><td class="cellrowborder" valign="top" width="18.45%" headers="mcps1.2.5.1.1 "><p id="p059455410332"><a name="p059455410332"></a><a name="p059455410332"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="25.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p959414548337"><a name="p959414548337"></a><a name="p959414548337"></a>mesh_ctl</p>
</td>
<td class="cellrowborder" valign="top" width="31.430000000000003%" headers="mcps1.2.5.1.3 "><p id="p1659414543335"><a name="p1659414543335"></a><a name="p1659414543335"></a>连续帧控制</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p3594154113313"><a name="p3594154113313"></a><a name="p3594154113313"></a>[0,100];</p>
</td>
</tr>
</tbody>
</table>

### 蒙版工具<a name="ZH-CN_TOPIC_0000002399739793"></a>

蒙版制作工具支持展示/生成圆形、高斯模糊、HSV三种蒙版文件。

- **使用方法**
- **控制参数**
- **注意事项**

#### 使用方法<a name="ZH-CN_TOPIC_0000002366100014"></a>

**运行<a name="section17318245565"></a>**

单击COMMANDS里面的Modeling Tools，在上方选择“Mask Tool”。

<img style="display:block;" src="figures/zh-cn_image_0000002423227462.png" width="606">

**界面介绍<a name="section1021463835619"></a>**

启动后工具主界面如图所示：

**图 1** 蒙版工具启动界面<a name="fig39911508561"></a>
<img style="display:block;" src="figures/蒙版工具启动界面.png" width="700" alt="蒙版工具启动界面">

其中按钮功能介绍如下：

- 模型类型：选择当前要使用的模型（高斯蒙版、圆形截图蒙版、HSV蒙版）
- 生成蒙版：在界面左侧区域生成蒙版图片
- 保存蒙版：保存蒙版文件。
- 显示日志/隐藏日志：打开/关闭下方的日志框

**操作步骤<a name="section17766850105615"></a>**

1. 选择模型类型
2. 修改右侧控制参数（可选）
3. 单击“生成蒙版”查看效果。
4. 单击“保存蒙版”保存蒙版文件

**素材默认路径<a name="section1982618594564"></a>**

HSV蒙版生成需要依赖素材文件。工具已提供默认素材文件，用户可自行替换。素材文件路径和文件名如下：

C:/Users/$\{用户名\}/.vscode/extensions/hispark.hisparkstudio-$\{版本号\}/dist/resources/mask/mask_test/res/input/hsv_img_w454_h454.data

其中$\{用户名\}为当前Windows登录账号用户名，$\{版本号\}为本插件版本号。

> ![](public_sys-resources/icon-notice.gif) **须知：**
> 该文件不能删除或修改文件名，否则会导致程序运行错误。

**高斯蒙版路径参数生成方法<a name="section710141005719"></a>**

1. 打开网址：[https://www.jyshare.com/more/svgeditor/](https://www.jyshare.com/more/svgeditor/)
2. 绘制图形：目前只支持以path开头的图形。
3. 注意：绘制图形时，需要在未选中图形时，在最右侧设置分辨率。
4. 单击菜单栏-\>视图-\>源代码。
5. 复制path中的“d=”之后的字符串到路径。

#### 控制参数<a name="ZH-CN_TOPIC_0000002399619925"></a>

路径：字符串（仅高斯蒙版模式需要）

宽度：素材width（最大640）

高度：素材height（最大600）

通道：素材channel（只支持3：RGB、4：ARGB）

#### 注意事项<a name="ZH-CN_TOPIC_0000002365940118"></a>

- 只有高斯蒙版需要路径，其他两个模式下路径默认为空。
- 圆形截图蒙版只支持正圆。
- HSV蒙版工具目前不支持RGB格式。

## GUI工程使用常见问题<a name="ZH-CN_TOPIC_0000002399739797"></a>

- **起模拟器日志记录位置**

### 起模拟器日志记录位置<a name="ZH-CN_TOPIC_0000002366100018"></a>

在启动模拟器运行过程中的日志信息记录在当前打开的工程根目录下的“simulator_build/error.txt”文件中。可参考“Demo运行”。
