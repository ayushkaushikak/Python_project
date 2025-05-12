def decorator(func):
    def wrapper():
        print('transaction initiated')
        func()
        print("transaction completed")
    return wrapper

def hello():
    print("....EXECUTING ALL STEPS OF TRANSACTION....")
    
hello1=decorator(hello)
hello1()
    
        
    