import numpy as np

# size returns total number of elements

#----------------------------------
# 1D array
array_1D = np.array([1,2,3,4,5])
size_1D = array_1D.size
print(size_1D)  # Gives total number of elements

#----------------------------------
# 2D array
array_2D = np.array([[1,2] , [3,4]])
size_2D = array_2D.size
print(size_2D)  # Output -> (4) (no of elements either in 2d counts all elements)