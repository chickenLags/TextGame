from locations.location_base import LocationBase


class LocationInventory(LocationBase):
    def __init__(self, instance, character):
        super(LocationInventory, self).__init__(instance, character)
        self.name = "inventory"
        self.loopEntryMessages = ["You have the following items in your inventory:",
                                  character.inventory.display]
        self.inputMessage = "You can leave or equip <item name>."
        self.actions.append( LocationBase.Action("leave", LocationBase.Action.leave, [], [instance.leaveInstance ], ["You left your inventory."]) )
        self.actions.append( LocationBase.Action("equip", LocationBase.Action.equip, [], [character.equip], [] ) )

        self.connectedAreas = []
