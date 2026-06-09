#By using ones we can put default values in array as 1
#It is used to fill array now and i future it can contain data
#Syntax = np.ones((no of elements))  
import numpy as np

default_array_1D = np.ones((3))
print(default_array_1D)

#To create a default 2D array
#Syntax = np.ones((no of rows , no of cols))  
default_array_2D = np.ones((3, 3))
print(default_array_2D)

#We can also specify the datatype of default values . It is float by default
#Syntax = np.ones(() , dtype = datatype)
dtype_array = np.ones((3) , dtype = int)
print(dtype_array)