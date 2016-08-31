import random
import Items as item
import Character as char
import Enemy as mob



class Location:
    location = "Dark Forest"

    # properties of location:
    # name, what monsters, level range
    # option for future additions.

    locationProperties = {"Default":
                              {"monstertypes":["Goblins", "Ogres", "Dragons"],
                               "levelRange": [1, 100]},
                          "Forest":
                              {"monstertypes": ["Goblins"],
                               "levelRange": [10, 20]},
                          "Dark Forest":
                              {"monstertypes": ["Goblins"],
                               "levelRange": [1, 2]}
                          }

#Random Number Generator
def RNG():
    higher_value = 10
    lower_value = 1
    final_value =random.randint(lower_value, higher_value)
    return final_value

def AddItems():
    Items.InventoryDict.append(RNG_Items())

def RemoveItems():
    Items.InventoryDict.remove()

def combat(enemy1):
    combat = True

# return location
# send location to monster type
# return monster type and stats


    mob.Enemy.monsterType(enemy1, Location)
    monster = enemy1.monster
    level = mob.monsterLevel
    print("you encountered a lvl " + str(level) + " " +str(monster ) + "!!")
    while combat:
        action = input('you can attack, run or examine the enemy with scan\n')
        if action == "attack" or action == "a":
            if RNG() >= 3:
                mob.Enemy.attack(enemy1)
                if mob.Enemy.isDeath(enemy1):
                    print("The " + monster + " falls down and makes it last wail before it dies")
                    char.Character.experience_gain(char, enemy1)
                    combat = False
                    if RNG() >= 2:
                        char.Character.inventoryDict.append(item.weapons.WeaponDrops(item.weapons))
#                        char.Character.inventoryDict.append(item.weapons.WeaponDrops())

                else:
                    char.Character.counter(char, enemy1)
            else:
                print("The " + monster + " avoided the hit")
                char.Character.counter(char, enemy1)
        elif action == "run" or action == "r":
            if RNG() <= 5:
                print("you failed to escape from the " + monster)
                char.Character.counter(char, enemy1)
            else:
                print("As fast as you can you leave the " + monster + " behind...")
                combat = False
        elif action == "scan" or action == "s":
            mob.Enemy.checkLife(enemy1)
            char.Character.counter(char, enemy1)
        else:
            print("You made a typo, you're brain freezes from embarrassment")
            char.Character.counter(char, enemy1)

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
        action = input("what will you do?\n")
        if action == "search" or action == "s":
            combat(mob)
        elif action == "leave" or action == "l":
            game = leaving_game()
        elif action == "check stat" or action == "stats" or action == "c":
            displayStats()
            print("do you want to switch weapons? Yes/No")
            switch()
        else:
            print("you can search, check your stats or leave.")

def switch():
    game = True
    while game:
        action = input("what will you do?\n")
        if action == "n" or action == "no":
            choices()
        elif action == "y" or action == "yes":
            print("which item do you like to equip?")
            char.Character.displayInventory(char)
            chosenItem = input("the name of the weapon is case sensitive\n")
            if chosenItem in inventoryDict:
                Items.InventoryDict.append(equipedWeapon)
                Items.equipedWeapon.append(chosenItem)
                Items.InventoryDict.remove(chosenItem)
                print("The "+ equipedWeapon +" is equiqed")

def displayStats():
    print("Current Stats: " + str(char.Character.stats))
    print("Current weapon: " + str(char.Character.equipedWeapon[0]))
    char.Character.displayInventory(char.Character)


#def displayInventory():
 #    print("Inventory: " + str(char.Character.inventoryDict))


print("You are in a dark forest")
print("your actions are attack and run unless you are told otherwise")

choices()


#if i want to make a save game, i can do so here.
'''
weapons made and default equip created. cant change the equip yet.
determine areas
determine random events
determine items
determine npc's
make AI!!!
make the monsters fit the levels better.
be able to determine the rarity of monsters.

'''