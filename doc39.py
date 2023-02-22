# l=[[0, 1, 2,'',''], [2, 3, 4,'',''], [3, 4, 5, 6,''], [7, 8, 9, 10, 11], [12, 13, 14,'','']]
# c=[]
# for i in range(len(l)):
#     sum=0
#     s=0
#     for j in range(len(l)):
#         b=l[j][i]
#         if type(b)==int:
#             sum+=b
#         if b=="":
#             s=s+0
#         else:
#             s=s+1
#     avg=sum/s
#     c.append(avg)
# print(c)

#    OR 

# i=0
# while i<len(l):
#     j=0
#     sum=0
#     k=0
#     while j<len(l):
#         b=l[j][i]
#         if type(b)==int:
#             sum=sum+b
#         if b=="":
#             k=k+0
#         else:
#             k+=1
#         j+=1
#     print(k)
#     avg=sum/k
#     c.append(avg)
#     i+=1
# print(c)
                                                                                                                                                                                                                                                                                                                                                                           
# a=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     s=0
#     while j<len(a):
#         s=s+a[j][i]
#         c=s/len(a)
#         j+=1
#     b.append(c)
#     i+=1
# print(b)

a=[[0, 1, 2,0,0], [2, 3, 4,0,0], [3, 4, 5, 6,0], [7, 8, 9, 10, 11], [12, 13, 14,0,0]]
i=0
c=[]
while i<len(a):
    j=0
    s=0
    k=0
    while j<len(a):
        b=a[i][j]
        if type(b)==int:
            s=s+b
        if b=="":
            k=k+0
        else:
            k=k+1
        j+=1
    avg=s/k
    c.append(avg)
    i+=1
print(c)       







                                                                                                                                                                                                                                                                                                                                                       