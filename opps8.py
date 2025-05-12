#polymorphism
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag= imag
    
    def show_number(self):
        print(self.real,"i +", self.imag,"j")
    
    def __add__(self, num2):
        newReal= self.real + num2.real
        newImag= self.imag + num2.imag
        return Complex(newReal, newImag)
        
        
num1= Complex(1,6)
num1.show_number()

num2=Complex(5,8)
num2.show_number()

num3 = num1+num2
#print(num3)
num3.show_number()
