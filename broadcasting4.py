import numpy as np
a=np.array([1,2,3])#shape(3,)
b=np.array([1,2])#shape(2,)
c=a+b
print(c)#we cannot broadcast because of the rows and columns of a and b