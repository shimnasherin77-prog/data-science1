lst=[[1,2,3],[4,5,6],[7,8,9]]
a=[]
b=[]
for i in lst:
    for j in i:
        n=j*5
        a.append(n)
        n=0
    b.append(a)  
    a=[]     
print(b)