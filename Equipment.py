from __future__ import annotations

from typing import List, Optional

from items.equip_type import EquipType
from items.equipable import Equipable
from items.item_type import ItemType


class Equipment:
    def __init__(self):
        self._equipment: List[ItemType, Optional[Equipable]] = {
            ItemType.WEAPON: None,
            ItemType.OFFHAND: None,
            ItemType.SHIELD: None,
            ItemType.HEAD: None,
            ItemType.BODY: None,
            ItemType.LEGS: None,
            ItemType.HANDS: None,
        }

    def unequip(self, item_type: ItemType):
        unequiped = self._equipment[item_type]
        self._equipment[item_type] = None
        return unequiped

    def equip(self, equipment: Equipable, silent=False):
        self._equipment[equipment.equipType.type] = equipment

        if not silent:
            print("Equiped the " + equipment.get_name().lower() + "!")

    def erode(self, item_type: ItemType):
        # @Todo: move erosion to the usage function of the equiable: weapon.attack or armour.defend
        current_equipment = self._equipment[item_type]
        if current_equipment is None:
            return

        current_equipment.durability -= 1

        if current_equipment.durability <= 0:
            self._equipment[item_type] = None

    def getName(self, item_type: ItemType):
        current_equipment = self._equipment[item_type]
        if current_equipment is None:
            if item_type == EquipType.type.WEAPON:
                return 'Fists'
            return ' None'

        return current_equipment.get_name()

    def get(self, item_type: ItemType):
        return self._equipment[item_type]

