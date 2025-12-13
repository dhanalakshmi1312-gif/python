def countvowelsconsonantsspecialcharacter():

 a=input("enter any text")
 count=0
 count1=0
 count2=0
for i in a.lower():
    if i in "aeiou":
      count+=1
print("the count of vowels in given string:",count)
    elif i.isalpha():
     count1+=1
print("the count of consonants in given string:",count1)
    else: 
      count2+=1
print("the count of special character  in given string:",count2)
countvowelsconsonantsspecialcharacter()
