import numpy as np

# Syntax = np.delete(array , index)
# Syntax = np.delete(array , [index,index...])  To delete multiple values
# It return the new array and the original one remain same

array = np.array([1,2,3,4,5])
new = np.delete(array , [1,2,3,4])

print(new)

# 2D array
print() # for spacing
# Syntax = np.delete(array , index , axis)
# axis = 0  (rows index)
# axis = 1  (cols index)
array_2d = np.array([[1,2,3],
                     [4,5,6]])
print(np.delete(array_2d , 0, axis=0))
print(np.delete(array_2d , 0, axis=1))