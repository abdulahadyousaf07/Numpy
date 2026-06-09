import numpy as np

# Use to find data type of the elements in array
# If array has elements that are of different type then dtype select data type on the basis of precision

# Order of precedence

# bool
#   ↓
# int8 → int16 → int32 → int64
#   ↓
# float16 → float32 → float64
#   ↓
# complex64 → complex128

# | Mixed Types       | Result dtype |
# | ----------------- | ------------ |
# | `bool + int`      | `int`        |
# | `int + float`     | `float`      |
# | `float + complex` | `complex`    |
# | `int + str`       | `str`        |
# | `str + list`      | `object`     |


array = np.array([1,2,3,4,5])
data_type = array.dtype
print(data_type)