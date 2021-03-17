from Dice import Dice
import random as r

# notes: die aufgabe des Würfels ist es die Zahlen zu produzieren.
# die Würfel produzieren die Zahlen selber, Becher ruft das Objekt auf über getter


class CubeCup:
    __dices = []

    def shakeCubeCup(self):  # shakeCup or whatever you want to call it
        print("You shake and slam the cup on the table")
        return (self.__dices[0].setDice(), self.__dices[1].setDice())

    def setNumberOfDices(self, dices, sides):
        for i in range(dices):
            dice = Dice()
            dice.setSides(sides)
            self.__dices.append(dice)

    def showDice(self):
        return f"the dice is {self.orderDice()}"

    def GetDice(self):
        return (self.__diceA.getDice(), self.__diceB.getDice())

    def showDice(self):  # you raise the cup either only to yourself or openly
        return f"the dice are {self.orderDice()}"

    # show the two dices, later we can add more values.
    def showDicesInsideCup(self):
        return (self.__dices[0].getDice(), self.__dices[1].getDice())

    def GetMin(self):
        return self.__min

    def GetMax(self):
        return self.__max
