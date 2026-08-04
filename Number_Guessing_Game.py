
name=input('ENTER YOUR FUll NAME :-')
print("WELCOME TO THE NUMBER GUESSING GAME", name)
while True :
    level=(input("choseee dificultie lavel\n1 for easy\n2 for medium \n3 for hard level:-   "))
    if level=="1":
        s=50 
        break 
    elif level=="2":
        s=100
        break
    elif level=="3":
        s=250
        break 
    else:
        print("INVALID INPUT PLEASE TRY AGAIN ")
        
ju="y"
while ju=="y":
    from random import randint  
    num=randint(1,s)
    #print("the random number is ",num)       
    count=1
    attempt=1
    guess=int(input("Enter your guess between 1 to "+str(s)+":-"))
    while num!=guess:
        if attempt<10:
            if guess>num:
                print(guess," is higher than actual number ")    
            elif guess<num:
                print(guess," is lower than actual number ")
            print(10-count,"attempts left")
            guess=int(input("Enter your guess again  :- "))
            print(10-count,"attempts left")
            count+=1
            attempt+=1
        else :
            print("YOU LOST BETTER FUCK NEXT TIME ")
            print("THE ACTUAL NUMBER IS ",num)
            break
    if num==guess:    
        print("CONGRATULATIONS!!!!!\nyou guess the correct number in ",count,"attempt")
    if count<=3:
        score=" YOUR  SCORE ARE EXELLENT"
    elif count<=7:
        score="YOUR SCORE ARE GOOD"
    elif count<=10:
        score="KEEP IMPROVVING "
    print("YOUR SCORE IS :- (",10-count,"/ 10 )",score)
    again=input("want to play again (y/n) :- ")
    while True:
        if again=="y":
            ju="y"
            break
        elif again=="n":
            ju="nafis "
            break
        else :
            print("PLEASE ENTER VALID INPUT.....")
            again=input("want to plau agian (y/n):- " )
print ("THANKS FOR PLAYYING THIS GAME \nWE HOPE YOU COME BACK SOON\nHAVE A NICE DAY!!!!!!")
print("FROM YOUR Well WISHER "'NAFIS KHAN'" .........")


