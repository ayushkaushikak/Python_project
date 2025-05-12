#Search for a number X in the tuple
list=(1,4,9,25,36,49,81,100) 
print(list)
a=int(input("Enter number from above list"))
for v in list:
    if(v==a):
        print(v,"Found")
        break
    else:
        continue