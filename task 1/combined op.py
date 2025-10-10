# 1. Two numbers – sum, difference, product, remainder, floor division
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Remainder:", a % b)
print("Floor Division:", a // b)

# 2. Increment by 5
a = int(input("Enter a number: "))
a += 5
print("After incrementing by 5:", a)

# 3. Triple the number and check if result > 50
a = int(input("Enter a number: "))
a *= 3
print("Tripled value:", a)
print("Is result greater than 50?", a > 50)

# 4. Two numbers - check if both > 10 (using and)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Both greater than 10:", a > 10 and b > 10)

# 5. Two numbers - check if at least one > 10 (using or)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("At least one greater than 10:", a > 10 or b > 10)
