"""
Python中的包

包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。

简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。__init__.py 用于标识当前文件夹是一个包。
"""

# import testpackage.supportutils as p
# from supportutils import *
import testpackage.supportutils
testpackage.supportutils.print_func("fdf")
# p.print_func("fdf")
# print_func("fdf")


# import math

# Money = 2000
#
# def AddMoney():
#     # 想改正代码就取消以下注释:
#     global Money
#     Money = Money + 1
#
#
#
# print(Money)
# AddMoney()
# print(Money)
#
# content = dir(math)
# print(content)


"""如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。

如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。

两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。"""



"""
reload() 函数

当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。

因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。该函数会重新导入之前导入过的模块。语法如下：

reload(module_name)"""









