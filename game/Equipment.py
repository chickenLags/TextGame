from Items import *


class Equipment:

    def __init__(self, itemManager):

        self.weapon     = None
        self.shield     = None
        self.head       = None
        self.body       = None
        self.legs       = None
        self.hands      = None

    def _equipPop(self, equipment, silent=False):
        dequiped = None
        if equipment.equipType.itemType == itemType.WEAPON:
            dequiped = self.weapon
            self.weapon = equipment
        elif equipment.equipType.itemType == itemType.SHIELD:
            dequiped = self.shield
            self.shield = equipment
        elif equipment.equipType.itemType == itemType.HEAD:
            dequiped = self.head
            self.head = equipment
        elif equipment.equipType.itemType == itemType.BODY:
            dequiped = self.body
            self.body = equipment
        elif equipment.equipType.itemType == itemType.LEGS:
            dequiped = self.legs
            self.legs = equipment
        elif equipment.equipType.itemType == itemType.HANDS:
            dequiped = self.hands
            self.hands = equipment
        else:
            print("Item to be equiped does not fit any slot. name: " + equipment.name)
            return equipment
        if not silent:
            print("Equiped the " + equipment.name.lower() + "!")
        return dequiped

    def erode(self, itemType):
        if itemType == itemType.WEAPON and self.weapon:
            self.weapon.durability -= 1
            if self.weapon.durability <=0:
                self.weapon = None
        elif itemType == itemType.SHIELD and self.shield:
            self.shield.durability -= 1
            if self.shield.durability <= 0:
                self.shield = None
        elif itemType == itemType.HEAD and self.head:
            self.head.durability -= 1
            if self.head.durability <= 0:
                self.head = None
        elif itemType == itemType.BODY and self.body:
            self.body.durability -= 1
            if self.body.durability <= 0:
                self.body = None
        elif itemType == itemType.LEGS and self.legs:
            self.legs.durability -= 1
            if self.legs.durability <= 0:
                self.legs = None
        elif itemType == itemType.HANDS and self.hands:
            self.hands.durability -= 1
            if self.hands.durability <= 0:
                self.hands = None

    def getName(self, itemType):
        if itemType == itemType.WEAPON:
            if self.weapon:
                return self.weapon.name
            else:
                return "Fist"
        elif itemType == itemType.SHIELD:
            if self.shield:
                return self.shield.name
        elif itemType == itemType.HEAD:
            if self.head:
                return self.head.name
        elif itemType == itemType.BODY:
            if self.body:
                return self.body.name
        elif itemType == itemType.LEGS:
            if self.legs:
                return self.legs.name
        elif itemType == itemType.HANDS:
            if self.hands:
                return self.hands.name

        return "None"

class EmptySlot:
    name = "None"