#all divisor of number in root complexity 
import time
t1 = time.time()
a=int(input("Enter the number to find its factor: "))
i=1
while i<=a:
    if a%i==0:
        print(i,end=" ")
    i=i+1
t2=time.time()
print("\n",t2-t1)
