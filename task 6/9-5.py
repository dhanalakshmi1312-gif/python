n=int(input("enter the value:"))
current_char_ord = ord('A')
for i in range(1, n + 1):  
    for j in range(1, i + 1):
        print(chr(current_char_ord), end=" ")
        current_char_ord += 1  
    print()
