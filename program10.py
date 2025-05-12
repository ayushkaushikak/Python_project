#WAP to Check if list a palindrome of elements.
list=[]
print("Enter 5 unit number to check palindrome")
list.append(input("1."))
list.append(input("2."))
list.append(input("3."))
list.append(input("4."))
list.append(input("5."))
a=list.copy()
a.reverse()
print(list)
print(a)
if(list==a):
    print("the list is in palindrome")
else:
    print("this is not palindrome")
