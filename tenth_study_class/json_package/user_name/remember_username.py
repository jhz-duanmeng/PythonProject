import json

user_name = input("What is your name? ")
filename = "username.json"
with open(filename, "w") as obj:
    json.dump(user_name, obj)
    print("We'll remember you when you come back, " + user_name + "!")
