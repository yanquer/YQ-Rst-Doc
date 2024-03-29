==========================
objdump
==========================

参考:

- https://zhuanlan.zhihu.com/p/115834125
- https://blog.csdn.net/wwchao2012/article/details/79980514

显示二进制文件信息

用来显示一个或者多个目标文件的信息, 可以是静态库归档文件.

语法::

  objdump [选项] objfile...

选项:

--archive-headers, -a       显示档案库的成员信息,类似 ls -l 将 lib*.a 的信息列出。
-b bfdname, --target=bfdname
                            指定目标码格式。
                            这不是必须的， objdump 能自动识别许多格式，比如：
                            $objdump -b oasys -m vax -h fu.o
                            显示 fu.o 的头部摘要信息，明确指出该文件是 Vax 系统下用 Oasys 编译器生成的目标文件。
                            objdump -i 将给出这里可以指定的目标码格式列表。
-C, --demangle              将底层的符号名解码成用户级名字，除了去掉所开头的下划线之外，
                            还使得C++函数名以可理解的方式显示出来。
--debugging, -g             显示调试信息。企图解析保存在文件中的调试信息并以C语言的语法显示出来。
                            仅仅支持某些类型的调试信息。有些其他的格式被 readelf -w 支持。
-e, --debugging-tags        类似 -g 选项，但是生成的信息是和 ctags 工具相兼容的格式。
--disassemble, -d           从 objfile 中反汇编那些特定指令机器码的 section 。
-D, --disassemble-all       与 -d 类似，但反汇编所有 section.
--prefix-addresses          反汇编的时候，显示每一行的完整地址。这是一种比较老的反汇编格式
-EB, -EL, --endian=<big|little>
                            指定目标文件的小端。这个项将影响反汇编出来的指令。
                            在反汇编的文件没描述小端信息的时候用。
                            例如 S-records 。
-f, --file-headers          显示 objfile 中每个文件的整体头部摘要信息
-h, --section-headers, --headers
                            显示目标文件各个 section 的头部摘要信息。
-H, --help                  简短的帮助信息。
-i, --info                  显示对于 -b 或者 -m 选项可用的架构和目标格式列表。
-j name, --section=name     仅仅显示指定名称为 name 的 section 的信息
-l, --line-numbers          用文件名和行号标注相应的目标代码，仅仅和 -d 、 -D 或者 -r 一起使用使用 -ld 和使用 -d 的区别不是很大，
                            在源码级调试的时候有用，要求编译时使用了 -g 之类的调试编译选项。
-m machine, --architecture=machine
                            指定反汇编目标文件时使用的架构，当待反汇编文件本身没描述架构信息的时候(比如 S-records )，
                            这个选项很有用。可以用 -i 选项列出这里能够指定的架构.
--reloc, -r                 显示文件的重定位入口。如果和 -d 或者 -D 一起使用，重定位部分以反汇编后的格式显示出来。
--dynamic-reloc, -R         显示文件的动态重定位入口，仅仅对于动态目标文件意义，比如某些共享库。
-s, --full-contents         显示指定 section 的完整内容。默认所有的非空 section 都会被显示。
-S, --source                尽可能反汇编出源代码，尤其当编译的时候指定了 -g 这种调试参数时，效果比较明显。隐含了 -d 参数。
--show-raw-insn             反汇编的时候，显示每条汇编指令对应的机器码，如不指定 --prefix-addresses ，这将是缺省选项。
--no-show-raw-insn          反汇编时，不显示汇编指令的机器码，如不指定 --prefix-addresses ，这将是缺省选项。
--start-address=address     从指定地址开始显示数据，该选项影响 -d 、 -r 和 -s 选项的输出。
--stop-address=address      显示数据直到指定地址为止，该项影响 -d 、 -r 和 -s 选项的输出。
-t, --syms                  显示文件的符号表入口。类似于 nm -s 提供的信息
-T, --dynamic-syms          显示文件的动态符号表入口，仅仅对动态目标文件意义，比如某些共享库。
                            它显示的信息类似于 nm -D|--dynamic 显示的信息。
-V, --version               版本信息
--all-headers, -x           显示所可用的头信息，包括符号表、重定位入口。 -x 等价于 -a -f -h -r -t 同时指定。
-z, --disassemble-zeroes    一般反汇编输出将省略大块的零，该选项使得这些零块也被反汇编。

@file 可以将选项集中到一个文件中，然后使用这个 @file 选项载入。


