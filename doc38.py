a="https://www.w3resource.com/python-exercises/list/"
b=['.com', '.edu', '.tv']
c=0
for i in b:
    if i in a:
        c+=1
if c>=1:
    print("True")
else:
    print("False")


