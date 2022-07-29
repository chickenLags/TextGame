import random
import string

from Enemy import Enemy
from Inventory import Inventory
from Equipment import Equipment
from items.Item import EquipType, Equipable
from items.item_type import ItemType


class Character:
    def __init__(self):
        self.stats = {"level": 1,  "title": "Wanderer",  "strength": 1,  "experience": 0, "hp": 20}
        self.inventory = Inventory()
        self.equipment = Equipment()

    def _force_equip(self, equipment: Equipable, silent=False):
        self.equipment.equip(equipment, silent)

    def equip(self, equipment_name: string):
        if not self.inventory.can_equip(equipment_name):
            return print ("can't equip this item")

        to_equip = self.inventory.pop(equipment_name)
        unequiped = self.equipment.unequip(to_equip.equipType.type)

        if unequiped:
            self.inventory.add(unequiped)
        self.equipment.equip(to_equip)


    def display_inventory(self):
        self.inventory.display()

    def get_damage(self):
        weapon = self.equipment.get(ItemType.WEAPON)
        if weapon:
            return self.stats['strength'] + weapon.get_damage()
        return self.stats['strength']

    def erode_weapon(self):
        self.equipment.erode(EquipType.type.WEAPON)

    def max_experience(self):
        temp_exp_cap = self.stats["level"]
        exp_till_next_level = temp_exp_cap * temp_exp_cap + 20
        return exp_till_next_level

    def attack(self, enemy: Enemy):
        self.stats["hp"] -= enemy.get_damage()
        if not self.is_alive():
            print(enemy.get_death_message())
            self.die()

    def is_alive(self):
        if self.stats["hp"] <= 0:
            return False
        return True

    def die(self):
        print("\"if only I had not entered this wretched forest\" Regret fills your mind as the light leaves your eyes")
        potato = input("You are dead!")
        quit()


    def experience_gain(self, experience):
        total_exp = self.stats["experience"] + experience
        has_exp_left = True

        while has_exp_left:
            exp_till_next_level = self.max_experience()
            if total_exp < exp_till_next_level:
                self.stats["experience"] += experience
                print("(" + str(experience) + " EXP obtained)")
                has_exp_left = False
            else:
                print("You feel stronger, what a great feeling! And you feel completely Restored!!")
                self.stats["experience"] = 0
                self.stats["level"] += 1
                self.stats["strength"] += random.randrange(1, 3)
                self.stats["hp"] += 10 * self.stats["level"]
                total_exp = experience - exp_till_next_level

    def display_stats(self):
        print("======= Current Stats =======")
        for key in self.stats:
            print(" \t" + key + ": " + str(self.stats[key]))

        print("\n======= Equipment =======")
        print("\tWeapon:  " + str(self.equipment.getName(ItemType.WEAPON)) )
        print("\tShield:  " + str(self.equipment.getName(ItemType.SHIELD)))
        print("\tHead  :  " + str(self.equipment.getName(ItemType.HEAD)))
        print("\tBody  :  " + str(self.equipment.getName(ItemType.BODY)))
        print("\tHands :  " + str(self.equipment.getName(ItemType.HANDS)))
        print("\tLegs  :  " + str(self.equipment.getName(ItemType.LEGS)) + "\n")