from random import randint

from exceptions.action_exception import ActionException


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
        action = [a for a in self.actions if action in a.synonims]

        if not action:
            raise ActionException()

        return action[0]

    def RNG_under_ten(self, lower_value: int = 1, higher_value: int = 10):
        return randint(lower_value, higher_value)


class TopLevelLocation(LocationBase):
    def __init__(self, instance, character):
        super(TopLevelLocation, self).__init__(instance, character)

        self.actions.append(
            LocationBase.Action(
                "Leave", LocationBase.Action.leave, ["leaving game"],
                [exit], [""])
        )

