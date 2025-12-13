print("extract key from old dict to new dict")
d1 = {}
count = int(input("Enter number of key-value pairs: "))

for i in range(count):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d1[key] = value

print("\nOriginal dictionary:")
print(d1)


extract_keys = input("Enter keys to extract (separated by space): ").split()

new_dict = {k: d1[k] for k in extract_keys if k in d1}

print("New dictionary with extracted keys:")
print(new_dict)
