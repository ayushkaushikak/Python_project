# Linear search

def Linear_seach(array):
    n=len(array)
    a=int(input("Enter the number that you want to find in your list"))
    k=0
    for i in range(n):
        if array[i]==a:
            print(f"found {a} at {i} position")
            k=1
            break
        
    if k!=1 :
        print("Not Found")
           
            
arr=[]
k=int(input("How many number do you want in your list: "))
i=0
while i<k:
    arr.append(int(input("Enter number in your list: ")))  
    i+=1     
    
Linear_seach(arr)