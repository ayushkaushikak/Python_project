#bubble sort

def bubble(arr):
    n=len(arr)
    for i in range(n):
        swapped = False
        for j in range (0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
                
        if  not swapped:
                break

arr=[]
n= int(input("Enter number of element do you want in your list: "))

for i in range (1,n+1):
    arr.append(int(input(f"Enter the element number {i}: ")))
    
print("List: ", arr)
bubble(arr)
print("sorted list: ",arr)