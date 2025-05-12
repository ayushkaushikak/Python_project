#Polymorphism Overiding

class Ayush:
    def Subject(self):
        print("Welcome to python class")
        
class Satvik(Ayush):
    def subject(self):
        super().Subject()
        print("welcome to maths class")
        
obj=Satvik()
obj.subject()

