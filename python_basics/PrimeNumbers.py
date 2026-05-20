num=int(input("enter the number:"))
if num<=1:
    print("not prime")
else:
    for i in range(2,num):
        if i%num==0:
            print("not prime")
            break
    else:
        print("prime")