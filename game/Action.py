

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


    def actionEntryMessage(self):
        for message in self.entryMessages:
            print(message)

    def actions(self):
        for func in self.computations:
            func()

    def actionEndMessage(self):
        for message in endMessages:
            print(message)