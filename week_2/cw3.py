from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        print(self.a * self.b)

    def perimeter(self):
        print((self.a + self.b) * 2)

rect1 = Rectangle(2, 4)
rect1.area()
rect1.perimeter()