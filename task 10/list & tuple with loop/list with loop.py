print("----list for with loop---")
print("6.list of cities")
cities = ["Chennai", "Delhi", "Mumbai", "Kolkata", "Bangalore"]

for city in cities:
    print(city)
print()

print("7.sum of the list")
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Sum of numbers:", total)

print()
print("8.count even numbers")
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print("Number of even numbers:", count)
print()
print("9.square each numbers")
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num, "squared is", num ** 2)
print()
print("10.reverse the items in list")
items = [10, 20, 30, 40, 50]

for i in range(len(items) - 1, -1, -1):
    print(items[i])
