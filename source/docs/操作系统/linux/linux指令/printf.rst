=================
printf
=================

功能
=================

不换行打印

使用
=================

.. code-block:: sh
	:caption: 使用天蓝色输出

	printf "\e[1;36;45m%s\e[0m\n" "${_strs}"

拓展--关于使用颜色输出
========================

.. topic:: 颜色输出相关字符说明

	- \\e 转义起始符，定义一个转义序列， 可以使用 \033代替
	- [ 表示开始定义颜色
	- 1表示高亮，36表示字体颜色为天蓝，45表示背景色为红色
	- “_strs” 属于文字内容
	- m 转义终止符，表示颜色定义完毕
	- 再次使用 \e[ ，表示再次开启颜色定义，0表示使用默认的颜色，m表示颜色定义结束，所以 \e[0m 的作用是恢复之前的配色方案

.. topic:: 数字与颜色关系

	.. csv-table:: 字体颜色(前景色): 30-37
		:header: 数字, 颜色

		0,		默认
		30,		黑色
		31,		红色
		32,		绿色
		33,		黄色
		34,		蓝色
		35,		紫色
		36,		天蓝色
		37,		白色

	.. csv-table:: 字背景颜色(后景色): 40-47
		:header: 数字, 颜色

		0,		默认
		40,		黑色
		41,		红色
		42,		绿色
		43,		黄色
		44,		蓝色
		45,		紫色
		46,		天蓝色
		47,		白色

	其他特殊颜色-黑底彩色

	.. csv-table:: 黑底彩色: 90-97
		:header: 数字, 颜色

		90,		黑
		91,		深红
		92,		绿
		93,		黄色
		94,		蓝色
		95,		紫色
		96,		深绿
		97,		白色

	字体控制选项

	.. csv-table:: 字体控制选项
		:header: 代码,

		\\033[0m	,		关闭所有属性
		\\033[1m	,		设置高亮度
		\\033[4m	,		下划线
		\\033[5m	,		闪烁
		\\033[7m	,		反显，撞色显示，显示为白色黑底，或者显示为黑底白字
		\\033[8m	,		消影，字符颜色将会与背景颜色相同
		\\033[nA	,		光标上移n行
		\\033[nB	,		光标下移n行
		\\033[nC	,		光标右移n行
		\\033[nD	,		光标左移n行
		\\033[y;xH	,	设置光标位置
		\\033[2J	,		清屏
		\\033[K	,		清除从光标到行尾的内容
		\\033[s	,		保存光标位置
		\\033[u	,		恢复光标位置
		\\033[?25l	,	隐藏光标
		\\033[?25h	,	显示光标

	另有一个更便捷的命令 :doc:`./tput`

	.. tip::

		echo的 ``\e`` 和 ``\033`` 一个效果