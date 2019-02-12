import packages.characters as chars
import packages.Dragons as dragn
import packages.Intro as intro
import packages.mechanics as mech

player = chars.player()
dragon = dragn.dragon()
player.player_name = intro.getName()
chars.setChar(player,chars.showChars())
intro.showIntro(intro.getStarted())
cave = mech.chooseCave()
mech.checkCave(cave,dragon,player)
