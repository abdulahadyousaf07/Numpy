import numpy as np

# ndim = Number of Dimension
# It gives the number of dimensions

#----------------------------
print() #for spacing
array_1D = np.array([1,2,3,4])
dimension_1D = array_1D.ndim
print(dimension_1D)

#----------------------------
print() #for spacing
array_2D = np.array([[1,2],[3,4]])
dimension_2D = array_2D.ndim
print(dimension_2D)

#----------------------------
print() #for spacing
array_3D = np.array([[[1],[2]],[[3],[4]]])
dimension_3D = array_3D.ndim
print(dimension_3D)