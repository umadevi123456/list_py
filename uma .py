# a="python prog"
# print(len(a))

# a="python Programming"
# b=a.capitalize()
# print(a.capitalize())
# print(b)


# a="AABCAAADA"
# i=0
# b=[]
# while i<=len(a):
#     if a[i]!="A":
#         b.append(a[i])
#     i+=1
# print(b)

# a="AABCAAADA"
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i+=1
# j=0
# while j<1:
#     c=1
#     while c<len(b):
#         print(b[0]+b[c])
#         c+=1
#     j+=1

# O/P:AB
#     AC
#     AD

a=["10","10","10","20","30","50","20","50","10","12"]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i+=1
b.pop()
print(b)
j=0
c=[]
while j<4:
    d=(b[j]+","+b[j])
    c.append(d)
    j+=1
print(c)


    



