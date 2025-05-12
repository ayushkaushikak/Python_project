def show(n):
    if n==-1:
        return
    print(n)
    show(n-1)
    
show(5)