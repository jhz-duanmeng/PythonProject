import json

filename = "users.json"
try:
    with open(filename) as obj:
        name = json.load(obj)
except FileNotFoundError:
    with open(filename, "w") as obj:
        name = input("What is your name? ")
        json.dump(name, obj)
        print("We'll remember you when you come back, " + name + "!")
else:
    print("Welcome back, " + name + "!")

