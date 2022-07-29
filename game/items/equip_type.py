import string

from items.item_type import ItemType


class EquipType:
    type = ItemType

    def __init__(self, name: string, item_type: ItemType, DEFDMG: int, dur: int):
        self.name = name
        self.itemType = item_type
        self.defDmg = DEFDMG
        self.durability = dur

