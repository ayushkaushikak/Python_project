#OOPs

class Employee:
    def __init__(self):
        self.emp_name= input("Enter Employee name: ")
        self.emp_id=int(input("Enter Employee id: "))
        self.emp_age=int(input("Enter Employee age: "))
    
    def show_data(self):
        print("Employee Name: ", self.emp_name)
        print("Employee age: ", self.emp_age)
        print("Employee id: ", self.emp_id)
obj = Employee()
obj.show_data()