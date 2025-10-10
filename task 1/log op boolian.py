# 1. Two boolean values (AND)
a = bool(int(input("Enter first boolean value (1 for True, 0 for False): ")))
b = bool(int(input("Enter second boolean value (1 for True, 0 for False): ")))
print("Result of a and b:", a and b)

# 2. Two boolean values (OR)
a = bool(int(input("Enter first boolean value (1 for True, 0 for False): ")))
b = bool(int(input("Enter second boolean value (1 for True, 0 for False): ")))
print("Result of a or b:", a or b)

# 3. One boolean value (NOT)
a = bool(int(input("Enter a boolean value (1 for True, 0 for False): ")))
print("Result of not a:", not a)

# 4. Three boolean values ((a and b) or c)
a = bool(int(input("Enter first boolean value (1 for True, 0 for False): ")))
b = bool(int(input("Enter second boolean value (1 for True, 0 for False): ")))
c = bool(int(input("Enter third boolean value (1 for True, 0 for False): ")))
print("Result of (a and b) or c:", (a and b) or c)

# 5. Two boolean values ((not a) and b)
a = bool(int(input("Enter first boolean value (1 for True, 0 for False): ")))
b = bool(int(input("Enter second boolean value (1 for True, 0 for False): ")))
print("Result of (not a) and b:", (not a) and b)
