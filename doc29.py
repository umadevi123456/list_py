# n=[5, 6, [], 3, [], [], 9]
# i=0
# b=[]
# while i<len(n):
#     if n[i]!=[]:
#         b.append(n[i])
#     i+=1
# print(b)

#   O/P:[5, 6, 3, 9]

x=[1,10]
count=0
i=0
while i<len(x):
    if count<=10:
        count=count+1
        print("no")
    else:
        print("yes")
    i+=1