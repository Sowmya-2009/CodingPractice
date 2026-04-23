import math
a=float(input("enter value of a:"))
b=float(input("enter value of b:"))
c=float(input("enter value of c:"))
if a==0:
    print("it is not a quadratic equation")
else:
    D=b**2-4*a*c
    if D>0:
        root1 = (-b + math.sqrt(D))/(2*a)
        root2 = (-b - math.sqrt(D))/(2*a)
        print("Roots are real and different:")
        print("Root1 is",root1)
        print("Root2 is",root2)
    elif D==0:
        root= -b/2*a
        print("root are same and real",root)
    else:
        real = -b/(2*a)
        imag = math.sqrt(-D) / (2*a)
        print("Roots are complex:")
        print("Root1 is",real,"+",imag,"i")
        print("Root2 is",real,"-",imag,"i")
