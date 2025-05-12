#**kwargs & args
def printmarks(**kwargs):
    print(type(kwargs))
    for keys, values in kwargs.items():
        print(keys,values)
        
        
Class = {"Ayush":100, "Aman":89,"Vinayak":92,"Shruti":56,"Kanishq":88, "Pankag":98,"Yasdeep":78}


printmarks(**Class)

print(Class)