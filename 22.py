#OOPs Area of circle

class Area:
    r=0
    area=0
    def get_radius(self, r1):
        self.r=r1
        
    def area_circle(self):
        self.area= 3.14*self.r**2
        print(self.area)
        
obj = Area()

obj.get_radius(21)

obj.area_circle()