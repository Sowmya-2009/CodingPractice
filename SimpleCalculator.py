num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
op=input("enter the operator(+,-,/,%,*):")
if op=='+':
    result=num1+num2
    print("result is",result)
elif op=='-':
    result=num1-num2
    print("result is",result)
elif op=='*':
    result=num1*num2
    print("result is",result)
elif op=='/':
    result=num1/num2
    print("result is",result)
elif op=='%':
    result=num1%num2
    print("result is",result)
else:
    print("invalid operator!!")

