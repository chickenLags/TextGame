import random

'''
class potions:
    def Type:
'''
import random

class ItemManager:

    weaponry = {"Dagger": {"DMG": 1,"dur": 5},
                "Mace": {"DMG": 3, "dur": 7} ,
                "Shield": {"DMG": 0, "dur": 10},
                "Sword": {"DMG": 5,"dur": 5},
                "Great Sword": {"DMG": 7, "dur": 3}}

    material = {"Rusty": {"DMG": 1,"dur": 1} ,
                "Bronze": {"DMG": 1,"dur": 2} ,
                "Iron": {"DMG": 3,"dur": 3} ,
                "Silver": {"DMG": 5,"dur": 1} ,
                "Mythril": {"DMG": 3,"dur": 3} ,
                "Mysterious alloy": {"DMG": 5,"dur": 2},
                "Dragon scales": {"DMG": 4,"dur": 4}}

    def __init__(self):
        pass



    def getWeaponType(self):
        weaponList = []
        list(self.weaponry.keys())
        for key in self.weaponry.keys():
            weaponList.append(key)

        weaponType = str(weaponList[random.randint(0, len(self.weaponry) - 1)])
        return weaponType

    def getMaterialType(self):
        materialList = []
        list(self.material.keys())
        for key in self.material.keys():
            materialList.append(key)

        weaponMaterial = str(materialList[random.randint(0, len(self.material) - 1 )])
        return weaponMaterial

    def getWeaponName(self, weaponType, materialType):
        newWeaponName = str(materialType) + " " + str(weaponType)
        return newWeaponName

    def generateWeapon(self):
        weaponType = self.getWeaponType()
        materialType = self.getMaterialType()
        newWeaponName = materialType + weaponType

        drop = Weapon(newWeaponName, weaponType, materialType)
        print("you obtained " + drop.name)
        return drop



class Item:

    def __init__(self, name):
        self.name = name;

class Weapon(Item):
    weaponry = {"Dagger": {"DMG": 1, "dur": 5},     "Mace": {"DMG": 3, "dur": 7},
                "Shield": {"DMG": 0, "dur": 10},    "Sword": {"DMG": 5, "dur": 5},
                "Great Sword": {"DMG": 7, "dur": 3}}

    material = {"Rusty": {"DMG": 1, "dur": 1},      "Bronze": {"DMG": 1, "dur": 2},
                "Iron": {"DMG": 3, "dur": 3},       "Silver": {"DMG": 5, "dur": 1},
                "Mythril": {"DMG": 3, "dur": 3},    "Mysterious alloy": {"DMG": 5, "dur": 2},
                "Dragon scales": {"DMG": 4, "dur": 4}}

    def __init__(self, name, weaponType, materialType):
        self.name = name
        self.weaponType = weaponType
        self.materialType = materialType

            # determine durability
        self.durability = self.material[self.materialType]["dur"] + self.weaponry[self.weaponType]['dur']


    def getDamage(self):
        weaponDMG = self.weaponry[self.weaponType]["DMG"]
        materialDMG = self.material[self.materialType]["DMG"]
        return weaponDMG + materialDMG

    def erode(self):
        self.durability -= 1;
