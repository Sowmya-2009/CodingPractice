L=[30,60]
n=int(input(" how many numbers you want to enter:"))
if n==1:
    x=int(input("enter the number:"))
    L.append(x)
else:
    new_list=[]
    for i in range(n):
        x=int(input("enter the number:"))
        new_list.append(x)
    L.extend(new_list)
print(L)
