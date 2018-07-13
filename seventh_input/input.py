# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
#
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
#
# name = input(prompt)
# print("\nHello, " + name + "!")

# age = input("How old are you? ")
# print(age)

height = input("How tall are you, in inches? ")
# 如果不适用int()强制转换为int类型的值，则下面的判断条件会报错
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")


