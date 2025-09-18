import numpy as np
nested_lst = [[1, 2, 3, 5, 9, 8],  [4, 5, 6, 7, 8, 9]]
new_arr = np.array(nested_lst)

print( new_arr[1, 0:4] )
print( new_arr[0:2, 1]  )  
print(new_arr[0:2, 1:4] ) 