> 19发伊莉雅,99发美游  

# "智能战斗不间断,不靠礼装不用拐"的FGO全自动脚本  
当前版本v3.1.4  
祝单身狗Master们情人节快乐  
祝小木曾雪菜生日快乐<del>你为什么这么熟练啊</del>  
GitHub项目地址:[https://github.com/hgjazhgj/FGO-py/](https://github.com/hgjazhgj/FGO-py/)  
快速跳转:[版本记录](#版本记录-Version-Logs)  
当前版本更新很快,因此**不建议fork**  
你可以star以便日后访问,或者直接把本项目地址加入浏览器收藏夹  

# 警告  
**[<<哔哩哔哩游戏平台用户协议V1.0.0>>](https://yhxy.biligame.com/)第11条第2款规定:**  
**用户不得通过不正当的手段或其他不公平的手段使用本平台游戏、本平台服务或参与本平台活动。**  
**用户不得干扰本平台正常地提供游戏和服务，包括但不限于：攻击、侵入本平台的网站服务器，或集中时间段内以超出正常用户登录需求的高频率登录或尝试登录服务器从而使网站服务器过载；破解、修改本平台提供的本平台游戏程序；攻击、侵入本平台游戏的服务器/游戏服务器端程序或使游戏服务器过载；制作、发布、传播、使用任何形式的妨碍游戏公平性的辅助工具或程序(包括但不限于“外挂”, “外挂”是指独立于游戏软件之外的，能够在游戏运行的同时影响游戏操作的所有程序，包括但不限于模拟用户操作、改变操作环境、修改数据等一切类型）。用户不得：利用程序的漏洞和错误(Bug)破坏游戏的正常进行或传播该漏洞或错误(Bug)；不合理地干扰或阻碍他人使用本平台所提供的游戏和服务；通过异常或者非法的方式使用本平台游戏(包括但不限于利用本平台游戏登录游戏私服)；使用异常的方法登录游戏（包括但不限于使用非本平台开发、授权或认可的第三方软件、系统登录游戏）、使用网络加速器等外挂软件或机器人程序等恶意破坏服务设施、扰乱正常服务秩序的行为；修改、翻译、注释、整理、汇编、演绎本平台游戏；利用本平台游戏或者线上游戏系统可能存在的技术缺陷或漏洞而以各种形式为自己及他人牟利（包括但不限于复制游戏虚拟物品等）或者从事其他不正当行为等。**  
**由于使用本脚本而导致的包括但不限于上述各项的损失本人概不负责,您下载并使用该脚本即代表您已知晓使用脚本可能带来的风险并愿意承担可能出现的后果,望周知**  
<del>但是fgo内部的用户条款好像没有限制脚本的使用</del>  
***  
# 使用说明 Instruction  
本readme仅使用了基本markdown语法,你可以在任意编辑器上查看  
本readme仅仅教你怎么用这个脚本来玩fgo,并不会告诉你代码是怎么写的,代码里也没有一行说明性质的注释,所以有几行代码我自己都得看一会儿才看得懂  
脚本可以后台运行,只要不发生错误就不影响你干其他事,模拟器窗口可以丢失焦点可以被遮挡但是不能被隐藏或最小化,锁定系统不干扰脚本运行  
若要用于真机,参见[这里](#如何将此脚本应用于真机)  
安卓分辨率和实际显示在屏幕上的分辨率最好是长1920或宽1080,其他分辨率亦可  
你的电脑上要有adb  
使用了以下外部库:  
`configParser` `opencv-python` `pywin32` `PyQt5`  
没有的直接`pip install`  
记得开启USB调试  
本脚本的代码部分仅有`fgoFunc.py`是fgo算法相关的,其他的部分基本是为ui服务的  
这个脚本会自动放技能(默认不用技能),自动放宝具(充能满就直接放宝具),[可以设定](#关于skillInfo_houguInfo_dangerPos_friendPos),自动选卡(优先三色chain,否则优先红卡).合理设定后实战7-12回合能够刷完无限池终本  
速览脚本功能,运行fgoGui.py  

我的联系方式  
qq 979449732(加好友请说明来意  
email huguangjing0411@geektip.cc  
有任何技术问题或bug反馈或本readme中有任何包括但不限于错别字语法错误描述错误的问题请联系,觉得有帮助请为我star  
**没有标明免费的东西都不是免费的**  
请向可怜的非酋投喂<del>圣晶石</del>彩苹果,实在是没钱过年了...  
## 你需要修改adbPath和各个hWnd  
使用ui界面时,即使不修改这些值脚本也能正常运作
`adbpath`要根据你的设备连接方式进行修改  
使用ui界面时,请在下拉列表中选择或输入  
`hPreFgoWnd`和`hFgoWnd`为显示游戏画面所在的窗口句柄,对于多数模拟器而言,一个主窗口(overlapped window,hPreFgoWnd)下就只有一个用于显示游戏画面的子窗口(child window,hFgoWnd),这时你只需要把hPreFgoWnd所在定义行中的字符串改为模拟器的主窗口标题就可以了.  
使用ui界面时,你可以使用'获取窗口句柄'按钮来给它们重新赋值  
## 关于skillInfo/houguInfo/dangerPos/friendPos  
你可以在ui中可视化地修改  
**`skillInfo`列表记录了技能的信息**  
`skillInfo[编队中的第i个从者][的第j个技能]=[该技能的最小使用stage数,在该stage的最小使用回合数,指向的目标(没有目标置0)]`  
也就是说,若不使用技能就`skillInfo[i][j][0]=4`  
这样的安排足以应付日常周回的各种情况,比如三面Boss充能五格,就把保命技能=[3,6,0]  
**`houguInfo`列表记录了宝具的信息**  
`houguInfo[编队中的第i个从者]=[的宝具的最小使用stage数,在该stage的最小使用回合数,优先级(越小越优先)]`  
**`dangerPos`代表各stage的优先攻击位置**  
右到左依次为dangerPos0-2,当boss血条与小兵血条不在同一行内时(魔伊,鬼岛,罗生门,FA,柱子,etc.)第二行的三个位置为dangerPos3-5  
**`friendPos`代表好友在几号位**  
从0开始编号  
## 助战 Friends  
你需要事先将你期望的各种助战的样子截图为png放在asserts/friend下,参照asserts/friend/unused中的文件,如果asserts/friend目录下没有文件,就选取好友列表中的第一个  
**被截图范围都应该可以点击来选中该好友**,实际的点击位置为图片的正中央  
如果你用的是模拟器,请使用本程序的`Check().save()`来截图而不要用模拟器自带的截图,更不要用<kbd>prtSc</kbd>键或其他工具来截图,这可能会导致识别错误  
如果你用的是手机,这些函数也可以大大方便你的操作  
使用`Check().save()`函数时,建议将显示画面和安卓系统画面都调整至1080p,以避免缩放带来的误差  
助战截图的文件名中若有下划线'\_',且下划线之前的部分为km,ml,cba,则代表好友就挂的是孔明,梅林,十八岁美少女,这会影响助战技能的使用,参见`chooseFriend`函数具体实现  
## 如何将此脚本应用于真机  
v2.7.x及之前版本能在任意支持python和adb的系统上用于任何1080p的Android设备,v2.7版本的代码现在也是可以用的尽管可能不是那么稳定功能也差得远,x2.8.0及之后的版本仅仅由于截图方式由adb改为win32api而只能在windows系统使用,如果使用真机,请把手机屏幕找一个投屏软件投到屏幕上
使用真机时,你还需要以下操作:  
投屏软件画质和分辨率尽可能开高  
理论上来说,你只需要把`tap`和`swipe`函数及其直接或间接引用的变量替换成适合你的设备的内容就可以了,但是部分真机会比较卡,你可能需要在各种地方添加延迟,并适当增加`Fuse.__max`  
你还可能需要适当增加各处识别的`delta`值,0为完全匹配,1为完全不匹配(`TM_SQDIFF_NORMED`)  
但是对于我自己用的手机,以上更改均未进行,照样很嗨皮  
# 注意 Caution  
模拟器窗口不可最小化,所以强烈建议关闭模拟器的"老板键(boss key)"功能  
若战斗失败会自动撤退并留下记录然后继续下一把(若战斗失败就发出噪音把你吵醒起来改代码?倒也不是不能做到啦~)  
音频文件sound/default.wav是超炮3的op<<final phase\>>  
有些时候对从者头像的识别会有错误,*已基本修复,大姐二姐这种长得没差几个像素的真没办法* ,当场上队员不足三个时,带指向的技能**可能**没法向正确目标施放,或者根本没法释放而卡住所以如果你打算睡觉去,就不要用后排的技能,也不要用带指向的技能,否则万一一觉起来发现打第二把的时候就卡住了...也请注意战斗到一半再启动`oneBattle`函数时场上队员不是首发队员时导致的此问题  
如果游戏画面是1920*1080(长宽至少一个相等)的,那么这个脚本可以完全稳定运行,如果缩得太小或非整数倍缩放,又或者投屏软件画质太低,可能会有部分识别判定不能得出正确结果,多半是宝具放不出来,问题不大,可以忽略,已基本修复,另外,由于浮点误差,可能在各个阶段有1px的偏差,请开发者们注意在识别时留出冗余  
# Q&A&杂谈  
2018年9月,一件大事发生了,没有人知道这个游戏正在经历一场变革  
那时我刚上大学,年轻人有的是时间,有的是精力,就开始研究怎么压榨电脑的剩余价值.答案就是这个脚本的前身,**[FGO-C](https://www.bilibili.com/video/av34399081)**,代码已经被删掉了,但是当时录了个视频.那时候我的脚本功能跟现在GitHub上别人写的脚本差不多简陋,就是想尽一切办法三回合宝具速刷,速刷不了就凉凉.但是那时候尼禄祭终本是术阶的,计算器一敲正好可以小莫稳定3t,当时NGA上还有专门的np回收计算程序,C#写的,[帖子](https://bbs.nga.cn/read.php?tid=15337515&_fp=16),[GitHub项目](https://github.com/markpanyi/PerpetualNPPerformance)**没错我挖了一晚上的坟把这个帖子找到了!** VisualStudio上装了.NET桌面开发的可以直接打开,但是这个程序有bug,你得在编译后把CraftEInfo.xml和SkillInfo.xml放到编译结果所在目录的Data文件夹里才能正常运行.54年10月31日,尼禄·克劳狄乌斯继承皇位,成为当时罗马帝国即位年龄最小的皇帝.2018年10月31日,我和千千万万玩家一起肝尼禄祭.那次的尼禄祭,283池.  
尝到了这么大的甜头,怎么能停得下来!当时没有现在这么高级的功能,只有用Win32API的keybd_event来模拟键盘事件,必须保持模拟器窗口完整显示并处于激活状态.当初为什么不用adb呢?因为**adb算是对Android的操作,有可能被检测**,这也是为什么日服禁root禁USB调试禁模拟器的原因,而**用Windows的函数隔着一层虚拟机你拿头来检测我** !这样的日子过得挺安逸,直到有一天,我突然发现我当时用的mumu模拟器禁用了虚拟键盘事件,可能是处于效率和延时考虑换成了更底层的实现,这要我来写的话就得创建虚拟设备然后发送硬件扫描码了.有点头大.于是我下定决心换用adb.同时也把语言改成了python,纯粹是因为python处理字符串简单.  
众所周知,python是万能的.于是我不断开发这个脚本,尝试了各种各样的功能,那些曾经使用现已废弃的部分仍可见于被注释掉的部分.先是PIL.Image读取像素进行识别,然后进化成了open-cv的matchTemplate.终于,从"开环控制"变为了"闭环控制".也就是你现在看到的这个脚本.下一步,也就是v3.0版本的目标,一是建立所有从者的数据库,标明技能宝具的详细信息,二是在战斗中获取敌方的信息和更多己方的信息,三是依靠一二两条中的信息在战斗中实现真正智能化的技能施放和选卡.也就是**我能打过的高难用同样的阵容脚本也能打个八九不离十**.而至于本脚本的究极形态,就是**服务器维护我也维护,维护结束我立刻上号挂机,把玩家变成只会抽卡的机器** .当然我有生之年要是没有利益可图就应该不会开发v3.0版,倒不如说2.8这一版本已经基本解决了玩家肝度和游戏强度之间的矛盾,算是接近我心中的理想形态了.讲真有那些时间去写超级复杂但提升不大的代码不如老老实实把那些时间用在亲自打游戏上.  
自古以来,我就有在模拟器上把每个技能每张指令卡都设置一个键位然后用键盘玩fgo的习惯,当初正是因为敲键盘只有按下弹起两种消息,不想鼠标要设定坐标,相对简单明了.比如看到'A'就知道代表使用第一个从者的第一个技能,看到(109,860)就一脸懵B.这一思想贯彻到了现在,代码里的press函数就是干的这件事.这样虽然看起来很蠢,一点都不"面向对象"(虽然我没对象,在线征婚啊喂!<del><<在GitHub上寻求邂逅是否搞错了什么>></del>),但却是**别人的代码得好几个文件加起来上千行,我的代码只要一个文件200-行,还功能比别人强,debug比别人容易**的根本原因.<del>我就是喜欢把所有代码挤在一个文件里怎么了!</del>别人只能三回合(我因此把那些代码叫做"三回合代码"),而像我一样能**实现智能战斗不间断,不靠礼装不用拐** ,并且保持更新的,github上怕不是**只有我一个**.就算找到了功能同等或更强的,代码也肯定没我短.  
承接上文,我自知这个脚本功能过于强大,强大到了严重影响游戏平衡,改变游戏性质,急剧扩大玩家间差异的程度.就算是在GitHub上开源我都是下了决心的.2019年刚过,B站up主[MCLAREN--](https://space.bilibili.com/13033022)搞了一套硬件来在iOS上跑脚本,虽然他的代码就是"三回合代码",硬件也非常简单,但他似乎是第一个做出来的,反正人家就是比我勤快([视频](https://www.bilibili.com/video/av82095192),[专栏](https://www.bilibili.com/read/cv4303413),[GitHub](https://github.com/McLaren12345/FGO_Bluetooth_Assistant)).注意到**硬件不被B站的条款限制** (虽然法律还是会管的),所以等我什么时候有空了,就搞一套差不多的硬件,只要把我的脚本底层交互接口从adb到伺服电机这么一改,然后新瓶装旧酒,挂羊头卖狗肉地出个视频既可以让网友们看到我的脚本,又不怕帐号被封,岂不美哉!  
GitHub上从来不缺有思想有执行力的程序员,希望这个脚本能越写越好,祈祷这个世界再无BUG.  
# 版本记录 Version Logs  
## 2020/02/16 v3.1.4  
bug修复:现在当hFgoWnd最小化时启动脚本不会把脚本窗口移到屏幕外面去  
对于最小化的窗口,GetWindowRect返回[i-32000for i in rcNormalPosition]也就是说,如果你不幸拥有一个分辨率高于32000*32000的显示屏,就可能在相关win32的判断上出问题  
<del>ロン！国士無双！-32000</del>  
bug修复:有些应用,尤其是游戏,不允许消息队列操作,此时不应让窗口弹出打扰用户,所以在setForeground里加了一个try  
优化:调整了tab顺序  
## 2020/02/14 v3.1.3  
杂七杂八的修改:  
处理了工作路径的问题,不依赖调试器设置工作路径(我才发现双击运行会报错)  
现有的7个队伍设置差不多够了,新建/重命名/删除等功能也不见得常用,如果要修改的话就手动改config文件吧,不想写代码了,删库跑路  
确认了Tab顺序  
试图减少了各ui文件的体积(-40%)  
## 2020/02/14 v3.1.2  
bug修复:有关类,列表生成式,eval之间命名空间继承所带来的bug修复  
bug修复:修复了宝具设置不生效的问题,这一bug可能是v2.10.3重构时留下的  
即将更新:编队设置的新建/重命名/删除等功能.代码已经写好了,但是效果有点不友好,所以相关控件被改为了不可编辑不可点击  
## 2020/02/12 v3.1.1  
bug修复:保证setForeground能正常执行  
优化:修改了Key映射,以应对boss血条与小兵血条不在一行里的情况,从上到下从右到左依次为dangerPos0-5,按键为小键盘9-4  
优化:你可以看见你点过哪个编队按钮  
"一个控制台窗口+一个ui"的布局基本确定,我希望移动动其中一个窗口时另一个跟着动  
## 2020/02/12 v3.1.0  
功能移植  
在以前版本中,我可以一边挂脚本一边修改代码,因为代码会在执行开始时全部载入内存  
但是现在由于线程之间共享内存,你可以战斗途中变更各项配置,如果你在两个设备上用相同的队伍打同一个图,你甚至可以在这两个设备间切换  
这究竟是好是坏有待实践证明,目前我认为应该删除这一特性  
但是,想要删除这一特性比较困难.首先我想到的是改为多进程,但是我希望进程退出时对ui进行变动,而Qt的一堆控件都是不可序列化的...  
所以**多进程**是不可能的,也无法利用多进程进行挂起或中断  
再者就是将各项配置都作为参数传入战斗函数,这将大幅重构代码  
还有就是强行禁止一些更改,这样就使用体验极差  
当然究极的解决方案是存在的,那就是搞一个服务端和客户端然后进程间交互,但是这对于一个小项目而言负担过重  
Qt好像有他自己的线程库Qthread,看看能不能解决这个问题----不能  
脑阔疼  
最后还是从进程与线程的区别入手,创建线程前拷贝一份变量,这样,我的线程有了属于他自己的内存.蠢,但是有效  
挂起/中断的功能也用了很原始的实现,但是绝对不会出问题  
## 2020/02/12 v3.0.0  
ui基本定型,基本功能基本生效.  
之后还会移植一些功能  
修订readme  
在开发中遇到了以下问题:  
1. 当`app=QApplication(sys.argv)`执行完毕后,Qt将系统缩放倍率强行调整为1.  
2. QtDesigner里面应用layout的显示效果和预期相去甚远.  
3. python的线程无法挂起或中断,目前要取消脚本运行必须关了整个应用重开  
## 2020/02/11 v3.0.0beta
我打算开始写ui了  
## 2020/01/31 v2.10.10  
代码结构更改,无实质性变化  
我才发现函数定义本身就是可以挤在一行里面的  
## 2020/01/30 v2.10.9  
加入英文readme  
<del>xjb乱写了一个ui之后说不定用得上</del>本来想搞个ui的但是测试到一半发现比直接改代码麻烦得多,就不搞了...但是今后可能会向代码中添加一些接口以便ui访问  
bug修复:修改了一些写代码时手抖留下的错误  
## 2020/01/22 v2.10.8  
优化:又把所有代码塞进一个文件里了,方便交互  
负优化:在`hWnd`初始化的下方加了一行被注释掉的代码,方便那些经常换设备/模拟器的用户  
现在所有启用中的代码少于200行  
## 2020/01/21 v2.10.7  
bug修复:彻底修复了先前版本存在的宝具充能检测方式存在的不稳定不兼容因素  
说明:录屏数了一波帧数,从按下选课按钮到普通指令卡加载完毕需要正好0.5秒,然而按下选课按钮到宝具卡加载完毕需要2.17秒,宝具充能条闪烁周期为1.62秒.因此,每隔0.81秒检测一次就可以保证任意连续两次检测中有一次检测中宝具条的亮度大于从最暗变到最亮区间时间中点的亮度.实际使用时考虑一波误差和截图运算所需时间,取40%亮度值.最暗,最亮和实际使用的亮度阈值的截图在  
另:`isHouguReady`现在应该在选卡之后运行,整合了之前的`isHouguSealed`函数,又压缩掉了一堆代码,并且由于短路运算符的关系效率应该比之前高一些  
另:严格来讲,亮度指的是`0.3*R+0.6*G+0.1*B`,但我的代码中就暴力地`(R+G+B)/3`,反正也是严格递增的,效果相同  
另:上一个版本的更改是完全错误的,只是碰巧圣诞节的几个本背景偏白才有效  
## 2020/01/20 v2.10.6  
优化:多设备兼容性优化,也可能没有优化,也可能负优化,更改了`isHouguReady`函数    
说明:随便网上找了个安卓投屏软件在我自己的手机上测试了一波.全屏显示要会员?C语言写了个脚本强行全屏显示.勤劳与智慧的天朝人民是绝对不会给你一分钱的!转念一想我的脚本现在已经不用全屏了啊...然后这个投屏软件有四个标题类名都一样的子窗口,所以我还得在每次投屏后手动填写句柄值...垃圾软件毁我青春!  
另:`isHouguReady`函数是当前唯一一个像素识别而非模板匹配的函数,之后可能还得改  
## 2020/01/20 v2.10.5  
bug修复:现在fgo_shell内的初始化部分能正确地获取尺寸及缩放信息  
说明:`adb shell wm size`会返回通常使用方向的尺寸,比如手机就是1080\*1920之类,而平板就可能是1920\*1080,而fgo始终是横屏(landscape)方式显示,这导致了之前版本的初始化有可能将长宽颠倒  
## 2020/01/18 v2.10.4  
优化:`setSkillInfo`更名为`setInfo`,以便添加更多快速换装信息  
优化:重写一些代码,现在能够适应任意(非16:9)分辨率及显示画面  
另:重构了一堆代码,极大地并且过分地压缩了代码的纵向长度,将已经基本定型的代码挤到了一行里,可读性大幅下降.用更精简的代码实现更强大的功能  
lambda函数是好文明!  
## 2020/01/16 v2.10.3  
修改了一些写代码时的失误,简化了一些代码,删去了一些很久都没有再次用上的代码段  
说明:能写在一行里的绝不写两行  
更改了代码开头的字符画  
## 2020/01/14 v2.10.2  
bug修复&优化:考虑了从者行动不能的情况,不会试图使用行动不能的从者的宝具,并更合理地选择指令卡  
说明:魅惑导致的行动不能的图标好像是不一样的,等实战遇到了再处理  
bug修复:增加了部分延时  
另:把所有模板的位深度都改为了24,删除了以后不会再用的图片  
另:明确了战斗函数的管辖范围  
## 2020/01/14 v2.10.1  
新:向代码中增加播放声音的功能,现在一旦脚本停止运行就会播放战歌  
说明:为什么不用pygame或者playsound呢?pygame音质奇差,playsound已经不更新了  
无限池最高效率本开启前几个小时发布此更新,就是为了牺牲睡眠质量保证24小时不断肝  
## 2020/01/13 v2.10.0  
bug修复:代码重构带来了一些后续的麻烦...但降低一点内聚性总是好的  
优化:现在这个脚本可以用于任意分辨率的16:9的模拟器显示画面了  
## 2020/01/13 v2.9.0  
代码重构,无实质性变化  
把所有(依赖于adb的)底层交互接口放到了一个新文件里,如果要换平台应用脚本,只要更改新文件里面的内容就行了  
看了一波下来突然发现我的脚本封装的是真滴好,只有三个函数和少数变量是跟fgo运行所在平台相关的,他们是:  
`tap`,`swipe`,`screenShot`(已弃用)  
并且对于当前版本的脚本,你几乎用不到`chooseFrined`函数,截图识别也跟adb无关,也就是说,你甚至可以不写`swipe`和`screenShot`函数,因为在所有其他地方都没有使用这两个函数,就是不停地点点点  
我要不要再把所有依赖Windows的函数也搞个文件放着呢?应该没有人吃了空用Linux打fgo吧...<del>mac?那是什么我不知道</del>
## 2020/01/12 v2.8.8  
bug修复:现在在战斗结束时如果提示加好友会更稳定地拒绝  
说明:此前版本中由于点击时机不精确有可能导致卡在加好友界面  
## 2020/01/12 v2.8.7  
重大bug修复:现在每截一次图就会释放在调用win32api时分配的内存  
说明:在此前的版本中进行大约9场battle就会占用大约8G内存进而导致截图中的某一步分配内存失败,  因此所有使用v2.8.x版本的用户都应该立刻安装此更新  
果然,珍爱生命,远离win32api  
## 2020/01/11 v2.8.6
优化:现在在好友选择界面发现没有好友时(多半是由于使用了过于严苛的筛选条件导致的),会刷新一次好友列表,再发现列表为空才会GG  
优化:`chooseFriend`函数现在不会无止境地找好友,最多识别`Fuse.__max`(默认300)个页面
## 2020/01/09 v2.8.5  
延时调整  
## 2020/01/09 v2.8.4  
bug修复:现在不会试图使用被封印的宝具  
对于这个bug的修复可能有bug  
## 2020/01/09 v2.8.3  
期末考结束了...  
稳定性大优化  
全面修订readme  
## 2020/01/08 v2.8.2  
截图从<某个已经消失的版本>的qt改回win32api了...  
修改了一些判定的模板图片  
由于截图效率的提高,正在尝试用多帧来进行一次判定来提高可靠性,比如houguinfo  
## 2020/01/08 v2.8.0  
稳定性优化  
肝!
## 2020/01/07 v2.8.0beta  
紧急更新  
本次更新内容可靠性未经充分验证,请谨慎下载使用  
使用了win32api代替之前的adb进行截图,单次截图时间从1s级别减低到了10ms级别  
这段代码是不带裁剪和缩放的,所以**需要模拟器在正好1920\*1080的显示器上全屏显示,真机的话要用投屏软件**  
由于之前的代码有一些地方是依赖截图的耗时来进行延迟的,这一延迟消失后可能引发各种各样的问题,所以我正在一点一点地在必要的地方加上显式延迟,但是仍然会有疏漏,之后发现一个解决一个,慢慢改  
## 2020/01/03 v2.7.0  
打版本日志的时候突然发现已经2020年了...期末考好累...  
圣诞活动7号晚上开始,但是期末考9号才结束...  
所以复习放一边去,先把脚本给写了  
重大bug修复,带指向的技能现在会正确地施放了(尽管识别错误的问题仍然存在)  
微调了部分按键坐标,**现在你可以吃银苹果和铜苹果了**  
小优化,切换目标后加了冗余点击以关闭在点击已选中目标时产生的敌人详情对话框  
增加了所谓"快速换装(setSkillInfo)"函数,**先把配置写好,然后活动一开就上号挂机岂不美哉**!  
flag:我圣诞要吃光苹果,当前金苹果当量287  
## 2019/11/26 v2.6.0
蓝叠模拟器更到最新版就不会闪退了  
chooseFriend函数还是挺重要的,要用来选取特定从者  
明天(2019年11月27日星期三)上午8:30通关主线第8话(前篇)后开启炎舞击退战,
增加了一小段代码用于otk,现在直接运行脚本就是单次执行该脚本  
这段代码专用于"三美少女队",如果你没有bba/cba中的任何一个,或嫖不到cba,告辞.  
需要极地迦勒底制服  
**本次活动特攻是"特殊的魔放",会稀释其他的倍率,可恶!**  
## 2019/11/10 v2.5.2
版本更新后蓝叠模拟器闪退,在物理机上的兼容性未发现显著问题.  
版本更新后可以对助战礼装进行筛选,chooseFriend函数变得不再重要,已在主程序中禁用.  
