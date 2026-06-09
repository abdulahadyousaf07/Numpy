import numpy as np

# V-stack (row wise)
# It increases number of rows
# It join arrays like first row and second row

array_1 = np.array([1,2,3,4,5])
array_2 = np.array([6,7,8,9,10])

new = np.vstack((array_1 , array_2))
print(new)

# H-stack (columns wise)
# It increases number of columns
# It join arrays like each element in new columns

array_1 = np.array([1,2,3,4,5])
array_2 = np.array([6,7,8,9,10])

new = np.hstack((array_1 , array_2))
print(new)