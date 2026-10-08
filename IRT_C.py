# Herritage oncept:
# we create a player class:
class player():
    def init(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("welcome to the player :", pseudo, "|health points :", health, "|attack points :", attack) # as function

    def get_pseudo(self): # get function without characteristics change 
        return self.pseudo

    def get_health(self): # \\\\\\\
        return self.health

    def get_attack_value(self): #\\\\\\
        return self.attack

    def damage(self, damage): #\\\\\\\\\
        self.health -= damage

    def attack_player(self, target_player):
        target_player.damage(self.attack) #----->


# we create a warrior class:
class warrior(player):
    def init(self, pseudo, health, attack):
        super().init(pseudo, health, attack) # we use here super() class :
        self.armor = 3 # we giving a defaut value 
        print("welcome to the hero:", pseudo, "health points:", health, "attack points :", attack)

    def damage(self, damage):
        if self.armor > 0:   # we use if condition self.armor>0 in damage function()
            self.armor -= 1  # in this case he lost -1
            damage = 0       # and damage=0
        super().damage(damage)  # we use super class damage from damage function {}

    def blade(self):
        self.armor = 3
        print("armor points were reacharged")

    def get_armor_points(self):
        return self.armor


dark_warrior = warrior("Dark_warrior", 20, 7) # default value 
dark_warrior.damage(15) # ------> dark_warrior -15

print("welcome to the hero :", dark_warrior.get_pseudo(), "|health points :", dark_warrior.get_health(), "|armor points :", dark_warrior.get_armor_points())
dark_warrior.damage(15)

print("welcome to the hero :", dark_warrior.get_pseudo(), "|health points :", dark_warrior.get_health(), "|armor points :", dark_warrior.get_armor_points())
dark_warrior.damage(15)