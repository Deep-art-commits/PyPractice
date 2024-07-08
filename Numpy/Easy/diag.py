# Create a 5x5 matrix with values 1, 2, 3, 4 just below the diagonal.
import numpy as np
arr=np.diag([1,2,3,4],k=-1)
arr1=np.diag_indices
print(arr)
print(np.diag(arr))
a = np.zeros((2, 2, 2), dtype=int)
print(a)