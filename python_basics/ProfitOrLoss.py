sp=float(input("enter the selling price:"))
cp=float(input("enter the cost price:"))
if sp>cp:
    profit= sp-cp
    print('profit=,profit')
elif sp<cp:
    loss= cp-sp
    print('loss=,loss')
else:
    print('no loss, no profit')

