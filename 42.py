#selection_sort

def selection(arr):
    n=len(arr)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr[mini]>arr[j]:
                mini=j
                arr[i],arr[mini]=arr[mini],arr[i]
                
arr=[]
n= int(input("Enter number of element do you want in your list: "))

for i in range (1,n+1):
    arr.append(int(input(f"Enter the element number {i}: ")))
    
print("List: ", arr)
selection(arr)
print("sorted list: ",arr)