# 10.	Write a program to generate the Fibonacci sequence up to n terms.
n =int(input("How many terms of fibonacci series do you wnat to generate ? : "))
a=0
b=1
fib=[]
for i in range(n):
        c=a+b
        a=b
        b=c
        fib.append(c)
print(f"Fibonacci of {n} terms is\n{fib}",end=" ")    

import os 
from time import sleep
sleep(5)
os.system('cls') 
    