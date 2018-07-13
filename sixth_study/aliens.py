# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个绿色的外星人
for alien in range(30):
    new_alien = {"color": "green", "speed": "slow", "num": str(alien)}
    aliens.append(new_alien)

for alie in aliens:
    print(alie)

print("Total number of alie: " + str(len(aliens)))
