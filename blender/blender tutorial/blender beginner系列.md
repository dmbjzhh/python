## blender beginner系列

#### Part1：了解界面

在没有小键盘的情况下，去设置里面，选择emulate numpad，就可以用上面的数字键来模拟小键盘的操作，137是可以从三视图观察物体的快捷键，TopView 7，FrontView1，SideView 3。不选择上面的emulate numpad的话，上面的数字键默认是切换图层的快捷键。

四周查看的快键键：shift+鼠标中间，可以移动查看；直接用鼠标中间是以正中间旋转查看。

选中物体后，按数字键盘的小数点键可以快速查看物体

 shift a可以创建新物体

空格键可以输入命令

alt a可以播放和暂停动画

#### Part2：移动、旋转和放缩

s调整scale，scale的时候按住control和没按control一样，按住shift的话变大的速度会慢一点

创建新物体后，左侧会出现一些新功能，它们在物体刚创建的时候会有，调整物体之后就会消失

有三个箭头，红色的代表x，绿色的代表y轴，蓝色的代表z轴，选中物体后点击轴，可以只在一个方向上移动

选中物体后按g键，可以到处移动物体，按g以后再按xyz，就会只按xyz轴移动，更快的方式是按g后按鼠标中间

r是旋转物体，gsr后都可以再敲xyz

属性栏的Modifier，可以在不用改变物体本质的情况下，给物体添加修改。比如说让物体的面多一点。这一点也可以通过创建物体后，调整它的面来实现，但是渲染起来会非常慢，而且不可修改，因为已经是物体的一部分了。而Modifier使得对mesh有完全的掌控，不想要的时候还可以删了，这是一开始就创建一个多面的物体做不到的。

#### Part3：Edit Mode

在添加modifier的时候，一般把Subdivision的View设低一点，Render设高一点，View只是你看到的，最终渲染不会出现，Render是最终渲染才使用的。这样做的好处在于，如果View的时候面太多很有可能会卡。

tab切换Edit mode

edit mode只允许对指定的一个物体进行调整形状

edit mode下的vertices mode，按shift可以多选点，按alt，可以选一排点，也就是线，同理可得Edges mode和faces mode，分别是选线和选点的，shift和alt都可以。

选中了不管是点线面以后，按g，可以移动它们，同理可得上面提到的rgs

选中了东西以后，按o，进入proportional editing mode，可以在一定范围内调节选中的东西，范围大小可以通过鼠标滚轮来调节。按o之后rgs都适用。而且proportional也有不同的模式，比如random、linear、sharp等等

box select：按b，然后鼠标左键拖拽，可以实现快速选择。按b，然后按鼠标中间拖拽，取消选择

全选和取消全选：a

circle select：按c，再按鼠标左键可以实现涂画选择，按鼠标中间可以涂画取消选择

但是这样直接选会有一个问题，就是背面选不到，只能选择看得到的地方。可以在edit mode中进入透视模式，就是在点线面旁边有个小图标，选中就可以透视，这个时候再选就可以选中看不到的面了。

wireframe mode，快捷键z，它移除了所有的面，只有物体的线存在，也可以同样的选中想选的东西

复制：shift d，escape

如果两个东西重叠到一起了不好选择，可以按L，它会选择所有的mesh只要是和你选中的点相连的，然后按g移开就可以了，但是这样终归有点不方便。所以可以选中需要的结点，按ctrl + L。选中重叠的部分后，用快捷键p，弹出seperate菜单，选择selection，就可以将两个部分分离开，变成两个对象。

如果只复制了一部分对象，那么复制出来的是个空的面，不是实体，而且没有任何厚度，看起来不好看，所以可以添加一个modifier：solidify，它能将重叠的线区分开，给面增加厚度吧，这个厚度什么的是可以通过modifier调节的

modifier是有先后顺序的，可以通过上三角的箭头或者下三角的箭头调整顺序，比如先solidify再smooth的话，整个甜甜圈涂得酱的边缘就会特别顺滑，很smooth；但是如果先smooth再solidify的话，整个甜甜圈边缘就会显得突兀。

用modifier增加面来顺滑以后，可能会出现卡顿的情况，这时候可以点一下modifier旁边的小眼睛，来取消在view port中显示那么多面。其实它是那么多面，只不过不显示了而已。在渲染的时候显示就好了。

#### Part4：material结点

使用material结点编辑器

