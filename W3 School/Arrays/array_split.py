#Splitting is reverse operation of Joining. Joining merges multiple arrays into one and Splitting breaks one array into multiple. We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

#Note: We also have the method split() available but it will not adjust the elements when elements are less in source array for splitting like in example above, array_split() worked properly but split() would fail.

#Syntax = np.array(arrayName , number of arrays you want to make by splitting it)
# It return the list containing number of arrays we mention not arrays
import numpy as np
array = np.array([1, 2, 3, 4, 5, 6])
split_array = np.array_split(array , 4)
print(split_array)


#-----------------------------------------------------
print() #for spacing
# Split into Arrays
#If you split an array into 3 arrays, you can access them from the result just like any array element then use index to print them 
array = np.array([1, 2, 3, 4, 5, 6])
new_array = np.array_split(array , 3)
print(new_array[0])
print(new_array[1])
print(new_array[2])


#-----------------------------------------------------
print() #for spacing
# Splitting 2-D Arrays
#Syntax is same as above 
array_2d = np.array([[1, 2] , [3, 4] , [5, 6] , [7, 8] , [9, 10]])
split_array_2d = np.array_split(array_2d , 3)
print(split_array_2d)
# we also have axis in it
array_2d_axis_0 = np.array([[1, 2] , [3, 4] , [5, 6] , [7, 8] , [9, 10]])
array_2d_axis_1 = np.array([[1, 2] , [3, 4] , [5, 6] , [7, 8] , [9, 10]])
split_array_2d_axis_0 = np.array_split(array_2d , 3 , axis = 0)
split_array_2d_axis_1 = np.array_split(array_2d , 3 , axis = 1)
print(split_array_2d_axis_0)
print(split_array_2d_axis_1)


#-----------------------------------------------------
print() #for spacing
#hsplit that is opposite of hstack in joining arrays
array_hstack = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_array_hstack = np.hsplit(array_hstack, 3)
print(new_array_hstack)

#Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().