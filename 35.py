#getter and setter

class student:
    def __init__(self):
        self.__name=""
    
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
        
obj = student()
obj.set_name("Ayush")
print(obj.get_name()) 