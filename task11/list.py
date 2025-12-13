print("---list----")

print(" 1. Reverse a given list")
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print("1. Reversed List:", list1)
print()
print(" 2. Concatenate two lists")
list1 = ["Hello", "Madam"]
list2 = ["Dear", "Sir"]
result = list1 + list2
print("2. Concatenated List:", result)
print()
print(" 3. Remove empty strings from a list")
items = ["Pen", "", "Pencil", "Eraser", "", "Scale"]
new_list = [x for x in items if x != ""]
print("3. After removing empty strings:", new_list)
print()
print(" 4. Convert a string to a list")
text = "HelloWorld"
list_from_string = list(text)
print("4. String to List:", list_from_string)
print()
print(" 5. Check if a list contains an element")
lst = [1, 2, 3, 'a', 'b', 'c']
print("5. 'a' in list:", 'a' in lst)
print("5. 5 in list:", 5 in lst)
print()
print(" 6. Remove all elements from a list")
nums = [1, 2, 3, 4]
nums.clear()
print("6. After clearing:", nums)
print()
print(" 7. Count the occurrence of a specific element")
pets = ['dog', 'cat', 'fish', 'fish', 'cat']
print("7. Count of 'fish':", pets.count('fish'))
print()
print(" 8. Return the length of a list without using len()")
lst = [10, 20, 30, 40]
count = 0
for _ in lst:
    count += 1
print("8. Length of list:", count)
print()
print("9. Insert a value at a specific index")
nums = [10, 20, 30, 40]
nums.insert(2, 25)
print("9. After insertion:", nums)
print()
print(" 10. Clone or copy a list")
list1 = [1, 2, 3, 4]
copy_list = list1.copy()
print("10. Copied List:", copy_list)
print()
print(" 11. Extend a list without append()")
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print("11. Extended List:", a)
print()
print(" 12. Remove duplicates from a list")
li = [3, 2, 2, 1, 1, 1]
unique = list(set(li))
print("12. List without duplicates:", unique)
print()
print(" 13. Find the index of the first matching element")
nums = [10, 20, 30, 20, 40]
print("13. Index of 20:", nums.index(20))
print()
print(" 14. Check if an element is NOT in a list")
nums = [1, 2, 3, 4, 5]
print("14. 10 not in list:", 10 not in nums)
print("14. 3 not in list:", 3 not in nums)
