import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

    def perimeter(self):
        return 2 * math.pi * self.r

class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s * self.s

    def perimeter(self):
        return 4 * self.s

class Triangle(Shape):
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def area(self):
        return 0.5 * self.b * self.h

    def perimeter(self):
        return self.a + self.b + self.c


c = Circle(5)
s = Square(4)
t = Triangle(3, 4, 5, 6)

print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

print("Square Area:", s.area())
print("Square Perimeter:", s.perimeter())

print("Triangle Area:", t.area())
print("Triangle Perimeter:", t.perimeter())
