print("\n  set creation ")
a=set()
b=int(input("enter  no of the values:"))
for i in range(b):
      c=input("enter the values")
      a.add(c)
      print("the set  is:",a)
print('\n  frozen set')
n=frozenset(set(a))
k=n.append("sheela")
print("the remove of set a:",k)
      
