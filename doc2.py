# list =[["g","f","g"],["i","s"],["b","e","s","t"]]
# print(list[0][0]+list[0][1]+list[0][2]+list[1][0]+list[1][1]+list[2][0]+list[2][1]+list[2][2]+list[2][3])


# list =[["g","f","g"],["i","s"],["b","e","s","t"]]
# i=0
# b=""
# while i<len(list):
#     c=list[i]
#     j=0
#     while j<len(c):
#         b=b+c[j]
#         j=j+1
#     i=i+1
# print(b)

#   O/P:gfgisbest

a=[["g","f","g"],["i","s"],["b","e","s","t"]]
i=0
s=""
while i<len(a):
    j=0
    b=a[i]
    while j<len(b):
        s=s+b[j]
        j+=1
    i+=1
print(s)






