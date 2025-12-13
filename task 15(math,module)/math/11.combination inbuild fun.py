def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

n = int(input("Enter n: "))
r = int(input("Enter r: "))

ncr = factorial(n) // (factorial(r) * factorial(n-r))
print("Combination =", ncr)
