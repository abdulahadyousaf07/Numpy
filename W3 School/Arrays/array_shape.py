#NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding element
#The return value of the arr.shape is represented in a certain data type that is tuple

#---------------------------------------------
#1D array
import numpy as np
array1 = np.array([1 , 2 , 3 , 4])
shape1 = array1.shape

print(shape1)  #Output (4,)
#It gives total number of elements in return

#---------------------------------------------
#2D array
import numpy as np
array2 = np.array([[1 , 2 , 3 , 4] , [5 , 6, 7 , 8]])
shape2 = array2.shape

print(shape2)  #Output (2 , 4)
#It gives two values (no of elements as bracket , no of elements in bracket)

#---------------------------------------------
#3D array
import numpy as np
array3 = np.array([[[1 , 2 , 3 , 4] , [5 , 6, 7 , 8]],[[9 , 10 , 11 , 12] , [13 , 14 , 15 , 16]]])
shape3 = array3.shape

print(shape3)  #Output (2, 2, 4)
#It gives two values (no of elements as outer bracket , no of elements as inner bracket , no of elements in bracket)

arr = np.array([1, 2, 3, 4], ndmin=5)
shape_random = arr.shape
print(shape_random) # Output (1, 1, 1, 1, 4)
#It can write the first four values to default(1) and in end it write the no of elements in array
