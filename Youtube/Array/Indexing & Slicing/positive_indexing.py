import numpy as np 

# It can be used to select specific element by using its index
 
# 1D array
array_1D = np.array([1,2,3,4,5])

print(f"1st element = {array_1D[0]}")
print(f"2nd element = {array_1D[1]}")
print(f"3rd element = {array_1D[2]}")
print(f"4th element = {array_1D[3]}")
print(f"5th element = {array_1D[4]}")

#---------------------------------
# 2D array
print()  #array
array_1D = np.array([[1,2,3],
                     [4,5,6]])

print(f"1st element of 1st row = {array_1D[0][0]}")
print(f"2nd element of 1st row = {array_1D[0][1]}")
print(f"3rd element of 1st row = {array_1D[0][2]}")
print(f"4th element of 2nd row = {array_1D[1][0]}")
print(f"5th element of 2nd row = {array_1D[1][1]}")
print(f"6th element of 2nd row = {array_1D[1][2]}")

#---------------------------------
# 3D array
print()  #array
array_1D = np.array([[[1,2],
                      [3,4]],
                     [[5,6],
                      [7,8]]])

print(f"1st element of 1st row of 1st block = {array_1D[0][0][0]}")
print(f"2nd element of 1st row of 1st block = {array_1D[0][0][1]}")
print(f"3rd element of 2nd row of 1st block = {array_1D[0][1][0]}")
print(f"4th element of 2nd row of 1st block = {array_1D[0][1][1]}")
print(f"4th element of 3rd row of 2nd block = {array_1D[1][0][0]}")
print(f"4th element of 3rd row of 2nd block = {array_1D[1][0][1]}")
print(f"4th element of 4th row of 2nd block = {array_1D[1][1][0]}")
print(f"4th element of 4th row of 2nd block = {array_1D[1][1][1]}")