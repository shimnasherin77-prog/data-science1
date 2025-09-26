import numpy as np
# 10. Filter with Logical NOT (~)
# Given:
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
# → Filter all elements NOT greater than 40
# → Compute the mean of these remaining elements
arr1=arr[~(arr > 40)]
print(arr1)
print("mean:",np.mean(arr1))

# 11. Create a 5×5 array of random integers between 1 and 100
# → Filter elements that are multiples of 5
# → Find their sum, mean, and total count
arr=np.random.randint(1,101,size=(5,5))
arr1=arr[arr % 5 == 0]
print(arr1)
print("sum:",np.sum(arr1))
print("mean:",np.mean(arr1))
print("count:",np.size(arr1))