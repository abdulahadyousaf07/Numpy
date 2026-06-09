import numpy as np 

# It finds the middle value
# If the number of elements is odd then it gives you the middle value
# If the number of elements is even then it gives average of middle two values
# Whether it is 2d or 1d or any other dimension it always take all elements and calculates its average 

# 1D array
array_1D = np.array([1,2,3,4,5])
print(np.median(array_1D))

# 2D array
array_2D = np.array([[1,2],[3,4]])
print(np.median(array_2D))

# 3D array
array_3D = np.array([[[1],[2]],[[3],[4]]])
print(np.median(array_3D))