import numpy as np

# nan = not a number 
# When calculation fail and something is missing in data set then we use it
# It returns boolean array

# Syntax = np.isnan(array)
# We do not compare the np.nan values directly

array = np.array([1,2,np.nan,4,np.nan])
print(np.isnan(array))