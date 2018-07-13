import json

file_name = "numbers.json"
with open(file_name) as obj:
    numbers = json.load(obj)

print(numbers)
