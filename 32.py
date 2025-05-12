#Polymorphism

class Maths:
    def area(self, a=None,b=None):
        if a !=None and b!=None:
            print("Area of rectangle ",a*b)
        elif a!=None:
            print("Area of square ",a**2)
        else:
            print("ERROR....")
            
obj=Maths()
obj.area(10,9)
obj.area(8)
obj.area()
