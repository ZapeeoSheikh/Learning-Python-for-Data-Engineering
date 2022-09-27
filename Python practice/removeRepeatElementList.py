number = [45,34,43,56,6,2,6,7,68,85,6,85,68,56,8,6]
unique = []
print("before " +  str(unique))

for numbers in number:
    if numbers not in unique:
        unique.append(numbers)


print(f"after {unique}")