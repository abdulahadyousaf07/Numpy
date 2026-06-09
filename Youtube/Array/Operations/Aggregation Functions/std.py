import numpy as np 

# It can be calculated by following method
# Find mean
# Subtract mean from each value separately
# Square each result
# Take sum
# Divide by N(no of elements in array) and take square root
    
# 1D array
array_1D = np.array([1,2,3,4])
print(np.std(array_1D))

# 2D array
array_2D = np.array([[1,2],[3,4]])
print(np.std(array_2D))

# 3D array
array_3D = np.array([[[1],[2]],[[3],[4]]])
print(np.std(array_3D))