ch=input("enter a character:")
if 'A'<=ch<='Z':
    print("you entered uppercase character")
elif 'a'<=ch<='z':
    print("you entered lowercase character")
elif '0'<=ch<='9':
    print("you enterd a digit")
else:
    print("you entered a special character!")