#decorator in python

def decorator(func):
    def wrapper():
        print('transaction initiated')
        func()
        print("transaction completed")
    return wrapper
@decorator
def hello():
    print("....EXECUTING ALL STEPS OF TRANSACTION....")
    
hello()    