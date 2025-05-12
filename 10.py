#List Comprehension

marks=[12,33,44,33,23,47,74,35,58,96,45,29,12,27]
new_marks=[]
for x in marks:
    print(x,end=", ")
   

for x in marks:
    new_marks.append(x+2)
    
print(new_marks)