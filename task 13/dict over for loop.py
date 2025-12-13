d={}
count=int(input("enter the count"))
for i in range (count):
          key=input("enter the key")
          value=input("enter the value")
          d[key]=value
          print(d)


for key,value in d.items():
    print(key,":",value)
