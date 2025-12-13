print("\n dict 1")
d1={}
count=int(input("enter the count"))
for i in range (count):
          key=input("enter the key")
          value=int(input("enter the value"))
          d1[key]=value
          print(d1)
print("\n sum all values")
d=sum(d1.values())
print(d)
