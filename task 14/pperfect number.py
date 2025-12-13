def perfectnumber():
    
    a = int(input("Enter the  values: "))
    total=0

    for i in range(1,a):
        
       
        if a % i == 0:
            total+=i
              
    if total==a:    
        print("its perfect number",a)
    else:
        print(a,"its not a perfect number")

    
   

perfectnumber ()
