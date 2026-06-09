# When working with multidimensional data shape used to find its dimension 
import numpy as np

#----------------------------------
#2D array
array_2D = np.array([[1,2,3] ,
                  [4,5,6]])
shape_2d = array_2D.shape
print(shape_2d)
#Output = (2 , 3) -> (no. of rows , no. of cols)

#----------------------------------
#1D array 
array_1D = np.array([1,2,3,4,5])
shape_1D = array_1D.shape
print(shape_1D)
#Output = (5,)  (no of elements)

#----------------------------------
#3D array 
array_3D = np.array([[[1],
                      [2],
                      [3]] ,
                     
                     [[4],
                      [5],
                      [6]]])
shape_3d = array_3D.shape
print(shape_3d)
#Output = (2,3,1) -> (no. of blocks , no. of rows in single block , no of cols)