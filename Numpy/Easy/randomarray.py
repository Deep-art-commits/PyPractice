import numpy as np
a=np.random.rand(2,2)
b=np.random.randn(2,2)
c=np.random.randint(1,10,3)
d=np.random.random_sample((3,3))
# Create a 3x3x3 array with random values.
e=np.random.randint(1,100,27).reshape(3,3,3)
print(f"a={a}\nb={b}\n c={c}\n d={d}\n e={e}")