# l=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# i=0
# min=10
# max=10
# while i<len(l):
#     d=len(l[i])
#     if d>max:
#         max=d
#         r=l[i]
#     if d<min:
#         min=d
#         n=l[i]
#     i+=1
#     n=max,r
#     k=min,n
#     print(tuple(k))
#     print(tuple(n))
    
    
# a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# i=0
# max=0
# min=int(input("enter max:"))
# while i<len(a):
#     b=a[i]
#     c=len(b)
#     if c>max:
#         max=c 
#         d=a[i]
#     else:
#         min=c
#         e=a[i]
#     i+=1
# print("leangth of maximum:",c,max,d)
# print("leangth of minmum:",c,min,b)
 

# a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# i=0
# max=0
# min=int(input("enter max:"))
# while i<len(a):
#     b=a[i]
#     c=len(b)
#     if c>max:
#         max=c 
#         d=a[i]
#     else:
#         min=c
#         e=a[i]
#     i+=1
# print("leangth of maximum:",max,d)
# print("leangth of minmum:",min,e)
 

a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
max=1
min=1
for i in range(len(a)):
    length=len(a[i])
    if length>max:
        max=length
    if length<min:
        min=length
print(max,a[max+1])
print(min,a[max-1])

