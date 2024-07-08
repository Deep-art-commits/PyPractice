# Normalize the array [1, 2, 3, 4, 5] so that the sum of its elements is 1.
import numpy as np
array= [1, 2, 3, 4, 5]
n_arr=array/np.sum(array)
print(n_arr,np.sum(n_arr))