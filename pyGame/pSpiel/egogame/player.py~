class Player:

    level=0
    
    def __init__(self,lifepoints,manapoints,exp):

        self.lifepoints = lifepoints
        self.manapoints = manapoints
        self.exp = exp

        
    def attack(self):
        weapon = input("What do you want to use to attack? :")
        if weapon == "axe":
            damage = 40
            print("You have done", damage , "damage")
        elif weapon == "wand":
            damage = 50
            player1.manapoints-=10
            print("You have done", damage, "damage,your mana is",player1.manapoints)
        return damage
        

    def levelUp(self):
        if player1.exp >= 100:
            level+=1
            print("You have leveled Up! your level is" + level)
            player1.exp=0
        return self.exp


    def enoughMana(self):
        if self.manapoints < 20:
            print(f"nicht genug Mana, dein Mana beträgt  {self.manapoints}")
        return self.manapoints


    def gameOver(lifepoints):
        if self.lifepoints <= 0:
            print("Game Over")


player1 = Player(200,100,0)



