import numpy as np
# 4. Multiply a matrix by a row vector
# Given:
A = np.array([[2, 4, 6],
              [1, 3, 5]])
b = np.array([1, 2, 3])
# → Multiply A by b elementwise using broadcasting.
c=A*b
print(c)