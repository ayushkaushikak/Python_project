class student:
    def __init__(self,rollnumber, name, marks):
        self.rollnumber=rollnumber
        self.name=name
        self.marks=marks
    
    def average(self):
        return  sum(self.marks)/len(self.marks)

first_student = student(1,"Ayush",[80,90,99,88,76])
print("Name of student: ",first_student.name)
print("Roll no. of student: ",first_student.rollnumber)
print("Marks of student: ",first_student.marks)
print(first_student.average())