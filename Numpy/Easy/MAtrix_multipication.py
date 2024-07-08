import numpy as np 

a,b=[int(i) for i in input("Enter size of matrix 1 (rows*columns): ").split(",")]
matrix1=3*np.random.random((a,b))
c,d=[int(i) for i in input("Enter size of matrix 2 (rows*columns): ").split(",")]
matrix2=3*np.random.random((c,d))
pr=np.zeros((a,d))
if b==c:
    print("Matrix Multipication  is possible")
    for i in range(a):
        for j in range(d):
            for k in range(b):
                pr[i][j]=matrix1[i][k]*matrix2[k][j]
    print(f"Product is {pr}")        
else:
    print("Matrix Multipication  is not possible")
        