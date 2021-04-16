import time
from Insult import Insult
from Role import Role
from random import randint

scoreinsult = 0
chara1 = 0
Mfree = True
Sfree = True
randomType = 0
listInsult = []

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
 

    print("\n")
    print(*listInsult, sep ="/ ")
    print ("now choose some of thes words to create your insult !" )
    Insult1 = input(">>>")
    Indsult = Insult1.split(' ')
    print(Indsult)
intro()

