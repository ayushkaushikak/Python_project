#Single Level Inheritance
class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car Started!!!")
    
    @staticmethod
    def stop():
        print("Car Stopped!!!")
    
class Toyota_car(Car):
    #color="Blue"
  
    def __init__(self, name,brand):
        self.name = name
        self.brand = brand
        
class Fortuner(Toyota_car):
    def __init__(self, type):
        self.type = type
         
car1 = Fortuner("Diesel")
car1.start()
print(car1.type)
print(car1.color)
#print(car1.name)
    