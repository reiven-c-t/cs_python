from random import randrange

class MSDie:
    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.slide+1)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

die1 = MSDie(6)
die1.getValue