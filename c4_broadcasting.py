#broadcasting allows numpy to work with arrays of different shapes when performing arithmetic operations. Frequently we have a smaller array and a larger array, and we want to use the smaller array multiple times to perform some operation on the larger array.
#with differnet shapes by virtually expanding the smaller array across the larger array so that they have compatible shapes. This is called broadcasting.
#so they match the larger arrays shape

#dimension have same size or one of them is 1

import numpy as np

array1 = np.array([[1, 2, 3]])
array2 = np.array([[4], [5], [6]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)
