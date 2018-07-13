a = {"color":"green","points":5}
print(a["color"])
print(a["points"])

points = a["points"]
print("You just earned " + str(points) + " points!")

a["kind"] = "MARS"
a["star"] = "mars"
print(a)

b = {}
b["kind"] = "human"
b["size"] = 50
print(b)

b["kind"] = "mars"
print("now ",b)

alient = {"x":0,"y":25,"speed":"speed"}
print("old position:" + str(alient["x"]))
if alient["speed"] == "slow":
	x = 1
elif alient["speed"] == "medium":
	x = 2
else:
	x = 3
alient["x"] = alient["x"] + x
print("new position:" + str(alient["x"]))

user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key,value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

#使用集合取字典中的值
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())








