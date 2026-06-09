import numpy as np

# It filters the elements from the array
# It is also called Boolean Masking
# It is faster than using loops from this as we done in w3 schools learning folder

array = np.array([1,2,3,4,5])

print(array[array > 2]) #print elements that are greater than 2