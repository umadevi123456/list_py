name=input("enter the name:")
print("welcome to KBC game")
ques=["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?","whats is the capital of karnataka"]
options=[["Four", "Nine", "Seven", "Eight"],
         ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
         ["Software Engineering", "Counseling", "Tourism", "Agriculture"],
         ["chennai","bangalore","mangalore","hydrabad"]]
help_line=[["four","seven"],["Chennai", "Delhi"],["Software Engineering", "Counseling"],["bangalore","mangalore"]]
ans=[3,4,1,2]
helpline_ans=[2,2,1,1]
i=0
help=0
while i<len(ques):
    print("Q"+str(i+1)+"."+ques[i])
    j=0
    while j<len(options):
        print("  "+str(j+1)+":"+options[i][j])
        j+=1
    k=0
    userans=int(input("enter the user answer:"))
    if  userans== ans[i]:
        print("good")
    elif  userans== 5:
        if help==0:
            k=0
            while k<len(help_line[i]):
                print("  "+str(k+1)+":"+help_line[i][k])
                k+=1
            help+=1
            help_ans=int(input("enter the helpline answer:"))
            if help_ans==helpline_ans[help]:
                print("congratulations")
            else:
                print("wrong answer")
                print("game end")
                break
        else:
            print("you already used the helpline")
            user_ans=int(input("enter the user answer:"))
            if user_ans==ans[i]:
                print("congratulation you won the game")
            else:
                print("your answer is wrong")
                print("exit the game")
                break
    else:
        print("over")
        break
    i+=1





