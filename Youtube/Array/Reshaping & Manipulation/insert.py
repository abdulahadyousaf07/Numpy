import numpy as np

# Syntax = np.insert(array , index , value , axis)
# axis = 0   (You are inserting data in rows)
# axis = 1   (You are inserting data in columns)

# It creates a new array and the original array remain unchanged

#-----------------------------------
# 1D array
array_1D = np.array([1,2,3,4,5])
add_1D = np.insert(array_1D, 3 , 0)
print(add_1D)

#-----------------------------------
# 2D array
# In this we use axis as a fourth parameter
# axis = 0    (You are inserting data in rows)
# axis = 1    (You are inserting data in columns)
# axis = none (It adds the value in flattened version like it takes the 2d array as 1d array and add value at their index)
array_2D = np.array([[1,2,3],
                     [4,5,6]])
add_2D = np.insert(array_2D , 0 , 0)
print(add_2D)