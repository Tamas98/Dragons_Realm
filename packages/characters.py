import time

class player:

    def __init__(self):
        player_name = ""
        player_class = ""
        player_max_hp = 0
        player_hp = 0
        player_dmg = 0
        player_shield = 0
        player_treasure = 0
        special_active = False

warrior = [ 120, 20, 10, 0,False ]
ninja = [ 80, 30, 1, 0,False ]
mage = [ 50, 50, 0, 0,False ]
#characters = { 'warrior':warrior, 'ninja':ninja, 'mage':mage }

def showChars():
    answ = ''
    while answ not in ['1','2','3']:
        print("Choose from the characters below: ")
        time.sleep(2)
        print("1.Warrior (120hp, 20dmg, 5 shield)")
        time.sleep(2)
        print("2.Ninja (80hp, 30dmg, 2 vanish)")
        time.sleep(2)
        print("3.Mage (50hp, 50dmg)")
        time.sleep(2)
        print("Choose one!(1 or 2 or 3)", end = ' ')
        answ = input()
        time.sleep(2)
    return int(answ)

def setChar(player_class,x):
    if x == 1:
        player_class.player_class = "warrior"
        player_class.player_max_hp = warrior[0]
        player_class.player_hp = warrior[0]
        player_class.player_dmg = warrior[1]
        player_class.player_shield = warrior[2]
        player_class.player_treasure = warrior[3]
        player_class.special_active = warrior[4]
        print("You choosed warrior!")
        time.sleep(2)
    elif x == 2:
        player_class.player_class = "ninja"
        player_class.player_max_hp = ninja[0]
        player_class.player_hp = ninja[0]
        player_class.player_dmg = ninja[1]
        player_class.player_shield = ninja[2]
        player_class.player_treasure = ninja[3]
        player_class.special_active = warrior[4]
        print("You choosed ninja!")
        time.sleep(2)
    elif x == 3:
        player_class.player_class = "mage"
        player_class.player_max_hp = mage[0]
        player_class.player_hp = mage[0]
        player_class.player_dmg = mage[1]
        player_class.player_shield = mage[2]
        player_class.player_treasure = mage[3]
        player_class.special_active = mage[4]
        print("You choosed mage!")
        time.sleep(2)
    return player

    
