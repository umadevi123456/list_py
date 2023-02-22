# a=[[2,3],6,[7,8,9,],[10],[11,12]]
# print(a[3][0])

# a=[1,2,3]
# print(a[0]+a[1]+a[2])

# a=2**3//4+3*(3+2)*5
# b=8//4+3*(5)*5
# c=2+15*5
# d=2+75
# # e=77
# print(d)

# a=[50,40,23,70,56,12,5,10,7]
# i=0
# min=a[i]
# max1=0
# max2=0
# while i<len(a):
#     num=a[i]
#     if num>max1:
#         max1=num
#     elif num>max2:
#         max2=num
#     elif num<min:
#         min=num
#     i+=1
# print("max1:",max1)
# print("max2:",max2)
# print("min:",min)

# l=[1,2,2,5,8,4,4,8]
# a=[]
# i=0
# while i<=len(l):
#     if l[i] not in a:
#         a.append(l[i])
#     i+=1
# print(len(a))
    
# a=int(input())
# r=a%10
# print(a-r,"+",r)

# def expanded_form(num):
#     num=str(num)
#     st="" 
#     for j,i in enumerate(num):
#         if i !="0":
#             st += " +{}{}".format(i, len(num[j+1:])*"0")
        # return st.strip(" +")

# a=['1', '2', '3', '4', '5', '6', '7', '8']
# i=0
# b=[]
# while i<len(a):
#     adjacent_member=a[i]
#     b.append(adjacent_member)
#     i+=1
# print(b,a[i])

# a=["apple","banana","cherry","apple"]
# a.clear()
# print(a)

# a=["meena","uma",2,3.0]
# print(a[0:2])

# a=["meena","uma",2,3.0]
# i=0
# b=[]
# while i<len(a):
#         c=a[i]
#         if type(c)==str:
#          b.append (c)
#         i+=1
# print(b)

# a=[6,7.0,"4.5"]
# b=[]
# i=0
# sum=0
# while i<len(a):
#         if type(a[i])==str:
#            sum=sum+float(a[i])
#         else:
#             sum=sum+a[i]
#         i=i+1
# print(sum)


# a=[4,56,7.9,76]
# print(a.pop())

# a=[4,56,7.9,76]
# a.pop()
# print(a)


# a="hello world"
# b=a.title()
# print(b)



# a=["meena","uma",2,3.0]
# i=0
# b=[]
# while i<len(a):
#         if (a[i])==i:
#                 b.append(a[i])
#         i=i+1
# print(b)


# a=["abc","uma","chinni","manu"]
# i=1
# b=[]
# while i<=len(a):
#         b.append(a[-i])
#         i+=1
# print(b)


# a=["abc","uma","chinni","manu"]
# a.revese()
# print(a)


# a=["1","3","67","85"]
# a.reverse()
# print(a)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# i=421
# while i>=1:
#         b=422-i
#         if b==41:
#                 break
#         else:
#                 print(b,end=" ")
#         i-=2
        









