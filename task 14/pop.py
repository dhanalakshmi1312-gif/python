def pop  ():
    n1 = []
    total=0
    a = int(input("Enter the count of values: "))
    for i in range(a):
        val = int(input(f"Enter value {i+1}: "))
        n1.append(val)
        total+=val
    print("List of values:", n1)
    if n1:
          remove=  n1.pop()

    
    print("removal of value:", remove)
    print("final list:", n1)

pop ()
