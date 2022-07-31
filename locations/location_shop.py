from locations.location_base import LocationBase


class LocationShop(LocationBase):
    def __init__(self, instance, character):
        self.name = "Shop"
        self.description = "a rustic shop in a small village."

        self.entryMessages.append("You enter the shop.")
        self.inputMessage = "what will you do."

        lookFunction = lambda: instance.printMessages(self.description)
        self.actions.append( LocationBase.Action ("Leave", LocationBase.Action.leave, [], instance.leaveInstance))
        self.actions.append( LocationBase.Action ("Look around", LocationBase.Action.look, [], [lookFunction], [] ))

