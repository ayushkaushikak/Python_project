# Binary search

def binary(array):
    target=int(input("Enter number that you want to find in your array"))
    left,right=0,len(array)-1
    k=0
    while left <= right:
        mid = (left+right)//2
        if array[mid]==target:
            print(f"Found at {mid+1} position")
            k=1
            break
        elif array[mid]<target:
            left= mid + 1 
        else:
            right=mid-1
    if k==0:
        print("Not found")
        
arr=[]
k=int(input("How many number do you want in your list: "))
i=0
while i<k:
    arr.append(int(input("Enter number in your list: ")))  
    i+=1     


binary(arr)        