friend = ["yanghaitao","guojinlong","liuzhen","xingyafan","zhangyun"]
print(friend)
friend1 = "Hello,my friend " + friend[0].title()
friend2 = "Hello,my friend " + friend[1].title()
friend3 = "Hello,my friend " + friend[2].title()
friend4 = "Hello,my friend " + friend[3].title()
friend5 = "Hello,my friend " + friend[4].title()
print(friend1)
print(friend2)
print(friend3)
print(friend4)
print(friend5)

friend[0] = "duanmeng"
print(friend)

friend.append("wangyonghui")
print(friend)

new_list = []
new_list.append("China")
new_list.append("America")
new_list.append("Janpan")
new_list.append("Australia")
print(new_list)

new_list.insert(0,"Canada")
print(new_list)

del new_list[0]
print(new_list)

last_country = new_list.pop()
print("The last country is " + last_country.title() + " in the list")

first_country = new_list.pop(0)
print("The first country is " + first_country.title() + " in the list")

new_list.remove("Janpan")
print(new_list)








