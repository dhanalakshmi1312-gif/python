print("\n   set into tuple  ")
a=set()
b=int(input("enter the count of the values:"))
for i in range(b):
 c=input("enter the values:")
 a.add(c)
 print(a)
 d=tuple(a)
print("the conversion of set into tuple:",d)
    
print("\n   tuple into set  ")
n1=()
n2=int(input("enter the count of the values:"))
new=[]
for i in range(n2):
 n3=input("enter the values:")
 new.append(n3)
 print("the list value:",new)

 
 print("\n  convert list into tuple")
 n4=tuple(new)
 print("the conversion of list to tuple:",n4)
 
 print("\n  convert tuple into set")
 n5=set(n4)
 print("the conversion of tuple into set:",n5)
    
