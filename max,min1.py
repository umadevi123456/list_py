a=[50,40,23,70,56,12,5,10,7]
i=0
min=a[i]
max1=0
max2=0
while i<len(a):
    num=a[i]
    if num>max1:
        max1=num
    elif num>max2:
        max2=num
    elif num<min:
        min=num
    i+=1
print("max1:",max1)
print("max2:",max2)
print("min:",min)