点击property窗口里面的render，就会开始渲染。blender中有3个渲染引擎，game一般不用，blender render是老的渲染引擎，cycle是新的。

对比不同的render效果，可以切换不同的slot，快捷键是J，然后就可以重新渲染一遍来对比效果。

blender render中的暗部是全黑的，在现实世界中不可能，旧的渲染引擎不会计算光的反射，而新的可以，如果要做那种像照片的渲染，cycle比较好，而且blender render以及不再被开发了。但是，cycle比较慢啊，blender render就要快很多。看需求吧，一般目前用cycle。

隐藏一个物体的快捷键：选中物体，按h，显示隐藏后的物体：alt h

给一个物体增加material：

* 在属性栏选中material选项卡，然后增加新的material就行
* 但是在做出改变以后，在3d窗口中发现物体并没有什么变化（比如改变颜色）那是因为我们还没参与到渲染中去。要看到效果的话，可以切到render选项卡，按render来渲染一下看效果。但是这么做很慢，所以更好的做法是，改变object mode按钮右边的那个小白球按钮，选择Rendered，就可以在3d视图中看到渲染后的效果，快捷键是shift z

快捷键0是可以看到摄像头中的画面

用modifier增加的许多面，看起来顺滑，但是仔细看还是不顺滑的，所以可以通过工具栏的shading中的smooth来顺滑，这个顺滑也是要建立在有一定形状的基础上的。

甜甜圈上面的酱看起来很假是因为在material中用了一个Diffuse的表面，这个表面不会产生任何反射，在现实世界中几乎不可能。

material中的表面有不同模式：

* 纯Glossy BSDF一般用在金属上，但是gloss会混合其他的一起用
* 一般使用diffuse和glossy混合到一起用，这就要用到node editor

Node editor：

* 快捷键：shift F3去Node editor，shift F5回3d view


* shift a，增加新节点
* Node editor中的每个节点的输入输出的dot的颜色要匹配才能相连，不然是没啥作用的
* 每个节点左侧的input点都只能有一个输入，所以要混合两种shade时，要增加一个mix shaders的结点，然后将要混合的两种材质都连到mix shader上，再从mix shader指向material output
* 为了能够更直观的看到更改结点后对当前模型产生了什么影响，可以将3d view分开，另一半放Node editor

Mix shader：里面的fac属性用来调节两种shader的比例，0是上面的input连着的结点的比例最大，1是下面input连着的结点比例最大

如果只想调整边缘，而不想proportional edit mode影响到其他地方，可以先选中不想影响的地方，按h隐藏起来，然后对想要调整的地方进行调整，调好以后，按h显示隐藏就可以了

#### Part5：Modeling

图层，可以用来专心刻画一个模型，而不被其他的干扰

选择多个图层，在底下的图层小方块中，按shift多选图层。

将对象移到另一个图层，点快捷键M，选择想要的图层即可。

可以根据图像来创建模型，按n显示property bar，然后勾选Background Images，点add image，选择需要的图像。但是在3d view中可能看不到，那是因为图片展示只能在137快捷键对应的角度看到，可以在旁边的property bar中的Axis选择front，就可以只在front view中看到图像，这样做是为了可以载入三视图，然后根据三视图的图像建模。还是看不到就按一下5，会转换成orthographic，就可以看到。

载入杯子的图像之后开始做杯子，创建一个圆柱体，就立刻在旁边的Vertices中修改它的顶点数（不立刻修改是会消失的），一般默认是32，可以改为16，因为这样可以避免渲染速度过慢。

blender的输入框中可以直接输入公式，比如要改为16，可以输入32/2，blender会自己算结果

Loop cut：调节mesh的部分区域，用ctrl R后会出现一个紫色的线，确定想要那个方向的线以后，鼠标左键，就可以进一步确定线的位置，要是确定位置的时候不小心选错了，可以双击g，重新回到选择。选择好线之后还是可以用rgs

切分表面的快捷键：ctrl 1或234，1234是切分表面的级别，如果切分表面切得不理想，太顺滑了，可以进入edit mode，ctrl R增加loop，其实是在想要的地方增加了顶点，就可以看到控制流subsurf的效果

油画笔：按住d，就可以用鼠标左键画画，用鼠标右键擦除

马克杯因为有16个顶点的圆柱体，边缘突出不好看，可以把顶点往里缩，用Inset，快捷键I，缩到边缘里面的位置就好，这样边缘就顺滑了，没有顶点的bumps

