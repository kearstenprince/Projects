
def setup():
    size(1000,1000)
    background(80, 100, 132)
    global currentScene
    currentScene = 0 
    add_library("minim")
    global Song
    minim = Minim(this)
    Song = minim.loadFile("backgroundMusic.mp3")
    
def draw():
    global Song
    Song.play()
    # getVolume ( )
    # isLooping ( )
    # isMuted ( )
    # isPlaying ( )
def scene1():    
    textSize(14)
    text('Samantha is a young girl who was told at a young age that her mother died in an accident when she was a baby.', 10, 250)
    text('She is now a teenager and starts to over hear too much information that she can not seem to piece together.', 10, 270)
    text('She begins an adventure to find out the secrets that are being withheld from her.', 10, 290)
def scene2():
    text ("""it\'s 7:30 a.m. and your alarm clock goes off. BRRRRIIIIIING! 
              You think about how amazing it would be to stay in the bed 
              and get just a couple more minutes of sleep,\n: 
              but you know a couple might lead to more. 
              Do you get up now or risk sleeping a little longer?\n:
              Press 1 to get up now or 2 sleep longer\n:""", 10, 290)
def choice1():
    textSize(14)
    text ("""You drag yourself out of the bed and head to the shower. 
          Upon heading to your personal bathroom\n: 
          you realize you left all the towels in the washer last night and forgot to dry them.""", 10, 290)

def scene3():
    textSize(14)
    text ("""As you shower sleepily, you hear yelling coming from your dads room. 
          He seems really upset, and if you turn the water off you could really hear him, but maybe its none of your business.
          Do you cut the shower to hear better, or keep showering and mind your business?
          Press cut to cut the shower off or business to mid your business'""", 10, 290)

def choice2():
    textSize(14)
    text ("""You tell yourself youre going to sleep 5 more minutes, but end up sleeping 20 more minutes. 
          You leap out of the bed and head to the shower.\n: 
          Upon heading to your personal bathroom\n: 
          you realize you left all the towels in the washer last night and forgot to dry them.""", 10, 290)

def choice3():
    textSize(14)
    text ("""Upon cutting the shower off you begin to hear your dad say, ‘\$200 late fee for the rent is ridiculous.\n:
          I plan on paying it tomorrow. Please extend me a day, Im a valued customer.\n:
          Ive been renting this space for 14 years.\’ Youre curious so you begin to get out the shower.\n:
          Press continue to put on your clothes""", 10, 290)
def choice33():
    textSize(14)
    text ("""You finish washing up and try to ignore the outrageous yelling.\n:
          Upon getting out the shower you hear the end of a conversation,\n:
          Ive been renting this space for 14 years.\’\n:
          Youre curious so you begin get dressed so that you can go in your dads room.\n:
          Press continue to put on your clothes""", 10, 290)
    
def choice4():
    textSize(14)
    text ("""Your dad stops in the middle of the doorway and tells you you need to be heading to school.\n:
          You say, ‘\I overheard the yelling and was trying to make sure everything is okay.’\n:
          He reassures you everything is fine kisses you on the forehead and rushes out the door.\n:
          You start to head back to your room to get ready for school, but you’re stopped by a,\n:
          bRRIIIIIIINNNGGGG You realize your dad left his phone.\n:
          Do you answer the phone or just leave it be?\n:
          Press Answer to answer the phone call or walk away to leave it be.""", 10, 290)
    
def choice44():
    textSize(14)
    text ("""You start to head back to your room, and make a mental note to act like you didnt hear anything.\n: 
          You start to head back to your room to get ready for school, but youre stopped by a,\n:
          bRRIIIIIIINNNGGGG You realize your dad left his Macbook which is hooked to his phone.\n:
          Hs getting a call from someone under a blocked caller ID.\n:
          Do you answer the phone or just leave it be?\n:
          Press Answer to answer the phone call or walk away to leave it be.""", 10, 290)
    
def choice5():
    textSize(14)
    text ("""You answer the phone call and a man immediately starts talking.\n:
          ‘\Mr.Lopez, we really have a problem. I need you to come to the cabin right now.\n:
          I think she may be pregnant. Mr. Lopez?? Mr. Lopez??\’ You hang up the phone quickly,\n:
          and stare for a minute. You try to understand what he was saying, but cant seem to make sense of it.""", 10, 290)
    
def choice55():
    textSize(14)
    text ("""The phone stops ringing and you start to walk away.\n:
          But then you see a notification pop up that says\n:
          Voicemail received, your curiosity gets the best of you so you listen to the voicemail.\n:
          A males voice comes through the speakers: Mr.Lopez we have a problem.\n:
          I think shs pregnant. Meet me at the cabin.\n:
          You stare for a minute and try to understand what he was saying, but cant seem to make sense of it.""", 10, 290)

def choice6():
    textSize(14)
    text ("""You cant shake the mysterious thoughts from your brain. You have to know more.\n:
          You start looking around to find things.\n:
          You start thinking of hiding places for information.\n:
          You open the drawers to find nothing but clothes. You see cabinets.\n:
          press continue to search to search the cabinets""", 10, 290)

def scene666():
    textSize(14)
    text ("""You open the cabinets to find some pills in a plastic bag.\n:
          You dont know what the pills are for, but they don’t seem to be for medical use.\n:
          press continue to put those in your pocket.""", 10, 290)
