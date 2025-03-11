from monster import Monster,Caster,Org
from player import Player


class maingame:
    player1=Player(100,100,0)
    o1 = Org(70,20,"org")
    while player1.lifepoints >= 1:
        print("An org is attacking you!")
        damage=player1.attack()
        o1.lifepoints -= damage
        print("Org hast",o1.lifepoints,"lifepoints left")
        if o1.lifepoints <=0:
            o1.isdefeated()
            player1.exp+=40
            o1.lifepoints=100
            print("Your exp is", player1.exp)
            continue
        damagetaken = o1.attack()
        player1.lifepoints -= damagetaken
        print("You have taken" , damagetaken, "damage your health is", player1.lifepoints)
        


o1 = Org(70,20,"org")
c1 = Caster(60,30,"caster")




