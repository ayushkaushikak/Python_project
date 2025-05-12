#OOPs Encapsulation

class Calculation:
    __name= 'Ayush'
    name= 'SATVIK Ayush'
    
    def __init__(self):
        print('My name is ',self.__name)
        
    def My_name(self):
        print('My name is ',self.__name)
        self.__get_sum(7,99)
        self.__sum()
    
    def __get_sum(self,a,b):
        self.a=a
        self.b=b
    def __sum(self):
        print(self.a+self.b)
        
obj = Calculation()
obj.My_name()
#obj.get_sum(6,9)
#obj.sum()
print("My name is: ",obj.name)

#print("My name is: ",obj.__name)