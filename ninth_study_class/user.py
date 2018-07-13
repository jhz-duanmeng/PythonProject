class User:
    def __init__(self, first, last, sex):
        self.first = first
        self.last = last
        self.sex = sex

    def describe_user(self):
        print("The user name is " + self.first + " " + self.last + ", the sex is " + str(self.sex))

    def greet_user(self):
        print("Hello," + self.first.title() + " " + self.last.title() + ",nice to meet you!")


first = User("kobe", "bryant", "male")
first.describe_user()
first.greet_user()

second = User("kevin", "durant", "male")
second.describe_user()
second.greet_user()

third = User("han", "meimei", "female")
third.describe_user()
third.greet_user()