往马克杯中挖个洞可以用extrude，快捷键：e，可以拿着面伸缩

blender保存多版本文件可以有个方便的功能：如果要保存的文件里面有数字，F2保存，按一下+，就可以自动增长那个数字，按enter保存下来。

EGR

blender中连接物体，是通过创建面来实现的，先选中四个点，然后按F，就可以在四个点中创建一个面。但是这样连接的会不自然，中间有痕迹，可以通过删掉连接处的面来解决问题，两个连接的都要删

为了避免不同图层物体大小（scale）相互影响，或者不好区分，按ctrl a，选择scale，这就应用了scale，在右边的property bar中可以看到scale都变成了1

#### Part6：Texturing

创建盘子：添加一个circle，在刚创建的左边的属性中的Fill type选择Ngon，这样就是一个有个面的环了

可以为物体添加图片来实现质地，但是随便找的普通图片不行，要那种没有阴影和高光的图片，必须要去专门的网址找，比如www.textures.com和www.poliigon.com

添加材质：

shift a，选择texture，选择image texture，创建了一个新的texture结点，它的color输出作为shader结点的color的输入，连接起来。但是这样感觉只变了颜色而已，还需要调整uv wrapping

添加材质，就是要让3d的东西变扁平2d来贴图，需要通过UV /Image Editor来做到，打开UV Editor，先点RenderResult旁边的×，因为一打开就直接是结果了。需要删掉做新的。

给指定对象进行uv调整：在3d view中选中对象，进入edit mode，按u，弹出uv unwrapping menu，选择unwrap，就会把对象映射到2d中。平面的东西这样做就行了，比如桌子面，但是对于立体的东西，比如cube，这样不够，直接这样会让一个面上的材质重复而已，不好看。

wrap cube：如何给一个cube添加材质，需要先把cube解体成不同的面（就像小时候做的那种题，给一个平面的正方体拆解后的图，这个图能折成一个正方形，问把这个正方形折起来，哪一面在哪），在edit mode下，选择需要的edges（要确保按选中的这些edges剪这个正方体后，它能变成一个完全的平面，而不是还有地方折起来），按ctrl e，选择mark seam，这个正方体就会拆成一个平面。

world颜色在属性栏的world选项卡里调整surface的color。

总的来说，要给一个立体的东西贴图，需要把这个东西想象成纸做的，怎样用剪刀剪它的边缘能够把这个物体完全展开成2d的。

这样添加好了以后，能在东西上看到材质效果，但是还不够，因为看不到物体表面特有的那种凸起，所以需要bump mapping，让它看起来更真实一点。

添加材质表面的纹理：

在结点编辑器中复制（Shift D）已经弄好的image editor，打开已经处理过的紫色的决定哪里凸起的图片，因为这个图片主要的是图中的纹理信息，而不是图片的颜色，所以要把Image Texture结点的Color选项改成Non-Color Data。再加一个结点，shift a，Vector，Normal map。从打开凸起图片的image editor连到Normal map的color上，再从Normal map的Normal上连到两个shader结点的Normal上。

现在已经有凸起的纹理了，还可以控制物体的粗糙度，也是要用特殊处理后的图片（浅灰色的），还是先创建一个image texture结点，打开特殊处理过的代表粗糙度的图片，然后同样选择non-color data，从输入的color，连到输出的Glossy BSDF结点的Roughness就可以了，这样就控制了这个表面的粗糙程度。

为了进一步调节粗糙程度，可以shift a，Converter，ColorRamp，放到刚刚连roughness的线上，这就做到了物体部分表面会有比较锐利的反射，另一部分会有比较散的反射。

还可以下载那种代表表面反射程度的图片（深灰色），然后还是用image texture打开，设为non-color data，连到mix shader的fac上，这样可以确定那部分要闪闪发亮一点，哪个比较diffuse一点。

#### Part7：Particles粒子

Particles可以用来在表面上创建超级多的物体，比如草地上的草啊，岩石啊等。

创建物体的话，最好一开始用面比较少的物体，免得物体一多了，渲染起来很费劲。Low poly。

在放缩物体的时候，按s之后再按shife z，这样就会只缩小xy轴，z轴不动。

