print("--- 10. Alphabet Triangle ---")
rows = 4

start_ascii = ord('A') 

for i in range(rows):
    row_letters = []
    
    for j in range(i + 1):
        
        letter = chr(start_ascii + j)
        row_letters.append(letter)
        
    print(" ".join(row_letters))
print("-" * 40)
