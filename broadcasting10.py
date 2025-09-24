import numpy as np
# 6. Mix row and column vector
# Given:
a = np.array([[1],
              [2],
              [3]])
b = np.array([10, 20, 30])
# → Add a and b using broadcasting. Predict the shape.
c=a+b
print(c)