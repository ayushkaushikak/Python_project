#selection sort
def selection_sort(array):
    n=len(array)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if array[mini]>array[j]:
                mini=j
                array[mini],array[i]=array[i],array[mini]
                
arr=[]
n= int(input("Enter number of element do you want in your list: "))

for i in range (1,n+1):
    arr.append(int(input(f"Enter the element number {i}: ")))
    
print("List: ", arr)
selection_sort(arr)
print("sorted list: ",arr)