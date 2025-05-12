#WAP to find greatest of 3 number
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
if(a>b and a>c):
    print(a," is largest number")
elif(b>a and b>c):
    print(b," is largest number")
elif(c>a and c>b):
    print(c," is largest number")
else:
    print("some number are equal or invalid")        