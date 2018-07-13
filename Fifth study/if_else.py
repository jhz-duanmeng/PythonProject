cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == "bmw":
		print(car.upper())
	else:
		print(car.title())

age0 = 18
age1 = 22
if age0 >=20 and age1 >=22:
	print("This is right")
else:
	print("This is wrong")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if "mushrooms" in requested_toppings:
	print("Yes")
else:
	print("no")

if "mushroom" not in requested_toppings:
	print("Yes")
else:
	print("no")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print(car.lower() == "subaru")

age = 12
if age <4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")
	

ages = 12
if ages <4:
	price = 0
elif ages <18:
	price = 5
elif ages < 65:
	price = 10
else:
	price = 5
print("Your admission cost is $" + str(price) + ".")

alien_color = ["green","yellow","red"]
if "green" in alien_color:
	points = 10
	print("green is in the color,get " + str(points))
else:
	points = 5
	print("green not in the color,get " + str(points))












