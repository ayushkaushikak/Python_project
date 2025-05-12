class A:
    def showdata(self):
        print("I am in class A")
        
class B(A):
    def showdata(self):
        super().showdata()
        print("I am in class B")
        
obj = B()
obj.showdata()