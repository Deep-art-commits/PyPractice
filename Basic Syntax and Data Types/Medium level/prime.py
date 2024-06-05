# Write a Python program to check if a number is prime.
n =int(input("Enter the number :"))
c=0
if n==1 or n==2:
    print(f"Number {n} is prime") 
elif n>2:    
    for i in range(3,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print(f"Number {n} is prime") 
    else:
        print(f"Number {n} is composite")    
        
import os 
from time import sleep
sleep(3)
os.system('cls')   