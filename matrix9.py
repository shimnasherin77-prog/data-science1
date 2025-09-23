# 9. Create a (4, 4) identity matrix using NumPy and multiply it with a (4, 4) random integer matrix.
# → What do you observe?

# Identity matrix , I = [[1 0 0 0]
#                        [0 1 0 0]
#                        [0 0 1 0]
#                        [0 0 0 1]]
import numpy as np
I = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
A=np.array([[3,4,6,7],[4,3,4,5],[6,7,8,9],[8,5,8,6]])
print(I@A)
# when we multipy any matrixes with identity matrix answer will be that matrix