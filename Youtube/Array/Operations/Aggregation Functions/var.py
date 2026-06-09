import numpy as np 

# Variance is a measure of how spread out the data values are from the mean.
# Relation with Standard Deviation
# Standard Deviation = (Variance)^(1/2)
# Variance = (Standard Deviation)^2

# 1D array
array_1D = np.array([1,2,3,4])
print(np.var(array_1D))

# 2D array
array_2D = np.array([[1,2],[3,4]])
print(np.var(array_2D))

# 3D array
array_3D = np.array([[[1],[2]],[[3],[4]]])
print(np.var(array_3D))