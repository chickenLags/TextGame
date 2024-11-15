from Character import Character
from Action import Action
from game import Game
from items.weapon import Weapon
from locations.Location import *

from items.item_manager import ItemManager


im = ItemManager()
character = Character()
w1 = Weapon(im.get_material('Rusty'), im.get_weapon_type("Dagger"))
w2 = Weapon(im.get_material('Rusty'), im.get_weapon_type("Sword"))
character._force_equip(w1, silent=True)
character.give(w2)


game = Game(im, character)
game.gotoInstance(LocationForest(game, character, Action))
game.start()


'''
@Todos:
should change comparator from equipable to item?
merge equipable and EquipType
expand ItemType to include Misc items.
EquipType should exists then too....

store location data in db and make it data based.

Currently program is not working because of a circular dependency in locations (forest and Dark forest)
- use graph to define how world looks instead of giving adjacent locations to location.

add easy alternative selection for list options (inventory, locations(gocommande), etc)
rework enemy creation
rework battle functions
rework battle mechanics
add situational things to battles
create a combat situation ~> multiple enemies and more interesting dynamics
fix defences for the player
fix defences for the enemy
add be able to determine the rarity of monsters.
expand on monster skills and behavior
make the monsters fit the levels better.
add other results for search action
add method of journeying through areas -> make it more engaging. perhaps multiple locations in the forest (location)?
SUSPENDED-UNNESSARY: add a method to make use of chance
examine weapon - > stats should be its own location.
add "examine" for items in inventory
add movement of monsters or npcs between locations.


add visual interface

add story?
add save game functionality
add random events
add items
add npc's
make AI!!!

add gathering:
- add mineral nodes
- add organic nodes (flowers, trees, mushrooms)
- add wildlive (hunting deer, rabbits, bears, etc)
- weight limits or item limit. require cart or other help to gather more and to move it.

refactor main loop for readability

was making the sql tables and making modifations in the items.py file: refactoring.

multiple enemy fights

add second screen for inventory
 - terminal seems impossible, however I could do a window screen with pygame.
 - pyglet?

'''