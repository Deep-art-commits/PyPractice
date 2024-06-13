# Write a Python program to find the factorial of a number.
fact=1
n= int(input("Enter a number for which factorial is to be calculated :"))
for i in range(n,0,-1):
    fact=fact*i
   
print(f"factorial of {n} is {fact}")   

import os 
from time import sleep
sleep(5)
os.system('cls')  

