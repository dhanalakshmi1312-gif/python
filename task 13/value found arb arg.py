print("2. Find the Value Found using Arbitrary Keyword Argument")
def find_value(**kwargs):
    for key, value in kwargs.items():
        print(f"Key: {key}, Value Found: {value}")

data = {}


n = int(input("How many key-value pairs do you want to add? "))


for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for '{key}': ")
    data[key] = value  


print("\n--- Output ---")
find_value(**data)
