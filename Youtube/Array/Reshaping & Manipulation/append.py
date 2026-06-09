import numpy as np

# Syntax = np.append(array , value)
# It add the value at the end of the array 
# It also return the copy of the array not the original array

array = np.array([1,2,3,4,5])
new = np.append(array , [6,7,8,9,10])

print(array)
print(new)