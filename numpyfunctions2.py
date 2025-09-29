import numpy as np
# ⿡ reshape() – Change the shape of an array
# =======================================
# Q1: Given the array:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# → Reshape it into a 4x2 2D array and print the result
b=arr.reshape(4,2)
print("1)",b)
# ⿢ flatten() – Convert multi-dimensional array into 1D
# =======================================
# Q2: Given:
arr2D = np.array([[10, 20], [30, 40], [50, 60]])
# → Convert this 2D array into a 1D flattened array and print it
b=arr2D.flatten()
print("2)",b)
# =======================================
# ⿣ ravel() – Similar to flatten(), returns a view (faster)
# =======================================
# Q3: Given:
arr = np.array([[1, 2, 3], [4, 5, 6]])
# → Use ravel() to convert it into 1D and change the 0th element of the result to 100
# → Check if the original array changes
c=arr.ravel()
c[0]=100
print("3)",c)
print("3)",arr)#Original after modification

# ⿤ transpose() / .T – Swap rows and columns
# =======================================
# Q4: Given:
arr = np.array([[1, 2, 3], [4, 5, 6]])
# → Transpose this array and print both the original and transposed arrays
# → What is the new shape?
d=arr.transpose()
print("4)",arr,d,d.shape)
# ⿥ concatenate() – Join two or more arrays
# =======================================
# Q5: Given: 
a=np.array([10, 20, 30]) 
b=np.array([40, 50, 60])
# → Concatenate these two arrays into one 1D array
# → Also try concatenating them column-wise as a 2D array
b=np.concatenate((a,b),axis=0)
print("5)",b)
# ⿦ vstack() and hstack() – Stack vertically or horizontally
# =======================================
# Q6: Given: 
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# → Stack them vertically (as rows)
# → Stack them horizontally (as one long array)
# → Print both results
c=np.vstack((a,b))
d=np.hstack((a,b))
print("6)",c)
print("6)",d)
#split() – Split an array into multiple parts (1D)
# =======================================
# Q7: Given: 
arr = np.array([5, 10, 15, 20, 25, 30])
# → Split this array into 3 equal parts and print each part
b=np.split(arr,3)
print("7)",b)
# =======================================
# ⿨ split() – Split an array into multiple parts (2D)
# =======================================
# Q8: Given:
arr2D = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# → Split this 2D array into 2 equal parts along rows and print them
b=np.split(arr2D,2)
print("8)",b)
# =======================================
# ⿩ unique() – Find unique elements in an array
# =======================================
# Q9: Given:
arr = np.array([2, 4, 4, 2, 5, 5, 7, 7, 7])
# → Find all the unique values and how many times each occurs
b=np.unique(arr)
print("9)",b)
# 🔟 Mixed Challenge
# =======================================
# Q10: Given: 
arr = np.array([[1, 2, 2], 
                [3, 4, 4], 
                [5, 6, 6]])
# → Flatten it
# → Find the unique values
# → Reshape it into a (2, -1) shape
# → Transpose the reshaped result
c=arr.flatten()
print("10)",c)
f=np.unique(c)
print("10)",f)
d=f.reshape(2,-1)
print("10)",d)
e=d.transpose()
print("10)",e)