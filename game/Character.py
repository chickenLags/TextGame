import random
from Inventory import Inventory
from Equipment import Equipment
from Items import itemType



class Character:
    def __init__(self, itemManager):
        self.stats = {"level": 1,  "title": "Wanderer",  "strength": 1,  "experience": 0, "hp": 20}
        self.inventory = Inventory()
        self.equipment = Equipment(itemManager)

    def _forceEquip(self, equipment, silent=False):
        self.equipment._equipPop(equipment, silent)

    def equip(self, equipmentName):
        if not self.inventory.canEquip(equipmentName):
            print ("can't equip this item")
        else:
            self.inventory.add( self.equipment._equipPop( self.inventory.popItem( equipmentName ) ) )


    def getInventoryAsList(self):
        return self.inventory.getInventoryAsList()

    def getDamage(self):
        if self.equipment.weapon:
            return self.stats['strength'] + self.equipment.weapon.getDamage()
        return self.stats['strength']

    def weaponErosion(self):
        self.equipment.erode(itemType.WEAPON)



    def maxExperience(self):
        tempExpCap = self.stats["level"]
        expTillNextLevel = tempExpCap * tempExpCap + 20
        return expTillNextLevel

    def attack(self, enemy):
        self.stats["hp"] -= enemy.getDamage()
        if not self.isAlive():
            print(enemy.getDeathMessage())
            self.die()

    def isAlive(self):
        if self.stats["hp"] <= 0:
            return False
        return True

    def die(self):
        print("\"if only I had not entered this wretched forest\" Regret fills your mind as the light leaves your eyes")
        potato = input("You are dead!")
        quit()


    def experience_gain(self, expReceived):
        totalExp = self.stats["experience"] + expReceived
        expLeft = True

        while expLeft:
            expTillNextLevel = self.maxExperience()
            if totalExp < expTillNextLevel:
                self.stats["experience"] += expReceived
                print("(" + str(expReceived) + " EXP obtained)")
                expLeft = False
            else:
                print("You feel stronger, what a great feeling! And you feel completely Restored!!")
                self.stats["experience"] = 0
                self.stats["level"] += 1
                self.stats["strength"] += random.randrange(1, 3)
                self.stats["hp"] += 10 * self.stats["level"]
                totalExp = expReceived - expTillNextLevel

    def displayStats(self):
        print("======= Current Stats =======")
        for key in self.stats:
            print(" \t" + key + ": " + str(self.stats[key]))

        print("\n======= Equipment =======")
        print("\tWeapon:  " + str(self.equipment.getName(itemType.WEAPON)) )
        print("\tShield:  " + str(self.equipment.getName(itemType.SHIELD)))
        print("\tHead  :  " + str(self.equipment.getName(itemType.HEAD)))
        print("\tBody  :  " + str(self.equipment.getName(itemType.BODY)))
        print("\tHands :  " + str(self.equipment.getName(itemType.HANDS)))
        print("\tLegs  :  " + str(self.equipment.getName(itemType.LEGS)) + "\n")