L=eval(input("enter a list:"))
new_list=L*2
print("replicated list:", new_list)
new_list.sort()
print("sorted in ascending order:",new_list)
new_list.sort(reverse=True)
print("sorted in descending order:",new_list)