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

