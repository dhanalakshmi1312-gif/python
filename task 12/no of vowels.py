print("\n  set 1")
a=set()
c=int(input("enter the count:"))
for i in range(c):
      e=input("enter the name")
      a.add(e)
      print("the set 1:",a)

print("\n  no of vowels")

b="aeiouAEIOU"

for e in  a:
    count=0
    for char in e:
       if char in b:
         count+=1
print(f"number of vowels in the set {e} = {count} vowels")
     
        
        
           
               
             
               


