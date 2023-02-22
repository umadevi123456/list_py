a=[[1,2,3],[3,4,5]]
i=0
b=[]
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j+=1
    b.append(sum)
    i+=1
print(b)

# O/P:[6, 12]

# a=[["red"],["rohini"],["amla"],["archana"],["deepti"],["deep"]]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     j=0
#     while j<len(a[j]):
#         count=a.count(a[i])
#     if a[i] not in b:
#         b.append(a[i])
#         v=a[i],count
#         c.append(list(v))
#         j+=1
#     i=i+1
# print(c)

# n=(input("enter number"))
# i=0
# sum=0
# while i<len(str(n)):
#     sum=sum+int(n[i])
#     i+=1
# print(sum)

# a="12345"
# i=0
# sum=0
# while i<len(a):
#     sum=sum+int(a[i])
#     i+=1
# print(sum)

# a=[["red"],["rohini"],["amla"],["archana"],["deepti"],["deep"]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     n=a[i]
#     c=[]
#     while j<len(n[j]):
#         k=a.count(n[j][0])
#         c.append(k)
#         c.append(n[j][0])
#         j+=1
#     b.append(c)
#     i+=1
# print(c)

# a=["red","rose","amala","archana","deep","dummu"]
# b=[]
# i=0
# while i<len(a)-1:
#     c=1
#     if a[i][0]==a[i+1][0]:
#         c+=1
#         d=[c,a[i][0]]
#         b.append(d)
#     i+=1
# print(b)



# for i in range(5):
#     if i%2==0:
#         pass
#     else:
#         print(i)







