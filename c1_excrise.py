#three letter words creat with array and write my name
import numpy as np
array = np.array([[["a", "b", "c"],["e", "f", "g"], ["h", "i", "j"]],
                  [["s", "t", "u"], ["v", "w", "o"], ["y", "z", "a"]],
                  [["b", "c", "d"], ["e", "n", "g"], ["h", "t", "j"]]])

word1 = array[1,0,0] + array[0,2,0]+ array [0,0,0] + array[2,1,1] + array[2,2,1] + array[1,1,2]
print(word1)    