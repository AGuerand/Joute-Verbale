import time

chara1= 0
Mfree = True
Sfree = True

charaC  = ["Cool dude", "cool dude"]
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

        introplayertwo(chara1)
    elif Charachoice1 in charaG :
      print ("\nVery good, you are the granny !"
      "\n\nPrepare your false teeths to spit on the younglings !")
      chara1=2
      introplayertwo(chara1)
    elif Charachoice1 in charaR :
        print ("\nVery good, you are the rich dude !"
        "\n\nBe ready to show to the plebs how superior you are")
        chara1 = 3
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
    elif Charachoice2 in charaG and chara1 != 2:
        print ("Very good, be ready to hit with your sitck !")
    elif Charachoice2 in charaR and chara1 != 3:
        print ("Very good, be ready to show them your wealth !")
    elif Charachoice2 in charaJ and chara1 != 4:
        print ("Very good, be ready to ... be Jeff, i guess ...")
    else :
        print (required)
        introplayertwo(chara1)
    

intro()