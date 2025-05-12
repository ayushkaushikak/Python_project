#search for a number X in tuple using loop
T=(1,55,78,890,56,27,89,83,86,40,23,31)
i=0
a=int(input("Enter the number which you want to find: "))
while i<len(T):
    if (T[i]==a):
        print(a,"FOUND at idx",i)
        break
    else:
        i=i+1
            
    