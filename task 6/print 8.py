rows = 7 

for i in range(rows):
    if i == 0 or i == rows-1 or i == rows//2:
        print("*" * 5)  
    else:
        print("*" + " " * 3 + "*") 
