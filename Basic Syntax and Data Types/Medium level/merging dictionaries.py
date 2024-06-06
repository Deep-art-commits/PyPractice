# 8.	Write a Python program to merge two dictionaries.
user_dict={}
ud={}
final={}
n1=int(input("How many dictionaries you want to create "))
for i in range(1,n1+1):
    
    a=int(input(f"How many Enteries  you want {i} dictiory:  "))
    
    for j in range(1,a+1):
        key=input("Enter Key :")
        value=input("Enter  value: ")
        user_dict[key]=value
    ud[i]=user_dict
    # print(f"{i} dictionary is {ud[i]}")
    final.update(ud[i])
print(f"The entered dictionaries are : {ud}\nMerged dictionary is :{final}")    
        
# import os
# from time import sleep
# sleep(3)
# os.system('cls')          