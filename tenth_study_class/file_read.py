print("==============第一种读取方式==================")
with open("papijiang") as file_object:
    contents = file_object.read()
    print(contents)

# s = "sdnasjhdasdaksnfcjdshdfufhaosinfdsjncxkjz"
# print("\n" + str(s.count("s")) + "\n")
print("===============第二种读取方式=================")

with open("papijiang") as file_object:
    for line in file_object:
        print(line.rstrip())

print("==============第三种读取方式==================")

file_name = "papijiang"
with open(file_name) as file_obs:
    lines = file_obs.readlines()

for l in lines:
    print(l.rstrip())

print("============读取文件中内容保存到内存并打印出来（借用第三种读取方式）====================")

pi = ""
for ll in lines:
    pi += ll.rstrip()

print(pi)
print(len(pi))

print("============读取文件中内容保存到内存并打印出来，省略太长的====================")

print(pi[:9] + "...")
print(len(pi))

dic = {}
for counts in pi:
    if counts in dic:
        dic[counts] = dic[counts] + 1
    else:
        dic[counts] = 1
print(dic)

