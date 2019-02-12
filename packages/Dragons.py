import random

class dragon:

    def __init__(self):
        dragon_name = ''
        dragon_hp = 0
        dragon_dmg = 0
        dragon_treasure = 0
        special_active = False

red_dragon = (200,10,random.randint(189,1000),False)
blue_dragon = (100,15,random.randint(265,1000),False)
green_dragon = (150,20,random.randint(321,1000),False)
void_dragon =(500,50,random.randint(1000,10000),False)
name_list = ('Red Dragon','Blue Dragon','Green Dragon','Void Dragon')

dragon_dict = { 'Red Dragon':red_dragon,
                'Blue Dragon':blue_dragon,
                'Green Dragon':green_dragon,
                'Void Dragon':void_dragon }

def chooseDragon():
    rand = random.randint(1,67)
    if rand <= 22:
        dragon.dragon_name = name_list[0]
        choosen = dragon_dict[name_list[0]]
    elif rand <= 44 and rand > 22:
        dragon.dragon_name = name_list[1]
        choosen = dragon_dict[name_list[1]]
    elif rand <= 66 and rand > 44:
        dragon.dragon_name = name_list[2]
        choosen = dragon_dict[name_list[2]]
    elif rand == 67:
        dragon.dragon_name = name_list[3]
        choosen = dragon_dict[name_list[3]]
    return [dragon.dragon_name,choosen]

def setDragonStats(entity,choosen_dragon):
    entity.dragon_name = choosen_dragon[0]
    entity.dragon_hp = choosen_dragon[1][0]
    entity.dragon_dmg = choosen_dragon[1][1]
    entity.dragon_treasure = choosen_dragon[1][2]
    entity.special_active = choosen_dragon[1][3]
