import random

'''
class potions:
    def Type:
'''
import random

class weapons:

    weaponry = {"Dagger": {"DMG": 1,"dur": 5} ,"Mace": {"DMG": 3, "dur": 7} ,"Shield": {"DMG": 0, "dur": 10}, "Sword": {"DMG": 5,"dur": 5},"Great Sword": {"DMG": 7, "dur": 3}}

    material = {"Rusty": {"DMG": 1,"dur": 1} ,"Bronze": {"DMG": 1,"dur": 2} ,"Iron": {"DMG": 3,"dur": 3} ,"Silver": {"DMG": 5,"dur": 1} ,"Mythril": {"DMG": 3,"dur": 3} ,"Mysterious alloy": {"DMG": 5,"dur": 2} ,"Dragon scales": {"DMG": 4,"dur": 4}}

#    action = input()



#weapoon name = [1] weapon dmg = [number[2]] weapon durability = [number[3]]

    #Random Number Generator weaponry
    def RNG_weaponry(self):
        higher_value = len(weapons.weaponry) -1
        print(higher_value)
        weapon_value =random.randint(0, higher_value)
        return weapon_value

    #Random Number Generator material
    def RNG_material(self):
        higher_value = len(weapons.material) -1
        material_value =random.randint(0, higher_value)
        return material_value


    def getWeaponType(self):
        weaponList = []
        list(weapons.weaponry.keys())
        for key in weapons.weaponry.keys():
            weaponList.append(key)

        weaponType = str(weaponList[weapons.RNG_weaponry(weapons)])
        return weaponType

    def getMaterialType(self):
        materialList = []

        list(weapons.material.keys())
        for key in weapons.material.keys():
            materialList.append(key)
        weaponmaterial = str(materialList[weapons.RNG_material(weapons)])
        return weaponmaterial

    def getWeaponName(self, weaponType, materialType):
        newWeaponName = str(materialType) + " " + str(weaponType)
        return newWeaponName

    def getWeaponDurability(self, weaponType, materialType):
        weaponDurability = weapons.weaponry[weaponType]["dur"]
        materialDurability = weapons.material[materialType]["dur"]
        newWeaponDurability = weaponDurability + materialDurability
        return newWeaponDurability

    def getWeaponDMG(self, weaponType, materialType):
        weaponDMG = weapons.weaponry[weaponType]["DMG"]
        materialDMG = weapons.material[materialType]["DMG"]
        newWeaponDMG = weaponDMG + materialDMG
        return newWeaponDMG

    def WeaponDrops(self):
        # wapen return in vorm van {"Rusty Dagger": [DMG, current durability, max durability]}
        # eerst moeten we de weapontype claimen en de materialtype
        weaponType = weapons.getWeaponType(weapons)
        materialType = weapons.getMaterialType(weapons)

        #nu moeten we beide Type's hebben om de gegevends van het nieuwe wapen te krijgen
        newWeaponName = weapons.getWeaponName(weapons, weaponType, materialType)
        newWeaponDurability = weapons.getWeaponDurability(weapons, weaponType, materialType)
        newWeaponDMG = weapons.getWeaponDMG(weapons, weaponType, materialType)

        drop = [newWeaponName, newWeaponDMG, newWeaponDurability, newWeaponDurability]




        print("you obtained " + drop[0])
        return drop
