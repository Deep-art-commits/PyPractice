# Write a program to find the GCD of two numbers
a,b=[int(i) for i in input("Enter the numbers ").split(",")]
c=0
factors_a=[]
factors_b=[]
for i in range(1,a+1):
    if a%i==0:
        factors_a.append(i)
for i in range(1,b+1):
    if b%i==0:
        factors_b.append(i)   
common_divisor =list(set(factors_a).intersection(set(factors_b)))
GCD_Euclidean=max(common_divisor)
        
print(f"The factors of {a} are: {factors_a}\nThe factors of {b} are {factors_b}\nThe GCD for {a} and {b} is {GCD_Euclidean}")             
        
import os
from time import sleep
sleep(3)
os.system('cls')    
            