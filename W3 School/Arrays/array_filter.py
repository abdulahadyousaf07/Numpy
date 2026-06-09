# Getting some elements out of an existing array and creating a new array out of them is called filtering. In NumPy, you filter an array using a boolean index list.

import numpy as np
array = np.array([41, 42, 43, 44])
# Create an empty list
filter_array = []
# go through each element in arr
for element in array:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_array.append(True)
  else:
    filter_array.append(False)
new_array = array[filter_array]

print(filter_array) #It gives boolean values
print(new_array)    #It gives filtered values


#----------------------------------------------------
print() #for spacing
#Creating Filter Directly From Array
direct_array = np.array([41, 42, 43, 44])
direct_filter_array = direct_array > 42
direct_new_array = direct_array[direct_filter_array]
print(direct_filter_array)
print(direct_new_array)