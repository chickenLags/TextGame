from inspect import signature
from Location import TopLevelLocation, LocationBase, LocationInventory

class Action:

    leave = ["leave", "l", "exit", "escape"]
    inventory = ['inventory', 'inv', 'i']
    equip = ["equip", "e"]
    attack = ["attack", "atk", "a"]
    run = ['run', 'r']
    scan = ['scan', 'sc']
    search = ['search', "s"]
    stats = ['stats', 's']
    actions = ['actions', 'action', 'a', 'help', 'h']
    examine = ['examine', 'e']
    go = ["go", "enter", "goto"]
    look = ["look", "l", "examine", "e"]

    def __init__(self, name, synonims, entryMessages, computations, endMessages):
        self.name = name
        self.synonims = synonims
        self.entryMessages = entryMessages
        self.computations = computations
        self.endMessages = endMessages

    def compute(self, argument):
        for func in self.computations:
            if len( signature( func ).parameters ) == 1:        ## should take into account other parameters...
                func(argument)

            else:
                func()


class Instance:
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
        self.baseActions.append(Action("Stats", Action.stats, [], [character.displayStats], []))
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
            temp = []
            for location in self.getCurrentInstance().connectedAreas:
                temp.append(location.__name__[8:])

            print(str(temp) + "\n")
