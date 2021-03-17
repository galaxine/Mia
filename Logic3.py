from CubeCup import CubeCup
from Player import Player


class Logic3:
    # we can record the round
    # we need to know whose turn it is
    # we need to find out if the first player
    # we need to creat a list of
    # players
    # dices thrown
    # dices announced
    # we need methods:
    # players can't have the same name
    # players need to be put into a list
    # order the dices
    # compare the dices
    # record the rounds, we don't actually need
    # this and the setters and getters
    __round = 0
    # check whose turn it is and use it to get the dices appended
    # after dices have been thrown
    __turn = 0
    # first player of the round:
    __firstPlayer = True
    # list of points
    __points = []
    # list of players
    __players = []
    # list of dices thrown as tuples
    __dices = []
    # list of announcements made instead of the dices.
    # if the player threw the dice and said the truth, this one is
    # also added into the list to compare with __turn
    __announcements = []
    __cubeCup = None

    # definitely need a list for points to get and set
    def getPoints(self):
        return self.__points

    def setPoints(self, point):
        self.__points.append(point)

    # we can keep the round, if we need it
    # but this makes no sense anymore to use.

    # get the current turn of player, used to access dices,
    # announcements, players:
    def getTurn(self):
        return self.__turn

    # not sure if we need this
    def setTurn(self, newTurn):
        self.__turn = newTurn

    # get the currentplayers of the game
    def getPlayers(self):
        return self.__players

    # set new Players into the game, also appends
    # values already for other lists to keep homogenous size
    def setPlayes(self, name):
        player = Player()
        player.setName(name)
        self.__players.append(player)
        self.setPoints(0)
        self.setDices((0, 0))
        self.setAnnouncements((0, 0))

    # adds the announcement of the currentplayer into the list
    def setAnnouncements(self, newAnnouncements):
        self.__announcements.append(newAnnouncements)

    # get the announced dices, we can use the index later to find the
    # correct element
    def getAnnouncements(self):
        return self.__announcements

    # set a cubecup object, this class needs one
    def setCubeCup(self, cubeCup):
        self.__cubeCup = cubeCup

    # get the CubeCup object in this class
    def getCubeCup(self):
        return self.__cubeCup

    # we get the dicesList
    def getDices(self):
        return self.__dices

    # we can set the dices here
    def setDices(self, newDices):
        self.__dices.append(newDices)

    # get the dice from the cubecup object and return it ordered
    def orderDices(self, tuples):
        diceA = tuples[0]
        diceB = tuples[1]

        if diceA > diceB:
            return (diceA, diceB)
        else:
            return (diceB, diceA)

    # get the shaken dice:
    def getThrownDices(self):
        # shake the cup
        self.getCubeCup().shakeCubeCup()
        # get the tuple and return it
        return self.getCubeCup().showDicesInsideCup()

    # we can change the tuple in the list by accessing the turn
    def changeDicesList(self, currentDice):
        print(self.getTurn())
        self.getDices()[self.getTurn()] = currentDice

    # same for the tuples in the announcemenlist, accessed by turn
    def changeAnnouncementsList(self, lies):
        self.getAnnouncements()[self.getTurn()] = lies

    # find out if this is the First Player starting the round:
    def isItFirstPlayer(self):
        return self.__firstPlayer

    # switch it everytime after player one and after
    # the turn incremented above 0
    def switchFirstPlayer(self):
        if self.isItFirstPlayer():
            self.__firstPlayer = False
        else:
            self.__firstPlayer = True

    # compare the dices. 1 for a > b, 2 for a < b, 3 for a = b
    def compareDices(self, tuple1, tuple2):
        if tuple1 > tuple2:
            return 1
        elif tuple1 < tuple2:
            return 2
        else:
            return 3

    def nullAnnouncementsAndDices(self):
        self.__dices.clear()
        self.__announcements.clear()
        for i in self.__players:
            self.setDices((0,0))
            self.setAnnouncements((0,0))
    # 21 is greatest, followed by 66,55,44,33,22,11, then by the other shit
    def checkDiceValues(self, tuple1):
        if tuple1 == (2, 1):
            return 99
        elif tuple == (6, 6):
            return 98
        elif tuple == (5, 5):
            return 96
        elif tuple == (4, 4):
            return 95
        elif tuple == (3, 3):
            return 94
        elif tuple == (2, 2):
            return 93
        elif tuple == (1, 1):
            return 92
        elif tuple == (6, 5):
            return 88
        elif tuple == (6, 4):
            return 87
        elif tuple == (6, 3):
            return 86
        elif tuple == (6, 2):
            return 85
        elif tuple == (6, 1):
            return 84
        elif tuple == (5, 4):
            return 83
        elif tuple == (5, 3):
            return 82
        elif tuple == (5, 2):
            return 81
        elif tuple == (5, 1):
            return 80
        elif tuple == (4, 3):
            return 79
        elif tuple == (4, 2):
            return 78
        elif tuple == (4, 1):
            return 77
        elif tuple == (3, 2):
            return 76
        elif tuple == (3, 1):
            return 75
        else:
            print("SOMETHING WENT WRONG")

    def lie(self):
        print("tell the first dice between 1 to 6: ")
        diceA = int(input())
        print("tell me the second dice between 1 to 6: ")
        diceB = int(input())
        # order the input and put it inside the announcements
        orderedLie = self.orderDices((diceA, diceB))
        self.changeAnnouncementsList(orderedLie)
        # show me the announcementList
        print(self.getAnnouncements())
        # Announce that the player rolled the dices:
        print(
            f"Player {self.getPlayers()[self.getTurn()]} rolled a {self.getAnnouncements()[self.getTurn()]}."
        )

    def truth(self):
        # also add the lie into the announcementList, to later check if it was correct
        self.changeAnnouncementsList(self.getDices()[self.getTurn()])
        print(
            f"Player {self.getPlayers()[self.getTurn()]} rolled a {self.getDices()[self.getTurn()]}."
        )

    def judge(self):
        print("You want to find out if the player lied: ")
        # previous Player lied?
        # if equal =3, current player -1, previous player +2
        if (
            self.compareDices(
                self.getDices()[self.getTurn() - 1],
                self.getAnnouncements()[self.getTurn() - 1],
            )
            == 3
        ):
            # the previous player told the truth
            print(
                "The previous player didn't lie, the current Player loses one life, previous gains one"
            )
            # the previous player gets a point, the current one loses it
            self.getPoints()[self.getTurn()] -= 1
            self.getPoints()[self.getTurn() - 1] += 1
            # the previous player lied and the current player was right.
            # BUT
        elif (
            not self.compareDices(
                self.getDices()[self.getTurn() - 1],
                self.getAnnouncements()[self.getTurn() - 1],
            )
            == 3
        ):
            # the previous player has still a higher dice:
            if self.checkDiceValues(
                self.getDices()[self.getTurn() - 1]
            ) > self.checkDiceValues(self.getDices()[self.getTurn()]):
                print(
                    "previous player still rolled a higher dice than the current player!"
                )
                # current player loses a life
                self.getPoints()[self.getTurn()] -= 1
                self.getPoints()[self.getTurn() - 1] += 1
            # the plaayer has rolled a lower value:
            else:
                print(
                    "previous player rolled lower, it loses a point, current Player wins a point "
                )
                self.getPoints()[self.getTurn()] += 1
                self.getPoints()[self.getTurn() - 1] -= 1

    # ----------------------------------------- needs to be dealt with --------------------------------------
    def startGame(self):
        dice = self.getThrownDices()
        print(dice)
        orderdice = self.orderDices(dice)
        self.changeDicesList(orderdice)
        if self.isItFirstPlayer():
            print(f"firstPlayer is {self.getPlayers()[self.getTurn()]}")
            # switch off the firstplayer when inside the firstplayer menu
            self.switchFirstPlayer()
            # tell the player what they rolled:
            print(
                f"You rolled a {self.getDices()[self.getTurn()]}. You can lie"
                + " or tell the truth"
            )
            # get an iput
            command = input()
            if command == "lie":
                self.lie()
            elif command == "truth":
                self.truth()
            self.setTurn(self.getTurn() + 1)
        # ----------------------------------------------------------------- after first player ---------------------------------------------------------------
        # you can either roll higher than announced
        # or lower and equal or
        else:
            print("hi")
            print(f"It is now {self.getPlayers()[self.getTurn()]}'s turn")
            # compare the previous Player's dice
            # if the dice before is greater, it is True:
            if (
                self.compareDices(
                    self.getAnnouncements()[self.getTurn() - 1],
                    self.getDices()[self.getTurn()],
                )
                == 1
            ):
                print(
                    f"the player {self.getPlayers()[self.getTurn()]} rolled higher, you have to lie, or judge it"
                )
                command = input()
                if command == "lie":
                    self.lie()
                elif command == "truth":
                    self.judge()
                    # delete the dice and announcement values, then increment the turn value
                    self.nullAnnouncementsAndDices()
                    self.setTurn(self.getTurn() + 1)
                    self.switchFirstPlayer()
                    # there is a bug for order, but i can't give a fuck about it.
                    if self.getTurn() == len(self.getPlayers()):
                        self.setTurn(0)
            else:
                print(
                    f"the player {self.getPlayers()[self.getTurn()]} rolled lower, you can lie, or judge him if he said the truth"
                )
                command = input()
                if command == "lie":
                    self.lie()
                    # increment the round
                    self.setTurn(self.getTurn() + 1)

                if command == "truth":
                    self.truth()
                    self.setTurn(self.getTurn() + 1)
                if command == "judge":
                    self.judge()
                    self.nullAnnouncementsAndDices()
                    self.setTurn(self.getTurn() + 1)
                    self.switchFirstPlayer()
                    # there is a bug for order, but i can't give a fuck about it.
                    if self.getTurn() == len(self.getPlayers()):
                        self.setTurn(0)
        print(self.getPoints())
        print(self.getAnnouncements())
        print(self.getDices())
        print(self.getTurn())

    # TODO: First take the cubeCup and create a few rolls
    # TEST BELOW:


# %%
# initialize the objects
cup = CubeCup()
game = Logic3()
# insert the cup into the LogicBoard
game.setCubeCup(cup)
# set the dices and the sides, here 2 dices, six sides each
game.getCubeCup().setNumberOfDices(2, 6)
# insert a few players.
game.setPlayes("Korelius")
game.setPlayes("Anton")
game.setPlayes("Nimbus")
# ----------------------------------------Game Starts------------------------------------
# EVERY player gets through this step
#
while True:
    game.startGame()
