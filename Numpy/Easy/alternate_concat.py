# word1='abc'
# word2='cdefg'
# word3=[]
# word4=[]
# i=0

# l1=len(word1)
# l2=len(word2)
# if(l1>l2):
#     m=l1
# else:
#     m=l2    

# while i<l1 or i<l2:
#     if i<l1:
#         word3.append(word1[i])
#     if i<l2:
#         word3.append(word2[i])
#     i+=1
# print("".join(word3))  
# for i in range(m):
#     if i<l1:
#         word4.append(word1[i])
#     if i<l2:
#         word4.append(word2[i])
# print("".join(word4))          
            
            
s="abc"
t="abce"
n=[]
for i in t:
    if(t.count(i)>s.count(i)):
        print(i)             