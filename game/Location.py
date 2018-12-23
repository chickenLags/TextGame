
from Enemy import Enemy
#from Action import Action
import random


class Location:
    name = "Dark Forest"

    # properties of location:
    # name, what monsters, level range
    # option for future additions.

    properties = {"Default":
                      {"monstertypes":["Goblins", "Ogres", "Dragons"],
                       "levelRange": [1, 100]},
                  "Forest":
                      {"monstertypes": ["Goblins"],
                       "levelRange": [10, 20]},
                  "Dark Forest":
                      {"monstertypes": ["Goblins"],
                       "levelRange": [1, 2]}
                  }

    def getMonster(self, random):
        monsterType = self.properties[self.name]['monstertypes'][random.randrange(0, len(self.properties[self.name]["monstertypes"]))]
        return monsterType

    def getLevelRange(self):
        return self.properties[self.name]["levelRange"]

class LocationBase:
    def __init__(self, instance, character):
        self.entryMessages = []
        self.loopEntryMessages = []
        self.inputMessage = ""
        self.loopEndMessages = []
        self.elseMessages = []
        self.actions = []
        self.enemies = []
        self.name = ""
        self.description = []
        self.connectedAreas = []



    def containsAction(self, action):
        for a in self.actions:
            if action in a.synonims:
                return a
        return False

class LocationInventory(LocationBase):
    def __init__(self, instance, character):
        super(LocationInventory, self).__init__(instance, character)
        self.name = "inventory"
        self.loopEntryMessages = ["You have the following items in your inventory:",
                                  character.inventory.getInventoryAsList]
        self.inputMessage = "You can leave or equip <item name>."
        self.actions.append( LocationBase.Action("leave", LocationBase.Action.leave, [], [instance.leaveInstance ], ["You left your inventory."]) )
        self.actions.append( LocationBase.Action("equip", LocationBase.Action.equip, [], [character.equip], [] ) )


        self.connectedAreas = []

# name, synonims, entryMessages, computations, endMessages




def RNG_under_ten(lower_value = 1, higher_value = 10):
    return random.randint(lower_value, higher_value)



class LocationCombatInstance(LocationBase):
    def __init__(self, instance, character):
        super(LocationCombatInstance, self).__init__(instance, character)
        self.enemy = Enemy(instance.getParentInstance())    # location should be changed to allow for enemy creation
        self.character = character
        self.instance = instance
        self.entryMessages.append("You encountered a lvl." + str(self.enemy.level) + " " + str(self.enemy.name) + ".")
        self.inputMessage = 'you can attack, run or examine the enemy with scan\n'

            # add attack with eitherOption
        #self.actions.append( LocationBase.Action("Attack", LocationBase.Action.attack, [], [self.attemptAttack], []) )
        attackLambda = lambda : self.enemy.attack(self.character, self.instance)
        self.actions.append( LocationBase.Action("Attack", LocationBase.Action.attack, [], [attackLambda], []))

        self.actions.append( LocationBase.Action("Run", LocationBase.Action.run, [], [self.run], []) )
        getAttacked = lambda : self.character.attack(self.enemy)
        self.actions.append( LocationBase.Action("Examine", LocationBase.Action.examine, [], [self.enemy.checkLife, getAttacked], []) )

        self.name = "combat"

    def run(self):
        if RNG_under_ten() <= 5:
            print("you failed to escape from the " + self.enemy.name)
            self.character.damage(self.enemy.getDamage())
        else:
            print("As fast as you can you leave the " + self.enemy.name + " behind...")
            self.instance.leaveInstance()


    def attemptAttack(self, argument):
        if RNG_under_ten() >= 3:  # determines whether i hit the enemy
            self.enemy.attack(self.character, self.instance)


class LocationLeaveGameInstance(LocationBase):
    pass

