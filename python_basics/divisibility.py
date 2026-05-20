num1=int(input("enter first number:"))
num2=int(input("enter the second number:"))
reminder= num1%num2
if reminder==0:
    print(num1,"is divisible by",num2)
else:
    print(num1,"is not divisible by",num2)
    