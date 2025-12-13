d1 = {}
count = int(input("Enter the count: "))

for i in range(count):
    key = input("Enter the key: ")
    value = int(input("Enter the value: "))
    d1[key] = value

print("Dictionary:", d1)
print("Size of the dictionary:", len(d1))
