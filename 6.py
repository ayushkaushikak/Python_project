#**kwargs & args

def multiply(*args):
    s=1
    for val in args:
        s*=val
    print(s)
    return s

multiply(2,5,35)
    
    
    