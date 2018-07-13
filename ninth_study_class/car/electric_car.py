from car1 import Car


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
