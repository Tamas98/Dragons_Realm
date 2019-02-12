import random
import time
import pickle
import packages.Dragons as drgn
import packages.characters as char

player_starts = False

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    return cave

def seq():
    print('You approach the cave....')
    time.sleep(2)
    print('It is dark and spooky....')
    time.sleep(2)
    print('You see a dark shape in front of you...')
    time.sleep(2)

def decide(dragon,player):
    begin = random.randint(1,2)
    if begin == 1:
        print("You can attack the dragon first or you can try to run away...")
        time.sleep(2)
        print("Attack or Run?")
        answ = input()
        if answ.lower().startswith('r'):
            run(dragon,player)
        else:
            player_starts = True
            battle(dragon,player,player_starts)
           
    else:
        player_starts = False
        battle(dragon,player,player_starts)
        
def checkCave(choosenCave,dragon,player):
    seq()
    friendlyCave=random.randint(1,10)

    if friendlyCave <= 3:
        treasureGet(dragon,player) 
        
    elif friendlyCave <= 9 and friendlyCave > 3:
        drgn.setDragonStats(dragon,drgn.chooseDragon())
        print('And it\'s a large ' + dragon.dragon_name + ' who attacks you!')
        decide(dragon,player)
    else:
        print("You are so lucky!You found a merchant")
        merchant(dragon,player)

def run(dragon,player):
    print('You are trying to run away! I will roll a dice for you!')
    print('If you are lucky enough you can rucn away.If you are not.You have to fight')
    time.sleep(2)
    res = random.randint(1,6)
    if dragon.dragon_name in ['Red Dragon','Green Dragon','Blue Dragon']:
        if res <= 2:
             runAway(dragon,player)
        elif res <= 4 and res > 2:
            print("The dragon cuts your way out but you still can surprise it!")
            player_starts = True
            battle(dragon,player,player_starts)
        else:
            print("Unfortunatly you can't run away and the dragon surprised you with an attack!")
            player_starts = False
            battle(dragon,player,player_starts)
    else:
        if res == 6:
            runAway(dragon,player)
        else:
            player_starts = False
            
def battle(dragon,player,starts):
    if player.player_class is 'ninja':
        player.player_shield = 2
        
    battleIntro(dragon,player)
    special_player = False
    special_dragon = False
    player_turn = starts
    while player.player_hp >= 0 or dragon.dragon_hp >= 0:
        if player_turn:
           playerAttack(dragon,player)
           player_turn = False
        else:
            dragonAttack(dragon,player)
            player_turn = True
        print("Current HP\'s: ")
        print("Player: " + str(player.player_hp))
        print("Dragon: " + str(dragon.dragon_hp))
        if dragon.dragon_hp <= 0:
            time.sleep(1)
            print("You survived! You can collect the dragon\'s treasure!")
            player.player_treasure += dragon.dragon_treasure
            time.sleep(1)
            print("You got " + str(dragon.dragon_treasure) +" gold")
            time.sleep(1)
            print("Let\'s continue your adventure!")
            continoue(dragon,player)
            break
        if player.player_hp <= 0:
            chs = {}
            print("You Died!")
            time.sleep(2)
            print("High scores:")
            with open(highscores.txt, ab) as hs:
                dct = {player.player_name:player.player_treasure}
                pickle.dump(dct,hs)
            chs = pickle.load(hs)
            print(chs)
            time.sleep(2)
            print("Game Over!")
            time.sleep(5)
            break
                        
def runAway(dragon,player):
    print("You succesfully ran away.")
    time.sleep(2)
    continoue(dragon,player)

def battleIntro(dragon,player):
    print("Your stats: ")
    time.sleep(1)
    print("HP: " + str(player.player_hp))
    time.sleep(1)
    print("DMG: " + str(player.player_dmg))
    time.sleep(1)
    print("special: " + str(player.player_shield))
    time.sleep(1)
    print()
    time.sleep(1)
    print(dragon.dragon_name + "\'s stats: ")
    time.sleep(1)
    print("HP: " +  str(dragon.dragon_hp))
    time.sleep(1)
    print("DMG: " + str(dragon.dragon_dmg))
    time.sleep(1)
    print("Treasure: " + str(dragon.dragon_treasure))
    time.sleep(1)
    print()
    time.sleep(2)

def playerAttack(dragon,player):
    attack = ''
    print("Your turn!")
    time.sleep(1)
    print("Choose you attack type: ")
    time.sleep(2)
    if player.player_class is "warrior":
        warrior_attack(dragon,player)
    elif player.player_class is "ninja":
        ninja_attack(dragon,player)
    else:
        mage_attack(dragon,player)



def treasureGet(dragon,player):
    print('and it\'s a friendly dragon!')
    time.sleep(2)
    print('who gives you his treasures!')
    treasure = random.randint(100,500)
    player.player_treasure += treasure
    print('You got ' + str(treasure) + ' gold and you have ' + str(player.player_treasure) + ' gold right now!')
    time.sleep(2)
    continoue(dragon,player)

