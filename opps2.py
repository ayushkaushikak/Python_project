class Account:
    def __init__(self, acc_number, acc_pass):
        self.acc_number= acc_number
        self.__acc_pass= acc_pass

    def reset_pass(self):
        print(self.__acc_pass)
        
acc1= Account("12345", "123@Ayush")

print(acc1.acc_number)
print(acc1.reset_pass())



        