print("\n  Two boolean values (AND)")
a = bool(int(input("Enter first boolean value : ")))
b = bool(int(input("Enter second boolean value : ")))
print("Result of a and b:", a and b)

print("\n print  Two boolean values (OR)")
a = bool(int(input("Enter first boolean value : ")))
b = bool(int(input("Enter second boolean value : ")))
print("Result of a or b:", a or b)

 print("\n One boolean value (NOT)")
a = bool(int(input("Enter a boolean value : ")))
print("Result of not a:", not a)

print("\n  Three boolean values ((a and b) or c)")
a = bool(int(input("Enter first boolean value : ")))
b = bool(int(input("Enter second boolean value : ")))
c = bool(int(input("Enter third boolean value : ")))
print("Result of (a and b) or c:", (a and b) or c)

print("\n   Two boolean values ((not a) and b)")
a = bool(int(input("Enter first boolean value : ")))
b = bool(int(input("Enter second boolean value : ")))
print("Result of (not a) and b:", (not a) and b)
