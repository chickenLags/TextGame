from Items import Equipable, Item

class Inventory:

    def __init__(self):
        self.inventory = []

    def getInventoryAsList(self):
        temp = []
        for item in self.inventory:
            temp.append(item.name);
        return temp

    def canEquip(self, itemName):
        for item in self.inventory:
            if (item.name == itemName or item.name.lower() == itemName ) and isinstance(item, Equipable):
                return True
        return False

    def add(self, item):
        if isinstance(item, Item):
            print("item is indeed instance of Item: " + item.name)
            self.inventory.append(item)
            print("Put the " + item.name.lower() + " in inventory.")

    def popItem(self, itemName):
        value = None
        for item in self.inventory:
            if item.name == itemName or item == itemName or item.name.lower() == itemName:
                value = self.inventory.pop(self.inventory.index(item))

        return value

