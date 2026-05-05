s = input("Enter a string: ")

if all(ch in 'aeiouAEIOU' for ch in s):
    print("Only vowels")
else:
    print("Contains other characters")