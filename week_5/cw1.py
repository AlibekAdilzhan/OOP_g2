class University:
    def __init__(self, name, rating, year):
        self.name = name
        self.__rating = rating
        self.year = year

    def get_rating(self):
        return f"this unver's rating is {self.__rating}"

    def set_rating(self, new_rating):
        self.__rating = new_rating
        print("rating was changed!")

    rating = property(get_rating, set_rating)


u1 = University("au", 5, 1804)
print(u1.rating)
u1.rating = 10
print(u1.rating)