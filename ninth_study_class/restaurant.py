class Restaurant:
    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    def describe_restaurant(self):
        print("This restaurant's name is " + self.restaurant_name.title() + " , it is a " + self.restaurant_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is opening now!")


my = Restaurant("lianjia", "hotel")
my.describe_restaurant()
my.open_restaurant()

your = Restaurant("woaiwojia", "hotel")
your.describe_restaurant()
your.open_restaurant()
