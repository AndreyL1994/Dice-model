from random import randint


class Dice():
    """Модель кубика"""
    def __init__(self, sides=int(input("Number of Dice's sides?(6 or 8)\n"))):
        """Инициализирует количество сторон кубика."""
        self.sides = sides

    def roll_dice(self):
        """Моделирует бросок кубика"""
        return randint(1, self.sides)


throw = Dice()

if throw.sides == 6 or throw.sides == 8:
    rolls = int(input("Number of rolls = ?\n"))
    for i in range(rolls):
        print(throw.roll_dice())
else:
    print('Dice can only have 6 or 8 sides')