class TopLevelLocation(LocationBase):
    def __init__(self, instance, character):
        super(TopLevelLocation, self).__init__(instance, character)

        gotoLeaveGame = lambda: instance.gotoInstance(LocationLeaveGameInstance(instance, character))
        self.actions.append(LocationBase.Action("Leave", LocationBase.Action.leave, ["leaving game"], [gotoLeaveGame], [""]))



class LocationForest(TopLevelLocation):
    synonims = ["forest", "f"]
    def __init__(self, instance, character, Action):
        LocationBase.Action = Action
        LocationBase.character = character
        super(LocationForest, self).__init__(instance, character)

        self.connectedAreas = [LocationDarkForest, LocationVillage]

        self.enemies.append("Goblins")
        self.levelRange = [1, 2]
        self.name = "Forest"
        self.description.append("It looks quiet but beware, there are monsters afoot.")

        self.entryMessages.append("You find yourself in a " + self.name + ".")
        self.entryMessages.append("You see nothing of interest around.")
        self.inputMessage = "what will you do in the " + self.name + "?"
        gotoCombat = lambda: instance.gotoInstance(LocationCombatInstance(instance, character))
        self.actions.append( Action( "Search", Action.search, [], [gotoCombat], [] ) )
        #gotoDarkForest = lambda: instance.gotoInstance(LocationDarkForest(instance, character))
        self.actions.append( Action( "go", LocationBase.Action.go, [], [instance.gotoHorizontalInstance], [""]))



class LocationDarkForest(TopLevelLocation):
    synonims = ["dark forest", "dark", "df"]
    def __init__(self, instance, character):
        super(LocationDarkForest, self).__init__(instance, character)

        self.enemies.append('dragons')
        self.enemies.append("fish")
        self.levelRange = [3, 4]
        self.name = "Dark Forest"
        self.description.append("A dark forest, the crowns of the trees are blocking out all light. You notice monsters marks.")

        self.connectedAreas = [LocationForest, LocationVillage]

        self.entryMessages.append("You find yourself in a " + self.name + ".")
        self.inputMessage = "what will you do in the " + self.name + "?"

        gotoCombat = lambda: instance.gotoInstance(LocationCombatInstance(instance, character))
        self.actions.append( LocationBase.Action("Search", LocationBase.Action.search, [], [gotoCombat], []))
        self.actions.append( LocationBase.Action("go", LocationBase.Action.go, [], [instance.gotoHorizontalInstance], [""]))


class LocationVillage(TopLevelLocation):
    synonims = ["village", "v"]

    def __init__(self, instance, character):
        super(LocationVillage, self).__init__(instance, character)

        self.name = "Starter Village"
        self.description.append("A Quiet village. There are not many people living here. You can resupply here and get your well earned rest.")

        self.connectedAreas = [LocationForest, LocationDarkForest]

        self.entryMessages.append("You entered the " + self.name + ".")
        self.inputMessage = "You wonder what you will do."

        self.actions.append( LocationBase.Action ("go", LocationBase.Action.go, [], [instance.gotoHorizontalInstance] , [] ) )
        lookFunction = lambda : instance.printMessages(self.description)
        self.actions.append( LocationBase.Action ("Look around", LocationBase.Action.look, [], [lookFunction], []))


class LocationShop(LocationBase):
    def __init__(self, instance, character):
        self.name = "Shop"
        self.description = "a rustic shop in a small village."

        self.entryMessages.append("You enter the shop.")
        self.inputMessage = "what will you do."

        lookFunction = lambda: instance.printMessages(self.description)
        self.actions.append( LocationBase.Action ("Leave", LocationBase.Action.leave, [], instance.leaveInstance))
        self.actions.append( LocationBase.Action ("Look around", LocationBase.Action.look, [], [lookFunction], [] ))



class Option:
    def __init__(self, percentage, action):
        self.percentage = percentage
        self.action = action

class BaseChance:
    def __init__(self):
        self.options = []


class EitherChance(BaseChance):
    def __init__(self, options, elseOption):
        for option in options:
            self.options.append(option)
        self.elseOption = elseOption


class AnyChance(BaseChance):
    pass

