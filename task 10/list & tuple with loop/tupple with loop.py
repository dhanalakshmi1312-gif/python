print(" Tuple Tasks  loop")
print("21. Print all tuple elements")
t1 = (5, 10, 15, 20, 25)
for item in t1:
    print(item)

print()

print(" 22. Find Sum of Tuple ")
t2 = (1, 2, 3, 4, 5)
total = 0
for num in t2:
    total += num
print("Sum of tuple elements:", total)

print()

print(" 23. Print Each Character")
t3 = ('A', 'B', 'C', 'D')
for ch in t3:
    print(ch)

print()

print(" 24. Find Even Numbers")
t4 = (10, 11, 12, 13, 14, 15)
for num in t4:
    if num % 2 == 0:
        print(num)

print()

print(" 25. Count Odd Numbers")
t5 = (1, 2, 3, 4, 5, 6, 7)
count = 0
for num in t5:
    if num % 2 != 0:
        count += 1
print("Total odd numbers:", count)

print()

print(" 26. Find Smallest Number")
t6 = (45, 12, 89, 33, 67)
smallest = t6[0]
for num in t6:
    if num < smallest:
        smallest = num
print("Smallest number:", smallest)

print()

print(" 27. Multiply All Elements")
t7 = (2, 3, 4, 5)
product = 1
for num in t7:
    product *= num
print("Product of all elements:", product)

print()

print(" 28. Tuple of Words (Uppercase)")
t8 = ('apple', 'banana', 'grapes')
for word in t8:
    print(word.upper())

print()

print(" 29. Count Vowels")
t9 = ('a', 'b', 'e', 'i', 'o', 'u', 'x', 'y')
vowels = ('a', 'e', 'i', 'o', 'u')
count = 0
for letter in t9:
    if letter.lower() in vowels:
        count += 1
print("Total vowels:", count)

print()

print(" 30. Index Display")
t10 = (100, 200, 300, 400)
for index in range(len(t10)):
    print("Index:", index, "Value:", t10[index])
