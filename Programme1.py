# File 2
from XS import player # type: ignore
from YZ import weapon   # type: ignore
player1=player("mohamed",20,3) # we define player1 as player() function 
player2=player("bob",20,5)   #   we define   player2   as   player()   function 
# we using attack_player() function 
knife=weapon("couteau",3) 

player1.equip_weapon(knife)
player1.attack_player(player2) # <--> here we used attack_player() with knife weapon function 
print(player1.get_pseudo(),"attaque :",player2.get_pseudo())
print("welcome to the player ",player1.get_pseudo(),"| heath points  :",player1.get_health(),"|attack points :",player1.get_attack_value())
print("Welcome to the player :",player2.get_pseudo(),"|health points :",player2.get_health(),"|attack points :",player2.get_attack_value())
player2.attack_player(player1)
print(" the player:",player2.get_pseudo(),"attack ",player1.get_pseudo()
      )
print(" Aie ",player1.get_pseudo(), " you get a damage :",player2.get_attack_value(),"health points :",player1.get_health())