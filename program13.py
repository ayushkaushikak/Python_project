#WAP to check entered number wheather a prime or not prime
a=int(input("Enter the number to check wheather a number is prime or not prime: "))
n=0
i=2
if a==1:
    print(a,"is neither prime nor composite")
else:
    while i<a:
        if a%i==0:
            n=1
            break
        i=i+1    
        
    if n==1:
            print(a,":NOT PRIME NUMBER")
    else:
            print(a,":PRIME NUMBER")