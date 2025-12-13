import math

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

    def perimeter(self):
        return 2 * math.pi * self.r


c = Circle(5)
print("Area =", c.area())
print("Perimeter =", c.perimeter())
