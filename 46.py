# Insection sort

def fun(array):
    n=len(array)
    
    for i in range(1,n):
        k=array[i]
        j=i-1
        while j>=0 and k<array[j]:
            array[j+1]=array[j]
            j-=1
            array[j+1]=k
            


arr=[]
n= int(input("Enter number of element do you want in your list: "))

for i in range (1,n+1):
    arr.append(int(input(f"Enter the element number {i}: ")))
    
print("List: ", arr)
fun(arr)
print("sorted list: ",arr)            