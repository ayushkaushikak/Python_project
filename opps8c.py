class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def show_number(self):
        print(self.real, "i +", self.imag, "j")
    
    def add(self, num2):
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return Complex(newReal, newImag)  # Corrected here
        
num1 = Complex(1, 6)
num1.show_number()

num2 = Complex(5, 8)
num2.show_number()

num3 = num1.add(num2)
num3.show_number()