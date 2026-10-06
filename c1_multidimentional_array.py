import numpy as np
array = np.array([[["a", "b", "c"],["e", "f", "g"], ["h", "i", "j"]],
                  [["s", "t", "u"], ["v", "w", "x"], ["y", "z", "a"]],
                  [["b", "c", "d"], ["e", "f", "g"], ["h", "i", "j"]]])
print(array.ndim)
print(array.shape)
print(array[0, 0, 0])