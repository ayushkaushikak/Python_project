a=int(input("Enter number for LCM: "))
b=int(input("Enter number for LCM: "))
i=1
while True:
    c=a*i
    if c%b==0:
        print(f"LCM={c}")
        break
    i=i+1
    
    