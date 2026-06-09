import numpy as np

#The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
#The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
#The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

#---------------------------------------------------------------------------------
#COPY Array
#It creates a completely new array with its own independent memory, separate from the original array
arr_copy = np.array([1, 2, 3, 4, 5])
copy = arr_copy.copy()
arr_copy[0] = 42

print(arr_copy)
print(copy)

#---------------------------------------------------------------------------------
# VIEW Array
#.view() does not copy data; it creates a new NumPy array that shares the same underlying memory buffer as the original array.
arr_view = np.array([1, 2, 3, 4, 5])
view = arr_view.view()
arr_view[0] = 42

print(arr_view)
print(view)

#---------------------------------------------------------------------------------
#As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
#Every NumPy array has the attribute base that returns None if the array owns the data.
#Otherwise, the base  attribute refers to the original object.

arr_base = np.array([1, 2, 3, 4, 5])

x = arr_base.copy() # x has its own data like it contains all the dat of arr_base 
y = arr_base.view() # y has no data 

print(x.base)
print(y.base)
