print("\n dict 1")
d1={}
count=int(input("enter the count"))
for i in range (count):
          key=int(input("enter the key"))
          value=int(input("enter the value"))
          d1[key]=value
          print(d1)
print("\n remove a key")
d=d1.keys()
k = int(input("Enter the key to remove: "))
if k in d1:
    del d1[k]
    print("Updated dictionary:", d1)
else:
    print("Key not found!")
