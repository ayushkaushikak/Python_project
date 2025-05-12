class Person:
    __name ="Ayush"
    def __hello(self):
        print("Hello World")
    def welcome(self):
        self.__hello()
p1= Person()

print(p1.welcome())