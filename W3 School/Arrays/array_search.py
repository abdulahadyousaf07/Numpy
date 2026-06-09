#You can search an array for a certain value, and return the indexes that get a match.To search an array, use the where() method.

# If array is not sorted then numpy assumes it is sorted in searchsorted applying 

import numpy as np
array = np.array([1, 2, 3, 4, 5])
search_array = np.where(array == 4)
print(search_array)
#The example above will return a tuple: (array([3]),)Which means that the value 4 is present at index 3.


#-----------------------------------------------
print() #for spacing
#Formulas inside where
array_formula = np.array([1, 2, 3, 4, 5])
search_formula = np.where(array_formula%2 != 0)  #Formula to find index of odd numbers in array
print(search_formula)


#-----------------------------------------------
print() #for spacing
#Search Sorted
#There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
#The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.
array_sort = np.array([1, 2, 3, 4, 5])
search_sort = np.searchsorted(array_sort , 3)
print(search_sort)


#-----------------------------------------------
print() #for spacing
#It is useful when we have duplicates number in the array and we want to add the new number after the last duplicate number in array
# Start searching from the right side then we have to give side after number
right_array = np.array([1, 2, 2, 3, 4, 5])
search_right = np.searchsorted(right_array , 2 , side = 'right')
print(search_right)


#-----------------------------------------------
print() #for spacing
#np.searchsorted() assumes the array is sorted in ascending order by default. in descending order we have to reverse the list by using
# len(arrayName) - searchsorted(arrayName[::-1, number])
desc_array = np.array([9, 8, 7, 6, 5])
desc_sort = len(desc_array) - np.searchsorted(desc_array[::-1] , 9)
print(desc_sort)


#-----------------------------------------------
print() #for spacing
#Multiple Values
multi_array = np.array([1, 3, 5, 7])
multi_search = np.searchsorted(multi_array, [2, 4, 6])
print(multi_search)