#WAP to  find factorial of n

def factorial(n):
    k=1
    i=1
    while i<n+1:
        k=k*i
        i=i+1
        
    return k
    
n=int(input("enter number: "))
print(factorial(n))