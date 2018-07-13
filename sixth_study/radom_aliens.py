# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(0,30):
	new_alien = {"color":"green","points":5,"speed":"slow","num":str(alien_number)}
	aliens.append(new_alien)


# 第8-12个外星人	变厉害了
for alien in aliens[7:13]:
	if alien["color"] == "green":
		alien["color"] == "yellow"
		alien["speed"] == "medium"
		alien["points"] == 10

for alien in aliens:
	print(alien)
