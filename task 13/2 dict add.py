print("\n dict 1")
d1={}
count=int(input("enter the count"))
for i in range (count):
          key=input("enter the key")
          value=input("enter the value")
          d1[key]=value
          print(d1)
print("\n dict 2")
d2={}
count=int(input("enter the count"))
for i in range (count):
          key=input("enter the key")
          value=input("enter the value")
          d2[key]=value
          print(d2)
print("\n merge")
d1.update(d2)
print("the merge of 2 dicts:",d1) 
