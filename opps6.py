#Multiple Inheritance
class A:
    VarA= "Welcome to class A"

class B:
    VarB= "Welcome to Class B"
    
class C(A,B):
    Varc="Welcome to class C"
    
c1 = C()

print(c1.Varc)
print(c1.VarB)
print(c1.VarA)
