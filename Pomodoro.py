import time

# To Do
#
# Skikkelige Ascii-tall
# Mulighet for lyd ved stopp
# Overkjøre/flash over screensaver

def pomodoro():
    boom=60*25
    print('Pomodoro starter')    
    while boom > 0:
        time.sleep(1)
        if boom%60==0:
            print('\n \n \n ' + str(int(boom/60)) + '\n \n \n ')
            #print(boom/60)
        boom -=1
    print('Pomodoro er over')


def pomPause():
    boom=60*5
    print('Pausen starter')
    while boom > 0:
        time.sleep(1)
        if boom%60==0:
            print(boom/60)
        boom -=1
    print('Pausen er over')


def startPomodoro():
    starte = input('Starte Pomodoro?: ')
    if starte in ['j','J','y','Y']:
        pomodoro()
        pomPause()
        startPomodoro()
    elif starte in ['n','N','q','Q']:
        print('Avslutter Pomodoro. Kjør startPomodoro() for å starte ny Pomodoro! :)')
    else:
        print('Error: Press "y" for Yes or "n" for No')
        startPomodoro()



print("""\n

 ____  ____  
|___  \| ___| 
  __)   |___  \ 
 /   __/ ___)  |
|_____|____/ 

  \n""")
