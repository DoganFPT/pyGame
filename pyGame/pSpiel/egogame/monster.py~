class Monster:
    
    def __init__(self,lifepoints,damage,typ):
        self.lifepoints = lifepoints
        self.damage = damage
        self.typ = typ

    def attack(self):
        print(f"{self.typ} has done {self.damage} damage")
        return self.damage

    def isdefeated(self):
        if self.lifepoints <= 0:
            print(f"{self.typ} has been defeated")
        return

class Caster(Monster):

    def attack(self):
        return self.damage
 


class Org(Monster):

    def attack(self):
        return self.damage



