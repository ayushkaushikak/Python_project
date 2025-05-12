class faculty:
    def putdata(self):
        self.id= int(input("Enter your id: "))
        self.name= input("Enter your Name: ")  
        self.salary= float(input("Enter your Salary in LPA: "))
        
    def displaydata(self):
        print("Faculty Id: ", self.id)
        print("Faculty Name: ",self.name)
        print("Faculty Salary in LPA: ",self.salary)
        
a=faculty()
a.putdata()
a.displaydata()
  
          