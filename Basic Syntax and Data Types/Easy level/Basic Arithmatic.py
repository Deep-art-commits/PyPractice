# Basic arithmetic: Write a program that calculates the sum, difference, product, and quotient of two numbers.
x,y= input("Enter 2 numbers : ").split(",")
x= int(x)
y=int(y)
print(f"Sum of 2 numbers is: {x+y}")
print(f"Difference  of 2 numbers is: {x-y}")
print(f"Product of 2 numbers is: {x*y}")
print(f"Quotient of 2 numbers is: {x/y}")

import os
from time import sleep
sleep(3)
os.system("cls")