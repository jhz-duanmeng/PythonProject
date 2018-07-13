age = 200
if age < 2 and age >= 0:
	print("This is a baby")
elif age >= 2 and age <4:
	print("it learn how to walking")
elif age >=4 and age <13:
	print("he is a boy")
elif age >=13 and age <20:
	print("he is a young")
elif age>=20 and age<65:
	print('he is a adult')
elif age>=65 and age <150:
	print("he is a old man")
elif age < 0 or age > 150:
	print("he is not stay in the world ,the age is "+ str(age))
else:
	print("thank you")
	
	
	
	
