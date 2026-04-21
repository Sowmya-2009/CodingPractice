print("1. area of a circle")
print("2. perimeter of a circle")
choice=int(input("enter your choice:"))
r=float(input("enter the radius:"))
if choice==1:
    area= 3.14*r*r
    print("the area of the circle is",area)
if choice==2:
    perimeter= 2*3.14*r
    print("the perimeter of the circle is",perimeter)
    
