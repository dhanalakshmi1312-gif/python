print("\n 2 values and function")
v1 =int(input("ener the value 1:"))
v2 =int(input("ener the value 2:"))
print("1=add")
print("2=difference")
print("3=product")
print("4=division")
operation=int(input("enter the operation"))


if operation ==1 :
    print("the sum is:", v1+v2)
elif operation == 2:
     print("the difference is:",v1-v2)
elif operation == 3:
     print("the product is:",v1*v2)
elif operation == 4:
    print("the floor division:",V1/v2)
else:
    print("its invalid")

