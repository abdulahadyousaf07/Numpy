#In python
list = [1, 2, 3, 4, 5]
print(list)   #With Commas

temperature = [35.8 , 45.0 , 33.9 , 0.0]
total = 0
for temp in temperature:
    total += temp
    
avg = total/len(temperature)
print(avg)

#In numpy 
import numpy as np
array = np.array([1, 2, 3, 4, 5]) #Without commas

print(array)
temperature =np.array([35.8 , 45.0 , 33.9 , 0.0])
average = np.mean(temperature)
print(average)