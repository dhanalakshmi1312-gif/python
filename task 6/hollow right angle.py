
rows =int( input("Enter the number of rows: "))

for i in range(1, rows + 1):
    
    print(" " * (rows - i), end="")
    
    
    for j in range(1, i + 1):
        if j == 1 or j == i or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()  
