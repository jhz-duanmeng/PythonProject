"""关键字参数"""


# 可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print("Name: ", name)
    print("Age ", age)
    return


printinfo("大卫", 20)
print("\n")
printinfo(age="19", name="李雷")

"""缺省参数"""


# 可写函数说明
def printinfos(name, age=35):
    "打印任何传入的字符串"
    print("\nName: ", name)
    print("Age ", age)
    return


printinfos(age=50, name="miki")
printinfos(name="黎明")

"""不定长参数
    ** 加了星号（*）的变量名会存放所有未命名的变量参数
"""


def printinfoS(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


printinfoS(98)
printinfoS(78, 15, 689, 978, 55)

"""匿名函数"""

sum = lambda arg1, arg2: arg1 * arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))

print("相加后的值为 : ", sum(20, 20))


# return
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


sum(10, 50)

# 全局变量与局部变量

localtotle = 0


def totle(arg1, arg2):
    localtotle = arg1 + arg2
    print("局部变量：", localtotle)
    return localtotle


totle(20, 90)
print("全局变量：", localtotle)
