from random import randint

from Action import Action
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
            Action(
                "Leave",
                Action.leave,
                ["leaving game"],
                [self.leave_game],
                [""])
        )

    def leave_game(self):
        game_choice = input(
            "Do you wish to leave the forrest behind and live a safe life from now on? (Yes/No)\n"
        )
        if game_choice in ['yes', 'y']:
            print('You Turn around start walking leaving this hellhole behind, \n'
                  'however, you can\'t help but look over your shoulder once more wondering what '
                  'would happen if you had stayed...')
            exit()
        elif game_choice in ['no', 'n']:
            print("You find new determination and head back to the forest!")