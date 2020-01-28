import random
import sqlite3
from enum import Enum

'''
class potions:
    def Type:
'''
import random

class ItemType(Enum):
        WEAPON  = 1
        SHIELD  = 2
        HANDS   = 3
        LEGS    = 4
        BODY    = 5
        HEAD    = 6
        OFFHAND = 7

class Material:

    def __init__(self, name, DMG, DEF, DUR):
        self.name = name



        self.damage = DMG
        self.defence = DEF
        self.durability = DUR


class EquipType:
    type = ItemType

    def __init__(self, name, itemType, DEFDMG, dur):
        self.name = name
        self.itemType = itemType
        self.defDmg = DEFDMG
        self.durability = dur




class ItemManager:
    weaponTypes         = []
    shieldTypes         = []
    armourTypes         = []
    armourMaterials     = []
    materials           = []

    def __init__(self):
#         self.materials.append(Material("Rusty",            DMG=1, DEF=2, DUR=2))
#         self.materials.append(Material("Bronze",           DMG=1, DEF=2, DUR=2 ))
#         self.materials.append(Material("Iron",             DMG=3, DEF=4, DUR=3 ))
#         self.materials.append(Material("Silver",           DMG=5, DEF=2, DUR=1 ))
#         self.materials.append(Material("Mythril",          DMG=3, DEF=5, DUR=3 ))
#         self.materials.append(Material("Mysterious alloy", DMG=5, DEF=6, DUR=2 ))
#         self.materials.append(Material("Dragon scales",    DMG=4, DEF=7, DUR=4 ))

#         self.armourMaterials.append(Material("Leather",    DMG=0, DEF=1, DUR=15))

        self.armourTypes.append(EquipType("Gauntlets", EquipType.type.HANDS, DEFDMG=1, dur=5))
        self.armourTypes.append(EquipType("Leggings", EquipType.type.LEGS, DEFDMG=3, dur=7))
        self.armourTypes.append(EquipType("Armour", EquipType.type.BODY, DEFDMG=5, dur=5))
        self.armourTypes.append(EquipType("Helmet", EquipType.type.HEAD, DEFDMG=7, dur=3))

        self.shieldTypes.append(EquipType("Shield", EquipType.type.SHIELD, DEFDMG=1, dur=10))

        self.weaponTypes.append(EquipType("Dagger", EquipType.type.WEAPON, DEFDMG=1, dur=5))
        self.weaponTypes.append(EquipType("Mace", EquipType.type.WEAPON, DEFDMG=3, dur=7))
        self.weaponTypes.append(EquipType("Sword", EquipType.type.WEAPON, DEFDMG=5, dur=5))
        self.weaponTypes.append(EquipType("Great Sword", EquipType.type.WEAPON, DEFDMG=7, dur=3))

    def getMaterial(self, materialName):
        for mat in self.materials:
            if mat.name == materialName:
                return mat
        for mat in self.armourMaterials:
            if mat.name == materialName:
                return mat
        return False

    def getWeaponType(self, weaponTypeName):
        for weaponType in self.weaponTypes:
            if weaponType.name == weaponTypeName:
                return weaponType
        return False

    def getArmourType(self, armourTypeName):
        for armourType in self.armourTypes:
            if armourType.name == armourTypeName:
                return armourType
        return False

    def getShieldType(self, shieldTypeName):
        for shieldType in self.shieldTypes:
            if shieldType.name == shieldTypeName:
                return shieldType
        return False

    def _generateMaterial(self, defensive = False):
        materialList = []
        for mat in self.materials:
            materialList.append(mat)
        if defensive:
            for mat in self.armourMaterials:
                materialList.append(mat)
        return materialList[random.randint(0, len(materialList) - 1)]

    def _generateWeaponType(self):
        return self.weaponTypes[random.randint(0, len(self.weaponTypes) - 1)]

    def _getShieldType(self):
        return self.shieldTypes[random.randint(0, len(self.shieldTypes) - 1)]

    def _generateArmour(self):
        return self.armourTypes[random.randint(0, len(self.armourTypes) - 1)]

    def generateWeapon(self):
        weaponType = self._generateWeaponType()
        material = self._generateMaterial()
        drop = Weapon(material, weaponType)
        print("you obtained " + drop.name + "!")
        return drop

    def generateShield(self):
        shieldType = self._getShieldType()
        material = self._generateMaterial(True)
        drop = Shield(material, shieldType)
        print("You obtained a " + drop.name + "!")
        return shield

    def generateArmour(self):
        armourType = self._generateArmour()
        material = self._generateMaterial(True)
        drop = Armour(material, armourType)
        print("You obtained a " + drop.name + "!")



class Item:
    def __init__(self, name):
        pass

class Equipable(Item):
    def __init__(self, material, equipType):
        self.name = material.name + " " + equipType.name.lower()
        self.material = material
        self.equipType = equipType
        self.durability = self.material.durability + self.equipType.durability

class DefensiveGear(Equipable):
    def getDefence(self):
        return self.material.defence + self.equipType.defDmg

class Armour(DefensiveGear):
    def __init__(self, material, equipType):
        super(Armour, self).__init__(material, equipType)

class Shield(DefensiveGear):
    def __init__(self, material, equipType):
        super(Shield, self).__init__(material, equipType)

class Weapon(Equipable):
    def __init__(self, material, equipType):
        super(Weapon, self).__init__(material, equipType)

    def getDamage(self):
        return self.equipType.defDmg + self.material.damage

    def erode(self):
        self.durability -= 1

