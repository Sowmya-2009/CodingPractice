total=0
choice="yes"
while choice=="yes":
    num=int(input("enter a number:"))
    if num<0:
        print("program aborted")
        break
    else:
        total= total+num
print("sum is",total)

    