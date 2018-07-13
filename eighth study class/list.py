def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


users_list = ["郭金龙", "邢亚凡", "张芸", "杨海涛", "刘振"]
greet_users(users_list)

