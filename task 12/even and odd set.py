print("\n  set creation ")
a=set()
b=int(input("enter  no of the values:"))
for i in range(b):
      c=int(input("enter the values"))
      a.add(c)
      print(a)
print("\n  even and odd number count")

even=0
odd=0
for num in a:
    if num % 2==0:
       even +=1
    else:
        odd+=1
print("the total no of even numbers:",even)
print("the total no of odd numbers:",odd)
        

