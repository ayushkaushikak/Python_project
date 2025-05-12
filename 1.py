#Sum of n natural number
#HCF
#LCM

#Sum of n natural numbers
def sum(n):
    a=(n)*(n+1)/2
    return a

def sum2(n):
    a=0
    for i in range (1,n+1):
        a = i+a
    return a
    

n=int(input("Enter Number of sum: "))
print(sum(n))

print(sum2(n))

