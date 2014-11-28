import time
import pygame.mixer


# To Do
#
# Skikkelige Ascii-tall
# Overkjøre/flash over screensaver


def spillLydStart():
    '''Spill en lyd'''
    #
    pygame.mixer.init()
    ss=pygame.mixer.Sound('desktop-logout.ogg')
    ss.play()


def spillLydStopp():
    '''Spill en lyd'''
    #
    pygame.mixer.init()
    ss=pygame.mixer.Sound('phone-incoming-call.ogg')
    ss.play()


def pomodoro():
    '''En Pomodoro på 25 minutter'''
    #
    boom=60*25
    spillLydStart()
    print('\n')*3
    print('Pomodoro starter')
    time.sleep(1)
    while boom > 0:
        time.sleep(1)
        if boom%60==0:
            print('\n')*30
            print(int(boom/60))
            print('\n')*3
            #print(boom/60)
        boom -=1
    print('Pomodoro er over')
    spillLydStopp()


def pomPause():
    '''5 minutter pause før neste Pomodoro'''
    #
    boom=60*5
    spillLydStart()
    print('Pausen starter')
    while boom > 0:
        time.sleep(1)
        if boom%60==0:
            print(boom/60)
        boom -=1
    print('Pausen er over')
    spillLydStopp()



def startPomodoro():
    '''Start Pomodoro-rekke'''
    #
    starte = raw_input('Starte Pomodoro?: ')
    if starte in ['j','J','y','Y']:
        pomodoro()
        pomPause()
        startPomodoro()
    elif starte in ['n','N','q','Q']:
        print('Avslutter Pomodoro. Kjør startPomodoro() for å starte ny Pomodoro! :)')
    else:
        print('Error: Press "y" for Yes or "n" for No')
        startPomodoro()


# Kjør Pomodoro
startPomodoro()




##
##print("""\n
##
## ____  ____  
##|___  \| ___| 
##  __)   |___  \ 
## /   __/ ___)  |
##|_____|____/ 
##
##  \n""")
