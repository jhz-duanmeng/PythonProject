import time
import calendar

# TempConvert.py
# val = input("请输入带有文档符号的温度值（例如：123C）：")
# if val[-1] in ['C', 'c']:
#     f = 1.8 * float(val[0:-1]) + 32
#     print("转换后的温度是：%2fF" % f)
# elif val[-1] in ['F', 'c']:
#     c = (float(val[0:-1]) - 32) / 1.8
#     print("转换后的温度是：%2fC" % c)
# else:
#     print("输入有误")


ticks = time.time()
print("当前时间戳：", ticks)
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%A %B %D %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

cal = calendar.month(2018, 4)
print("以下输出2018年4月份的日历:")
print(cal)


# 可写函数说明
def printMe(names):
    (print(names))
    return


printMe("你好")











