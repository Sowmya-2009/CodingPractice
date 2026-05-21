L=[]
row=int(input("enter the no of rows:"))
colm=int(input("enter the no of columns:"))
for i in range(row):
    row=[]
    for j in range(colm):
        x=int(input("enter an element:"))
        row.append(x)
    L.append(row)
print(L)

