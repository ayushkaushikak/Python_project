#**kwargs & args

def fun(*args):
    print(type(args))
    if len(args)==3:
        print("My name is ",args[0],",my age is ",args[1],"and my marks is ",args[2])
    
    elif len(args)==2:
        print("My name is ",args[0],"and my age is ",args[1])
    
    elif len(args)==1:
        print("My name is ",args[0])
    
    else:
        print("ERROR")
    
fun("Ayush")