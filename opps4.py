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
    def __init__(self, name):
        self.name = name
        
car1 = Toyota_car("Fortuner")
car2= Toyota_car("Prius")

print(car1.name)
print(car1.color)
print(car1.start())
        