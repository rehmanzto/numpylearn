import numpy as np

# comparision operators
scores = np.array([90, 80, 70, 60, 50])
print(scores > 70)
print(scores == 90)
print(scores == 100)
scores[scores < 60] = 0
print(scores)

