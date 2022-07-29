import string
from typing import List

from Table import Table
from items.Item import Item, Equipable, Weapon


class Inventory:

    def __init__(self):
        self.inventory = []

    def display(self):
        # equipabiles = self.get_equips()

        header = ['name', 'damage', 'durability']
        rows = [item.to_row() for item in self.get_weapons()]
        Table([header] + rows, "weapons").print()

        header = ['name', 'defence', 'durability']
        rows = [item.to_row() for item in self.get_equips()]
        Table([header] + rows, "equips").print()

        header = ['name']
        rows = [item.to_row() for item in self.get_misc_items()]
        Table([header] + rows, "misc").print()


    def get_equips(self) -> List[Equipable]:
        return [
            item for item in self.inventory
            if isinstance(item, Equipable) and not isinstance(item, Weapon)
        ]

    def get_weapons(self):
        return [
            item for item in self.inventory
            if isinstance(item, Weapon)
        ]

    def get_misc_items(self):
        return [
            item for item in self.inventory
            if not isinstance(item, Equipable) and not isinstance(item, Weapon)
        ]

    def can_equip(self, name: string):
        equipables = self.get_equips()

        for item in equipables:
            if item.get_name().lower() == name.lower():
                return True
        return False

    def add(self, item: Item):
        self.inventory.append(item)
        print("You put the " + item.get_name().lower() + " in the inventory.")

    def pop(self, itemName: string) -> Equipable:
        value = None
        for item in self.inventory:
            if item.get_name().lower() == itemName.lower():
                value = self.inventory.pop(self.inventory.index(item))

        return value

