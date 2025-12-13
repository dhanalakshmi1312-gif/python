print("\n  set 1")
a=set()
c=int(input("enter the count:"))
for i in range(c):
      e=int(input("enter the value"))
      a.add(e)
      print("the set 1:",a)

print("\n perfect numbers")

perfectnumber=set()
for num in  a:
    if num > 0:
        count=0
        for i in range(1, num):
           if num % i== 0:
               count+=i
             
               if count==num:
                 perfectnumber.add(num)
             

print("Perfect  numbers in the set:", perfectnumber)
