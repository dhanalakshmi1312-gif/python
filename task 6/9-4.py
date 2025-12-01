n=int(input("enter the value:"))
start_char_ord = ord('A')
for i in range(1, n + 1):
    char_to_print = chr(start_char_ord + i - 1)
    for j in range(1, i + 2):  
        print(char_to_print, end=" ")
    print()
