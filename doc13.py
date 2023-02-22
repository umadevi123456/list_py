# [[2, 1], 2, 3, [2, 4], 5, 1]


# list=[1,1,2,3,4,4,5,1]
# b=[]
# count=0
# i=0
# while i<len(list):
#     if list[i] not in b:
#         count=count+1
#         b.append([count,i])
#     i+=1
# print(b)


# [[2, 1], 2, 3, [2, 4], 5, 1]

list=[1,1,2,3,4,4,5,1]
a=[]
i=0
while i<len(list)-1:
    k=list.count(list[i])
    a.append(k)
    i+=1
print(a)
    
    
    



# arr = [1, 2, 3, 4, 2, 7, 8, 8, 3];   
# for i in range(0, len(arr)):  
#     for j in range(i+1, len(arr)):  
#         if(arr[i] == arr[j]): 
             
#             print(arr[j]);  





        
        
        