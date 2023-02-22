# a=[6,2.9,"18.9",40,"50"]
# i=0
# sum=0
# b=[]
# while i<len(a):
#     c=a[i]
#     if type(c)==str:
#         sum+=int(float(c))
#     elif type(c)==float:
#         sum+=int(c)
#     else:
#         sum+=c  
#     i+=1
# print(sum)

#   O/P:116

# a=[6,2.9,"18.9",40,"50"]         
# l=[]
# i=0
# s=0
# while i<len(a):
#     if type(a[i])==str:
#         b=float(a[i])
#         b=int(b)
#         s=s+b
#         l.append(b)
#     elif type(a[i])==float:
#         c=int(a[i])
#         s=s+c
#         l.append(c)
#     else:
#         l.append(a[i])
#         s=s+a[i]
#     i=i+1
# print(l)
# print(sum(l))
# print(s)