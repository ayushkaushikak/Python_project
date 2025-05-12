#Write a recursive funcyion to print all element in a list 
li=['a','ayush','ganesh','bb','aman','chirag','cbvh']
def print_list(list, idx=0):
    if idx==len(list):
        return
    print(list[idx])
    return print_list(list,idx+1)
    
    
print(print_list(li))