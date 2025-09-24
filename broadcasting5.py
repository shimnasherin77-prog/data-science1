import numpy as np

# 1. Add a scalar
# Given:
arr = np.array([5, 10, 15])
# → Add 3 to every element using broadcasting.
arr1=np.array([3])
c=arr+arr1
print(c)