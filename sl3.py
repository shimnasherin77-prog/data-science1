# 3. From the array:
# arr = np.arange(1, 21).reshape(4, 5)
# → Slice the last two rows and first three columns.
import numpy as np
arr=np.arange(1,21).reshape(4,5)
print(arr[2:4,0:3])

