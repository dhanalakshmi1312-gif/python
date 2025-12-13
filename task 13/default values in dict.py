print("default values in dictionary")
count = int(input("Enter how many keys you want: "))


keys = []


for i in range(count):
    key = input("Enter key name: ")
    keys.append(key)


default_value = 1


d1 = dict.fromkeys(keys, default_value)


print("\nInitialized dictionary with default values:")
print(d1)
