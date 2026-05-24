L=[20,30,407,60]
print("1.insert element")
print("2.delete element")
choice=int(input("enter you choice:"))
if choice==1:
    x=int(input("enter the element:"))
    L.append(x)
elif choice==2:
    print("1.delete by value")
    print("2.delete by position")
    print("3.delete by slice")
    ch=int(input("enter your choice:"))
    if ch==1:
        x=int(input("enter value to delete:"))
        L.remove(x)
    elif ch==2:
        x=int(input("enter the position:"))
        L.pop(x)
    elif ch==3:
        start=int(input("enter start index:"))
        end=int(input("enter end index:"))
        del L[start:end]
else:
    print("it is not available")
print(L)
