# Write a Python program to find the maximum of two numbers.
a,b,c=[int(i) for i in input("Enter three numbers: ").split(",")]
if a>b and a>c:
    print(f"{a} is greater")
elif b>c and b>a:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")    

import os 
from time import sleep
sleep(5)
os.system('cls')    