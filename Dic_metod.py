student ={
    "Name":"Ayush Kaushik",
    "subject":{
        "phy":89,
        "chem":88,
        "English":98,
        "Maths":78   
    }
}
print(list(student.keys()))
print(len((student)))
print(type(student))
print(list(student.values()))
print(list(student.items()))
print(student.get("Name"))
print(student["Name"])
student.update({"city":"Faridabad"})
print(student)
new_student={
    "name":"satvik Kaushik",
    "age":16
}
student.update(new_student)
print(student)