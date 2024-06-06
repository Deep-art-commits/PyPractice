# 7.	How do you remove duplicates from a list in Python?

import collections
lst=[int(i) for i in input("Enter numerical List: ").split(",")]
# print(f"original List is :{lst}")
# c_lst=list(set(lst))
# print(f" List after removing duplicates  is :{c_lst}")
r_lst=[]
c_lst=[]
[r_lst.append(k) for k,v in collections.Counter(lst).items() if v > 1]
[c_lst.append(j) for j in lst if j not in c_lst ]
print(f"original List is :{lst}")
print(f"Elements removed are: {r_lst}")
print(f" List after removing duplicates  is :{c_lst}")

# print([k for k, v in collections.Counter(l).items() if v > 1])
# # [3, 2, 1]

import os
from time import sleep
sleep(5)
os.system('cls')  

# lst=[1,1,2,2,3,4,5,6,6]
# print(collections.Counter(lst))