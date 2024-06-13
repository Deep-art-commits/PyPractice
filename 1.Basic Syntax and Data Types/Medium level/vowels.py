# Write a program to count the number of vowels in a string.
# input=input("eneter a string :")
# c=0
# v=['a','e','i','o','u']
# for i in input.lower():
#     if i in v:
#         c=c+1
# print(f"No of vowels in input string : {input} are {c}")     

import re
input=input("enter a string :")
v=['a','e','i','o','u']
vow=re.findall(f"{v}",input,re.I)
print(f"No of Vowels in {input} are {len(vow)} and vowels present are {vow}")

   
import os
from time import sleep
sleep(3)
os.system('cls')    