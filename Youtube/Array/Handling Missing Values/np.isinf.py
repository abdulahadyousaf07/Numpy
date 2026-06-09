import numpy as np 

#------------------------------------
# It is used to handle infinite numbers
# It returns boolean array
# Syntax = np.isinf(array)

array = np.array([1,2,3,np.inf,4,-np.inf,6])
print(np.isinf(array))

#------------------------------------
# Now replacing infinite values to specific number
# Syntax = np.nan_to_num(array , posinf(to replace positive infinite value in array) = value , neginf(to replace negative infinite value in array) = value)
cleaned_arr = np.nan_to_num(array , posinf = 1 , neginf = -1)  # -  posinf = positive infinity
print(cleaned_arr)