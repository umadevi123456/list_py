a=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
i=0
while i<len(a):
    if a[i]=="f":
        b=i
    elif a[i]=="c":
        c=i
    elif a[i]=="k":
        d=i
    elif a[i]=="w":
        e=i
    i+=1
print("Last occurance of F is:","b:",b)
print("Last occurance of C is:","c:",c)
print("Last occurance of K is:","d:",d)
print("Last occurance of W is:","e:",e)


