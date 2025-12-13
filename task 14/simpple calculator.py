def simplecalculator():
    a=int(input("enter the value 1:"))
    b=int(input("enter the value 2:"))
    print("operation=1.add,2.sub,3.multiply,4.division")
    operation=int(input("enter the value from 1 to 4:)"))

    if operation==1:
          print("the result:",a+b)
    elif operation==2:
          print("the result:",a-b)
    elif operation==3:
          print("the result:",a*b)
    elif operation==4:
          print("the result:",a/b)
    else:
        print("invalid result")
    
simplecalculator()    
