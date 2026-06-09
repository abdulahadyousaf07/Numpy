#Iterating means going through elements one by one. As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python. If we iterate on a 1-D array it will go through each element one by one.

#---------------------------------------
#Iterating 1D array
import numpy as np
array1 = np.array([1 , 2 , 3 , 4 , 5])
for x in array1:
    print(x)
    
    
#---------------------------------------
print() # For spacing
# Iterating 2D array
array2 = np.array([[1 , 2 , 3] , [4 , 5 ,6]])
for x in array2: #It iterates through rows
    for y in x:  #It iterate through elements of rows on which x iterates
        print(y)


#---------------------------------------
print() # For spacing
# Iterating 3D array  
array3 = np.array([[[1, 2, 3] , [4, 5, 6]] , [[7, 8, 9] , [10, 11, 12]]])
for x in array3: #It iterate through 2d arrays
    for y in x:  #It iterates through rows of 2d arrays
        for z in y:  #It iterate through elements of rows on which y iterates
            print(z)
      
            
#---------------------------------------            
print() # For spacing
#Iterating 1D Array Using nditer()
n_array1 = np.array([1, 2, 3, 4, 5])
for x in np.nditer(n_array1):
    print(x)
    
    
#---------------------------------------            
print() # For spacing
#Iterating 2D Array Using nditer()
n_array2 = np.array([[1, 2] , [3 , 4]])
for x in np.nditer(n_array2):
    print(x)
    
    
#---------------------------------------            
print() # For spacing
#Iterating 3D Array Using nditer()
n_array3 = np.array([[[1, 2] , [3, 4]] , [[5, 6] , [7, 8]]])
for x in np.nditer(n_array3):
    print(x)
    
    
#---------------------------------------  
#NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered']. 
         
print() # For spacing

#Iterating Array With Different Data Types means we can iterate through array and also convert their elements data types , op_dtype['type in which element is converted']
diff_array = np.array([1, 2, 3])
for x in np.nditer(diff_array , flags = ['buffered'] , op_dtypes = ['float']):
    print(x)


#---------------------------------------  
print() # For spacing
#Iterating With Different Step Size in 1D array
step_array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
for x in np.nditer(step_array1[::2]): #2 is step number
    print(x)
    

#---------------------------------------  
print() # For spacing
#Iterating With Different Step Size in 1D array
step_array2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(step_array2[:,::2]): #2 is step number
    print(x)
    
    
#---------------------------------------  
print() # For spacing
#Iterating With Different Step Size in 1D array
step_array2 = np.array([[[1, 2], [3, 4]] , [[5, 6], [7, 8]]])
for x in np.nditer(step_array2[:,:,::2]): #2 is step number
    print(x)
    
    
#--------------------------------------- 
#Through enumeraton we can get the sequence or indexes of the elements 
print() # For spacing
# Enumerated Iteration Using ndenumerate()
#Enumeration means mentioning sequence number of somethings one by one.Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.

en_array1 = np.array([1, 2, 3])
for idx, x in np.ndenumerate(en_array1):
  print(idx, x)


#---------------------------------------  
print() # For spacing
#Enumerating 2D array
en_array2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(en_array2):
  print(idx, x)