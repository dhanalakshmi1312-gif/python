import math

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

area = 2 * math.pi * r * (r + h)
volume = math.pi * r * r * h

print("Surface Area =", area)
print("Volume =", volume)
