import numpy as np

# =======================================
# ⿡ reshape() – Change the shape of an array
# =======================================

arr = np.array([4,5,6,7,8,9])
b= arr.reshape(2, 3)   # 2 rows, 3 columns
print("reshape():\n", b)
# ⿢ flatten() – Convert multi-dimensional array into 1D
# =======================================

arr2D = np.array([[4,5,6], [7, 8, 6]])
flat = arr2D.flatten()
print("flatten():", flat)
# ⿣ ravel() – Similar to flatten(), returns a view (faster)
# =======================================

arr2D = np.array([[11, 20], [33, 40]])
ravelled = arr2D.ravel()
print("ravel():", ravelled)
# ⿤ transpose() / .T – Swap rows and columns
# =======================================

arr2D = np.array([[4,5,6], [7,8,9]])
transposed = arr2D.transpose()  # or arr2D.T
print("transpose():\n", transposed)
# ⿥ concatenate() – Join two or more arrays
# =======================================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
joined = np.concatenate((a, b))
print("concatenate():", joined)

# 2D Example
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6],[6,7]])
C = np.concatenate((A, B),axis = 1)#axis o is default
print("concatenate 2D:\n", C)
arr = np.array([10, 20, 30, 40, 50, 60])
parts = np.split(arr, 3)
print("split():", parts)
# Output:
# [array([10, 20]), array([30, 40]), array([50, 60])]
# =======================================
# ⿨ unique() – Find unique elements in an array
# =======================================

arr = np.array([1, 6, 3, 3, 4, 6, 5])
unique_values = np.unique(arr)
print("unique():", unique_values)
# =======================================
# ⿦ vstack() and hstack() – Stack vertically or horizontally
# =======================================

a = np.array([4, 6, 8])
b = np.array([3, 5, 6])

vertical = np.vstack((a, b))
horizontal = np.hstack((a, b))

print("vstack():\n", vertical) # Row-wise
print("hstack():", horizontal) # Column-wise



