import numpy as np
array=np.array([[50,60,40,89,90],
                [89,78,56,75,99]])
marks=array[array > 40]
print(marks)
marks1=array[(array > 40)&(array < 90)]#logical AND
print(marks1)
marks2=array[(array < 50)|(array > 90)]#Logical OR
print(marks2)
marks3=array[~(array > 50)]#logical NOT (tilde ~)in python and numpy
print(marks3)