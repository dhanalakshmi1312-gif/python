print("--- 8. Sum of Matrix Elements ---")
matrix = [
    [10, 20],  
    [30, 40] 
]
total_sum = 0
for row in matrix:
    for element in row:
        total_sum += element

print(f"The matrix is: {matrix}")
print(f"The total sum of elements is: {total_sum}")
print("-" * 40)
