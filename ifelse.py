age=int(input("Enter your age: "))

if(age<13):
    print("you are a child")
elif(age<18 and age>=13):
    print("you are in the category of teenage")
elif(age>=18 and age<50):
    print("you are in the category of adult")
else:
    print("you are senior citizen")
    