 
    
def add():
    n1 = []
    a = int(input("Enter the count of values: "))
    total = 0

    for i in range(a):
        val = int(input(f"Enter value {i+1}: "))
        n1.append(val)
        total += val

    print("List of values:", n1)
    print("Sum of values:", total)

add()
