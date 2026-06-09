import numpy as np

# It is used when we want to replace nan values to specific values 
# The default value is 0

# Syntax = np.nan_to_num(array , nan = value)

array = np.array([1,2,np.nan,3,4,np.nan])
cleaned_array = np.nan_to_num(array ,nan = 3)
print(cleaned_array)