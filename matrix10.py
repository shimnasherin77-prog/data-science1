# 10. Write a program to generate two (2, 3) and (3, 2) random integer matrices.
#     - Compute A @ B (valid matrix multiplication).
#     - Try B @ A (check the result shape).
# → Compare the two outputs.
import numpy as np
A=np.array([[2,4,7],[6,8,7]])
B=np.array([[1,4],[4,5],[6,3]])
c=B@A
d=A@B
print(A@B)
print(c.shape)
print(d.shape)
#the shape of 2 matrices are different