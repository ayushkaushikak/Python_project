#map

marks=[78,57,68,73,90,56,99,89,23,34,44]

def grades(marks):
    if marks>=90:
        return 'A1'
    elif marks>=80 and marks<90:
        return 'A2'
    elif marks>=70 and marks<80:
        return 'B1'
    elif marks>=60 and marks<70:
        return 'B2'
    elif marks>=50 and marks<60:
        return 'C1'
    elif marks>=40 and marks<50:
        return 'C2'
    elif marks>=33 and marks<40:
        return 'D'
    else:
        return 'FAIL....'
    
grades = map(grades, marks)

print("Marks : ", marks)
print("Grades  : ", list(grades))

print( "Failing Score: ",list(filter(lambda x:x<50, marks )))