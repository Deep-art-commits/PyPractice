# How do you reverse a string in Python?
# inp=input("Enter a string :")
# print(f"Reverse of {inp} is {inp[::-1]}")

input_str=input("Enter the string ")
s=input_str.split()

rev_str=[]
for i in s:
    rev_str.append(i[::-1])
print(" ".join(rev_str))  
import os 
from time import sleep
sleep(5)
os.system('cls') 
    
        
    