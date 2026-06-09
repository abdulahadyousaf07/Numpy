import numpy as np

# Without Vectorisation

list_1 = [1,2,3]
list_2 = [4,5,6]

result = [x+y for x,y in zip(list_1 , list_2)]
# The above one adds the first element from 1st list with 1st element of 2nd list and so on 
print(result)


print()   # for spacing
# With Vectorisation
array_1 = np.array([1,2,3])
array_2 = np.array([4,5,6])

result = array_1 + array_2
print(result)