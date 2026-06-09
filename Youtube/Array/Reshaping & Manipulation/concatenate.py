import numpy as np

#----------------------------------------
# 1d array
# Using concatenate() function
# Syntax = concatenate(array1 , array2)
array_1 = np.array([1,2,3,4,5])
array_2 = np.array([6,7,8,9,10])

join = np.concatenate((array_1 , array_2))
print(join)

#----------------------------------------
# 2d array
# Using concatenate() function
# Syntax = concatenate(array1 , array2)
array_1 = np.array([[1,2,3]])
array_2 = np.array([[4,5,6]])

join_0 = np.concatenate((array_1 , array_2), axis=0) # v-stack
join_1 = np.concatenate((array_1 , array_2), axis=1) # h-stack
print(join_0)
print(join_1)