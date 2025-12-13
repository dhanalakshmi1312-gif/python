a=set()
b=int(input("enter  no of the values:"))
for i in range(b):
      c=input("enter the words for set a")
    
      a.add(c)
      print(a)
      print( )
b=set()

d=int(input("enter the count:"))
for i in range(d):    
      f=input("enter the words for set b")
      b.add(f)
      print(b)
      print("\n" )

c=set()

e=int(input("enter the count:"))
for i in range(e):    
      e=input("enter the words for set c")
      c.add(e)
      print(c)
      print("\n" )
      
      
g= a.intersection(b,c)
print("the common value is:",g)
 
