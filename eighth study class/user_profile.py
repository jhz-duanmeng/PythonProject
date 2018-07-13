
def build_info(first, last, **user_info):
    """创建一个字典， 其中包含我们知道的有关用户的一切"""
    profile = {"first": first, "last": last}

    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_info("kobe", "bryant", location="America", city="Los Angeles")
print(user_profile)
