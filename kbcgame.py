print("Welcome to the kbc game")
a=input("enter the name: ")
questions=["1.what is the capital of india","2.what is the capital of andhrapradesh","3.where was the tajmahal is located","4.how many days are there in a week"]
options=[["1.andhra","2.delhi","3.bhopal","4.maharashtra"],["1.amaravathi","2.vizag","3.ananthapur","4.vijayawada"],["1.hyderabad","2.agra","3.mumbai","4.j&k"],["1.five","2.three","3.seven","4.ten"]]
solution_list=[2,1,2,3]
fifty_percentages=[["1.bhopal","2.delhi"],["1.vizag","2.amaravathi"],["1.agra","2.j&k"],["1.five","2.seven"]]
percentage_sol=[2,2,1,2]
result=["congratulation! you won the prize","wowww!you won 10,000 rupees","super!!,you are the super winner","congrats!you are great"]
lost=["you lost the game","better luck next time","good luck for next time","bad luck for this time"]
i=0
s=0
count=0
while i<len(questions):
    b=questions[i]
    print(b)
    j=0
    while j<len(options):
        c=options[i][j]
        j=j+1
        print(c)
    print("1.with lifeline")
    print("2.without lifeline")
    choice=int(input("enter the choice:-"))
    if choice==1:
        if count==0:
            d=0
            while d<len(fifty_percentages):
                e=fifty_percentages[i]
                d=d+1
            print(e)
            chances=int(input("enter the answer: "))
            if chances==fifty_percentages[s]:
                print(result[i])
            else:
                print(lost[i])
                break
        else:
            print("already used 50-50 lifeline")
            choice=int(input("enter the choice: "))
            if choice==solution_list[s]:
                print(result[i])
            else:
                print(lost[i])
                break
    else:
        choice=int(input("enter the answer: "))
        if choice==solution_list[s]:
            print(result[i])
        else:
            print(lost[i])
    s=s+1
    i=i+1

a=["R",["A","N","I"]]
i=0
b=[]
while i<len(a):
    if type (a[i]) is list:
        j=0
        while j<len(a[i]):
            d=a[i][j]
            b.append(d.lower())
            j=j+1
    else:
        b.append(a[i])
    i=i+1
p="".join(b)
print(p)






