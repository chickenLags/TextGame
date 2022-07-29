
from Enemy import Enemy
#from Action import Action
import random

from locations.location_base import LocationBase, TopLevelLocation
from locations.location_combat import LocationCombatInstance
# from locations.location_dark_forest import LocationDarkForest
# from locations.location_forest import LocationForest
# from locations.location_village import LocationVillage


class World:
    def __init__(self):
        self.states = []

class State:
    def __init__(self):
        self.provinces = []


class Province:
    def __init__(self):
        self.areas = []

class Area:
    def __init__(self):
        self.locations = []

# world = World()
# state = State()
# province = Province()
# area = Area()
#
# world.states.append(state)
# state.provinces.append(province)
# province.areas.append(area)
# area.locations = [
#     LocationForest,
#     LocationDarkForest,
#     LocationVillage
# ]


class LocationForest(TopLevelLocation):
    synonims = ["forest", "f"]
    def __init__(self, instance, character, Action=False):
        if Action:
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
        self.actions.append( LocationBase.Action( "Search", LocationBase.Action.search, [], [gotoCombat], [] ) )
        self.actions.append( LocationBase.Action( "go", LocationBase.Action.go, [], [instance.gotoHorizontalInstance], [""]))




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




# class Location:
#     name = "Dark Forest"
#
#     # properties of location:
#     # name, what monsters, level range
#     # option for future additions.
#
#     properties = {"Default":
#                       {"monstertypes":["Goblins", "Ogres", "Dragons"],
#                        "levelRange": [1, 100]},
#                   "Forest":
#                       {"monstertypes": ["Goblins"],
#                        "levelRange": [10, 20]},
#                   "Dark Forest":
#                       {"monstertypes": ["Goblins"],
#                        "levelRange": [1, 2]}
#                   }
#
#     def getMonster(self, random):
#         monsterType = self.properties[self.name]['monstertypes'][random.randrange(0, len(self.properties[self.name]["monstertypes"]))]
#         return monsterType
#
#     def getLevelRange(self):
#         return self.properties[self.name]["levelRange"]


# name, synonims, entryMessages, computations, endMessages


# class Option:
#     def __init__(self, percentage, action):
#         self.percentage = percentage
#         self.action = action
#
# class BaseChance:
#     def __init__(self):
#         self.options = []
#
#
# class EitherChance(BaseChance):
#     def __init__(self, options, elseOption):
#         for option in options:
#             self.options.append(option)
#         self.elseOption = elseOption
#
#
# class AnyChance(BaseChance):
#     pass

