import numpy as np 

# arr[start:end:step]
# If start is not given then it is 0
# If end is not given then it consider length of the array
# If step is not given then it is 1
# Stop means to print element till stop-1 not the stop index
# Step means to skip the element like if step is 2 and start is 0 then print 0 2 4 6 ..... , do not skip 2 elements between 
arr = np.array([1 , 2 , 3 , 4 , 5 , 6 , 7])
sliced_arr = arr[1:4]
print(sliced_arr)

# Negative Slicing
# In this we use negative indexes
#  1    2    3    4    5
# -5   -4   -3   -2   -1 
     
array = np.array([1 , 2 , 3 , 4 , 5])
sliced_array = array[-4:-1]
print(sliced_array)

# Slicing 2D array
# array[row_number , col_start:col_end] 
# array[row_number , column_number]
# array[row_start:row_end , col_start:col_end]

#            Columns
#           0   1   2     
#  Rows
#   0       1   2   3
#   1       4   5   6
array_2d = np.array([[1 , 2 , 3] , [4 , 5 , 6]])
sliced_array_2d = array_2d[0, 0:2]
print(sliced_array_2d)