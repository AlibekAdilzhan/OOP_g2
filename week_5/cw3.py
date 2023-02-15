class University:
    def __init__(self, name, rating, year):
        self.name = name
        self.__rating = rating
        self.year = year

    @property
    def rating(self):
        return f"this unver's rating is {self.__rating}"

    @rating.setter
    def rating(self, new_rating):
        raise AttributeError("you cant change this attribute")


u1 = University("au", 5, 1804)
print(u1.rating)
u1.rating = 10