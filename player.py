class player:

    def __init__(self,pseudo,cashstart):
        self.pseudo = pseudo
        self.money = cashstart
        self.handcards = []
        self.handvalue = 0

    def addcash(self,amount):
        self.money += amount

    def display(self):
        print("Pseudo: {} Money: {} $".format(self.pseudo,self.money))


if __name__ == "__main__":
    p1 = player('Thomas',12000)
    p1.display()
    p1.addcash(5000)
    p1.display()