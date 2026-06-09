# Identity matrix = 1 at diagnols and 0 elsewhere
#   | 1  0 |
#   | 0  1 |
# To create this matrix we use eye() function

# Note = In eye we do not pass tuple in no of rows or either at that place like this eye((8)) ❌
# If this happened then the dtype won't work with it

import numpy as np

#-------------------------------
# Simple Identity Matrix
# Syntax = eye(size)
identity_matrix_simple = np.eye(4)
print(identity_matrix_simple)

#-------------------------------
print() #for spacing
# 2D Identity Matrix
# Syntax = eye(no of rows , no of cols)
identity_matrix_2D = np.eye(4)
print(identity_matrix_2D)

#-------------------------------
print() #for spacing
# Identity Matrix with specifying shape
# Syntax = eye((no of rows , no of cols) , dtype = datatype)
identity_matrix_with_dtype = np.eye(4,4 , dtype = int)
print(identity_matrix_with_dtype)