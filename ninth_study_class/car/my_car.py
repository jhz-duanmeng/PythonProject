from car1 import Car
from electric_car import ElectricCar

my_car = Car("audi", "A8", 2018)
# my_car = car2.Car("audi", "A8", 2018)
print(my_car.get_descriptive_name())

my_car.odometer_reading = 30
my_car.read_odometer()

my_new_car = ElectricCar("benz", "a700", 2019)
# my_new_car = car2.ElectricCar("benz", "a700", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.battery.describe_battery()
my_new_car.battery.get_range()