def choice67():
    textSize(14)
    text ("""You decide not to worry about it and begin to gather your supplies for school.\n:
          On your way out the door you realize you have a headache and decide to go to the cabinet to find some Advil.\n:
          You grab your advil, but next to it you see a bag of mysterious pills.\n:
          You realize you cant go to school with all these mysteries going on.\n:
          You dont know what the pills are for, but they dont seem to be for medical use.\n:
          press continue to put those in your pocket.""", 10, 290)



def scene4():
    textSize(14)
    text ("""You put on your clothes and head to your dads room and find him rushing to leave.\n:
          Do you ask him to wait so you can inquire about the phone call?\n:
          Or do you let him leave? Press WAIT to stop him and ask or press leave to let him leave""", 10, 290)

def scene5():
    textSize(14)
    text ("""A million thoughts are going through your head. Pregnant??? Cabin????\n:
          What could he be talking about?? You try to go back to getting ready\n:
          for school but so many thoughts run through your head.\n:
          You cant go you have to figure out whats going on. Or maybe you should go, and worry about it later.\n:
          Press worry if you want to skip school and search for clues or dont worry if you want to go to school and forget about it""", 10, 290)








def mouseClicked():
    global currentScene
    if mouseX > 10 and mouseX <110 and mouseY >10 and mouseY <110:
        textSize(14)
        currentScene = currentScene + 1
        background(80, 100, 132)
    print currentScene
    if currentScene == 1:
        scene1()
    elif currentScene == 2:
        scene2()
        fill(0)
        rect(10, 590, 100, 100)
        fill(255)
        textSize (14)
        text("1", 50, 640)
        fill(0)
        rect(120, 590, 100, 100)
        fill(255)
        textSize (14)
        text("2", 150, 640)
        if mouseX > 10 and mouseX <110 and mouseY >590  and mouseY< 690:
            background(80, 100, 132)
            choice1()
        elif mouseX > 120 and mouseX <220 and mouseY >590 and mouseY < 690:
            background(80, 100, 132)
            choice2()
    elif currentScene == 3:
        scene3()
        fill(0)
        rect(10, 590, 100, 100)
        fill(255)
        textSize (14)
        text("cut", 50, 640)
        fill(0)
        rect(120, 590, 100, 100)
        fill(255)
        textSize (14)
        text("business", 150, 640)
        if mouseX > 10 and mouseX <110 and mouseY >590  and mouseY< 690:
            background(80, 100, 132)
            choice3()
        elif mouseX > 120 and mouseX <220 and mouseY >590 and mouseY < 690:
            background(80, 100, 132)
            choice33()
    elif currentScene == 4:
        scene4()
    
    elif currentScene == 5:
        scene4()
        fill(0)
        rect(10, 590, 100, 100)
        fill(255)
        textSize (14)
        text("wait", 50, 640)
        fill(0)
        rect(120, 590, 100, 100)
        fill(255)
        textSize (14)
        text("leave", 150, 640)
        if mouseX > 10 and mouseX <110 and mouseY >590  and mouseY< 690:
            background(80, 100, 132)
            choice4()
            fill(0)
            rect(10, 590, 100, 100)
            fill(255)
            textSize (14)
            text("answer", 50, 640)
            fill(0)
            rect(120, 590, 100, 100)
            fill(255)
            textSize (14)
            text("walk away", 150, 640)
            if mouseX > 10 and mouseX <110 and mouseY >590  and mouseY< 690:
                background(80, 100, 132)
                choice5()
            elif mouseX > 120 and mouseX <220 and mouseY >590 and mouseY < 690:
                background(80, 100, 132)
                choice55()
        elif mouseX > 120 and mouseX <220 and mouseY >590 and mouseY < 690:
            background(80, 100, 132)
            choice44()
            fill(0)
            rect(10, 590, 100, 100)
            fill(255)
            textSize (14)
            text("answer", 50, 640)
            fill(0)
            rect(120, 590, 100, 100)
            fill(255)
            textSize (14)
            text("walk away", 150, 640)
            if mouseX > 10 and mouseX <110 and mouseY >590  and mouseY< 690:
                background(80, 100, 132)
                choice5()
            elif mouseX > 120 and mouseX <220 and mouseY >590 and mouseY < 690:
                background(80, 100, 132)
                choice55()
    elif currentScene == 6:
        scene5()
        fill(0)
        rect(10, 590, 100, 100)
        fill(255)
        textSize (14)
        text("worry", 50, 640)
        fill(0)
        rect(120, 590, 100, 100)
        fill(255)
        textSize (14)
        text("dont worry", 150, 640)
        if mouseX > 10 and mouseX <110 and mouseY >590  and mouseY< 690:
            background(80, 100, 132)
            choice6()
            fill(0)
            rect(10, 590, 100, 100)
            fill(255)
            textSize (14)
            text("open", 50, 640)
            if mouseX > 10 and mouseX <110 and mouseY >590  and mouseY< 690:
                scene666()
        elif mouseX > 120 and mouseX <220 and mouseY >590 and mouseY < 690:
            background(80, 100, 132)
            choice67()
def draw():
    fill(0)
    rect(10, 10, 100, 100)
    fill(255)
    textSize (14)
    text("continue", 30, 60)
    
    
    
