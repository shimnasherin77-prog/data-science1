# 3. From the array:
# arr = np.arange(1, 26).reshape(5, 5)
# → Extract the last column using slicing.
import numpy as np
arr = np.arange(1, 26).reshape(5, 5)
print(arr[0:5,-1])