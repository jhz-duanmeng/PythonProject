# 求模运算符 （%） 是一个很有用的工具， 它将两个数相除并返回余数：
a = 5 % 4
print(a)

a = 5 % 3
print(a)

a = 6 % 3
print(a)

a = 7 % 3
print(a)

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
#
# # 除2 余数是0 则是偶数
# if number % 2 == 0:
#     print("\nThe number " + str(number) + " is even.")
# else:
#     print("\nThe number " + str(number) + " is odd.")

current_number = 1
while current_number < 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)













