from Character import Character
from Action import Action, Instance
from items.item_type import ItemType
from locations.Location import *
from items.Item import Weapon
from items.item_manager import ItemManager
# from locations.location_forest import LocationForest


def RNG_under_ten(lower_value = 1, higher_value = 10):
    return random.randint(lower_value, higher_value)

def leaving_game():
    game_choice = input(
        "Do you wish to leave the forrest behind and live a safe life from now on? (Yes/No)\n"
    )
    escaping = True
    while escaping:
        if game_choice == "yes" or game_choice == "y":
            game = False
            print('You Turn around start walking leaving this hellhole behind, \n'
                  'however, you can\'t help but look over your shoulder once more wondering what '
                  'would happen if you had stayed...')
            return game
        elif game_choice == "no" or game_choice == "n":
            game = True
            print("You find new determination and head back to the forest!")
            return game
        else:
            game_choice = input("What? Do you or don't you? (yes/No)\n")

def getAction(string):
    command = input(string + "\n\n => ")
    print("")
    if command.count(" ") > 0:
        action, argument = command.split(" ", 1)
        return action, argument

    else:
        return command, ""


def gameEntry():
    while instance.playing:
        instance.running = True
        instance.printMessages(instance.getCurrentInstance().entryMessages)
        while instance.running:
            instance.printMessages(instance.getCurrentInstance().loopEntryMessages)
            action, argument = getAction(instance.getCurrentInstance().inputMessage)
            if instance.getCurrentInstance().containsAction(action):
                retrievedAction = instance.getCurrentInstance().containsAction(action)
                instance.printMessages( retrievedAction.entryMessages )
                retrievedAction.compute(argument)
                instance.printMessages(retrievedAction.endMessages)
                instance.printMessages(instance.getCurrentInstance().loopEndMessages )
            elif instance.getBaseActions(action):
                retrievedAction = instance.getBaseActions(action)
                instance.printMessages(retrievedAction.entryMessages)
                retrievedAction.compute(argument)
                instance.printMessages(retrievedAction.endMessages)
                instance.printMessages(instance.getCurrentInstance().loopEndMessages)
            else:
                instance.printMessages( instance.getCurrentInstance().elseMessages )


im = ItemManager()
character = Character()
w1 = Weapon (im.get_material('Rusty'), im.get_weapon_type("Dagger"))
character._force_equip(w1, silent=True)

# Testing equiping weapon.
# r1 = im.generateWeapon()
# character.inventory.add(r1)
# character.equip(r1.get_name()  )

# testing inventory show.
# print(character.equipment._equipment)
# for type_ in ItemType:
#     print(type_.name, character.equipment.getName(type_))


instance = Instance(im, character)
instance.gotoInstance(LocationForest(instance, character, Action))
gameEntry()


'''
@Todos:
add testing
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


'''