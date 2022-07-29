# from locations.location_base import TopLevelLocation, LocationBase
# from locations.location_combat import LocationCombatInstance
# from locations.location_forest import LocationForest
# from locations.location_village import LocationVillage

#
# class LocationDarkForest(TopLevelLocation):
#     synonims = ["dark forest", "dark", "df"]
#     def __init__(self, instance, character):
#         super(LocationDarkForest, self).__init__(instance, character)
#
#         self.enemies.append('dragons')
#         self.enemies.append("fish")
#         self.levelRange = [3, 4]
#         self.name = "Dark Forest"
#         self.description.append("A dark forest, the crowns of the trees are blocking out all light. You notice monsters marks.")
#
#         self.connectedAreas = [LocationForest, LocationVillage]
#
#         self.entryMessages.append("You find yourself in a " + self.name + ".")
#         self.inputMessage = "what will you do in the " + self.name + "?"
#
#         gotoCombat = lambda: instance.gotoInstance(LocationCombatInstance(instance, character))
#         self.actions.append( LocationBase.Action("Search", LocationBase.Action.search, [], [gotoCombat], []))
#         self.actions.append( LocationBase.Action("go", LocationBase.Action.go, [], [instance.gotoHorizontalInstance], [""]))
#
