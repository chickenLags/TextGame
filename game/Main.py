import random
from Character import Character
from Enemy import Enemy
from Action import Action
from Location import Location
from Items import Weapon, Item, ItemManager, Armour


location = Location()
itemManager = ItemManager()
character = Character(itemManager)
#character._forceEquip( Weapon ( itemManager.getMaterial("Rusty"), itemManager.getWeaponType("Dagger") ) )
character._forceEquip( Armour ( itemManager.getMaterial("Rusty"), itemManager.getArmourType("Leggings") ) )
character.inventory.add(itemManager.generateWeapon())
character.inventory.add(itemManager.generateWeapon())


#potato = getattr(character, "displayStats")
#potato()


#Random Number Generator
def RNG_under_ten(lower_value = 1, higher_value = 10):
    return random.randint(lower_value, higher_value)


def combat():
    combat = True
    enemy = Enemy(location)
    
    print("you encountered a lvl " + str(enemy.level) + " " +str(enemy.name) + "!!")
    while combat:
        action = input('you can attack, run or examine the enemy with scan\n')
        if action in Action.attack:
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
                        character.inventory.add(itemManager.generateWeapon())

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

        elif action in Action.run:
            if RNG_under_ten() <= 5:
                print("you failed to escape from the " + enemy.name)
                character.damage(enemy.getDamage())
            else:
                print("As fast as you can you leave the " + enemy.name + " behind...")
                combat = False
        elif action in Action.scan:
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
            character.displayStats()
        elif action == "check inventory" or action == "inventory" or action == "i" or action == "inv":
            check_inventory()
        else:
            print("you can search, check your stats or leave.")

def getAction(string):
    command = input(string + "\n => ")
    print("")
    if command.count(" ") > 0:
        action, argument = command.split(" ", 1)
        return action, argument

    else:
        return command, ""

def check_inventory():
    in_inventory = True
    while in_inventory:
        print("You have the following items in your inventory:")
        print(str(character.inventory.getInventoryAsList()))
        action, argument = getAction(" you can leave or equip <item name>.")
        if action in Action.leave:
            in_inventory = False
        elif action in Action.equip:
            character.equip(argument)

        else:
            print("I have no such item in my inventory...")

# spacing after typing.
#
# on entry text
# in loop text
#
# actions allowed + argument allowed +  text connected to action + consequences()
#
# else text

def gameEntry():
    while Playing:
        instance.entryMessages()
        while instance.running:
            instance.loopEntryMessages()
            action, argument = getAction(instance.inputMessage())
            if instance.options.containsAction(action):
                option.actionEntryMessage()     ##
                option.actions()          ##
                option.actionEndMessage()       ##
                instance.loopEndMessages()
            else:
                instance.elseMessages()


class Option:
    def __init__(self, actions):
        self.actions = actions

    def containsAction(self, action, argument):
        for option in self.actions:
            if action in option.synonims:
                return option


class Instance:
    def __init__(self, entryMessages, loopEntryMessages, inputMessage, options, loopEndMessages, elseMessages):
        self.entryMessages = entryMessages
        self.loopEntryMessages = loopEntryMessages
        self.inputMessage = inputMessage
        self.options = options
        self.loopEndMessages = loopEndMessages
        self.elseMessages = elseMessages
        self.running = True

    def entryMessages(self):
        for message in self.entryMessages:
            print(message)

    def loopEntryMessages(self):
        for message in self.loopEntryMessages:
            print(message)

    def inputMessage(self):
        return self.inputMessage


    def loopEndMessages(self):
        for message in self.loopEndMessages():
            print(message)

    def loopElseMessages(self):
        for message in self.loopElseMessages():
            print(message)






print("You are in a dark forest")
print("your actions are attack and run unless you are told otherwise")

choices()


#if i want to make a save game, i can do so here.
'''
    DONE: weapons made and default equip created. 
    DONE: can change the equip.
    DONE: prevent items from being equiped
    DONE: reworked the items, material, and equipType to make it OOP
    DONE: fixed combat with no weapons.
    DONE: fix damage and other functions
    DONE: fix displayname for nonetype equipment
    DONE: fix pop of nonexsistent equipment
    rework statemachine => SEEMS IMPLEMENTED, SHOULD TRY IT WITH COMBAT CLASS...
    make actions easily visible
    fix defences for the player
    fix defences for the enemy
    create a combat situation ~> multiple enemies and more interesting dynamics 
    make save game
    determine areas
    determine random events
    determine items
    determine npc's
    make AI!!!
    make the monsters fit the levels better.
    be able to determine the rarity of monsters.

'''