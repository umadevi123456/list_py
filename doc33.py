# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
# Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7

# a=[12, 67, 98, 34]
# i=0
# b=[]
# while i<len(a):
#     sum=0
#     if a[i]>0:
#         r=a[i]%10
#         sum=sum+r
#         q=a[i]//10
#         b.append(sum+q)
#     i+=1
# print(b)

#   O/P:[3, 13, 17, 7]



# a=[12, 67, 98, 34]
# i=0
# b=[]      
# while i<len(a):
#     sum=0
#     j=0
#     n=str(a[i])
#     while j<len(n):
#         sum=sum+int(n[j])
#         j+=1
#         b.append(sum)
#     i+=1
# print(sum)