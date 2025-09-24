import numpy as np
# 2. Add a row vector to a matrix
# Given:
A = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
# → Use broadcasting to add b to each row of A.
c=A+b
print(c)

