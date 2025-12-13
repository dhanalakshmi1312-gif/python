print("\n  set 1")
a=set()
c=int(input("enter the count:"))
for i in range(c):
      e=input("enter the value")
      a.add(e)
      print("the set 1:",a)

print("\n  set 2")
b=set()
d=int(input("enter the count:"))
for i in range(d):    
      f=input("enter the value")
      b.add(f)
      print("the set 2:",b)
print("\n  intersection")
n1=a.intersection(b)
print("the intersection is:",n1)




