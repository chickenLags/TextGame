from inspect import signature


class Action:
    leave = ["leave", "exit", "escape"]
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
        # @Todo
        # an argument at this point can contain more spaces. originally "go village potato" would
        # become here "village potato". perhaps a "attack enemy1 fire" or other combinations
        # would be cool to catch? perhaps recursive actions are possible? allowing for complex
        # commands to be given?
        for func in self.computations:
            if len( signature( func ).parameters ) == 1:  # should take into account other
                # parameters...
                func(argument)

            else:
                func()


