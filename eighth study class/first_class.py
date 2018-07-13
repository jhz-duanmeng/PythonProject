def get_green(username):
    """显示简单的问候语"""
    print("Hello!", username.title())


get_green("kevin")


def pet(animal_type, animal_name):
    print("I have a " + animal_type + "!")
    print("My " + animal_type + "'s name is " + animal_name.title() + ".")


pet("HaShiQi", "curry")
pet("TaiRiTian", "huanhuan")

"""关键字实参"""


def my_pet(animal_type, animal_name):
    print("I have a " + animal_type + "!")
    print("My " + animal_type.title() + "'s name is " + animal_name.title() + ".")


my_pet(animal_name="gousheng", animal_type="taiRiTian")


def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='willie')
describe_pet(pet_name='willie', animal_type='hamster')


def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


player = get_formatted_name("kvein", "durant")
print(player)


def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


kobe = get_formatted_name("kobe", "bryant")
print(kobe)

ovein = get_formatted_name("kvein", "durant", "curry")
print(ovein)


# 返回字典
def build_person(first_name, last_name):
    """返回一个字典， 其中包含有关一个人的信息"""
    persion = {"first": first_name, "last": last_name}
    return persion


persions = build_person("kobe", "bryant")
print(persions)


def build_persons(first_name, last_name, age=""):
    persion = {"first": first_name, "last": last_name, "age": age}
    if age:
        persion["age"] = age
    return persion


new_persion = build_persons("kobe", "bryant", age="38")
print(new_persion)

new_persion = build_persons("kobe", "bryant")
print(new_persion)

