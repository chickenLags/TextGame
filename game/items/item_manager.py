import string
from random import random, randint
from typing import List

from items.Item import Weapon
from items.armour import Armour
from items.equip_type import EquipType
from items.material import Material
from items.shield import Shield


class ItemManager:
    weaponTypes         = []
    shieldTypes         = []
    armourTypes         = []
    armourMaterials     = []
    materials           = []

    def __init__(self):
        self.materials.append(Material("Rusty",            DMG=1, DEF=2, DUR=2))
        self.materials.append(Material("Bronze",           DMG=1, DEF=2, DUR=2 ))
        self.materials.append(Material("Iron",             DMG=3, DEF=4, DUR=3 ))
        self.materials.append(Material("Silver",           DMG=5, DEF=2, DUR=1 ))
        self.materials.append(Material("Mythril",          DMG=3, DEF=5, DUR=3 ))
        self.materials.append(Material("Mysterious alloy", DMG=5, DEF=6, DUR=2 ))
        self.materials.append(Material("Dragon scales",    DMG=4, DEF=7, DUR=4 ))

        self.armourMaterials.append(Material("Leather",    DMG=0, DEF=1, DUR=15))

        self.armourTypes.append(EquipType("Gauntlets", EquipType.type.HANDS, DEFDMG=1, dur=5))
        self.armourTypes.append(EquipType("Leggings", EquipType.type.LEGS, DEFDMG=3, dur=7))
        self.armourTypes.append(EquipType("Armour", EquipType.type.BODY, DEFDMG=5, dur=5))
        self.armourTypes.append(EquipType("Helmet", EquipType.type.HEAD, DEFDMG=7, dur=3))

        self.shieldTypes.append(EquipType("Shield", EquipType.type.SHIELD, DEFDMG=1, dur=10))

        self.weaponTypes.append(EquipType("Dagger", EquipType.type.WEAPON, DEFDMG=1, dur=5))
        self.weaponTypes.append(EquipType("Mace", EquipType.type.WEAPON, DEFDMG=3, dur=7))
        self.weaponTypes.append(EquipType("Sword", EquipType.type.WEAPON, DEFDMG=5, dur=5))
        self.weaponTypes.append(EquipType("Great Sword", EquipType.type.WEAPON, DEFDMG=7, dur=3))

    def get_material(self, material_name: string):
        for mat in self.materials:
            if mat.name == material_name:
                return mat
        for mat in self.armourMaterials:
            if mat.name == material_name:
                return mat
        return False

    def get_weapon_type(self, weapon_type_name: string):
        return [weapon_type for weapon_type in self.weaponTypes if weapon_type.name == weapon_type_name][0]

    def get_armour_type(self, armour_type_name: string):
        return [armour for armour in self.armourTypes if armour.name == armour_type_name][0]

    def get_shield_type(self, shield_type_name: string):
        return [shield for shield in self.shieldTypes if shield.name == shield_type_name][0]

    def _generate_material(self, defensive = False):
        materialList = []
        for mat in self.materials:
            materialList.append(mat)
        if defensive:
            for mat in self.armourMaterials:
                materialList.append(mat)
        return materialList[randint(0, len(materialList) - 1)]

    def _generate_weapon_type(self):
        return self.weaponTypes[randint(0, len(self.weaponTypes) - 1)]

    def _get_shield_type(self):
        return self.shieldTypes[randint(0, len(self.shieldTypes) - 1)]

    def _generate_armour(self):
        return self.armourTypes[randint(0, len(self.armourTypes) - 1)]

    def generateWeapon(self):
        weaponType = self._generate_weapon_type()
        material = self._generate_material()
        drop = Weapon(material, weaponType)
        print("you obtained " + drop.get_name() + "!")
        return drop

    def generateShield(self):
        shieldType = self._get_shield_type()
        material = self._generate_material(True)
        drop = Shield(material, shieldType)
        print("You obtained a " + drop.get_name() + "!")
        return drop

    def generateArmour(self):
        armourType = self._generate_armour()
        material = self._generate_material(True)
        drop = Armour(material, armourType)
        print("You obtained a " + drop.get_name() + "!")
        return drop
