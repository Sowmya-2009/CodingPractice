a=int(input("enter first number :"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a<b and a<c:
    if b<c:
        print(a,b,c)
    else:
        print(a,c,b)
if b<a and b<c:
    if a<c:
        print(b,a,c)
    else:
        print(b,c,a)
else:
    if a<b:
        print(c,a,b)
    else:
        print(c,b,a)
        