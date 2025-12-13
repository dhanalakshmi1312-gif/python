print("\n list a")
a=[]
b=int(input("enter  no of the values:"))
for i in range(b):
      c=input("enter the words for set a:")
      a.append(c)
      print(a)
      
print("\n list b")
b=[]
d=int(input("enter the count:"))
for i in range(d):    
      f=input("enter the words for set b:")
      b.append(f)
      print(b)
print("\n convert list into set")     
n1=set(a)
n2=set(b)
print(n1)
print(n2)
print("\n difference")
g=n1.difference(n2)
print("the difference:",g)


