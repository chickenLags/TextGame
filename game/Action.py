from inspect import signature

class Action:

    leave = ["leave", "l", "exit", "escape"]
    Inventory = ['inventory', 'inv', 'i']
    equip = ["equip", "e"]
    attack = ["attack", "atk", "a"]
    run = ['run', 'r']
    scan = ['scan', 's']


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
    def __init__(self):
        self.entryMessages = []
        self.loopEntryMessages = []
        self.inputMessage = ""
        self.loopEndMessages = []
        self.elseMessages = []
        self.running = True
        self.playing = True

    def containsAction(self, action):
        for a in self.actions:
            if action in a.synonims:
                return a

    def printMessages(self, parameters):
        for p in parameters:
            if hasattr(p, '__call__'):      ### If parameter required then it will be added. no logical situation
                print( str( p() ) )         ### for another argument than given parameter.
            else:
                print( str( p ) )

    def inputMessage(self):
        return self.inputMessage

    def leaveGame(self):
        self.entryMessages = []
        self.loopEntryMessages = []
        self.inputMessage = ""
        self.loopEndMessages = []
        self.elseMessages = []
        self.running = False
        self.playing = False

    def gotoInstance(self, other):
        self.addEntryMessages(other.entryMessages)
        self.addLoopEntryMessages(other.loopEntryMessages)
        self.addInputMessage(other.inputMessage)
        self.addActions(other.actions)
        self.addLoopEndMessages(other.loopEndMessages)
        self.addElseMessages(other.elseMessages)

    def addEntryMessages(self, entryMessages):
        self.entryMessages = entryMessages

    def addLoopEntryMessages(self, loopEntryMessages):
        self.loopEntryMessages = loopEntryMessages

    def addInputMessage(self, inputMessage):
        self.inputMessage = inputMessage

    def addActions(self, actions):
        self.actions = actions

    def addLoopEndMessages(self, loopEndMessages):
        self.loopEndMessages = loopEndMessages

    def addElseMessages(self, elseMessages):
        self.elseMessages = elseMessages