str1=input("enter first string:")
str2=input("enter second string:")
if str1 in str2:
   str3=str2[:4]+"restore"
   print(str3, "is the third string")
else:
    print("string 1 is not contained in string 2")
    