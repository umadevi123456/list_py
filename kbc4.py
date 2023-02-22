question_list=["1.Bahubali festival is related to?",
"2.The language of Lakshadweep. a Union Territory of India, is",
"3.The International Literacy Day is observed on"]
options_list=[["Islam", "Hinduism","Buddhism","Jainism"],
["Tamil","Hindi","Malayalam","Telugu"],["Sep 8","Nov 28","May 2","Sep 22"]]
life_line_5050=[["Buddhism","Jainism"],["Malayalam","Telugu"],["Sep 8","May 2"]]
sol_life_line=[2,1,1]
sol=[4,3,1]
count=0
for i in range(len(question_list)):
    print(question_list[i])
    for j in range(len(options_list[i])):
        print(j+1,options_list[i][j])
    user=int(input("select number from 1 to 4 or 5050 lifeline;"))
    if user==sol[i]:
        print("congrats your ans is correct")
    elif user==5050:
        if count==0:
           for k in range(len(life_line_5050[i])):
               print(k+1,life_line_5050[i][k])
           count+=1
           user1=int(input("enter the number:"))
           if user1==sol_life_line[i]:
              print("congrats your ans is correct")
           else:
              print("sadly your ans is wrong")
              break
        else:
            print("you already used your 5050 lifeline")
            user2=int(input("select options from 1 t0 4:"))
            if user2==sol[i]:
                print("congrats your ans is correct")
            else:
                print("sadly your ans is wrong")
                break
    else:
        print("your ans is wrong")
        break
    
    


