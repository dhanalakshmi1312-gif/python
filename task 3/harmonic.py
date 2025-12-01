n = int(input("Enter number of terms: "))
sum = 0
for i in range(1, n + 1):
    sum += 1 / i
    print("1/", i, end="  ")
print("\nSum of harmonic series =",sum)
