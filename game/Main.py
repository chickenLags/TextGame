import random
from Character import Character
from Enemy import Enemy
from Action import Action
from Location import Location
from Items import Weapon, Item, ItemManager

actions = Action()
location = Location()
character = Character()
character.equipweapon(Weapon("Rusty Dagger", "Dagger", "Rusty"))
itemManager = ItemManager()

#Random Number Generator
def RNG_under_ten(lower_value = 1, higher_value = 10):
    return random.randint(lower_value, higher_value)


def combat():
    combat = True

# return location
# send location to monster type
# return monster type and stats
    enemy = Enemy(location)
    
    print("you encountered a lvl " + str(enemy.level) + " " +str(enemy.name) + "!!")
    while combat:
        action = input('you can attack, run or examine the enemy with scan\n')
        if action in actions.attack:
            if RNG_under_ten() >= 3: #determines whether i hit the enemy
                print("you make a swing for it and hit the " + enemy.name + " perfectly on the spot ")
                print("the " + enemy.name + " makes a painful sound!")
                enemy.damage(character.getDamage())
                character.weaponErosion()

                if enemy.isDead():
                    print("The " + enemy.name + " falls down and makes it last wail before it dies")
                    character.experience_gain(enemy.getExperience())
                    combat = False

                    if RNG_under_ten() >= 2:
                        character.inventory.append(itemManager.generateWeapon())

                else:
                    character.damage(enemy.getDamage())
                    if not character.isAlive():
                        print(enemy.getDeathMessage())
                        character.die()

            else:
                print("The " + enemy.name + " avoided the hit")
                character.damage(enemy.getDamage())
                if not character.isAlive():
                    print(enemy.getDeathMessage())
                    character.die()

        elif action in actions.run:
            if RNG_under_ten() <= 5:
                print("you failed to escape from the " + enemy.name)
                character.damage(enemy.getDamage())
            else:
                print("As fast as you can you leave the " + enemy.name + " behind...")
                combat = False
        elif action in actions.scan:
            enemy.checkLife()
            character.damage(enemy.getDamage())
        else:
            print("You made a typo, you're brain freezes from embarrassment")
            character.damage(enemy.getDamage())

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

def choices():
    print("You see nothing of interest around.")
    game = True
    while game:
        action = input("what will you do in " + location.name + "?\n")
        if action == "search" or action == "s":
            combat()
        elif action == "leave" or action == "l":
            game = leaving_game()
        elif action == "check stat" or action == "stats" or action == "c":
            displayStats()
        elif action == "check inventory" or action == "inventory" or action == "i" or action == "inv":
            check_inventory()
        else:
            print("you can search, check your stats or leave.")

def getAction(string):
    command = input(string + "\n =>")
    if command.count(" ") > 0:
        action, argument = command.split(" ", 1)
        return action, argument

    else:
        return command, ""

def check_inventory():
    in_inventory = True
    print("You have the following items in your inventory")
    print(str(character.getInventoryAsList()))
    while in_inventory:
        action, argument = getAction(" you can leave or equip <item name>.")
        if action in actions.leave:
            in_inventory = False
        elif action in actions.equip:
            if argument in character.getInventoryAsList():
                character.inventory.append(character.weapon)
                for item in character.inventory:
                    if item.name == argument:
                        character.weapon = character.inventory.pop(character.inventory.index(item))
                        print("equiped " + character.weapon.name)
            else:
                print("I have no such item in my inventory...")


def displayStats():
    print("======= Current Stats =======")
    for key in character.stats:
        print(" \t" + key + ": \t" + str(character.stats[key]) )
    print("======= Current weapon =======")
    print("\t" + str(character.weapon.name))




print("You are in a dark forest")
print("your actions are attack and run unless you are told otherwise")

choices()


#if i want to make a save game, i can do so here.
'''
    DONE: weapons made and default equip created. 
    DONE: can change the equip.
    prevent items from being equiped
    make save game
    determine areas
    determine random events
    determine items
    determine npc's
    make AI!!!
    make the monsters fit the levels better.
    be able to determine the rarity of monsters.

'''