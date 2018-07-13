from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, time):
        while time <= 10:
            self.sides = randint(1, 6)
            print("This sides is " + str(self.sides))
            time += 1


my_sides = Die()
my_sides.roll_die(1)
