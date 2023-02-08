from dataclasses import dataclass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

    def __eq__(self, p2):
        if self.name == p2.name and self.age == p2.age:
            return True
        else:
            return False

@dataclass
class Person:
    name : str
    age : int


p1 = Person("Aaa", 31)
print(p1.name, p1.age)