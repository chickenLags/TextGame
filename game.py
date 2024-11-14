from Action import Action
from Table import Table
from exceptions.action_exception import ActionException
from exceptions.game_exception import GameException, SilentException
from exceptions.not_found_exceptions import AreaNotFoundException
from locations.location_base import LocationBase, TopLevelLocation
from locations.location_inventory import LocationInventory


class Game:
    def __init__(self, itemManager, character):
        self.running = True
        self.playing = True
        self.character = character
        self.instances = []
        self.itemManager = itemManager
        self.baseActions = []

        lookFunction = lambda: self.printMessages(self.getCurrentInstance().description)
        gotoInventory = lambda: self.gotoInstance(LocationInventory(self, character))
        self.baseActions.append(Action(
            "Actions", Action.actions, ["==== available actions ====:"],
            [self.displayActions, self.gotoHorizontalInstance], [])
        )
        self.baseActions.append(Action(
            "Display instance stack", ["display", "stack", "d"],
            ["==== available instances ====:"], [self.displayInstances],
            [])
        )
        self.baseActions.append(Action("Stats", Action.stats, [], [character.display_stats], []))
        self.baseActions.append(Action("Inventory", Action.inventory, [], [gotoInventory], [""]))
        self.baseActions.append(Action("Look around", Action.look, [], [lookFunction], []))

    def displayInstances(self):
        Table([[i.name] for i in self.instances]).print()

    def displayActions(self):
        actionNames = []
        for action in self.getCurrentInstance().actions:
            actionNames.append(action.name)
        for action in self.baseActions:
            actionNames.append(action.name)
        print(str(actionNames))


    def getCurrentInstance(self):
        return self.instances[-1]

    def getParentInstance(self):
        return self.instances[-1]

    def printMessages(self, parameters):
        for p in parameters:
            if hasattr(p, '__call__'):
                print( str( p() ) )
            else:
                print( str( p ) )

    def inputMessage(self):
        return self.inputMessage

    def leaveInstance(self):
        self.instances.pop()
        self.running = False
        if not len(self.instances):
            quit()

    def gotoInstance(self, other):
        self.running = False
        if isinstance(other, TopLevelLocation) and len(self.instances) > 0:
            self.instances.pop()
        self.instances.append(other)

    def find_action(self, search):
        actions = self.getCurrentInstance().actions + self.baseActions
        action = [a for a in actions if search in a.synonims]

        if not action: raise ActionException()

        return action[0]

    def connected_areas(self):
        return self.getCurrentInstance().connectedAreas

    def gotoHorizontalInstance(self, argument):
        if not argument:
            # would be cool to have a description next to the name, but it is not yet initialized.
            areas = [[l.__name__[8:]] for l in self.connected_areas()]
            return Table(areas, "\nBordering Area's").print()

        area = [area for area in self.connected_areas() if argument in area.synonims]

        if not area: raise AreaNotFoundException()

        self.gotoInstance(area[0](self, LocationBase.character))

    def get_user_input(self, string):
        command = input(string + "\n\n    => ")
        print("")
        if command.count(" ") > 0:
            action, argument = command.split(" ", 1)
            return action, argument

        else:
            return command, ""

    def start(self):
        while self.playing:
            self.running = True
            self.printMessages(self.getCurrentInstance().entryMessages)

            while self.running:
                try:
                    self.execute_action()
                except GameException as e:
                    print(f"[ALERT] {e.message}\n")
                except SilentException as e:
                    pass

    def execute_action(self):
        self.printMessages(self.getCurrentInstance().loopEntryMessages)

        search_action, argument = self.get_user_input(self.getCurrentInstance().inputMessage)
        action = self.find_action(search_action)

        if not action:
            return self.printMessages(self.getCurrentInstance().elseMessages)

        self.printMessages(action.entryMessages)
        action.compute(argument)
        self.printMessages(action.endMessages)
        self.printMessages(self.getCurrentInstance().loopEndMessages)