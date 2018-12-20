from Action import Action

class Location:
    name = "Dark Forest"

    # properties of location:
    # name, what monsters, level range
    # option for future additions.

    properties = {"Default":
                      {"monstertypes":["Goblins", "Ogres", "Dragons"],
                       "levelRange": [1, 100]},
                  "Forest":
                      {"monstertypes": ["Goblins"],
                       "levelRange": [10, 20]},
                  "Dark Forest":
                      {"monstertypes": ["Goblins"],
                       "levelRange": [1, 2]}
                  }

    def getMonster(self, random):
        monsterType = self.properties[self.name]['monstertypes'][random.randrange(0, len(self.properties[self.name]["monstertypes"]))]
        return monsterType

    def getLevelRange(self):
        return self.properties[self.name]["levelRange"]



class locationInventory:
    def __init__(self, instance, character):
        self.entryMessages = []
        self.loopEntryMessages = ["You have the following items in your inventory:",
                                  character.inventory.getInventoryAsList]
        self.inputMessage = "You can leave or equip <item name>."
        self.actions = [Action("leave", Action.leave, [],
                               [instance.leaveGame ],
                               ["You left your inventory."]),
                        Action("equip", Action.equip, [],
                               [character.equip],
                               [])]
        self.loopEndMessages = []
        self.elseMessages = []