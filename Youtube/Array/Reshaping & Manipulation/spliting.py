import numpy as np

# It is used to divides the array into multiple array
# In this the number of elements must be even 
# Syntax = np.split(array , number of new array)
array = np.array([1,2,3,4,5,6])
new = np.split(array , 2)
print(new)