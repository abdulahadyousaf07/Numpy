import numpy as np 

# It finds the maximum number and return it

# 1D array
array_1D = np.array([1,2,3,4])
print(np.max(array_1D))

# 2D array
array_2D = np.array([[1,2],[3,4]])
print(np.max(array_2D))

# 3D array
array_3D = np.array([[[1],[2]],[[3],[4]]])
print(np.max(array_3D))