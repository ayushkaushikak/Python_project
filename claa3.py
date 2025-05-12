class Student:
    def __init__(self,name,marks):
        self.name= name
        self.marks= marks
        print("Adding details of new student in database")
    def welcome(self):
        print("Welcome",self.name)

s1= Student("karan",98)
print(s1.name)
print(s1.marks)
s1.welcome()
s2= Student("Ayush",89)
print(s2.name)
print(s2.marks)
s3= Student("Aman",87)
print(s3.name)
print(s3.marks)
s4= Student("Satvik",65)
print(s4.name)
print(s4.marks)

    
    