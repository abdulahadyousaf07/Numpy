import numpy as np

# In this to do a broadcasting there is rule
# Number of columns in 2D = Number of elements in 1D
# If not then It gives error
# The same matrix rule that we studied in grade 9 applied here

matrix = np.array([[1,2,3],[4,5,6]]) #shape(2,3)
vector = np.array([10,20,30]) # shape(3)

# it can be calculated as 
# shape(2,3)
# shape( ,3)   3 and 3 are same

result = matrix + vector
print(result)

# to avoid thi we use reshape()