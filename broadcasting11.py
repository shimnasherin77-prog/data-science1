import numpy as np
# 7. Subtract two arrays
# Given:
a = np.array([[1, 2, 3]])
b = np.array([[10],
              [20],
              [30]])
# → Subtract a - b using broadcasting. What is the result shape?
c=a-b
print(c.shape)