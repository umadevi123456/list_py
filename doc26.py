# n=[4, 5, 5, 5, 3, 8]
# i=0
# a=[]
# while i<len(n)-1:
#     k=n.count(n[i])
#     if k==3:
#         if n[i] not in a:
#             a.append(n[i])
#     i+=1
# print(a)

#   O/P:[5]

n=[1, 1, 1, 64, 23, 64, 22, 22, 22]
i=0
a=[]
while i<len(n):
    k=n.count(n[i])
    if k==3:
        if n[i] not in a:
            a.append(n[i])
    i+=1
print(a)

#    O/P:[1, 22]
