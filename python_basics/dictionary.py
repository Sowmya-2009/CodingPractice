phone={}
for i in range(3):
    name=input("enter the name:")
    number=int(input("enter the number:"))
    phone[name]=number
for key in phone:
    print(key,":", phone[key])
    