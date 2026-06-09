#By using full we can put default values in array as our own choice
#It is used to fill array now and i future it can contain data
#Syntax = np.full((no of elements) , value)  
import numpy as np

default_array_1D = np.full((3) , 5)
print(default_array_1D)

#To create a default 2D array
#Syntax = np.full((no of rows , no of cols) , value)  
default_array_2D = np.full((3, 3) , 3)
print(default_array_2D)

#We can also specify the datatype of default values
#Syntax = np.full(() , dtype = datatype)
dtype_array = np.full((3) , 5 , dtype = str)
print(dtype_array)