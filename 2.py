#HCF

n=int(input("Enter number for HCF: "))
m=int(input("Enter number for HCF: "))

i=min(m,n)
while i>0:
    if n % i==0 and m%i ==0:
        a=i
        break
    i=i-1
    
print(f"HCF of {m} and {n} is {a}")
    
    
