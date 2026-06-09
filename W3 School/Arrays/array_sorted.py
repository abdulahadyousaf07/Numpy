# Sorting means putting elements in an ordered sequence. Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending. The NumPy ndarray object has a function called sort(), that will sort a specified array.

# Note: This method returns a copy of the array, leaving the original array unchanged.

import numpy as np 
array = np.array([3, 2, 1, 6, 4, 5]) # Un-sorted array
sort_array = np.sort(array)
print(sort_array)
# We can also sort boolean and Strings array
#Boolean -> False , True
#String -> on the basis of place values 


#----------------------------------------------
print() #for spacing
# Sorting 2D array
# The elements in 1d array is sorted lonely no element move form one to another 1d array in 2d array
array_2d = np.array([[3, 2, 4] , [5, 0, 1]])
sort_array_2d = np.sort(array_2d)
print(sort_array_2d)
