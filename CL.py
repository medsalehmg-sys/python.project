# creation of gamer classe :
class Gamer:
    def __init__(self,name,health,attack):
        self.name=name
        self.health=health
        self.attack=attack
        self.weapon=None
        print("welcome to the player :",name,"|health points :",health,"|attack points :",attack)

def get_name(self):
    return self.name
def get_health(self):
    return self.health
def get_attack_value(self):
    return self.attack
def damage(self,damage):
    if self.health>0:
         self.health-=damage
def attack_gamer(self,target_gamer):
        target_gamer.damage(self.attack)
def equip_weapon(self,weapon):
     self.weapon=weapon
     print("weapon equipped :",weapon.get_name())



