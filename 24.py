class Addition:
    def __init__(self, a1, b1):
        self.a = a1  # Instance variable
        self.b = b1  # Instance variable
        self.sum = 0  # Initialize instance variable

    def calculation(self):    
        self.sum = self.a + self.b  # Perform addition
        print("SUM:", self.sum)  # Print the sum

# Creating objects
obj = Addition(10, 44)
obj1 = Addition(13, 54)
obj2 = Addition(89, 76)

# Calling the calculation method
obj.calculation()
obj1.calculation()
obj2.calculation()
