import random
print("=======  wecome to the rock paper seasor game ======")
again=True
while again==True :
    code=int(input("enter 1 for rock 2 for paper and 3 for scisors"))
    if code==1:
        user_chice="rock"
    elif code==2:
        user_chice="paper"
    elif code==3:
        user_chice="scissors"
    else:
        print("invalid input")
    com_choice=random.choice(["rock","paper","scissors"])
    print("Your choice is      :- ",user_chice)
    print("Computer choice is  :-",com_choice)

    if (user_chice=="rock" and com_choice=="paper")or(user_chice=="paper" and com_choice=="rock")or(user_chice=="scissors"and com_choice=="paper"):
        winner=1
    else:
        winner=2



    if com_choice==user_chice:
        print ("===RESULT OF GAME=====")
        print ("==DRAW==")
    elif winner==1:
        print ("===RESULT OF GAME=====")
        print("You won the game")
    elif winner==2:
        print ("===RESULT OF GAME=====")
        print("Computer won the game")
    aga=input("press 'ENTER' for play again ('n') for 'EXIT' ")
    if aga=="n":
        break
print("==== thanks for playing this game")
    

    






