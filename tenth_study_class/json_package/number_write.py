import json

numbers = [2, 3, 5, 7, 11, 13]

# filename = "numbers.json"
filename = "numbers.txt"
with open(filename, "w") as obj:
    json.dump(numbers, obj)