对于那种对称的物体，不用调好左边之后，再对右边做同样的事情，而是可以通过添加一个modifier，选择mirror。其中axis是对称的方向，可以三个方向都对称。注意它的对称会把中轴上的所有部分都对称下去，所以会造成重叠，最好就是搞一半，然后对称过去，拉到中间连着就行（edit mode模式下。记得选择clipping，这样到中间了就会自动停住）。

particle就是用来将一个物体作为原型来创建无数个跟这个物体一样的物体。

先选择想要出现东西的表面，然后去属性栏选择particles选项卡，按new。如果这时候按z去wire frame模式，按alt a，就会有效果。

blender中有两种粒子，一个是静态的，叫做Hair；一个是动态的，叫做Emitter。默认是动态的，用来创建可以动的粒子。在type里面选择hair，发现hair是朝里面的，因为前面的solidify modifier的影响，会filpping，所以要把甜甜圈icing的面朝里（在edit mode中查看面朝向：按N调出属性栏，在Mesh display的Normal中选择代表面的那个小正方形），具体是在edit mode中选中面，在工具栏的shading/uvs选项卡，选择Normal中的Flip Direction，然后再调节一下icing的solidify modifier的Offset。

用Hair作为粒子显然不对，虽然它是静态的，所以要把hair换成想重复的物体，先在None、Path（默认）、Object、Group中选择Object，然后再在底下的Dupli Object中选择我们要重复的物体的名字。

然后勾选上面的Advanced框，出现Rotation框，勾上，将Rotation中的Velocity/Hair改成Normal。然后Normal下面有两个Random框，左边的是可以使粒子立起来的，右边是使得粒子在表面上旋转的，这里用到右边的random。

还可以在Physics中修改size

如果想重复出现多个物体，可以用group。选中所有想要group的物体，然后按ctrl g，就绑成了一个组。

然后在particles中不选择Object而选择Group，然后选择刚才绑好的组即可。

按住ctrl或shift或两个一起按，可以成倍调节一个框里的数值。

如果想给多个物体添加同一个已经调好了的样式的话，选中多个物体，最后选那个已经调好了的，然后按ctrl L，选择Material就行，然后共享的那个material会在旁边显示一个数字，代表有多少个对象共享这个material，按一下那个数字按钮，就解除了link，变成了新的独立的material。这时候修改material不会对之前共享的material造成影响。

上面的步骤完成了，那些糖粒是均匀散布在icing上的，但是现实中总会有的地方撒的密集，有的地方稀疏，所以可以改变物体的散落：Vertex Group

从object mode进入weight paint mode：ctrl tab，然后3d view中就显示了蓝色，蓝色代表什么都没，即0；红色代表密度最大，即1，然后可以在工具栏的Tool选项卡中看到Brush，此时它的weight是1.0，用鼠标去刷蓝色部分，红色的部分代表密度最大。刷得次数越多越红。

然后在Particles选项卡的Vertex Group中的Density选项选择Group，就达到按红色部分密集分布的效果。

Vertex Group可以让物体的一部分做一些事情，让另一部分做另一些事。

#### Part8：Lighting

**Lamps**：

* point lamp

  向四周发射光

  size越小，光越锐利，细节越多；越大，影子的边缘越模糊，物体越柔和。所以拍人像最好size越大越好。


* sun

  如果切换到sun lamp，strength最好不要超过5。

  而且不管sun在哪，物体总是会被以同样的角度同样的光照照亮。除非改变sun的角度。

  同理可得，正午的太阳size小。

* spot lamp

  聚光灯，有范围限制。

  用size控制范围大小，用blend控制边缘的模糊程度

  勾选show cone可以看到在object mode的solid模式中看到物体的哪部分被光照亮。

* Hemi

  一般不用，被sun代替，据说是在旧的blender渲染器中使用的。

**World lighting**

在属性栏的world选项卡中，可以修改color，来修改世界的颜色。

一般还是要结合上面的灯使用，一般世界灯可以给物体的阴影添色调的。

**Mesh**

让物体成为光源，在属性栏的Material中，将Surface改成Emission，就可以让物体成为光源，还可以调节。

一般的用法是创建一个平面，当做灯源，有时候比用lamp好。



灯光取决于将摄像机放在哪，所以最后在设置灯光的时候，先把摄像机的机位找好，在开始设置灯光

自己的角度找好以后想把摄像机移过来的快捷键：ctrl alt 0

0进入摄像机视野

按r并且用鼠标滚轮，可调节摄像机角度

