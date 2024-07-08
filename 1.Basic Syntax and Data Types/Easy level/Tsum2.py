

# def twoSum( nums, target):
        
#         n=len(nums)
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 if nums[i]+nums[j]==target:
#                     return[i,j]
#         return []     
    
nums=[int(i) for i in input("Enter a numerical list separated by comma:").split(",")]
target=int(input("Enter Target: "))  
n=len(nums)
# for i in range(n-1):
#     for j in range(i+1,n):
#         if nums[i]+nums[j]==target:
#             print(i,j)       
# result=twoSum(nums,target)

numset={}
for i in range(n):
    numset[nums[i]]=i
    print(numset[nums[i]]) 
# a-b=target
# b=target-a 2,3,4,5
# Find the complement
for i in range(n):
    complement = target - nums[i]
    if complement in numset :
        print([i, numset[complement]] ) 
# import os 
# from time import sleep
# sleep(5)
# os.system('cls')