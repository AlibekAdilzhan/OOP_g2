class Car:
    def __init__(self, eng_volume, prod_year, mark):
        self.__eng_volume = eng_volume
        self.prod_year = prod_year
        self.mark = mark

    def get_volume(self):
        return self.__eng_volume



car1 = Car(3.8, 2007, "BMW")
print(car1.get_volume())