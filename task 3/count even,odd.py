numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:",odd)
