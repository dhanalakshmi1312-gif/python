print(" a string made of first, middle, and last character")

a = input("Enter any string: ")


if len(a) >= 3:
    middle_index = len(a) // 2
    result = a[0] + a[middle_index] + a[-1]
    print("New string:", result)
else:
    print("String too short!")
