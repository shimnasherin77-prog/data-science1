lst=[[1,2,3,4,5,6],[1,2,3,4,5,6]]
a=[]
for i in range(len(lst[0])):
    a.append(lst[0][i]+lst[1][i])
print(a)