# a=['Red', 'Maroon', 'Yellow', 'Olive']
# b=[]
# i=0
# while i<len(a):
#     c=a[i]
#     d=list(c)
#     b.append(d)
#     i+=1
# print(b)

#   O/P : [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]

#        OR

# a=['Red', 'Maroon', 'Yellow', 'Olive']
# b=[]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         c=[a[i][j]]
#         b.append(c)
#         j+=1
#     i+=1
# print(b)

#    O/P : [['R'], ['e'], ['d'], ['M'], ['a'], ['r'], ['o'], ['o'], ['n'], ['Y'], ['e'], ['l'], ['l'], ['o'], ['w'], ['O'], ['l'], ['i'], ['v'], ['e']]

#       OR

# a=['Red', 'Maroon', 'Yellow', 'Olive']
# b=[]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         c=(a[i][j])
#         b.append(c)
#         j+=1
#     i+=1
# print(b)     

#    O/P: ['R', 'e', 'd', 'M', 'a', 'r', 'o', 'o', 'n', 'Y', 'e', 'l', 'l', 'o', 'w', 'O', 'l', 'i', 'v', 'e']