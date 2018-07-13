new_list = []
new_list.append("China")
new_list.append("America")
new_list.append("Janpan")
new_list.append("Australia")
print(new_list)

new_list.remove("Janpan")
print(new_list)

too_faraway = 'America'
new_list.remove(too_faraway)
print("\nThe " + too_faraway.title() + " is too far away to me.")
