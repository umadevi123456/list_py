# a=int(input("enter number:"))
# b=[]
# i=0
# while i<a:
#     x=int(input("enter number:"))
#     b.append(x)
#     num=x
#     r=num%1000
#     m=r%100
#     y=m%10
#     i+=1
#     print("'",num-r,"+",r-m,"+",m-y,"+",y,"'")
    
a=int(input(" enter number"))
i=0
while i<a:
	l=a%100000
	tent=a%10000
	onet=a%1000
	h=a%100
	t=a%10
	i=i+1
print(a-l,"+",l-tent,"+",tent-onet,"+",onet-h,"+",h-t,"+",t)   



