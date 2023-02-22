list=[1,2,2,5,8,4,4,8]
b=[]
i=0
while i<len(list):
    if list[i] not in b:
        b.append(list[i])
    i+=1
print(b)


a=[1,2,2,5,8,4,4,8]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i+=1
print(b)




