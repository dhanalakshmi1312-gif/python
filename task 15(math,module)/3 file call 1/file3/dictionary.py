def get_dictionary():
    d = {}
    n = int(input("Enter number of elements: "))
    for i in range(n):
        key = input("Enter key: ")
        value = int(input("Enter value: "))
        d[key] = value
    return d



def print_dictionary(d):
    print("Dictionary Values:")
    for key, value in d.items():
        print(key, ":", value)

def sum_dictionary_values(d):
    total = sum(d.values())
    return total
