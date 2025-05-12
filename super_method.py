#super method
class Car:
    def __init__(self,type):
        self.type = type
            
    @staticmethod
    def start():
        print("CAR STARTED.....")
        
    def stop():
        print("CAR STOPPED.....")
        

class Toyota_car(Car):
    def __init__(self, name,type):
        self.name = name
        #self.type = type
        super().__init__(type)

car1= Toyota_car("pirus","electric")
print(car1.type)     
print(car1.name)   