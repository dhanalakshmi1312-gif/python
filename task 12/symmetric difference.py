print("\n  set creation ")
a=set()
b=int(input("enter  no of the values:"))
for i in range(b):
      c=input("enter the values")
      a.add(c)
      print("the set first is:",a)
      print()


      

n1=set()
n2=int(input("enter  no of the values:"))
for i in range(n2):
      n3=input("enter the values")
      n1.add(n3)
      print("the set second is:",n1)
      print()


      

print("\n set difference  ")
f=a.symmetric_difference(n1)
print("the difference value:",f)

      
