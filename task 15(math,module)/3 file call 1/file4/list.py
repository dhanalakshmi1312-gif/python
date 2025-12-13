def get_list():
    lst = []
    n = int(input("Enter number of elements: "))
    for i in range(n):
        value = int(input("Enter value: "))
        lst.append(value)
    return lst



def print_list(lst):
    print("List Values:")
    for i in lst:
        print(i)


def count_even_numbers(lst):
    count = 0
    for i in lst:
        if i % 2 == 0:
            count += 1
    return count
