# 7. Verify the shape of the result when multiplying a (3, 2) matrix with a (2, 4) matrix.
import numpy as np
a=np.array([[1,2],
    [4,5],
    [6,7]])
b=np.array([[2,3,4,5],
   [4,5,6,7]])
c=a@b
print(c.shape)
