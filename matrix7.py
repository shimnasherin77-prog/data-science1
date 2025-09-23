# 7. Verify the shape of the result when multiplying a (4, 3) matrix with a (3, 2) matrix.
import numpy as np
A=np.array([[1,2,3],
           [3,2,1],
           [4,5,6],
           [6,7,8]])
B= np.array([[4,5],[6,7],[8,9]])
c=A@B
print(c.shape)
    