import numpy as np 

arr = np.array([11 , 22 , 33 , 44 , 55])
length_arr = len(arr)

for i in range (0 , length_arr):
    print(f"Value at {i} = {arr[i]}")

# Accessing 2D arrays
# It can arrange data like in form of columns and rows
#            Columns
#           0   1   2     
#  Rows
#   0       1   2   3
#   1       4   5   6
#   2       7   8   9 

a = np.array([[1 , 2 , 3] , [4 , 5 , 6] , [7 , 8 , 9]])
print(f"{a[0 , 0]} , {a[1 , 0]} , {a[2 , 0]}")


#Accessing 3D array
# It can be access like [layer][rows][columns]
#It makes layer and then store data in rows and columns
# It can arrange data like in form of columns and rows
# Layer 0
#            Columns
#           0   1   2     
#  Rows
#   0       1   2   3
#   1       4   5   6
#
#Layer 1
#            Columns
#           0    1    2     
#  Rows
#   0       10   20   30
#   1       40   50   60


b = np.array([[[1 , 2 , 3] , [4 , 5 , 6]] , [[10 , 20 , 30] , [40 , 50 , 60]]])
print(f"{b[0 , 0 , 0]} , {b[1 , 0 , 0]}")

#Negative Indexing
# -index used to access element from last of the array the last element starts from -1 not from 0
# [1 , 2 , 3 , 4 , 5]
#  0   1   2   3   4    Positive indexes
# -5  -4  -3  -2   -1   Negative indexes
c = np.array([1 , 2 , 3 , 4 , 5])
print(f"{c[4]} , {c[-5]}")