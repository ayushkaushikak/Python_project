#OOPs

class Addition:
    a=0
    b=0
    sum=0
    def get_data(self,a1,b1):
        self.a = a1
        self.b = b1
    def calculate(self):
        self.sum=self.a+self.b
        print(self.sum)

obj = Addition()
obj.get_data(9,6)
obj.calculate()
        