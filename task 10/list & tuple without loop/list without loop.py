print("---- list without loop-----")
print()

print("list of 5 fruits without loop")
fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]
print("Fruits List:", fruits)
print()
print("list of 5 fruits without loop")
fruits.append("Pineapple")     
fruits.remove("Banana")        
print("After Add/Remove:", fruits)
print()
print(" Find Maximum and Minimum")
numbers = [10, 45, 2, 67, 33]
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print()
print(" Sort the List")
numbers = [5, 1, 8, 3, 9]
numbers.sort()
print("Sorted List:", numbers)
print()
print(" Join Two Lists")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Joined List:", combined)
