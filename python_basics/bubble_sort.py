L = eval(input("Enter the list: "))
n = len(L)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
print("Sorted list:", L)