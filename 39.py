#Insertion sort

def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        k=arr[i]
        j=i-1
        while j>=0 and k<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=k
            
arr=[]
n= int(input("Enter number of element do you want in your list: "))

for i in range (1,n+1):
    arr.append(int(input(f"Enter the element number {i}: ")))
    
print("List: ", arr)
insertion_sort(arr)
print("sorted list: ",arr)
        
    