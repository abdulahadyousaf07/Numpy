import numpy as np 

# It sums all the elements of the array
# Whether it is 2d or 1d or any other dimension it always take all elements and sum it 

# 1D array
array_1D = np.array([1,2,3,4])
print(np.sum(array_1D))

# 2D array
array_2D = np.array([[1,2],[3,4]])
print(np.sum(array_2D))

# 3D array
array_3D = np.array([[[1],[2]],[[3],[4]]])
print(np.sum(array_3D))