def dragonAttack(dragon,player):
    print("The dragon attacks!")
    time.sleep(1)
    if player.special_active and player.player_class is "warrior":
        attack = random.randint(1,3)
        if attack is 1:
            print("The dragon attacks you with his firebreath!")
            player.player_hp -= dragon.dragon_dmg-player.player_shield*2
            player.special_active = False
        elif attack is 2:
            print("The dragon attacks you with his claws!")
            player.player_hp -= dragon.dragon_dmg-player.player_shield*2
            player.special_active = False
        else:
            print("The dragon bites you with his sharp teeth!")
            player.player_hp -= dragon.dragon_dmg-player.player_shield*2
            player.special_active = False
 
            
    elif dragon.special_active and player.player_class is "warrior":
        attack = random.randint(1,3)
        if attack is 1:
            print("The dragon attacks you with his firebreath!")
            player.player_hp -= dragon.dragon_dmg
            dragon.special_active = False
        elif attack is 2:
            print("The dragon attacks you with his claws!")
            player.player_hp -= dragon.dragon_dmg
            dragon.special_active = False
        else:
            print("The dragon bites you with his sharp teeth!")
            player.player_hp -= dragon.dragon_dmg
            dragon.special_active = False

    elif dragon.special_active and player.player_class is "ninja":
        attack = random.randint(1,3)
        if attack is 1:
            print("The dragon attacks you with his firebreath!")
            player.player_hp -= dragon.dragon_dmg*2
            dragon.special_active = False
        elif attack is 2:
            print("The dragon attacks you with his claws!")
            player.player_hp -= dragon.dragon_dmg*2
            dragon.special_active = False
        else:
            print("The dragon bites you with his sharp teeth!")
            player.player_hp -= dragon.dragon_dmg*2
            dragon.special_active = False

    elif player.special_active and player.player_class is "ninja":
        attack = random.randint(1,3)
        if attack is 1:
            print("The dragon attacks you with his firebreath!")
            time.sleep(2)
            print("And he missed it!")
            player.special_active = False
        elif attack is 2:
            print("The dragon attacks you with his claws!")
            time.sleep(2)
            print("And he missed it!")
            player.special_active = False
        else:
            print("The dragon bites you with his sharp teeth!")
            time.sleep(2)
            print("And he missed it!")
            player.special_active = False

    elif dragon.special_active and player.player_class is "mage":
        attack = random.randint(1,3)
        if attack is 1:
            print("The dragon attacks you with his firebreath!")
            player.player_hp -= dragon.dragon_dmg*2
            dragon.special_active = False
            dragonAttack(dragon,player)
        elif attack is 2:
            print("The dragon attacks you with his claws!")
            player.player_hp -= dragon.dragon_dmg*2
            dragon.special_active = False
            dragonAttack(dragon,player)
        else:
            print("The dragon bites you with his sharp teeth!")
            player.player_hp -= dragon.dragon_dmg*2
            dragon.special_active = False
            dragonAttack(dragon,player)

    elif player.special_active and player.player_class is "mage":
        attack = random.randint(1,3)
        if attack is 1:
            print("The dragon attacks you with his firebreath!")
            player.player_hp -= dragon.dragon_dmg//2
            dragon.dragon_hp -= dragon.dragon_dmg//2
            player.special_active = False

        elif attack is 2:
            print("The dragon attacks you with his claws!")
            player.player_hp -= dragon.dragon_dmg//2
            dragon.dragon_hp -= dragon.dragon_dmg//2
            player.special_active = False
        else:
            print("The dragon bites you with his sharp teeth!")
            player.player_hp -= dragon.dragon_dmg//2
            dragon.dragon_hp -= dragon.dragon_dmg//2
            player.special_active = False

    else:
        dragonAttackNoSpec(dragon,player)
            
def continoue(dragon,player):
    print("Now you are heading to the next two caves")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)   
    print(".")
    time.sleep(2)
    cave = chooseCave()
    checkCave(cave,dragon,player)

#CLASS ATTACKS

