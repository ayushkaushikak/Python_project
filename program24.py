#Write a recursion function to calculate the sum of fiest n naturat number

def sum(n):
    if (n==0):
        return 0
    return sum(n-1)+n
        
a=int(input("enter Number: "))
print(sum(a))