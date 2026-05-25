L=eval(input("enter the list:"))
x=int(input("enetr the element to be searched:"))
if x in L:
    index=L.index(x)
    print("element found at index:", index)
else:
    print("element not found")