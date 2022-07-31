from Action import Action
from exceptions.game_exception import GameException
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
        self.baseActions.append(Action("Actions", Action.actions, ["==== available actions ====:"], [self.displayActions, self.gotoHorizontalInstance], []))
        self.baseActions.append(Action("DisplayInstanceTrree", ["DisplayInstanceThree", "d"], ["==== available something ====:"], [self.displayInstances], []))
        self.baseActions.append(Action("Stats", Action.stats, [], [character.display_stats], []))
        self.baseActions.append(Action("Inventory", Action.inventory, [], [gotoInventory], [""]))
        self.baseActions.append(Action("Look around", Action.look, [], [lookFunction], []))

    def displayInstances(self):
        for i in self.instances:
            print(i.name)

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

    def printMessages(self, parameters):    ## should check whether parameter exist.
        for p in parameters:
            if hasattr(p, '__call__'):      ### If parameter required then it will be added. no logical situation
                print( str( p() ) )         ### for another argument than given parameter.
            else:
                print( str( p ) )

    def inputMessage(self):
        return self.inputMessage

    def leaveGame(self):
        self.running = False
        self.playing = False

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

    def getBaseActions(self, action):
        for a in self.baseActions:
            if action in a.synonims:
                return a
        return False

    def gotoHorizontalInstance(self, argument):
        if argument:
            for c in self.getCurrentInstance().connectedAreas:
                if argument in c.synonims:
                    self.gotoInstance(c(self, LocationBase.character))
        else:
            print("\n==== Bordering Area's ====:")
            [print(str(loc.__name__[8:])) for loc in self.getCurrentInstance().connectedAreas]

    def getAction(self, string):
        command = input(string + "\n\n => ")
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
                    self.printMessages(self.getCurrentInstance().loopEntryMessages)
                    action, argument = self.getAction(self.getCurrentInstance().inputMessage)
                    if self.getCurrentInstance().containsAction(action):
                        retrievedAction = self.getCurrentInstance().containsAction(action)
                        self.printMessages(retrievedAction.entryMessages)
                        retrievedAction.compute(argument)
                        self.printMessages(retrievedAction.endMessages)
                        self.printMessages(self.getCurrentInstance().loopEndMessages)
                    elif self.getBaseActions(action):
                        retrievedAction = self.getBaseActions(action)
                        self.printMessages(retrievedAction.entryMessages)
                        retrievedAction.compute(argument)
                        self.printMessages(retrievedAction.endMessages)
                        self.printMessages(self.getCurrentInstance().loopEndMessages)
                    else:
                        self.printMessages(self.getCurrentInstance().elseMessages)
                except GameException as e:
                    print(f"[ALERT] {e.message}\n")

