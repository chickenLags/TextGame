# from locations.location_base import TopLevelLocation, LocationBase
# from locations.location_combat import LocationCombatInstance
# from locations.location_dark_forest import LocationDarkForest
# from locations.location_village import LocationVillage
#
# class LocationForest(TopLevelLocation):
#     synonims = ["forest", "f"]
#     def __init__(self, instance, character, Action=False):
#         if Action:
#             LocationBase.Action = Action
#         LocationBase.character = character
#         super(LocationForest, self).__init__(instance, character)
#
#         self.connectedAreas = [LocationDarkForest, LocationVillage]
#
#         self.enemies.append("Goblins")
#         self.levelRange = [1, 2]
#         self.name = "Forest"
#         self.description.append("It looks quiet but beware, there are monsters afoot.")
#
#         self.entryMessages.append("You find yourself in a " + self.name + ".")
#         self.entryMessages.append("You see nothing of interest around.")
#         self.inputMessage = "what will you do in the " + self.name + "?"
#         gotoCombat = lambda: instance.gotoInstance(LocationCombatInstance(instance, character))
#         self.actions.append( LocationBase.Action( "Search", LocationBase.Action.search, [], [gotoCombat], [] ) )
#         self.actions.append( LocationBase.Action( "go", LocationBase.Action.go, [], [instance.gotoHorizontalInstance], [""]))
#
