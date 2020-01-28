import random
from Character import Character
from Enemy import Enemy
from Action import Action, Instance
from Location import *
from Items import Weapon, Item, ItemManager, Armour



#Random Number Generator
def RNG_under_ten(lower_value = 1, higher_value = 10):
    return random.randint(lower_value, higher_value)

def leaving_game():
    game_choice = input("Do you wish to leave the forrest behind and live a safe life from now on? (Yes/No)\n")
    escaping = True
    while escaping:
        if game_choice == "yes" or game_choice == "y":
            game = False
            print('You Turn around start walking leaving this hellhole behind, \nhowever, you can\'t help but look over your shoulder once more wondering what would happen if you had stayed...')
            return game
        elif game_choice == "no" or game_choice == "n":
            game = True
            print("You find new determination and head back to the forest!")
            return game
        else:
            game_choice = input("What? Do you or don't you? (yes/No)\n")

def getAction(string):
    command = input(string + "\n => ")
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


itemManager = ItemManager()
character = Character(itemManager)
character._forceEquip( Weapon ( Material("Rusty"), itemManager.getWeaponType("Dagger") ), silent=True )
# character._forceEquip( Weapon ( itemManager .getMaterial("Rusty"), itemManager.getWeaponType("Dagger") ), silent=True )
# character._forceEquip( Armour ( itemManager.getMaterial("Rusty"), itemManager.getArmourType("Leggings") ), silent=True )
#character.inventory.add(itemManager.generateWeapon())
#character.inventory.add(itemManager.generateWeapon())


instance = Instance(itemManager, character)
instance.gotoInstance(LocationForest(instance, character, Action))
gameEntry()



def Done():
    pass

def Todo():
    '''
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

    was making the sql tables and making modifations in the items.py file: refactoring.
    

'''