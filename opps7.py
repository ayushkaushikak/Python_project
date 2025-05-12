class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
      #  self.percentage = str((self.phy+ self.math+self.chem)/3)+ "%"
        
  #      def calc_percentage(self):
   #         self.percentage = str((self.phy+ self.math+self.chem)/3)+ "%"
    @property
    def percentage(self):
        return str((self.phy+ self.math+self.chem)/3)+ "%"
        
        #percentage
a=int(input("enter marks of physics: "))
b=int(input("enter marks of math: "))
c=int(input("enter marks of chem: "))

        
stu1 = Student(a,b,c)
print(stu1.percentage)

d = int(input("enter physics mark again: "))        
stu1.phy = d

print(stu1.phy)
#stu1.calc_percentage()
print(stu1.percentage)

    