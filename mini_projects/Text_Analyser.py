text=input("enter your text:")
print("1. count vowels")
print("2. reverse text")
print("3. upper/lower case check")
print("4. word count")
print("5. palindrome check")
choice=int(input("enter your choice:"))
if choice==1:
    count=0
    for i in text:
       if i.lower() in "aeiou":
           count+=1
    print("number of vowels:",count)
elif choice==2:
    reversed_text=text[::-1]
    print("reversed text:",reversed_text)
elif choice==3:
    if text.isupper():
        print("text is fully UPPERCASE")
    elif text.islower():
        print("text is fully lowercase")
    else:
        print("print has mixed case")
elif choice==4:
    words= text.split()
    print("number of words:",len(words))
elif choice==5:
    cleaned_text=text.lower()
    reversed_text=cleaned_text[::-1]
    if cleaned_text==reversed_text:
        print("it is palindrome")
    else:
        print("it is not a palindrome")
else:
    print("invalid choice")