def warrior_attack(dragon,player):
    attack = ''
    print("1.Heavy attack: " + str(player.player_dmg*2) + " (if you choose this one you can\'t defend yourself for one turn)")
    time.sleep(1)
    print("2.Normal attack: "+ str(player.player_dmg) + " (normal attack)")
    time.sleep(1)
    print("3.Fast attack: " + str(player.player_dmg//2) + " (half of your dmg but you can defend twice as much as you normally can in the next turn)")
    time.sleep(1)
    while attack not in ['1','2','3']:
        print("Choose: ", end = ' ')
        attack = input()
    if attack is '1':
        dragon.dragon_hp -= player.player_dmg*2
        dragon.special_active = True
    elif attack is '2':
        dragon.dragon_hp -= player.player_dmg
    else:
        dragon.dragon_hp -= player.player_dmg//2
        player.special_active = True

def ninja_attack(dragon,player):
    attack = ''
    print("1.Melee attack: " + str(player.player_dmg*2) + " (double of your damege but the dragon will damage double too")
    time.sleep(1)
    print("2.Shuriken attack: " + str(player.player_dmg*1.5) + " (normal attack)")
    time.sleep(1)
    print("3.Vanishing attack: " + str(player.player_dmg) + " (if you choose this you will vanish from the dragons next attack)")
    time.sleep(1)
    while attack not in ['1','2','3']:
        print("Choose: ", end = ' ')
        attack = input()
    if attack is '1':
        dragon.dragon_hp -= player.player_dmg*2
        dragon.special_active = True
    elif attack is '2':
        dragon.dragon_hp -= player.player_dmg*1.5
    elif attack is '3' and player.player_shield > 0:
        dragon.dragon_hp -= player.player_dmg
        player.player_shield = player.player_shield - 1
        player.special_active = True

def mage_attack(dragon,player):
    attack = ''
    print("1.Ultimate spell: " + str(player.player_dmg*2) + " (double of your damege but you can't attack next turn and the dragon will damage double")
    time.sleep(1)
    print("2.Fire bomb: " + str(player.player_dmg) + " (normal attack)")
    time.sleep(1)
    print("3.Defence spell: " + str(player.player_dmg//2) + " (half of your damage but deflect half of the dragons damage)")
    time.sleep(1)
    while attack not in ['1','2','3']:
        print("Choose: ", end = ' ')
        attack = input()
    if attack is '1':
        dragon.dragon_hp -= player.player_dmg*2
        dragon.special_active = True
    elif attack is '2':
        dragon.dragon_hp -= player.player_dmg*1
    else:
        dragon.dragon_hp -= player.player_dmg//2
        player.special_active = True

#MERCHANT THINGS

def merchant(dragon,player):
    print("Hello there adventurer")
    time.sleep(2)
    print("Take a look: ")
    if player.player_class is "mage":
        merchant_mage()
    elif player.player_class is "ninja":
        merchant_ninja()
    else:
        merchant_warrior()
    choosed = ' '
    while choosed not in ['1','2','3','4','5']:
         print("Choose one!",end = ' ')
         choosed = input()
    merchant_choose(dragon,player,choosed)

def merchant_mage():
    print("1.Fire staff(dmg + 5) for 1000 gold")
    time.sleep(1)
    print("2.Health potion(restores maximum health) for 750 gold")
    time.sleep(1)
    print("3.Hearth potion(Gives you 20 extra hp points) for 1500 gold")
    time.sleep(1)
    print("4.Legendary wand(Increase you damage by 20) for 2500 gold")
    time.sleep(1)
    print("5.Nothing")
    time.sleep(2)

def merchant_warrior():
    print("1.Steel sword(dmg + 5) for 1000 gold")
    time.sleep(1)
    print("2.Health potion(restores maximum health for 750 gold")
    time.sleep(1)
    print("3.Hearth potion(Gives you 20 extra hp points) for 1500 gold")
    time.sleep(1)
    print("4.Legendary spear(Gives you 20 extra damage) for 2500 gold")
    time.sleep(1)
    print("5.Nothing")
    time.sleep(2)

def merchant_ninja():
    print("1.Katana(dmg + 5) for 1000 gold")
    time.sleep(1)
    print("2.Health potion(restores maximum health for 750 gold")
    time.sleep(1)
    print("3.Hearth potion(Gives you 20 extra hp points) for 1500")
    time.sleep(1)
    print("4,Wish Ender bow(Gives you 20 extra damage) for 2500 gold")
    time.sleep(1)
    print("5.Nothing")
    time.sleep(2)

def dragonAttackNoSpec(dragon,player):
    attack = random.randint(1,3)
    if attack is 1:
        print("The dragon attacks you with his firebreath!")
        player.player_hp -= dragon.dragon_dmg
    elif attack is 2:
        print("The dragon attacks you with his claws!")
        player.player_hp -= dragon.dragon_dmg
    else:
        print("The dragon bites you with his sharp teeth!")
        player.player_hp -= dragon.dragon_dmg
    dragon.special_active = False
    player.special_active = False

def merchant_choose(dragon,player,decide):
    if decide is '1' and player.player_treasure >= 1000:
        player.player_dmg = player.player_dmg + 5
        player.player_treasure = player.player_treasure - 1000
        print("Thanks for shopping " + player.player_name)
        continoue(dragon,player)
    elif decide is '2' and player.player_treasure >= 750:
        player.player_hp = player.player_max_hp
        print("Thanks for shopping " + player.player_class)
        continoue(dragon,player)
    elif decide is '3' and player.player_treasure >= 1500:
        player.player_max_hp = player.player_max_hp + 20
        player.player_hp = player.player_max_hp
        continoue(dragon,player)
        #print("Do you want do continue shopping? (yes or no)", end = " ")
        #answ = input()
        #if answ[0] is 'y':
    elif decide is '4' and player.player_treasure >= 2500:
        player.player_dmg = player.player_dmg + 20
        continoue(dragon,player)
    elif decide is '5':
        print("Sorry to hear that.Bye")
        continoue(dragon,player)
    else:
        print("You don\'t have enough money to buy this.Choose again!")
        decide = input()
        merchant_choose(dragon,player,decide)
        
        
