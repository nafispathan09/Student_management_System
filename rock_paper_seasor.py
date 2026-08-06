import random
print("=======  wecome to the rock paper seasor game ======")
again=True
while again==True :
    while True:
        code=int(input("enter 1 for rock 2 for paper and 3 for scisors"))
        if code==1:
            user_chice="rock"
            break
        elif code==2:
            user_chice="paper"
            break
        elif code==3:
            user_chice="scissors"
            break
        else:
            print("invalid input")

    com_choice=random.choice(["rock","paper","scissors"])
    print("Your choice is      :- ",user_chice)
    print("Computer choice is  :-",com_choice)

    if (user_chice=="rock" and com_choice=="scissors")or(user_chice=="paper" and com_choice=="rock")or(user_chice=="scissors"and com_choice=="paper"):
        winner="you"
    else:
        winner="computer"


    print ("===RESULT OF GAME=====")
    if com_choice==user_chice:
        print ("==DRAW==")
    print("====",winner," won the game =====")
    print("====",winner," won the game =====")

    play_again=input("press 'ENTER' for play again ('n') for 'EXIT' ")
    if play_again=="n":
        break
print("==== thanks for playing this game")
    

    






