===========================
cursor
===========================

cursor 用于指定鼠标指针在元素上的外观。
通过设置 cursor 属性，你可以改变用户与特定元素交互时鼠标指针的样式，以提供视觉反馈或指示元素的可操作性。

cursor 属性的值可以是以下之一：

预定义光标

- pointer（手型光标，表示链接或可点击元素）
- default（默认光标）
- text（文本输入光标）等。

CSS 光标值（Cursor values）

- 通过指定一个 URL，使用自定义图像作为光标。
  使用名为 "cursor.png" 的图像作为光标，
  并设置 auto 作为回退值（如果图像无法加载，则使用默认光标）::

    cursor: url(cursor.png), auto;

系统光标:
cursor 属性还支持指定系统光标样式，如 crosshair（十字线）、help（帮助光标）、move（移动光标）等。
这些样式会根据操作系统和浏览器的不同而有所变化::

  cursor: crosshair;

