# a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# i=0
# d=[]
# b=[]
# while i<len(a):
#     n=a[i]
#     if n>a[2]:
#         d.append(n)
#     else:  et       
#         b.append(n)
#     i+=1
# list3=d+b
# print(list3)

#    O/P:['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']

#        AND 

a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i=0
b=[]
c=[]
while i<len(a):
    n=a[i]
    if n>a[2]:
        b.append(n)
    else:
        c.append(n)
    i+=1
k=b+c
print(k)


