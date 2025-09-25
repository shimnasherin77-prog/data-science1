import numpy as np
array=np.array([[1,2,3,4,5],
                [6,7,8,9,10]])
print("sum of all elements:",np.sum(array))
print("mean:",np.mean(array))
print("max:",np.max(array))
print("min:",np.min(array))
print("argmax:",np.argmax(array))#highest index of array
print("argmin:",np.argmin(array))#lowest index of array
print("column wise sum:",np.sum(array,axis=0))#sum across column
print("row wise sum:",np.sum(array,axis=1))#sum across rows
print("product of all elements:",np.prod(array))
print("count of an array:",array.size)
rand_array=np.random.randint(1,101,size=15)#any 15 random numbers from 1 to 100
print(rand_array)