# from locations.location_base import TopLevelLocation, LocationBase
# from locations.location_dark_forest import LocationDarkForest
# from locations.location_forest import LocationForest

#
# class LocationVillage(TopLevelLocation):
#     synonims = ["village", "v"]
#
#     def __init__(self, instance, character):
#         super(LocationVillage, self).__init__(instance, character)
#
#         self.name = "Starter Village"
#         self.description.append("A Quiet village. There are not many people living here. You can resupply here and get your well earned rest.")
#
#         self.connectedAreas = [LocationForest, LocationDarkForest]
#
#         self.entryMessages.append("You entered the " + self.name + ".")
#         self.inputMessage = "You wonder what you will do."
#
#         self.actions.append( LocationBase.Action ("go", LocationBase.Action.go, [], [instance.gotoHorizontalInstance] , [] ) )
#         lookFunction = lambda : instance.printMessages(self.description)
#         self.actions.append( LocationBase.Action ("Look around", LocationBase.Action.look, [], [lookFunction], []))
#
