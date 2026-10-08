#  creation of class player :
class Player:
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("welcome to the player", pseudo, "| health points:", health, "| attack points:", attack)  

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):          
        return self.attack

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def damage(self, amount):            
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def attack_player(self, target_player):
        if self.weapon is None:         
            degats = self.attack
        else:
            degats = self.attack + self.weapon.get_damage()
        target_player.damage(degats)