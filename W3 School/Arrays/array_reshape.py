#Reshaping means changing the shape of an array. The shape of an array is the number of elements in each dimension.By reshaping we can add or remove dimensions or change number of elements in each dimension.

#----------------------------------------
#1-D to 2-D
#reshape(no of arrays , no of elements in each array)
import numpy as np
array2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
reshape2 = array2.reshape(4 , 3)  # It means make 4 arrays each of 3 elements
print(reshape2)

#----------------------------------------
#1-D to 3-D
print()
array3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
reshape3 = array3.reshape(2 , 3 , 2)  # It means make 2 main arrays and then put 3 arrays each of element 2 in both main arrays
#Output = [[[1 2],[3 4],[5 6]] , [[7 8],[9 10],[11 12]]]
print(reshape3)

#The return is also view not copy like it contain view of original array not the copy
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base) #Output = [1, 2, 3, 4, 5, 6, 7, 8] means it is view

# If we want to calculate the number of elements in each array automatically then we pass -1
#.reshape(-1 , -1 , -1)  -> It is invalid

#----------------------------------------
# Multidimensional array to 1D array. The way is same from 3D to 1D and from 2D to 1D put -1 in reshape just.
multi_array = np.array([[1 , 2 , 3] , [4 , 5 , 6]])
multi_reshape = multi_array.reshape(-1)
print(multi_reshape)
