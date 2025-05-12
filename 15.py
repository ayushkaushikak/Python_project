#lamda function

number=[12,11,21,56,44,48,97,75,87,88,98,78,67,76,56,45,90]

def even(x):
    return x%2==0

even = list(filter(even,number))

print("even number :", even)

