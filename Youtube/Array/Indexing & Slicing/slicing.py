import numpy as np

# It is used to pull out specific number of elements on the basis of step we provide
#Syntax = array[start:stop:step]
#[no of index of element from which we want to start : no of index of element from which we want to end : (number of values we want to skip)-1 ]

# The end index is not included the included one element is index-1

array = np.array([1,2,3,4,5,6])

print(array[::1]) #Print whole array
print(array[::2]) #Take whole array but pick the every 2nd element
print(array[:4]) #index 0 to 3
print(array[::-1]) #reverse the array