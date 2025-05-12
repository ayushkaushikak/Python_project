a=int(input("Enter number for LCM: "))
b=int(input("Enter number for LCM: "))

i=max(a,b)
while True:
    if i%a==0 and i%b==0:
        print(f"LCM = {i}")
        break
    i+=1