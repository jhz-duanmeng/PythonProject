pizzas = ["fruit","beef","pork","fish"]
for pizza in pizzas:
	print(pizza)
	print("I like this pizza: " + pizza)
print("I really like pizzas")

for values in range(1,5):
	print(values)

numbers = list(range(1,5))
print(numbers)

#range() 从2开始数， 然后不断地加2， 直到达到或超过终值（11） 
event_number = list(range(2,11,2))
print(event_number)

squares = []
for value in range(1,11):
	square = value ** 2
	squares.append(square)
print(squares)

squaress = [value**2 for value in range(1,11)]
print(squaress)


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))





