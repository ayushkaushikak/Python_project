class person:
    name="anonymous"
    
    def change_Name(self, name):
        #person.name = name
        p1.name= name
        #self.__class__.name="Ayush"
    @classmethod
    def change_Name(cls, name):
        cls.name= name    
p1 = person()
p1.change_Name("rahul kumar")

print(p1.name)

print(person.name)