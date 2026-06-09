#---------------------------------------------------------------------------------## dtype is used to check the data type of array
import numpy as np
arr_int = np.array([1 , 2 , 3 , 4 , 5])
data_type_int = arr_int.dtype
print(data_type_int)
# Output = int64

arr_str = np.array(['apple' , 'banana' , 'orange' , 'mango' , 'pineapple'])
data_type_str = arr_str.dtype
print(data_type_str)
# <U9  (9 is because it represents the max letter in single like longest word in array)

#---------------------------------------------------------------------------------
# Defined Data type
# arrayName = np.array([elements], dtype='data_type')   data_type is any like int , string or whatever you want

# Byte String uses 'S' dtype
# Unicode String uses 'U' dtype

def_array_1 = np.array([1.0 , 2.0 , 3.0 , 4.0 , 5.0])
print(def_array_1.dtype) #Output float64

#Byte String
def_array = np.array([1.0 , 2.0 , 3.0 , 4.0 , 5.0] , dtype = 'S')
print(def_array.dtype)
print(def_array)

#Unicode String
def_array = np.array([1.0 , 2.0 , 3.0 , 4.0 , 5.0] , dtype = 'U')
print(def_array.dtype)
print(def_array)

#---------------------------------------------------------------------------------
# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
# The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
# newName = actualArrayName.astype('data_type')
#It does not change the real array but make copy of array and change in copy

as_array = np.array([1.0 , 2.0 , 3.0 , 4.0 , 5.0])
new_arr = as_array.astype('i')
print(as_array)
print(new_arr)