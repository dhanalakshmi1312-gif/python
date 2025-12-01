print("--- 7. Multiplication Grid ---")
size = 5
for i in range(1, size + 1):
    row_output = ""
    for j in range(1, size + 1):
        
        row_output += f"{i * j:3}"
    print(row_output)
