import numpy as np

ages = np .array([[25, 30, 35,34,17],
                  [40, 45, 50,33,19]])

teenagers = ages < 20

adults = ages >= 20 

print(teenagers)  # Output: [[False False False False  True]
print(adults)     # Output: [[ True  True  True  True False]