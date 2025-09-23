# 10. Write a program to generate two (3, 3) matrices with random integers and compute:
#     - A @ B (matrix multiplication)
#     - A * B (element-wise multiplication)
# → Compare the outputs.
import numpy as np
A=np.array([[2,4,6],[4,8,12],[6,12,18]])
B=np.array ([[3,4,6],
            [6,7,8],
            [8,5,8]])
print(A@B)#in this ,matrix multiplication is done here

print(A*B)#in this,directly multiply  the elements in A and B matrix