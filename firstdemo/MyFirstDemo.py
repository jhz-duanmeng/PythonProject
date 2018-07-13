import time

print("你好")

print(1 + 1)
print('a')
print(""" 三个引号 """)

if True:
    print("Answer")
    print("true")

else:
    print("Answer")
    print("false")

# 注释 这是第一行代码

'''这是多行注释，使用单引号'''
"""
这是多行注释，使用双引号

"""

print("Kobe" + " " + "Bryant")
print("Kobe" + "." + "Bryant")
print("Kobe", "Bryant")

print("Kobe %s %s" % ("Bryant", "Man"))
print("Kobe %s %s %s %s" % ("Bryant", "is", "a", "BasketBallPlayer"))
print("Kobe %s %s %s %50s" % ("Bryant", "is", "a", "BasketBallPlayer"))

m = 1
n = 2
print("百分号d的用法 %d.%d" % (m, n))

print(type(1))
print(type(""))
print(type(1.0))
print(type(1j))  # 虚数
print(type(1.0 + 1j))
print(type(999 + 1j))
print(999 + 2j)

print("$%.1f " % 30.00163)
print("$%.0f " % 30.00163)
print("%.2f" % 30.000163)

print(169 + 4515)
print(1566 - 450.266)
print(20 * 10)
print(30 / 10)
print(30 % 12)

print("%f" % (5 / 3))
print("%.2f" % (5 / 3))
print(5 * (8 - 3 + 1.0))
print(5 * (8 - 3 + 1.0) / 12)

a = 10
b = 20
lists = [1, 2, 3, 4, 5, 6]
if (a in lists):
    print("a 在list中")
else:
    print("a 不在list中")

name = -1
if (name == 2):
    print("boss")

elif (name == 3):
    print("user")
elif (name < 1):
    print("false")
else:
    print('roadom')

num = [8, 10, 37, 5, 3, 9, 18]
yes = []
no = []
n = 0
while len(num) > 0:
    nums = num.pop()
    if nums % 2 == 0:
        yes.append(nums)
        print("The count yes is ", yes)
    else:
        no.append(nums)
        print("The count no is ", no)

# 无限循环
# var = 1
# while (var == 1):
#     numbers = input("Enter a number：")
#     print("you entered:", numbers)

"""while 语句时还有另外两个重要的命令 continue，break 来跳过循环，
continue 用于跳过该次循环，break 则是用于退出循环，
此外"判断条件"还可以是个常值，表示循环必定成立，具体用法如下："""
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print(i)

j = 1
while 1:
    print(j)
    j += 1
    if j > 10:
        print("跳出循环")
        break

count = 0
while count < 5:
    print(count, "is less than 5")
    count += 1
else:
    print(count, "is not less than 5")

for letter in 'PYTHON':
    print("当前字母：", letter)

fruit = ["apple", "banana", "orange", "water melon", "peach", "pear", "grape", "cherry", "mango"]
for fruits in fruit:
    print("当前水果", fruits)

fruited = ['banana', 'apple', 'mango']
for index in range(len(fruited)):
    print('索引 当前水果 :', fruited[index])

for num in range(9, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print(num, '是一个质数')

# 循环嵌套
ia = 2
while ia < 100:
    js = 2
    while js <= (ia / js):
        if not (ia % js):
            break
        js = js + 1
    if js > ia / js:
        print(ia, " 是素数")
    ia = ia + 1
print("\n")

# continue 语句是一个删除的效果，他的存在是为了删除满足循环条件下的某些不需要的成分:
var = 10

while var > 0:
    var = var - 1
    if var == 5 or var == 8:
        continue
    print('当前值 :', var)
print("\n")

n1 = 0
while n1 < 10:
    n1 = n1 + 1
    if n1 % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n1)

for letter in 'Python':
    if letter == 'h':
        pass
        print('这是 pass 块')
    print('当前字母 :', letter)

# del语句删除单个或多个对象
var1 = 12
var_a = 1
var_b = 2
del var1
del var_a, var_b

# 更新列表
listed = []
listed.append("nihao")
listed.append("nidaye")
print(listed)

# 删除列表元素
list1 = ['physics', 'chemistry', 1997, 2000]
print(list1)
del list1[2]
print("After deleting value at index 2 : ")
print(list1)

# 修改字典
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8  # update existing entry
dict['School'] = "DPS School"  # Add new entry

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

# 删除字典元素
del dict['Name']  # 删除键是'Name'的条目
# dict.clear()  # 清空词典所有条目
# del dict  # 删除词典



print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])






















