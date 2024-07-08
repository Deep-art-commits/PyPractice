# Create an array of all zeros with the same shape as the array [1, 2, 3].
import numpy as np
arr=np.array([1,2,3])
z=np.zeros_like(arr)
z1=np.zeros((3,3))
print(z,z1)