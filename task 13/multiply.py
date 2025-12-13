print("\n dict 1")
d1={}
count=int(input("enter the count"))
for i in range (count):
          key=int(input("enter the key"))
          value=int(input("enter the value"))
          d1[key]=value
          print(d1)
print("\n multiply of items")
import math
result1=math.prod(d1.values())
print("the multiple of values",result1)
result2=math.prod(d1.keys())
print("the multiple of key",result2)
