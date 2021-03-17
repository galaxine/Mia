class Player:
    # Charaktereigenschaften
    # TODO: Kommentare

    __name = None  # Unviersally, a player has always a name

    def GetName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def __str__(self):
        return f"""name: {self.GetName()}"""
