# a="manvithamm"
# i=0
# b=[]
# d=""
# while i<len(a):
#     c=a.count(a[i])
#     if a[i] not in b:
#         b.append(a[i])
#         d=d+str(c)+a[i]
#     i+=1
# print(d)

# O/P:3m2a1n1v1i1t1h

a="my3 na7me i8s r9ajitha"
i=0
n=''
while i<len(a):
    if a[i]>='1' and a[i]<="9":
        print(a[i],end="")
    else:
        n=n+a[i]
    i=i+1
print(n) 



