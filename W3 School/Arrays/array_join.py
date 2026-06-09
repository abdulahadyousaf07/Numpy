import numpy as np

#For joining array we can use concatenate(array1 , array2) to join the two arrays
# Joining 1D array
print("Concatenate")
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])
join = np.concatenate((array1 , array2))
print(join)


#------------------------------------------
print()
# Joining 2D array
#axis = 0 means join vertically (It simply write down all sub arrays in 2d array in vertical form) like below
# [ [1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

#axis = 1 means join horizontally (It joins sub arrays elements of same array index, like it join 1st sub array in 1st main array elements to the 1st sub array in 2nd main array elements)
# [[1 2 5 6]
#  [3 4 7 8]]
print("Concatenate using axis")
array2_1 = np.array([[1, 2], [3, 4]])
array2_2 = np.array([[5, 6], [7, 8]])
arr_axis_0 = np.concatenate((array2_1, array2_2), axis=0)
arr_axis_1 = np.concatenate((array2_1, array2_2), axis=1)
print(arr_axis_0)
print(arr_axis_1)


#------------------------------------------
print()
# Joining Arrays Using Stack Functions , Stacking is same as concatenation, the only difference is that stacking is done along a new axis , If axis is not given then it is taken by default 0 , It makes a 2D shape
print("Stack using axis")
stack_array_1 = np.array([1 , 2 , 3])
stack_array_2 = np.array([4 , 5 , 6])
stack_join_axis_0 = np.stack((stack_array_1 , stack_array_2), axis = 0)
stack_join_axis_1 = np.stack((stack_array_1 , stack_array_2), axis = 1)

#axis = 0 mean joins vertically (It simply write down all sub arrays in 2d array in vertical form) like below
# [[1, 2, 3]
#  [4 , 5 ,6]]

#axis = It means join horizontally , in 1D array -> (It joins 1st elements of both array in separate array and then 2nd element and then so on)
# [[1 4]
#  [2 5]
#  [3 6]]

print(stack_join_axis_0)
print()
print(stack_join_axis_1)


#------------------------------------------
print()
# Stacking Along Rows
# NumPy provides a helper function: hstack() to stack along rows. Join all elements in one row
print("H-stack")
h_array1 = np.array([1, 2, 3])
h_array2 = np.array([4, 5, 6])
hstack_join = np.hstack((h_array1,h_array2))
print(hstack_join)


#------------------------------------------
print()
# Stacking Along Columns
# NumPy provides a helper function: vstack() to stack along columns. stacks arrays vertically (row-wise) , equivalent to axis=0 concatenation
print("V-Stack")
v_array1 = np.array([1, 2, 3])
v_array2 = np.array([4, 5, 6])
vstack_join = np.vstack((h_array1,h_array2))
print(vstack_join)


#------------------------------------------
print()
# Stacking Along Height (depth)
# NumPy provides a helper function: dstack() to stack along depth (third axis).
# It creates a new axis at the end and turns 1D or 2D arrays into a 3D array.
print("D-Stack")
d_array1 = np.array([1, 2, 3])
d_array2 = np.array([4, 5, 6])
dstack_join = np.dstack((d_array1,d_array2))
print(dstack_join)
