#OOPs

class Addition:
    a=0
    b=0
    sum=0
    def __init__(self,a1,b1):
        self.a = a1
        self.b = b1
    def calculation(self):    
            self.sum = self.a + self.b
            print("SUM: ", self.sum)

obj = Addition(10,44)
obj1 = Addition(13,54)
obj2 = Addition(89,76)
obj.calculation()
obj1.calculation()
obj2.calculation()
