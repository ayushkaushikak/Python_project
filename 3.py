def HCF(n,m):
    i=min(n,m)
    while i>0:
        if n%i==0 and m%i==0:
            print(f"HCF of {m} and {n} is {i}")
            break   
        i-=1
        
    
m=int(input("Enter number for HCF: "))
n=int(input("Enter number for HCF: "))
print(HCF(n,m))