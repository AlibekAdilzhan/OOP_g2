class FastFood:
    def __init__(self, name, price, kal):
        self.name = name
        self.price = price
        self.kal = kal

    def sell(self):
        # print(self.name, "was sold for", self.price, "tg")
        print(f"{self.name} was sold for {self.price} tenge")

    def good_reaction(self):
        print("mmmm, delicious fast food!")


class Burger(FastFood):
    def __init__(self, name, price, kal, cutlet_number):
        # FastFood.__init__(name, price, kal)
        super().__init__(name, price, kal)
        self.cutlet_number = cutlet_number

    def add_cutlet(self, cut_num=1):
        self.cutlet_number += cut_num

    def good_reaction(self):
        print("mmmm, delicious burger!")



ff1 = FastFood("burger", 1000, 700)
b1 = Burger("cheeseburger", 800, 600, 2)
b1.good_reaction()