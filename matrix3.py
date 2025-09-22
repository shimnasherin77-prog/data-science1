# 8. Given:
# A = np.array([[2, 0], [1, 3]])
# B = np.array([[1], [4]])
# → Perform matrix multiplication (A @ B) and explain the result.
import numpy as np
A = np.array([[2, 0], [1, 3]])
B = np.array([[1], [4]])
print(A@B)
#first we need to multipy Ath first row and B th col 2*1 and 0*4 and 
# then ath second row and column 1*1 and 3*4 and we need to sum 2+0 
# and 1+12 