print("Welcome to the kbc game")
a=input("enter the name: ")
questions=["1.what is the capital of india","2.what is the capital of andhrapradesh","3.where was the charminar is located","4.how many days are there in a year"]
options=[["1.andhra","2.delhi","3.bhopal","4.maharashtra"],["1.amaravathi","2.vizag","3.ananthapur","4.vijayawada"],["1.agra","2.mumbai","3.chennai","4.hydarabad"],["1.300","2.350","3.360","4.365"]]
solution_list=[2,1,4,3]
result=["congratulation! you win the prize","wowww!you won 10,000 rupees","super!!,you are the super winner","congrats!you are great"]
lost=["you lost the game","better luck next time","good luck for next time","bad luck for this time"]
i=0
s=0
while i<len(questions):
    b=questions[i]
    print(b)
    j=0
    while j<len(options):
        c=options[i][j]
        j=j+1
        print(c)
    
    else:
        choice=int(input("enter the answer: "))
        if choice==solution_list[s]:
            print(result[i])
        else:
            print(lost[i])
            break
    s=s+1
    i=i+1







