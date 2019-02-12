import time

def getName():
    print("Welcome in the Dragons Realm traveler!")
    time.sleep(2)
    print("First things firts,please tell me your name: ", end = '')
    name = input()
    time.sleep(1)
    print("Greetings, " + name)
    time.sleep(2)
    return name

def getStarted():
    time.sleep(2)
    answ = ''
    while not answ.lower().startswith('y') or not answ.lower().startswith('n'):
        print("Can we start?? (yes or no)", end = ' ')
        answ = input()
        if answ.lower().startswith('y'):
            return True
        else:
            return False

def showIntro(a):
    if a:
        time.sleep(2)
        print("Let me tell you the main story: ")
        time.sleep(2)
        print('You are on a planet full of dragons. In front of you,')
        time.sleep(2)
        print('you see two caves. In one cave, the dragon is friendly')
        time.sleep(2)
        print('and will share his treasure with you. The other dragon')
        time.sleep(2)
        print('is greedy and hungry, and will attack you.')
        time.sleep(2)
        print('But if you are lucky enough you can meet with a mercahnt')
        print('and you can buy powefull gear from him')
        time.sleep(2)
        print('Good luck adventurer!')
        time.sleep(2)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(2)
        print('The first two cave is in front of you!')
        time.sleep(2)
    else:
        exit(0)
