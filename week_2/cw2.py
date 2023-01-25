class Animal:
    def __init__(self, food, location):
        self.food = food
        self.location = location

    def make_noise(self):
        print("animal is making noise")

    def eat(self):
        print("animal is eating")

    def sleep(self):
        print("animal is sleeping")


class Dog(Animal):
    def __init__(self, name, food, location):
        super().__init__(food, location)
        self.name = name

    def make_noise(self):
        print(self.name, "is barking")


class Cat(Animal):
    def __init__(self, name, food, location):
        super().__init__(food, location)
        self.name = name

    def make_noise(self):
        print(self.name, "is meowing")



class Vet:
    def treat_animal(self, animal):
        print(animal.food, animal.location)

d1 = Dog("Tuzik", "korm", "home")
d2 = Dog("Lastik", "meat", "butka")
d3 = Dog("Aqtos", "banan", "penthouse")

c1 = Cat("Barsik", "wiskas", "home")
c2 = Cat("Felix", "katicat", "butka")
c3 = Cat("Barsik3", "mouse", "home")

v = Vet()
animals_list = [d1, d2, d3, c1, c2, c3]



for animal in animals_list:
    v.treat_animal(animal)
