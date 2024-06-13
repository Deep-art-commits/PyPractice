while True:
    message= input("what do you want to convert , miles to km or km to miles , \
                   \nenter 1 for miles to km and 2 for km to miles: ")

    if message=="1":
        dm=int(input("enter distance in miles: "))
        k=dm/1.6093442
        print(f"{dm} miles  in kilometers is {k} kms")
        break
    elif message=="2":
        km=int(input("enter distance in kilometers: "))
        m=km*1.6093442
        print(f"{km} Kms  in miles  is {m} miles")
        break
    else:
        print("Enter either 1 or 2 \n")
        
import os
from time import sleep
sleep(3)
os.system('cls')
        
