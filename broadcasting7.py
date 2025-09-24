import numpy as np
# 3. Add a column vector to a matrix
# Given:
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
c = np.array([[100],
              [200],
              [300]])
# → Add c to each column of A.
d=A+c
print(d)