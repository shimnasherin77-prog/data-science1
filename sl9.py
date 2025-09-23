# 4. Given:
# arr = np.array([[100, 200, 300],
#                 [400, 500, 600],
#                 [700, 800, 900]])
# → Slice out the first two rows and last two columns.
import numpy as np
arr = np.array([[100, 200, 300],
            [400, 500, 600],
              [700, 800, 900]])
print(arr[0:2,1:3])