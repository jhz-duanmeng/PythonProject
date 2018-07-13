class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # TODO 1.指定默认值
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    # TODO 3.通过方法属性修改值
    # def update_odometer(self, mile):
    #     self.odometer_reading = mile

    # TODO 3.针对3的方法进行扩展
    def update_odometer(self, mile):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mile >= self.odometer_reading:
            self.odometer_reading = mile
        else:
            print("You can't roll back an odometer!")

    # TODO 4.对属性值进行递增
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

    # 子类会重写父类的该方法
    def repeat_write(self):
        print("The Father method")


# TODO 继承自父类
class ElectricCar(Car):
    """电动汽车的独特之处
        初始化父类的属性， 再初始化电动汽车特有的属性"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# TODO 将实例用作属性
class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery=70):
        self.battery = battery

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery) + "-kWh battery.")

    def get_range(self):
        """打印一条消息， 指出电瓶的续航里程"""
        if self.battery == 70:
            range = 240
        elif self.battery == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery != 85:
            self.battery = 85


# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()