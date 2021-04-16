import time
from Insult import Insult
from Role import Role
from random import randint


chara1 = 0
Mfree = True
Sfree = True
randomType = 0
# global listInsult
# global player1Insult
# global player2Insult
# global listInsult 
listInsult = []
player1Insult = []
player2Insult = []




charaC  = ["Cool dude", "cool dude", "Cool Dude", "cool Dude"]
charaG = ["Granny", "granny", "the granny", "the Granny", "The granny", "The Granny"]
charaR= ["Rich dude", "rich dude", "the rich dude", "rich Dude"]
charaJ = ["Jeff", "jeff", "the looser", "looser"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

required = ("\nYou have to choose an available character\n") 

def intro():
    print( "Welcome to Joute Verbale, be ready to speak some french to your friends !"
    " \n First, choose your character !")
    time.sleep(1)
    choice()

def choice():
    print("" "\nSo, who will you be ? You have a choice betwen: \n"
    "-Cool dude\n"
    "-The granny\n"
    "-Rich dude\n"
    "-Jeff\n")
    global player

    Charachoice1 = input(">>>")
    if Charachoice1 in charaC :
        print("\n The one and only, COOL DUDE!"
        "\n Be ready to teach them what it is to be cool")
        chara1 = 1
        player = Role("The cool dude")

        introplayertwo(chara1)
    elif Charachoice1 in charaG :
      print ("\nVery good, you are the granny !"
      "\n\nPrepare your false teeths to spit on the younglings !")
      chara1=2
      player = Role("The granny")
      introplayertwo(chara1)
    elif Charachoice1 in charaR :
        print ("\nVery good, you are the rich dude !"
        "\n\nBe ready to show to the plebs how superior you are")
        chara1 = 3
        player = Role("The rich dude")
        introplayertwo(chara1)
    elif Charachoice1 in charaJ :
        print ("\nUh ... are you sure you want to take Jeff ?"
        "\n\nHe is really bad you know ..."
        "\ny/n ?")
        jeffanswer = input(">>")
        if jeffanswer in yes :
            print ("\n we want you to have fun you know, but we can't help you if you take Jeff ..."
            "\ny/n ?")
            jeffanswer2 = input(">>")
            if jeffanswer2 in yes :
                print ("\n Well ... at least we warned you ...")
                chara1 = 4
                player = Role("Jeff")
                introplayertwo(chara1)
            elif jefanswer2 in no :
                print ("\n thank god, choose a good character now, please.")
                choice()
            else: 
                print ("\n I'll take that as a no !")
                choice()
        elif jeffanswer in no :
            print ("\n nice, now take a good character")
            choice()
        else: 
            print ("\n I'll take that as a no !")
            choice()
    else:
        print (required)
        choice()

def introplayertwo(chara1):
    global player2
    print ("Now, it's time for player 2 to choose his character."
    "\n but you can't choose the same one as player 1")
    Charachoice2 = input(">>>")
    if Charachoice2 in charaC and chara1 != 1 :
        print ("Very good, be ready to be the coolest !")
        player2 = Role("The cool dude")
    elif Charachoice2 in charaG and chara1 != 2:
        print ("Very good, be ready to hit with your sitck !")
        player2 = Role("The granny")
    elif Charachoice2 in charaR and chara1 != 3:
        print ("Very good, be ready to show them your wealth !")
        player2 = Role("The rich dude")
    elif Charachoice2 in charaJ and chara1 != 4:
        print ("Very good, be ready to ... be Jeff, i guess ...")
        player2 = Role("Jeff")
    else :
        print (required)
        introplayertwo(chara1)
    randomInsult()

def randomInsult():
    global types
    randomType = randint(1 , 4)
    if randomType == 1:
        print ("The insult type is : Money")
        types = Insult("Money")        
        for i in range(0,3):
            Random = randint(0 , 3)
            listInsult.append(types.insultFinal[Random])
        for i in range(0,3):
            Random = randint(0 , 3)
            listInsult.append(types.sujet[Random])
        for i in range(0,3):
            Random = randint(0 , 3)
            listInsult.append(types.adjectives[Random])
        for i in range(0,3): 
            Random = randint(0 , 4)
            listInsult.append(types.starter[Random])
        for i in range(0,3):
            Random = randint(0 , 8)
            listInsult.append(types.complement[Random])
        for i in range(0,3):
            Random = randint(0 , 11)
            listInsult.append(types.liaisons[Random])
        for i in range(0,3):
            Random = randint(0 , 13)
            listInsult.append(types.verb[Random])            
    if randomType == 2:
        print ("The insult type is : Family")
        types = Insult("Family")
        for i in range(0,3):
            Random = randint(0 , 3)
            listInsult.append(types.insultFinal[Random])
        for i in range(0,3):
            Random = randint(0 , 9)
            listInsult.append(types.sujet[Random])
        for i in range(0,3):
            Random = randint(0 , 7)
            listInsult.append(types.adjectives[Random])
        for i in range(0,3):
            Random = randint(0 , 4)
            listInsult.append(types.starter[Random])
        for i in range(0,3):
            Random = randint(0 , 8)
            listInsult.append(types.complement[Random])
        for i in range(0,3):
            Random = randint(0 , 11)
            listInsult.append(types.liaisons[Random])
        for i in range(0,3):
            Random = randint(0 , 13)
            listInsult.append(types.verb[Random])   
    if randomType == 3:
        print ("The insult type is : Style")
        types = Insult("Style")        
        for i in range(0,3):            
            Random = randint(0 , 3)
            listInsult.append(types.insultFinal[Random])
        for i in range(0,3):      
            Random = randint(0 , 10)
            listInsult.append(types.sujet[Random])
        for i in range(0,3):
            Random = randint(0 , 3)
            listInsult.append(types.adjectives[Random])
        for i in range(0,3):
            Random = randint(0 , 4)
            listInsult.append(types.starter[Random])
        for i in range(0,3):
            Random = randint(0 , 8)
            listInsult.append(types.complement[Random])
        for i in range(0,3):
            Random = randint(0 , 11)
            listInsult.append(types.liaisons[Random])
        for i in range(0,3):
            Random = randint(0 , 13)
            listInsult.append(types.verb[Random])   
    if randomType == 4:
        print ("The insult type is : Action")
        types = Insult("Action")        
        for i in range(0,3):
            Random = randint(0 , 3)
            listInsult.append(types.insultFinal[Random])
        for i in range(0,3):
            Random = randint(0 , 3)
            listInsult.append(types.sujet[Random])
        for i in range(0,3):
            Random = randint(0 , 3)
            listInsult.append(types.adjectives[Random])
        for i in range(0,3):
            Random = randint(0 , 4)
            listInsult.append(types.starter[Random])
        for i in range(0,3):
            Random = randint(0 , 8)
            listInsult.append(types.complement[Random])
        for i in range(0,3):
            Random = randint(0 , 11)
            listInsult.append(types.liaisons[Random])
        for i in range(0,3):
            Random = randint(0 , 13)
            listInsult.append(types.verb[Random])  
    print ("now choose some of thes words to create your insult player1! \nType stop to finish your insult" )        
    select()
 
def select():
    print("\n")
    print(*listInsult, sep ="/ ")
    print("Get in there player 1")
    if len(listInsult) >= 1:
        Insult1 = input(">>>")
        if Insult1 in listInsult:
            player1Insult.append(Insult1)
            try:
                listInsult.remove(Insult1)
            except ValueError:
                pass
            print("your current sentence is :")
            print(player1Insult)
            select2()
        elif Insult1 == "end":
            select2alone()
        else:
            print ("Choose a valide word\n" )
            select()
    else:
        print("no more words let's see the result")
        endgame()

def select2():
    print("\n")
    print(*listInsult, sep ="/ ")
    print("\n")
    print("Get in there player 2")
    if len(listInsult) >= 1:
        Insult2 = input(">>>")
        if Insult2 in listInsult:
            player2Insult.append(Insult2)
            try:
                listInsult.remove(Insult2)
            except ValueError:
                pass
            print("your current sentence is :")
            print(player2Insult)
            
            select()
        elif Insult2 == "end":
            selectalone()
        else:
            print ("Choose a valide word\n" )
            select()
    else:
        print("no more words let's see the result")
        endgame()
    print(Insult2)

def selectalone():
    print("\n")
    print(*listInsult, sep ="/ ")
    print("\n")
    print("Get in there player 1, finish your insult")
    if len(listInsult) >= 1:
        Insult1 = input(">>>")
        if Insult1 in listInsult:
            player1Insult.append(Insult1)
            try:
                listInsult.remove(Insult1)
            except ValueError:
                pass
            print("your current sentence is :")
            print(player1Insult)
            selectalone()
        elif Insult1 == "end":
            endgame()
        else:
            print ("Choose a valide word\n" )
            selectalone()
    else:
        print("no more words let's see the result")
        endgame()
    print(Insult1)



def select2alone():
    print("\n")
    print(*listInsult, sep ="/ ")
    print("\n")
    print("Get in there player 2, finish your insult.")
    if len(listInsult) >= 1:
        Insult2 = input(">>>")
        if Insult2 in listInsult:
            player2Insult.append(Insult2)
            try:
                listInsult.remove(Insult2)
            except ValueError:
                pass
            print("your current sentence is :")
            print(player2Insult)
            select2alone()
        elif Insult2 == "end":
            endgame()
        else:
            print ("Choose a valide word\n" )
            select2alone()
    else:
        print("no more words let's see the result")
        endgame()
    print(Insult2)

def endgame():
    scorePlayer1 = player.point
    scorePlayer2 = player2.point
    i = 0
    i2 = 0
    while i < len(player1Insult):
        i = i + 1
        scorePlayer1 = scorePlayer1 + 10
    while i2 < len(player2Insult):
        i2 = i2 + 1
        scorePlayer2 = scorePlayer2 + 10
    special = randint(0,25)
    if special == 25 and player.role == "Jeff" or player2.role == "Jeff" and special == 25:
        print("you roasted jeff so good that the only rational responce for him was to unleash nuclear armagedon uppon earth.")
        time.sleep(4)
        print("turning the planet into a dead chunk of rock, tumbling through the vast vacuum of an uncaring universe.")
        time.sleep(6)
        print("jeff wins")
        return
    if special == 15 and player.role == "The granny":
        print("The granny didn't hear half of what you were saying so it's not as impactful")
        scorePlayer2 = scorePlayer2 - 100
    elif special == 15 and player2.role == "The granny":
        print("The granny didn't hear half of what you were saying so it's not as impactful")
        scorePlayer = scorePlayer - 100
    if special == 7 and player.role == "The cool dude":
        print("you'r so cool !")
        scorePlayer = scorePlayer + 100
    elif special == 7 and player2.role == "The cool dude":
        print("you'r so cool !")
        scorePlayer2 = scorePlayer2 + 100
    print("the score of player1 is :" + str(scorePlayer1) + "\n")
    print("the score of player2 is :" + str(scorePlayer2) + "\n")
    if scorePlayer1 > scorePlayer2:
        print("Player1 wins the day")
        return
    elif scorePlayer1 < scorePlayer2:
        print("Player2 wins this time")
        return
    else:
        print("What ? a tie ? Damn !")
        return



    
intro()




