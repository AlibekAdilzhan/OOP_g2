class Vector3:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"{self.a} {self.b} {self.c}"

    def __add__(self, v):
        print("this is first vector", self)
        print("this is the second vector", v)
        new_v = Vector3(self.a + v.a, self.b + v.b, self.c + v.c)
        return new_v

v1 = Vector3(2, 1, 5)
v2 = Vector3(0, 1, 10)
print(v1 + v2)
print(v1.__add__(v2))