按g并且用鼠标滚轮，可以调节摄像机远近距离

世界色最好设为0，即黑色，要不然还是会有一点点光的。

一般用area lamp比较方便

进入render view的快捷键：shift z

根据需要加光源，而不是漫无目的，没有依据地加



可以将所有的灯光移到一个图层：选中所有需要移动图层的物体，按M，选择想移过去的图层。

给同一个物体添加多个material：

进入Edit mode，选中物体中想加别的材质的部分，在属性栏材质选项卡选中别的想加的material，按下面的Assign(有Assign、Select、Deselect三个键，只能在edit mode下看到)

在默认的3d view中看到物体的颜色，而不用去render view：

默认View port中所有物体的颜色都是白色的。在属性栏的材质选项卡中选中材质的Color，拖到下面Settings的Viewport Color中的颜色就好。

#### Part9：渲染和Compositing

blender可以用CPU和GPU进行渲染，一般来说用GPU会快很多。

* 查看是否电脑是否有GPU：

  在用户设置的System中，左侧底下有个Compute Device，如果有CUDA选项，就有blender可以用的GPU。选中CUDA，就可以选想要用的显卡，然后保存用户设置。

  然后去属性栏的Render选项卡，Device中选择GPU后，就可以用GPU渲染。

  ​

以下所有设置都在属性栏的Render选项卡中找：

blender渲染的时候会出现小方块，按小方块一个个渲染的，渲染的过程主要是消除其中的颗粒。

Sampling中的Samples，render的值越低，渲染出现的颗粒越多；这个值也可以设得超级高，但是其实到一定程度就停了的，设得再高也没用，渲染图像中总会有一点点颗粒的。

一般开发测试的时候可以将render值设低，快一点；最终出成果的时候render值可以设高。室内场景，render值一定要设高，因为涉及到很多光的反射，设低的话颗粒会很明显；室外场景可以设低一些。

用CPU渲染的话，小方块的个数就是CPU的核数（可以在Performance的Threads的Auto-detect的下面看到核数），如果有八核，一次能渲染八个小方块；用GPU渲染，小方块的个数通常只有一个，也就是一次只能渲染一个小方块。

因为用GPU一次只能渲染一个小方块，所以可以把小方块的大小设大一些，在Performance的Tiles的Hillbert Spiral中的xy值，比如设为256。相反，用CPU的话，将Tile size设小一点，比如16，渲染速度比较快。

渲染出来的图像的大小在Dimension的Resolution中可以调节，一般调节下面的百分比就够了，百分比越小，图像越小。在日常做场景的时候，可以将百分比设低，那样图像会小，渲染很快。最终场景可以把百分比设为100%。



**艺术角度**：

一般来说，画面中最好不要超过三个主要颜色。

* 调节物体的饱和度：

  在Node Editor中，增加新节点，选Color，选Hue/Saturation，将这个结点加到Image Texture和Diffuse之间，就可以调节结点上的Saturation值来调节饱和度。

* 调节摄像机景深：

  在现实世界中，摄像机不可能聚焦到每个物体上，所以要调节景深。

  具体做法：

  选中摄像机，在属性栏的摄像机选项卡的最后面，有Depth of Field，法一是直接在Focus下面的小方块中选中物体的名字；法二是，Focus的Distance就是调节摄像机焦距的。先选中上面的Display的Limits，这样就会出现一个摄像机视野的线，然后调节Distance大小，就可以看到一个十字线在摄像机线上移动，然后将十字线放到想要聚焦的物体上即可。

  Focus旁的Aperture是光圈大小，一般用F-stop，然后根据需要调节下面的number。


渲染好了以后保存相片的快捷键：F3

Compositor一般用于最后调整相片的时候，像Photoshop一样调节渲染出的相片的效果。

进入Compositor：先进入Node editor，然后在底下选中Node右边三个小图标的中间那个Compositing。勾选Backdrop会让渲染好的图片出现在背景中。然后像调节材质一样通过节点调节图像就行。

通过Compositor调节好图片以后，直接按F11进入渲染模式，是不会直接看到调节后的效果的，因为没有刷新最终渲染。保存调节的图片需要，切分view，然后将其中一个view进入UV/Image Editor中，默认进入Render result，如果没有的话，在Image右边选择Render Result，这时候再把最后调好的线连到Compositor中的Composite结点上，UV Editor中就会刷新渲染效果，这时候保存图片就是调节后的图片了。