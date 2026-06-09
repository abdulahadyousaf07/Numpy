import numpy as np

## 1D array
arr1 = np.array([1, 2, 3 , 4 , 5 , 6])
## 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
## 3D array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

## ndim is used to print the number of dimensions in the array
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

## Method of applying custom number of dimensions to a 1D array
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)