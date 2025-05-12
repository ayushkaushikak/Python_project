def insertion_sort(a):
    l=len(a)
    
    for i in range(1,l):
        k=a[i]
        j=i-1
        
        while j>=0 and k<a[j]:
            a[j+1]=a[j]
            j=j-1
            a[j+1]=k
            
n= int(input("Enter Number: "))
arr1=[]
i=1
while i<n+1:
    arr1.append(int(input(f"Enter number {i} : ")))
    i+=1
    
print(arr1) 

insertion_sort(arr1)
print(arr1)     