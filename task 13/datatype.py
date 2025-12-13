print("  find datatype ")



a = input("Enter any value: ")


if a.isdigit():
    value = int(a)
elif a.replace('.', '', 1).isdigit():
    value = float(a)
elif a.lower() in ['true', 'false']:
    value = bool(a)
else:
    value = a
    

print("Value:", value)
print("Detected datatype:", type(value))
