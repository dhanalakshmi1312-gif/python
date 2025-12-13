def add():
    n1 = []
    a = int(input("Enter the count of values: "))
    total=0

    for i in range(a):
        val = int(input("Enter value : "))
        n1.append(val)
        
        if val% 2 == 0:
           total+=val
           print("its even",val)

    print("List of values:", n1)
    print("even number :", total)

add()
