L = eval(input("Enter the list: "))
unique = []
duplicate = []
print("Frequency of elements:")
for x in L:
    print(x, "=", L.count(x))
    if L.count(x) == 1:
        if x not in unique:
            unique.append(x)
    else:
        if x not in duplicate:
            duplicate.append(x)
print("Unique elements:", unique)
print("Duplicate elements:", duplicate)