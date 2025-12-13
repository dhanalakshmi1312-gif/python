d={}
count=int(input("enter the count"))
for i in range (count):
          key=input("enter the key")
          value=input("enter the value")
          d[key]=value
          print(d)
print("\n check the key exist")
key=input("enter the   key to check")
if key in d:
    print("its exit")
else:
   print("its not exist")
