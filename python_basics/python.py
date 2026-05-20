line=input("enter a line:")
upper=0
lower=0
alpha=0
digit=0
symbol=0
for ch in line:
    if ch.isupper():
        upper=upper+1
    if ch.islower():
        lower=lower+1
    if ch.isalpha():
        alpha=alpha+1
    elif ch.isdigit():
        digit=digit+1
    else:
        symbol=symbol+1
print("uppercase letters=", upper)
print("lowercase letters =", lower)
print("alphabets =", alpha)
print("digits =", digit)
print("symbols =", symbol)