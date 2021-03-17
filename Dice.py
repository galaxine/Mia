import random as r


class Dice:
    __dice = 0
    __sides = 6 #hardcoded to 6 for now cause we have no place to set the number of sides yet

    def setSides(self, sides):
        self.__sides = sides

    def setDice(self):
        self.__dice = r.randrange(1, self.__sides+1)

    def getDice(self):
        return self.__dice


