#LIST COMPREHENSION

cube=[x**3 for x in range(10) if x%2==0]
print(cube)

square=[x**2 for x in range(10)]
print(square)
a=int(input("Enter number: " ))
table=[a*x for x in range(11)]
print(table)