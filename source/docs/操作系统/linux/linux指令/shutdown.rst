================================
shutdown
================================

shutdown 会给系统计划一个时间关机。它可以被用于停止、关机、重启机器。shutdown 会给系统计划一个时间关机。
它可以被用于停止、关机、重启机器。

关闭机器::

  shutdown -p now

停止机器::

  shutdown -H now

在 09:35am 重启机器::

  shutdown -r 09:35

要取消即将进行的关机，只要输入下面的命令::

  shutdown -c


