# Write a Python program to swap two variables.
# a,b=[int(i) for i in input("Eneter  two numbers :").split(",")]
# print(f"The numbers before swapping  are a={a} and b={b}")
# a,b=b,a
# print(f"The numbers after  swapping  are a={a} and b={b}")

# swapping using 3rd variable 
# a,b=[int(i) for i in input("Eneter  two numbers :").split(",")]
# print(f"The numbers before swapping  are a={a} and b={b}")
# c=a
# a=b
# b=c
# print(f"The numbers after  swapping  are a={a} and b={b}")

# swapping  without using 3rd variable 
a,b=[int(i) for i in input("Eneter  two numbers :").split(",")]
print(f"The numbers before swapping  are a={a} and b={b}")
a=a+b
b=a-b
a=a-b
print(f"The numbers after  swapping  are a={a} and b={b}")

import os
from time import sleep
sleep(3)
os.system('cls')
