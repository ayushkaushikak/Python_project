#calculator
import math
print("Calculator: +,-,X,/,%,squatroot(sq), square(^2)")
a=float(input("Enter Number: "))
b=input("Enter Operator: ")
if b != 'sq' and b!='^2':
    c=float(input("Enter Number: "))
if b=='+' or b=='-' or b =='X'or b=='/' or b== '%':
    match b:
        case '+':
            print(f"{a} + {c} = {a + c}")
        case '-':
            print(f"{a} - {c} = {a - c}")
        case '*':
            print(f"{a} X {c} = {a * c}")
        case '/':
            print(f"{a} / {c} = {a / c}")
        case '%':
            print(f"{a} % {c} = {a % c}")
        case _:
            print("Error")
elif b=='sq':
    print(math.sqrt(a))
elif b=='^2':
    print(a*a)
else:
    print("ERROR")
    
    