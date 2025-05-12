# Insetion sort
def fun1(arr1):
    n=len(arr1)
    for i in range(1,n):
        key= arr1[i]
        j=i-1
        while j>=0 and key<arr1[j]:
            arr1[j+1] = arr1[j]
            j-=1
            arr1[j+1]=key


n= int(input("Enter Number: "))
arr1=[]
i=1
while i<n+1:
    arr1.append(int(input(f"Enter number {i} : ")))
    i+=1
    
print(arr1) 

fun1(arr1)
print(arr1)     